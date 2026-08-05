#!/usr/bin/env python3
"""Validate historical Cert routes and bounded successor overlays."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

import validate_current_cert_routes as base_routes

ROOT = Path(__file__).resolve().parents[1]
BASE_REGISTRY_PATH = ROOT / "contracts" / "mathcert_current_routes.json"
REFERENCE_REGISTRY_PATH = ROOT / "contracts" / "programme_reference_registry.json"
MANIFEST_DIR = ROOT / "campaign_manifests"
HANDOFF_DIR = ROOT / "cert_handoffs"

VGSE_ID = "VGSE-001"
EUCLID_ID = "EUCLID-GCD-E2E-001"
DIO_ID = "EUCLID-DIOPHANTINE-E2E-002"
SUCCESSOR_IDS = {VGSE_ID, EUCLID_ID, DIO_ID}

OVERLAY_PATH = ROOT / "contracts" / "mathcert_current_routes_vgse_overlay.json"
OVERLAY_SCHEMA_PATH = ROOT / "schemas" / "mathcert_current_routes_vgse_overlay.schema.json"
EUCLID_OVERLAY_PATH = ROOT / "contracts" / "mathcert_current_routes_euclid_gcd_overlay.json"
EUCLID_OVERLAY_SCHEMA_PATH = ROOT / "schemas" / "mathcert_current_routes_euclid_gcd_overlay.schema.json"
DIO_OVERLAY_PATH = ROOT / "contracts" / "mathcert_current_routes_euclid_diophantine_overlay.json"
DIO_OVERLAY_SCHEMA_PATH = ROOT / "schemas" / "mathcert_current_routes_euclid_diophantine_overlay.schema.json"

ADJUDICATED_STATES = {"certified", "qualified", "rejected", "proof_debt"}
POSITIVE_STATES = {"certified", "qualified"}
GATED_STAGES = {"SPECIFICATION", "REALIZATION", "CONFRONTATION", "JUDGMENT", "INTEGRATION", "CLAIM_PROMOTION"}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload, usedforsecurity=False).hexdigest()


def schema_errors(instance: Any, schema: Any, label: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{label}: {error.json_path}: {error.message}" for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))]


def _ref_errors(ref: dict[str, Any], label: str) -> list[str]:
    path = ROOT / str(ref.get("path", ""))
    if not path.is_file():
        return [f"{label}: local artifact is missing"]
    actual = git_blob_sha1(path)
    if actual != ref.get("digest"):
        return [f"{label}: Git blob identity drift; expected {ref.get('digest')}, found {actual}"]
    return []


def _coverage_errors() -> list[str]:
    base_ids = set(load_json(BASE_REGISTRY_PATH).get("campaigns", {}))
    reference_ids = set(load_json(REFERENCE_REGISTRY_PATH).get("campaigns", {}))
    expected = base_ids | SUCCESSOR_IDS
    return [] if reference_ids == expected else ["successor-overlay campaign coverage does not match Programme references"]


def _overlay_errors(*, overlay_path: Path, schema_path: Path, campaign_id: str, handoff_status: str, predecessor_id: str | None = None) -> list[str]:
    overlay = load_json(overlay_path)
    errors = schema_errors(overlay, load_json(schema_path), str(overlay_path))
    errors.extend(_ref_errors(overlay.get("base_registry", {}), f"{overlay_path}: base_registry"))
    if predecessor_id is not None:
        errors.extend(_ref_errors(overlay.get("predecessor_overlay", {}), f"{overlay_path}: predecessor_overlay"))
        predecessor = load_json(ROOT / overlay.get("predecessor_overlay", {}).get("path", ""))
        if predecessor.get("campaign", {}).get("campaign_id") != predecessor_id:
            errors.append(f"{overlay_path}: predecessor campaign identity drift")
    errors.extend(_coverage_errors())

    base_ids = set(load_json(BASE_REGISTRY_PATH).get("campaigns", {}))
    if base_ids & SUCCESSOR_IDS:
        errors.append(f"{overlay_path}: historical base registry contains successor campaign state")

    campaign = overlay.get("campaign", {})
    manifest_path = MANIFEST_DIR / f"{campaign_id}.json"
    handoff_path = HANDOFF_DIR / f"{campaign_id}.json"
    for ref, path, label in ((campaign.get("manifest", {}), manifest_path, "manifest"), (campaign.get("handoff", {}), handoff_path, "handoff")):
        if not path.is_file():
            errors.append(f"{overlay_path}: {label} is missing")
        elif git_blob_sha1(path) != ref.get("digest"):
            errors.append(f"{overlay_path}: {label} identity drift")

    if manifest_path.is_file():
        manifest = load_json(manifest_path)
        if manifest.get("campaign_id") != campaign_id:
            errors.append(f"{overlay_path}: manifest campaign identity drift")
        if manifest.get("certification", {}).get("handoff_state") != handoff_status:
            errors.append(f"{overlay_path}: manifest handoff state drift")
        if manifest.get("promotion", {}).get("eligible") is not False:
            errors.append(f"{overlay_path}: unadjudicated manifest cannot be promotion eligible")

    if handoff_path.is_file():
        handoff = load_json(handoff_path)
        if handoff.get("status") != handoff_status:
            errors.append(f"{overlay_path}: handoff status drift")
        if handoff_status == "pending" and not handoff.get("blockers"):
            errors.append(f"{overlay_path}: pending handoff requires blockers")
        if handoff_status == "ready" and handoff.get("blockers") != []:
            errors.append(f"{overlay_path}: ready handoff must have no producer blockers")

    if campaign.get("route_registry_entry_present") is not False:
        errors.append(f"{overlay_path}: absent route cannot be represented as registered")
    if campaign.get("route_state") != "pending":
        errors.append(f"{overlay_path}: unregistered route must remain pending")
    if campaign.get("handoff_state") != handoff_status:
        errors.append(f"{overlay_path}: overlay handoff state drift")
    for field in ("mathematical_target_proved", "may_adjudicate", "may_issue_certificate_output"):
        if campaign.get(field) is not False:
            errors.append(f"{overlay_path}: prohibited authority inflation in {field}")
    if campaign.get("cert_output") is not None or campaign.get("qualification_scope") is not None:
        errors.append(f"{overlay_path}: pending route cannot carry output or qualification scope")
    if not campaign.get("current_promotion_blockers"):
        errors.append(f"{overlay_path}: pending route requires promotion blockers")
    return errors


def vgse_overlay_errors(*, overlay_path: Path = OVERLAY_PATH, schema_path: Path = OVERLAY_SCHEMA_PATH, manifest_dir: Path = MANIFEST_DIR, handoff_dir: Path = HANDOFF_DIR) -> list[str]:
    del manifest_dir, handoff_dir
    return _overlay_errors(overlay_path=overlay_path, schema_path=schema_path, campaign_id=VGSE_ID, handoff_status="pending")


def euclid_overlay_errors(*, overlay_path: Path = EUCLID_OVERLAY_PATH, schema_path: Path = EUCLID_OVERLAY_SCHEMA_PATH, manifest_dir: Path = MANIFEST_DIR, handoff_dir: Path = HANDOFF_DIR) -> list[str]:
    del manifest_dir, handoff_dir
    return _overlay_errors(overlay_path=overlay_path, schema_path=schema_path, campaign_id=EUCLID_ID, handoff_status="ready", predecessor_id=VGSE_ID)


def diophantine_overlay_errors(*, overlay_path: Path = DIO_OVERLAY_PATH, schema_path: Path = DIO_OVERLAY_SCHEMA_PATH, manifest_dir: Path = MANIFEST_DIR, handoff_dir: Path = HANDOFF_DIR) -> list[str]:
    del manifest_dir, handoff_dir
    return _overlay_errors(overlay_path=overlay_path, schema_path=schema_path, campaign_id=DIO_ID, handoff_status="ready", predecessor_id=EUCLID_ID)


def merged_current_cert_route_errors(registry_path: Path = BASE_REGISTRY_PATH, schema_path: Path = base_routes.SCHEMA_PATH, manifest_dir: Path = MANIFEST_DIR, overlay_path: Path = OVERLAY_PATH, euclid_overlay_path: Path = EUCLID_OVERLAY_PATH, diophantine_overlay_path: Path = DIO_OVERLAY_PATH) -> list[str]:
    original = base_routes.expected_campaigns
    base_routes.expected_campaigns = lambda: original() - SUCCESSOR_IDS
    try:
        errors = base_routes.current_cert_route_errors(registry_path=registry_path, schema_path=schema_path, manifest_dir=manifest_dir)
    finally:
        base_routes.expected_campaigns = original
    errors.extend(vgse_overlay_errors(overlay_path=overlay_path))
    errors.extend(euclid_overlay_errors(overlay_path=euclid_overlay_path))
    errors.extend(diophantine_overlay_errors(overlay_path=diophantine_overlay_path))
    return errors


def merged_current_route_state(campaign_id: str) -> str:
    overlays = {VGSE_ID: OVERLAY_PATH, EUCLID_ID: EUCLID_OVERLAY_PATH, DIO_ID: DIO_OVERLAY_PATH}
    if campaign_id in overlays:
        return str(load_json(overlays[campaign_id])["campaign"]["route_state"])
    return base_routes.current_route_state(campaign_id)


def merged_provider_gate_errors(campaign_id: str, stage: str, manifest_dir: Path = MANIFEST_DIR) -> list[str]:
    if stage not in GATED_STAGES:
        return []
    if merged_current_cert_route_errors(manifest_dir=manifest_dir):
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
    print("validated historical Cert routes plus bounded VGSE, GCD, and Diophantine successor overlays")
