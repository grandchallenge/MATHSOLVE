#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADJ = ROOT / "contributions/OPENMATH-2026/OM26-H2/WP01/adjudications/OM26-H2-WP01-ADJ-001.json"
STATUS = ROOT / "work_packages/OPENMATH_2026/OM26_H2_BUSY_BEAVER_6/WP01_STATUS.json"
REGISTRY = ROOT / ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = ROOT / "work_packages/OPENMATH_2026/HILL_LANES.json"
EVAL = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/eval.py"
PRIVATE_LOCK = ROOT / "work_packages/OPENMATH_2026/AUTHORITATIVE_SOURCE_POOL/busy-beaver-6-certificates/PUBLIC_SOURCE/private.lock"


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def load_eval_module():
    spec = importlib.util.spec_from_file_location("om26_h2_eval", EVAL)
    if spec is None or spec.loader is None:
        raise AssertionError("cannot import protected evaluator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def baseline_machine():
    rows = {
        "A": {0: (1, "R", "B"), 1: (1, "R", "H")},
        "B": {0: (1, "R", "C"), 1: (1, "R", "H")},
        "C": {0: (1, "R", "D"), 1: (1, "R", "H")},
        "D": {0: (1, "R", "E"), 1: (1, "R", "H")},
        "E": {0: (1, "R", "F"), 1: (1, "R", "H")},
        "F": {0: (1, "R", "H"), 1: (1, "R", "H")},
    }
    return {(q, s): rows[q][s] for q in rows for s in (0, 1)}


def first_write_zero_counterexample():
    rows = {
        "A": {0: (0, "R", "B"), 1: (1, "R", "H")},
        "B": {0: (1, "R", "C"), 1: (1, "R", "H")},
        "C": {0: (1, "R", "D"), 1: (1, "R", "H")},
        "D": {0: (1, "R", "E"), 1: (1, "R", "H")},
        "E": {0: (1, "R", "F"), 1: (1, "R", "H")},
        "F": {0: (1, "R", "H"), 1: (1, "R", "H")},
    }
    return {(q, s): rows[q][s] for q in rows for s in (0, 1)}


def validate():
    evaluator = load_eval_module()

    base = evaluator._run(baseline_machine(), 10)
    assert base == {
        "halted": True,
        "steps": 6,
        "ones": 6,
        "tape_span": 7,
        "reached": {"A", "B", "C", "D", "E", "F"},
    }

    counter = evaluator._run(first_write_zero_counterexample(), 10)
    assert counter["halted"] is True
    assert counter["steps"] == 6
    assert counter["reached"] == {"A", "B", "C", "D", "E", "F"}
    assert first_write_zero_counterexample()[("A", 0)][0] == 0

    lock = load(PRIVATE_LOCK)
    entries = {x["path"]: x for x in lock["entries"]}
    assert entries["private/validation.json"]["size"] == 22
    assert entries["private/validation.json"]["sha256"] == "0b875b68f6a678186abba15a8b26edc5738ef62fb50b6b8cccfe7bb06beabe56"
    assert entries["private/test.json"]["size"] == 23
    assert entries["private/test.json"]["sha256"] == "1ce68cbe0e8e3c2a2f0003dc57792c5e9a621284eb08fe100e1d069d88dad811"

    adj = load(ADJ)
    assert adj["disposition"] == "ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING"
    assert adj["adjudicator_checks"]["evaluator_semantics_replay"] == "PASS"
    assert adj["adjudicator_checks"]["exact_search_normalization"].startswith("FAIL")
    assert adj["lifecycle_effect"]["certification"] == "NONE"
    assert adj["lifecycle_effect"]["competition"] == "NONE"

    status = load(STATUS)
    assert status["state"] == "SCORER_CONCORDANCE_ACCEPTED__EXACT_SEARCH_DESIGN_REQUIRED"
    assert status["narrowed"]["tn_normalization"] == "FIRST_WRITE_1_NOT_WLOG"

    registry = load(REGISTRY)
    assignment = next(x for x in registry["assignments"] if x["assignment_id"] == "OM26-H2-WP01")
    assert assignment["state"] == "ACCEPTED"
    assert assignment["lease"]["execution_authorized"] is False
    assert assignment["lifecycle"]["closed"] is True
    assert assignment["lifecycle"]["adjudication"] == "ACCEPTED_SCORER_CONCORDANCE_WITH_SEARCH_NARROWING"

    lanes = load(LANES)
    h2 = next(x for x in lanes["hills"] if x["hill_slot"] == "OM26-H2")
    assert h2["active_lease"]["assignment_id"] == "OM26-H2-WP02"
    assert h2["active_lease"]["lifecycle_state"] == "LEASED_NOT_LAUNCHED"
    assert h2["predecessor_lease"]["assignment_id"] == "OM26-H2-WP01"
    assert h2["predecessor_lease"]["lifecycle_state"] == "ACCEPTED"
    assert h2["competition_state"]["official_submission"] == "NOT_SUBMITTED"
    assert "FIRST_WRITE_1_NOT_WLOG" in h2["obligations"]["representation_or_reduction"]

    for i in range(3, 8):
        hill = next(x for x in lanes["hills"] if x["hill_slot"] == f"OM26-H{i}")
        assert hill["active_lease"]["lifecycle_state"] == "LEASED_NOT_LAUNCHED"

    print("PASS: H2 WP01 scorer concordance accepted; exact search claims narrowed")


if __name__ == "__main__":
    validate()
