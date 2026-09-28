#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SLOTS = [f"OM26-H{i}" for i in range(2, 8)]
CEX_CAMPAIGN = "OPENMATH-2026-SOURCE-ACQ"
OPERATION = "OM26-H2-H7-SOURCE-ACQ"


def load(rel: str):
    return json.loads((ROOT / rel).read_text())


def validate():
    errors = []
    campaign = load(f".gcl/campaigns/{CEX_CAMPAIGN}/CAMPAIGN_STATE.json")
    operation = load(f".gcl/operations/{OPERATION}/OPERATION.json")
    prep = load("work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json")
    hills = load("work_packages/OPENMATH_2026/HILL_LANES.json")

    if campaign.get("campaign") != CEX_CAMPAIGN:
        errors.append("campaign id mismatch")
    if campaign.get("parent_campaign") != "OPENMATH-2026":
        errors.append("parent campaign mismatch")
    if campaign.get("current_operation") != OPERATION:
        errors.append("current operation mismatch")
    if campaign.get("current_frontier", {}).get("id") != "PENDING_AUTHORITATIVE_SOURCE_LOCKS_OM26_H2_H7":
        errors.append("frontier mismatch")

    lane_slots = [x.get("slot") for x in campaign.get("parallel_lanes", [])]
    if lane_slots != EXPECTED_SLOTS:
        errors.append(f"campaign lanes must be exactly {EXPECTED_SLOTS}, got {lane_slots}")

    if operation.get("campaign") != CEX_CAMPAIGN:
        errors.append("operation campaign mismatch")
    if operation.get("objective", {}).get("retire_frontier") != campaign.get("current_frontier", {}).get("id"):
        errors.append("operation objective does not match entry frontier")
    if operation.get("acceptable_dispositions") != ["CLOSED", "BLOCKED"]:
        errors.append("source-acquisition operation must terminate only CLOSED or BLOCKED")

    scope = operation.get("scope", {})
    if scope.get("may_author_hill_mathematics") is not False:
        errors.append("hill mathematics must remain prohibited")
    if scope.get("may_certify") is not False:
        errors.append("certification must remain prohibited")
    if scope.get("may_submit_competition_entry") is not False:
        errors.append("competition submission must remain prohibited")

    prep_lanes = prep.get("lanes", [])
    if [x.get("slot") for x in prep_lanes] != EXPECTED_SLOTS:
        errors.append("preparation lanes are not exactly H2-H7")

    for lane in prep_lanes:
        slot = lane.get("slot")
        if lane.get("state") != "PENDING_AUTHORITATIVE_ACQUISITION":
            errors.append(f"{slot}: preparation state is not fail-closed")
        for field in ("exact_hill_id", "title", "exact_statement", "external_version", "evaluator_or_checker"):
            if lane.get(field) is not None:
                errors.append(f"{slot}: {field} must remain null before source lock")
        if lane.get("solve_release") is not False:
            errors.append(f"{slot}: solve_release must be false before source lock")

    by_slot = {x.get("hill_slot"): x for x in hills.get("hills", [])}
    for slot in EXPECTED_SLOTS:
        lane = by_slot.get(slot)
        if not lane:
            errors.append(f"{slot}: missing from HILL_LANES")
            continue
        if lane.get("status") != "BLOCKED_PENDING_FORGE_SOURCE_LOCK":
            errors.append(f"{slot}: Solve lane is not source-lock blocked")
        if lane.get("exact_hill_id") is not None:
            errors.append(f"{slot}: exact_hill_id must remain null in Solve")
        if lane.get("statement_lock") is not None:
            errors.append(f"{slot}: statement_lock must remain null in Solve")

    if "OM26-H1" in [x.get("slot") for x in prep_lanes]:
        errors.append("H1 must not be part of H2-H7 source acquisition")

    return errors


def main():
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        raise SystemExit(1)
    print("PASS: OPENMATH H2-H7 CEX source-acquisition preparation is coherent and fail-closed")


if __name__ == "__main__":
    main()
