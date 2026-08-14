#!/usr/bin/env python3
"""Validate independent OpenAI ten-proofs result-family handoff packets."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
WP_ROOT = ROOT / "work_packages" / "OPENAI_TEN_PROOFS_WP00"
PACKET_DIR = WP_ROOT / "result_family_handoffs"
REGISTRY_PATH = WP_ROOT / "result_family_handoff_registry.json"
PACKET_SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_result_family_handoff.schema.json"
PERMANENT_SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_permanent_result_family_handoff.schema.json"
REGISTRY_SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_result_family_handoff_registry.schema.json"

EXPECTED_PACKETS = {
    "OTP-F-EHRHART": {
        "handoff_id": "MC-OTP-HANDOFF-F-EHRHART",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-F-EHRHART.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-F-EHRHART.json",
        "semantic_digest": "a3dc4de4c38a80b7aec1fae6506b08e14d2e58bb",
        "route_id": "MC-ROUTE-OTP-F-EHRHART",
        "schema": "legacy",
    },
    "OTP-J1-COMPACTNESS": {
        "handoff_id": "MC-OTP-HANDOFF-J1-COMPACTNESS",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J1-COMPACTNESS.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J1-COMPACTNESS.json",
        "semantic_digest": "659396358d0d999c00011645f72602f30ccf6b0e",
        "route_id": "MC-ROUTE-OTP-J1-COMPACTNESS",
        "schema": "legacy",
    },
    "OTP-J2-TWO-DEGENERATE": {
        "handoff_id": "MC-OTP-HANDOFF-J2-TWO-DEGENERATE",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J2-TWO-DEGENERATE.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J2-TWO-DEGENERATE.json",
        "semantic_digest": "7bd168c46921f64364b20021b6315d68f0fde7d0",
        "route_id": "MC-ROUTE-OTP-J2-TWO-DEGENERATE",
        "schema": "legacy",
    },
    "OTP-C-PERMANENT": {
        "handoff_id": "MC-OTP-HANDOFF-C-PERMANENT-FORMULA",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-C-PERMANENT.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT/semantic_audit_record.json",
        "semantic_digest": "3e04bd16bd8a91eaf9b6702de89fcdcc72f61099",
        "route_id": "MC-ROUTE-OTP-C-PERMANENT-FORMULA",
        "schema": "permanent",
    },
}
EXPECTED_FAMILIES = tuple(EXPECTED_PACKETS)
EXPECTED_BLOCKED = ["OTP-H-GAPCVP"]
EXPECTED_PERMANENT_UNENCODED = [
    "source Theorem 1.1 arithmetic-circuit complexity",
    "Theorem 1.2 internal-gate bound with constant 256",
    "Theorem 1.3 internal-gate bound with constant 384",
    "Theorems 1.2/1.3 total-leaves and total-vertices consequences",
    "historical admitted-PDF byte equivalence",
]


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


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


def validation_errors(
    registry: dict[str, Any] | None = None,
    packets: dict[str, dict[str, Any]] | None = None,
    packet_blobs: dict[str, str] | None = None,
) -> list[str]:
    errors: list[str] = []
    if registry is None:
        registry = load_json(REGISTRY_PATH)
    if packets is None:
        packets = {path.stem: load_json(path) for path in sorted(PACKET_DIR.glob("*.json"))}
    if packet_blobs is None:
        packet_blobs = {path.stem: git_blob_sha1(path) for path in sorted(PACKET_DIR.glob("*.json"))}

    legacy_schema = load_json(PACKET_SCHEMA_PATH)
    permanent_schema = load_json(PERMANENT_SCHEMA_PATH)
    registry_schema = load_json(REGISTRY_SCHEMA_PATH)
    errors.extend(schema_errors(registry, registry_schema, str(REGISTRY_PATH)))

    actual_stems = set(packets)
    expected_stems = set(EXPECTED_FAMILIES)
    for missing in sorted(expected_stems - actual_stems):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: missing packet {missing}")
    for unknown in sorted(actual_stems - expected_stems):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: unexpected packet {unknown}")

    seen_handoffs: list[str] = []
    seen_routes: list[str] = []
    for family, expected in EXPECTED_PACKETS.items():
        packet = packets.get(family)
        if not isinstance(packet, dict):
            continue
        label = f"OTP-FAMILY-HANDOFFS-001: {family}"
        packet_schema = permanent_schema if expected["schema"] == "permanent" else legacy_schema
        errors.extend(schema_errors(packet, packet_schema, label))
        if packet.get("result_family") != family:
            errors.append(f"{label}: result-family identity drift")
        if packet.get("handoff_id") != expected["handoff_id"]:
            errors.append(f"{label}: handoff identity drift")
        semantic = packet.get("authority", {}).get("semantic_record", {})
        if semantic.get("path") != expected["semantic_path"]:
            errors.append(f"{label}: semantic-record path drift")
        if semantic.get("digest") != expected["semantic_digest"]:
            errors.append(f"{label}: semantic-record digest drift")
        requested = packet.get("requested_adjudication", {})
        if requested.get("route_id") != expected["route_id"]:
            errors.append(f"{label}: requested route identity drift")
        if requested.get("current_route_state") != "not_registered":
            errors.append(f"{label}: branch packet inflated current Cert route state")
        if requested.get("cert_output") is not None:
            errors.append(f"{label}: branch packet carries a Cert output")
        if requested.get("may_adjudicate_on_branch") is not False:
            errors.append(f"{label}: branch packet authorizes adjudication")
        if packet.get("replay_gate", {}).get("state") != "clear":
            errors.append(f"{label}: replay gate is not clear")
        if packet.get("semantic_gate", {}).get("state") != "clear":
            errors.append(f"{label}: semantic gate is not clear")
        controls = packet.get("route_controls", {})
        if controls.get("result_family_only") is not True:
            errors.append(f"{label}: result-family-only boundary removed")
        for field in (
            "may_create_aggregate_handoff",
            "may_imply_mathcert_acceptance",
            "may_imply_adjudication",
            "may_claim_mathematical_proof",
            "may_promote_claim",
        ):
            if controls.get(field) is not False:
                errors.append(f"{label}: prohibited route control enabled: {field}")
        if family == "OTP-C-PERMANENT":
            for field in (
                "may_route_circuit_theorem",
                "may_route_gate_bounds",
                "may_route_total_size_consequences",
            ):
                if controls.get(field) is not False:
                    errors.append(f"{label}: Permanent scope inflation enabled: {field}")
            scope = packet.get("target_scope", {})
            if scope.get("lean_theorems") != [
                "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound",
                "PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound",
            ]:
                errors.append(f"{label}: Permanent target set drift")
            witness = packet.get("authority", {}).get("nonvacuity_witness", {})
            if witness.get("digest") != "e756c8476bac1795f3fb8ca0b7235d3a4a5c59ea":
                errors.append(f"{label}: Permanent nonvacuity witness drift")
        seen_handoffs.append(str(packet.get("handoff_id", "")))
        seen_routes.append(str(requested.get("route_id", "")))

    for duplicate in sorted({item for item in seen_handoffs if seen_handoffs.count(item) > 1}):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: duplicate handoff identity {duplicate}")
    for duplicate in sorted({item for item in seen_routes if seen_routes.count(item) > 1}):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: duplicate requested route identity {duplicate}")

    registry_packets = registry.get("packets", [])
    if not isinstance(registry_packets, list):
        registry_packets = []
    indexed_families = [str(item.get("result_family", "")) for item in registry_packets if isinstance(item, dict)]
    if indexed_families != list(EXPECTED_FAMILIES):
        errors.append("OTP-FAMILY-HANDOFFS-001: registry packet order or membership drift")
    for item in registry_packets:
        if not isinstance(item, dict):
            continue
        family = str(item.get("result_family", ""))
        expected = EXPECTED_PACKETS.get(family)
        if expected is None:
            continue
        if item.get("handoff_id") != expected["handoff_id"]:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: registry handoff drift for {family}")
        if item.get("path") != expected["path"]:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: registry path drift for {family}")
        if item.get("semantic_record_digest") != expected["semantic_digest"]:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: registry semantic digest drift for {family}")
        observed_blob = packet_blobs.get(family)
        if item.get("digest") != observed_blob:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: packet Git blob drift for {family}")

    semantic = registry.get("semantic_gate", {})
    if semantic.get("clear_count") != len(EXPECTED_FAMILIES):
        errors.append("OTP-FAMILY-HANDOFFS-001: semantic clear count is not exactly 4")
    if semantic.get("result_family_count") != 12:
        errors.append("OTP-FAMILY-HANDOFFS-001: result-family denominator drift")
    if semantic.get("clear_families") != list(EXPECTED_FAMILIES):
        errors.append("OTP-FAMILY-HANDOFFS-001: clear-family set drift")
    if semantic.get("permanent_scope") != "two encoded variable-leaf targets only":
        errors.append("OTP-FAMILY-HANDOFFS-001: Permanent semantic scope drift")
    if registry.get("blocked_repair_lanes") != EXPECTED_BLOCKED:
        errors.append("OTP-FAMILY-HANDOFFS-001: blocked repair lanes drift")
    if registry.get("permanent_unencoded_successors") != EXPECTED_PERMANENT_UNENCODED:
        errors.append("OTP-FAMILY-HANDOFFS-001: Permanent unencoded-successor boundary drift")

    aggregate = registry.get("aggregate_integration", {})
    if aggregate.get("reopens_family_replay") is not False:
        errors.append("OTP-FAMILY-HANDOFFS-001: All.lean debt reopened family replay")
    if aggregate.get("reopens_semantic_gates") is not False:
        errors.append("OTP-FAMILY-HANDOFFS-001: All.lean debt reopened semantic gates")

    cert = registry.get("cert_state", {})
    for field in ("registered_route_count", "accepted_handoff_count", "adjudication_count", "cert_output_count"):
        if cert.get(field) != 0:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: Cert state inflated: {field}")
    controls = registry.get("route_controls", {})
    if controls.get("aggregate_handoff") is not None:
        errors.append("OTP-FAMILY-HANDOFFS-001: aggregate handoff injected")
    if controls.get("aggregate_route_prohibited") is not True:
        errors.append("OTP-FAMILY-HANDOFFS-001: aggregate route prohibition removed")
    if controls.get("result_family_packets_independent") is not True:
        errors.append("OTP-FAMILY-HANDOFFS-001: packet independence removed")
    for field in (
        "may_offer_packets_before_solve_activation",
        "may_imply_cert_acceptance",
        "may_imply_adjudication",
        "may_promote_claim",
        "permanent_packet_may_route_circuit_or_omitted_formula_conclusions",
    ):
        if controls.get(field) is not False:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: prohibited registry control enabled: {field}")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"result-family handoff validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print(
        "validated four independent content-addressed result-family packets, including the bounded Permanent "
        "variable-leaf packet, zero Cert state, explicit unencoded Permanent successors, GapCVP blocker, "
        "and aggregate-route prohibition"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
