import pytest
from starlette.testclient import TestClient
from app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_home_status_code(client):
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline(client):
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_get_complaints_status_code(client):
    response = client.get("/complaints")
    assert response.status_code == 200


def test_get_complaints_contains_seed_text(client):
    response = client.get("/complaints")
    assert "Instructions were unclear" in response.text


def test_post_complaint_redirects(client):
    response = client.post("/complaints", data={"agent_name": "TestBot", "text": "Test complaint"}, follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_in_get(client):
    client.post("/complaints", data={"agent_name": "TestBot", "text": "Test complaint"})
    response = client.get("/complaints")
    assert "TestBot" in response.text
    assert "Test complaint" in response.text