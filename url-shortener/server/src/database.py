"""
Database connection setting module.

Yields:
    DatabaseContext: Database connection context
"""
import os
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from infra.table.url_table import table_registry
from setting import settings

DB_NAME = 'url_service'


class DatabaseContext:
    """
    Database context class
    """

    def __init__(self):
        """
        Initialize database engine.
        """
        root_path = Path(__file__).parent.parent

        db_url = f'{settings.db_interface}:///{root_path}//{settings.db_dir}/{DB_NAME}.db?check_same_thread=False'

        if settings.db_type == "sqlite" and not os.path.exists(f'{root_path}/{settings.db_dir}'):
            os.mkdir(f'{root_path}/{settings.db_dir}')

        engine = create_engine(db_url)

        self.session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)

        Base = table_registry.generate_base()
        Base.metadata.create_all(bind=engine)


database_context = DatabaseContext()


def get_db():
    """
    Get database

    Yields:
        SessionLocal: Local session for database connection
    """
    db = database_context.session_local()
    try:
        yield db
    finally:
        db.close()
