#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/raw/OM26-H2-WP02-IA-001/github-comment-5889734796.md"
ADJ = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP02/adjudications/OM26-H2-WP02-ADJ-001.json"
STATUS = ROOT / "work_packages/OPENMATH_2026/OM26_H2_BUSY_BEAVER_6/WP02_STATUS.json"
BOOT = ROOT / "handoffs/OPENMATH-2026/jobs/OM26-H2-WP03-IA-001.md"
LAUNCH = ROOT / "handoffs/OPENMATH-2026/launch/OM26-H2-WP03.md"
DISPATCH = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP03/dispatches/OM26-H2-WP03-IA-001.json"
OP = ROOT / ".gcl/operations/OM26-H2-WP03-IA-001/OPERATION.json"
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json"
BOARD = ROOT / "handoffs/OPENMATH-2026/CEX_JOB_BOARD.md"
EVAL = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py"

W89911 = {
    ("A",0):(1,"R","B"), ("A",1):(1,"L","E"),
    ("B",0):(1,"R","C"), ("B",1):(1,"R","B"),
    ("C",0):(1,"R","D"), ("C",1):(1,"L","H"),
    ("D",0):(1,"L","A"), ("D",1):(1,"L","D"),
    ("E",0):(0,"R","F"), ("E",1):(0,"L","F"),
    ("F",0):(1,"L","C"), ("F",1):(0,"L","A"),
}
W8021 = {
    ("A",0):(0,"R","B"), ("A",1):(1,"L","D"),
    ("B",0):(1,"R","C"), ("B",1):(1,"L","D"),
    ("C",0):(1,"R","D"), ("C",1):(1,"R","C"),
    ("D",0):(1,"R","E"), ("D",1):(0,"L","F"),
    ("E",0):(0,"L","A"), ("E",1):(1,"L","E"),
    ("F",0):(1,"L","H"), ("F",1):(0,"L","B"),
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_eval():
    spec = importlib.util.spec_from_file_location("om26_h2_eval", EVAL)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot import protected evaluator")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    raw = RAW.read_text(encoding="utf-8")
    adj = load_json(ADJ)
    status = load_json(STATUS)
    dispatch = load_json(DISPATCH)
    op = load_json(OP)
    registry = load_json(REGISTRY)
    lanes = load_json(LANES)
    board = BOARD.read_text(encoding="utf-8")
    boot = BOOT.read_text(encoding="utf-8")
    launch = LAUNCH.read_text(encoding="utf-8")
    ev = load_eval()

    r1 = ev._run(W89911, 250000)
    assert r1 == {
        "halted": True, "steps": 89911, "ones": 185, "tape_span": 541,
        "reached": {"A","B","C","D","E","F"},
    }
    r2 = ev._run(W8021, 250000)
    assert r2 == {
        "halted": True, "steps": 8021, "ones": 41, "tape_span": 122,
        "reached": {"A","B","C","D","E","F"},
    }

    # Returned replay defects must remain directly inspectable.
    assert 'def score_protected_evaluator(' in raw
    protected_fn = raw.split('def score_protected_evaluator(', 1)[1].split('\ndef apply_symmetry(', 1)[0]
    assert 'return score_independent(' in protected_fn
    assert '("orbit_8021_w0_eq_0", m_8021, [8_021, 41, 121])' in raw
    assert '(steps=8021, ones=41, tape_span=122)' in raw
    assert 'matches unpruned enumeration with exact set equality' in raw
    assert 'def run_unpruned' not in raw and 'def unpruned' not in raw

    assert adj["disposition"] == "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED"
    assert {x["claim_id"] for x in adj["accepted_claims"]} == {
        "OM26-H2-W89911-001", "OM26-H2-W8021-001"
    }
    assert adj["adjudicator_checks"]["protected_evaluator_independence"].startswith("FAIL")
    assert adj["adjudicator_checks"]["unpruned_small_horizon_reference"].startswith("FAIL")
    assert adj["lifecycle_effect"]["certification"] == "NONE"
    assert adj["lifecycle_effect"]["competition"] == "NONE"

    assert status["state"] == "WITNESSES_ACCEPTED__EXACT_SEARCH_REPLAY_NOT_VALIDATED"
    assert status["next_work_package"]["id"] == "OM26-H2-WP03"

    assert dispatch["dispatch_id"] == "OM26-H2-WP03-IA-001"
    assert dispatch["agent_ref"] == "INDEPENDENT-AGENT-009"
    assert dispatch["github_issue_number"] == 537
    assert dispatch["bootstrap_path"] == "handoffs/OPENMATH-2026/jobs/OM26-H2-WP03-IA-001.md"
    assert op["acceptable_dispositions"] == [
        "EXACT_SEARCH_REPLAY_VALIDATED",
        "WITNESSES_CONFIRMED_SEARCH_NOT_VALIDATED",
        "EXACT_PRUNING_COUNTEREXAMPLE",
        "EXACT_BLOCKER",
    ]
    for marker in (
        "GCL-CONTRIBUTION-DISPATCH/1",
        "OM26-H2-WP03-IA-001",
        "W89911",
        "W8021",
        "distinct unpruned reference enumerator",
        "translated-cycle pruning",
    ):
        assert marker in boot
    for marker in (
        "GCL-ZERO-CONTEXT-LAUNCH/2",
        "OM26-H2-WP03",
        "INDEPENDENT-AGENT-009",
        "GCL-RETURN-RELAY/1",
    ):
        assert marker in launch

    assignments = {x["assignment_id"]: x for x in registry["assignments"]}
    wp02 = assignments["OM26-H2-WP02"]
    wp03 = assignments["OM26-H2-WP03"]
    assert wp02["state"] == "ACCEPTED"
    assert wp02["lease"]["state"] == "CLOSED_AFTER_RETURN"
    assert wp02["lease"]["execution_authorized"] is False
    assert wp02["lifecycle"]["adjudication"] == "ACCEPTED_WITNESSES_WITH_EXACT_SEARCH_REPLAY_REJECTED"
    assert wp03["state"] == "LEASED_NOT_LAUNCHED"
    assert wp03["lease"]["protected_lease_merge"] == "208fa322f52d06eb7f9b6affff0f359217a5118e"
    assert wp03["lease"]["readback_verified"] is True
    assert wp03["lease"]["execution_authorized"] is True
    assert wp03["lifecycle"]["launched"] is False
    lane = next(x for x in lanes["hills"] if x["hill_slot"] == "OM26-H2")
    assert lane["active_lease"]["assignment_id"] == "OM26-H2-WP03"
    assert lane["active_lease"]["lifecycle_state"] == "LEASED_NOT_LAUNCHED"
    assert lane["predecessor_lease"]["assignment_id"] == "OM26-H2-WP02"
    assert lane["predecessor_lease"]["lifecycle_state"] == "ACCEPTED"
    assert "| `OM26-H2-WP03` | `OM26-H2` | `LEASED_NOT_LAUNCHED` |" in board

    print("PASS: H2 WP02 narrowed adjudication replays both witnesses and generates bounded WP03 replay closure")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
