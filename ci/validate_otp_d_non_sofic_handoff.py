#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-D-NON-SOFIC.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_d_non_sofic_handoff.schema.json"
TARGETS = ["SoficGroups.SourceTopLevelCompressionFinal.exists_finitelyPresented_nonsofic_group"]
CLASSES = ["derived_finitely_presented_nonsofic_consequence_of_source_nonsofic_construction"]
AXIOMS = ["propext", "Classical.choice", "Quot.sound"]


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(record=None, schema=None):
    r = load(RECORD) if record is None else record
    s = load(SCHEMA) if schema is None else schema
    e: list[str] = []
    if s.get("additionalProperties") is not False:
        e.append("schema must remain top-level closed")
    e.extend(f"schema: {x.message}" for x in Draft202012Validator(s).iter_errors(r))
    if (r.get("handoff_id"), r.get("result_family"), r.get("tracker_issue")) != ("MC-OTP-HANDOFF-D-NON-SOFIC", "OTP-D-NON-SOFIC", 123):
        e.append("handoff identity drift")
    if r.get("protected_solve_base") != "c19735edf4c16ac9765bb66c7209bbf11bf1312e":
        e.append("protected Solve base drift")
    a = r.get("authority", {})
    for k, v in {
        "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
        "forge_semantic_merge":"081928fceaca9606af4920559f8b79d5e40225a7",
        "forge_semantic_reviewed_head":"a80fe85315f51089b30fad918ce8089cd00be3f6",
        "forge_semantic_review_id":4956527688,
        "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k) != v:
            e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {
        "repository":"grandchallenge/MATHFORGE","commit_sha":"081928fceaca9606af4920559f8b79d5e40225a7","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-D-NON-SOFIC/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"a9a5a2d56fceda6ebddf0c729d97c7cbeaf0d48b"}:
        e.append("semantic record identity drift")
    subj = a.get("official_subject", {})
    for k, v in {
        "commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","config_blob":"af023106a83552d7fafb4f0d122f121a095f802c","challenge_blob":"158d97224fbd51c203ff07a2f74041ffa2c6013b","solution_blob":"dd1f8e63960300c8674fcd491007d2a628fbc6fe","mathlib_finite_presentation_commit":"81a5d257c8e410db227a6665ed08f64fea08e997","mathlib_finite_presentation_blob":"449ec578624bd05410992e89048a7c1a7bae238d"}.items():
        if subj.get(k) != v:
            e.append(f"formal subject drift: {k}")
    replay = a.get("replay", {})
    if (replay.get("run_id"), replay.get("job_id"), replay.get("result")) != (31945652355, 95161117044, "comparator_lean_kernel_nanoda_accept"):
        e.append("replay identity/result drift")
    if replay.get("permitted_axioms") != AXIOMS:
        e.append("axiom boundary drift")
    gate = r.get("semantic_gate", {})
    if gate.get("state") != "clear" or gate.get("disposition") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("semantic gate drift")
    if gate.get("activated_by_protected_merge") != "081928fceaca9606af4920559f8b79d5e40225a7" or gate.get("forge_record_solve_handoff_authorized") is not False:
        e.append("semantic activation/authority drift")
    scope = r.get("target_scope", {})
    if scope.get("lean_theorems") != TARGETS:
        e.append("target inventory/order drift")
    if scope.get("classifications") != CLASSES:
        e.append("target classification drift")
    q = "\n".join(scope.get("mandatory_qualifications", []))
    for token in ("does not state", "formal derived consequence", "EL_D(R)/EL_9(R)", "Group.IsFinitelyPresented", "whole-chapter"):
        if token not in q:
            e.append(f"mandatory qualification lost: {token}")
    if r.get("nonvacuity", {}).get("state") != "clear_for_exact_target":
        e.append("nonvacuity state drift")
    adj = r.get("requested_adjudication", {})
    if (adj.get("route_id"), adj.get("current_route_state"), adj.get("cert_output"), adj.get("may_adjudicate_on_branch")) != ("MC-ROUTE-OTP-D-NON-SOFIC", "not_registered", None, False):
        e.append("requested adjudication boundary drift")
    controls = r.get("route_controls", {})
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_chapter_equivalence"):
        if controls.get(k) is not False:
            e.append(f"route/claim authority inflation: {k}")
    if controls.get("result_family_only") is not True:
        e.append("result-family isolation lost")
    boundary = r.get("claim_boundary", "")
    for token in ("exact single configured target", "does not rewrite Chapter 3 Theorem 1.1", "historical six-packet registry", "aggregate OpenAI Ten Proofs", "MATHCERT route"):
        if token not in boundary:
            e.append(f"claim boundary lost: {token}")
    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-D Non-Sofic successor handoff candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
