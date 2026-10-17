from typing import Literal
from pydantic import BaseModel, Field, ConfigDict


class LearnerIndicators(BaseModel):
    """Aggregated observations only; do not submit names or direct identifiers."""
    model_config = ConfigDict(extra="forbid")
    attendance_rate: float | None = Field(default=None, ge=0, le=1, description="Fraction of attended sessions in observation window")
    grade_trend: float | None = Field(default=None, ge=-1, le=1, description="Normalized change in grades (-1 to 1)")
    assignment_completion_rate: float | None = Field(default=None, ge=0, le=1)
    consecutive_absences: int | None = Field(default=None, ge=0, le=100)


class Contribution(BaseModel):
    indicator: str
    points: float
    explanation: str


class RiskAssessment(BaseModel):
    level: Literal["low", "medium", "high", "insufficient_data"]
    score: float | None = None
    data_completeness: float = Field(ge=0, le=1)
    contributions: list[Contribution]
    next_step: str
    model_version: str = "heuristic-v0.1"
    disclaimer: str = "Research/demo triage aid, not a validated probability or automated decision. Human review required."
