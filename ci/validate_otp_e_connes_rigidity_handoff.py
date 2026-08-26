#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-E-CONNES-RIGIDITY.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_e_connes_rigidity_handoff.schema.json"
TARGETS = [
    "ConnesRigidity.exists_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors",
    "ConnesRigidity.exists_infinite_pairwise_nonisomorphic_propertyT_icc_groups_with_isomorphic_factors",
]
CLASSES = [
    "source_faithful_two_group_consequence_with_structured_factor_isomorphism",
    "source_faithful_theorem_1_2_projection_with_derived_pairwise_factor_transitivity",
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
    if (r.get("handoff_id"), r.get("result_family"), r.get("tracker_issue")) != ("MC-OTP-HANDOFF-E-CONNES-RIGIDITY", "OTP-E-CONNES-RIGIDITY", 124):
        e.append("handoff identity drift")
    if r.get("protected_solve_base") != "c19735edf4c16ac9765bb66c7209bbf11bf1312e":
        e.append("protected Solve base drift")
    a = r.get("authority", {})
    for k, v in {
        "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
        "forge_semantic_merge":"ed8a65410336489ea5646808265c44f5387bebb8",
        "forge_semantic_reviewed_head":"bfc88a4ca0e63e358a1a33e6bad635f8d5852b3e",
        "forge_semantic_review_id":4956768577,
        "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k) != v:
            e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {
        "repository":"grandchallenge/MATHFORGE","commit_sha":"ed8a65410336489ea5646808265c44f5387bebb8","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-E-CONNES-RIGIDITY/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"ab38a22d029bacc09d7567166b3b5e380f207f99"}:
        e.append("semantic record identity drift")
    subj = a.get("official_subject", {})
    for k, v in {
        "commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","config_blob":"f5d2964be6b1a154bc12b38a0f99f0960960a2d9","challenge_blob":"9425edabd79319cbe2943888c6ece107bdd81dfb","solution_blob":"81cf03e3f7ccdc66815cc00c9969bcfd2341c8d6","mathlib_finite_generation_commit":"81a5d257c8e410db227a6665ed08f64fea08e997","mathlib_finite_generation_blob":"b23c7420082cfcfe583ba2ed39a8c9f0c86d73b1"}.items():
        if subj.get(k) != v:
            e.append(f"formal subject drift: {k}")
    replay = a.get("replay", {})
    if (replay.get("run_id"), replay.get("job_id"), replay.get("result")) != (31945652355, 95161117059, "comparator_lean_kernel_nanoda_accept"):
        e.append("replay identity/result drift")
    if replay.get("permitted_axioms") != AXIOMS:
        e.append("axiom boundary drift")
    gate = r.get("semantic_gate", {})
    if gate.get("state") != "clear" or gate.get("disposition") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("semantic gate drift")
    if gate.get("activated_by_protected_merge") != "ed8a65410336489ea5646808265c44f5387bebb8" or gate.get("forge_record_solve_handoff_authorized") is not False:
        e.append("semantic activation/authority drift")
    scope = r.get("target_scope", {})
    if scope.get("lean_theorems") != TARGETS:
        e.append("target inventory/order drift")
    if scope.get("classifications") != CLASSES:
        e.append("target classification drift")
    q = "\n".join(scope.get("mandatory_qualifications", []))
    for token in ("ConnesRigidity2.*", "spatial/tracial refinement", "every analytic notion of normality", "transitivity consequence through Lambda", "universe scope", "whole-chapter"):
        if token not in q:
            e.append(f"mandatory qualification lost: {token}")
    if r.get("nonvacuity", {}).get("state") != "clear_for_exact_two_target_surface_with_universe_scope_recorded":
        e.append("nonvacuity state drift")
    adj = r.get("requested_adjudication", {})
    if (adj.get("route_id"), adj.get("current_route_state"), adj.get("cert_output"), adj.get("may_adjudicate_on_branch")) != ("MC-ROUTE-OTP-E-CONNES-RIGIDITY", "not_registered", None, False):
        e.append("requested adjudication boundary drift")
    controls = r.get("route_controls", {})
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_chapter_equivalence"):
        if controls.get(k) is not False:
            e.append(f"route/claim authority inflation: {k}")
    if controls.get("result_family_only") is not True:
        e.append("result-family isolation lost")
    boundary = r.get("claim_boundary", "")
    for token in ("exact two configured current ConnesRigidity.* targets", "ConnesRigidity2.*", "spatial/tracial refinement", "historical six-packet registry", "aggregate OpenAI Ten Proofs", "MATHCERT route"):
        if token not in boundary:
            e.append(f"claim boundary lost: {token}")
    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-E Connes Rigidity successor handoff candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
