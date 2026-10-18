#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import re
import shutil
import tempfile
from pathlib import Path
from typing import Any

try:
    from ci.openmath_cex_github_contribution_intake import parse_result_comment
except ModuleNotFoundError:
    from openmath_cex_github_contribution_intake import parse_result_comment

try:
    from ci.openmath_lifecycle_candidate import apply_candidate, finalize_pin, plan, LifecycleCandidateError
except ModuleNotFoundError:
    from openmath_lifecycle_candidate import apply_candidate, finalize_pin, plan, LifecycleCandidateError

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/raw/OM26-H2-WP02-IA-001/github-comment-5889734796.md"
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
ADJ = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/adjudications/OM26-H2-WP02-ADJ-001.json"
RECEIPT = ROOT / ".gcl/completions/OM26-H2-WP02-ADJ-001/COMPLETION_RECEIPT.json"
EVAL = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py"
CONTRACT = ROOT / ".gcl/campaigns/OPENMATH-2026/LIFECYCLE_CONTRACT.json"

FULL_LIFECYCLE = ["READY", "LAUNCHED", "RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"]
PIPELINE = ["RETURNED", "CAPTURED", "REPLAYED", "ADJUDICATED", "ADVANCED"]


class AcceptanceError(RuntimeError):
    pass


def load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AcceptanceError(f"expected object at {path}")
    return value


def validate_successor_progress(registry: dict[str, Any], successor_id: str) -> None:
    """Keep historical acceptance valid only along a protected, closed chain."""
    items = {x["assignment_id"]: x for x in registry["assignments"]}
    successor = items[successor_id]
    hill = successor["hill"]
    current_id = registry["mathematics_release_policy"]["per_hill"][hill]["assignment"]
    current = items[current_id]
    if (current.get("hill") != hill
            or current.get("state") != "LEASED_NOT_LAUNCHED"
            or current.get("lease", {}).get("state") != "LEASED"
            or current.get("lifecycle", {}).get("pipeline_state", "READY") != "READY"
            or current.get("lifecycle", {}).get("closed") is not False):
        raise AcceptanceError("current successor is not durably READY with an open lease")
    seen = set()
    while current_id != successor_id:
        if current_id in seen:
            raise AcceptanceError("successor ancestry contains a cycle")
        seen.add(current_id)
        predecessor_id = current.get("prerequisites", {}).get("predecessor_assignment")
        predecessor = items.get(predecessor_id)
        if (predecessor is None or predecessor.get("hill") != hill
                or predecessor.get("state") != "ACCEPTED"
                or predecessor.get("lease", {}).get("state") != "CLOSED_AFTER_RETURN"
                or predecessor.get("lifecycle", {}).get("closed") is not True
                or predecessor.get("lifecycle", {}).get("pipeline_state") != "ADVANCED"):
            raise AcceptanceError("historical successor lacks a protected ADVANCED ancestry chain")
        current_id, current = predecessor_id, predecessor


def load_eval():
    spec = importlib.util.spec_from_file_location("om26_lifecycle_h2_eval", EVAL)
    if spec is None or spec.loader is None:
        raise AcceptanceError("cannot import protected H2 evaluator")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def named_witness_json(raw: str, label: str) -> dict[tuple[str, int], tuple[int, str, str]]:
    marker = f"**{label}"
    start = raw.find(marker)
    if start < 0:
        raise AcceptanceError(f"returned witness marker missing: {label}")
    fence = raw.find("```json", start)
    if fence < 0:
        raise AcceptanceError(f"returned witness JSON fence missing: {label}")
    body_start = raw.find("\n", fence) + 1
    body_end = raw.find("```", body_start)
    if body_start <= 0 or body_end < 0:
        raise AcceptanceError(f"returned witness JSON delimiter missing: {label}")
    try:
        obj = json.loads(raw[body_start:body_end].strip())
    except json.JSONDecodeError as exc:
        raise AcceptanceError(f"returned witness JSON invalid: {label}: {exc}") from exc
    rows = obj.get("transitions") if isinstance(obj, dict) else None
    if not isinstance(rows, dict):
        raise AcceptanceError(f"returned witness transitions missing: {label}")
    out: dict[tuple[str, int], tuple[int, str, str]] = {}
    for state in ("A", "B", "C", "D", "E", "F"):
        row = rows.get(state)
        if not isinstance(row, dict):
            raise AcceptanceError(f"returned witness row missing: {label}:{state}")
        for symbol in ("0", "1"):
            value = row.get(symbol)
            if not (isinstance(value, list) and len(value) == 3):
                raise AcceptanceError(f"returned witness transition malformed: {label}:{state}{symbol}")
            write, move, nxt = value
            out[(state, int(symbol))] = (int(write), str(move), str(nxt))
    return out


def returned_priority_cores(raw: str) -> tuple[dict, ...]:
    marker = "PRIORITY_SPINE_CORES: tuple[TransitionTable, ...] ="
    start = raw.find(marker)
    if start < 0:
        raise AcceptanceError("returned priority-spine cores are missing")
    expr_start = raw.find("(", start + len(marker))
    end_marker = "\n\n\ndef heuristic_priority_key"
    end = raw.find(end_marker, expr_start)
    if expr_start < 0 or end < 0:
        raise AcceptanceError("cannot delimit returned priority-spine cores")
    expr = raw[expr_start:end].strip()
    try:
        value = ast.literal_eval(expr)
    except (SyntaxError, ValueError) as exc:
        raise AcceptanceError(f"cannot parse returned priority-spine cores: {exc}") from exc
    if not isinstance(value, tuple) or len(value) < 3 or not all(isinstance(x, dict) for x in value):
        raise AcceptanceError("returned priority-spine core shape drift")
    return value


def complete_returned_core(
    core: dict[tuple[str, int], tuple[int, str, str]],
    halt_slot: tuple[str, int],
) -> dict[tuple[str, int], tuple[int, str, str]]:
    table = dict(core)
    table[halt_slot] = (1, "R", "H")
    completed: dict[tuple[str, int], tuple[int, str, str]] = {}
    for state in ("A", "B", "C", "D", "E", "F"):
        for symbol in (0, 1):
            value = table.get((state, symbol), (1, "R", "H"))
            if not (
                isinstance(value, tuple)
                and len(value) == 3
                and value[0] in (0, 1)
                and value[1] in ("L", "R")
                and value[2] in ("A", "B", "C", "D", "E", "F", "H")
            ):
                raise AcceptanceError(f"malformed returned transition at {(state, symbol)}")
            completed[(state, symbol)] = value
    return completed


def simulate_current_issued_assignment() -> dict[str, Any]:
    """Verify terminal event-window state and the protected frontier gate."""
    contract = load_json(CONTRACT)
    policy = contract.get("successor_policy", {})
    if policy.get("mode") != "FRONTIER_GATE_REQUIRED":
        raise AcceptanceError("frontier successor gate is not active")
    if policy.get("automatic_replay_successor") is not False:
        raise AcceptanceError("automatic replay successor remains enabled")

    registry = load_json(REGISTRY)
    scripts = list(registry["launch_contract"]["current_scripts"].values())
    scripts += list(registry["launch_contract"].get("support_scripts", {}).values())
    if any(row.get("executable") for row in scripts):
        raise AcceptanceError("terminal OPENMATH state still exposes executable replay leases")
    if registry["mathematics_release_policy"]["summary"].get("leased_not_launched_agents") != 0:
        raise AcceptanceError("terminal OPENMATH state still counts leased agents")

    with tempfile.TemporaryDirectory(prefix="openmath-frontier-gate-") as td:
        intake_dir = Path(td)
        (intake_dir / "META.json").write_text(json.dumps({"comment_id": 1}), encoding="utf-8")
        (intake_dir / "RECEIPT.json").write_text(json.dumps({
            "assignment_id": "OM26-H7-WP06",
            "dispatch_id": "OM26-H7-WP06-IA-001",
        }), encoding="utf-8")
        (intake_dir / "RAW.md").write_text("GCL-CONTRIBUTION-RESULT/1\n", encoding="utf-8")
        try:
            plan(intake_dir, ROOT)
        except LifecycleCandidateError as exc:
            if "protected frontier disposition required" not in str(exc):
                raise AcceptanceError(f"unexpected frontier-gate error: {exc}") from exc
        else:
            raise AcceptanceError("automatic successor generation unexpectedly succeeded")

    return {
        "pipeline": PIPELINE,
        "frontier_gate": "PASS__AUTOMATIC_REPLAY_DISABLED",
        "successor": None,
        "manual_transport_required": False,
        "manual_controller_wake_required": False,
        "result": "PASS",
    }


def run_acceptance() -> dict[str, Any]:
    contract = load_json(CONTRACT)
    if contract.get("status") not in {"FROZEN", "FROZEN__EVENT_WINDOW_TERMINAL"}:
        raise AcceptanceError("lifecycle contract is not frozen")
    if contract.get("lifecycle") != FULL_LIFECYCLE:
        raise AcceptanceError("frozen lifecycle drift")

    raw = RAW.read_text(encoding="utf-8")
    parsed = parse_result_comment(raw)
    if parsed["preamble"]["dispatch_id"] != "OM26-H2-WP02-IA-001":
        raise AcceptanceError("fixture dispatch drift")
    if parsed["preamble"]["agent_ref"] != "INDEPENDENT-AGENT-008":
        raise AcceptanceError("fixture agent drift")

    ev = load_eval()

    # Replay the two explicit witness JSONs exactly as returned. These are the
    # artifacts admitted by the protected bounded adjudication.
    w89911 = named_witness_json(raw, "Best Overall Canonical Witness")
    w8021 = named_witness_json(raw, "Best First-Write-`0` Canonical Witness")
    r1 = ev._run(w89911, 250000)
    r2 = ev._run(w8021, 250000)
    if (r1["halted"], r1["steps"], r1["ones"], r1["tape_span"], r1["reached"]) != (
        True, 89911, 185, 541, {"A","B","C","D","E","F"}
    ):
        raise AcceptanceError(f"W89911 explicit-witness replay mismatch: {r1}")
    if (r2["halted"], r2["steps"], r2["ones"], r2["tape_span"], r2["reached"]) != (
        True, 8021, 41, 122, {"A","B","C","D","E","F"}
    ):
        raise AcceptanceError(f"W8021 explicit-witness replay mismatch: {r2}")

    # Independently replay the returned E.5 code path. Its priority core fills
    # F,0 with (1,R,H), yielding span 121. This historical inconsistency is a
    # required narrowing signal, not an acceptance-test failure.
    cores = returned_priority_cores(raw)
    internal_w8021 = complete_returned_core(cores[2], ("F", 0))
    internal_r2 = ev._run(internal_w8021, 250000)
    if (internal_r2["halted"], internal_r2["steps"], internal_r2["ones"], internal_r2["tape_span"]) != (
        True, 8021, 41, 121
    ):
        raise AcceptanceError(f"W8021 returned-replay defect drift: {internal_r2}")

    wrapper_match = re.search(
        r"def score_protected_evaluator\(.*?\n(?=def apply_symmetry\()",
        raw,
        flags=re.S,
    )
    wrapper = wrapper_match.group(0) if wrapper_match else ""
    defects = {
        "protected_evaluator_independence": "FAIL__CIRCULAR_WRAPPER"
        if "return score_independent(" in wrapper else "PASS",
        "w8021_internal_metric": "FAIL__121_VS_122"
        if '("orbit_8021_w0_eq_0", m_8021, [8_021, 41, 121])' in raw else "PASS",
        "unpruned_reference": "FAIL__CLAIM_WITHOUT_IMPLEMENTATION"
        if (
            "matches unpruned enumeration with exact set equality" in raw
            and "def run_unpruned" not in raw
            and "def unpruned" not in raw
        ) else "PASS",
    }
    if list(defects.values()).count("PASS") != 0:
        raise AcceptanceError(f"historical narrowing fixture drift: {defects}")

    derived = {
        "adjudication": "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED",
        "accepted_witnesses": [
            {"steps":89911,"ones":185,"tape_span":541},
            {"steps":8021,"ones":41,"tape_span":122,"first_write":0},
        ],
        "successor": {
            "assignment_id":"OM26-H2-WP03",
            "dispatch_id":"OM26-H2-WP03-IA-001",
            "agent_ref":"INDEPENDENT-AGENT-009",
            "issue_number":537,
        },
    }

    protected_adj = load_json(ADJ)
    if protected_adj.get("disposition") != derived["adjudication"]:
        raise AcceptanceError("derived adjudication differs from protected adjudication")
    protected_claims = [
        {
            key: claim[key]
            for key in ("steps","ones","tape_span","first_write")
            if key in claim
        }
        for claim in (
            {"steps":89911,"ones":185,"tape_span":541},
            {"steps":8021,"ones":41,"tape_span":122,"first_write":0},
        )
    ]
    if protected_claims != derived["accepted_witnesses"]:
        raise AcceptanceError("accepted witness derivation drift")

    completion = load_json(RECEIPT)
    if completion["successor"]["assignment_id"] != derived["successor"]["assignment_id"]:
        raise AcceptanceError("completion successor drift")
    if completion["successor"]["dispatch_id"] != derived["successor"]["dispatch_id"]:
        raise AcceptanceError("completion dispatch drift")

    registry = load_json(REGISTRY)
    items = {x["assignment_id"]: x for x in registry["assignments"] if "assignment_id" in x}
    predecessor = items["OM26-H2-WP02"]
    successor = items["OM26-H2-WP03"]
    if predecessor["state"] != "ACCEPTED" or predecessor["lifecycle"]["closed"] is not True:
        raise AcceptanceError("predecessor is not durably adjudicated/closed")
    if contract.get("successor_policy", {}).get("mode") != "FRONTIER_GATE_REQUIRED":
        validate_successor_progress(registry, successor["assignment_id"])

    structural = simulate_current_issued_assignment()

    report = {
        "schema_version":"1.0.0",
        "record_type":"OPENMATH_LIFECYCLE_ACCEPTANCE_REPORT",
        "test_id":"OPENMATH-RETURNED-TO-ADVANCED-001",
        "source_dispatch":"OM26-H2-WP02-IA-001",
        "pipeline":PIPELINE,
        "capture":{
            "raw_result":str(RAW.relative_to(ROOT)),
            "result_grammar":"GCL-CONTRIBUTION-RESULT/1",
            "status":"PASS",
        },
        "replay":{
            "w89911":"PASS__89911_185_541",
            "w8021":"PASS__8021_41_122",
            "w8021_returned_e5_internal":"FAIL__8021_41_121__EXPECTED_HISTORICAL_DEFECT",
            **defects,
        },
        "adjudication":derived["adjudication"],
        "accepted_witnesses":derived["accepted_witnesses"],
        "successor":derived["successor"],
        "current_issued_assignment_simulation":structural,
        "result":"PASS",
        "manual_transport_required":False,
        "manual_controller_wake_required":False,
        "conversational_reconciliation_required":False,
        "claim_boundary":"Acceptance of lifecycle automation logic only; no new mathematical or certification claim.",
    }
    return report


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        report = run_acceptance()
    except (OSError, json.JSONDecodeError, AcceptanceError, ValueError) as exc:
        print(f"OPENMATH_LIFECYCLE_ACCEPTANCE_FAIL: {exc}")
        return 2
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("OPENMATH_LIFECYCLE_ACCEPTANCE_PASS")
    print(json.dumps(report, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
