#!/usr/bin/env python3
"""Fail-closed validation of protected Erdős successor-003 evidence and adjudication.

No external theorem, Lean kernel build, workunit inventory or independent
agent-runtime claim is certified by this validator.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("contributions/ERDOS-OPEN-001/SUCCESSOR_003")
ADJ_PATH = ROOT / BASE / "adjudications/ERDOS-SUCCESSOR-003-ADJUDICATION-001.json"
CLOSURES = {
    593: ROOT / BASE / "closures/ERDOS-593-SUCCESSOR-003-EVIDENCE-CLOSURE.json",
    470: ROOT / BASE / "closures/ERDOS-470-SUCCESSOR-003-EVIDENCE-CLOSURE.json",
}
EXPECTED_DISPATCHES = {
    "ERDOS-593-N3-IA-001": (1031, 6081359458, 1042),
    "ERDOS-593-N4-IA-001": (1032, 6081231380, 1039),
    "ERDOS-470-N3-IA-001": (1033, 6081010515, 1038),
}

def git_blob_sha(data: bytes) -> str:
    prefix = ("blob " + str(len(data))).encode() + bytes([0])
    return hashlib.sha1(prefix + data).hexdigest()

def validate(root: Path = ROOT) -> list[str]:
    errors = []
    closures = {
        problem: json.loads((root / path.relative_to(ROOT)).read_text(encoding="utf-8"))
        for problem, path in CLOSURES.items()
    }
    adjudication = json.loads((root / ADJ_PATH.relative_to(ROOT)).read_text(encoding="utf-8"))
    found: set[str] = set()
    if adjudication.get("record_type") != "GCL_ERDOS_SUCCESSOR_003_CRITICAL_ADJUDICATION":
        errors.append("adjudication record type drift")
    if adjudication.get("lifecycle") != [
        "RETURNED","CAPTURED","PROTECTED","COHORT_EVIDENCE_CLOSED",
        "SOURCE_CROSSCHECKED","CLAIMS_ADJUDICATED"
    ]:
        errors.append("inaccurate phase inflation or missing lifecycle phase")
    evidence = adjudication.get("agent_provenance", {})
    if (evidence.get("authenticated_github_actor") != "fyremael"
            or evidence.get("separate_runtime_evidence") is not False
            or evidence.get("worker_blind_independence_verified") is not False):
        errors.append("unsupported independence attestation")

    for problem, closure in closures.items():
        if closure.get("problem_id") != problem:
            errors.append(f"{problem}: closure problem identity mismatch")
        if closure.get("record_type") != "GCL_ERDOS_SUCCESSOR_003_EVIDENCE_COHORT_CLOSURE":
            errors.append(f"{problem}: closure record type drift")
        if closure.get("state") != "EVIDENCE_CLOSED_FOR_SYNTHESIS":
            errors.append(f"{problem}: evidence not closed")
        if closure.get("source_transport_account") != "fyremael":
            errors.append(f"{problem}: source actor mismatch")
        if closure.get("claim_of_agent_runtime_independence") != "UNVERIFIED_SHARED_AUTHENTICATED_GITHUB_ACCOUNT":
            errors.append(f"{problem}: falsely attested independent workers")
        effects = closure.get("effects", {})
        if (effects.get("mathematical_certification") is not False
                or effects.get("problem_solution") is not False
                or effects.get("independent_mathematical_review") is not False):
            errors.append(f"{problem}: cohort authorization inflation")
        for entry in closure.get("inputs", []):
            dispatch = entry["dispatch_id"]
            if dispatch in found:
                errors.append("duplicate dispatch " + dispatch)
            found.add(dispatch)
            expected = EXPECTED_DISPATCHES.get(dispatch)
            if not expected or expected != (
                entry.get("issue_number"), entry.get("comment_id"),
                entry.get("protected_evidence_pr")
            ):
                errors.append("unexpected protected return " + dispatch)
                continue
            for key in ("raw_path", "receipt_path"):
                path = Path(entry[key])
                if path.is_absolute() or ".." in path.parts:
                    errors.append(dispatch + ": unsafe evidence path")
            raw_path = root / entry["raw_path"]
            receipt_path = root / entry["receipt_path"]
            if not raw_path.is_file() or not receipt_path.is_file():
                errors.append(dispatch + ": protected raw or receipt missing")
                continue
            raw, receipt_data = raw_path.read_bytes(), receipt_path.read_bytes()
            receipt = json.loads(receipt_data)
            if hashlib.sha256(raw).hexdigest() != entry["raw_sha256"]:
                errors.append(dispatch + ": raw digest changed")
            if git_blob_sha(raw) != entry["raw_blob_sha1"]:
                errors.append(dispatch + ": raw Git blob identity changed")
            if git_blob_sha(receipt_data) != entry["receipt_blob_sha1"]:
                errors.append(dispatch + ": receipt Git blob identity changed")
            matched = {
                "dispatch_id": dispatch,
                "github_comment_id": entry["comment_id"],
                "raw_artifact_path": entry["raw_path"],
                "raw_sha256": entry["raw_sha256"],
                "schema_result": "valid",
                "worker_reservation_enforced": True,
                "worker_reservation_owner": "fyremael",
                "authenticated_github_actor": "fyremael",
                "mathematical_correctness_adjudicated": False,
                "independence_strength_adjudicated": False,
                "certification_effect": False,
            }
            for key, value in matched.items():
                if receipt.get(key) != value:
                    errors.append(dispatch + ": receipt field drift " + key)
            if not raw.startswith(b"GCL-CONTRIBUTION-RESULT/1\n"):
                errors.append(dispatch + ": raw marker mismatch")
    if found != set(EXPECTED_DISPATCHES):
        errors.append("not exactly three successor-003 protected returns")
    claims = {
        item.get("id"): item.get("disposition")
        for item in adjudication.get("claim_decisions", [])
    }
    for key, expected in {
        "593-N3-LEAN-KERNEL-COMPLETION":"NOT_REPLAYED",
        "593-N4-PAIR_TRIANGLE_LINEARITY":"ACCEPTED_ELEMENTARY_ALREADY_REPLAYED_IN_002",
        "470-N3-WORKUNIT_HEADER_INCOMPATIBILITY":"PRECISE_FALSIFIABLE_WORKER_REPORTED_BLOCKER",
        "470-N3-EXCLUSION_BELOW_1E21":"NOT_CERTIFIED",
    }.items():
        if claims.get(key) != expected:
            errors.append("claim adjudication drift: " + key)
    effects = adjudication.get("authority_effects", {})
    for key in ("agent_runtime_independence_verified", "lean_kernel_replayed",
                "odd_weird_exhaustive_search_replayed", "erdos_593_solved",
                "erdos_470_solved", "certification", "publication"):
        if effects.get(key) is not False:
            errors.append("authority inflation: " + key)
    residual_ids = {x.get("id") for x in adjudication.get("residuals", [])}
    if residual_ids != {"ERDOS-593-N5-KERNEL-REPLAY", "ERDOS-470-N4-HISTORICAL-REPLAY-INTERFACE"}:
        errors.append("unbound or missing bounded research residual")
    synth = root / adjudication.get("synthesis_path", "")
    if not synth.is_file():
        errors.append("synthesis document missing")
    else:
        s = synth.read_text(encoding="utf-8")
        for phrase in ("fyremael", "UNVERIFIED", "NOT REPLAYED",
                       "seven", "nine", "source", "MathCert"):
            if phrase not in s:
                errors.append("synthesis boundary omitted: " + phrase)
    return errors

if __name__ == "__main__":
    errors = validate()
    for e in errors:
        print("FAIL:", e)
    if errors:
        raise SystemExit(1)
    print("PASS: 3 protected returns, qualified adjudication and certification boundaries")
