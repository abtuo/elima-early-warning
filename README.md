# Elima Early Warning Open

[![Tests](https://github.com/OWNER/elima-early-warning-open/actions/workflows/tests.yml/badge.svg)](https://github.com/OWNER/elima-early-warning-open/actions/workflows/tests.yml)

**Transparent educational early-warning baseline | Open source | MIT**

Elima Early Warning Open is an independent, reusable research and demonstration component for examining **potential school disengagement signals** from aggregated educational indicators. The project supports the broader mission of improving educational access and student support in African school systems.

> **Important:** This is a **working software prototype**, not an empirically validated dropout predictor. It implements an explainable heuristic (not trained machine learning), and its score is **not a probability of dropout**. No operational decisions about a child should be based on this software without evidence, safeguards and authorized human review.

## Features
- Four interpretable input indicators with validation
- Explainable composite score and per-indicator contributions
- Abstention when fewer than three observations are provided
- FastAPI endpoint and command-line interface
- Synthetic sample inputs and automated tests
- No dependency on Elima's proprietary SaaS or codebase

## Quick start

Requires Python 3.10+.

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -e '.[dev]'
pytest -q
elima-ew examples/synthetic_learner.json
uvicorn elima_early_warning.api:app --host 127.0.0.1 --port 8000
```

Open `http://127.0.0.1:8000/docs` for interactive documentation. Or run:

```bash
curl -X POST http://127.0.0.1:8000/v1/assess \
  -H 'Content-Type: application/json' \
  -d '{"attendance_rate":0.78,"grade_trend":-0.3,"assignment_completion_rate":0.62,"consecutive_absences":3}'
```

The service uses only aggregated, non-identifying indicators and forbids unexpected fields. It **does not have authentication**; keep it local for demonstration. See [Responsible use](docs/RESPONSIBLE_USE.md).

## How scoring works

An adverse value of 0 is no signal; 1 is the strongest signal *within this artificial scale*. The four signals are lower attendance (35%), negative grade trend (20%), incomplete assignments (25%), and consecutive absences, capped at 10 (20%). The result is a weighted average of observed signals. A minimum of 3 of 4 fields is required. Illustrative thresholds: under 0.35 (low), 0.35–0.6499 (medium), at least 0.65 (high).

These weights, ranges, and thresholds are **demonstration design choices**, not validated educational rules. See [Model card](docs/MODEL_CARD.md).

## Standalone reuse and licensing

The repository can be installed independently and integrated into other educational systems via the documented API. It does not require an Elima subscription. Released under the MIT license: third parties may use, modify and redistribute the open code, including commercially, subject to license terms. The Elima name and logos are not licensed for third-party branding.

## Project documentation
- [Model card](docs/MODEL_CARD.md)
- [Responsible use and safeguarding](docs/RESPONSIBLE_USE.md)
- [Roadmap](docs/ROADMAP.md)
- [Contributing](CONTRIBUTING.md)
- [Security](SECURITY.md)

## About Elima

Elima develops education software for schools, teachers, learners and families in Africa. This open component is intentionally separated from Elima's proprietary platforms, interfaces, commercial workflows and private data.

**Contact:** contact@elima.africa · https://www.elima.africa

## Before publishing to GitHub

Replace the `OWNER` placeholder in the badge above with your GitHub organization or user name. Review the copyright ownership, dependency licenses and repository contents before release.
