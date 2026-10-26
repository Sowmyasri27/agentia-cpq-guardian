# Presentation Outline — Agentia CPQ Guardian
Suggested length: 6–8 minutes, 7 slides. Use screenshots from your actual run; do not imply an Agentia integration that is not implemented.

## Slide 1 — Title and value proposition (30 sec)
- Agentia CPQ Guardian
- AI-assisted validation for telecom B2C CPQ configuration changes
- One-liner: Catch catalog relationship defects before they become quote/order issues.
- Presenter and hackathon name.

## Slide 2 — Problem (60 sec)
- Telecom product catalogs have bundles, required components, and incompatible add-ons.
- Manual review is inconsistent and late defects cause rework.
- Teams need evidence-based findings that developers and product owners can act on.
- Use one fictional example: a bundle is missing its required modem and includes mutually exclusive video tiers.

## Slide 3 — Solution and user journey (60 sec)
- Load normalized catalog snapshot + proposed change.
- Run deterministic rules.
- Prioritize findings and attach rule evidence.
- Optional agent layer explains findings and drafts remediation/test cases.
- Human reviews before release.

## Slide 4 — Architecture (60 sec)
- Input JSON / future Salesforce catalog adapter
- Validation engine
- Finding and severity model
- Optional Agentia/LLM orchestration layer
- JSON report / CI gate / reviewer
- Clearly mark the adapter and agent layer as planned if not built.

## Slide 5 — Live demo (2 min)
- Run the deliberately flawed sample.
- Show missing required product and incompatible products.
- Open the JSON report and trace each finding to a rule.
- Run the valid sample (or modify the request) to show PASS.
- Run the automated tests.

## Slide 6 — Trust, safety, and evaluation (60 sec)
- Rule engine is the source of truth.
- AI suggestions are advisory and human-reviewed.
- No production writes; fictional data only.
- Evaluation: seeded-defect detection, precision, runtime, reviewer usefulness.

## Slide 7 — Impact and next steps (45 sec)
- Potential benefits: earlier defect detection, faster review, repeatable regression tests.
- Next: actual supported Agentia integration, Salesforce catalog adapter, more rule types, CI workflow.
- End with a measurable claim only if measured during the demo.
