#!/usr/bin/env python3
"""Validate the bounded VGSE Solve activation and current Cert-route overlay."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

import validate_current_cert_routes as base_routes

ROOT = Path(__file__).resolve().parents[1]
BASE_REGISTRY_PATH = ROOT / "contracts" / "mathcert_current_routes.json"
OVERLAY_PATH = ROOT / "contracts" / "mathcert_current_routes_vgse_overlay.json"
OVERLAY_SCHEMA_PATH = ROOT / "schemas" / "mathcert_current_routes_vgse_overlay.schema.json"
REFERENCE_REGISTRY_PATH = ROOT / "contracts" / "programme_reference_registry.json"
MANIFEST_DIR = ROOT / "campaign_manifests"
HANDOFF_DIR = ROOT / "cert_handoffs"
VGSE_ID = "VGSE-001"
INTAKE_STATES = {"pending", "ready", "submitted"}
ADJUDICATED_STATES = {"certified", "qualified", "rejected", "proof_debt"}
POSITIVE_STATES = {"certified", "qualified"}
GATED_STAGES = {
    "SPECIFICATION", "REALIZATION", "CONFRONTATION",
    "JUDGMENT", "INTEGRATION", "CLAIM_PROMOTION",
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(
        f"blob {len(payload)}\0".encode("ascii") + payload,
        usedforsecurity=False,
    ).hexdigest()


def schema_errors(instance: Any, schema: Any, label: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))
    ]


def _ref_errors(ref: dict[str, Any], label: str) -> list[str]:
    path = ROOT / str(ref.get("path", ""))
    if not path.is_file():
        return [f"{label}: local artifact is missing"]
    actual = git_blob_sha1(path)
    if actual != ref.get("digest"):
        return [f"{label}: Git blob identity drift; expected {ref.get('digest')}, found {actual}"]
    return []


def vgse_overlay_errors(
    *,
    overlay_path: Path = OVERLAY_PATH,
    schema_path: Path = OVERLAY_SCHEMA_PATH,
    manifest_dir: Path = MANIFEST_DIR,
    handoff_dir: Path = HANDOFF_DIR,
) -> list[str]:
    overlay = load_json(overlay_path)
    schema = load_json(schema_path)
    errors = schema_errors(overlay, schema, str(overlay_path))

    base_ref = overlay.get("base_registry", {})
    errors.extend(_ref_errors(base_ref, f"{overlay_path}: base_registry"))
    base = load_json(BASE_REGISTRY_PATH)
    base_ids = set(base.get("campaigns", {}))
    if VGSE_ID in base_ids:
        errors.append(f"{overlay_path}: historical base registry may not be rewritten with VGSE")

    reference_ids = set(load_json(REFERENCE_REGISTRY_PATH).get("campaigns", {}))
    if reference_ids != base_ids | {VGSE_ID}:
        errors.append(f"{overlay_path}: merged campaign coverage does not match Programme references")

    campaign = overlay.get("campaign", {})
    manifest_ref = campaign.get("manifest", {})
    handoff_ref = campaign.get("handoff", {})
    manifest_path = manifest_dir / "VGSE-001.json"
    handoff_path = handoff_dir / "VGSE-001.json"
    for ref, path, label in (
        (manifest_ref, manifest_path, "manifest"),
        (handoff_ref, handoff_path, "handoff"),
    ):
        if not path.is_file():
            errors.append(f"{overlay_path}: {label} is missing")
        elif git_blob_sha1(path) != ref.get("digest"):
            errors.append(f"{overlay_path}: {label} identity drift")

    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        if manifest.get("campaign_id") != VGSE_ID:
            errors.append(f"{overlay_path}: manifest campaign identity drift")
        if manifest.get("certification", {}).get("handoff_state") != "pending":
            errors.append(f"{overlay_path}: manifest must remain pending before route registration")
        if manifest.get("promotion", {}).get("eligible") is not False:
            errors.append(f"{overlay_path}: pending VGSE manifest cannot be promotion eligible")

    if handoff_path.is_file():
        handoff = load_json(handoff_path)
        if handoff.get("handoff_id") != "MC-HANDOFF-VGSE-001":
            errors.append(f"{overlay_path}: handoff identity drift")
        if handoff.get("status") != "pending" or not handoff.get("blockers"):
            errors.append(f"{overlay_path}: handoff must remain blocked and pending")
        if handoff.get("cert_contract", {}).get("route_id") != "MC-ROUTE-VGSE-001":
            errors.append(f"{overlay_path}: proposed route identity drift")

    if campaign.get("route_registry_entry_present") is not False:
        errors.append(f"{overlay_path}: absent route cannot be represented as registered")
    for field in ("mathematical_target_proved", "may_adjudicate", "may_issue_certificate_output"):
        if campaign.get(field) is not False:
            errors.append(f"{overlay_path}: prohibited authority inflation in {field}")
    if campaign.get("cert_output") is not None or campaign.get("qualification_scope") is not None:
        errors.append(f"{overlay_path}: pending route cannot carry output or qualification scope")
    if not campaign.get("current_promotion_blockers"):
        errors.append(f"{overlay_path}: pending route requires promotion blockers")
    return errors


def merged_current_cert_route_errors(
    registry_path: Path = BASE_REGISTRY_PATH,
    schema_path: Path = base_routes.SCHEMA_PATH,
    manifest_dir: Path = MANIFEST_DIR,
    overlay_path: Path = OVERLAY_PATH,
) -> list[str]:
    original = base_routes.expected_campaigns
    base_routes.expected_campaigns = lambda: original() - {VGSE_ID}
    try:
        errors = base_routes.current_cert_route_errors(
            registry_path=registry_path,
            schema_path=schema_path,
            manifest_dir=manifest_dir,
        )
    finally:
        base_routes.expected_campaigns = original
    errors.extend(vgse_overlay_errors(overlay_path=overlay_path, manifest_dir=manifest_dir))
    return errors


def merged_current_route_state(campaign_id: str) -> str:
    if campaign_id == VGSE_ID:
        return str(load_json(OVERLAY_PATH)["campaign"]["route_state"])
    return base_routes.current_route_state(campaign_id)


def merged_provider_gate_errors(
    campaign_id: str,
    stage: str,
    manifest_dir: Path = MANIFEST_DIR,
) -> list[str]:
    if stage not in GATED_STAGES:
        return []
    errors = merged_current_cert_route_errors(manifest_dir=manifest_dir)
    if errors:
        return [f"{campaign_id} {stage}: merged current Cert route registry is invalid"]
    manifest_path = manifest_dir / f"{campaign_id}.json"
    if not manifest_path.is_file():
        return [f"{campaign_id} {stage}: no MATHSOLVE campaign manifest"]
    route_state = merged_current_route_state(campaign_id)
    if stage in {"JUDGMENT", "INTEGRATION"} and route_state not in ADJUDICATED_STATES:
        return [f"{campaign_id} {stage}: MATHCERT route is not an adjudicated disposition"]
    if stage == "CLAIM_PROMOTION":
        manifest = load_json(manifest_path)
        if not manifest.get("promotion", {}).get("eligible"):
            return [f"{campaign_id} {stage}: manifest is not promotion eligible"]
        if route_state not in POSITIVE_STATES:
            return [f"{campaign_id} {stage}: claim promotion requires a positive MATHCERT route state"]
    return []


if __name__ == "__main__":
    failures = merged_current_cert_route_errors()
    if failures:
        raise SystemExit("\n".join(failures))
    print("validated historical Cert routes plus bounded VGSE pending-route overlay")
