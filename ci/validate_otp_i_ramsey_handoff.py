#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-I-RAMSEY.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_i_ramsey_handoff.schema.json"
TARGETS = [
    "ErdosProblems.MulticolourTriangleRamsey.erdos_183",
    "ErdosProblems.MulticolourTriangleRamsey.erdos_problem_183_explicit",
    "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_sharp_coefficients",
    "ErdosProblems.MulticolourTriangleRamsey.triangleRamseyNumber_log_isTheta",
]
CLASSES = [
    "source_faithful_exact_projection_of_displayed_consequence_4",
    "formal_explicit_constant_strengthening_plus_source_faithful_divergence",
    "source_faithful_epsilonized_logarithmic_reformulation",
    "source_faithful_logarithmic_reformulation_of_printed_theta",
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
    if (r.get("handoff_id"), r.get("result_family"), r.get("tracker_issue")) != ("MC-OTP-HANDOFF-I-RAMSEY", "OTP-I-RAMSEY", 121):
        e.append("handoff identity drift")
    if r.get("protected_solve_base") != "c19735edf4c16ac9765bb66c7209bbf11bf1312e":
        e.append("protected Solve base drift")
    a = r.get("authority", {})
    exact = {
        "forge_formal_source_successor_merge": "48e8bf8e0fd157688ae83a8110d63b1e500ee688",
        "forge_semantic_merge": "dbf3b099331a1807c4d3036e7a6a406711ea7cf3",
        "forge_semantic_reviewed_head": "8141ab3bbd2f94574c9ea5fe1d29d11f40f4c484",
        "forge_semantic_review_id": 4950160253,
        "forge_semantic_reviewer": "jimsteeg",
    }
    for k, v in exact.items():
        if a.get(k) != v:
            e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {
        "repository":"grandchallenge/MATHFORGE","commit_sha":"dbf3b099331a1807c4d3036e7a6a406711ea7cf3","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-I-RAMSEY/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"a7c014fb623b66355ef5d6260e5b994d99d67a6d"}:
        e.append("semantic record identity drift")
    subj = a.get("official_subject", {})
    for k, v in {
        "commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","config_blob":"ce67db0653e18a2deccda3a12fb6cab","challenge_blob":"6a9e42d686720f4b74ddc2001006b0b7a20f11aa","solution_blob":"24b55f531a4d36347cd2277b1b9c7d784d91ae35"}.items():
        if subj.get(k) != v:
            e.append(f"formal subject drift: {k}")
    replay = a.get("replay", {})
    if (replay.get("run_id"), replay.get("job_id"), replay.get("result")) != (31945652355, 95161117103, "comparator_lean_kernel_nanoda_accept"):
        e.append("replay identity/result drift")
    if replay.get("permitted_axioms") != AXIOMS:
        e.append("axiom boundary drift")
    gate = r.get("semantic_gate", {})
    if gate.get("state") != "clear" or gate.get("disposition") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("semantic gate drift")
    if gate.get("activated_by_protected_merge") != "dbf3b099331a1807c4d3036e7a6a406711ea7cf3" or gate.get("forge_record_solve_handoff_authorized") is not False:
        e.append("semantic activation/authority drift")
    scope = r.get("target_scope", {})
    if scope.get("lean_theorems") != TARGETS:
        e.append("target inventory/order drift")
    if scope.get("classifications") != CLASSES:
        e.append("target classification drift")
    q = "\n".join(scope.get("mandatory_qualifications", []))
    for token in ("1/(6*exp 38)", "natural-log", "Filter-Theta", "least-Ramsey-number", "whole-chapter"):
        if token not in q:
            e.append(f"mandatory qualification lost: {token}")
    if r.get("nonvacuity", {}).get("state") != "clear_for_all_four_targets":
        e.append("nonvacuity state drift")
    adj = r.get("requested_adjudication", {})
    if (adj.get("route_id"), adj.get("current_route_state"), adj.get("cert_output"), adj.get("may_adjudicate_on_branch")) != ("MC-ROUTE-OTP-I-RAMSEY", "not_registered", None, False):
        e.append("requested adjudication boundary drift")
    controls = r.get("route_controls", {})
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_chapter_equivalence"):
        if controls.get(k) is not False:
            e.append(f"route/claim authority inflation: {k}")
    if controls.get("result_family_only") is not True:
        e.append("result-family isolation lost")
    boundary = r.get("claim_boundary", "")
    for token in ("exact four configured targets", "1/(6*exp 38)", "historical six-packet registry", "aggregate OpenAI Ten Proofs", "MATHCERT route"):
        if token not in boundary:
            e.append(f"claim boundary lost: {token}")
    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-I Ramsey successor handoff candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
