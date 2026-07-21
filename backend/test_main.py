from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_returns_welcome_message():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to PulseBoard"}


def test_health_check_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    body = response.json()
    assert body["status"] == "ok"
    assert body["service"] == "pulseboard-api"


def test_health_check_response_has_no_extra_fields():
    response = client.get("/health")
    body = response.json()
    assert set(body.keys()) == {"status", "service"}


def test_nonexistent_route_returns_404():
    response = client.get("/this-route-does-not-exist")
    assert response.status_code == 404
