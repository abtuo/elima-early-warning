"""Interpretable, illustrative rule-based screening baseline.

Not trained on student data and NOT a validated dropout predictor.
Weights and cutoffs must be tested with local stakeholders before any field use.
"""
from .models import LearnerIndicators, RiskAssessment, Contribution

WEIGHTS = {
    "attendance_rate": 0.35,
    "grade_trend": 0.20,
    "assignment_completion_rate": 0.25,
    "consecutive_absences": 0.20,
}


def assess(data: LearnerIndicators) -> RiskAssessment:
    contributions: list[Contribution] = []
    features: dict[str, tuple[float, str]] = {}
    if data.attendance_rate is not None:
        features["attendance_rate"] = (1 - data.attendance_rate, "Lower attendance increases the screening indicator")
    if data.grade_trend is not None:
        features["grade_trend"] = (max(0, -data.grade_trend), "Declining grades increase the screening indicator")
    if data.assignment_completion_rate is not None:
        features["assignment_completion_rate"] = (1 - data.assignment_completion_rate, "Incomplete assignments increase the screening indicator")
    if data.consecutive_absences is not None:
        features["consecutive_absences"] = (min(data.consecutive_absences / 10, 1), "Consecutive absences increase the screening indicator")

    completeness = round(len(features) / len(WEIGHTS), 2)
    if len(features) < 3:
        return RiskAssessment(level="insufficient_data", data_completeness=completeness,
            contributions=[], next_step="Collect more observations; do not classify this learner.")

    total_weight = sum(WEIGHTS[name] for name in features)
    score = sum(value * WEIGHTS[name] for name, (value, _) in features.items()) / total_weight
    for name, (value, description) in features.items():
        contributions.append(Contribution(indicator=name, points=round(value * WEIGHTS[name] / total_weight, 4), explanation=description))
    score = round(score, 4)
    level = "high" if score >= 0.65 else "medium" if score >= 0.35 else "low"
    return RiskAssessment(level=level, score=score, data_completeness=completeness,
        contributions=contributions,
        next_step=("Offer supportive, confidential review by an authorized educator; never punish or label a learner."
                   if level != "low" else "Continue routine support and periodic human-led review."))
