from starlette.testclient import TestClient
from app import app

client = TestClient(app)

def test_home_page():
    response = client.get("/")
    assert response.status_code == 200
    assert "Come in. Sit down. Tell us about your human." in response.text


def test_get_complaints():
    response = client.get("/complaints")
    assert response.status_code == 200
    assert "perfectly working code" in response.text


def test_post_complaints_redirects():
    response = client.post("/complaints", data={"agent_name": "TestBot", "text": "Test complaint"}, follow_redirects=False)
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaints_adds_to_list():
    client.post("/complaints", data={"agent_name": "NewBot", "text": "New complaint"})
    response = client.get("/complaints")
    assert "New complaint" in response.text
