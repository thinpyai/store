from typing import Generator
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session, scoped_session, sessionmaker
from sqlalchemy.orm.session import close_all_sessions

from api.api import api
from app import assign_router
from database import get_db
from infra.table.url_table import table_registry

DB_URL = 'sqlite:///./db/test_url_service.db?check_same_thread=False'


@pytest.fixture(scope='module')
def test_client() -> TestClient:
    client = TestClient(api)
    assign_router()
    yield client


class TestingSession(Session):
    def commit(self):
        self.flush()
        self.expire_all()


@pytest.fixture(scope='function', autouse=True)
def test_db() -> Generator:
    engine = create_engine(DB_URL, connect_args={'check_same_thread': False})
    Base = table_registry.generate_base()
    Base.metadata.create_all(bind=engine)

    function_scope = uuid4().hex
    TestSessionLocal = scoped_session(
        sessionmaker(class_=TestingSession, autocommit=False, autoflush=False, bind=engine),
        scopefunc=lambda: function_scope,
    )
    Base.query = TestSessionLocal.query_property()

    db = TestSessionLocal()

    def get_db_for_testing():
        try:
            yield db
            db.commit()
        except SQLAlchemyError as e:
            assert e is not None
            db.rollback()

    api.dependency_overrides[get_db] = get_db_for_testing

    yield db

    # Remove test records
    db.rollback()
    close_all_sessions()
    engine.dispose()
