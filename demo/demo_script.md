# Demo Script — Agentia CPQ Guardian
Target runtime: 3–4 minutes. Keep the terminal and sample files ready before recording.

## Opening (20 sec)
“Telecom B2C product catalogs have dependencies and exclusions. A small catalog error can break a quote or create order fallout. Agentia CPQ Guardian is a prototype that checks a proposed configuration and returns evidence-based findings.”

## Step 1 — Explain sample (20 sec)
“This is fictional sample data. HOME_STARTER requires BROADBAND_MODEM. BASIC_VIDEO and PREMIUM_VIDEO are mutually incompatible. The change intentionally omits the modem and selects both video tiers.”

## Step 2 — Run validator (30 sec)
From the repository root:
```bash
python src/guardian.py --catalog sample_data/catalog.json --change sample_data/change_request.json --output report.json
```
Point out `status: FAIL`, `finding_count`, the rule IDs, severity, evidence, and suggested next steps.

## Step 3 — Explain traceability (30 sec)
“The findings are produced by deterministic rules. Each one names the rule and the products involved. An optional agent layer can turn this evidence into a clearer explanation and draft regression tests, but it should not invent or override findings.”

## Step 4 — Show a passing case (30 sec)
Create `sample_data/change_request_valid.json` with:
```json
{
  "change_id": "CHG-DEMO-002",
  "description": "Valid starter bundle with modem and voice add-on",
  "target_bundle_id": "HOME_STARTER",
  "proposed_product_ids": ["HOME_STARTER", "BROADBAND_MODEM", "VOICE_ADDON"]
}
```
Run:
```bash
python src/guardian.py --catalog sample_data/catalog.json --change sample_data/change_request_valid.json
```
Point out `status: PASS` and zero findings.

## Step 5 — Run tests (30 sec)
```bash
python -m unittest discover -s tests -v
```
Show that tests cover missing requirements, incompatible products, unknown products, a valid configuration, and an unknown target.

## Closing (20 sec)
“The current deliverable is an offline reference prototype. The next milestone is to connect it to the supported Agentia runtime and a read-only Salesforce catalog adapter, then evaluate it on an approved, anonymized test set. No live Salesforce writes are performed.”

## Recording checklist
- Hide credentials, personal information, and unrelated browser tabs.
- Use only the included fictional data.
- Capture the full command and result.
- Do not claim Copado/Agentia API connectivity unless it is genuinely implemented and shown.
