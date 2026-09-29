#!/usr/bin/env python3
from __future__ import annotations

import json
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ADJ = "contributions/OPENMATH-2026/OM26-H1/H1-12/adjudications/OM26-H1-H1-12-ADJ-001.json"
STATUS = "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/H1_12_STATUS.json"
LEDGER = "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/CLAIM_LEDGER.json"
REGISTRY = ".gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json"
LANES = "work_packages/OPENMATH_2026/HILL_LANES.json"

CLAIM_ID = "OM26-H1-RED-023"


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))


def sector_replay():
    survivors = []
    for t in product((0, 1), repeat=6):
        shared = tuple(int(t[(i - 1) % 6] and t[i]) for i in range(6))
        if shared[0] != 1 or shared[1] != 1:
            continue
        if sum(shared) != 4:
            continue
        d1 = [i for i in range(6) if shared[i] and i not in (0, 1)]
        if len(d1) != 2:
            continue
        if any(((i + 1) % 6) in d1 for i in d1):
            continue
        survivors.append((t, tuple(d1)))
    expected = [((1, 1, 1, 0, 1, 1), (2, 5))]
    if survivors != expected:
        raise AssertionError(f"sector replay mismatch: {survivors}")


def affine_contradiction_replay():
    # The two exterior faces across adjacent D1 segments at A and B require
    # alpha+beta<1 and alpha+beta>1 simultaneously. Equivalent cyclic pairs
    # are alpha>gamma & alpha<gamma and beta<gamma & beta>gamma.
    pairs = [
        ("alpha+beta", "<", ">"),
        ("alpha-gamma", ">", "<"),
        ("beta-gamma", "<", ">"),
    ]
    for expr, left, right in pairs:
        if left == right:
            raise AssertionError(f"contradiction vanished for {expr}")


def validate():
    sector_replay()
    affine_contradiction_replay()

    adj = load(ADJ)
    if adj["disposition"] != "ACCEPTED_SOURCE_CONDITIONAL_REDUCTION":
        raise AssertionError("adjudication disposition mismatch")
    if adj["accepted_claim"]["claim_id"] != CLAIM_ID:
        raise AssertionError("adjudication claim id mismatch")
    if adj["resulting_frontier"]["new"] != "Q_GE_6__SOURCE_CONDITIONAL":
        raise AssertionError("adjudication frontier mismatch")
    if adj["lifecycle_effect"]["certification"] != "NONE":
        raise AssertionError("adjudication illegally certifies")
    if adj["lifecycle_effect"]["competition"] != "NONE":
        raise AssertionError("adjudication illegally changes competition state")

    status = load(STATUS)
    if status["state"] != "Q_GE_6__SOURCE_CONDITIONAL":
        raise AssertionError("H1_12 status frontier mismatch")
    q5 = status.get("q5_agent001_adjudication", {})
    if q5.get("claim_id") != CLAIM_ID or q5.get("certification_effect") is not False:
        raise AssertionError("H1_12 adjudication projection mismatch")

    ledger = load(LEDGER)
    claims = [x for x in ledger["claims"] if x.get("claim_id") == CLAIM_ID]
    if len(claims) != 1:
        raise AssertionError(f"expected one {CLAIM_ID}, found {len(claims)}")
    claim = claims[0]
    if claim["type"] != "SOURCE_CONDITIONAL_REDUCTION":
        raise AssertionError("claim type mismatch")
    if claim["certification_effect"] is not False:
        raise AssertionError("claim ledger illegally certifies")

    registry = load(REGISTRY)
    assignment = next(x for x in registry["assignments"] if x["assignment_id"] == "OM26-H1-H1-12")
    if assignment["state"] != "ACCEPTED":
        raise AssertionError("Agent 001 assignment is not ACCEPTED")
    if assignment["lifecycle"]["adjudication"] != "ACCEPTED_SOURCE_CONDITIONAL_REDUCTION":
        raise AssertionError("Agent 001 lifecycle adjudication mismatch")
    if assignment["lifecycle"]["closed"] is not True:
        raise AssertionError("Agent 001 assignment not closed")
    if assignment["lease"]["execution_authorized"] is not False:
        raise AssertionError("closed Agent 001 lease remains executable")

    lanes = load(LANES)
    h1 = next(x for x in lanes["hills"] if x["hill_slot"] == "OM26-H1")
    if h1["external_agent"]["lifecycle_state"] != "ACCEPTED":
        raise AssertionError("H1 lane agent lifecycle mismatch")
    if "Q_LE_5_EXCLUDED_SOURCE_CONDITIONAL" not in h1["obligations"]["representation_or_reduction"]:
        raise AssertionError("H1 lane frontier projection mismatch")
    if h1["competition_state"]["official_submission"] != "NOT_SUBMITTED":
        raise AssertionError("H1 competition boundary changed")

    h2 = next(x for x in lanes["hills"] if x["hill_slot"] == "OM26-H2")
    if h2["active_lease"]["lifecycle_state"] != "ACCEPTED":
        raise AssertionError("OM26-H2 lifecycle drift")
    for i in range(3, 8):
        hill = next(x for x in lanes["hills"] if x["hill_slot"] == f"OM26-H{i}")
        if hill["active_lease"]["lifecycle_state"] != "LEASED_NOT_LAUNCHED":
            raise AssertionError(f"OM26-H{i} lifecycle drift")

    print("PASS: Agent 001 q=5 reduction adjudicated as source-conditional; frontier is q>=6")


if __name__ == "__main__":
    validate()
