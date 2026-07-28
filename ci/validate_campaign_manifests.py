#!/usr/bin/env python3
"""Validate recursive MATHSOLVE campaign manifests and handoff discipline."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_DIR = ROOT / "campaign_manifests"
SCHEMA_PATH = ROOT / "schemas" / "campaign_manifest.schema.json"
EXPECTED_CAMPAIGNS = {
    "UC-001", "NS-CI-001", "HC-001", "BSD-001",
    "PNP-001", "RH-001", "YM-001", "OZ-001",
}
COMPUTATIONAL_TYPES = {
    "EXACT_COMPUTATIONAL_SCREEN",
    "ALGEBRAIC_GEOMETRY_CAMPAIGN",
    "INTERVAL_CERTIFICATION_CAMPAIGN",
    "COUNTEREXAMPLE_SEARCH",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def artifact_errors(artifact: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    algorithm = artifact.get("digest_algorithm")
    digest = str(artifact.get("digest", ""))
    commit = str(artifact.get("commit_sha", ""))
    if algorithm == "git_commit_sha1" and digest != commit:
        errors.append(f"{label}: git_commit_sha1 digest must equal commit_sha")
    if algorithm in {"git_commit_sha1", "git_blob_sha1"} and len(digest) != 40:
        errors.append(f"{label}: {algorithm} digest must contain 40 hexadecimal characters")
    if algorithm == "sha256" and len(digest) != 64:
        errors.append(f"{label}: sha256 digest must contain 64 hexadecimal characters")
    return errors


def walk_work_packages(items: list[dict[str, Any]], prefix: str = ""):
    for index, item in enumerate(items):
        label = f"{prefix}work_packages[{index}]"
        yield label, item
        yield from walk_work_packages(item.get("children", []), prefix=label + ".")


def manifest_errors(path: Path, instance: dict[str, Any], schema: dict[str, Any]) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = [
        f"{path}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]
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
            errors.extend(artifact_errors(artifact, f"{path}: {label}.artifacts[{index}]"))
        ledgers = wp.get("ledgers", {})
        for name in ("claim", "proof_obligation", "failed_route", "resource", "certification"):
            artifact = ledgers.get(name)
            if isinstance(artifact, dict):
                errors.extend(artifact_errors(artifact, f"{path}: {label}.ledgers.{name}"))
        if wp.get("primary_type") in COMPUTATIONAL_TYPES:
            if not isinstance(ledgers.get("failed_route"), dict):
                errors.append(f"{path}: {label}: computational package requires failed-route ledger")
            if not isinstance(ledgers.get("resource"), dict):
                errors.append(f"{path}: {label}: computational package requires resource ledger")

    for index, artifact in enumerate(instance.get("forge_inputs", [])):
        errors.extend(artifact_errors(artifact, f"{path}: forge_inputs[{index}]"))

    promotion = instance.get("promotion", {})
    certification = instance.get("certification", {})
    if promotion.get("eligible") is True:
        if promotion.get("blockers"):
            errors.append(f"{path}: promotion-eligible manifest must have no blockers")
        if certification.get("handoff_state") != "ready":
            errors.append(f"{path}: promotion eligibility requires ready MATHCERT handoff state")
        if not certification.get("handoff_packets"):
            errors.append(f"{path}: promotion eligibility requires at least one MATHCERT handoff")
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
    for missing in sorted(EXPECTED_CAMPAIGNS - actual):
        errors.append(f"campaign manifests: active campaign is uncovered: {missing}")
    for unknown in sorted(actual - EXPECTED_CAMPAIGNS):
        errors.append(f"campaign manifests: unregistered campaign: {unknown}")
    return errors


def provider_gate_errors(campaign_id: str, stage: str, directory: Path = MANIFEST_DIR) -> list[str]:
    """Fail closed for future mathematical promotion."""
    gated = {"SPECIFICATION", "REALIZATION", "CONFRONTATION", "JUDGMENT", "INTEGRATION"}
    if stage not in gated:
        return []
    path = directory / f"{campaign_id}.json"
    if not path.exists():
        return [f"{campaign_id} {stage}: no MATHSOLVE campaign manifest"]
    instance = load_json(path)
    errors = campaign_manifest_errors(directory)
    if errors:
        return [f"{campaign_id} {stage}: MATHSOLVE manifest registry is invalid"]
    if stage in {"JUDGMENT", "INTEGRATION"}:
        certification = instance["certification"]
        if certification["handoff_state"] not in {"ready", "partial"}:
            return [f"{campaign_id} {stage}: no admissible MATHCERT handoff state"]
    return []


def main() -> int:
    errors = campaign_manifest_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"MATHSOLVE campaign validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("validated 8 recursive MATHSOLVE campaign manifests with GitHub lineage and Cert boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
