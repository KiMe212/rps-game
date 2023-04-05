import pytest

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


@pytest.fixture()
def test_client():
    clin = client.get
    return clin
