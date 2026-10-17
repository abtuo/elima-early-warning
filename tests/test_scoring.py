import pytest
from pydantic import ValidationError

from elima_early_warning.models import LearnerIndicators
from elima_early_warning.scoring import assess


def test_low_score():
    result = assess(
        LearnerIndicators(
            attendance_rate=1, grade_trend=0.2, assignment_completion_rate=1, consecutive_absences=0
        )
    )
    assert result.level == "low" and result.score == 0


def test_high_score():
    result = assess(
        LearnerIndicators(
            attendance_rate=0, grade_trend=-1, assignment_completion_rate=0, consecutive_absences=10
        )
    )
    assert result.level == "high" and result.score == 1


def test_missing_data_abstains():
    result = assess(LearnerIndicators(attendance_rate=0.7))
    assert result.level == "insufficient_data" and result.score is None


def test_3_features_renormalize():
    result = assess(
        LearnerIndicators(attendance_rate=0.8, grade_trend=-0.2, consecutive_absences=1)
    )
    assert result.score is not None
    assert result.data_completeness == 0.75
    assert sum(x.points for x in result.contributions) == pytest.approx(result.score, abs=0.0002)


def test_invalid_input_rejected():
    with pytest.raises(ValidationError):
        LearnerIndicators(attendance_rate=1.1)
    with pytest.raises(ValidationError):
        LearnerIndicators(attendance_rate=0.5, student_name="John")


@pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
def test_non_finite_input_rejected(value):
    with pytest.raises(ValidationError):
        LearnerIndicators(attendance_rate=value)


def test_exact_thresholds_have_documented_levels():
    medium = assess(
        LearnerIndicators(
            attendance_rate=0,
            grade_trend=0,
            assignment_completion_rate=1,
            consecutive_absences=0,
        )
    )
    high = assess(
        LearnerIndicators(
            attendance_rate=0,
            grade_trend=-0.25,
            assignment_completion_rate=0,
            consecutive_absences=0,
        )
    )

    assert medium.score == 0.35
    assert medium.level == "medium"
    assert high.score == 0.65
    assert high.level == "high"


def test_consecutive_absence_signal_is_capped_at_ten():
    at_cap = assess(
        LearnerIndicators(
            attendance_rate=1,
            grade_trend=0,
            assignment_completion_rate=1,
            consecutive_absences=10,
        )
    )
    above_cap = assess(
        LearnerIndicators(
            attendance_rate=1,
            grade_trend=0,
            assignment_completion_rate=1,
            consecutive_absences=100,
        )
    )

    assert at_cap.score == above_cap.score == 0.2
    assert at_cap.contributions == above_cap.contributions
