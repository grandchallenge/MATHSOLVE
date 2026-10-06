#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

try:
    from ci.erdos_open_cohort_closure import ROOT, validate_closure
    from ci.erdos_241_replay import build_report
except ModuleNotFoundError:
    from erdos_open_cohort_closure import ROOT, validate_closure
    from erdos_241_replay import build_report

BASE = ROOT / "contributions" / "ERDOS-OPEN-001" / "RECON_TRANCHE_001"
CLOSURE = BASE / "closures" / "ERDOS-241-BLIND-COHORT-001.json"
REPLAY = BASE / "replays" / "ERDOS-241-RA-REPLAY-001.json"
SYNTHESIS = BASE / "synthesis" / "ERDOS-241-RA-SYNTHESIS-001.md"
ADJUDICATION = BASE / "adjudications" / "ERDOS-241-RA-ADJUDICATION-001.json"
SUCCESSOR = ROOT / "work_packages" / "ERDOS_OPEN" / "ERDOS_241_N1_LOCAL_DIFFERENCE_POWER.md"

PIPELINE = [
    "RETURNED",
    "CAPTURED",
    "PROTECTED",
    "BLIND_COHORT_CLOSED",
    "REPLAYED",
    "ADJUDICATED",
    "ADVANCED",
]


def readj(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate_objects(
    closure: dict[str, Any],
    replay: dict[str, Any],
    adjudication: dict[str, Any],
    synthesis_text: str,
    successor_text: str,
) -> list[str]:
    errors: list[str] = []
    errors.extend(f"closure: {x}" for x in validate_closure("241", closure))

    if replay != build_report():
        errors.append("replay artifact differs from deterministic native replay")
    if replay.get("no_seven_element_b3_set_through_64") is not True:
        errors.append("replay does not close the exact N=64 finite boundary")
    if replay.get("expected_minimal_spans_match") is not True:
        errors.append("minimal-span replay mismatch")
    if replay.get("expected_extremizers_match") is not True:
        errors.append("minimal-span extremizer replay mismatch")
    if replay.get("external_sources_used") is not False:
        errors.append("replay external-source boundary inflated")

    checks = {
        "schema": adjudication.get("schema_version") == "1.0.0",
        "record_type": adjudication.get("record_type") == "GCL_ERDOS_OPEN_SYNTHESIS_ADJUDICATION",
        "id": adjudication.get("adjudication_id") == "ERDOS-241-RA-ADJUDICATION-001",
        "campaign": adjudication.get("campaign") == "ERDOS-OPEN-RECON",
        "problem": adjudication.get("problem_id") == 241,
        "cohort": adjudication.get("cohort_id") == "ERDOS-241-BLIND-COHORT-001",
        "pipeline": adjudication.get("pipeline") == PIPELINE,
        "closure_path": adjudication.get("closure") == str(CLOSURE.relative_to(ROOT)).replace("\\", "/"),
        "replay_path": adjudication.get("replay") == str(REPLAY.relative_to(ROOT)).replace("\\", "/"),
        "synthesis_path": adjudication.get("synthesis") == str(SYNTHESIS.relative_to(ROOT)).replace("\\", "/"),
    }
    for name, ok in checks.items():
        if not ok:
            errors.append(f"adjudication identity drift: {name}")

    source = adjudication.get("source_lane")
    if not isinstance(source, dict):
        errors.append("source lane record missing")
    else:
        if source.get("dispatch_id") != "ERDOS-241-S1-IA-001":
            errors.append("source lane identity drift")
        if source.get("protected_at_adjudication") is not False:
            errors.append("source lane incorrectly marked protected")
        if source.get("literature_dependent_promotion_gate_satisfied") is not False:
            errors.append("literature-dependent source gate incorrectly satisfied")

    closure_evidence = {
        item.get("dispatch_id"): item
        for item in closure.get("evidence", [])
        if isinstance(item, dict)
    }
    adjudication_evidence = adjudication.get("evidence")
    if not isinstance(adjudication_evidence, dict):
        errors.append("adjudication evidence map missing")
    else:
        for lane, dispatch in (
            ("R1", "ERDOS-241-R1-IA-001"),
            ("A1", "ERDOS-241-A1-IA-001"),
        ):
            got = adjudication_evidence.get(lane)
            live = closure_evidence.get(dispatch)
            if not isinstance(got, dict) or not isinstance(live, dict):
                errors.append(f"{lane}: evidence binding missing")
                continue
            if got.get("dispatch_id") != dispatch:
                errors.append(f"{lane}: dispatch binding drift")
            if got.get("raw_blob_sha1") != live.get("raw_blob_sha1"):
                errors.append(f"{lane}: raw blob binding drift")
            if got.get("receipt_blob_sha1") != live.get("receipt_blob_sha1"):
                errors.append(f"{lane}: receipt blob binding drift")

    claim_ids = {
        row.get("claim_id")
        for row in adjudication.get("claim_adjudications", [])
        if isinstance(row, dict)
    }
    required_claims = {
        "ERDOS-241-FINITE-F-THROUGH-64",
        "ERDOS-241-MINIMAL-SPAN-EXTREMIZERS-K1-K6",
        "ERDOS-241-DELTA-NO-DOUBLES",
        "ERDOS-241-DISJOINT-DIFFERENCE-SUM",
        "ERDOS-241-B2-DIFFERENCE-UNIQUENESS",
        "ERDOS-241-NAIVE-BRIDGE-ELIMINATIONS",
    }
    if claim_ids != required_claims:
        errors.append("adjudicated claim set drift")

    effects = adjudication.get("effects")
    if not isinstance(effects, dict):
        errors.append("adjudication effects missing")
    else:
        if effects.get("mathematical_correctness_adjudicated_for_listed_internal_claims") is not True:
            errors.append("listed internal claims not marked adjudicated")
        for key in (
            "independent_external_verification",
            "literature_status_effect",
            "source_currentness_effect",
            "parent_erdos_problem_effect",
            "certification_effect",
            "publication_effect",
            "prize_effect",
        ):
            if effects.get(key) is not False:
                errors.append(f"authority inflation: {key}")

    successor = adjudication.get("selected_successor")
    if not isinstance(successor, dict):
        errors.append("successor record missing")
    else:
        if successor.get("id") != "ERDOS-241-N1-LOCAL-DIFFERENCE-POWER":
            errors.append("successor identity drift")
        if successor.get("path") != str(SUCCESSOR.relative_to(ROOT)).replace("\\", "/"):
            errors.append("successor path drift")
        if successor.get("status") != "READY_NATIVE_GCL":
            errors.append("successor state drift")

    for marker in (
        "ERDOS-241-N1-LOCAL-DIFFERENCE-POWER",
        "EXTERNAL_DISPATCH_AUTHORIZED: NO",
        "CANONICAL_PARENT_PROBLEM_EFFECT: NO",
        "CERTIFICATION_AUTHORIZED: NO",
        "LOCAL_CONSTRAINT_BOUND_IMPROVED",
        "LOCAL_CONSTRAINTS_INSUFFICIENT",
    ):
        if marker not in successor_text:
            errors.append(f"successor missing marker: {marker}")

    for marker in (
        "f(N)=6 for 46<=N<=64",
        "Delta(A) intersect 2 Delta(A) is empty",
        "S1 was not protected at closure",
        "Erdos-241-N1-LOCAL-DIFFERENCE-POWER".upper(),
    ):
        if marker.lower() not in synthesis_text.lower():
            errors.append(f"synthesis missing marker: {marker}")

    return errors


def validate() -> list[str]:
    missing = [
        str(path.relative_to(ROOT))
        for path in (CLOSURE, REPLAY, SYNTHESIS, ADJUDICATION, SUCCESSOR)
        if not path.is_file()
    ]
    if missing:
        return [f"missing ERDOS-241 synthesis artifact: {x}" for x in missing]
    return validate_objects(
        readj(CLOSURE),
        readj(REPLAY),
        readj(ADJUDICATION),
        SYNTHESIS.read_text(encoding="utf-8"),
        SUCCESSOR.read_text(encoding="utf-8"),
    )


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: ERDOS-241 R1+A1 closure, replay, adjudication, and successor are coherent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
