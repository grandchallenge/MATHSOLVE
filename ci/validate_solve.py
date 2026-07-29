#!/usr/bin/env python3
"""Validate MATHSOLVE ledgers and bounded tactic-routing contracts."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
WORKSPACE = ROOT.parent
GROBNER_REGISTRY_PATH = ROOT / "governance" / "grobner_tactic_registry.json"
GROBNER_INVOCATION_DIR = ROOT / "examples" / "grobner_tactic_invocations"


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode("ascii") + data).hexdigest()


def schema_path() -> Path:
    candidates = [
        WORKSPACE / "MATH-PROGRAMME" / "schemas" / "claim_ledger.schema.json",
        WORKSPACE / "schemas" / "claim_ledger.schema.json",
        ROOT / "schemas" / "claim_ledger.schema.json",
    ]
    return next(path for path in candidates if path.exists())


def local_schema_path(name: str) -> Path:
    path = ROOT / "schemas" / name
    if not path.is_file():
        raise FileNotFoundError(name)
    return path


def schema_errors(data: Any, name: str, label: str) -> list[str]:
    schema = load_json(local_schema_path(name))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    return [
        f"{label}: {error.json_path}: {error.message}"
        for error in sorted(validator.iter_errors(data), key=lambda item: list(item.path))
    ]


def graph_refs() -> set[str]:
    """Return programme references for all registered Solve campaigns.

    A sibling MATH-PROGRAMME checkout may provide richer live graph nodes. The
    checked-in registry is the deterministic CI fallback and is no longer
    Union-Closed-specific.
    """
    refs: set[str] = set()
    registry_path = ROOT / "contracts" / "programme_reference_registry.json"
    registry = json.loads(registry_path.read_text(encoding="utf-8"))
    for campaign in registry.get("campaigns", {}).values():
        if not isinstance(campaign, dict):
            continue
        refs.update(str(item) for item in campaign.get("knowledge_graph_refs", []))
        refs.update(str(item) for item in campaign.get("classification_mapping_refs", []))

    graph_root = WORKSPACE / "MATH-PROGRAMME" / "knowledge_graph"
    if graph_root.exists():
        for graph_path in sorted(graph_root.glob("*.json")):
            graph = json.loads(graph_path.read_text(encoding="utf-8"))
            refs.update(
                str(node["node_id"])
                for node in graph.get("nodes", [])
                if isinstance(node, dict) and node.get("node_id")
            )
    return refs


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


def grobner_tactic_errors() -> list[str]:
    errors: list[str] = []
    registry_label = str(GROBNER_REGISTRY_PATH.relative_to(ROOT))
    if not GROBNER_REGISTRY_PATH.is_file():
        return [f"{registry_label}: missing governed tactic registry"]

    registry = load_json(GROBNER_REGISTRY_PATH)
    errors.extend(schema_errors(registry, "grobner_tactic_registry.schema.json", registry_label))
    entries = registry.get("invocations", []) if isinstance(registry, dict) else []
    registered_paths = [str(entry.get("path", "")) for entry in entries if isinstance(entry, dict)]
    registered_ids = [str(entry.get("invocation_id", "")) for entry in entries if isinstance(entry, dict)]
    if len(registered_paths) != len(set(registered_paths)):
        errors.append(f"{registry_label}: duplicate invocation path")
    if len(registered_ids) != len(set(registered_ids)):
        errors.append(f"{registry_label}: duplicate invocation_id")

    discovered = {
        path.relative_to(ROOT).as_posix()
        for path in GROBNER_INVOCATION_DIR.rglob("*.json")
    }
    registered = set(registered_paths)
    if not discovered:
        errors.append("Groebner tactic coverage: zero invocations discovered")
    for missing in sorted(registered - discovered):
        errors.append(f"Groebner tactic coverage: registered invocation is missing: {missing}")
    for orphan in sorted(discovered - registered):
        errors.append(f"Groebner tactic coverage: unregistered invocation: {orphan}")

    witness_required = {
        "witness_available",
        "ready_for_mathcert",
        "submitted",
        "certified",
        "qualified",
        "rejected",
        "proof_debt",
    }
    adjudicated = {"certified", "qualified", "rejected", "proof_debt"}

    for entry in entries:
        if not isinstance(entry, dict):
            continue
        relative = str(entry.get("path", ""))
        path = ROOT / relative
        if not path.is_file():
            continue
        actual_blob = git_blob_sha1(path)
        if actual_blob != entry.get("git_blob_sha1"):
            errors.append(
                f"{relative}: git_blob_sha1 mismatch; expected {entry.get('git_blob_sha1')}, found {actual_blob}"
            )
        invocation = load_json(path)
        errors.extend(schema_errors(invocation, "grobner_tactic_invocation.schema.json", relative))
        if invocation.get("invocation_id") != entry.get("invocation_id"):
            errors.append(f"{relative}: invocation_id does not match registry")
        status = invocation.get("status")
        if status != entry.get("status"):
            errors.append(f"{relative}: status does not match registry")

        variables = invocation.get("variables", {})
        names = variables.get("names", []) if isinstance(variables, dict) else []
        variable_count = variables.get("variable_count") if isinstance(variables, dict) else None
        if variable_count != len(names):
            errors.append(f"{relative}: variables.variable_count must equal len(variables.names)")
        budget = invocation.get("resource_budget", {})
        if isinstance(variable_count, int) and isinstance(budget, dict):
            if variable_count > budget.get("max_variables", -1):
                errors.append(f"{relative}: variable count exceeds route budget")

        witness_source = invocation.get("witness_source")
        handoff = invocation.get("handoff", {})
        acknowledgement = handoff.get("intake_acknowledgement") if isinstance(handoff, dict) else None
        cert_output = handoff.get("mathcert_output") if isinstance(handoff, dict) else None
        if status in witness_required and not isinstance(witness_source, dict):
            errors.append(f"{relative}: {status} requires content-addressed witness_source")
        if status in {"submitted", *adjudicated} and not str(acknowledgement or "").strip():
            errors.append(f"{relative}: {status} requires MATHCERT intake acknowledgement")
        if status in adjudicated:
            if not isinstance(cert_output, dict):
                errors.append(f"{relative}: {status} requires content-addressed MATHCERT output")
            elif cert_output.get("disposition") != status:
                errors.append(f"{relative}: MATHCERT output disposition does not match status")
        elif cert_output is not None:
            errors.append(f"{relative}: intake state must not claim a MATHCERT output")

        failure = invocation.get("failure_record", {})
        failure_status = failure.get("status") if isinstance(failure, dict) else None
        failure_entries = failure.get("entries", []) if isinstance(failure, dict) else []
        if failure_status == "none" and failure_entries:
            errors.append(f"{relative}: failure_record status none requires zero entries")
        if failure_status == "recorded" and not failure_entries:
            errors.append(f"{relative}: recorded failure requires at least one entry")
        if status in {"rejected", "proof_debt"} and not failure_entries:
            errors.append(f"{relative}: {status} requires a failure record")
    return errors


def main() -> int:
    allowed_graph_refs = graph_refs()
    seen_claim_ids: dict[str, Path] = {}
    errors: list[str] = []
    paths = sorted(ROOT.rglob("*claim*ledger*.yaml"))
    for path in paths:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        errors.extend(validate_ledger(data, path, allowed_graph_refs, seen_claim_ids))
    errors.extend(grobner_tactic_errors())
    for name in (
        "grobner_tactic_invocation.schema.json",
        "grobner_tactic_registry.schema.json",
    ):
        Draft202012Validator.check_schema(load_json(local_schema_path(name)))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(
        f"validated {len(paths)} MATHSOLVE claim ledger(s) plus governed bounded Groebner tactic routing"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
