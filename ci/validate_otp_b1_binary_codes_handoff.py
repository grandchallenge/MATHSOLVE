#!/usr/bin/env python3
from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-B1-BINARY-CODES.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_b1_binary_codes_handoff.schema.json"
TARGETS = [
    "MetricCodes.Hamming.binaryRate_lt_classicalRate",
    "MetricCodes.Hamming.exists_binaryRate_improvement",
    "MetricCodes.Johnson.binaryRate_le_combinedVariationalRate",
    "MetricCodes.MRRW.strict_mrrw2",
    "MetricCodes.Johnson.binaryRate_lt_mrrw",
    "MetricCodes.Johnson.exists_binaryRate_mrrw_improvement",
]
CLASSES = [
    "source_faithful_derived_consequence",
    "derived_positive_margin_certificate",
    "source_faithful_exact_projection",
    "source_faithful_exact_projection",
    "source_faithful_derived_consequence",
    "derived_positive_margin_certificate",
]
AXIOMS = ["propext", "Quot.sound", "Classical.choice"]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e: list[str] = []
    if s.get("additionalProperties") is not False:
        e.append("schema must remain top-level closed")
    e.extend(f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r))

    if (r.get("handoff_id"), r.get("result_family"), r.get("tracker_issue")) != (
        "MC-OTP-HANDOFF-B1-BINARY-CODES", "OTP-B1-BINARY-CODES", 114
    ):
        e.append("handoff identity drift")
    if r.get("protected_solve_base") != "7d1f9edf16558ba4c4396126e24fd2c9ae4826f7":
        e.append("protected Solve base drift")

    a = r.get("authority", {})
    exact = {
        "forge_formal_source_successor_merge": "48e8bf8e0fd157688ae83a8110d63b1e500ee688",
        "forge_semantic_merge": "24a1fa0f020ee9cc7fbe2e7aea4cd840268ca748",
        "forge_semantic_reviewed_head": "708375b57b158fdf1af2cc59343eb2371fd673f3",
        "forge_semantic_review_id": 4949261532,
        "forge_semantic_reviewer": "jimsteeg",
    }
    for k, v in exact.items():
        if a.get(k) != v:
            e.append(f"authority drift: {k}")

    sem = a.get("semantic_record", {})
    if sem != {
        "repository": "grandchallenge/MATHFORGE",
        "commit_sha": "24a1fa0f020ee9cc7fbe2e7aea4cd840268ca748",
        "path": "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-B1-BINARY-CODES/audit_record.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "0ab4d973bc046084e9d2dc6c7552ab5428d7412d",
    }:
        e.append("semantic record identity drift")

    pdf = a.get("source_pdf", {})
    if (pdf.get("revision"), pdf.get("sha256"), pdf.get("byte_length"), pdf.get("successor_record_blob")) != (
        "2026-08-06",
        "ebc561ab5c53dbd240e17a8fdb6fffeb648591eca85dbfc7466f563638f8c566",
        2487031,
        "02d1748abed36717afba46451330be165c076737",
    ):
        e.append("source PDF authority drift")

    subj = a.get("official_subject", {})
    for k, v in {
        "repository": "openai/ten-proofs",
        "commit": "94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6",
        "tree": "174289e4d4958cb0509874e6e53400e098213de7",
        "formal_successor_record_blob": "6993ce9fac2c65ffae7f2a0c7d728aab828ed532",
        "config_blob": "b530b77972c83396c1f2aed2deccda3a12fb6cab",
        "challenge_blob": "c9e93b1944e6806802068cf593fa6557e4267bb1",
        "solution_blob": "51628c0db81bd6cb9a79777fa601306c9d64cbc5",
    }.items():
        if subj.get(k) != v:
            e.append(f"formal subject drift: {k}")

    replay = a.get("replay", {})
    if (replay.get("run_id"), replay.get("job_id"), replay.get("result")) != (
        31945652355, 95161117069, "comparator_lean_kernel_nanoda_accept"
    ):
        e.append("replay identity/result drift")
    if replay.get("permitted_axioms") != AXIOMS:
        e.append("axiom boundary drift")

    gate = r.get("semantic_gate", {})
    if gate.get("state") != "clear" or gate.get("disposition") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("semantic gate drift")
    if gate.get("activated_by_protected_merge") != "24a1fa0f020ee9cc7fbe2e7aea4cd840268ca748":
        e.append("semantic activation drift")
    if gate.get("forge_record_solve_handoff_authorized") is not False:
        e.append("Forge authority inflated")

    scope = r.get("target_scope", {})
    if scope.get("lean_theorems") != TARGETS:
        e.append("target inventory/order drift")
    if scope.get("classifications") != CLASSES:
        e.append("target classification drift")
    q = "\n".join(scope.get("mandatory_qualifications", []))
    for token in ("positive-margin", "sInf", "logarithm base", "whole-chapter"):
        if token not in q:
            e.append(f"mandatory qualification lost: {token}")

    nv = r.get("nonvacuity", {})
    if nv.get("state") != "clear_for_all_six_targets":
        e.append("nonvacuity state drift")
    nvt = "\n".join(nv.get("evidence", []))
    for token in ("delta=1/4", "codeNumber_pos", "rateSet_nonempty_of_interior", "exists_mrrw_minimizer"):
        if token not in nvt:
            e.append(f"nonvacuity evidence lost: {token}")

    adj = r.get("requested_adjudication", {})
    if adj != {
        "mode": "independent_result_family_review",
        "route_id": "MC-ROUTE-OTP-B1-BINARY-CODES",
        "current_route_state": "not_registered",
        "cert_output": None,
        "may_adjudicate_on_branch": False,
    }:
        e.append("requested adjudication boundary drift")

    controls = r.get("route_controls", {})
    for k in (
        "historical_six_packet_registry_mutable",
        "may_create_aggregate_handoff",
        "may_imply_mathcert_acceptance",
        "may_imply_adjudication",
        "may_claim_mathematical_proof",
        "may_promote_claim",
        "whole_chapter_equivalence",
    ):
        if controls.get(k) is not False:
            e.append(f"route/claim authority inflation: {k}")
    if controls.get("result_family_only") is not True:
        e.append("result-family isolation lost")

    boundary = r.get("claim_boundary", "")
    for token in ("exact six configured targets", "positive-margin", "historical six-packet registry", "aggregate OpenAI Ten Proofs", "MATHCERT route"):
        if token not in boundary:
            e.append(f"claim boundary lost: {token}")
    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-B1 Binary Codes successor handoff candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
