#!/usr/bin/env python3
"""Validate durable OM26-H1 H1-14 Wolfram bridge artifacts."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
H1 = ROOT / "work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES"
sys.path.insert(0, str(H1))

import h1_14_repair_prefilter as prefilter
import wolfram_94_semialgebraic as bridge

SEED = H1 / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"
ATLAS = H1 / "H1_14_NEAR_MISS_ATLAS.json"
RECEIPT = H1 / "H1_14_WOLFRAM_TRANCHE1_RECEIPT.json"


def git_blob_sha1(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def main():
    lines = [tuple(x) for x in json.loads(SEED.read_text())["lines"]]
    if bridge.wall.exact_score(lines) != 93:
        raise SystemExit("H1-14 seed score drift")
    if git_blob_sha1(SEED) != "bb244e4b0422922ae9f85cc4facb2109c33162b3":
        raise SystemExit("H1-14 seed blob drift")

    committed = json.loads(ATLAS.read_text())
    recomputed = bridge.build_atlas(lines)

    expected = {
        "seed_score": 93,
        "proper_triangle_count": 93,
        "improper_triple_count": 48,
        "one_blocker_count": 0,
        "two_blocker_count": 60,
    }
    for key, value in expected.items():
        if recomputed[key] != value or committed[key] != value:
            raise SystemExit(f"atlas mismatch {key}: {recomputed[key]} / {committed[key]} != {value}")

    if recomputed["proper_nonface_blocker_distribution"] != committed["proper_nonface_blocker_distribution"]:
        raise SystemExit("blocker distribution drift")
    if len(committed["two_blocker_cases"]) != 60:
        raise SystemExit("two-blocker atlas length drift")
    if any(x["minimal_two_flip_abstract_score"] != 89 for x in committed["two_blocker_cases"]):
        raise SystemExit("minimal dual-exit score drift")
    if any(
        b["single_flip_abstract_score"] != 90
        for x in committed["two_blocker_cases"]
        for b in x["blockers"]
    ):
        raise SystemExit("minimal single-exit score drift")

    receipt = json.loads(RECEIPT.read_text())
    ranked = receipt["wolfram"]["ranked_single_blocker_cases"]
    if len(ranked) != 20:
        raise SystemExit("Wolfram ranked-case count drift")
    feasible = sum(1 for x in ranked if x["feasible"])
    if feasible != 6:
        raise SystemExit(f"Wolfram feasible-cell count drift: {feasible}")
    target_pairs = {}
    for x in ranked:
        target_pairs.setdefault(tuple(x["target"]), []).append(bool(x["feasible"]))
    both = sorted(target for target, states in target_pairs.items() if states == [True, True])
    if both != [(0, 4, 14)]:
        raise SystemExit(f"unexpected independently feasible dual target(s): {both}")

    witness = [list(x) for x in lines]
    witness[6] = receipt["coupled_cell"]["materialized_integer_lines"]["line_6"]
    witness[11] = receipt["coupled_cell"]["materialized_integer_lines"]["line_11"]
    score = bridge.wall.exact_score(witness)
    if score != 89 or receipt["coupled_cell"]["exact_score"] != 89:
        raise SystemExit(f"coupled witness score drift: {score}")

    repair = prefilter.run(lines)
    if repair["abstract_cells_evaluated"] != 14400:
        raise SystemExit(f"repair cell count drift: {repair['abstract_cells_evaluated']}")
    if repair["best_abstract_score"] != 89:
        raise SystemExit(f"repair best score drift: {repair['best_abstract_score']}")
    if repair["best_cells"] != [{"extra_1": None, "extra_2": None}]:
        raise SystemExit(f"repair best-cell identity drift: {repair['best_cells']}")

    print("H1_14_WOLFRAM_BRIDGE=PASS")
    print("seed_score=93")
    print("two_blocker_cases=60")
    print("single_resolve_feasible=6")
    print("single_resolve_infeasible=14")
    print("coupled_exact_score=89")
    print("repair_cells=14400")
    print("repair_best=89")


if __name__ == "__main__":
    main()
