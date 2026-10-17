# Responsible use and safeguarding

This repository is a **demonstration**, not a validated dropout prediction system. The heuristic score is NOT a probability of dropout. The words low/medium/high refer only to illustrative **screening bands** and must not be shown as a definitive assessment of a child.

## Safeguards
- No automated disciplinary, exclusion, grading, resource-withholding or other high-stakes decision.
- Human educators and safeguarding staff must contextualize any result and offer supportive interventions.
- Never use protected or sensitive traits (health, religion, ethnicity, disability, family income) as inputs.
- Avoid uploading direct identifiers. No real student data appears in this repository.
- Protect any deployed system with authentication, authorization, TLS, audit logging, retention/deletion policies, and role-based access. The demo API contains **no authentication**.
- Underlying data quality can be affected by attendance reporting and unequal access to resources. Investigate disparate error rates across relevant groups using appropriately governed evaluation data.
- Establish a legal basis for processing children's data, parental/guardian communications as applicable, and a child safeguarding process aligned with local regulations.
- Apply privacy-preserving validation, local ethics review, and meaningful consent/notice practices before pilot use.

## Field-readiness checklist
- [ ] Ethics/safeguarding and data-protection review completed
- [ ] Representative local labeled longitudinal dataset acquired under lawful agreement
- [ ] Operational dropout definition, horizon, and measurement procedure specified
- [ ] Baseline model evaluated prospectively and externally across schools
- [ ] Calibration, precision, recall, false-positive/false-negative harms and fairness assessed
- [ ] Human review process designed with educators and families
- [ ] Security controls, access rights, audit and deletion in place
- [ ] Incident response and appeal/correction mechanisms documented
