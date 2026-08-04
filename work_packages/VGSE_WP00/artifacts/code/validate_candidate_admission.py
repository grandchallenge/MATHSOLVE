#!/usr/bin/env python3
"""Validate the bounded VGSE activation state after Programme decision PR #217."""
from __future__ import annotations

import hashlib
import json
import pathlib
import sys
from typing import Any

WP_ROOT = pathlib.Path(__file__).resolve().parents[2]
REPO_ROOT = WP_ROOT.parents[1]
RECORD_PATH = WP_ROOT / "candidate_admission.json"
MANIFEST_PATH = REPO_ROOT / "campaign_manifests" / "VGSE-001.json"
HANDOFF_PATH = REPO_ROOT / "cert_handoffs" / "VGSE-001.json"
OVERLAY_PATH = REPO_ROOT / "contracts" / "mathcert_current_routes_vgse_overlay.json"
EXPECTED_REPLAY_PATH = WP_ROOT / "artifacts" / "data" / "expected_replay.json"

PROGRAMME_MERGE = "3e2c4148d4304b2446a84c1e9a414d4a976a0464"
PROGRAMME_DECISION_DIGEST = "a419d6832757ec2631e67d7f2b5f71d16e51f359"
CANDIDATE_REGISTRY_DIGEST = "5cd3f34f8cce130cd64dbea6aa8652d80783280b"
RUNTIME_DIGEST = "33cf79f38f1273a834bb43d4cc55bfc79ba2c5e0"
AUTHOR_SOURCE_DIGEST = "e513789426ae6247438920bfc80cfba6bd9c32dc6799a4f7873d806a865f95de"
ARXIV_SOURCE_DIGEST = "f5aefb71dd0d662679e85cd0c7f96d1bbbc029a6b5cd2f1cfaa06286cc718e34"
NORMALIZED_TEXT_DIGEST = "74d58d4465166fc5035e5064a2c1cabc8b0f1e62cdcf82f7b41c6af65492cba4"
PROVIDER_MANIFEST_DIGEST = "9cb5ac2d92b458f7f63e8a9811448f245a151ddd"
SOURCE_CONCORDANCE_DIGEST = "6685cd1b0ed4d759f7447fce4b217ef8a59f0f93"
SOLVE_REVIEWED_HEAD = "0d66a75412543e534b81c21a51a6ad88c035b55b"
SOLVE_MERGE = "709c7d3f388b8df75c87a247f80424e560c31e72"
MANIFEST_DIGEST = "3bb6b18052f5754e9ae9aa4f813d9b43dcd4e3b4"
HANDOFF_DIGEST = "42cfa84978fd63c75f074b388afd8b1fcbd56091"
OVERLAY_DIGEST = "3ca77c89c3d199d1632feedc0f9ad3bfe1f66d31"

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
COMPLETED_GATES = {
    "forge_provider_manifest_admitted",
    "source_revision_concordance_complete",
    "solve_candidate_package_reviewed",
}


def load_json(path: pathlib.Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: pathlib.Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload,
        usedforsecurity=False,
    ).hexdigest()


def _artifact_errors(
    artifact: dict[str, Any],
    *,
    expected_path: str,
    expected_digest: str,
    label: str,
    local_path: pathlib.Path | None = None,
) -> list[str]:
    errors: list[str] = []
    if artifact.get("path") != expected_path:
        errors.append(f"{label} path drift")
    if artifact.get("digest_algorithm") != "git_blob_sha1":
        errors.append(f"{label} digest algorithm drift")
    if artifact.get("digest") != expected_digest:
        errors.append(f"{label} identity drift")
    if local_path is not None:
        if not local_path.is_file():
            errors.append(f"{label} local artifact missing")
        elif git_blob_sha1(local_path) != expected_digest:
            errors.append(f"{label} local Git blob identity drift")
    return errors


def validation_errors(
    record: dict[str, Any] | None = None,
    *,
    manifest: dict[str, Any] | None = None,
    handoff: dict[str, Any] | None = None,
    overlay: dict[str, Any] | None = None,
    expected_replay: dict[str, Any] | None = None,
    verify_local_blobs: bool = True,
) -> list[str]:
    errors: list[str] = []
    if record is None:
        record = load_json(RECORD_PATH)
    if manifest is None:
        manifest = load_json(MANIFEST_PATH)
    if handoff is None:
        handoff = load_json(HANDOFF_PATH)
    if overlay is None:
        overlay = load_json(OVERLAY_PATH)
    if expected_replay is None:
        expected_replay = load_json(EXPECTED_REPLAY_PATH)

    if record.get("campaign_id") != "VGSE-001":
        errors.append("candidate identity drift")
    if record.get("lifecycle_state") != "candidate":
        errors.append("VGSE-001 must remain candidate pending cross-repository activation")
    if record.get("active_portfolio_member") is not False:
        errors.append("candidate leaked into active Programme portfolio")

    authority = record.get("programme_authority", {})
    if authority.get("merge_commit") != PROGRAMME_MERGE:
        errors.append("Programme bounded-admission merge identity drift")
    decision = authority.get("decision", {})
    if decision.get("decision") != "ADMIT_BOUNDED_PENDING_CROSS_REPOSITORY_ACTIVATION":
        errors.append("Programme bounded-admission disposition drift")
    errors.extend(_artifact_errors(
        decision,
        expected_path="governance/vgse_bounded_admission_decision.json",
        expected_digest=PROGRAMME_DECISION_DIGEST,
        label="Programme decision",
    ))
    errors.extend(_artifact_errors(
        authority.get("candidate_registry", {}),
        expected_path="governance/campaign_admission_registry.json",
        expected_digest=CANDIDATE_REGISTRY_DIGEST,
        label="candidate registry",
    ))
    errors.extend(_artifact_errors(
        authority.get("runtime_contract", {}),
        expected_path="governance/umbrella_runtime_contract_v4.json",
        expected_digest=RUNTIME_DIGEST,
        label="runtime contract",
    ))
    if authority.get("state_authority") != "protected_branch_repository_records":
        errors.append("protected repository authority required")
    if authority.get("github_issue_role") != "mutable_navigational_mirror":
        errors.append("GitHub issue must remain a navigational mirror")
    if authority.get("candidate_work_can_self_admit") is not False:
        errors.append("candidate work may not self-admit")

    source = record.get("source_provenance", {})
    if source.get("state") != "provider_verified":
        errors.append("provider-verified source state rolled back or inflated")
    if source.get("forge_repository") != "grandchallenge/MATHFORGE" or source.get("forge_issue") != 32:
        errors.append("Forge provider identity drift")
    provider = source.get("provider_manifest", {})
    if provider.get("commit_sha") != "593afd971a53ca0285f8b94570997ed7c3d7c170":
        errors.append("Forge provider merge identity drift")
    errors.extend(_artifact_errors(
        provider,
        expected_path="provider_manifests/VGSE-001.json",
        expected_digest=PROVIDER_MANIFEST_DIGEST,
        label="Forge provider manifest",
    ))
    concordance = source.get("source_concordance", {})
    if concordance.get("commit_sha") != "593afd971a53ca0285f8b94570997ed7c3d7c170":
        errors.append("Forge source-concordance merge identity drift")
    errors.extend(_artifact_errors(
        concordance,
        expected_path="sources/VGSE-001/source_revision_concordance.json",
        expected_digest=SOURCE_CONCORDANCE_DIGEST,
        label="Forge source concordance",
    ))
    candidate_source = source.get("candidate_source", {})
    expected_source = {
        "author": "Pavel Galashin",
        "title": "Amplituhedra and Origami, I: Tree Level",
        "author_pdf_sha256": AUTHOR_SOURCE_DIGEST,
        "arxiv_v2_sha256": ARXIV_SOURCE_DIGEST,
        "normalized_text_sha256": NORMALIZED_TEXT_DIGEST,
    }
    if candidate_source != expected_source:
        errors.append("provider source identity or revision-concordance drift")

    solve = record.get("solve_candidate", {})
    if solve.get("issue") != 84 or solve.get("pull_request") != 85:
        errors.append("Solve candidate mirror identity drift")
    if solve.get("reviewed_head") != SOLVE_REVIEWED_HEAD:
        errors.append("Solve reviewed head identity drift")
    if solve.get("merge_commit") != SOLVE_MERGE:
        errors.append("Solve merge identity drift")
    if solve.get("state") != "merged_candidate_work_package":
        errors.append("Solve work must remain merged candidate work package")
    for field in (
        "may_merge_candidate_work_package",
        "may_create_campaign_manifest",
        "may_create_cert_handoff",
        "may_create_adjudication",
        "may_create_promotion_record",
    ):
        if solve.get(field) is not False:
            errors.append(f"obsolete candidate authority retained in {field}")

    activation = record.get("activation_artifacts", {})
    if activation.get("state") != "prepared_pending_protected_merge":
        errors.append("Solve activation state drift")
    errors.extend(_artifact_errors(
        activation.get("campaign_manifest", {}),
        expected_path="campaign_manifests/VGSE-001.json",
        expected_digest=MANIFEST_DIGEST,
        label="VGSE campaign manifest",
        local_path=MANIFEST_PATH if verify_local_blobs else None,
    ))
    errors.extend(_artifact_errors(
        activation.get("cert_handoff", {}),
        expected_path="cert_handoffs/VGSE-001.json",
        expected_digest=HANDOFF_DIGEST,
        label="VGSE Cert handoff",
        local_path=HANDOFF_PATH if verify_local_blobs else None,
    ))
    if activation.get("cert_handoff", {}).get("status") != "pending":
        errors.append("VGSE Cert handoff must remain pending")
    errors.extend(_artifact_errors(
        activation.get("current_route_overlay", {}),
        expected_path="contracts/mathcert_current_routes_vgse_overlay.json",
        expected_digest=OVERLAY_DIGEST,
        label="VGSE current-route overlay",
        local_path=OVERLAY_PATH if verify_local_blobs else None,
    ))
    if activation.get("current_route_overlay", {}).get("route_registry_entry_present") is not False:
        errors.append("MATHCERT route claimed before protected registration")

    if manifest.get("campaign_id") != "VGSE-001" or manifest.get("coverage_mode") != "native":
        errors.append("VGSE native campaign manifest identity drift")
    if manifest.get("programme", {}).get("commit_sha") != PROGRAMME_MERGE:
        errors.append("manifest Programme decision identity drift")
    if manifest.get("certification", {}).get("handoff_state") != "pending":
        errors.append("manifest handoff state inflated before route registration")
    if manifest.get("promotion", {}).get("eligible") is not False:
        errors.append("manifest cannot become promotion eligible before adjudication")

    if handoff.get("handoff_id") != "MC-HANDOFF-VGSE-001":
        errors.append("VGSE handoff identity drift")
    if handoff.get("status") != "pending" or not handoff.get("blockers"):
        errors.append("VGSE handoff must remain blocked and pending")
    if handoff.get("cert_contract", {}).get("route_id") != "MC-ROUTE-VGSE-001":
        errors.append("proposed MATHCERT route identity drift")
    claim_ids = [item.get("claim_id") for item in handoff.get("target_claims", [])]
    if claim_ids != ["VGSE-C00", "VGSE-C01", "VGSE-C04", "VGSE-C05", "VGSE-C06"]:
        errors.append("bounded handoff target set drift")

    overlay_campaign = overlay.get("campaign", {})
    if overlay_campaign.get("campaign_id") != "VGSE-001":
        errors.append("current-route overlay campaign identity drift")
    if overlay_campaign.get("route_registry_entry_present") is not False:
        errors.append("current-route overlay claims absent route as registered")
    if overlay_campaign.get("handoff_state") != "pending" or overlay_campaign.get("route_state") != "pending":
        errors.append("current-route overlay state inflated before route registration")
    for field in ("mathematical_target_proved", "may_adjudicate", "may_issue_certificate_output"):
        if overlay_campaign.get(field) is not False:
            errors.append(f"current-route authority inflation in {field}")
    if overlay_campaign.get("cert_output") is not None or overlay_campaign.get("qualification_scope") is not None:
        errors.append("pending current-route overlay cannot carry output or qualification")

    cert = record.get("certification_candidate", {})
    if cert.get("state") != "handoff_prepared_route_pending":
        errors.append("Cert state must remain handoff-prepared and route-pending")
    if cert.get("route_id") != "MC-ROUTE-VGSE-001" or cert.get("route_registry_entry") is not None:
        errors.append("Cert route registration state drift")
    if cert.get("may_adjudicate") is not False or cert.get("may_issue_certificate_output") is not False:
        errors.append("pending Cert route may not adjudicate or issue output")

    gates = record.get("admission_gates", {})
    if set(gates) != GATE_NAMES:
        errors.append("candidate admission gate set drift")
    for field in GATE_NAMES:
        expected = field in COMPLETED_GATES
        if gates.get(field) is not expected:
            errors.append(f"candidate admission gate drift: {field}")

    scope = record.get("bounded_candidate_scope", {})
    for field in (
        "source_and_semantics_lock",
        "exact_arrangement_replay",
        "numerical_algebraic_witness_replay",
        "source_vector_geometry_replication",
        "numerical_weighted_graph_replay",
        "numerical_t_embedding_reconstruction",
        "active_campaign_manifest_created",
        "cert_handoff_created",
    ):
        if scope.get(field) is not True:
            errors.append(f"completed bounded scope rolled back: {field}")
    for field in ("cert_route_created", "adjudication_created", "promotion_record_created"):
        if scope.get(field) is not False:
            errors.append(f"unauthorized bounded scope inflation: {field}")

    boundary = record.get("claim_boundary", {})
    if boundary.get("candidate_registered_not_admitted") is not True:
        errors.append("candidate non-admission boundary missing")
    if boundary.get("source_verified") is not True:
        errors.append("provider source verification state missing")
    for field, value in boundary.items():
        if field not in {"candidate_registered_not_admitted", "source_verified"} and value is not False:
            errors.append(f"downstream claim inflation in {field}")

    if expected_replay.get("source", {}).get("author_pdf_sha256") != AUTHOR_SOURCE_DIGEST:
        errors.append("legacy replay source checksum drift")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        "validated provider-verified VGSE candidate, bounded Solve manifest and pending handoff, "
        "absent MATHCERT route, and closed adjudication and promotion boundaries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
