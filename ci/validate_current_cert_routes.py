#!/usr/bin/env python3
"""Validate current MATHCERT route state without rewriting Solve handoff history."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
REGISTRY_PATH = ROOT / "contracts" / "mathcert_current_routes.json"
SCHEMA_PATH = ROOT / "schemas" / "mathcert_current_routes.schema.json"
REFERENCE_REGISTRY_PATH = ROOT / "contracts" / "programme_reference_registry.json"
MANIFEST_DIR = ROOT / "campaign_manifests"

INTAKE_STATES = {"pending", "ready", "submitted"}
ADJUDICATED_STATES = {"certified", "qualified", "rejected", "proof_debt"}
POSITIVE_STATES = {"certified", "qualified"}
GATED_STAGES = {
    "SPECIFICATION",
    "REALIZATION",
    "CONFRONTATION",
    "JUDGMENT",
    "INTEGRATION",
    "CLAIM_PROMOTION",
}
EXPECTED_ROUTE_STATES = {
    "UC-001": "qualified",
    "NS-CI-001": "qualified",
    "HC-001": "ready",
    "BSD-001": "pending",
    "PNP-001": "pending",
    "RH-001": "qualified",
    "YM-001": "pending",
    "OZ-001": "pending",
}
EXPECTED_CERT_OUTPUTS = {
    "UC-001": {
        "repository": "grandchallenge/MATHCERT",
        "commit_sha": "214c4f4d7962883bb10172db84d5162dde2e5c4e",
        "path": "certificates/union_closed/MC-UC-WP04-QUAL-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "265c185d6b2b2970dc675729efa3fc4860f29204",
    },
    "NS-CI-001": {
        "repository": "grandchallenge/MATHCERT",
        "commit_sha": "b1aa08001eb8537be8e204c3866aefd5f898252e",
        "path": "certificates/formal_sources/MC-FC-WP00-NS-CI-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "6047ad774957974a6c2aa86bae72b51841e774a4",
    },
    "RH-001": {
        "repository": "grandchallenge/MATHCERT",
        "commit_sha": "b1aa08001eb8537be8e204c3866aefd5f898252e",
        "path": "certificates/formal_sources/MC-FC-WP00-RH-001.json",
        "digest_algorithm": "git_blob_sha1",
        "digest": "3668bbf792d994a6d8919101417f2f3cad342cdc",
    },
}
EXPECTED_QUALIFICATION_SCOPES = {
    "UC-001": "qualified_restricted_claims_only",
    "NS-CI-001": "qualified_interface_only",
    "RH-001": "qualified_interface_only",
}
EXPECTED_PROVIDER_ARTIFACTS = {
    "UC-001": {
        "work_package_id": "MS-UC-WP04",
        "source_commit": "443daf537dc7e4ee34ab43aeb01508d9177816ab",
        "artifact": {
            "repository": "grandchallenge/MATHSOLVE",
            "commit_sha": "443daf537dc7e4ee34ab43aeb01508d9177816ab",
            "path": "domains/union_closed/WP04_small_cases_and_certificates/README.md",
            "digest_algorithm": "git_blob_sha1",
            "digest": "e4f4882666653fa1f0996aa7923e6290137fe2ee",
            "role": "solve_artifact",
        },
    },
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload,
        usedforsecurity=False,
    ).hexdigest()


def expected_campaigns() -> set[str]:
    registry = load_json(REFERENCE_REGISTRY_PATH)
    campaigns = registry.get("campaigns", {})
    if not isinstance(campaigns, dict) or not campaigns:
        raise ValueError("programme reference registry contains no campaigns")
    return {str(campaign_id) for campaign_id in campaigns}


def schema_errors(instance: dict[str, Any], schema: dict[str, Any], label: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def local_artifact_errors(artifact: dict[str, Any], label: str) -> list[str]:
    errors: list[str] = []
    path = ROOT / str(artifact.get("path", ""))
    digest = str(artifact.get("digest", ""))
    if not path.is_file():
        return [f"{label}: local artifact is missing: {artifact.get('path')}"]
    actual = git_blob_sha1(path)
    if actual != digest:
        errors.append(f"{label}: Git blob identity drift; expected {digest}, found {actual}")
    return errors


def current_cert_route_errors(
    registry_path: Path = REGISTRY_PATH,
    schema_path: Path = SCHEMA_PATH,
    manifest_dir: Path = MANIFEST_DIR,
) -> list[str]:
    registry = load_json(registry_path)
    schema = load_json(schema_path)
    errors = schema_errors(registry, schema, str(registry_path))

    campaigns = registry.get("campaigns", {})
    if not isinstance(campaigns, dict):
        return errors + [f"{registry_path}: campaigns must be an object"]

    actual = set(campaigns)
    expected = expected_campaigns()
    for missing in sorted(expected - actual):
        errors.append(f"{registry_path}: current Cert routes omit governed campaign {missing}")
    for unknown in sorted(actual - expected):
        errors.append(f"{registry_path}: current Cert routes include unregistered campaign {unknown}")

    for campaign_id, record in sorted(campaigns.items()):
        label = f"{registry_path}: campaigns.{campaign_id}"
        if not isinstance(record, dict):
            errors.append(f"{label}: route record must be an object")
            continue
        expected_route_id = f"MC-ROUTE-{campaign_id}"
        if record.get("route_id") != expected_route_id:
            errors.append(f"{label}: route_id drift; expected {expected_route_id}")
        expected_state = EXPECTED_ROUTE_STATES.get(campaign_id)
        if expected_state is not None and record.get("route_state") != expected_state:
            errors.append(
                f"{label}: route_state drift; expected {expected_state}, found {record.get('route_state')}"
            )

        manifest_ref = record.get("manifest", {})
        handoff_ref = record.get("handoff", {})
        if isinstance(manifest_ref, dict):
            errors.extend(local_artifact_errors(manifest_ref, f"{label}.manifest"))
        if isinstance(handoff_ref, dict):
            errors.extend(local_artifact_errors(handoff_ref, f"{label}.handoff"))

        manifest_path = manifest_dir / f"{campaign_id}.json"
        if manifest_path.is_file():
            manifest = load_json(manifest_path)
            if manifest.get("campaign_id") != campaign_id:
                errors.append(f"{label}: manifest campaign_id does not match overlay key")
            packet_status = manifest.get("certification", {}).get("handoff_state")
            if packet_status != record.get("handoff_state"):
                errors.append(
                    f"{label}: overlay handoff_state does not match immutable manifest handoff state"
                )

            expected_provider = EXPECTED_PROVIDER_ARTIFACTS.get(campaign_id)
            if expected_provider is not None:
                work_package_id = expected_provider["work_package_id"]
                work_package = next(
                    (
                        item
                        for item in manifest.get("work_packages", [])
                        if isinstance(item, dict) and item.get("work_package_id") == work_package_id
                    ),
                    None,
                )
                if work_package is None:
                    errors.append(f"{label}: expected provider work package {work_package_id} is missing")
                else:
                    if work_package.get("source_commit") != expected_provider["source_commit"]:
                        errors.append(f"{label}: provider source_commit drift")
                    expected_artifact = expected_provider["artifact"]
                    provider_artifact = next(
                        (
                            item
                            for item in work_package.get("artifacts", [])
                            if isinstance(item, dict)
                            and item.get("path") == expected_artifact["path"]
                        ),
                        None,
                    )
                    if provider_artifact != expected_artifact:
                        errors.append(f"{label}: exact provider artifact identity drift")

        handoff_path = ROOT / str(handoff_ref.get("path", ""))
        if handoff_path.is_file():
            packet = load_json(handoff_path)
            if packet.get("campaign_id") != campaign_id:
                errors.append(f"{label}: handoff campaign_id does not match overlay key")
            if packet.get("handoff_id") != f"MC-HANDOFF-{campaign_id}":
                errors.append(f"{label}: handoff_id is not canonical")
            if packet.get("status") != record.get("handoff_state"):
                errors.append(
                    f"{label}: overlay handoff_state does not match immutable packet status"
                )

        route_state = record.get("route_state")
        cert_output = record.get("cert_output")
        qualification_scope = record.get("qualification_scope")
        if route_state in POSITIVE_STATES:
            if not isinstance(cert_output, dict):
                errors.append(f"{label}: positive route state requires an exact Cert output")
            if not isinstance(qualification_scope, str) or not qualification_scope:
                errors.append(f"{label}: positive route state requires qualification scope")
        elif route_state in INTAKE_STATES:
            if cert_output is not None:
                errors.append(f"{label}: non-adjudicated intake cannot carry a Cert output")
            if qualification_scope is not None:
                errors.append(f"{label}: non-adjudicated intake cannot carry qualification scope")

        expected_output = EXPECTED_CERT_OUTPUTS.get(campaign_id)
        if expected_output is not None and cert_output != expected_output:
            errors.append(f"{label}: exact Cert output identity drift")
        expected_scope = EXPECTED_QUALIFICATION_SCOPES.get(campaign_id)
        if expected_scope is not None and qualification_scope != expected_scope:
            errors.append(
                f"{label}: qualification scope drift; expected {expected_scope}, found {qualification_scope}"
            )

        if record.get("mathematical_target_proved") is not False:
            errors.append(f"{label}: current interface or intake state cannot imply target proof")
        blockers = record.get("current_promotion_blockers", [])
        if not blockers:
            errors.append(f"{label}: current blocked campaign requires promotion blockers")

    rh_blockers = campaigns.get("RH-001", {}).get("current_promotion_blockers", [])
    stale_phrase = "has not independently replayed"
    if any(stale_phrase in str(item) for item in rh_blockers):
        errors.append(
            f"{registry_path}: RH current blockers repeat the superseded no-replay assertion"
        )

    return errors


def current_route_state(campaign_id: str, registry_path: Path = REGISTRY_PATH) -> str:
    registry = load_json(registry_path)
    campaigns = registry.get("campaigns", {})
    if campaign_id not in campaigns:
        raise KeyError(f"no current Cert route for {campaign_id}")
    return str(campaigns[campaign_id]["route_state"])


def provider_gate_errors(
    campaign_id: str,
    stage: str,
    manifest_dir: Path = MANIFEST_DIR,
    registry_path: Path = REGISTRY_PATH,
) -> list[str]:
    if stage not in GATED_STAGES:
        return []
    errors = current_cert_route_errors(
        registry_path=registry_path,
        manifest_dir=manifest_dir,
    )
    if errors:
        return [f"{campaign_id} {stage}: current Cert route registry is invalid"]

    manifest_path = manifest_dir / f"{campaign_id}.json"
    if not manifest_path.is_file():
        return [f"{campaign_id} {stage}: no MATHSOLVE campaign manifest"]

    route_state = current_route_state(campaign_id, registry_path=registry_path)
    if stage in {"JUDGMENT", "INTEGRATION"} and route_state not in ADJUDICATED_STATES:
        return [f"{campaign_id} {stage}: MATHCERT route is not an adjudicated disposition"]

    if stage == "CLAIM_PROMOTION":
        manifest = load_json(manifest_path)
        if not manifest.get("promotion", {}).get("eligible"):
            return [f"{campaign_id} {stage}: manifest is not promotion eligible"]
        if route_state not in POSITIVE_STATES:
            return [
                f"{campaign_id} {stage}: claim promotion requires certified or qualified MATHCERT route state"
            ]
    return []


def main() -> int:
    errors = current_cert_route_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(
            f"current MATHCERT route-state validation failed with {len(errors)} error(s)",
            file=sys.stderr,
        )
        return 1
    print(
        "validated immutable Solve handoff states, exact provider identities, current Cert adjudications, exact outputs, and promotion boundaries"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
