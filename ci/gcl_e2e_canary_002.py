#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "contributions" / "GCL-E2E-CANARY-002"
DISPATCH_ID = "GCL-E2E-CANARY-002-IA-001"
COHORT_ID = "GCL-E2E-CANARY-COHORT-002"
ASSIGNMENT_ID = "GCL-E2E-CANARY-002"
SUCCESSOR_ID = "GCL-E2E-CANARY-003"
SHA40 = re.compile(r"^[0-9a-f]{40}$")
DATE = re.compile(r"^20\d\d-\d\d-\d\d$")

EXPECTED_SECTIONS = {
    "strongest": "3 + 4 = 7.",
    "derivation": "Integer addition gives 3 + 4 = 7.",
    "assumptions": "None.",
    "verification": "Recompute the integer sum 3 + 4.",
    "boundary": "This is a live-participant production-path canary only. It creates no mathematical, certification, publication, or external claim authority.",
    "residual": "Advance only to the precommitted canary successor GCL-E2E-CANARY-003 if deterministic replay confirms the exact fixed answer.",
}

def readj(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))

def blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()

def receipt() -> dict[str, Any] | None:
    directory = BASE / "receipts" / DISPATCH_ID
    if not directory.is_dir():
        return None
    paths = sorted(directory.glob("github-comment-*.json"))
    if len(paths) != 1:
        raise ValueError(f"{DISPATCH_ID}: expected exactly one protected receipt, found {len(paths)}")
    path = paths[0]
    r = readj(path)
    raw_rel = r.get("raw_artifact_path")
    if not isinstance(raw_rel, str):
        raise ValueError("canary receipt raw_artifact_path missing")
    raw = ROOT / raw_rel
    if not raw.is_file():
        raise ValueError("canary protected raw artifact missing")
    raw_text = raw.read_text(encoding="utf-8")
    if hashlib.sha256(raw_text.encode()).hexdigest() != r.get("raw_sha256"):
        raise ValueError("canary raw sha256 mismatch")
    checks = {
        "dispatch": r.get("dispatch_id") == DISPATCH_ID,
        "cohort": r.get("blind_cohort_id") == COHORT_ID,
        "schema": r.get("schema_result") == "valid",
        "freshness": r.get("freshness") == "current_for_dispatch",
        "handling": r.get("handling_state") == "received_unadjudicated",
        "claim": r.get("canonical_claim_effect") is False,
    }
    failed = [k for k,v in checks.items() if not v]
    if failed:
        raise ValueError("invalid canary receipt: " + ", ".join(failed))
    return {
        "dispatch_id": DISPATCH_ID,
        "github_issue_number": r.get("github_issue_number"),
        "github_comment_id": r.get("github_comment_id"),
        "raw_artifact_path": raw_rel,
        "raw_blob_sha1": blob_sha1(raw),
        "raw_sha256": r.get("raw_sha256"),
        "receipt_path": str(path.relative_to(ROOT)).replace("\\","/"),
        "receipt_blob_sha1": blob_sha1(path),
        "disposition_declared": r.get("disposition_declared"),
    }

def build_closure(protected_commit: str, closure_date: str) -> dict[str, Any]:
    if not SHA40.fullmatch(protected_commit):
        raise ValueError("protected evidence commit must be SHA-1")
    if not DATE.fullmatch(closure_date):
        raise ValueError("closure date must be YYYY-MM-DD")
    ev = receipt()
    if ev is None:
        raise ValueError("canary protected RESULT/1 absent")
    cohort_path = BASE / "cohort.json"
    cohort = readj(cohort_path)
    if cohort.get("state") != "OPEN_AWAITING_RESULT" or cohort.get("synthesis_allowed") is not False:
        raise ValueError("canary activation cohort state drift")
    return {
        "schema_version":"1.0.0",
        "record_type":"GCL_BLIND_COHORT_CLOSURE_RECEIPT",
        "receipt_id":COHORT_ID + ":CLOSURE-001",
        "campaign":"GCL-E2E-CANARY-002",
        "work_package":ASSIGNMENT_ID,
        "cohort_id":COHORT_ID,
        "closure_date":closure_date,
        "protected_evidence_base_commit":protected_commit,
        "activation_cohort_path":str(cohort_path.relative_to(ROOT)).replace("\\","/"),
        "activation_cohort_blob_sha1":blob_sha1(cohort_path),
        "evidence":[ev],
        "minimum_synthesis_evidence_satisfied":True,
        "blind_cohort_closed":True,
        "synthesis_allowed":True,
        "mathematical_correctness_adjudicated":False,
        "canonical_claim_effect":False,
        "certification_effect":False,
        "claim_boundary":"Mechanical one-member canary closure only; no mathematical or certification authority."
    }

def validate_closure(c: dict[str, Any]) -> list[str]:
    e=[]
    if c.get("record_type")!="GCL_BLIND_COHORT_CLOSURE_RECEIPT": e.append("record type drift")
    if c.get("cohort_id")!=COHORT_ID: e.append("cohort identity drift")
    if c.get("campaign")!="GCL-E2E-CANARY-002": e.append("campaign drift")
    if c.get("blind_cohort_closed") is not True or c.get("synthesis_allowed") is not True: e.append("closure not open")
    if c.get("mathematical_correctness_adjudicated") is not False: e.append("premature adjudication")
    if c.get("canonical_claim_effect") is not False or c.get("certification_effect") is not False: e.append("authority inflation")
    live=receipt()
    ev=c.get("evidence")
    if live is None or ev != [live]: e.append("protected evidence binding drift")
    return e

def _section(raw: str, heading: str, next_heading: str | None) -> str:
    start=raw.index(heading)+len(heading)
    end=raw.index(next_heading,start) if next_heading else len(raw)
    return raw[start:end].strip()

def build_replay() -> dict[str, Any]:
    ev=receipt()
    if ev is None: raise ValueError("canary protected RESULT/1 absent")
    raw=(ROOT/ev["raw_artifact_path"]).read_text(encoding="utf-8")
    headings=[
        "## Strongest exact statement","## Derivation","## Assumptions beyond bootstrap",
        "## Verification / falsification hooks","## Claim boundary","## Next residual"
    ]
    vals=[
        _section(raw,headings[i],headings[i+1] if i+1<len(headings) else None)
        for i in range(len(headings))
    ]
    expected=list(EXPECTED_SECTIONS.values())
    exact = vals == expected
    return {
        "schema_version":"1.0.0",
        "record_type":"GCL_E2E_CANARY_DETERMINISTIC_REPLAY",
        "replay_id":"GCL-E2E-CANARY-002-REPLAY-001",
        "dispatch_id":DISPATCH_ID,
        "raw_sha256":ev["raw_sha256"],
        "fixed_expression":"3 + 4",
        "expected_value":7,
        "recomputed_value":3+4,
        "sections_exact_match":exact,
        "replay_pass": exact and (3+4==7),
        "external_sources_used":False,
    }

def build_adjudication(replay: dict[str, Any]) -> dict[str, Any]:
    passed = replay.get("replay_pass") is True
    return {
        "schema_version":"1.0.0",
        "record_type":"GCL_E2E_CANARY_ADJUDICATION",
        "adjudication_id":"GCL-E2E-CANARY-002-ADJ-001",
        "campaign":"GCL-E2E-CANARY-002",
        "dispatch_id":DISPATCH_ID,
        "cohort_id":COHORT_ID,
        "fixed_expected_answer":7,
        "replay_pass":passed,
        "disposition":"ADVANCE" if passed else "REJECT",
        "selected_successor":SUCCESSOR_ID if passed else None,
        "effects":{
            "canary_effect":passed,
            "mathematical_claim_effect":False,
            "certification_effect":False,
            "publication_effect":False,
        },
    }

def successor_text() -> str:
    return """# GCL-E2E-CANARY-003\n\nSTATE: READY_CANARY_SUCCESSOR\nPREDECESSOR: GCL-E2E-CANARY-002\nEXPECTED_PREDECESSOR_ANSWER: 7\nCANONICAL_MATHEMATICAL_EFFECT: NO\nCERTIFICATION_AUTHORIZED: NO\n\nThis file exists only if the deterministic production canary replay/adjudication selected the precommitted successor.\n"""

def validate_bundle(replay: dict[str,Any], adj: dict[str,Any], successor: str) -> list[str]:
    e=[]
    if replay != build_replay(): e.append("replay differs from deterministic rebuild")
    if replay.get("replay_pass") is not True: e.append("replay failed")
    if adj != build_adjudication(replay): e.append("adjudication differs from deterministic rebuild")
    if adj.get("selected_successor") != SUCCESSOR_ID: e.append("successor identity drift")
    if successor != successor_text(): e.append("successor bytes drift")
    return e
