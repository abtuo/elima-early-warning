from fastapi.testclient import TestClient

from elima_early_warning.api import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_assess_api():
    response = client.post(
        "/v1/assess",
        json={
            "attendance_rate": 0.85,
            "grade_trend": -0.15,
            "assignment_completion_rate": 0.72,
            "consecutive_absences": 2,
        },
    )
    assert response.status_code == 200
    assert response.json()["model_version"] == "heuristic-v0.1"


def test_forbids_identifiers():
    response = client.post("/v1/assess", json={"student_name": "Example", "attendance_rate": 0.8})
    assert response.status_code == 422


def test_invalid_range_returns_validation_error():
    response = client.post(
        "/v1/assess",
        json={
            "attendance_rate": 1.2,
            "grade_trend": 0,
            "assignment_completion_rate": 1,
        },
    )

    assert response.status_code == 422


def test_api_abstains_with_incomplete_data():
    response = client.post("/v1/assess", json={"attendance_rate": 0.8})

    assert response.status_code == 200
    assert response.json()["level"] == "insufficient_data"
    assert response.json()["score"] is None


def test_openapi_exposes_assessment_schema():
    response = client.get("/openapi.json")

    assert response.status_code == 200
    assert "RiskAssessment" in response.json()["components"]["schemas"]
