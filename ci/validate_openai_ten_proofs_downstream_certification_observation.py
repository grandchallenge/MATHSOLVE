#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/downstream_certification_observation.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_downstream_certification_observation.schema.json"
FILES = {
    "umbrella_sync": (ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/umbrella_sync.json", "deef1ee179042226128c7fdb2906abacbcaea60c"),
    "handoff_registry": (ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_registry.json", "82b4cc14a3c7700ab51ee25f06e6ba03c72e499c"),
    "ehrhart_packet": (ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-F-EHRHART.json", "4653985d4980113514266c3c421804437bacb019"),
    "compactness_packet": (ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J1-COMPACTNESS.json", "2d9c6e555a03b71eb33c476321e7f2d311ed168f"),
    "two_degenerate_packet": (ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J2-TWO-DEGENERATE.json", "0d226492bf13e13bc1a437be01104db3d4c96f79"),
}


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload, usedforsecurity=False).hexdigest()


def validation_errors(*, record=None, schema=None, blobs=None) -> list[str]:
    record = load(RECORD) if record is None else record
    schema = load(SCHEMA) if schema is None else schema
    blobs = {name: git_blob_sha1(path) for name, (path, _) in FILES.items()} if blobs is None else blobs
    errors: list[str] = []

    if schema.get("additionalProperties") is not False:
        errors.append("observation schema must remain closed")
    errors.extend(f"schema violation: {error.message}" for error in Draft202012Validator(schema).iter_errors(record))

    for name, (_, expected) in FILES.items():
        if blobs.get(name) != expected:
            errors.append(f"protected Solve blob drift: {name}")

    authority = record.get("solve_authority", {})
    if authority.get("owns_cert_route") is not False:
        errors.append("Solve route authority inflation")
    if authority.get("owns_adjudication") is not False:
        errors.append("Solve adjudication authority inflation")
    if authority.get("owns_cert_output") is not False:
        errors.append("Solve Cert-output authority inflation")

    cert = record.get("mathcert_authority", {})
    expected_cert = {
        "repository": "grandchallenge/MATHCERT",
        "execution_merge": "1d5b1e6514787005ed75e363df7ea953dcd9391a",
        "documentary_closure_merge": "150344d25b50895203c59f4193a8e97bb1cbbf81",
        "closure_exact_reviewed_head": "207df8462f427e0c41604614ebe1a291ad89273f",
        "closure_review_id": 4840018727,
        "closure_human_steward_disposition_comment": 5160923732,
        "route_registry_blob": "0487c3ebf702229741f16a544d68af25cf994e41",
        "certificate_id": "MC-OTP-F-EHRHART-QUAL-001",
        "certificate_blob": "27a855c949b67e71372c7f0d6601d80125d33968",
        "attestation_manifest_blob": "d8b36ffdb3b5e732b385c9bac5576aa96dd1fcbe",
        "successor_closure_blob": "c50a397a84873b358a54db2e602058da103b75e8",
    }
    for key, value in expected_cert.items():
        if cert.get(key) != value:
            errors.append(f"MATHCERT authority drift: {key}")

    states = record.get("observed_family_state", [])
    if [entry.get("result_family") for entry in states] != ["OTP-F-EHRHART", "OTP-J1-COMPACTNESS", "OTP-J2-TWO-DEGENERATE"]:
        errors.append("family membership or order drift")
    if any(entry.get("producer_packet_unchanged") is not True for entry in states):
        errors.append("producer packet mutation admitted")
    if not states or states[0].get("route_state") != "qualified" or states[0].get("restricted_cert_output_count") != 1:
        errors.append("Ehrhart downstream state drift")
    for entry in states[1:]:
        if entry.get("route_state") != "submitted" or entry.get("adjudication_count") != 0 or entry.get("restricted_cert_output_count") != 0:
            errors.append(f"another-family downstream inflation: {entry.get('result_family')}")
    if record.get("aggregate_handoff") is not None or record.get("aggregate_output_count") != 0:
        errors.append("aggregate authority inflation")
    if record.get("mathematical_targets_marked_proved") != 0:
        errors.append("proof-status promotion")

    limitations = record.get("preserved_limitations", {})
    if limitations.get("blocked_repair_lanes") != ["OTP-C-PERMANENT", "OTP-H-GAPCVP"]:
        errors.append("blocked repair lanes drift")
    if limitations.get("all_lean_state") != "failed_namespace_collision":
        errors.append("All.lean blocker drift")
    if limitations.get("unexamined_result_family_count") != 9:
        errors.append("unexamined family count drift")
    if limitations.get("aggregate_ten_proofs_authority") is not False:
        errors.append("aggregate ten-proofs authority inserted")

    boundary = str(record.get("claim_boundary", ""))
    for token in ("does not modify the three producer packets", "create or own a Cert route", "mathematical target proved", "Compactness or Two-degenerate", "aggregate authority", "commercial claims"):
        if token not in boundary:
            errors.append(f"claim boundary missing token: {token}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated Solve downstream certification observation with immutable producer packets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
