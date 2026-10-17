import pytest
from elima_early_warning.models import LearnerIndicators
from elima_early_warning.scoring import assess


def test_low_score():
    result = assess(LearnerIndicators(attendance_rate=1, grade_trend=.2, assignment_completion_rate=1, consecutive_absences=0))
    assert result.level == "low" and result.score == 0


def test_high_score():
    result = assess(LearnerIndicators(attendance_rate=0, grade_trend=-1, assignment_completion_rate=0, consecutive_absences=10))
    assert result.level == "high" and result.score == 1


def test_missing_data_abstains():
    result = assess(LearnerIndicators(attendance_rate=.7))
    assert result.level == "insufficient_data" and result.score is None


def test_3_features_renormalize():
    result = assess(LearnerIndicators(attendance_rate=.8, grade_trend=-.2, consecutive_absences=1))
    assert result.score is not None
    assert result.data_completeness == .75
    assert sum(x.points for x in result.contributions) == pytest.approx(result.score, abs=.0002)


def test_invalid_input_rejected():
    with pytest.raises(ValueError):
        LearnerIndicators(attendance_rate=1.1)
    with pytest.raises(ValueError):
        LearnerIndicators(attendance_rate=.5, student_name="John")
