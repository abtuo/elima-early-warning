from fastapi.testclient import TestClient
from elima_early_warning.api import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_assess_api():
    response = client.post("/v1/assess", json={"attendance_rate": .85, "grade_trend": -.15, "assignment_completion_rate": .72, "consecutive_absences": 2})
    assert response.status_code == 200
    assert response.json()["model_version"] == "heuristic-v0.1"


def test_forbids_identifiers():
    response = client.post("/v1/assess", json={"student_name": "Example", "attendance_rate": .8})
    assert response.status_code == 422
