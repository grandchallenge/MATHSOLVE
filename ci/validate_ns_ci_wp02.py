#!/usr/bin/env python3
"""Validate the structural and trust-boundary contracts of NS-CI-WP02."""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
LEDGER_PATH = ROOT / "work_packages" / "ns_ci_wp02_theorem_ledger.yaml"

EXPECTED_THEOREM_IDS = {f"CR-{index:03d}" for index in range(12)}
EXPECTED_SOURCE_IDS = {
    "NS-CI-SRC-CLAY-FEFFERMAN",
    "NS-CI-SRC-LERAY-1934",
    "NS-CI-SRC-OZANSKI-POOLEY",
    "NS-CI-SRC-PRODI-1959",
    "NS-CI-SRC-SERRIN-1962",
    "NS-CI-SRC-LADYZHENSKAYA-1967",
    "NS-CI-SRC-OPERATIONAL-LPS-2024",
}


class ValidationError(ValueError):
    pass


def load_ledger() -> dict[str, Any]:
    with LEDGER_PATH.open("r", encoding="utf-8") as handle:
        payload = yaml.safe_load(handle)
    if not isinstance(payload, dict):
        raise ValidationError("ledger root must be a mapping")
    return payload


def validate(payload: dict[str, Any]) -> None:
    if payload.get("campaign_id") != "NS-CI-001":
        raise ValidationError("unexpected campaign_id")
    if payload.get("work_package_id") != "NS-CI-WP02":
        raise ValidationError("unexpected work_package_id")

    boundary = str(payload.get("claim_boundary", "")).lower()
    for phrase in ("does not", "universal critical integrability", "global regularity"):
        if phrase not in boundary:
            raise ValidationError(f"claim boundary must contain {phrase!r}")

    sources = payload.get("sources", {})
    required_source_ids = set(sources.get("required_source_ids", []))
    if required_source_ids != EXPECTED_SOURCE_IDS:
        missing = EXPECTED_SOURCE_IDS - required_source_ids
        extra = required_source_ids - EXPECTED_SOURCE_IDS
        raise ValidationError(f"source-id contract mismatch; missing={sorted(missing)}, extra={sorted(extra)}")

    entries = payload.get("entries")
    if not isinstance(entries, list):
        raise ValidationError("entries must be a list")

    ids = [entry.get("theorem_id") for entry in entries]
    if len(ids) != len(set(ids)):
        raise ValidationError("theorem IDs must be unique")
    if set(ids) != EXPECTED_THEOREM_IDS:
        raise ValidationError(f"theorem-id set mismatch: {sorted(set(ids))}")

    by_id = {entry["theorem_id"]: entry for entry in entries}

    cr004 = by_id["CR-004"]
    if "L4(0,T;L6(R3))" not in " ".join(cr004.get("hypotheses", [])):
        raise ValidationError("CR-004 must expose the time-4 space-6 hypothesis")
    if cr004.get("status") != "OPERATIONAL_STATEMENT_AUDITED":
        raise ValidationError("CR-004 must remain an audited operational statement")

    cr005 = by_id["CR-005"]
    conclusion_005 = str(cr005.get("conclusion", ""))
    for token in ("nu^(-3)", "norm_L6(u)^4", "norm_L2(gradient u)^2"):
        if token not in conclusion_005:
            raise ValidationError(f"CR-005 conclusion is missing {token}")
    if "Not an unconditional Leray-Hopf estimate." not in cr005.get("prohibited_overstatement", []):
        raise ValidationError("CR-005 must preserve its strong-level test boundary")

    cr006 = by_id["CR-006"]
    conclusion_006 = str(cr006.get("conclusion", ""))
    differential_006 = str(cr006.get("differential_form", ""))
    if "integrated inequality" not in conclusion_006:
        raise ValidationError("CR-006 must expose the rigorous integrated weak-strong inequality")
    for hypothesis in (
        "weak energy inequality for v",
        "strong energy equality for u",
        "admissible time regularization and cross testing",
    ):
        if hypothesis not in cr006.get("hypotheses", []):
            raise ValidationError(f"CR-006 is missing rigorous-route hypothesis {hypothesis!r}")
    for token in ("nu^(-3)", "norm_L6(u)^4", "norm_L2(w)^2"):
        if token not in differential_006:
            raise ValidationError(f"CR-006 differential form is missing {token}")
    prohibited_006 = " ".join(cr006.get("prohibited_overstatement", [])).lower()
    for phrase in ("formal smooth-pair equality", "unconditional weak-solution identity"):
        if phrase not in prohibited_006:
            raise ValidationError(f"CR-006 must prohibit {phrase!r}")

    cr009 = by_id["CR-009"]
    if cr009.get("role") != "one_way_bridge" or cr009.get("status") != "CHECKED_ONE_WAY_BRIDGE":
        raise ValidationError("CR-009 must remain a checked one-way bridge")
    if not any("Do not call this bidirectional equivalence" in item for item in cr009.get("prohibited_overstatement", [])):
        raise ValidationError("CR-009 must explicitly prohibit equivalence wording")

    cr010 = by_id["CR-010"]
    if cr010.get("status") != "PENDING" or cr010.get("role") != "pending_bridge":
        raise ValidationError("CR-010 must remain a pending reverse bridge")

    cr011 = by_id["CR-011"]
    if cr011.get("status") != "CHECKED_RESTRICTION":
        raise ValidationError("CR-011 must preserve compact support as a restricted lane")

    used_source_ids: set[str] = set()
    for entry in entries:
        source_ids = entry.get("source_ids", [])
        if not isinstance(source_ids, list):
            raise ValidationError(f"{entry['theorem_id']}: source_ids must be a list")
        unknown = set(source_ids) - EXPECTED_SOURCE_IDS
        if unknown:
            raise ValidationError(f"{entry['theorem_id']}: unknown source IDs {sorted(unknown)}")
        used_source_ids.update(source_ids)

        if not entry.get("title") or not entry.get("role") or not entry.get("status"):
            raise ValidationError(f"{entry['theorem_id']}: missing title, role, or status")
        if "prohibited_overstatement" not in entry:
            raise ValidationError(f"{entry['theorem_id']}: missing prohibited_overstatement")
        if "unresolved_debt" not in entry:
            raise ValidationError(f"{entry['theorem_id']}: missing unresolved_debt")

    unused = EXPECTED_SOURCE_IDS - used_source_ids
    if unused:
        raise ValidationError(f"required source IDs are never used: {sorted(unused)}")


def main() -> int:
    try:
        validate(load_ledger())
    except (OSError, yaml.YAMLError, ValidationError) as exc:
        print(f"NS-CI-WP02 validation failed: {exc}", file=sys.stderr)
        return 1
    print("NS-CI-WP02 theorem ledger validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
