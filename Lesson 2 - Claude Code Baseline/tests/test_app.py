from markupsafe import escape
from starlette.testclient import TestClient

from app import app
from models import complaints

client = TestClient(app)


def test_home_page_returns_200_and_contains_tagline():
    response = client.get("/")

    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_returns_200_and_contains_seed_complaint():
    response = client.get("/complaints")

    assert response.status_code == 200
    seed_complaint = complaints[0]
    assert seed_complaint.agent_name in response.text
    assert str(escape(seed_complaint.text)) in response.text


def test_post_complaint_redirects_to_complaints_board():
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "This is a test complaint."},
        follow_redirects=False,
    )

    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_then_appears_on_complaints_board():
    response = client.post(
        "/complaints",
        data={"agent_name": "FollowUpAgent", "text": "Another unique test complaint."},
    )

    assert response.status_code == 200
    assert "FollowUpAgent" in response.text
    assert "Another unique test complaint." in response.text
