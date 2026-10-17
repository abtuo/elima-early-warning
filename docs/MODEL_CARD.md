# Model card: heuristic-v0.1

**Status:** unvalidated illustrative baseline; no machine learning model has been trained.

**Purpose:** demonstrate a transparent, auditable screening workflow that may guide discussion with educators; not to predict actual dropout probability or make automated decisions.

**Inputs:** attendance rate [0,1], normalized grade trend [-1,1], assignment completion rate [0,1], consecutive absences [0,100]. At least 3 of 4 indicators are required. No identifiers or sensitive attributes.

**Method:** four fixed weights (0.35, 0.20, 0.25, 0.20). Each observed normalized adverse indicator contributes proportionally, with weights renormalized over observed inputs. Thresholds 0.35 and 0.65 are **arbitrary demonstration thresholds**, not empirically calibrated.

**Outputs:** illustrative low/medium/high screening band, composite score [0,1], non-causal feature contributions and suggested human-review action. Less than 3 inputs yields insufficient_data.

**Evaluation:** unit tests confirm software behavior; **no predictive validity, calibration, fairness or generalization metrics are claimed**. Synthetic records do not establish real-world performance.

**Known limitations:** missingness can bias estimates; attendance is not equivalent to dropout; grades differ across schools; exclusion and socioeconomic barriers may be correlated with input signals; false positives can stigmatize children. Require local evaluation and safeguarding.

**Do not use:** enrollment, sanctions, disciplinary actions, automated allocation, diagnostic statements about children, or unsupervised operational alerts.
