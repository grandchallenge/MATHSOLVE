#!/usr/bin/env python3
"""Exact canonical closest-dual-cell search for H1-14.

For each two-blocker near-miss, choose one exact rational representative of
each blocker's closest target-unblocked event cell and rescore the individual
and paired representatives with the integer determinant scorer.

Bounded scope: mutual blocker-blocker event surfaces can subdivide the product
of the two individual cells, so one paired representative does not exhaust the
coupled product cell.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from pathlib import Path

import build_94_near_miss_atlas as atlaslib
import search_94_coordinate_sweep as wall

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"
ATLAS = ROOT / "H1_14_NEAR_MISS_ATLAS.json"


def eval_form(form, m, b):
    return form[0] * m + form[1] * b + form[2]


def materialize(m, b):
    den = math.lcm(m.denominator, b.denominator)
    return wall.normalize((int(m * den), -1000 * den, int(b * den)))


def crossing_signs(lines, triple, blocker):
    i, j, k = triple
    li, lj, lk = lines[i], lines[j], lines[k]
    wij, wjk, wki = wall.det2(li, lj), wall.det2(lj, lk), wall.det2(lk, li)
    lm = lines[blocker]
    return [
        wall.sign(wall.det3(lm, li, lj) * wij),
        wall.sign(wall.det3(lm, lj, lk) * wjk),
        wall.sign(wall.det3(lm, lk, li) * wki),
    ]


def canonical_target_cell(lines, triple, route):
    moving = route["line"]
    flip_pair = tuple(route["target_vertex_pair"])
    before, oriented_pairs = atlaslib.target_crossing_signs(lines, triple, moving)
    minority = before.index(1) if before.count(1) == 1 else before.index(-1)
    preserve_pairs = {
        tuple(sorted(oriented_pairs[i])) for i in range(3) if i != minority
    }

    events = atlaslib.events_for_moving(lines, moving)
    target = next(
        e for e in events if e[0] == "vertex" and e[1] == flip_pair
    )
    A, B, C = target[2]

    substituted = []
    critical = set()
    if B != 0:
        p, q = -A / B, -C / B
        for e in events:
            if e is target:
                continue
            a, b, c = e[2]
            alpha, beta = a + b * p, b * q + c
            substituted.append((e, alpha, beta))
            if alpha:
                critical.add(-beta / alpha)
        critical = sorted(critical)
        samples = (
            [Fraction(0)]
            if not critical
            else [critical[0] - 1, critical[-1] + 1]
            + [(x + y) / 2 for x, y in zip(critical, critical[1:])]
        )
        wall_point = lambda t: (t, p * t + q)
    else:
        mconst = -C / A
        for e in events:
            if e is target:
                continue
            a, b, c = e[2]
            alpha, beta = b, a * mconst + c
            substituted.append((e, alpha, beta))
            if alpha:
                critical.add(-beta / alpha)
        critical = sorted(critical)
        samples = (
            [Fraction(0)]
            if not critical
            else [critical[0] - 1, critical[-1] + 1]
            + [(x + y) / 2 for x, y in zip(critical, critical[1:])]
        )
        wall_point = lambda t: (mconst, t)

    ranked = []
    for t in samples:
        changes = []
        valid = True
        for e, alpha, beta in substituted:
            s = wall.sign(alpha * t + beta)
            if s == 0:
                valid = False
                break
            if e[0] == "vertex" and e[1] in preserve_pairs and s != e[3]:
                valid = False
                break
            if e[3] == 0 or s != e[3]:
                changes.append(
                    {"kind": e[0], "object": list(e[1]), "seed_sign": e[3], "new_sign": s}
                )
        if valid:
            ranked.append((len(changes), t, changes))
    if not ranked:
        raise RuntimeError("no open target-wall segment preserves other target signs")
    _, t, changes = min(ranked, key=lambda x: (x[0], x[1]))
    m0, b0 = wall_point(t)

    desired = -target[3]
    dm, db = desired * A, desired * B
    bounds = []
    for e in events:
        if e is target:
            continue
        g0 = eval_form(e[2], m0, b0)
        if g0 == 0:
            raise RuntimeError("open target-wall sample hit another event")
        deriv = e[2][0] * dm + e[2][1] * db
        if deriv:
            bounds.append(abs(g0 / deriv))
    eps = min(bounds) / 2 if bounds else Fraction(1)
    m1, b1 = m0 + eps * dm, b0 + eps * db
    new_line = materialize(m1, b1)

    candidate = list(lines)
    candidate[moving] = new_line
    after = crossing_signs(candidate, triple, moving)
    if 1 in after and -1 in after:
        raise RuntimeError("constructed line still blocks target")

    return {
        "moving_line": moving,
        "target_vertex_pair": list(flip_pair),
        "target_signs_before": before,
        "target_signs_after": after,
        "m": [m1.numerator, m1.denominator],
        "b": [b1.numerator, b1.denominator],
        "integer_line": list(new_line),
        "additional_event_changes": changes,
    }


def blockers_for_triple(lines, triple):
    b = atlaslib.blockers_for_triple(lines, *triple)
    return b if b is not None else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=Path, default=SEED)
    ap.add_argument("--atlas", type=Path, default=ATLAS)
    ap.add_argument("--output", type=Path, default=ROOT / "H1_14_DUAL_CELL_RECEIPT.json")
    args = ap.parse_args()

    lines = [tuple(x) for x in json.loads(args.start.read_text())["lines"]]
    if wall.exact_score(lines) != 93:
        raise SystemExit("protected 93 seed drift")
    atlas = json.loads(args.atlas.read_text())

    pair_hist, individual_hist = Counter(), Counter()
    records = []
    for target in atlas["targets"]:
        triple = tuple(target["support_triple"])
        reps, scores = [], []
        for route in target["blocker_routes"]:
            rep = canonical_target_cell(lines, triple, route)
            candidate = list(lines)
            candidate[rep["moving_line"]] = tuple(rep["integer_line"])
            score = wall.exact_score(candidate)
            scores.append(score)
            individual_hist[score] += 1
            reps.append(rep)

        paired = list(lines)
        for rep in reps:
            paired[rep["moving_line"]] = tuple(rep["integer_line"])
        remaining = blockers_for_triple(paired, triple)
        if remaining:
            raise RuntimeError(f"target {triple} remains blocked by {remaining}")
        pair_score = wall.exact_score(paired)
        pair_hist[pair_score] += 1
        records.append(
            {
                "support_triple": list(triple),
                "blockers": target["blockers"],
                "individual_scores": scores,
                "pair_score": pair_score,
                "extra_event_changes": [len(rep["additional_event_changes"]) for rep in reps],
            }
        )

    records.sort(key=lambda x: (-x["pair_score"], x["support_triple"]))
    out = {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-14-DUAL-CELL-RECEIPT",
        "campaign_id": "OPENMATH-2026",
        "hill_slot": "OM26-H1",
        "obligation": "H1-14",
        "state": "COMPLETE__CANONICAL_CLOSEST_DUAL_CELLS_NO_94__BOUNDED_NEGATIVE_ONLY",
        "method": {
            "targets": len(records),
            "blocker_routes": 2 * len(records),
            "arithmetic": "EXACT_RATIONAL_AND_INTEGER_DETERMINANT_SIGNS",
        },
        "results": {
            "best_individual_score": max(individual_hist),
            "individual_score_histogram": {str(k): v for k, v in sorted(individual_hist.items())},
            "best_pair_score": max(pair_hist),
            "pair_score_histogram": {str(k): v for k, v in sorted(pair_hist.items())},
            "found_94_or_better": max(max(individual_hist), max(pair_hist)) >= 94,
        },
        "top_pairs": records[:10],
        "limitations": [
            "One canonical rational representative is scored for each closest individual blocker cell.",
            "Mutual blocker-blocker event surfaces can subdivide the product of two individual cells.",
            "Search failure is not an upper bound or optimality proof.",
        ],
        "next_action": (
            "Enumerate mutual two-moving-line event subdivisions in the highest-ranked product cells, "
            "use Wolfram semialgebraic feasibility for coupled subcells, and exact-rescore every witness."
        ),
        "claim_boundary": "Bounded negative route evidence only; campaign-best-observed remains 93.",
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out["results"], sort_keys=True))


if __name__ == "__main__":
    main()
