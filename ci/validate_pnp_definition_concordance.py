#!/usr/bin/env python3
"""Fail-closed checks for PNP-DEFINITION-CONCORDANCE-001."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RECORD = ROOT / "work_packages/PNP_DEFINITION_CONCORDANCE_001/concordance.json"
ROUTE = ROOT / "formal_sources/formal_conjectures/MS-FC-WP01.json"
CONTRACT = ROOT / "contracts/formal_conjectures_expanded_evidence.json"
MANIFEST = ROOT / "campaign_manifests/PNP-001.json"
HANDOFF = ROOT / "cert_handoffs/PNP-001.json"

EXPECTED_SOURCES = {
    "formal_statement": ("85f863718beeec7b58a3a1926ee92e3472bc2020", "255b60b9fc875a38481b1fbaba7f4b9c8928da70"),
    "formal_dependency_lock": ("85f863718beeec7b58a3a1926ee92e3472bc2020", "13a1771e215c0200be3db3d1d6881017a1f5d179"),
    "formal_pair_encoding": ("85f863718beeec7b58a3a1926ee92e3472bc2020", "984fbbae61764f13e26ba57f1afd1c78f630b968"),
    "mathlib_machine_and_cost": ("a3a10db0e9d66acbebf76c5e6a135066525ac900", "04c41973bab9aa1fda13e2316dbfbb2bbbaaa6ab"),
    "mathlib_encoding_contract": ("a3a10db0e9d66acbebf76c5e6a135066525ac900", "d746f48947b813e938288f9ef00a0ae65e718df6"),
    "programme_charter": ("32fc4d3a792c4e7dd2fcdf680768b7fb264979b3", "810867b34aaf4007e78650a69cec63f5003deafd"),
    "programme_machine_lock": ("32fc4d3a792c4e7dd2fcdf680768b7fb264979b3", "f33ad992159fc2dc7d17e52cf2e376b57c146f79"),
}
EXPECTED_CHECKS = {
    "PNP-CONC-ORIENTATION-001": "matched",
    "PNP-CONC-PROOF-001": "placeholder_not_evidence",
    "PNP-CONC-CARRIER-001": "matched_with_unproved_bridge",
    "PNP-CONC-ENCODING-001": "matched",
    "PNP-CONC-TOTALITY-001": "matched",
    "PNP-CONC-MALFORMED-001": "not_applicable_at_class_level",
    "PNP-CONC-UNIFORMITY-001": "matched",
    "PNP-CONC-MACHINE-001": "matched_with_unproved_bridge",
    "PNP-CONC-POLYTIME-001": "matched_with_unproved_bridge",
    "PNP-CONC-NP-001": "matched_with_unproved_bridge",
    "PNP-CONC-REDUCTION-001": "absent",
}
EXPECTED_BRIDGES = {
    "PNP-BRIDGE-CARRIER-001",
    "PNP-BRIDGE-MODEL-001",
    "PNP-BRIDGE-POLYBOUND-001",
    "PNP-BRIDGE-NP-001",
    "PNP-BRIDGE-ENDPOINT-001",
}
EXPECTED_DISPOSITION = "DEFINITION_CONCORDANCE_AUDITED__KERNEL_EQUIVALENCE_AND_MODEL_BRIDGES_OPEN"


def load(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    try:
        record = load(root / RECORD.relative_to(ROOT))
        route = load(root / ROUTE.relative_to(ROOT))
        contract = load(root / CONTRACT.relative_to(ROOT))
        manifest = load(root / MANIFEST.relative_to(ROOT))
        handoff = load(root / HANDOFF.relative_to(ROOT))
    except (OSError, json.JSONDecodeError) as exc:
        return [f"PNP concordance load failed: {exc}"]

    if record.get("schema_version") != "1.0.0" or record.get("concordance_id") != "PNP-DEFINITION-CONCORDANCE-001":
        errors.append("PNP concordance identity drift")
    if record.get("campaign_id") != "PNP-001":
        errors.append("PNP concordance campaign drift")
    if record.get("governance_issue") != "https://github.com/grandchallenge/MATHSOLVE/issues/145":
        errors.append("PNP concordance governance issue drift")

    sources = record.get("sources", {})
    if set(sources) != set(EXPECTED_SOURCES):
        errors.append("PNP concordance source set drift")
    for name, (commit, blob) in EXPECTED_SOURCES.items():
        source = sources.get(name, {})
        if source.get("commit_sha") != commit or source.get("git_blob_sha1") != blob:
            errors.append(f"{name}: pinned source identity drift")
    if sources.get("formal_dependency_lock", {}).get("mathlib_commit_sha") != "a3a10db0e9d66acbebf76c5e6a135066525ac900":
        errors.append("Formal Conjectures mathlib dependency drift")

    checks = record.get("checks", [])
    by_id = {item.get("check_id"): item for item in checks if isinstance(item, dict)}
    if len(by_id) != len(checks) or set(by_id) != set(EXPECTED_CHECKS):
        errors.append("PNP concordance check coverage drift")
    for check_id, disposition in EXPECTED_CHECKS.items():
        if by_id.get(check_id, {}).get("disposition") != disposition:
            errors.append(f"{check_id}: disposition drift")

    bridges = record.get("open_bridges", [])
    bridge_ids = {item.get("bridge_id") for item in bridges if isinstance(item, dict)}
    if len(bridge_ids) != len(bridges) or bridge_ids != EXPECTED_BRIDGES:
        errors.append("PNP open bridge coverage drift")
    for item in by_id.values():
        bridge_id = item.get("bridge_id")
        if bridge_id is not None and bridge_id not in bridge_ids:
            errors.append(f"{item.get('check_id')}: unresolved bridge reference")

    interface = record.get("exact_theorem_interface", {})
    if interface.get("upstream_theorem") != "ComplexityTheory.P_ne_NP":
        errors.append("PNP exact theorem interface drift")
    if interface.get("admitted_use") != "separation_side_candidate_only":
        errors.append("PNP theorem orientation was broadened")
    if interface.get("mathcert_route_state") != "pending":
        errors.append("PNP concordance must retain pending MATHCERT state")
    if set(interface.get("required_bridge_ids", [])) != EXPECTED_BRIDGES - {"PNP-BRIDGE-ENDPOINT-001"}:
        errors.append("PNP theorem-interface bridge set drift")
    if interface.get("concrete_endpoint_bridge_id") != "PNP-BRIDGE-ENDPOINT-001":
        errors.append("PNP concrete endpoint bridge drift")

    if record.get("disposition") != EXPECTED_DISPOSITION:
        errors.append("PNP concordance disposition drift")
    if record.get("certification_effect") != "none":
        errors.append("PNP concordance cannot change certification")
    if record.get("next_solve_target", {}).get("target_id") != "PNP-BRIDGE-001":
        errors.append("PNP next bridge target drift")
    boundary = str(record.get("claim_boundary", ""))
    for phrase in ("does not prove P != NP", "does not prove", "does not resolve"):
        if phrase in boundary:
            break
    else:
        errors.append("PNP claim boundary does not disclaim proof")

    pnp_route = next((item for item in route.get("routes", []) if item.get("campaign_id") == "PNP-001"), {})
    if pnp_route.get("disposition") != "definition-concordance-audited-bridges-open":
        errors.append("MS-FC-WP01 does not consume the PNP concordance result")
    if pnp_route.get("concordance_id") != "PNP-DEFINITION-CONCORDANCE-001":
        errors.append("MS-FC-WP01 PNP concordance identity missing")
    pnp_contract = contract.get("campaigns", {}).get("PNP-001", {})
    if pnp_contract.get("disposition") != "definition-concordance-audited-bridges-open":
        errors.append("expanded-evidence contract retains stale PNP disposition")

    if manifest.get("cert") is not None:
        errors.append("unexpected manifest authority field")
    if manifest.get("certification", {}).get("handoff_state") != "pending":
        errors.append("PNP manifest route changed from pending")
    if manifest.get("promotion", {}).get("eligible") is not False:
        errors.append("PNP concordance cannot make promotion eligible")
    if handoff.get("status") != "pending":
        errors.append("PNP handoff changed from pending")
    if handoff.get("target_claims", [{}])[0].get("support_type") != "SPECIALIST_AUDIT_PENDING":
        errors.append("PNP terminal target support was inflated")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PNP definition concordance validated: 11 scoped findings, five open bridges, pending Cert route, and no theorem promotion.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
