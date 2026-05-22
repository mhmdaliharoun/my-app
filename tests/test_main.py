import pytest
from app.main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_hello(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"

def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200