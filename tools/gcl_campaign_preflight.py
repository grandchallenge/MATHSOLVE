#!/usr/bin/env python3
"""Deterministic preflight for governed GCL campaign operations.

This validator intentionally uses only the Python standard library. It checks
repository-local contracts before reviewer effort or expensive CI is consumed.
It does not certify mathematics and it does not create authority.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class PreflightError(RuntimeError):
    pass


def load_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise PreflightError(f"missing required record: {path.relative_to(ROOT)}") from exc
    except json.JSONDecodeError as exc:
        raise PreflightError(f"invalid JSON in {path.relative_to(ROOT)}: {exc}") from exc


def require(condition: bool, message: str) -> None:
    if not condition:
        raise PreflightError(message)


def git_blob_sha1(path: Path) -> str:
    payload = path.read_bytes()
    framed = f"blob {len(payload)}\0".encode("ascii") + payload
    return hashlib.sha1(framed).hexdigest()


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require_text(path: Path, needle: str) -> None:
    require(path.exists(), f"missing required artifact: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    require(needle in text, f"missing required token {needle!r} in {path.relative_to(ROOT)}")


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: gcl_campaign_preflight.py CAMPAIGN OPERATION", file=sys.stderr)
        return 2

    campaign_id, operation_id = sys.argv[1:]
    state_path = ROOT / ".gcl" / "campaigns" / campaign_id / "CAMPAIGN_STATE.json"
    operation_path = ROOT / ".gcl" / "operations" / operation_id / "OPERATION.json"
    freeze_path = ROOT / ".gcl" / "admission" / operation_id / "FREEZE.json"

    state = load_json(state_path)
    operation = load_json(operation_path)
    freeze = load_json(freeze_path)

    require(state.get("record_type") == "GCL_CAMPAIGN_STATE", "campaign-state record_type mismatch")
    require(operation.get("record_type") == "GCL_OPERATION_CONTRACT", "operation record_type mismatch")
    require(freeze.get("record_type") == "GCL_CONTENT_FREEZE", "freeze record_type mismatch")
    require(state.get("campaign") == campaign_id, "campaign-state identity mismatch")
    require(operation.get("campaign") == campaign_id, "operation campaign mismatch")
    require(operation.get("operation") == operation_id, "operation identity mismatch")
    require(freeze.get("campaign") == campaign_id, "freeze campaign mismatch")
    require(freeze.get("operation") == operation_id, "freeze operation mismatch")
    require(state.get("current_operation") == operation_id, "campaign does not point to this operation")

    math_base = state["protected_inputs"]["math_base"]
    provider = state["protected_inputs"]["provider"]
    constitution = state["authority"]["constitution"]
    require(math_base.endswith(operation["protected_base"]), "protected math base mismatch")
    require(provider.endswith(operation["provider_anchor"]), "provider anchor mismatch")
    require(constitution.endswith(operation["constitutional_anchor"]), "constitutional anchor mismatch")
    require(freeze.get("protected_base") == operation["protected_base"], "freeze protected base mismatch")

    frontier = state["current_frontier"]["id"]
    require(frontier == operation["objective"]["retire_frontier"], "operation does not retire current frontier")
    disposition = operation["candidate_disposition"]
    require(disposition in operation["acceptable_dispositions"], "candidate disposition is not allowed")
    require(state["candidate_disposition"]["type"] == disposition, "campaign/operation disposition mismatch")

    if disposition == "CLOSED":
        next_frontier = state["candidate_disposition"].get("next_frontier_if_protected")
        require(bool(next_frontier), "CLOSED disposition requires next_frontier_if_protected")

    required_completion = {
        "preflight_pass",
        "content_freeze",
        "exact_head_adversary_review",
        "exact_head_referee_review",
        "required_ci_green",
        "protected_merge",
        "protected_readback",
        "completion_receipt",
    }
    require(required_completion.issubset(set(operation["completion_requires"])), "completion gate set is incomplete")

    receipt = operation["completion_receipt"]
    cold_start = state["cold_start"]
    require(
        cold_start.get("completion_receipt_surface") == receipt.get("surface"),
        "campaign cold-start completion receipt surface does not match operation contract",
    )
    require(
        cold_start.get("completion_receipt_validator") == receipt.get("validator"),
        "campaign cold-start receipt validator does not match operation contract",
    )
    receipt_path = ROOT / receipt["surface"]
    require(receipt_path.exists(), "machine completion receipt is missing")
    require(load_json(receipt_path).get("record_type") == "GCL_COMPLETION_RECEIPT", "completion receipt record_type mismatch")
    resolution = state.get("state_resolution", {})
    require("entry_snapshot_rule" in resolution, "campaign state lacks entry-snapshot resolution rule")
    require("completion_overlay_rule" in resolution, "campaign state lacks completion-overlay resolution rule")
    require("stale_receipt_rule" in resolution, "campaign state lacks stale-receipt resolution rule")

    firewall = operation["claim_firewall"]
    for false_fact in state["known_false"]:
        require(false_fact in firewall, f"known-false fact omitted from operation firewall: {false_fact}")
        require(firewall[false_fact] is False, f"known-false fact not preserved false: {false_fact}")

    ledger = ROOT / "work_packages" / "BSD_R2_A1_WP60S_BSS_INVERSE_LIMIT" / "03_CLAIM_LEDGER.yaml"
    require_text(ledger, "BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED")
    require_text(ledger, operation["objective"]["retire_frontier"])
    require_text(ledger, state["candidate_disposition"]["next_frontier_if_protected"])
    for key, value in firewall.items():
        if value is False:
            require_text(ledger, f"{key}: false")

    handoff = ROOT / "handoffs" / campaign_id / "README.md"
    require_text(handoff, "grandchallenge/MATHSOLVE#245")
    require_text(handoff, "BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED")
    handoff_text = handoff.read_text(encoding="utf-8")
    require("closed by WP60R candidate, subject to protected review/merge/readback" not in handoff_text,
            "stale WP60R candidate language remains in canonical handoff")

    workflow_rel = ".github/workflows/bsd-wp60s-certificate.yml"
    workflow_path = ROOT / workflow_rel
    require(workflow_path.exists(), f"missing operation workflow: {workflow_rel}")
    routing = load_json(ROOT / ".ghos-routing" / "workflows.json")
    registered = {entry.get("path") for entry in routing.get("workflows", [])}
    require(workflow_rel in registered, "WP60S workflow is not registered in GH-OS routing")

    for pattern in operation.get("forbidden_successor_globs", []):
        matches = sorted(ROOT.glob(pattern))
        require(not matches, "successor package exists before WP60S disposition: " + ", ".join(str(p.relative_to(ROOT)) for p in matches))

    governed = operation["governed_artifacts"]
    frozen = freeze.get("artifacts", {})
    require(set(frozen) == set(governed), "freeze artifact set does not exactly match operation contract")
    observed_sha256: dict[str, str] = {}
    for rel in governed:
        path = ROOT / rel
        require(path.exists(), f"governed artifact missing: {rel}")
        expected = frozen[rel]
        observed_blob = git_blob_sha1(path)
        require(observed_blob == expected, f"content freeze mismatch for {rel}: expected {expected}, observed {observed_blob}")
        observed_sha256[rel] = sha256_file(path)

    require(receipt.get("surface") == ".gcl/completions/BSD-WP60S/COMPLETION_RECEIPT.json", "completion receipt surface mismatch")
    require("protected_readback_sha" in receipt.get("required_fields", []), "completion receipt must bind protected readback")
    require("staffing_authority" in receipt.get("required_fields", []), "completion receipt must bind current staffing authority")

    freeze_digest = hashlib.sha256(
        json.dumps(observed_sha256, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()

    print(
        json.dumps(
            {
                "status": "PASS",
                "campaign": campaign_id,
                "operation": operation_id,
                "frontier": frontier,
                "candidate_disposition": disposition,
                "completion_receipt_surface": receipt["surface"],
                "frozen_artifacts": len(governed),
                "sha256_freeze_digest": freeze_digest,
                "authority_created": False,
                "mathematics_certified": False,
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except PreflightError as exc:
        print(f"GCL campaign preflight: FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
