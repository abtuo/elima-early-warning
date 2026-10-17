import argparse
import json
from pathlib import Path

from pydantic import ValidationError

from .models import LearnerIndicators
from .scoring import assess


def main() -> None:
    parser = argparse.ArgumentParser(description="Score aggregated, non-identifying indicators")
    parser.add_argument("input", type=Path, help="JSON file containing aggregated indicators")
    args = parser.parse_args()
    try:
        content = args.input.read_text(encoding="utf-8")
        data = LearnerIndicators.model_validate_json(content)
    except (OSError, UnicodeError, ValidationError) as exc:
        parser.error(f"cannot read valid indicator JSON from {args.input}: {exc}")
    print(json.dumps(assess(data).model_dump(), indent=2))


if __name__ == "__main__":
    main()
