"""Local demonstration API. No authentication: NOT suitable for internet exposure."""
from fastapi import FastAPI
from .models import LearnerIndicators, RiskAssessment
from .scoring import assess

app = FastAPI(title="Elima Early Warning Open", version="0.1.0",
              description="Educational, explainable screening baseline. Not for automated decisions.")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/v1/assess", response_model=RiskAssessment)
def assess_learner(indicators: LearnerIndicators) -> RiskAssessment:
    return assess(indicators)
