# Agentia Headless Hackathon — submission form content

Use the same work email used at registration: **sowmya@sowmyatech.in**.
Registered project title: **Agentia CPQ Guardian**.

## Problem statement
Salesforce CPQ developers working with complex product catalogs often face challenges identifying configuration errors, broken dependencies, and potential impacts of product changes before deployment. In telecom environments, a small change to a product attribute or product relationship can affect dependent products and existing configurations. Manual dependency investigation and test selection can be time-consuming and may miss defects. Agentia CPQ Guardian addresses this problem with a local prototype that validates a normalized JSON catalog snapshot, detects missing required products, unknown references, and incompatible combinations, traces declared dependencies, and produces evidence-based findings and suggested regression tests. The current version uses fictional sample data and deterministic rules; live Salesforce/EPC connectivity and verified Agentia runtime integration are not implemented.

## Abstract
Agentia CPQ Guardian is a command-line prototype for earlier detection of configuration defects in telecom B2C CPQ catalogs. It accepts a normalized catalog snapshot and a proposed configuration change as JSON, checks required product relationships, unknown product references, incompatible combinations, and invalid change targets, and produces a structured report with severity, evidence, and suggested next steps. It also demonstrates a path toward focused regression-test recommendations based on declared dependencies. Deterministic rules remain the source of truth so findings are traceable and reviewable. The included fictional scenario models a starter bundle that requires a modem and two mutually incompatible video tiers; the validator flags the missing component and conflict, while a valid scenario can pass. This submission is an offline reference implementation, not a live Salesforce integration. A future phase would connect the validator to a supported Agentia extension workflow and an approved read-only catalog adapter, then evaluate it against anonymized test cases.

## What problem does it solve?
Manual review of complex CPQ bundles and product dependencies can miss required components, unresolved references, and incompatible combinations. Guardian makes a defined set of checks repeatable and emits evidence-based JSON findings for developer review before a change progresses.

## Tools and technologies actually used
- Python 3.10+ (prototype implementation)
- JSON (fictional sample catalog, change request, and report)
- Python standard-library `unittest` (automated tests)
- Git and GitHub (source control / public repository, to be completed by submitter)
- Copado Agentia Headless CLI: intended extension target; integration is not verified in this prototype
- Salesforce CPQ / Industries CPQ domain knowledge informs the sample scenario; no live org/API connection is included
- AI/LLM explanations: planned, not implemented in this package

Do not list TypeScript, live Salesforce REST API, MCP, or AI/LLM as implemented technologies unless you separately implement and verify them.

## Gap / limitations
This prototype currently analyzes normalized fictional JSON input offline. It does not connect to a Salesforce org, retrieve real CPQ/Vlocity/EPC metadata, invoke an LLM, or execute inside an authenticated Agentia runtime. Rules are intentionally limited to the checks described in the README. The next step is to validate a custom command against the current documented Agentia plugin scaffold, and only then add a permissioned, read-only source adapter and optional AI explanation layer.

## Demo video
Record a 3–4 minute screen walkthrough and upload it to a shareable location (for example, an unlisted video link if allowed by the form). Show:
1. The fictional sample data and the invalid change.
2. The validator command and its JSON findings.
3. The valid change and PASS result.
4. The five automated tests passing.
5. A clear statement that Agentia integration and live Salesforce access are not yet implemented.

## Before clicking Submit
- Make the GitHub repository public and confirm it opens in a private/incognito browser.
- Include the README, source, sample data, tests, demo script, slide outline, and MIT license.
- Upload the presentation deck and paste the demo video link if the form requests them.
- Use the exact registered work email above.
- Save a screenshot or confirmation email after submission.
