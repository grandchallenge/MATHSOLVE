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
