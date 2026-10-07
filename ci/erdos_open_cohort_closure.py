#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

try:
    from ci.erdos_open_semantic_gate import (
        effective_blockers,
        merge_blockers,
        required_source_dispatches,
    )
except ModuleNotFoundError:
    from erdos_open_semantic_gate import (
        effective_blockers,
        merge_blockers,
        required_source_dispatches,
    )

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions" / "ERDOS-OPEN-001" / "RECON_TRANCHE_001"
PROBLEMS = ["593", "595", "241", "470", "1052", "99", "101", "138"]
SHA40 = re.compile(r"^[0-9a-f]{40}$")
DATE = re.compile(r"^20\d\d-\d\d-\d\d$")


def readj(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def lane_dispatch(problem: str, lane: str) -> str:
    return f"ERDOS-{problem}-{lane}-IA-001"


def lane_receipt(problem: str, lane: str) -> dict[str, Any] | None:
    did = lane_dispatch(problem, lane)
    directory = BASE / "receipts" / did
    if not directory.is_dir():
        return None
    paths = sorted(directory.glob("github-comment-*.json"))
    if len(paths) != 1:
        raise ValueError(f"{did}: expected exactly one protected receipt, found {len(paths)}")
    path = paths[0]
    receipt = readj(path)
    raw_rel = receipt.get("raw_artifact_path")
    if not isinstance(raw_rel, str):
        raise ValueError(f"{did}: receipt raw_artifact_path missing")
    raw = ROOT / raw_rel
    if not raw.is_file():
        raise ValueError(f"{did}: protected raw artifact missing")
    raw_text = raw.read_text(encoding="utf-8")
    if hashlib.sha256(raw_text.encode("utf-8")).hexdigest() != receipt.get("raw_sha256"):
        raise ValueError(f"{did}: raw sha256 mismatch")
    checks = {
        "dispatch_id": receipt.get("dispatch_id") == did,
        "blind_cohort_id": receipt.get("blind_cohort_id") == f"ERDOS-{problem}-BLIND-COHORT-001",
        "schema_result": receipt.get("schema_result") == "valid",
        "freshness": receipt.get("freshness") == "current_for_dispatch",
        "handling_state": receipt.get("handling_state") == "received_unadjudicated",
        "canonical_claim_effect": receipt.get("canonical_claim_effect") is False,
        "mathematical_correctness_adjudicated": receipt.get("mathematical_correctness_adjudicated") is False,
        "independence_strength_adjudicated": receipt.get("independence_strength_adjudicated") is False,
        "visibility_phase": receipt.get("visibility_phase") == "BLIND_COLLECTION",
        "sibling_use_policy": receipt.get("sibling_use_policy") == "FORBIDDEN",
    }
    failed = sorted(k for k, ok in checks.items() if not ok)
    if failed:
        raise ValueError(f"{did}: protected receipt invalid: {', '.join(failed)}")
    return {
        "lane": lane,
        "dispatch_id": did,
        "issue_number": receipt.get("github_issue_number"),
        "github_comment_id": receipt.get("github_comment_id"),
        "disposition_declared": receipt.get("disposition_declared"),
        "raw_artifact_path": raw_rel,
        "raw_blob_sha1": blob_sha1(raw),
        "raw_sha256": receipt.get("raw_sha256"),
        "receipt_path": str(path.relative_to(ROOT)).replace("\\", "/"),
        "receipt_blob_sha1": blob_sha1(path),
        "schema_result": "valid",
        "freshness": "current_for_dispatch",
        "handling_state": "received_unadjudicated",
        "canonical_claim_effect": False,
        "semantic_blockers": effective_blockers(receipt, ROOT),
    }


def evidence_binding_matches(
    protected_item: dict[str, Any] | None,
    live_item: dict[str, Any] | None,
) -> bool:
    if protected_item == live_item:
        return True
    if not isinstance(protected_item, dict) or not isinstance(live_item, dict):
        return False
    comparable = dict(live_item)
    if "semantic_blockers" not in protected_item and not comparable.get("semantic_blockers"):
        comparable.pop("semantic_blockers", None)
    return protected_item == comparable


def build_closure(problem: str, protected_commit: str, closure_date: str) -> dict[str, Any]:
    if problem not in PROBLEMS:
        raise ValueError(f"unsupported ERDOS problem: {problem}")
    if not SHA40.fullmatch(protected_commit):
        raise ValueError("protected evidence commit must be a SHA-1")
    if not DATE.fullmatch(closure_date):
        raise ValueError("closure date must be YYYY-MM-DD")

    r = lane_receipt(problem, "R1")
    a = lane_receipt(problem, "A1")
    if r is None or a is None:
        raise ValueError(f"ERDOS-{problem}: R1+A1 protected minimum not satisfied")

    semantic_blockers = merge_blockers(
        r.get("semantic_blockers", []),
        a.get("semantic_blockers", []),
    )
    semantic_gate_dispatches = required_source_dispatches(semantic_blockers)
    expected_source_dispatch = lane_dispatch(problem, "S1")
    if semantic_gate_dispatches and semantic_gate_dispatches != [expected_source_dispatch]:
        raise ValueError(
            f"ERDOS-{problem}: semantic blocker points outside the matching S1 lane"
        )

    s = lane_receipt(problem, "S1")
    semantic_source_audit_discharged = not semantic_gate_dispatches
    if semantic_gate_dispatches:
        if s is None:
            raise ValueError(
                f"ERDOS-{problem}: semantic source gate requires protected return "
                f"{expected_source_dispatch}"
            )
        if s.get("disposition_declared") == "EXACT_BLOCKER":
            raise ValueError(
                f"ERDOS-{problem}: source-audit return is itself blocked; "
                "semantic source gate remains open"
            )
        semantic_source_audit_discharged = True

    required_synthesis_lanes = ["R1", "A1"]
    if semantic_gate_dispatches:
        required_synthesis_lanes.append("S1")

    cohort_path = BASE / "cohorts" / f"ERDOS-{problem}-BLIND-COHORT-001.json"
    cohort = readj(cohort_path)
    if cohort.get("state") != "OPEN_AWAITING_RESULTS":
        raise ValueError(f"ERDOS-{problem}: activation cohort state drift")
    if cohort.get("synthesis_allowed") is not False:
        raise ValueError(f"ERDOS-{problem}: activation record opened synthesis in place")

    return {
        "schema_version": "1.0.0",
        "record_type": "GCL_BLIND_COHORT_CLOSURE_RECEIPT",
        "receipt_id": f"ERDOS-{problem}-BLIND-COHORT-001:CLOSURE-001",
        "campaign": "ERDOS-OPEN-RECON",
        "work_package": f"ERDOS-{problem}-RECON-PACK-001",
        "cohort_id": f"ERDOS-{problem}-BLIND-COHORT-001",
        "closure_date": closure_date,
        "protected_evidence_base_commit": protected_commit,
        "activation_cohort_path": str(cohort_path.relative_to(ROOT)).replace("\\", "/"),
        "activation_cohort_blob_sha1": blob_sha1(cohort_path),
        "closure_basis": (
            "R1 and A1 each have one durably protected schema-valid RESULT/1 raw artifact and receipt; "
            + (
                "an outcome-changing source/formal semantic blocker is present, so the matching protected S1 return is additionally required before synthesis."
                if semantic_gate_dispatches
                else "this is the protected Programme minimum for synthesis."
            )
        ),
        "required_synthesis_lanes": required_synthesis_lanes,
        "evidence": [r, a],
        "source_lane": {
            "dispatch_id": lane_dispatch(problem, "S1"),
            "protected_at_closure": s is not None,
            "evidence": s,
        },
        "minimum_synthesis_evidence_satisfied": True,
        "semantic_blockers": semantic_blockers,
        "semantic_gate_required": bool(semantic_gate_dispatches),
        "semantic_gate_required_dispatch_ids": semantic_gate_dispatches,
        "semantic_source_audit_obligation_discharged": semantic_source_audit_discharged,
        "semantic_gate_satisfied_at_closure": semantic_source_audit_discharged,
        "blind_cohort_closed": True,
        "synthesis_allowed": semantic_source_audit_discharged,
        "source_lane_required_for_literature_dependent_promotion": True,
        "source_lane_protected_at_closure": s is not None,
        "literature_dependent_promotion_source_gate_satisfied_at_closure": s is not None,
        "mathematical_correctness_adjudicated": False,
        "independence_strength_adjudicated": False,
        "canonical_claim_effect": False,
        "certification_effect": False,
        "claim_promotion_effect": False,
        "late_source_lane_policy": (
            "Not applicable while a semantic source gate is active: the matching S1 return is a precondition for synthesis."
            if semantic_gate_dispatches
            else "A later S1 return is preserved as source-dependency evidence but does not retroactively alter the completed blind R1+A1 comparison; literature-dependent promotion remains separately adjudicated."
        ),
        "claim_boundary": "This receipt closes only the blind evidence-collection barrier at the protected R1+A1 synthesis minimum. It permits internal comparison and synthesis; it does not admit a mathematical claim, establish literature status, certify a theorem, authorize publication, or create MATHCERT effect.",
    }


def validate_closure(problem: str, closure: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    expected_cohort = f"ERDOS-{problem}-BLIND-COHORT-001"
    if closure.get("schema_version") != "1.0.0":
        errors.append("schema version drift")
    if closure.get("record_type") != "GCL_BLIND_COHORT_CLOSURE_RECEIPT":
        errors.append("record type drift")
    if closure.get("cohort_id") != expected_cohort:
        errors.append("cohort identity drift")
    if closure.get("campaign") != "ERDOS-OPEN-RECON":
        errors.append("campaign drift")
    if closure.get("work_package") != f"ERDOS-{problem}-RECON-PACK-001":
        errors.append("work package drift")
    if not SHA40.fullmatch(str(closure.get("protected_evidence_base_commit", ""))):
        errors.append("protected evidence base malformed")
    if closure.get("required_synthesis_lanes") not in (
        ["R1", "A1"],
        ["R1", "A1", "S1"],
    ):
        errors.append("minimum synthesis lane set drift")
    if closure.get("minimum_synthesis_evidence_satisfied") is not True:
        errors.append("minimum synthesis evidence not satisfied")
    if closure.get("blind_cohort_closed") is not True or closure.get("synthesis_allowed") is not True:
        errors.append("closure/synthesis state not open")
    for key in (
        "mathematical_correctness_adjudicated",
        "independence_strength_adjudicated",
        "canonical_claim_effect",
        "certification_effect",
        "claim_promotion_effect",
    ):
        if closure.get(key) is not False:
            errors.append(f"authority inflation: {key}")

    cohort_path = BASE / "cohorts" / f"{expected_cohort}.json"
    expected_cohort_rel = str(cohort_path.relative_to(ROOT)).replace("\\", "/")
    if closure.get("activation_cohort_path") != expected_cohort_rel:
        errors.append("activation cohort path drift")
    elif cohort_path.is_file() and closure.get("activation_cohort_blob_sha1") != blob_sha1(cohort_path):
        errors.append("activation cohort blob drift")
    if cohort_path.is_file():
        cohort = readj(cohort_path)
        if cohort.get("state") != "OPEN_AWAITING_RESULTS" or cohort.get("synthesis_allowed") is not False:
            errors.append("activation cohort was reclassified in place")

    evidence = closure.get("evidence")
    if not isinstance(evidence, list) or len(evidence) != 2:
        errors.append("closure must bind exactly R1+A1 evidence")
        evidence = []
    by_lane = {item.get("lane"): item for item in evidence if isinstance(item, dict)}
    for lane in ("R1", "A1"):
        try:
            live = lane_receipt(problem, lane)
        except ValueError as exc:
            errors.append(str(exc))
            continue
        if live is None:
            errors.append(f"{lane}: protected receipt absent")
            continue
        item = by_lane.get(lane)
        if not evidence_binding_matches(item, live):
            errors.append(f"{lane}: closure evidence binding differs from protected evidence")

    try:
        live_r = lane_receipt(problem, "R1")
        live_a = lane_receipt(problem, "A1")
        live_blockers = merge_blockers(
            live_r.get("semantic_blockers", []) if live_r else [],
            live_a.get("semantic_blockers", []) if live_a else [],
        )
        live_gate_dispatches = required_source_dispatches(live_blockers)
    except ValueError as exc:
        errors.append(str(exc))
        live_blockers = []
        live_gate_dispatches = []

    expected_required_lanes = ["R1", "A1"] + (["S1"] if live_gate_dispatches else [])
    if closure.get("required_synthesis_lanes") != expected_required_lanes:
        errors.append("semantic gate synthesis lane set drift")
    if closure.get("semantic_blockers", []) != live_blockers:
        errors.append("semantic blocker binding drift")
    if closure.get("semantic_gate_required", False) is not bool(live_gate_dispatches):
        errors.append("semantic gate required flag drift")
    if closure.get("semantic_gate_required_dispatch_ids", []) != live_gate_dispatches:
        errors.append("semantic gate dispatch set drift")
    if live_gate_dispatches:
        if closure.get("semantic_source_audit_obligation_discharged") is not True:
            errors.append("semantic source-audit obligation not discharged")
        if closure.get("semantic_gate_satisfied_at_closure") is not True:
            errors.append("semantic gate not satisfied at closure")
        if closure.get("synthesis_allowed") is not True:
            errors.append("semantic gate did not open synthesis")

    source = closure.get("source_lane")
    if not isinstance(source, dict) or source.get("dispatch_id") != lane_dispatch(problem, "S1"):
        errors.append("source lane identity drift")
    else:
        try:
            live_s = lane_receipt(problem, "S1")
        except ValueError as exc:
            errors.append(str(exc))
            live_s = None
        at_close = source.get("protected_at_closure")
        if at_close not in (True, False):
            errors.append("source protected-at-closure flag malformed")
        if at_close is True and not evidence_binding_matches(source.get("evidence"), live_s):
            errors.append("source closure evidence differs from protected evidence")
        if closure.get("source_lane_protected_at_closure") is not at_close:
            errors.append("source lane closure flag disagreement")
        if closure.get("literature_dependent_promotion_source_gate_satisfied_at_closure") is not at_close:
            errors.append("source promotion gate flag disagreement")
        if live_gate_dispatches:
            if live_s is None:
                errors.append("semantic source gate required S1 but protected receipt is absent")
            elif live_s.get("disposition_declared") == "EXACT_BLOCKER":
                errors.append("semantic source gate S1 remains blocked")
            if at_close is not True:
                errors.append("semantic source gate requires S1 protected at closure")

    return errors
