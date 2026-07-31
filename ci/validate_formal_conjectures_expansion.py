#!/usr/bin/env python3
"""Validate the MS-FC-GOV-001 / MS-FC-WP01 admission and routing contract."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "contracts" / "formal_conjectures_expanded_evidence.json"
ROUTE_PATH = ROOT / "formal_sources" / "formal_conjectures" / "MS-FC-WP01.json"
MANIFEST_DIR = ROOT / "campaign_manifests"
HANDOFF_DIR = ROOT / "cert_handoffs"

AFFECTED = {"UC-001", "PNP-001", "OZ-001", "BSD-001", "HC-001", "YM-001"}
PILOT = {"RH-001", "NS-CI-001"}
EXPECTED_DISPOSITIONS = {
    "UC-001": ("statement-correspondence", "formulation-concordance-only"),
    "PNP-001": ("definition-audit", "blocked-pending-definition-concordance"),
    "OZ-001": ("theorem-lattice", "eight-scopes-preserved"),
    "BSD-001": ("explicit-non-route", "adjacency-only"),
    "HC-001": ("explicit-non-route", "bounded-negative-source-screen"),
    "YM-001": ("explicit-non-route", "lexical-false-positive"),
}
EXPECTED_OZ_SCOPES = [
    "zeta3",
    "zeta5",
    "zeta7",
    "zeta9",
    "zeta11",
    "universal-odd-irrationality",
    "odd-value-infinitude",
    "finite-zudilin-disjunction",
]
EXPECTED_OZ_PROGRAMME_PATHS = {
    "campaigns/odd_zeta/OZ_WP00_SOURCE_NORMALIZATION_EQUIVALENCE/09_QUALIFIED_CLOSURE_OZ_NEXT_006.md",
    "campaigns/odd_zeta/OZ_WP01_FALSE_PROOF_ATLAS/ATLAS.yaml",
    "campaigns/odd_zeta/OZ_WP02_THEOREM_OBLIGATION_LEDGER/THEOREM_LEDGER.yaml",
    "campaigns/odd_zeta/OZ_RT_APERY_BROW_001/README.md",
    "campaigns/odd_zeta/OZ_RT_LB_INSTANCE_001/README.md",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def artifact_key(record: dict[str, Any]) -> tuple[str, str, str, str, str, str]:
    return (
        str(record.get("repository", "")),
        str(record.get("commit_sha", "")),
        str(record.get("path", "")),
        str(record.get("digest_algorithm", "")),
        str(record.get("digest", "")),
        str(record.get("role", "")),
    )


def expected_provider_keys(contract: dict[str, Any], campaign_id: str) -> set[tuple[str, str, str, str, str, str]]:
    records = list(contract["common_artifacts"]) + list(contract["campaigns"][campaign_id]["artifacts"])
    return {artifact_key(item) for item in records}


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    contract_path = root / CONTRACT_PATH.relative_to(ROOT)
    route_path = root / ROUTE_PATH.relative_to(ROOT)
    manifest_dir = root / MANIFEST_DIR.relative_to(ROOT)
    handoff_dir = root / HANDOFF_DIR.relative_to(ROOT)

    try:
        contract = load_json(contract_path)
        route = load_json(route_path)
    except (OSError, json.JSONDecodeError) as exc:
        return [f"formal-conjectures contract load failed: {exc}"]

    programme = contract.get("programme_admission", {})
    provider = contract.get("provider", {})
    programme_commit = str(programme.get("commit_sha", ""))
    provider_commit = str(provider.get("commit_sha", ""))

    if contract.get("contract_id") != "MS-FC-GOV-001":
        errors.append("contract_id must be MS-FC-GOV-001")
    if programme_commit != "aafd5d5d18989d4ac246de8f6dd2455f02614307":
        errors.append("Programme admission commit drift")
    if programme.get("digest") != "3b796157324eeb925051efee78795a2ad1bcb2b5":
        errors.append("Programme admission registry blob drift")
    if provider_commit != "0faee396ffa56c568ee0ae6a348bdb43ca80ac4d":
        errors.append("MATHFORGE provider commit drift")
    if provider.get("source_id") != "FC-GDM-002":
        errors.append("expanded source_id must be FC-GDM-002")

    replay = provider.get("replay", {})
    replay_expected = {
        "workflow_run_id": 30544600547,
        "artifact_id": 8761186970,
        "archive_sha256": "1c74747519c17f873f323198a92104538667092f3274a667a09e1a6b219a7bcb",
        "snapshot_sha256": "e7534f913160cc9cef4eb80a735c44b7b1a8ea4273f0f5236d82cc7b9dab042b",
        "snapshot_canonical_sha256": "2b6bda841d15b022ec8c66bc332177d1283ca791f5d5f6e82323c304d1e6fdf6",
        "snapshot_byte_length": 52589,
        "statement_count": 43,
        "inventory_sha256": "2693de3b83c0990b0e7c62ab5032698c6dde6de0942441ba7d6cdb035625e687",
        "inventory_byte_length": 1255363,
        "problem_count": 3232,
    }
    for key, expected in replay_expected.items():
        if replay.get(key) != expected:
            errors.append(f"replay identity drift: {key}")

    campaign_contracts = contract.get("campaigns", {})
    if set(campaign_contracts) != AFFECTED:
        errors.append("contract must cover exactly the six affected campaigns")

    expected_states = contract.get("certification_states", {})
    if set(expected_states) != AFFECTED | PILOT:
        errors.append("certification-state lock must cover all eight campaigns")

    manifests: dict[str, dict[str, Any]] = {}
    for path in sorted(manifest_dir.glob("*.json")):
        try:
            manifest = load_json(path)
        except json.JSONDecodeError as exc:
            errors.append(f"{path}: invalid JSON: {exc}")
            continue
        campaign_id = str(manifest.get("campaign_id", ""))
        manifests[campaign_id] = manifest

    if set(manifests) != AFFECTED | PILOT:
        errors.append("manifest replay must cover exactly the eight governed campaigns")

    for campaign_id, expected_state in expected_states.items():
        manifest = manifests.get(campaign_id)
        if not manifest:
            continue
        certification = manifest.get("certification", {})
        if certification.get("handoff_state") != expected_state:
            errors.append(f"{campaign_id}: MATHCERT aggregate state changed")
        packet_statuses = {
            str(item.get("status", ""))
            for item in certification.get("handoff_packets", [])
            if isinstance(item, dict)
        }
        if packet_statuses != {expected_state}:
            errors.append(f"{campaign_id}: manifest packet state changed")
        packet_path = handoff_dir / f"{campaign_id}.json"
        if not packet_path.exists():
            errors.append(f"{campaign_id}: MATHCERT handoff packet missing")
        else:
            packet = load_json(packet_path)
            if packet.get("status") != expected_state:
                errors.append(f"{campaign_id}: MATHCERT handoff file state changed")

    for campaign_id in AFFECTED:
        manifest = manifests.get(campaign_id)
        if not manifest:
            continue
        campaign_contract = campaign_contracts[campaign_id]
        if manifest.get("coverage_mode") != campaign_contract.get("coverage_mode"):
            errors.append(f"{campaign_id}: coverage mode drift")
        if manifest.get("programme", {}).get("commit_sha") != programme_commit:
            errors.append(f"{campaign_id}: Programme admission commit is not pinned")

        forge_inputs = manifest.get("forge_inputs", [])
        if not isinstance(forge_inputs, list):
            errors.append(f"{campaign_id}: forge_inputs must be an array")
            continue
        keys = [artifact_key(item) for item in forge_inputs if isinstance(item, dict)]
        if len(keys) != len(set(keys)):
            errors.append(f"{campaign_id}: duplicate provider artifact reference")
        if not any(key[2] == f"provider_manifests/{campaign_id}.json" for key in keys):
            errors.append(f"{campaign_id}: historical provider manifest lineage was removed")

        actual_expanded = {key for key in keys if key[1] == provider_commit}
        expected_expanded = expected_provider_keys(contract, campaign_id)
        if actual_expanded != expected_expanded:
            missing = sorted(expected_expanded - actual_expanded)
            extra = sorted(actual_expanded - expected_expanded)
            if missing:
                errors.append(f"{campaign_id}: incomplete FC-GDM-002 evidence: {missing}")
            if extra:
                errors.append(f"{campaign_id}: unregistered FC-GDM-002 evidence: {extra}")

    for campaign_id in PILOT:
        manifest = manifests.get(campaign_id)
        if not manifest:
            continue
        if any(str(item.get("commit_sha", "")) == provider_commit for item in manifest.get("forge_inputs", [])):
            errors.append(f"{campaign_id}: FC-GDM-002 contaminated the unchanged pilot lane")

    routes = route.get("routes", [])
    route_by_campaign = {
        str(item.get("campaign_id", "")): item
        for item in routes
        if isinstance(item, dict)
    }
    if set(route_by_campaign) != AFFECTED:
        errors.append("MS-FC-WP01 must route exactly the six affected campaigns")
    for campaign_id, (route_class, disposition) in EXPECTED_DISPOSITIONS.items():
        item = route_by_campaign.get(campaign_id, {})
        if item.get("route_class") != route_class:
            errors.append(f"{campaign_id}: route class drift")
        if item.get("disposition") != disposition:
            errors.append(f"{campaign_id}: route disposition drift")
    if route_by_campaign.get("OZ-001", {}).get("scopes") != EXPECTED_OZ_SCOPES:
        errors.append("OZ-001: eight theorem scopes are incomplete, reordered, or collapsed")
    for campaign_id in ("BSD-001", "HC-001", "YM-001"):
        if route_by_campaign.get(campaign_id, {}).get("route_class") != "explicit-non-route":
            errors.append(f"{campaign_id}: explicit non-route was promoted")

    pilot = route.get("pilot_lane", {})
    if pilot.get("source_id") != "FC-GDM-001" or pilot.get("disposition") != "unchanged":
        errors.append("RH/NS pilot lane scope drift")
    if set(pilot.get("campaigns", [])) != PILOT:
        errors.append("RH/NS pilot lane campaign set drift")
    if route.get("certification_effect", {}).get("states") != expected_states:
        errors.append("route ledger certification states drift from contract")

    oz = manifests.get("OZ-001", {})
    work_packages = oz.get("work_packages", [])
    if len(work_packages) != 1 or work_packages[0].get("work_package_id") != "OZ-WP00-LB-INSTANCE-RETROSPECTIVE":
        errors.append("OZ-001: stale retrospective work-package identity")
    elif work_packages:
        wp = work_packages[0]
        if wp.get("status") != "active" or wp.get("source_commit") != programme_commit:
            errors.append("OZ-001: retrospective package status or Programme commit is stale")
        paths = {str(item.get("path", "")) for item in wp.get("artifacts", [])}
        if paths != EXPECTED_OZ_PROGRAMME_PATHS:
            errors.append("OZ-001: completed Programme stage artifact set is incomplete or drifted")
        ledgers = wp.get("ledgers", {})
        if ledgers.get("claim", {}).get("path") != "campaigns/odd_zeta/OZ_WP02_THEOREM_OBLIGATION_LEDGER/THEOREM_LEDGER.yaml":
            errors.append("OZ-001: theorem ledger is not current")
        if ledgers.get("proof_obligation", {}).get("path") != "campaigns/odd_zeta/OZ_WP02_THEOREM_OBLIGATION_LEDGER/PROOF_OBLIGATIONS.yaml":
            errors.append("OZ-001: proof-obligation ledger is not current")
    migration_text = "\n".join(oz.get("solve", {}).get("migration_debt", []))
    blocker_text = "\n".join(oz.get("promotion", {}).get("blockers", []))
    if "OZ-RT-BZ-T3-001" not in migration_text:
        errors.append("OZ-001: next active T3 migration obligation is missing")
    if "T3 remains open" not in blocker_text or "Sharp-12" not in blocker_text:
        errors.append("OZ-001: current T3 and Sharp-12 blockers are not preserved")
    if route.get("oz_reconciliation", {}).get("next_active_obligation") != "OZ-RT-BZ-T3-001":
        errors.append("OZ route ledger points to a stale next obligation")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Formal Conjectures expansion validated: six reconciled campaigns, two unchanged pilot campaigns, eight unchanged MATHCERT states.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
