#!/usr/bin/env python3
"""Validate exact successor-002 review and authority boundaries on protected input."""
from __future__ import annotations

import json
from pathlib import Path
try:
    from ci.erdos_successor_002_replay import BASE, INPUTS, ROOT, build_report
except ModuleNotFoundError:
    from erdos_successor_002_replay import BASE, INPUTS, ROOT, build_report

ADJ = ROOT / BASE / "adjudications/ERDOS-SUCCESSOR-002-ADJUDICATION-001.json"
SYNTH = ROOT / BASE / "synthesis/ERDOS-SUCCESSOR-002-SYNTHESIS-001.md"
EXPECTED = ROOT / BASE / "replays/ERDOS-SUCCESSOR-002-REPLAY-001.json"
CLOSURES = {
    593: ROOT / BASE / "closures/ERDOS-593-SUCCESSOR-BLIND-COHORT-002.json",
    470: ROOT / BASE / "closures/ERDOS-470-SUCCESSOR-BLIND-COHORT-002.json",
}


def validate() -> list[str]:
    errors = []
    adj = json.loads(ADJ.read_text(encoding="utf-8"))
    replay = json.loads(EXPECTED.read_text(encoding="utf-8"))
    if replay != build_report():
        errors.append("native replay artifact changed relative to inputs or algorithm")
    if adj.get("record_type") != "GCL_ERDOS_OPEN_SUCCESSOR_SYNTHESIS_ADJUDICATION":
        errors.append("adjudication record type differs")
    if adj.get("pipeline") != [
        "RETURNED","CAPTURED","PROTECTED","BLIND_COHORT_CLOSED",
        "REPLAYED","ADJUDICATED","SUCCESSOR_SPECIFIED"
    ]:
        errors.append("pipeline phase inflation or missing phase")
    if not adj.get("input_protection",{}).get("evidence_from_protected_main"):
        errors.append("missing protected evidence boundary")

    all_ids = []
    for problem, path in CLOSURES.items():
        closure = json.loads(path.read_text(encoding="utf-8"))
        if closure.get("problem_id") != problem or closure.get("state") != "BLIND_COLLECTION_CLOSED_AFTER_PROTECTED_EVIDENCE":
            errors.append(f"invalid closure: {problem}")
        if closure.get("synthesis_allowed") is not True:
            errors.append(f"closure cannot synthesize: {problem}")
        if closure.get("certification_effect") is not False or closure.get("parent_problem_effect") is not False:
            errors.append(f"authority inflation in closure: {problem}")
        for item in closure.get("protected_evidence", []):
            did = item.get("dispatch_id")
            all_ids.append(did)
            if did not in INPUTS or item.get("github_comment_id") != INPUTS[did]:
                errors.append(f"unrecognized closure evidence {did}")
                continue
            raw_path = ROOT / item["raw_artifact_path"]
            receipt_path = ROOT / item["receipt_path"]
            if not raw_path.is_file() or not receipt_path.is_file():
                errors.append(f"missing protected evidence {did}")
                continue
            import hashlib
            def blob_sha(data:bytes) -> str:
                return hashlib.sha1(("blob " + str(len(data))).encode() + bytes([0]) + data).hexdigest()
            if blob_sha(raw_path.read_bytes()) != item["raw_blob_sha1"]:
                errors.append(f"raw git blob drift: {did}")
            if blob_sha(receipt_path.read_bytes()) != item["receipt_blob_sha1"]:
                errors.append(f"receipt git blob drift: {did}")
            if item.get("mathematical_correctness_adjudicated") is not False:
                errors.append(f"closure overclaims mathematical review: {did}")
    if set(all_ids) != set(INPUTS) or len(all_ids) != len(INPUTS):
        errors.append("not exactly the three protected successor returns")

    claims = {x.get("claim_id"):x.get("disposition") for x in adj.get("claim_adjudications", [])}
    if claims.get("593-R2-TWO_COLOR_SHARPNESS") != "REFUTED_BY_RAMSEY_R3_3_EQUAL_6":
        errors.append("missing falsification")
    if claims.get("470-S2-ODD_WEIRD_EXCLUSION_BELOW_1E21") != "NOT_REPLAY_CERTIFIED":
        errors.append("odd-weird source promotion")
    if claims.get("593-S2-LI-FULL-CLASSIFICATION") != "SOURCE_REPORTED_NOT_REBUILT_OR_ADJUDICATED":
        errors.append("external Lean artifact incorrectly certified")

    successors = adj.get("selected_successors", [])
    if len(successors) != 3:
        errors.append("must specify exactly three bounded successor tasks")
    for next_job in successors:
        path = ROOT / str(next_job.get("path", ""))
        if next_job.get("status") != "READY_FOR_PROTECTED_DISPATCH" or next_job.get("registered_as_queue_job") is not False:
            errors.append("successor launch/registration authority inflated")
        if not path.is_file() or "EXTERNAL_DISPATCH_AUTHORIZED: NO" not in path.read_text(encoding="utf-8"):
            errors.append("successor missing or unauthorized")

    effects = adj.get("effects", {})
    for key in ("parent_problem_593_solved","parent_problem_470_solved",
                "external_theorem_dependency_discharged","external_lean_build_replayed",
                "full_odd_weird_search_replayed","certification_effect",
                "publication_effect","prize_effect"):
        if effects.get(key) is not False:
            errors.append(f"adjudication authority inflation: {key}")
    synth = SYNTH.read_text(encoding="utf-8")
    for phrase in ("32768", "first differing coordinate", "SOURCE_REPORTED_NOT_VERIFIED",
                   "NOT", "READY_FOR_PROTECTED_DISPATCH"):
        if phrase not in synth:
            errors.append(f"synthesis missing boundary: {phrase}")
    return errors


if __name__ == "__main__":
    problems = validate()
    for problem in problems:
        print("FAIL:", problem)
    if problems:
        raise SystemExit(1)
    print("PASS: ERDOS successor-002 replay, closures, adjudication, successor boundaries")
