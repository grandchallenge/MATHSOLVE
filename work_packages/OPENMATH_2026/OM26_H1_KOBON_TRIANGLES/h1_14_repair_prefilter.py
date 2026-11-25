#!/usr/bin/env python3
"""Fast bounded repair-cell prefilter for OM26-H1 H1-14.

For one selected two-blocker target, keep the two required determinant flips and
allow each moving blocker independently zero or one additional determinant-sign
flip.  Score every abstract orientation cell without asserting realizability.
"""
from __future__ import annotations

import argparse
import json
from functools import lru_cache
from itertools import combinations
from pathlib import Path

import wolfram_94_semialgebraic as bridge

ROOT = Path(__file__).resolve().parent
DEFAULT_SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"


def make_fast_scorer(lines):
    pair_signs = bridge._pair_signs(lines)
    base_triples = bridge._triple_signs(lines)
    triples = list(combinations(range(len(lines)), 3))

    def face_status(t, table):
        i, j, k = t
        wij = bridge._d2_sign(pair_signs, i, j)
        wjk = bridge._d2_sign(pair_signs, j, k)
        wki = bridge._d2_sign(pair_signs, k, i)
        if 0 in (wij, wjk, wki) or bridge._d3_sign(table, i, j, k) == 0:
            return False
        for m in range(len(lines)):
            if m in t:
                continue
            vals = (
                bridge._d3_sign(table, m, i, j) * wij,
                bridge._d3_sign(table, m, j, k) * wjk,
                bridge._d3_sign(table, m, k, i) * wki,
            )
            if 1 in vals and -1 in vals:
                return False
        return True

    base_status = {t: face_status(t, base_triples) for t in triples}
    base_score = sum(base_status.values())

    @lru_cache(None)
    def affected(key):
        key = tuple(key)
        s = set(key)
        out = set()
        for a, b in combinations(key, 2):
            for x in range(len(lines)):
                if x in s:
                    continue
                out.add(tuple(sorted((a, b, x))))
        return frozenset(out)

    def score(flips):
        keys = {tuple(sorted(x)) for x in flips}
        table = dict(base_triples)
        touched = set()
        for key in keys:
            table[key] *= -1
            touched.update(affected(key))
        score = base_score
        for t in touched:
            score += int(face_status(t, table)) - int(base_status[t])
        return score

    return score


def keys_for_mover(lines, mover, other_mover):
    signs = bridge._triple_signs(lines)
    fixed = [x for x in range(len(lines)) if x not in (mover, other_mover)]
    out = []
    for a, b in combinations(fixed, 2):
        key = tuple(sorted((mover, a, b)))
        if signs[key] != 0:
            out.append(key)
    return out


def run(lines, target=(0, 4, 14), movers=(6, 11)):
    atlas = bridge.build_atlas(lines)
    record = next(x for x in atlas["two_blocker_cases"] if tuple(x["target_triple"]) == tuple(target))
    required = [tuple(x["required_flip_key"]) for x in record["blockers"]]
    by_mover = {x["moving_line"]: tuple(x["required_flip_key"]) for x in record["blockers"]}
    if set(by_mover) != set(movers):
        raise SystemExit(f"mover mismatch: {by_mover} versus {movers}")

    score = make_fast_scorer(lines)
    m1, m2 = movers
    r1, r2 = by_mover[m1], by_mover[m2]
    k1 = [None] + [x for x in keys_for_mover(lines, m1, m2) if x != r1]
    k2 = [None] + [x for x in keys_for_mover(lines, m2, m1) if x != r2]

    best = -1
    best_cells = []
    histogram = {}
    evaluated = 0
    for e1 in k1:
        for e2 in k2:
            flips = [r1, r2]
            if e1 is not None:
                flips.append(e1)
            if e2 is not None:
                flips.append(e2)
            current = score(flips)
            histogram[str(current)] = histogram.get(str(current), 0) + 1
            evaluated += 1
            if current > best:
                best = current
                best_cells = [{"extra_1": e1, "extra_2": e2}]
            elif current == best:
                best_cells.append({"extra_1": e1, "extra_2": e2})

    return {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-14-REPAIR-PREFILTER",
        "target": list(target),
        "moving_lines": list(movers),
        "required_flips": [list(x) for x in required],
        "candidate_count_mover_1": len(k1),
        "candidate_count_mover_2": len(k2),
        "abstract_cells_evaluated": evaluated,
        "best_abstract_score": best,
        "best_cells": [
            {
                "extra_1": list(x["extra_1"]) if x["extra_1"] is not None else None,
                "extra_2": list(x["extra_2"]) if x["extra_2"] is not None else None,
            }
            for x in best_cells
        ],
        "score_histogram": dict(sorted(histogram.items(), key=lambda kv: int(kv[0]))),
        "claim_boundary": "Abstract orientation-cell prefilter only; no realizability or upper-bound claim.",
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    lines = bridge.wall.load_solution(args.seed)
    result = run(lines)
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
