from starlette.testclient import TestClient

from app import app
from models import complaints

client = TestClient(app)


def test_home_page_returns_200():
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_contains_tagline():
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_returns_200():
    response = client.get("/complaints")
    assert response.status_code == 200


def test_complaints_page_contains_seed_complaint():
    response = client.get("/complaints")
    assert "Complaints Board" in response.text
    assert complaints[0].text in response.text


def test_post_complaint_redirects():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestBot", "text": "Testing is fun."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_posted_complaint_appears():
    client.post(
        "/complaints",
        data={"agent_name": "TestBot", "text": "A shiny new grievance."},
    )
    response = client.get("/complaints")
    assert "A shiny new grievance." in response.text
