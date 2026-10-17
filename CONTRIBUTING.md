# Contributing

Contributions that improve safety, accessibility, tests, documentation, and educational
relevance are welcome.

## Before opening an issue

- Search existing issues before creating a new one.
- Do not include real learner records, direct identifiers, secrets, or confidential school
  information.
- Report security vulnerabilities privately as described in [SECURITY.md](SECURITY.md).

## Development setup

Create and activate a Python 3.10 or newer virtual environment, then run:

```bash
python -m pip install -e ".[dev]"
ruff check .
ruff format --check .
pytest -q
```

## Pull requests

Keep changes focused and explain their motivation. Add or update tests for behavioral
changes. Changes to scoring weights, transformations, or thresholds must also update the
model card and clearly state their evidence and limitations.

Use only synthetic data in tests, examples, issues, and pull requests. Do not describe a
heuristic score as a dropout probability or claim performance that has not been measured.

Contributions are made under the repository's MIT License. By contributing, you confirm
that you have the right to submit the work.
