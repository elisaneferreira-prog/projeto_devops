from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_status():
    response = client.get("/")
    assert response.status_code == 200

def test_root_message():
    response = client.get("/")
    assert response.json() == {"message": "Hello World"}

def test_root_not_empty():
    response = client.get("/")
    assert response.json() != {}

def test_root_has_message_key():
    response = client.get("/")
    assert "message" in response.json()

def test_root_message_type():
    response = client.get("/")
    assert isinstance(response.json()["message"], str)
