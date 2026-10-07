#!/usr/bin/env python3
"""Validate the durable H1-15 compound order-type search receipt."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES"
SOURCE = H1 / "H1_15_COMPOUND_ORDER_TYPE_SOURCE.json"
RECEIPT = H1 / "H1_15_COMPOUND_ORDER_TYPE_RECEIPT.json"
SCRIPT = H1 / "search_94_compound_order_type.py"
SEED = H1 / "candidates/RH_BADER_PROJECTIVE_NOPARALLEL_093/solution.json"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate():
    source = json.loads(SOURCE.read_text())
    receipt = json.loads(RECEIPT.read_text())
    seed = json.loads(SEED.read_text())

    assert source["tracker"] == 955
    assert source["external_proposal_generator"]["commit"] == "22d1165f6c455fe45e461baef4410f6d5c78a014"
    assert source["proposal_seed"]["expected_score"] == 93
    assert source["search"] == {
        "script": "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/search_94_compound_order_type.py",
        "family": "compound anchor-line projective macros",
        "width": 256,
        "depth": 10,
        "bridge_budget": 1,
        "seed": 2026100701,
        "projective_weight": 0.08,
        "noise": 0.35,
        "no_score_drop_cutoff": True,
        "intended_effect": "Cross score valleys pruned by H1-13 drop=4 while retaining a structured macro around one anchor line plus at most one off-anchor bridge mutation.",
    }

    external_seed = {
        "lines_frac": [[str(a), str(b), str(-c)] for a, b, c in seed["lines"]]
    }
    external_bytes = (json.dumps(external_seed) + "\n").encode()
    assert receipt["source"] == "research/finite-table/gcl-om26-h1-093.json"
    assert receipt["source_sha256"] == sha256_bytes(external_bytes)
    assert receipt["search_script_sha256"] == sha256_bytes(SCRIPT.read_bytes())
    assert receipt["external_commit_required"] == source["external_proposal_generator"]["commit"]

    assert receipt["n"] == 18
    assert receipt["initial_score"] == 93
    assert receipt["realized_best"] == 93
    assert receipt["combinatorial_best"] == 93
    assert receipt["initial_projective_score"] == 102
    assert receipt["projective_best"] == 102
    assert receipt["nodes"] == 38718
    assert receipt["edges"] == 631968
    assert receipt["endpoints_ge_94"] == 0
    assert receipt["realization_attempts"] == 0
    assert receipt["realized_candidates"] == []
    assert receipt["best_endpoint"] is None
    assert receipt["anchors_completed"] == 18
    assert receipt["completed_all_anchors"] is True
    assert receipt["found_94_or_better"] is False
    assert receipt["width"] == 256
    assert receipt["depth"] == 10
    assert receipt["bridge_budget"] == 1
    assert receipt["seed"] == 2026100701
    assert receipt["projective_weight"] == 0.08
    assert receipt["noise"] == 0.35

    anchors = receipt["anchor_summaries"]
    assert [x["anchor"] for x in anchors] == list(range(18))
    assert sum(x["nodes"] for x in anchors) == receipt["nodes"]
    assert sum(x["edges"] for x in anchors) == receipt["edges"]
    assert max(x["best_score"] for x in anchors) == 93

    return {
        "record_id": receipt["record_id"],
        "anchors_completed": receipt["anchors_completed"],
        "nodes": receipt["nodes"],
        "edges": receipt["edges"],
        "combinatorial_best": receipt["combinatorial_best"],
        "found_94_or_better": receipt["found_94_or_better"],
        "claim_boundary": receipt["claim_boundary"],
    }


if __name__ == "__main__":
    print(json.dumps(validate(), indent=2, sort_keys=True))
