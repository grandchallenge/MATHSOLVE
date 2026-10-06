#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

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
    }


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
    s = lane_receipt(problem, "S1")

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
        "closure_basis": "R1 and A1 each have one durably protected schema-valid RESULT/1 raw artifact and receipt; this is the protected Programme minimum for synthesis.",
        "required_synthesis_lanes": ["R1", "A1"],
        "evidence": [r, a],
        "source_lane": {
            "dispatch_id": lane_dispatch(problem, "S1"),
            "protected_at_closure": s is not None,
            "evidence": s,
        },
        "minimum_synthesis_evidence_satisfied": True,
        "blind_cohort_closed": True,
        "synthesis_allowed": True,
        "source_lane_required_for_literature_dependent_promotion": True,
        "source_lane_protected_at_closure": s is not None,
        "literature_dependent_promotion_source_gate_satisfied_at_closure": s is not None,
        "mathematical_correctness_adjudicated": False,
        "independence_strength_adjudicated": False,
        "canonical_claim_effect": False,
        "certification_effect": False,
        "claim_promotion_effect": False,
        "late_source_lane_policy": "A later S1 return is preserved as source-dependency evidence but does not retroactively alter the completed blind R1+A1 comparison; literature-dependent promotion remains separately adjudicated.",
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
    if closure.get("required_synthesis_lanes") != ["R1", "A1"]:
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
        if item != live:
            errors.append(f"{lane}: closure evidence binding differs from protected evidence")

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
        if at_close is True and source.get("evidence") != live_s:
            errors.append("source closure evidence differs from protected evidence")
        if closure.get("source_lane_protected_at_closure") is not at_close:
            errors.append("source lane closure flag disagreement")
        if closure.get("literature_dependent_promotion_source_gate_satisfied_at_closure") is not at_close:
            errors.append("source promotion gate flag disagreement")

    return errors
