from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_flight_search():
    r = client.post("/flights/search", json={"origin": "DOH", "destination": "JFK"})
    assert r.status_code == 200
    assert r.json()["count"] >= 1


def test_assist_without_openai_key():
    r = client.post(
        "/assist",
        json={
            "question": "What is the baggage allowance?",
            "passenger_name": "Test Passenger",
        },
    )
    assert r.status_code == 200
    assert len(r.json()["sources"]) >= 1


def test_disruption():
    r = client.post(
        "/disruption",
        json={
            "flight_number": "QR739",
            "issue": "Delay may affect passenger connection",
        },
    )
    assert r.status_code == 200
    assert r.json()["flight_found"] is True


def test_evaluation():
    r = client.post("/evaluate")
    assert r.status_code == 200
    assert r.json()["passed"] == r.json()["total"]
