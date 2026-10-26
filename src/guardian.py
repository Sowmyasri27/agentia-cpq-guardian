#!/usr/bin/env python3
"""Offline reference rule engine for Agentia CPQ Guardian.

This is a minimal, deterministic prototype. It does not connect to Salesforce.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        value = json.load(f)
    if not isinstance(value, dict):
        raise ValueError(f"{path}: top-level JSON value must be an object")
    return value


def validate(catalog: dict[str, Any], change: dict[str, Any]) -> dict[str, Any]:
    products = catalog.get("products", [])
    if not isinstance(products, list):
        raise ValueError("catalog.products must be a list")
    by_id = {p.get("id"): p for p in products if isinstance(p, dict) and p.get("id")}
    findings: list[dict[str, Any]] = []

    def add(rule_id: str, severity: str, message: str, product_ids: list[str], evidence: dict[str, Any], next_step: str) -> None:
        findings.append({
            "rule_id": rule_id,
            "severity": severity,
            "message": message,
            "product_ids": product_ids,
            "evidence": evidence,
            "suggested_next_step": next_step,
        })

    target = change.get("target_bundle_id")
    proposed = change.get("proposed_product_ids", [])
    if not isinstance(proposed, list):
        raise ValueError("change.proposed_product_ids must be a list")
    if target not in by_id:
        add(
            "UNKNOWN_TARGET_BUNDLE", "critical",
            f"Target bundle '{target}' does not exist in the catalog.",
            [str(target)], {"target_bundle_id": target},
            "Check the change request and use a valid bundle ID."
        )
        return _report(findings, target, proposed)

    for pid in proposed:
        if pid not in by_id:
            add(
                "UNKNOWN_PRODUCT_REFERENCE", "high",
                f"Proposed product '{pid}' is not present in the catalog.",
                [str(pid)], {"referenced_product_id": pid},
                "Correct the product ID or refresh the catalog snapshot."
            )

    target_product = by_id[target]
    required = target_product.get("requires", [])
    present = set(proposed)
    for req in required:
        if req not in present:
            add(
                "MISSING_REQUIRED_PRODUCT", "high",
                f"Bundle '{target}' requires '{req}', but it is absent from the proposed configuration.",
                [str(target), str(req)],
                {"bundle_id": target, "required_product_id": req, "proposed_product_ids": proposed},
                f"Add '{req}' if the bundle is intended to be valid, or review the requirement with the catalog owner."
            )

    for pid in proposed:
        product = by_id.get(pid)
        if not product:
            continue
        for incompatible in product.get("incompatible_with", []):
            if incompatible in present and str(pid) < str(incompatible):
                add(
                    "INCOMPATIBLE_PRODUCTS", "high",
                    f"Products '{pid}' and '{incompatible}' cannot be selected together.",
                    [str(pid), str(incompatible)],
                    {"product_a": pid, "product_b": incompatible},
                    "Remove one product or review the incompatibility rule with the product owner."
                )

    return _report(findings, target, proposed)


def _report(findings: list[dict[str, Any]], target: Any, proposed: list[Any]) -> dict[str, Any]:
    order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    findings.sort(key=lambda f: (order.get(f["severity"], 99), f["rule_id"], f["product_ids"]))
    return {
        "tool": "Agentia CPQ Guardian",
        "report_version": "0.1",
        "mode": "offline_reference_prototype",
        "target_bundle_id": target,
        "proposed_product_ids": proposed,
        "finding_count": len(findings),
        "status": "FAIL" if any(f["severity"] in {"critical", "high"} for f in findings) else "PASS",
        "findings": findings,
        "disclaimer": "Advisory prototype report. Validate findings and recommendations with a qualified catalog owner before release."
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a proposed telecom CPQ configuration.")
    parser.add_argument("--catalog", required=True, help="Path to catalog JSON")
    parser.add_argument("--change", required=True, help="Path to proposed change JSON")
    parser.add_argument("--output", help="Optional path to write report JSON")
    args = parser.parse_args()
    report = validate(load_json(args.catalog), load_json(args.change))
    rendered = json.dumps(report, indent=2)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    print(rendered)


if __name__ == "__main__":
    main()
