import pytest
from fastapi.testclient import TestClient

from api import api
from app import assign_router


@pytest.fixture(scope='module')
def test_client() -> TestClient:
    client = TestClient(api)
    assign_router()
    yield client
