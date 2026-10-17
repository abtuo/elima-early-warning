import json
import sys

import pytest

from elima_early_warning.cli import main


def test_cli_assesses_json_file(tmp_path, monkeypatch, capsys):
    input_path = tmp_path / "learner.json"
    input_path.write_text(
        json.dumps(
            {
                "attendance_rate": 0.78,
                "grade_trend": -0.3,
                "assignment_completion_rate": 0.62,
                "consecutive_absences": 3,
            }
        ),
        encoding="utf-8",
    )
    monkeypatch.setattr(sys, "argv", ["elima-ew", str(input_path)])

    main()

    result = json.loads(capsys.readouterr().out)
    assert result["level"] == "low"
    assert result["score"] == 0.292


def test_cli_reports_invalid_json(tmp_path, monkeypatch, capsys):
    input_path = tmp_path / "invalid.json"
    input_path.write_text("not JSON", encoding="utf-8")
    monkeypatch.setattr(sys, "argv", ["elima-ew", str(input_path)])

    with pytest.raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 2
    assert "cannot read valid indicator JSON" in capsys.readouterr().err
