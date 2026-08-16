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
FULL_FORMULA_SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_permanent_full_formula_handoff.schema.json"
REGISTRY_SCHEMA_PATH = ROOT / "schemas" / "openai_ten_proofs_result_family_handoff_registry.schema.json"

EXPECTED_PACKETS = {
    "OTP-F-EHRHART": {
        "family": "OTP-F-EHRHART", "handoff_id": "MC-OTP-HANDOFF-F-EHRHART",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-F-EHRHART.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-F-EHRHART.json",
        "semantic_digest": "a3dc4de4c38a80b7aec1fae6506b08e14d2e58bb",
        "route_id": "MC-ROUTE-OTP-F-EHRHART", "schema": "legacy",
    },
    "OTP-J1-COMPACTNESS": {
        "family": "OTP-J1-COMPACTNESS", "handoff_id": "MC-OTP-HANDOFF-J1-COMPACTNESS",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J1-COMPACTNESS.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J1-COMPACTNESS.json",
        "semantic_digest": "659396358d0d999c00011645f72602f30ccf6b0e",
        "route_id": "MC-ROUTE-OTP-J1-COMPACTNESS", "schema": "legacy",
    },
    "OTP-J2-TWO-DEGENERATE": {
        "family": "OTP-J2-TWO-DEGENERATE", "handoff_id": "MC-OTP-HANDOFF-J2-TWO-DEGENERATE",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-J2-TWO-DEGENERATE.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic_audits/OTP-J2-TWO-DEGENERATE.json",
        "semantic_digest": "7bd168c46921f64364b20021b6315d68f0fde7d0",
        "route_id": "MC-ROUTE-OTP-J2-TWO-DEGENERATE", "schema": "legacy",
    },
    "OTP-C-PERMANENT": {
        "family": "OTP-C-PERMANENT", "handoff_id": "MC-OTP-HANDOFF-C-PERMANENT-FORMULA",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-C-PERMANENT.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT/semantic_audit_record.json",
        "semantic_digest": "3e04bd16bd8a91eaf9b6702de89fcdcc72f61099",
        "route_id": "MC-ROUTE-OTP-C-PERMANENT-FORMULA", "schema": "permanent",
        "protected_blob": "a993c530880021930a2b468e76235b91122ca854",
    },
    "OTP-C-PERMANENT-FULL-FORMULA": {
        "family": "OTP-C-PERMANENT", "handoff_id": "MC-OTP-HANDOFF-C-PERMANENT-FULL-FORMULA",
        "path": "work_packages/OPENAI_TEN_PROOFS_WP00/result_family_handoffs/OTP-C-PERMANENT-FULL-FORMULA.json",
        "semantic_path": "sources/OPENAI-TEN-PROOFS-001/semantic/OTP-C-PERMANENT-FULL-FORMULA-CONSEQUENCES/audit_record.json",
        "semantic_digest": "520bdaa3bba075e411f7a0a2b8422e9c9d42c818",
        "route_id": "MC-ROUTE-OTP-C-PERMANENT-FULL-FORMULA", "schema": "full_formula",
        "protected_blob": "8755a1067963e5b46555872cb46025fff2625295",
    },
}
EXPECTED_KEYS = tuple(EXPECTED_PACKETS)
EXPECTED_CLEAR_FAMILIES = ["OTP-F-EHRHART", "OTP-J1-COMPACTNESS", "OTP-J2-TWO-DEGENERATE", "OTP-C-PERMANENT"]
EXPECTED_BLOCKED = ["OTP-H-GAPCVP"]
EXPECTED_PERMANENT_UNENCODED = [
    "source Theorem 1.1 arithmetic-circuit complexity",
    "historical admitted-PDF byte equivalence",
]
EXPECTED_VARIABLE_PROJECTION = {
    "formula_target_count": 2, "circuit_target_count": 0, "coefficient_field": "complex",
    "dimension_threshold": 32, "log_base": 2,
    "division_free": {"source_theorem": "Theorem 1.2", "variable_leaf_constant": 128, "source_gate_constant": 256,
                      "encoded_variable_leaf_bound": True, "encoded_gate_bound": False, "encoded_total_leaves_vertices": False},
    "rational": {"source_theorem": "Theorem 1.3", "variable_leaf_constant": 192, "source_gate_constant": 384,
                 "encoded_variable_leaf_bound": True, "encoded_gate_bound": False, "encoded_total_leaves_vertices": False},
    "historical_pdf_byte_equivalence": False,
}
EXPECTED_FULL_FORMULA_PROJECTION = {
    "formula_target_count": 2, "circuit_target_count": 0, "coefficient_field": "complex",
    "dimension_threshold": 32, "log_base": 2,
    "division_free": {"source_theorem": "Theorem 1.2", "variable_leaf_constant": 128, "leaf_count_constant": 128,
                      "vertex_count_constant": 128, "internal_gate_constant": 256},
    "rational": {"source_theorem": "Theorem 1.3", "variable_leaf_constant": 192, "leaf_count_constant": 192,
                 "vertex_count_constant": 192, "internal_gate_constant": 384},
    "historical_pdf_byte_equivalence": False,
}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    return hashlib.sha1(f"blob {len(payload)}\0".encode("ascii") + payload, usedforsecurity=False).hexdigest()


def schema_errors(instance: dict[str, Any], schema: dict[str, Any], label: str) -> list[str]:
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [f"{label}: {error.json_path}: {error.message}"
            for error in sorted(validator.iter_errors(instance), key=lambda item: list(item.path))]


def validation_errors(registry: dict[str, Any] | None = None,
                      packets: dict[str, dict[str, Any]] | None = None,
                      packet_blobs: dict[str, str] | None = None) -> list[str]:
    errors: list[str] = []
    registry = load_json(REGISTRY_PATH) if registry is None else registry
    if packets is None:
        packets = {path.stem: load_json(path) for path in sorted(PACKET_DIR.glob("*.json"))}
    if packet_blobs is None:
        packet_blobs = {path.stem: git_blob_sha1(path) for path in sorted(PACKET_DIR.glob("*.json"))}

    schemas = {
        "legacy": load_json(PACKET_SCHEMA_PATH),
        "permanent": load_json(PERMANENT_SCHEMA_PATH),
        "full_formula": load_json(FULL_FORMULA_SCHEMA_PATH),
    }
    errors.extend(schema_errors(registry, load_json(REGISTRY_SCHEMA_PATH), str(REGISTRY_PATH)))

    actual_keys = set(packets)
    expected_keys = set(EXPECTED_KEYS)
    for missing in sorted(expected_keys - actual_keys):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: missing packet {missing}")
    for unknown in sorted(actual_keys - expected_keys):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: unexpected packet {unknown}")

    seen_handoffs: list[str] = []
    seen_routes: list[str] = []
    for key, expected in EXPECTED_PACKETS.items():
        packet = packets.get(key)
        if not isinstance(packet, dict):
            continue
        label = f"OTP-FAMILY-HANDOFFS-001: {key}"
        errors.extend(schema_errors(packet, schemas[expected["schema"]], label))
        if packet.get("result_family") != expected["family"]:
            errors.append(f"{label}: result-family identity drift")
        if packet.get("handoff_id") != expected["handoff_id"]:
            errors.append(f"{label}: handoff identity drift")
        semantic = packet.get("authority", {}).get("semantic_record", {})
        if semantic.get("path") != expected["semantic_path"] or semantic.get("digest") != expected["semantic_digest"]:
            errors.append(f"{label}: semantic-record identity drift")
        requested = packet.get("requested_adjudication", {})
        if requested.get("route_id") != expected["route_id"]:
            errors.append(f"{label}: requested route identity drift")
        if requested.get("current_route_state") != "not_registered" or requested.get("cert_output") is not None:
            errors.append(f"{label}: branch packet inflated Cert state")
        if requested.get("may_adjudicate_on_branch") is not False:
            errors.append(f"{label}: branch packet authorizes adjudication")
        if packet.get("replay_gate", {}).get("state") != "clear" or packet.get("semantic_gate", {}).get("state") != "clear":
            errors.append(f"{label}: protected replay/semantic gate is not clear")
        controls = packet.get("route_controls", {})
        for field in ("may_create_aggregate_handoff", "may_imply_mathcert_acceptance", "may_imply_adjudication",
                      "may_claim_mathematical_proof", "may_promote_claim"):
            if controls.get(field) is not False:
                errors.append(f"{label}: prohibited route control enabled: {field}")
        if controls.get("result_family_only") is not True:
            errors.append(f"{label}: result-family-only boundary removed")
        protected_blob = expected.get("protected_blob")
        if protected_blob and packet_blobs.get(key) != protected_blob:
            errors.append(f"{label}: protected packet blob drift")
        seen_handoffs.append(str(packet.get("handoff_id", "")))
        seen_routes.append(str(requested.get("route_id", "")))

    variable = packets.get("OTP-C-PERMANENT", {})
    if variable.get("target_scope", {}).get("source_projection") != EXPECTED_VARIABLE_PROJECTION:
        errors.append("OTP-FAMILY-HANDOFFS-001: historical Permanent variable-leaf projection drift")
    if variable.get("target_scope", {}).get("lean_theorems") != [
        "PermanentFormulaLowerBound.permanent_divisionFree_formula_logarithmic_lower_bound",
        "PermanentFormulaLowerBound.permanent_rational_formula_logarithmic_lower_bound",
    ]:
        errors.append("OTP-FAMILY-HANDOFFS-001: historical Permanent target set drift")

    full = packets.get("OTP-C-PERMANENT-FULL-FORMULA", {})
    if full.get("target_scope", {}).get("source_projection") != EXPECTED_FULL_FORMULA_PROJECTION:
        errors.append("OTP-FAMILY-HANDOFFS-001: full-formula source projection drift")
    if full.get("target_scope", {}).get("lean_theorems") != [
        "PermanentFormulaLowerBound.permanent_divisionFree_formula_lower_bound",
        "PermanentFormulaLowerBound.permanent_rational_formula_lower_bound",
    ]:
        errors.append("OTP-FAMILY-HANDOFFS-001: full-formula target set drift")
    if full.get("authority", {}).get("human_steward_control_plan_comment") != 5307218742:
        errors.append("OTP-FAMILY-HANDOFFS-001: full-formula Human Steward authority drift")
    if full.get("route_controls", {}).get("historical_variable_leaf_packet_mutable") is not False:
        errors.append("OTP-FAMILY-HANDOFFS-001: historical Permanent packet mutation authority enabled")
    if full.get("route_controls", {}).get("may_route_circuit_theorem") is not False:
        errors.append("OTP-FAMILY-HANDOFFS-001: circuit authority inserted into full-formula packet")

    for duplicate in sorted({x for x in seen_handoffs if seen_handoffs.count(x) > 1}):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: duplicate handoff identity {duplicate}")
    for duplicate in sorted({x for x in seen_routes if seen_routes.count(x) > 1}):
        errors.append(f"OTP-FAMILY-HANDOFFS-001: duplicate requested route identity {duplicate}")

    registry_packets = registry.get("packets", []) if isinstance(registry.get("packets"), list) else []
    expected_paths = [EXPECTED_PACKETS[key]["path"] for key in EXPECTED_KEYS]
    if [item.get("path") for item in registry_packets if isinstance(item, dict)] != expected_paths:
        errors.append("OTP-FAMILY-HANDOFFS-001: registry packet order or path membership drift")
    for key, item in zip(EXPECTED_KEYS, registry_packets):
        if not isinstance(item, dict):
            continue
        expected = EXPECTED_PACKETS[key]
        if item.get("result_family") != expected["family"] or item.get("handoff_id") != expected["handoff_id"]:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: registry identity drift for {key}")
        if item.get("semantic_record_digest") != expected["semantic_digest"]:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: registry semantic digest drift for {key}")
        if item.get("digest") != packet_blobs.get(key):
            errors.append(f"OTP-FAMILY-HANDOFFS-001: packet Git blob drift for {key}")

    semantic = registry.get("semantic_gate", {})
    if semantic.get("clear_count") != 4 or semantic.get("result_family_count") != 12 or semantic.get("packet_count") != 5:
        errors.append("OTP-FAMILY-HANDOFFS-001: family/packet census drift")
    if semantic.get("clear_families") != EXPECTED_CLEAR_FAMILIES:
        errors.append("OTP-FAMILY-HANDOFFS-001: clear-family set drift")
    if registry.get("blocked_repair_lanes") != EXPECTED_BLOCKED:
        errors.append("OTP-FAMILY-HANDOFFS-001: blocked repair lanes drift")
    if registry.get("permanent_unencoded_successors") != EXPECTED_PERMANENT_UNENCODED:
        errors.append("OTP-FAMILY-HANDOFFS-001: Permanent successor boundary drift")

    aggregate = registry.get("aggregate_integration", {})
    if aggregate.get("reopens_family_replay") is not False or aggregate.get("reopens_semantic_gates") is not False:
        errors.append("OTP-FAMILY-HANDOFFS-001: All.lean debt reopened family authority")
    cert = registry.get("cert_state", {})
    for field in ("registered_route_count", "accepted_handoff_count", "adjudication_count", "cert_output_count"):
        if cert.get(field) != 0:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: Cert state inflated: {field}")
    controls = registry.get("route_controls", {})
    if controls.get("aggregate_handoff") is not None or controls.get("aggregate_route_prohibited") is not True:
        errors.append("OTP-FAMILY-HANDOFFS-001: aggregate handoff/route boundary weakened")
    for field in ("may_offer_packets_before_solve_activation", "may_imply_cert_acceptance", "may_imply_adjudication", "may_promote_claim",
                  "permanent_packet_may_route_circuit_or_omitted_formula_conclusions", "historical_permanent_packet_mutable"):
        if controls.get(field) is not False:
            errors.append(f"OTP-FAMILY-HANDOFFS-001: prohibited registry control enabled: {field}")
    if controls.get("result_family_packets_independent") is not True or controls.get("full_formula_successor_packet_separate") is not True:
        errors.append("OTP-FAMILY-HANDOFFS-001: packet independence/successor separation removed")
    return errors


def main() -> int:
    errors = validation_errors()
    if errors:
        print("\n".join(errors), file=sys.stderr)
        print(f"result-family handoff validation failed with {len(errors)} error(s)", file=sys.stderr)
        return 1
    print("validated five independent packets across four cleared families; historical Permanent bytes preserved; full-formula 128/256/192/384 successor closed; circuit and Cert authority excluded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
