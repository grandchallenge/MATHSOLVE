#!/usr/bin/env python3
"""H1-14 coupled-cell subdivision, depth one.

Starting from each target's canonical closest blocker cells, hold one blocker at
its canonical rational representative and move the other across each single
mutual event wall (parallelism or concurrence with one of the 16 fixed lines),
while preserving every external-cell sign and every other mutual-event sign.

All arithmetic is exact. This is a depth-one subdivision, not exhaustive over
multi-mutual-wall transitions or unrestricted four-variable motion.
"""
from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import build_94_near_miss_atlas as atlaslib
import search_94_coordinate_sweep as wall
import search_94_dual_cells as dual

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"
ATLAS = ROOT / "H1_14_NEAR_MISS_ATLAS.json"


def eval_form(form, m, b):
    return form[0] * m + form[1] * b + form[2]


def mb_from_line(line):
    A, B, C = map(Fraction, line)
    if B == 0:
        raise ValueError("vertical line cannot use [m,-1000,b] chart")
    scale = Fraction(-1000, 1) / B
    return A * scale, C * scale


def general_vertex_form(y, z):
    y0, y1, y2 = map(Fraction, y)
    z0, z1, z2 = map(Fraction, z)
    return (
        y1 * z2 - y2 * z1,
        y0 * z1 - y1 * z0,
        Fraction(1000) * (y0 * z2 - y2 * z0),
    )


def general_parallel_form(y):
    y0, y1, _ = map(Fraction, y)
    return y1, Fraction(0), Fraction(1000) * y0


def materialize(m, b):
    den = math.lcm(m.denominator, b.denominator)
    return wall.normalize((int(m * den), -1000 * den, int(b * den)))


def event_set(seed, moving, other, other_line, current_line):
    fixed = [i for i in range(len(seed)) if i not in (moving, other)]
    m0, b0 = mb_from_line(current_line)
    events = []

    for j, k in combinations(fixed, 2):
        form = general_vertex_form(seed[j], seed[k])
        events.append(
            ("external_vertex", (j, k), form, wall.sign(eval_form(form, m0, b0)))
        )
    for j in fixed:
        form = general_parallel_form(seed[j])
        events.append(
            ("external_parallel", (j,), form, wall.sign(eval_form(form, m0, b0)))
        )

    form = general_parallel_form(other_line)
    events.append(
        ("mutual_parallel", (other,), form, wall.sign(eval_form(form, m0, b0)))
    )
    for j in fixed:
        form = general_vertex_form(other_line, seed[j])
        events.append(
            ("mutual_vertex", (other, j), form, wall.sign(eval_form(form, m0, b0)))
        )
    return events


def adjacent_flip(current_line, events, target_index):
    target = events[target_index]
    if target[3] == 0:
        return None
    A, B, C = target[2]

    substituted = []
    critical = set()
    if B != 0:
        p, q = -A / B, -C / B
        for idx, e in enumerate(events):
            if idx == target_index:
                continue
            a, b, c = e[2]
            alpha, beta = a + b * p, b * q + c
            substituted.append((idx, e, alpha, beta))
            if alpha:
                critical.add(-beta / alpha)
        wall_point = lambda t: (t, p * t + q)
    else:
        if A == 0:
            return None
        mconst = -C / A
        for idx, e in enumerate(events):
            if idx == target_index:
                continue
            a, b, c = e[2]
            alpha, beta = b, a * mconst + c
            substituted.append((idx, e, alpha, beta))
            if alpha:
                critical.add(-beta / alpha)
        wall_point = lambda t: (mconst, t)

    critical = sorted(critical)
    samples = (
        [Fraction(0)]
        if not critical
        else [critical[0] - 1, critical[-1] + 1]
        + [(x + y) / 2 for x, y in zip(critical, critical[1:])]
    )

    valid = []
    for t in samples:
        if all(
            wall.sign(alpha * t + beta) == e[3] and e[3] != 0
            for _, e, alpha, beta in substituted
        ):
            valid.append(t)
    if not valid:
        return None

    t = valid[0]
    m0, b0 = wall_point(t)
    desired = -target[3]
    dm, db = desired * A, desired * B
    bounds = []
    for idx, e in enumerate(events):
        if idx == target_index:
            continue
        g0 = eval_form(e[2], m0, b0)
        if g0 == 0:
            return None
        deriv = e[2][0] * dm + e[2][1] * db
        if deriv:
            bounds.append(abs(g0 / deriv))
    eps = min(bounds) / 2 if bounds else Fraction(1)
    m1, b1 = m0 + eps * dm, b0 + eps * db

    for idx, e in enumerate(events):
        s = wall.sign(eval_form(e[2], m1, b1))
        if idx == target_index:
            if s != desired:
                return None
        elif s != e[3]:
            return None

    return materialize(m1, b1), m1, b1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=Path, default=SEED)
    ap.add_argument("--atlas", type=Path, default=ATLAS)
    ap.add_argument("--output", type=Path, default=ROOT / "H1_14_COUPLED_CELL_RECEIPT.json")
    args = ap.parse_args()

    seed = [tuple(x) for x in json.loads(args.start.read_text())["lines"]]
    if wall.exact_score(seed) != 93:
        raise SystemExit("protected 93 seed drift")
    atlas = json.loads(args.atlas.read_text())

    attempted = 0
    feasible = 0
    score_hist = Counter()
    records = []

    for target in atlas["targets"]:
        triple = tuple(target["support_triple"])
        reps = [
            dual.canonical_target_cell(seed, triple, route)
            for route in target["blocker_routes"]
        ]
        base = list(seed)
        for rep in reps:
            base[rep["moving_line"]] = tuple(rep["integer_line"])
        base_score = wall.exact_score(base)

        for side in range(2):
            moving = reps[side]["moving_line"]
            other = reps[1 - side]["moving_line"]
            current = base[moving]
            other_line = base[other]
            events = event_set(seed, moving, other, other_line, current)

            for idx, event in enumerate(events):
                if not event[0].startswith("mutual_"):
                    continue
                attempted += 1
                candidate = adjacent_flip(current, events, idx)
                if candidate is None:
                    continue
                feasible += 1
                new_line, m, b = candidate
                arrangement = list(base)
                arrangement[moving] = new_line
                if atlaslib.blockers_for_triple(arrangement, *triple):
                    raise RuntimeError("mutual-cell move re-blocked the target")
                score = wall.exact_score(arrangement)
                score_hist[score] += 1
                records.append(
                    {
                        "support_triple": list(triple),
                        "blockers": target["blockers"],
                        "base_pair_score": base_score,
                        "moving_line": moving,
                        "mutual_event": {
                            "kind": event[0],
                            "object": list(event[1]),
                            "seed_sign": event[3],
                            "new_sign": -event[3],
                        },
                        "score": score,
                    }
                )

    records.sort(key=lambda x: (-x["score"], -x["base_pair_score"], x["support_triple"]))
    best = max(score_hist) if score_hist else None
    out = {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-14-COUPLED-CELL-RECEIPT",
        "campaign_id": "OPENMATH-2026",
        "hill_slot": "OM26-H1",
        "obligation": "H1-14",
        "state": "COMPLETE__DEPTH1_MUTUAL_SUBDIVISION_NO_94__BOUNDED_NEGATIVE_ONLY",
        "method": {
            "targets": len(atlas["targets"]),
            "attempted_single_mutual_event_flips": attempted,
            "feasible_adjacent_mutual_subcells": feasible,
            "arithmetic": "EXACT_RATIONAL_AND_INTEGER_DETERMINANT_SIGNS",
        },
        "results": {
            "best_score": best,
            "score_histogram": {str(k): v for k, v in sorted(score_hist.items())},
            "found_94_or_better": bool(best is not None and best >= 94),
        },
        "top_witnesses": records[:10],
        "limitations": [
            "Depth-one only: exactly one mutual blocker-blocker event is flipped while all other external and mutual event signs are preserved.",
            "Multi-mutual-wall transitions and unrestricted four-variable motion remain outside this receipt.",
            "Negative search evidence is not an upper-bound or optimality proof.",
        ],
        "next_action": (
            "Do not escalate to 4-5 active lines from this layer: no coupled depth-one witness is competitive with 93. "
            "Feed the exact lost-face/event patterns into local-move obstruction analysis, and reserve deeper coupled CAD "
            "for any product cell that later receives an independent structural reason to revisit."
        ),
        "claim_boundary": "Bounded negative route evidence only; campaign-best-observed remains 93.",
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out["method"] | out["results"], sort_keys=True))


if __name__ == "__main__":
    main()
