#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from ci.openmath_cex_github_contribution_intake import validate_event
REGISTRY = ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = "work_packages/OPENMATH_2026/HILL_LANES.json"
READBACK = "work_packages/OPENMATH_2026/CORE_CLARITY_LIFECYCLE_READBACK.json"
RAW = "contributions/OPENMATH-2026/OM26-H1/H1-12/raw/OM26-H1-H1-12-IA-001/github-comment-5881108260.md"
RECEIPT = "contributions/OPENMATH-2026/OM26-H1/H1-12/receipts/OM26-H1-H1-12-IA-001/RECOVERY_RECEIPT.json"
BOOTSTRAP = "handoffs/OPENMATH-2026/jobs/OM26-H1-H1-12-IA-001.md"
BOARD = "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
DISPATCH = "contributions/OPENMATH-2026/OM26-H1/H1-12/dispatches/OM26-H1-H1-12-IA-001.json"


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    lanes = load(LANES)
    readback = load(READBACK)
    receipt = load(RECEIPT)
    dispatch = load(DISPATCH)
    raw = (ROOT / RAW).read_text(encoding="utf-8").rstrip("\n")
    bootstrap = (ROOT / BOOTSTRAP).read_text(encoding="utf-8").rstrip("\n")

    event = {
        "issue": {
            "number": 498,
            "title": dispatch["github_issue_title"],
            "body": bootstrap,
        },
        "comment": {
            "id": 5881108260,
            "body": raw,
            "created_at": "2026-09-29T00:10:21Z",
            "user": {"login": "fyremael"},
        },
    }
    try:
        parsed, protected_dispatch, _dispatch_path, operation, observed = validate_event(event, ROOT)
    except Exception as exc:
        errors.append(f"recovered Agent 001 result does not pass current generic intake: {exc}")
    else:
        if parsed["preamble"]["dispatch_id"] != "OM26-H1-H1-12-IA-001":
            errors.append("recovered dispatch identity mismatch")
        if parsed["preamble"]["agent_ref"] != "INDEPENDENT-AGENT-001":
            errors.append("recovered agent identity mismatch")
        if parsed["preamble"]["disposition"] != "PROVED_REDUCTION":
            errors.append("recovered disposition mismatch")
        if protected_dispatch["assignment_id"] != "OM26-H1-H1-12":
            errors.append("protected dispatch assignment mismatch")
        if operation["dispatch_id"] != "OM26-H1-H1-12-IA-001":
            errors.append("protected operation mismatch")
        if observed["comment_id"] != 5881108260:
            errors.append("recovered comment identity mismatch")

    if receipt.get("handling_state") != "CAPTURED_RECOVERED_UNADJUDICATED":
        errors.append("recovery receipt handling state mismatch")
    for key in ("mathematical_correctness_adjudicated", "independence_strength_adjudicated", "canonical_claim_effect", "certification_effect", "competition_effect"):
        if receipt.get(key) is not False:
            errors.append(f"recovery receipt illegally widens {key}")
    if receipt.get("source", {}).get("github_comment_id") != 5881108260:
        errors.append("recovery receipt comment binding mismatch")

    assignments = {x.get("assignment_id"): x for x in registry.get("assignments", [])}
    h1 = assignments.get("OM26-H1-H1-12", {})
    if h1.get("state") != "CAPTURED":
        errors.append("H1 assignment must be CAPTURED")
    if h1.get("lifecycle", {}).get("adjudication") != "PENDING":
        errors.append("H1 adjudication must remain PENDING")
    if h1.get("lease", {}).get("execution_authorized") is not False:
        errors.append("H1 returned lease must not remain executable")
    h2_h7 = [assignments.get(f"OM26-H{i}-WP01", {}) for i in range(2, 8)]
    if any(x.get("state") != "LEASED_NOT_LAUNCHED" for x in h2_h7):
        errors.append("H2-H7 assignments must be LEASED_NOT_LAUNCHED")
    if any(x.get("lifecycle", {}).get("launched") is not False for x in h2_h7):
        errors.append("H2-H7 launch state must be false")
    if registry.get("mathematics_release_policy", {}).get("h2_h7_launched_math_jobs") != 0:
        errors.append("H2-H7 launched counter must be zero")

    issue_map = {x["issue_number"]: x for x in readback.get("issues", [])}
    for issue in range(505, 511):
        row = issue_map.get(issue)
        if row is None or row.get("comment_count") != 0 or row.get("result_comments") != []:
            errors.append(f"issue #{issue} does not support LEASED_NOT_LAUNCHED")
    h1row = issue_map.get(498, {})
    if h1row.get("result_comments") != [{"id": 5881108260, "actor": "fyremael", "created_at": "2026-09-29T00:10:21Z"}]:
        errors.append("H1 lifecycle readback does not identify exact returned result")

    board = (ROOT / BOARD).read_text(encoding="utf-8")
    if "| `OM26-H1-H1-12` | `OM26-H1` | `CAPTURED` |" not in board:
        errors.append("human job board does not show H1 CAPTURED")
    for i in range(2, 8):
        if f"| `OM26-H{i}-WP01` | `OM26-H{i}` | `LEASED_NOT_LAUNCHED` |" not in board:
            errors.append(f"human job board does not show OM26-H{i} LEASED_NOT_LAUNCHED")
    if "No OPENMATH-2026 hill currently has a recorded official competition submission." not in board:
        errors.append("human job board lacks explicit competition submission state")

    hill_map = {x["hill_slot"]: x for x in lanes.get("hills", [])}
    if set(hill_map) != {f"OM26-H{i}" for i in range(1, 8)}:
        errors.append("hill lane cardinality/identity mismatch")
    h1lane = hill_map.get("OM26-H1", {})
    if h1lane.get("external_agent", {}).get("lifecycle_state") != "CAPTURED":
        errors.append("H1 lane does not expose CAPTURED Agent 001 state")
    if h1lane.get("competition_state", {}).get("official_submission") != "NOT_SUBMITTED":
        errors.append("H1 competition state must be explicit NOT_SUBMITTED")
    for i in range(2, 8):
        lane = hill_map.get(f"OM26-H{i}", {})
        if lane.get("active_lease", {}).get("lifecycle_state") != "LEASED_NOT_LAUNCHED":
            errors.append(f"OM26-H{i} lane lifecycle mismatch")
        if lane.get("competition_state", {}).get("official_submission") != "NOT_SUBMITTED":
            errors.append(f"OM26-H{i} competition state must be explicit NOT_SUBMITTED")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH Core Clarity reconciliation preserves Agent 001 and explicit lifecycle/submission state")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
