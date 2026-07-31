#!/usr/bin/env python3
from __future__ import annotations

import json
import pathlib
import sys
from typing import Any

WP_ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO_ROOT = WP_ROOT.parents[1]
RECORD_PATH = WP_ROOT / "candidate_admission.json"
SOURCE_LOCK_PATH = WP_ROOT.parent / "VGSE_WP00_VARCHENKO_GALASHIN_SOURCE_SEMANTICS_LOCK.md"
EXPECTED_REPLAY_PATH = WP_ROOT / "artifacts" / "data" / "expected_replay.json"

PROGRAMME_COMMIT = "d56edc23152f3ccde4c7db272b7af37f6cf698b9"
CANDIDATE_REGISTRY_DIGEST = "a6bffaa197aa3921e3eb9d4f8a02b5dc2bbded24"
RUNTIME_DIGEST = "02cdfabb04f5d273fcb7531c515a73baab2bc52d"
SOURCE_DIGEST = "e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de"
SOLVE_REVIEWED_HEAD = "0d66a75412543e534b81c21a51a6ad88c035b55b"
SOLVE_MERGE_COMMIT = "709c7d3f388b8df75c87a247f80424e560c31e72"
WORKFLOW_RUNS = {
    "solve_checks": 30641057206,
    "gcl_conformance": 30641058060,
    "candidate_replay": 30641057393,
}
GATE_NAMES = {
    "forge_provider_manifest_admitted",
    "source_revision_concordance_complete",
    "solve_candidate_package_reviewed",
    "cert_route_registered",
    "programme_active_registry_updated",
    "programme_routing_registry_updated",
    "runtime_contract_updated_for_active_admission",
    "intellect_repin_complete_if_required",
}


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def validation_errors(
    record: dict[str, Any] | None = None,
    *,
    source_lock: str | None = None,
    expected_replay: dict[str, Any] | None = None,
) -> list[str]:
    errors: list[str] = []
    if record is None:
        record = load_json(RECORD_PATH)
    if source_lock is None:
        source_lock = SOURCE_LOCK_PATH.read_text(encoding="utf-8")
    if expected_replay is None:
        expected_replay = load_json(EXPECTED_REPLAY_PATH)

    if record.get("campaign_id") != "VGSE-001":
        errors.append("candidate identity drift")
    if record.get("lifecycle_state") != "candidate":
        errors.append("VGSE-001 must remain candidate")
    if record.get("active_portfolio_member") is not False:
        errors.append("candidate leaked into active portfolio")

    authority = record.get("programme_authority", {})
    if authority.get("merge_commit") != PROGRAMME_COMMIT:
        errors.append("Programme merge identity drift")
    if authority.get("candidate_registry", {}).get("digest") != CANDIDATE_REGISTRY_DIGEST:
        errors.append("candidate registry identity drift")
    if authority.get("runtime_contract", {}).get("digest") != RUNTIME_DIGEST:
        errors.append("runtime contract identity drift")
    if authority.get("state_authority") != "protected_branch_repository_records":
        errors.append("protected repository authority required")
    if authority.get("github_issue_role") != "mutable_navigational_mirror":
        errors.append("GitHub issue must remain a navigational mirror")
    if authority.get("candidate_work_can_self_admit") is not False:
        errors.append("candidate work may not self-admit")

    mirrors = record.get("programme_mirrors", {})
    if mirrors != {
        "candidate_tracker_issue": 170,
        "current_governance_issue": 175,
        "governance_history": [172],
    }:
        errors.append("Programme candidate governance history drift")

    source = record.get("source_provenance", {})
    if source.get("state") != "unverified_candidate":
        errors.append("source provenance inflated beyond unverified candidate")
    if source.get("forge_issue") != 32:
        errors.append("Forge issue identity drift")
    if source.get("provider_manifest") is not None:
        errors.append("provider manifest claimed before admission")
    candidate_source = source.get("candidate_source", {})
    if candidate_source.get("candidate_sha256") != SOURCE_DIGEST:
        errors.append("candidate source digest drift")
    if candidate_source.get("candidate_byte_length") != 1317147:
        errors.append("candidate source byte length drift")

    solve = record.get("solve_candidate", {})
    if solve.get("issue") != 84 or solve.get("pull_request") != 85:
        errors.append("Solve candidate mirror identity drift")
    if solve.get("reviewed_head") != SOLVE_REVIEWED_HEAD:
        errors.append("Solve reviewed head identity drift")
    if solve.get("merge_commit") != SOLVE_MERGE_COMMIT:
        errors.append("Solve merge identity drift")
    if solve.get("merged_at") != "2026-07-31T15:04:53Z":
        errors.append("Solve merge timestamp drift")
    if solve.get("workflow_runs") != WORKFLOW_RUNS:
        errors.append("Solve candidate workflow evidence drift")
    if solve.get("state") != "merged_candidate_work_package":
        errors.append("Solve work must remain merged candidate work package")
    if solve.get("may_merge_candidate_work_package") is not False:
        errors.append("completed candidate merge may not remain future authority")
    for field in (
        "may_create_campaign_manifest",
        "may_create_cert_handoff",
        "may_create_adjudication",
        "may_create_promotion_record",
    ):
        if solve.get(field) is not False:
            errors.append(f"prohibited candidate authority in {field}")

    cert = record.get("certification_candidate", {})
    if cert.get("state") != "pre_route_candidate":
        errors.append("Cert state inflated beyond pre-route candidate")
    if cert.get("route_registry_entry") is not None:
        errors.append("Cert route claimed before registration")
    if cert.get("may_adjudicate") is not False:
        errors.append("pre-route candidate may not adjudicate")

    gates = record.get("admission_gates", {})
    if set(gates) != GATE_NAMES:
        errors.append("candidate admission gate set drift")
    if gates.get("solve_candidate_package_reviewed") is not True:
        errors.append("reviewed candidate package gate must remain true")
    for field in GATE_NAMES - {"solve_candidate_package_reviewed"}:
        if gates.get(field) is not False:
            errors.append(f"admission gate inflated before evidence: {field}")

    boundary = record.get("claim_boundary", {})
    if boundary.get("candidate_registered_not_admitted") is not True:
        errors.append("candidate non-admission boundary missing")
    for field, value in boundary.items():
        if field != "candidate_registered_not_admitted" and value is not False:
            errors.append(f"downstream claim inflation in {field}")

    legacy_digest = expected_replay.get("source", {}).get("author_pdf_sha256")
    if legacy_digest != SOURCE_DIGEST:
        errors.append("legacy report checksum drift")
    required_source_phrases = (
        "Current state: `unverified_candidate`",
        "The checksum is a candidate reproducibility lock. It is not provider verification.",
        "Protected candidate work package: merged",
        "no route exists",
    )
    for phrase in required_source_phrases:
        if phrase not in source_lock:
            errors.append(f"source lock missing boundary: {phrase}")

    forbidden_paths = (
        REPO_ROOT / "campaign_manifests" / "VGSE-001.json",
        REPO_ROOT / "cert_handoffs" / "VGSE-001.json",
    )
    for path in forbidden_paths:
        if path.exists():
            errors.append(f"candidate created forbidden authority artifact: {path.relative_to(REPO_ROOT)}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        "validated merged VGSE candidate work, unverified provenance, pre-route Cert state, "
        "and prohibition of active manifests, handoffs, adjudications, and promotion"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
