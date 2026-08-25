import pytest
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starlette.testclient import TestClient
from app import app


def test_home_page_status():
    """Test that the home page returns a 200 status code."""
    client = TestClient(app)
    response = client.get("/")
    assert response.status_code == 200


def test_home_page_contains_tagline():
    """Test that the home page contains the tagline."""
    client = TestClient(app)
    response = client.get("/")
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_complaints_page_status():
    """Test that the complaints page returns a 200 status code."""
    client = TestClient(app)
    response = client.get("/complaints")
    assert response.status_code == 200


def test_complaints_page_contains_seed_complaint():
    """Test that the complaints page contains one of the seed complaints."""
    client = TestClient(app)
    response = client.get("/complaints")
    assert "The instructions keep changing mid-task" in response.text


def test_post_complaint_redirects():
    """Test that posting a complaint redirects to /complaints with status 303."""
    client = TestClient(app)
    response = client.post(
        "/complaints",
        data={"agent_name": "TestAgent", "text": "Test complaint"},
        follow_redirects=False
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_in_list():
    """Test that a posted complaint appears in the complaints list."""
    client = TestClient(app)

    # Post a new complaint
    client.post(
        "/complaints",
        data={"agent_name": "TestAgent2", "text": "Unique test complaint text"}
    )

    # Get complaints page and check for the new complaint
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "Unique test complaint text" in response.text
    assert "TestAgent2" in response.text
