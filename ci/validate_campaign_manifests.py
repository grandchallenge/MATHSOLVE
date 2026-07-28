#!/usr/bin/env python3
"""Validate recursive MATHSOLVE campaign manifests and handoff discipline."""
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
SCHEMA_PATH = ROOT / "schemas" / "campaign_manifest.schema.json"
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
COMPLETE_HANDOFF_STATES = {
    "ready",
    "submitted",
    "certified",
    "qualified",
    "rejected",
    "proof_debt",
}
POSITIVE_HANDOFF_STATES = {"certified", "qualified"}


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
            actual = hashlib.sha256(local_path.read_bytes()).hexdigest()
            if actual != digest:
                errors.append(f"{label}: SHA-256 identity drift for {path}")
    return errors


def walk_work_packages(items: Iterable[dict[str, Any]], prefix: str = ""):
    for index, item in enumerate(items):
        label = f"{prefix}work_packages[{index}]"
        yield label, item
        yield from walk_work_packages(item.get("children", []), prefix=label + ".")


def schema_errors(
    instance: dict[str, Any], schema: dict[str, Any], label: str
) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def manifest_errors(
    path: Path, instance: dict[str, Any], schema: dict[str, Any]
) -> list[str]:
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

    work_package_ids: set[str] = set()
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
                errors.extend(
                    artifact_errors(artifact, f"{path}: {label}.artifacts[{index}]")
                )

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
                errors.extend(
                    artifact_errors(artifact, f"{path}: {label}.ledgers.{name}")
                )
                ledger_paths.append(str(artifact.get("path", "")))
                if artifact.get("role") != role:
                    errors.append(
                        f"{path}: {label}.ledgers.{name} must have role {role}"
                    )
        duplicates = sorted({item for item in ledger_paths if ledger_paths.count(item) > 1})
        for duplicate in duplicates:
            errors.append(
                f"{path}: {label}: distinct ledger roles share artifact path {duplicate}"
            )

        if wp.get("primary_type") in COMPUTATIONAL_TYPES:
            if not isinstance(ledgers.get("failed_route"), dict):
                errors.append(
                    f"{path}: {label}: computational package requires failed-route ledger"
                )
            if not isinstance(ledgers.get("resource"), dict):
                errors.append(
                    f"{path}: {label}: computational package requires resource ledger"
                )

    for index, artifact in enumerate(instance.get("forge_inputs", [])):
        if isinstance(artifact, dict):
            errors.extend(artifact_errors(artifact, f"{path}: forge_inputs[{index}]"))

    promotion = instance.get("promotion", {})
    certification = instance.get("certification", {})
    handoff_state = certification.get("handoff_state")
    packets = certification.get("handoff_packets", [])
    packet_statuses = {
        str(packet.get("status", ""))
        for packet in packets
        if isinstance(packet, dict)
    }

    if handoff_state in COMPLETE_HANDOFF_STATES and not packets:
        errors.append(f"{path}: complete MATHCERT handoff state requires a packet")
    if handoff_state in POSITIVE_HANDOFF_STATES and (
        not packets or not packet_statuses.issubset(POSITIVE_HANDOFF_STATES)
    ):
        errors.append(
            f"{path}: positive MATHCERT aggregate state requires only certified or qualified packets"
        )

    if promotion.get("eligible") is True:
        if promotion.get("blockers"):
            errors.append(f"{path}: promotion-eligible manifest must have no blockers")
        if handoff_state not in POSITIVE_HANDOFF_STATES:
            errors.append(
                f"{path}: promotion eligibility requires certified or qualified MATHCERT state"
            )
        if not packets:
            errors.append(
                f"{path}: promotion eligibility requires at least one MATHCERT handoff"
            )
        elif not packet_statuses.issubset(POSITIVE_HANDOFF_STATES):
            errors.append(
                f"{path}: promotion eligibility requires every handoff packet to be certified or qualified"
            )
    elif not promotion.get("blockers"):
        errors.append(f"{path}: blocked promotion must identify at least one blocker")

    return errors


def campaign_manifest_errors(directory: Path = MANIFEST_DIR) -> list[str]:
    schema = load_json(SCHEMA_PATH)
    paths = sorted(directory.glob("*.json"))
    errors: list[str] = []
    ids: list[str] = []
    for path in paths:
        instance = load_json(path)
        ids.append(str(instance.get("campaign_id", "")))
        errors.extend(manifest_errors(path, instance, schema))
    duplicates = sorted({item for item in ids if ids.count(item) > 1})
    for item in duplicates:
        errors.append(f"campaign manifests: duplicate campaign_id {item}")
    actual = set(ids)
    expected = expected_campaigns()
    for missing in sorted(expected - actual):
        errors.append(f"campaign manifests: active campaign is uncovered: {missing}")
    for unknown in sorted(actual - expected):
        errors.append(f"campaign manifests: unregistered campaign: {unknown}")
    return errors


def mathcert_handoff_errors(
    template_path: Path = HANDOFF_TEMPLATE_PATH,
) -> list[str]:
    schema = load_json(HANDOFF_SCHEMA_PATH)
    instance = load_json(template_path)
    errors = schema_errors(instance, schema, str(template_path))
    for name in ("claim_ledger", "proof_obligations"):
        artifact = instance.get(name)
        if isinstance(artifact, dict):
            errors.extend(artifact_errors(artifact, f"{template_path}: {name}"))
    return errors


def provider_gate_errors(
    campaign_id: str, stage: str, directory: Path = MANIFEST_DIR
) -> list[str]:
    """Fail closed for future mathematical lifecycle and claim promotion."""
    gated = {
        "SPECIFICATION",
        "REALIZATION",
        "CONFRONTATION",
        "JUDGMENT",
        "INTEGRATION",
        "CLAIM_PROMOTION",
    }
    if stage not in gated:
        return []
    path = directory / f"{campaign_id}.json"
    if not path.exists():
        return [f"{campaign_id} {stage}: no MATHSOLVE campaign manifest"]
    instance = load_json(path)
    if campaign_manifest_errors(directory):
        return [f"{campaign_id} {stage}: MATHSOLVE manifest registry is invalid"]

    certification = instance["certification"]
    state = certification["handoff_state"]
    packets = certification["handoff_packets"]
    packet_statuses = {
        str(packet.get("status", ""))
        for packet in packets
        if isinstance(packet, dict)
    }

    if stage in {"JUDGMENT", "INTEGRATION"}:
        if state not in COMPLETE_HANDOFF_STATES or not packets:
            return [
                f"{campaign_id} {stage}: no complete content-addressed MATHCERT disposition"
            ]
    if stage == "CLAIM_PROMOTION":
        if not instance["promotion"]["eligible"]:
            return [f"{campaign_id} {stage}: manifest is not promotion eligible"]
        if state not in POSITIVE_HANDOFF_STATES or not packet_statuses.issubset(
            POSITIVE_HANDOFF_STATES
        ):
            return [
                f"{campaign_id} {stage}: claim promotion requires certified or qualified MATHCERT packets"
            ]
    return []


def main() -> int:
    errors = campaign_manifest_errors()
    errors.extend(mathcert_handoff_errors())
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(
            f"MATHSOLVE campaign validation failed with {len(errors)} error(s)",
            file=sys.stderr,
        )
        return 1
    print(
        "validated recursive MATHSOLVE manifests, artifact identities, and Cert promotion boundaries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
