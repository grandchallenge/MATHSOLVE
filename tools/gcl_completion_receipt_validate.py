#!/usr/bin/env python3
"""Validate the authoritative BSD-WP60S GCL-CEX completion receipt."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RECEIPT_PATH = ROOT / ".gcl" / "completions" / "BSD-WP60S" / "COMPLETION_RECEIPT.json"

EXPECTED_CANDIDATE = "93a5e27028c2ea189eb9db90a6a13cdf92a060f6"
EXPECTED_MERGE = "b6f4a11425b5b6f75da24b7c13b4b7a97bd82927"
EXPECTED_GCL_CEX = "f20623dc6f8e8ef8c7c04ba4823f2773e2a0f407"
EXPECTED_INTELLECT = "2badd8c3197ef4515591bba05ff782ff3cafc930"
EXPECTED_PROVIDER = "770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074"
EXPECTED_FRONTIER = "MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS"
EXPECTED_NEXT = "MISSING_LITERAL_P2_BSS_THEOREM_6_12_COROLLARY_6_15_APPLICATION_REPLAY_WITHOUT_INFINITE_H3"
EXPECTED_FALSE = [
    "formal_higher_level_hypothesis_3_2_iii",
    "full_bss_hypothesis_4_7",
    "bss_hypothesis_4_7_iii",
    "infinite_bss_h3",
    "bss_theorem_6_12",
    "bss_corollary_6_15",
    "r5_lift",
    "r5_prim",
    "d2d",
    "bsd_r2_a1",
    "mathcert_certification",
]
EXPECTED_CHECKS = {
    ("candidate", "BSD WP60S inverse-limit theorem replay", 35039279742, EXPECTED_CANDIDATE),
    ("candidate", "BSD WP60Q selected residual core graph", 35039279777, EXPECTED_CANDIDATE),
    ("candidate", "BSD WP60R finite BSS theorem replay", 35039279807, EXPECTED_CANDIDATE),
    ("candidate", "GCL conformance", 35039280139, EXPECTED_CANDIDATE),
    ("candidate", "Solve checks", 35039279747, EXPECTED_CANDIDATE),
    ("protected_readback", "BSD WP60S inverse-limit theorem replay", 35039487602, EXPECTED_MERGE),
    ("protected_readback", "BSD WP60Q selected residual core graph", 35039487690, EXPECTED_MERGE),
    ("protected_readback", "BSD WP60R finite BSS theorem replay", 35039487721, EXPECTED_MERGE),
    ("protected_readback", "Solve checks", 35039487649, EXPECTED_MERGE),
    ("protected_readback", "GCL conformance", 35039488239, EXPECTED_MERGE),
}


class ReceiptError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ReceiptError(message)


def main() -> int:
    receipt = json.loads(RECEIPT_PATH.read_text(encoding="utf-8"))
    require(receipt["record_type"] == "GCL_COMPLETION_RECEIPT", "record_type mismatch")
    require(receipt["campaign"] == "BSD-001", "campaign mismatch")
    require(receipt["operation"] == "BSD-WP60S", "operation mismatch")
    require(receipt["candidate_head"] == EXPECTED_CANDIDATE, "candidate head mismatch")
    require(receipt["merge_sha"] == EXPECTED_MERGE, "merge identity mismatch")
    require(receipt["protected_readback_sha"] == EXPECTED_MERGE, "protected readback mismatch")

    standard = receipt["enforcement_standard"]
    require(standard["identifier"] == "GCL-CEX-01", "execution standard mismatch")
    require(standard["repository"] == "grandchallenge/gcl-standards", "standard repository mismatch")
    require(standard["commit"] == EXPECTED_GCL_CEX, "GCL-CEX enforcement anchor mismatch")

    staffing = receipt["staffing_authority"]
    require(staffing["repository"] == "grandchallenge/INTELLECT", "staffing authority repository mismatch")
    require(staffing["directive"] == "GI-STEWARD-0003", "staffing directive mismatch")
    require(staffing["separation_model"] == "role_scoped_logical_passes", "separation model mismatch")
    require(staffing["protected_anchor"] == EXPECTED_INTELLECT, "INTELLECT staffing anchor mismatch")

    adversary = receipt["adversary_record"]
    referee = receipt["referee_record"]
    require(adversary["role"] == "Adversary", "Adversary role mismatch")
    require(referee["role"] == "Referee", "Referee role mismatch")
    require(adversary["mode"] == referee["mode"] == "non_authoring_read_only", "reviews must be read-only")
    require(adversary["reviewed_repository"] == referee["reviewed_repository"] == "grandchallenge/MATHSOLVE", "review repository mismatch")
    require(adversary["reviewed_candidate_head"] == referee["reviewed_candidate_head"] == EXPECTED_CANDIDATE, "reviewed candidate mismatch")
    require(adversary["logical_pass_id"] != referee["logical_pass_id"], "logical review passes must differ")
    require(adversary["record_ref"] != referee["record_ref"], "durable review records must differ")
    require(adversary["finding"] == referee["finding"] == "approved", "both review findings must approve")
    require(not adversary["unresolved_obligations"] and not referee["unresolved_obligations"], "approved reviews cannot retain unresolved obligations")
    for review in (adversary, referee):
        require(not any(bool(value) for value in review["authority_claims"].values()), "review cannot manufacture authority or certification")
    require(
        (tuple(sorted(adversary["criteria"])), tuple(sorted(adversary["evidence"])))
        != (tuple(sorted(referee["criteria"])), tuple(sorted(referee["evidence"]))),
        "duplicated analysis is not functional separation",
    )

    observed = set()
    routing_seen = False
    for check in receipt["required_checks"]:
        require(check["result"] == "success", "non-success check in receipt")
        require(check["phase"] in {"candidate", "protected_readback"}, "invalid check phase")
        expected_head = EXPECTED_CANDIDATE if check["phase"] == "candidate" else EXPECTED_MERGE
        require(check["head"] == expected_head, "stale check head")
        if "run" in check:
            observed.add((check["phase"], check["name"], check["run"], check["head"]))
        elif check.get("name") == "routing-enforcement":
            require(check.get("check_run") == 104614934010, "routing check identity mismatch")
            require(check["phase"] == "candidate", "routing evidence must bind candidate")
            routing_seen = True
        else:
            raise ReceiptError("check lacks governed run identity")
    require(EXPECTED_CHECKS.issubset(observed), "required theorem/CI evidence missing")
    require(routing_seen, "routing-enforcement evidence missing")

    disposition = receipt["disposition"]
    require(disposition["type"] == "CLOSED", "WP60S disposition must be CLOSED")
    require(disposition["frontier"] == EXPECTED_FRONTIER, "retired frontier mismatch")
    require(disposition["established"] == ["BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED"], "established disposition mismatch")
    require(disposition["next_frontier"] == EXPECTED_NEXT, "next frontier mismatch")
    require(set(receipt["preserved_false"]) == set(EXPECTED_FALSE), "preserved-false firewall mismatch")

    ledger = (ROOT / "work_packages" / "BSD_R2_A1_WP60S_BSS_INVERSE_LIMIT" / "03_CLAIM_LEDGER.yaml").read_text(encoding="utf-8")
    require("BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED" in ledger, "ledger disposition missing")
    for key in EXPECTED_FALSE:
        require(f"{key}: false" in ledger, f"ledger firewall missing: {key}")
    require(EXPECTED_PROVIDER in (ROOT / ".gcl" / "operations" / "BSD-WP60S" / "OPERATION.json").read_text(encoding="utf-8"), "provider anchor missing from operation contract")

    print(json.dumps({
        "status": "PASS",
        "campaign": "BSD-001",
        "operation": "BSD-WP60S",
        "candidate_head": EXPECTED_CANDIDATE,
        "protected_readback": EXPECTED_MERGE,
        "review_separation": "role_scoped_logical_passes",
        "disposition": "CLOSED",
        "next_frontier": EXPECTED_NEXT,
        "mathcert_certified": False,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except ReceiptError as exc:
        print(f"GCL completion receipt: FAIL: {exc}")
        raise SystemExit(1)
