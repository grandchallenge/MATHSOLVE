#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoff_successors/OTP-G-QUANTUM-PARALLEL-REPETITION.json"
SCHEMA = ROOT / "schemas/openai_ten_proofs_g_quantum_parallel_repetition_handoff.schema.json"
TARGETS = [
    "QuantumParallelRepetition.distributionUniformExponential",
    "QuantumParallelRepetition.standardQuantumParallelRepetition",
]
CLASSES = [
    "source_faithful_exact_coordinate_projection_of_theorem_1_1",
    "source_faithful_consequence_on_source_domain_with_formal_empty_answer_extension",
]
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
    if (r.get("handoff_id"), r.get("result_family"), r.get("tracker_issue")) != ("MC-OTP-HANDOFF-G-QUANTUM-PARALLEL-REPETITION", "OTP-G-QUANTUM-PARALLEL-REPETITION", 122):
        e.append("handoff identity drift")
    if r.get("protected_solve_base") != "c19735edf4c16ac9765bb66c7209bbf11bf1312e":
        e.append("protected Solve base drift")
    a = r.get("authority", {})
    for k, v in {
        "forge_formal_source_successor_merge":"48e8bf8e0fd157688ae83a8110d63b1e500ee688",
        "forge_semantic_merge":"f0a40146cca7fd39c5724ed5be033ee9092625ac",
        "forge_semantic_reviewed_head":"6588608420da2651c83793852226cc321e1c85cf",
        "forge_semantic_review_id":4956356890,
        "forge_semantic_reviewer":"jimsteeg",
    }.items():
        if a.get(k) != v:
            e.append(f"authority drift: {k}")
    if a.get("semantic_record") != {
        "repository":"grandchallenge/MATHFORGE","commit_sha":"f0a40146cca7fd39c5724ed5be033ee9092625ac","path":"sources/OPENAI-TEN-PROOFS-001/semantic/OTP-G-QUANTUM-PARALLEL-REPETITION/audit_record.json","digest_algorithm":"git_blob_sha1","digest":"bfcbee0fd6174b8856b17c3d56ee320f27c18ec6"}:
        e.append("semantic record identity drift")
    subj = a.get("official_subject", {})
    for k, v in {
        "commit":"94bc0feb6a9ff12c7d31d6de640a725c9d43d2b6","tree":"174289e4d4958cb0509874e6e53400e098213de7","config_blob":"c7dd59e9df9ae5d90b35f76a9d958943d8e94770","challenge_blob":"8257e7726643a8f8c08c7e91584e003ab204c589","solution_blob":"887c4378f124a5d81a3f2624b6dc34867ec409c4"}.items():
        if subj.get(k) != v:
            e.append(f"formal subject drift: {k}")
    replay = a.get("replay", {})
    if (replay.get("run_id"), replay.get("job_id"), replay.get("result")) != (31945652355, 95161117041, "comparator_lean_kernel_nanoda_accept"):
        e.append("replay identity/result drift")
    if replay.get("permitted_axioms") != AXIOMS:
        e.append("axiom boundary drift")
    gate = r.get("semantic_gate", {})
    if gate.get("state") != "clear" or gate.get("disposition") != "SEMANTIC_AND_NONVACUITY_CLEAR_CURRENT_ROOT":
        e.append("semantic gate drift")
    if gate.get("activated_by_protected_merge") != "f0a40146cca7fd39c5724ed5be033ee9092625ac" or gate.get("forge_record_solve_handoff_authorized") is not False:
        e.append("semantic activation/authority drift")
    scope = r.get("target_scope", {})
    if scope.get("lean_theorems") != TARGETS:
        e.append("target inventory/order drift")
    if scope.get("classifications") != CLASSES:
        e.append("target classification drift")
    q = "\n".join(scope.get("mandatory_qualifications", []))
    for token in ("Independent finite Alice and Bob", "supremum", "exponent 13", "empty-answer extension", "whole-chapter"):
        if token not in q:
            e.append(f"mandatory qualification lost: {token}")
    if r.get("nonvacuity", {}).get("state") != "clear_on_declared_source_domain_with_empty_answer_extension_separated":
        e.append("nonvacuity state drift")
    adj = r.get("requested_adjudication", {})
    if (adj.get("route_id"), adj.get("current_route_state"), adj.get("cert_output"), adj.get("may_adjudicate_on_branch")) != ("MC-ROUTE-OTP-G-QUANTUM-PARALLEL-REPETITION", "not_registered", None, False):
        e.append("requested adjudication boundary drift")
    controls = r.get("route_controls", {})
    for k in ("historical_six_packet_registry_mutable","may_create_aggregate_handoff","may_imply_mathcert_acceptance","may_imply_adjudication","may_claim_mathematical_proof","may_promote_claim","whole_chapter_equivalence"):
        if controls.get(k) is not False:
            e.append(f"route/claim authority inflation: {k}")
    if controls.get("result_family_only") is not True:
        e.append("result-family isolation lost")
    boundary = r.get("claim_boundary", "")
    for token in ("exact two configured targets", "empty-answer", "historical six-packet registry", "aggregate OpenAI Ten Proofs", "MATHCERT route"):
        if token not in boundary:
            e.append(f"claim boundary lost: {token}")
    return e


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("validated OTP-G Quantum Parallel Repetition successor handoff candidate")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
