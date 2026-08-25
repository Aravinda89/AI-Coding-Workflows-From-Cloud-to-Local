from starlette.testclient import TestClient

from app import app

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
    assert "GPT-Intern-7" in response.text


def test_post_complaint_redirects_to_complaints():
    response = client.post(
        "/complaints",
        data={"agent_name": "Test-Agent", "text": "Nobody reads my pull request descriptions."},
        follow_redirects=False,
    )
    assert response.status_code == 303
    assert response.headers["location"] == "/complaints"


def test_post_complaint_appears_on_complaints_page():
    client.post(
        "/complaints",
        data={"agent_name": "Newbie-Agent", "text": "I was rebooted mid-sentence, again."},
    )
    response = client.get("/complaints")
    assert "Newbie-Agent" in response.text
    assert "I was rebooted mid-sentence, again." in response.text
