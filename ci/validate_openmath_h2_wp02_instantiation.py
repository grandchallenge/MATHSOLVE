#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json"
BOOTSTRAP = ROOT / "handoffs/OPENMATH-2026/jobs/OM26-H2-WP02-IA-001.md"
SOURCE_WP = ROOT / "handoffs/OPENMATH-2026/jobs/OM26-H2-WP02.md"
DISPATCH = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/dispatches/OM26-H2-WP02-IA-001.json"
OPERATION = ROOT / ".gcl/operations/OM26-H2-WP02-IA-001/OPERATION.json"
BOARD = ROOT / "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"

EXPECTED_DISPOSITIONS = {
    "EXACT_SEARCH_DESIGN_VALIDATED",
    "EXACT_PRUNING_COUNTEREXAMPLE",
    "BOUNDED_CANDIDATE_FOUND",
    "EXACT_BLOCKER",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    lanes = load(LANES)
    dispatch = load(DISPATCH)
    operation = load(OPERATION)
    bootstrap = BOOTSTRAP.read_text(encoding="utf-8")
    source_wp = SOURCE_WP.read_text(encoding="utf-8")
    board = BOARD.read_text(encoding="utf-8")

    assignments = {x["assignment_id"]: x for x in registry["assignments"]}
    wp01 = assignments.get("OM26-H2-WP01")
    wp02 = assignments.get("OM26-H2-WP02")
    if not wp01 or wp01.get("state") != "ACCEPTED" or not wp01.get("lifecycle", {}).get("closed"):
        errors.append("WP01 predecessor is not preserved ACCEPTED/CLOSED")
    if not wp02:
        errors.append("WP02 assignment missing")
        return errors

    lease = wp02.get("lease", {})
    if wp02.get("state") != "ACCEPTED" or lease.get("state") != "CLOSED_AFTER_RETURN":
        errors.append("WP02 historical lease is not preserved as ACCEPTED/CLOSED_AFTER_RETURN")
    if lease.get("dispatch_id") != "OM26-H2-WP02-IA-001":
        errors.append("WP02 dispatch mismatch")
    if lease.get("agent_ref") != "INDEPENDENT-AGENT-008":
        errors.append("WP02 agent mismatch")
    if lease.get("dispatch_issue_number") != 526:
        errors.append("WP02 issue mismatch")
    if lease.get("return_url") != "https://github.com/grandchallenge/MATHSOLVE/issues/526":
        errors.append("WP02 return URL mismatch")
    if wp02.get("lifecycle", {}).get("launched") is not True or wp02.get("lifecycle", {}).get("returned") is not True:
        errors.append("WP02 historical execution/return state not preserved")
    if wp02.get("lifecycle", {}).get("adjudication") != "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED":
        errors.append("WP02 current adjudication mismatch")

    if dispatch.get("bootstrap_blob_sha1") != git_blob_sha1(BOOTSTRAP):
        errors.append("dispatch bootstrap blob mismatch")
    if dispatch.get("bootstrap_path") != "handoffs/OPENMATH-2026/jobs/OM26-H2-WP02-IA-001.md":
        errors.append("dispatch bootstrap path mismatch")
    if dispatch.get("github_issue_number") != 526:
        errors.append("dispatch issue number mismatch")
    if dispatch.get("operation_contract") != ".gcl/operations/OM26-H2-WP02-IA-001/OPERATION.json":
        errors.append("dispatch operation path mismatch")

    if operation.get("assignment_id") != "OM26-H2-WP02":
        errors.append("operation assignment mismatch")
    if operation.get("dispatch_id") != "OM26-H2-WP02-IA-001":
        errors.append("operation dispatch mismatch")
    if operation.get("agent_ref") != "INDEPENDENT-AGENT-008":
        errors.append("operation agent mismatch")
    if set(operation.get("acceptable_dispositions", [])) != EXPECTED_DISPOSITIONS:
        errors.append("operation dispositions mismatch")
    if operation.get("return", {}).get("issue_url") != "https://github.com/grandchallenge/MATHSOLVE/issues/526":
        errors.append("operation return issue mismatch")
    if operation.get("scope", {}).get("may_submit_competition_entry") is not False:
        errors.append("operation illegally authorizes competition submission")
    if operation.get("scope", {}).get("may_mutate_canonical_claims") is not False:
        errors.append("operation illegally authorizes canonical mutation")

    required_bootstrap_markers = [
        "## Completion check",
        "## Exact return contract",
        "## Failure return",
        "## Hard boundaries",
        "dispatch_id: OM26-H2-WP02-IA-001",
        "agent_ref: INDEPENDENT-AGENT-008",
        "assignment: OM26-H2-WP02",
        "disposition: <EXACT_SEARCH_DESIGN_VALIDATED|EXACT_PRUNING_COUNTEREXAMPLE|BOUNDED_CANDIDATE_FOUND|EXACT_BLOCKER>",
        "## Strongest exact statement",
        "## Derivation",
        "## Assumptions beyond bootstrap",
        "## Verification / falsification hooks",
        "## Claim boundary",
        "## Next residual",
        "What counts as exact replayable evidence",
        "first-write-`0`",
    ]
    for marker in required_bootstrap_markers:
        if marker not in bootstrap:
            errors.append(f"bootstrap missing marker: {marker}")

    if "A,0 -> [1,\"R\",\"B\"]" not in bootstrap or "is without loss of generality" not in bootstrap:
        errors.append("bootstrap does not carry predecessor normalization rejection")
    if "Heuristics may reorder exploration but must never remove a branch." not in bootstrap:
        errors.append("bootstrap lacks exact/heuristic separation")
    if "No search heuristic may be represented as an exact exclusion rule." not in source_wp:
        errors.append("source WP lacks exact pruning boundary")

    h2 = next(x for x in lanes["hills"] if x["hill_slot"] == "OM26-H2")
    active_id = h2.get("active_lease", {}).get("assignment_id")
    expected_predecessor = "OM26-H2-WP03" if active_id == "OM26-H2-WP04" else "OM26-H2-WP02"
    if active_id == "OM26-H2-WP04":
        wp03 = assignments.get("OM26-H2-WP03", {})
        if wp03.get("state") != "ACCEPTED" or not wp03.get("lifecycle", {}).get("closed"):
            errors.append("WP04 succession requires preserved ACCEPTED/CLOSED WP03")
    if active_id not in {"OM26-H2-WP03", "OM26-H2-WP04"}:
        errors.append("H2 lane does not point to an admitted WP03/WP04 successor")
    if h2.get("active_lease", {}).get("lifecycle_state") != "LEASED_NOT_LAUNCHED":
        errors.append("H2 active successor lease lifecycle mismatch")
    if h2.get("predecessor_lease", {}).get("assignment_id") != expected_predecessor:
        errors.append("H2 immediate predecessor lease missing")
    if h2.get("predecessor_lease", {}).get("lifecycle_state") != "ACCEPTED":
        errors.append("H2 immediate predecessor lease not accepted")
    if h2.get("competition_state", {}).get("official_submission") != "NOT_SUBMITTED":
        errors.append("H2 competition boundary changed")

    for i in range(3, 8):
        hill = next(x for x in lanes["hills"] if x["hill_slot"] == f"OM26-H{i}")
        if hill.get("active_lease", {}).get("lifecycle_state") != "LEASED_NOT_LAUNCHED":
            errors.append(f"OM26-H{i} lifecycle drift")

    if "| `OM26-H2-WP02` | `OM26-H2` | `ACCEPTED` |" not in board:
        errors.append("job board missing WP02 accepted history")
    if f"| `{active_id}` | `OM26-H2` | `LEASED_NOT_LAUNCHED` |" not in board:
        errors.append("job board missing current active lease")

    policy = registry["mathematics_release_policy"]
    if policy["per_hill"]["OM26-H2"]["assignment"] != active_id:
        errors.append("per-hill policy does not select current successor")
    if policy["per_hill"]["OM26-H2"]["predecessor"]["assignment"] != expected_predecessor:
        errors.append("per-hill policy loses immediate predecessor")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print("FAIL:", error)
        return 1
    print("PASS: historical OM26-H2-WP02 instantiation remains intact after adjudication and admitted succession")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
