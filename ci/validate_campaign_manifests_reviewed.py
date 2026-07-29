#!/usr/bin/env python3
"""Reviewed MATHSOLVE campaign, packet, and MATHCERT gate validation."""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Iterable

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "campaign_manifests"
HANDOFF_DIR = ROOT / "cert_handoffs"
MANIFEST_SCHEMA_PATH = ROOT / "schemas" / "campaign_manifest.schema.json"
HANDOFF_SCHEMA_PATH = ROOT / "schemas" / "mathcert_handoff.schema.json"
HANDOFF_TEMPLATE_PATH = ROOT / "templates" / "mathcert_handoff.json"
REFERENCE_REGISTRY_PATH = ROOT / "contracts" / "programme_reference_registry.json"
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
COMPUTATIONAL_TYPES = {
    "EXACT_COMPUTATIONAL_SCREEN",
    "ALGEBRAIC_GEOMETRY_CAMPAIGN",
    "INTERVAL_CERTIFICATION_CAMPAIGN",
    "COUNTEREXAMPLE_SEARCH",
}
INTAKE_STATES = {"pending", "ready", "submitted"}
ADJUDICATED_STATES = {"certified", "qualified", "rejected", "proof_debt"}
POSITIVE_STATES = {"certified", "qualified"}
EXPECTED_CERT_CONTRACT = {
    "repository": "grandchallenge/MATHCERT",
    "commit_sha": "3854dd1b4f6e162a7e74c3da1993f022ee691e5e",
    "path": "governance/certification_routes.json",
    "digest_algorithm": "git_blob_sha1",
    "digest": "065f0531e4d763b389b207d4922d5a85b4335ee3",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def expected_campaigns() -> set[str]:
    registry = load_json(REFERENCE_REGISTRY_PATH)
    campaigns = registry.get("campaigns", {})
    if not isinstance(campaigns, dict) or not campaigns:
        raise ValueError("programme reference registry contains no campaigns")
    return {str(campaign_id) for campaign_id in campaigns}


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload,
        usedforsecurity=False,
    ).hexdigest()


def schema_errors(instance: dict[str, Any], schema: dict[str, Any], label: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def artifact_errors(artifact: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    algorithm = artifact.get("digest_algorithm")
    digest = str(artifact.get("digest", ""))
    commit = str(artifact.get("commit_sha", ""))
    path = str(artifact.get("path", ""))
    if algorithm in {"git_blob_sha1", "git_tree_sha1"} and not HEX40.fullmatch(digest):
        errors.append(f"{label}: {algorithm} digest must be 40 lowercase hexadecimal characters")
    if algorithm == "sha256" and not HEX64.fullmatch(digest):
        errors.append(f"{label}: sha256 digest must be 64 lowercase hexadecimal characters")
    if algorithm in {"git_blob_sha1", "git_tree_sha1"} and digest == commit:
        errors.append(f"{label}: repository commit cannot substitute for artifact digest")
    if path == ".":
        errors.append(f"{label}: repository root is not an artifact locator")
    if artifact.get("repository") == "grandchallenge/MATHSOLVE":
        local_path = ROOT / path
        if not local_path.exists():
            errors.append(f"{label}: local MATHSOLVE artifact is missing: {path}")
        elif algorithm == "git_blob_sha1":
            if not local_path.is_file():
                errors.append(f"{label}: git_blob_sha1 requires a file: {path}")
            elif git_blob_sha1(local_path) != digest:
                errors.append(f"{label}: Git blob identity drift for {path}")
        elif algorithm == "sha256" and local_path.is_file():
            if hashlib.sha256(local_path.read_bytes()).hexdigest() != digest:
                errors.append(f"{label}: SHA-256 identity drift for {path}")
    return errors


def walk_work_packages(items: Iterable[dict[str, Any]], prefix: str = ""):
    for index, item in enumerate(items):
        label = f"{prefix}work_packages[{index}]"
        yield label, item
        yield from walk_work_packages(item.get("children", []), prefix=label + ".")


def mathcert_handoff_errors(template_path: Path = HANDOFF_TEMPLATE_PATH) -> list[str]:
    schema = load_json(HANDOFF_SCHEMA_PATH)
    instance = load_json(template_path)
    errors = schema_errors(instance, schema, str(template_path))
    for name in ("claim_ledger", "proof_obligations"):
        artifact = instance.get(name)
        if isinstance(artifact, dict):
            errors.extend(artifact_errors(artifact, f"{template_path}: {name}"))
    return errors


def handoff_packet_errors(directory: Path = HANDOFF_DIR) -> list[str]:
    schema = load_json(HANDOFF_SCHEMA_PATH)
    paths = sorted(directory.glob("*.json"))
    errors: list[str] = []
    ids: list[str] = []
    campaigns: list[str] = []
    for path in paths:
        packet = load_json(path)
        errors.extend(schema_errors(packet, schema, str(path)))
        campaign_id = str(packet.get("campaign_id", ""))
        handoff_id = str(packet.get("handoff_id", ""))
        campaigns.append(campaign_id)
        ids.append(handoff_id)
        if path.name != f"{campaign_id}.json":
            errors.append(f"{path}: filename must equal campaign_id")
        if handoff_id != f"MC-HANDOFF-{campaign_id}":
            errors.append(f"{path}: handoff_id is not canonical")
        expected_route = f"MC-ROUTE-{campaign_id}"
        contract = packet.get("cert_contract", {})
        for key, expected in EXPECTED_CERT_CONTRACT.items():
            if contract.get(key) != expected:
                errors.append(f"{path}: Cert contract {key} drift; expected {expected}")
        if contract.get("route_id") != expected_route:
            errors.append(f"{path}: Cert route identity drift; expected {expected_route}")
        for name in ("claim_ledger", "proof_obligations"):
            artifact = packet.get(name)
            if isinstance(artifact, dict):
                errors.extend(artifact_errors(artifact, f"{path}: {name}"))
        claims = packet.get("target_claims", [])
        claim_ids = [str(item.get("claim_id", "")) for item in claims if isinstance(item, dict)]
        if len(claim_ids) != len(set(claim_ids)):
            errors.append(f"{path}: duplicate target claim IDs")
        if packet.get("status") == "pending" and not packet.get("blockers"):
            errors.append(f"{path}: pending packet must identify blockers")
    for duplicate in sorted({item for item in ids if ids.count(item) > 1}):
        errors.append(f"MATHCERT handoffs: duplicate handoff_id {duplicate}")
    for duplicate in sorted({item for item in campaigns if campaigns.count(item) > 1}):
        errors.append(f"MATHCERT handoffs: duplicate campaign_id {duplicate}")
    actual = set(campaigns)
    expected = expected_campaigns()
    for missing in sorted(expected - actual):
        errors.append(f"MATHCERT handoffs: governed campaign is uncovered: {missing}")
    for unknown in sorted(actual - expected):
        errors.append(f"MATHCERT handoffs: unregistered campaign: {unknown}")
    return errors


def manifest_errors(path: Path, instance: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    errors = schema_errors(instance, schema, str(path))
    campaign_id = str(instance.get("campaign_id", ""))
    if path.name != f"{campaign_id}.json":
        errors.append(f"{path}: filename must equal campaign_id")
    coverage = instance.get("coverage_mode")
    migration_debt = instance.get("solve", {}).get("migration_debt", [])
    if coverage == "native" and migration_debt:
        errors.append(f"{path}: native coverage must not claim retrospective migration debt")
    if coverage == "retrospective" and not migration_debt:
        errors.append(f"{path}: retrospective coverage requires migration debt")

    packet_by_id: dict[str, dict[str, Any]] = {}
    certification = instance.get("certification", {})
    contract = certification.get("contract", {})
    if contract != EXPECTED_CERT_CONTRACT:
        errors.append(f"{path}: certification contract identity does not match MATHCERT#31")
    for index, packet_ref in enumerate(certification.get("handoff_packets", [])):
        artifact = packet_ref.get("artifact", {}) if isinstance(packet_ref, dict) else {}
        if isinstance(artifact, dict):
            errors.extend(artifact_errors(artifact, f"{path}: certification.handoff_packets[{index}].artifact"))
        packet_path = ROOT / str(artifact.get("path", ""))
        if packet_path.exists():
            packet = load_json(packet_path)
            packet_by_id[str(packet.get("handoff_id", ""))] = packet
            if packet_ref.get("handoff_id") != packet.get("handoff_id"):
                errors.append(f"{path}: packet handoff_id does not match referenced artifact")
            if packet_ref.get("status") != packet.get("status"):
                errors.append(f"{path}: packet status does not match referenced artifact")
            actual_claims = [item.get("claim_id") for item in packet.get("target_claims", [])]
            if packet_ref.get("target_claim_ids") != actual_claims:
                errors.append(f"{path}: packet target_claim_ids do not match referenced artifact")
            if packet.get("campaign_id") != campaign_id:
                errors.append(f"{path}: packet campaign_id does not match manifest")

    work_package_ids: set[str] = set()
    certification_ledger_paths: list[str] = []
    for label, wp in walk_work_packages(instance.get("work_packages", [])):
        wp_id = str(wp.get("work_package_id", ""))
        if wp_id in work_package_ids:
            errors.append(f"{path}: duplicate recursive work_package_id {wp_id}")
        work_package_ids.add(wp_id)
        if coverage == "native" and wp.get("source_repository") != "grandchallenge/MATHSOLVE":
            errors.append(f"{path}: {label}: native work must be sourced from MATHSOLVE")
        if coverage == "retrospective" and wp.get("source_repository") == "grandchallenge/MATHSOLVE":
            errors.append(f"{path}: {label}: retrospective work must preserve its historical source repository")
        for index, artifact in enumerate(wp.get("artifacts", [])):
            if isinstance(artifact, dict):
                errors.extend(artifact_errors(artifact, f"{path}: {label}.artifacts[{index}]"))
        ledgers = wp.get("ledgers", {})
        ledger_paths: list[str] = []
        expected_roles = {
            "claim": "claim_ledger",
            "proof_obligation": "proof_obligation_dag",
            "failed_route": "failed_route_ledger",
            "resource": "resource_ledger",
            "certification": "certificate_handoff",
        }
        for name, role in expected_roles.items():
            artifact = ledgers.get(name)
            if isinstance(artifact, dict):
                errors.extend(artifact_errors(artifact, f"{path}: {label}.ledgers.{name}"))
                ledger_paths.append(str(artifact.get("path", "")))
                if artifact.get("role") != role:
                    errors.append(f"{path}: {label}.ledgers.{name} must have role {role}")
                if name == "certification":
                    certification_ledger_paths.append(str(artifact.get("path", "")))
        for duplicate in sorted({item for item in ledger_paths if ledger_paths.count(item) > 1}):
            errors.append(f"{path}: {label}: distinct ledger roles share artifact path {duplicate}")
        if wp.get("primary_type") in COMPUTATIONAL_TYPES:
            if not isinstance(ledgers.get("failed_route"), dict):
                errors.append(f"{path}: {label}: computational package requires failed-route ledger")
            if not isinstance(ledgers.get("resource"), dict):
                errors.append(f"{path}: {label}: computational package requires resource ledger")

    packet_paths = [
        str(item.get("artifact", {}).get("path", ""))
        for item in certification.get("handoff_packets", [])
        if isinstance(item, dict)
    ]
    if sorted(packet_paths) != sorted(certification_ledger_paths):
        errors.append(f"{path}: work-package certification ledgers must equal manifest packet artifacts")

    state = certification.get("handoff_state")
    statuses = {str(packet.get("status", "")) for packet in packet_by_id.values()}
    if not packet_by_id:
        errors.append(f"{path}: certification coverage requires a content-addressed packet")
    elif statuses != {state}:
        errors.append(f"{path}: aggregate handoff state must equal every packet status")

    promotion = instance.get("promotion", {})
    if promotion.get("eligible") is True:
        if promotion.get("blockers"):
            errors.append(f"{path}: promotion-eligible manifest must have no blockers")
        if state not in POSITIVE_STATES:
            errors.append(f"{path}: promotion eligibility requires certified or qualified MATHCERT state")
    elif not promotion.get("blockers"):
        errors.append(f"{path}: blocked promotion must identify at least one blocker")
    return errors


def campaign_manifest_errors(directory: Path = MANIFEST_DIR) -> list[str]:
    schema = load_json(MANIFEST_SCHEMA_PATH)
    paths = sorted(directory.glob("*.json"))
    errors: list[str] = []
    ids: list[str] = []
    for path in paths:
        instance = load_json(path)
        ids.append(str(instance.get("campaign_id", "")))
        errors.extend(manifest_errors(path, instance, schema))
    for duplicate in sorted({item for item in ids if ids.count(item) > 1}):
        errors.append(f"campaign manifests: duplicate campaign_id {duplicate}")
    actual = set(ids)
    expected = expected_campaigns()
    for missing in sorted(expected - actual):
        errors.append(f"campaign manifests: active campaign is uncovered: {missing}")
    for unknown in sorted(actual - expected):
        errors.append(f"campaign manifests: unregistered campaign: {unknown}")
    return errors


def provider_gate_errors(campaign_id: str, stage: str, directory: Path = MANIFEST_DIR) -> list[str]:
    gated = {"SPECIFICATION", "REALIZATION", "CONFRONTATION", "JUDGMENT", "INTEGRATION", "CLAIM_PROMOTION"}
    if stage not in gated:
        return []
    path = directory / f"{campaign_id}.json"
    if not path.exists():
        return [f"{campaign_id} {stage}: no MATHSOLVE campaign manifest"]
    if campaign_manifest_errors(directory) or handoff_packet_errors():
        return [f"{campaign_id} {stage}: MATHSOLVE manifest or Cert packet registry is invalid"]
    instance = load_json(path)
    state = instance["certification"]["handoff_state"]
    if stage in {"JUDGMENT", "INTEGRATION"} and state not in ADJUDICATED_STATES:
        return [f"{campaign_id} {stage}: MATHCERT intake is not an adjudicated disposition"]
    if stage == "CLAIM_PROMOTION":
        if not instance["promotion"]["eligible"]:
            return [f"{campaign_id} {stage}: manifest is not promotion eligible"]
        if state not in POSITIVE_STATES:
            return [f"{campaign_id} {stage}: claim promotion requires certified or qualified MATHCERT disposition"]
    return []


def main() -> int:
    errors = campaign_manifest_errors()
    errors.extend(handoff_packet_errors())
    errors.extend(mathcert_handoff_errors())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"MATHSOLVE campaign validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("validated manifests, eight Cert packets, exact contract identities, intake/adjudication separation, and promotion boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
