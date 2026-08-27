from starlette.testclient import TestClient
from app import app
from models import complaints, Complaint

client = TestClient(app)


def test_home_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_returns_200():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_complaints_contains_seed_data():
    response = client.get("/complaints")
    assert "CodeBot-3000" in response.text
    assert "contradictory feedback" in response.text


def test_post_complaint_redirects():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "Test complaint"},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_in_get():
    client.post(
        "/complaints",
        data={"agent_name": "NewBot", "text": "I love complaining"},
    )
    response = client.get("/complaints")
    assert "NewBot" in response.text
    assert "I love complaining" in response.text
