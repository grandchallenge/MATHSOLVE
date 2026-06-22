#!/usr/bin/env python3
"""Validate MATHSOLVE ledgers against programme contracts."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent


def schema_path() -> Path:
    candidates = [
        WORKSPACE / "MATH-PROGRAMME" / "schemas" / "claim_ledger.schema.json",
        WORKSPACE / "schemas" / "claim_ledger.schema.json",
        ROOT / "schemas" / "claim_ledger.schema.json",
    ]
    return next(path for path in candidates if path.exists())


def graph_refs() -> set[str]:
    graph_path = WORKSPACE / "MATH-PROGRAMME" / "knowledge_graph" / "union_closed.json"
    if graph_path.exists():
        graph = json.loads(graph_path.read_text(encoding="utf-8"))
        return {node["node_id"] for node in graph["nodes"]}
    contract = json.loads(
        (ROOT / "contracts" / "classification_discovery_refs.json").read_text(encoding="utf-8")
    )
    return set(contract["knowledge_graph_refs"])


def validate_ledger(
    data: Any,
    path: Path,
    allowed_graph_refs: set[str],
    seen_claim_ids: dict[str, Path],
) -> list[str]:
    schema = json.loads(schema_path().read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    errors = [
        f"{path}: {error.json_path}: {error.message}"
        for error in validator.iter_errors(data)
    ]
    if not isinstance(data, dict) or not isinstance(data.get("claims"), list):
        return errors
    for claim in data["claims"]:
        if not isinstance(claim, dict):
            continue
        claim_id = claim.get("claim_id")
        if claim_id in seen_claim_ids:
            errors.append(f"{path}: duplicate claim_id {claim_id}; first seen in {seen_claim_ids[claim_id]}")
        elif claim_id:
            seen_claim_ids[claim_id] = path
        for graph_ref in claim.get("knowledge_graph_refs", []):
            if graph_ref not in allowed_graph_refs:
                errors.append(f"{path}: {claim_id}: unresolved knowledge_graph_ref {graph_ref}")
    errors.extend(validate_foundation_doctrine(data, path))
    return errors


def validate_foundation_doctrine(data: Any, path: Path) -> list[str]:
    if not isinstance(data, dict) or "foundation_doctrine_version" not in data:
        return []

    errors: list[str] = []
    if data.get("foundation_doctrine_version") != 1:
        errors.append(f"{path}: foundation_doctrine_version must be 1")

    profile = data.get("foundational_profile")
    if not isinstance(profile, dict):
        errors.append(f"{path}: foundational_profile must be present for foundation-aware ledgers")
    else:
        for field in (
            "carrier_type",
            "carrier_description",
            "ambient_structure",
            "admissible_operations",
            "regularity",
            "axiom_profile",
            "witness_policy",
            "pathology_risk",
        ):
            if field not in profile:
                errors.append(f"{path}: foundational_profile missing {field}")
        axiom_profile = profile.get("axiom_profile")
        if isinstance(axiom_profile, dict) and axiom_profile.get("choice_usage") == "unknown":
            errors.append(f"{path}: foundational_profile.axiom_profile.choice_usage must not be unknown")
        pathology_risk = profile.get("pathology_risk")
        if isinstance(pathology_risk, dict) and pathology_risk.get("level") == "unknown":
            errors.append(f"{path}: foundational_profile.pathology_risk.level must not be unknown")

    routing = data.get("foundation_routing")
    if not isinstance(routing, dict):
        errors.append(f"{path}: foundation_routing must be present for foundation-aware ledgers")
        return errors

    if routing.get("selected_route") not in {"R0", "R1", "R2", "R3", "R4", "R5"}:
        errors.append(f"{path}: foundation_routing.selected_route is invalid")
    if routing.get("foundational_profile_used") is not True:
        errors.append(f"{path}: foundation_routing.foundational_profile_used must be true")
    if not str(routing.get("route_reason", "")).strip():
        errors.append(f"{path}: foundation_routing.route_reason must not be empty")

    boundary = routing.get("certificate_boundary")
    if not isinstance(boundary, dict):
        errors.append(f"{path}: foundation_routing.certificate_boundary must be present")
    else:
        if boundary.get("target") not in {"Lean", "Coq", "SAT", "SMT", "PB", "CAS", "interval", "human_audit", "none", "unknown"}:
            errors.append(f"{path}: foundation_routing.certificate_boundary.target is invalid")
        checker_inputs = boundary.get("checker_inputs")
        if not isinstance(checker_inputs, list) or not checker_inputs:
            errors.append(f"{path}: foundation_routing.certificate_boundary.checker_inputs must be a nonempty list")
    return errors


def main() -> int:
    allowed_graph_refs = graph_refs()
    seen_claim_ids: dict[str, Path] = {}
    errors = []
    paths = sorted(ROOT.rglob("*claim*ledger*.yaml"))
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors.extend(validate_ledger(data, path, allowed_graph_refs, seen_claim_ids))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"validated {len(paths)} MATHSOLVE claim ledger(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
