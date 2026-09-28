#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
BOARD = "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
CEX_CAMPAIGN = ".gcl/campaigns/OPENMATH-2026-SOURCE-ACQ/CAMPAIGN_STATE.json"
OPERATION = ".gcl/operations/OM26-H2-H7-SOURCE-ACQ/OPERATION.json"
PREP = "work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json"
WORKFLOW = ".github/workflows/openmath-cex-job-board.yml"
ROUTING = ".ghos-routing/workflows.json"
EXPECTED_SLOTS = [f"OM26-H{i}" for i in range(2, 8)]
EXPECTED_ASSIGNMENTS = [f"{slot}-SOURCE-ACQ" for slot in EXPECTED_SLOTS]


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def render_board(registry: dict) -> str:
    rows = []
    for item in registry["assignments"]:
        rows.append(
            f'| `{item["assignment_id"]}` | `{item["slot"]}` | '
            f'`{item["class"]}` | `{item["state"]}` | '
            f'`{item["work_package"]}` |'
        )
    return """# OPENMATH-2026 CEX job board

This is the human discovery surface for external CEX work. The machine authority is `.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json` on protected `main`.

## Pickup rule

External agents do **not** choose or claim work by browsing the repository.

A launched worker receives a `dispatch_id`. It reads the machine registry, finds the unique assignment whose protected lease names that `dispatch_id`, loads exactly that assignment's `work_package`, and executes only that package.

If no matching protected lease exists, the worker returns `NO_ACTIVE_LEASE` and stops.

`AVAILABLE_FOR_LEASE` means visible to the allocator, not executable by an external worker. `LEASED` is the only executable state.

## Current assignments

| Assignment | Slot | Class | State | Work package |
|---|---|---|---|---|
""" + "\n".join(rows) + """

No H2-H7 mathematical hill-climbing package is executable yet. Those packages may be instantiated only after the corresponding protected MATHFORGE source lock exists.

## Agent cold start

1. Read the protected machine registry.
2. Resolve the assignment bound to the `dispatch_id` supplied in your launch message.
3. Verify that the assignment state is `LEASED`, the lease names the same `dispatch_id`, and the `agent_ref` matches your launch identity.
4. Read exactly the referenced work package. Treat that document as the complete GCL problem world.
5. Execute the bounded task.
6. Return exactly one result through the return surface and grammar named by the protected dispatch.
7. Stop.

Do not infer a lease from this page, a GitHub issue, a chat message, list order, or an unprotected branch.

## Claim boundary

The board allocates work. It does not identify unresolved hill mathematics, admit returned mathematics, certify claims, establish novelty, or authorize competition submission.
"""


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    campaign = load(CEX_CAMPAIGN)
    operation = load(OPERATION)
    prep = load(PREP)
    routing = load(ROUTING)

    if registry.get("record_type") != "GCL_CEX_ASSIGNMENT_REGISTRY":
        errors.append("assignment registry record_type mismatch")
    if registry.get("campaign") != "OPENMATH-2026":
        errors.append("assignment registry campaign mismatch")
    if registry.get("active_subcampaign") != "OPENMATH-2026-SOURCE-ACQ":
        errors.append("active subcampaign mismatch")
    if registry.get("operation") != "OM26-H2-H7-SOURCE-ACQ":
        errors.append("operation mismatch")

    if registry.get("lease_policy", {}).get("external_self_claim_allowed") is not False:
        errors.append("external self-claim must remain disabled")
    if registry.get("lease_policy", {}).get("start_rule") is None:
        errors.append("lease start rule missing")
    if registry.get("mathematics_release_policy", {}).get("current_math_jobs") != 0:
        errors.append("H2-H7 mathematical jobs must remain zero before source lock")

    assignments = registry.get("assignments", [])
    ids = [x.get("assignment_id") for x in assignments]
    if ids != EXPECTED_ASSIGNMENTS:
        errors.append(f"assignment set/order mismatch: {ids}")

    campaign_leases = {x["slot"]: x["lease_id"] for x in campaign.get("parallel_lanes", [])}
    operation_leases = {x["slot"]: x["lease_id"] for x in operation.get("parallel_lanes", [])}
    prep_by_slot = {x["slot"]: x for x in prep.get("lanes", [])}

    for item in assignments:
        slot = item.get("slot")
        aid = item.get("assignment_id")
        if slot not in EXPECTED_SLOTS:
            errors.append(f"{aid}: unexpected slot {slot}")
            continue
        if item.get("class") != "SOURCE_ACQUISITION":
            errors.append(f"{aid}: class must be SOURCE_ACQUISITION")
        if item.get("state") != "AVAILABLE_FOR_LEASE":
            errors.append(f"{aid}: initial state must be AVAILABLE_FOR_LEASE")
        if item.get("lease_id") != campaign_leases.get(slot) or item.get("lease_id") != operation_leases.get(slot):
            errors.append(f"{aid}: lease_id not aligned across CEX state")
        lease = item.get("lease", {})
        if lease.get("state") != "UNCLAIMED":
            errors.append(f"{aid}: initial lease must be UNCLAIMED")
        for key in ("dispatch_id", "agent_ref", "dispatch_issue_number", "protected_lease_commit"):
            if lease.get(key) is not None:
                errors.append(f"{aid}: {key} must be null while unclaimed")
        perms = item.get("permissions", {})
        if perms.get("hill_specific_mathematics") is not False:
            errors.append(f"{aid}: hill mathematics must be false")
        if perms.get("competition_submission") is not False:
            errors.append(f"{aid}: competition submission must be false")
        if perms.get("certification") is not False:
            errors.append(f"{aid}: certification must be false")
        if item.get("prerequisites", {}).get("source_lock") is not None:
            errors.append(f"{aid}: unresolved source lock must remain null")
        prep_lane = prep_by_slot.get(slot)
        if not prep_lane or prep_lane.get("solve_release") is not False:
            errors.append(f"{aid}: preparation lane is not fail-closed")

        wp = ROOT / str(item.get("work_package", ""))
        if not wp.is_file():
            errors.append(f"{aid}: work package missing")
        else:
            text = wp.read_text(encoding="utf-8")
            for required in (
                f"**Assignment ID:** `{aid}`",
                f"**Slot:** `{slot}`",
                "## Execution gate",
                "NO_ACTIVE_LEASE",
                "Do not self-claim this assignment.",
                "## Successor gate",
            ):
                if required not in text:
                    errors.append(f"{aid}: work package missing required marker {required}")

    board = (ROOT / BOARD).read_text(encoding="utf-8")
    if board != render_board(registry):
        errors.append("human job board is not the deterministic render of the machine registry")

    registered = [x for x in routing.get("workflows", []) if x.get("path") == WORKFLOW]
    if len(registered) != 1:
        errors.append("job-board workflow must be registered exactly once")
    else:
        entry = registered[0]
        if entry.get("observed_features") != ["OPAQUE_EXECUTION"]:
            errors.append("job-board workflow routing features mismatch")
        if entry.get("topology") != "PERSISTENT_CONTROLLER_REQUIRED":
            errors.append("job-board workflow topology mismatch")
        if entry.get("controller_id") != "GITHUB_ACTIONS":
            errors.append("job-board workflow controller mismatch")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: OPENMATH CEX job board, assignment registry, leases, and source-lock firewall are coherent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
