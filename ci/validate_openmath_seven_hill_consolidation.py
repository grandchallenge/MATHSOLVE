#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANES = "work_packages/OPENMATH_2026/HILL_LANES.json"
REGISTRY = ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
HISTORICAL = "work_packages/OPENMATH_2026/HISTORICAL_TRANCHE_REGISTRY.json"
BOARD = "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
EXPECTED = [f"OM26-H{i}" for i in range(1, 8)]


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def git_blob_sha1(rel: str) -> str:
    data = (ROOT / rel).read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    lanes = load(LANES)
    registry = load(REGISTRY)
    historical = load(HISTORICAL)

    lane_topology = lanes.get("current_topology", {})
    if lane_topology.get("lane_model") != "SEVEN_FIRST_CLASS_HILLS":
        errors.append("HILL_LANES current topology model mismatch")
    if lane_topology.get("hills") != EXPECTED:
        errors.append("HILL_LANES current hill roster mismatch")
    if lane_topology.get("grouped_current_lanes") != []:
        errors.append("HILL_LANES still exposes grouped current lanes")
    if [x.get("hill_slot") for x in lanes.get("hills", [])] != EXPECTED:
        errors.append("HILL_LANES rows are not exactly H1-H7 in order")

    # Deprecated topology syntax is forbidden on current operational surfaces.
    # Historical provenance remains immutable and is validated separately below.
    deprecated = "H2-H7"
    for hill in lanes.get("hills", []):
        active_projection = {
            "hill_slot": hill.get("hill_slot"),
            "status": hill.get("status"),
            "obligations": hill.get("obligations"),
            "next_action": hill.get("next_action"),
            "active_lease": hill.get("active_lease"),
            "competition_state": hill.get("competition_state"),
        }
        if deprecated in json.dumps(active_projection, sort_keys=True):
            errors.append(f"{hill.get('hill_slot')}: deprecated H2-H7 syntax leaked into current hill projection")
    if deprecated in lanes.get("claim_boundary", ""):
        errors.append("HILL_LANES current claim boundary reintroduces deprecated H2-H7 grouping")

    assignment_topology = registry.get("current_topology", {})
    if assignment_topology.get("lane_model") != "SEVEN_FIRST_CLASS_HILLS":
        errors.append("assignment current topology model mismatch")
    if assignment_topology.get("hills") != EXPECTED:
        errors.append("assignment current hill roster mismatch")
    if "H2-H7 is not a current assignment domain" not in assignment_topology.get("rule", ""):
        errors.append("assignment topology does not explicitly retire H2-H7 as current domain")

    mapping = registry.get("slot_binding_policy", {}).get("mapping", {})
    if set(mapping) != set(EXPECTED):
        errors.append("slot-binding current mapping is not exactly seven hills")

    policy = registry.get("mathematics_release_policy", {})
    per_hill = policy.get("per_hill", {})
    if list(per_hill) != EXPECTED:
        errors.append("mathematics release policy is not ordered H1-H7")
    if per_hill.get("OM26-H1", {}).get("agent_state") != "ACCEPTED":
        errors.append("H1 current agent state mismatch")
    if per_hill.get("OM26-H2", {}).get("agent_state") != "LEASED_NOT_LAUNCHED":
        errors.append("H2 current agent state mismatch")
    if per_hill.get("OM26-H2", {}).get("assignment") != "OM26-H2-WP03":
        errors.append("H2 current assignment mismatch")
    predecessor = per_hill.get("OM26-H2", {}).get("predecessor", {})
    if predecessor.get("assignment") != "OM26-H2-WP02" or predecessor.get("agent_state") != "ACCEPTED":
        errors.append("H2 predecessor state mismatch")
    for i in range(3, 8):
        if per_hill.get(f"OM26-H{i}", {}).get("agent_state") != "LEASED_NOT_LAUNCHED":
            errors.append(f"OM26-H{i} current agent state mismatch")
    if policy.get("historical_tranche_metrics", {}).get("deprecated_for_current_state") is not True:
        errors.append("historical aggregate metrics are not deprecated")

    current_registry_surfaces = {
        "per_hill": per_hill,
        "return_policy": registry.get("return_policy", {}),
        "launch_contract": registry.get("launch_contract", {}),
        "claim_boundary": registry.get("claim_boundary", ""),
    }
    if deprecated in json.dumps(current_registry_surfaces, sort_keys=True):
        errors.append("deprecated H2-H7 syntax leaked into current registry operational surfaces")

    if historical.get("current_topology_authority", {}).get("hills") != EXPECTED:
        errors.append("historical registry points to wrong current topology")
    if historical.get("current_topology_authority", {}).get("lane_model") != "SEVEN_FIRST_CLASS_HILLS":
        errors.append("historical registry current topology model mismatch")
    if "SHALL NOT define current campaign topology" not in historical.get("rule", ""):
        errors.append("historical registry lacks current-authority exclusion")

    seen = set()
    for tranche in historical.get("historical_tranches", []):
        if tranche.get("status") != "CLOSED__HISTORICAL_PROVENANCE_ONLY":
            errors.append(f"{tranche.get('id')}: not historical-only")
        if tranche.get("current_authority") is not False:
            errors.append(f"{tranche.get('id')}: still marked current authority")
        for artifact in tranche.get("artifacts", []):
            rel = artifact.get("path")
            expected_sha = artifact.get("git_blob_sha1")
            if rel in seen:
                errors.append(f"duplicate historical artifact {rel}")
                continue
            seen.add(rel)
            path = ROOT / rel
            if not path.is_file():
                errors.append(f"missing historical artifact {rel}")
                continue
            actual = git_blob_sha1(rel)
            if actual != expected_sha:
                errors.append(f"historical artifact bytes drift: {rel} expected={expected_sha} actual={actual}")

    for completion in (
        ".gcl/completions/OM26-H2-H7-SOURCE-ACQ/COMPLETION_RECEIPT.json",
        ".gcl/completions/OM26-H2-H7-WP01-DECOMPOSITION/COMPLETION_RECEIPT.json",
        ".gcl/completions/OM26-H2-H7-WP01-LEASES/COMPLETION_RECEIPT.json",
    ):
        state = load(completion).get("state", "")
        if not state.startswith("CLOSED"):
            errors.append(f"historical tranche receipt is not closed: {completion}")

    board = (ROOT / BOARD).read_text(encoding="utf-8")
    if "## Current seven-hill independent-agent lifecycle" not in board:
        errors.append("human board lacks seven-hill current topology heading")
    if "Historical aggregate labels such as `H2-H7` identify closed onboarding tranches only" not in board:
        errors.append("human board does not classify H2-H7 as historical")
    if "The H2-H7 leases are" in board:
        errors.append("human board still presents H2-H7 as a current lease bloc")
    for i in range(1, 8):
        if f"`OM26-H{i}`" not in board:
            errors.append(f"human board missing OM26-H{i}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH current topology is seven first-class hills; H2-H7 aggregates are historical-only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
