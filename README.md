# Agentia CPQ Guardian
**Copado Agentia™ Headless Virtual Hackathon — Submission Package**

> **Project status:** Prototype concept and runnable reference implementation scaffold. Validate the implementation against the hackathon's current rules and your actual Copado/Agentia environment before submission. Do not claim production Salesforce integration unless you implement and demonstrate it.

## 1. One-line pitch
Agentia CPQ Guardian is an AI-assisted quality gate for Salesforce Industries CPQ / Vlocity telecom B2C product configuration. It checks product relationships and configuration rules, explains detected issues in plain language, prioritizes risks, and proposes actionable remediation and regression tests.

## 2. Problem
Telecom B2C catalogs contain product bundles, required components, incompatibilities, eligibility conditions, and dependencies that can interact in surprising ways. Manual review and late discovery can lead to invalid offers, failed cart validation, order fallout, rework, and slower releases. Teams need a repeatable way to review configuration changes before they reach customers.

## 3. Proposed solution
Guardian accepts a normalized catalog/configuration snapshot and a change request, runs deterministic checks, then uses an LLM/agent layer (when configured) to explain findings and draft remediation suggestions and test cases. Deterministic rules remain the source of truth; generated recommendations must be reviewed by a human.

### Core workflow
1. Load a JSON catalog snapshot and a proposed change.
2. Validate required relationships, unknown references, and incompatible product pairs.
3. Rank findings by severity and provide evidence (rule ID and affected product IDs).
4. Generate remediation suggestions and regression test ideas.
5. Export a JSON report suitable for CI review or a human approval gate.

## 4. Intended users
- Salesforce Industries CPQ / Vlocity developers
- Product catalog and CPQ analysts
- Telecom order management and release teams
- QA engineers validating quote-to-order journeys

## 5. MVP scope
**Included**
- Local JSON input; no credentials required
- Deterministic validation rules
- Severity-based findings
- JSON report output
- Sample telecom catalog and test cases
- Optional agent/LLM explanation layer as a future integration point

**Not claimed in this scaffold**
- Live Salesforce org connectivity
- Direct writes to Product2, Vlocity catalog objects, or OmniStudio metadata
- Autonomous production changes
- Verified Copado Agentia API integration
- Guaranteed detection of every catalog or runtime issue

## 6. Quick start
Requires Python 3.10+.

```bash
python src/guardian.py --catalog sample_data/catalog.json --change sample_data/change_request.json --output report.json
python src/guardian.py --catalog sample_data/catalog.json --change sample_data/change_request_valid.json --output valid-report.json
python -m unittest discover -s tests -v
```

Expected: a JSON report with findings for the deliberately flawed sample change request. The command is offline and does not require secrets.

## 7. Architecture
```text
Catalog snapshot + change request
              |
              v
      Input/schema validation
              |
              v
     Deterministic rule engine
   - missing required products
   - unknown product references
   - incompatible combinations
   - invalid change targets
              |
              v
       Severity + evidence
              |
              v
  Optional Agent/LLM explanation layer
  (summarize; suggest; draft tests)
              |
              v
      JSON report + human review
```

## 8. Safety and trust
- Deterministic rules produce the findings; the LLM must not silently invent rule outcomes.
- Recommendations are advisory and require review.
- No production writes are made.
- Sample data is fictional and contains no customer information.
- Never commit credentials, customer data, or real catalog exports to a public repository.
- Treat generated explanations as untrusted until verified against the rule evidence.

## 9. Repository layout
```text
.
├── README.md
├── src/guardian.py
├── sample_data/catalog.json
├── sample_data/change_request.json
├── tests/test_guardian.py
├── presentation/slide_outline.md
├── demo/demo_script.md
└── SUBMISSION_CHECKLIST.md
```

## 10. Example output
The sample change adds `PREMIUM_VIDEO` to `HOME_STARTER`. The catalog requires `BROADBAND_MODEM`, but the proposed bundle omits it, and `PREMIUM_VIDEO` conflicts with `BASIC_VIDEO`. Guardian should report:
- `MISSING_REQUIRED_PRODUCT` (high)
- `INCOMPATIBLE_PRODUCTS` (high)
The report also includes product IDs, evidence, and a suggested next step.

## 11. Evaluation plan
Measure:
- Rule precision on a manually labeled test set
- Detection rate for intentionally seeded defects
- Runtime on catalogs of increasing size
- Reviewer usefulness of explanations and suggested tests
- Whether every finding is traceable to deterministic evidence

## 12. Demo and submission checklist
See `demo/demo_script.md`, `presentation/slide_outline.md`, and `SUBMISSION_CHECKLIST.md`.

## 13. Honest claims for the presentation
Say “prototype,” “reference implementation,” and “designed to integrate” until the live agent integration has been built and demonstrated. Only claim successful Agentia/Copado integration if you can show it running in the actual supported environment and can explain the integration path.
