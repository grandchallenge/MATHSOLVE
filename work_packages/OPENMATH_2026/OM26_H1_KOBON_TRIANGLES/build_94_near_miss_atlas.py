#!/usr/bin/env python3
"""Build the exact two-blocker near-miss atlas around RH_BADER_RECONSTRUCTION_093.

The atlas is route evidence only. It enumerates support triples under the same
integer-determinant face predicate used by search_94_coordinate_sweep.py and
measures how many fixed-arrangement event walls separate each blocking line
from the target-unblocked side.
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction
from itertools import combinations
from pathlib import Path

import search_94_coordinate_sweep as wall

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"


def blockers_for_triple(lines, i, j, k):
    li, lj, lk = lines[i], lines[j], lines[k]
    wij, wjk, wki = wall.det2(li, lj), wall.det2(lj, lk), wall.det2(lk, li)
    if wij == 0 or wjk == 0 or wki == 0 or wall.det3(li, lj, lk) == 0:
        return None
    out = []
    for m, lm in enumerate(lines):
        if m in (i, j, k):
            continue
        vals = (
            wall.sign(wall.det3(lm, li, lj) * wij),
            wall.sign(wall.det3(lm, lj, lk) * wjk),
            wall.sign(wall.det3(lm, lk, li) * wki),
        )
        if 1 in vals and -1 in vals:
            out.append(m)
    return out


def form_coeff(lines, j, k):
    aj, _, cj = lines[j]
    ak, _, ck = lines[k]
    # det3({m,-1000,b}, Lj, Lk) / 1000
    return Fraction(cj - ck), Fraction(ak - aj), Fraction(aj * ck - cj * ak)


def events_for_moving(lines, moving):
    events = []
    others = [i for i in range(len(lines)) if i != moving]
    m0, _, b0 = lines[moving]
    for j, k in combinations(others, 2):
        form = form_coeff(lines, j, k)
        value = form[0] * m0 + form[1] * b0 + form[2]
        events.append(("vertex", (j, k), form, wall.sign(value)))
    for j in others:
        aj = lines[j][0]
        form = (Fraction(-1), Fraction(0), Fraction(aj))
        value = aj - m0
        events.append(("parallel", (j,), form, wall.sign(value)))
    return events


def target_crossing_signs(lines, triple, blocker):
    i, j, k = triple
    li, lj, lk = lines[i], lines[j], lines[k]
    wij, wjk, wki = wall.det2(li, lj), wall.det2(lj, lk), wall.det2(lk, li)
    lm = lines[blocker]
    vals = [
        wall.sign(wall.det3(lm, li, lj) * wij),
        wall.sign(wall.det3(lm, lj, lk) * wjk),
        wall.sign(wall.det3(lm, lk, li) * wki),
    ]
    return vals, [(i, j), (j, k), (k, i)]


def target_route(lines, triple, blocker):
    signs, oriented_pairs = target_crossing_signs(lines, triple, blocker)
    if not (1 in signs and -1 in signs):
        raise RuntimeError("declared blocker does not cross target")
    minority = signs.index(1) if signs.count(1) == 1 else signs.index(-1)
    flip_pair = tuple(sorted(oriented_pairs[minority]))
    preserve_pairs = {
        tuple(sorted(oriented_pairs[i])) for i in range(3) if i != minority
    }

    events = events_for_moving(lines, blocker)
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

    best = None
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
                    {
                        "kind": e[0],
                        "object": list(e[1]),
                        "seed_sign": e[3],
                        "new_sign": s,
                    }
                )
        if valid and (best is None or len(changes) < best[0]):
            best = (len(changes), changes)

    if best is None:
        raise RuntimeError("no open target-wall segment preserves the other target signs")

    return {
        "line": blocker,
        "target_vertex_pair": list(flip_pair),
        "target_crossing_signs": signs,
        "minimum_additional_event_changes": best[0],
        "additional_event_changes": best[1],
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=Path, default=SEED)
    ap.add_argument("--output", type=Path, default=ROOT / "H1_14_NEAR_MISS_ATLAS.json")
    args = ap.parse_args()

    lines = [tuple(x) for x in json.loads(args.start.read_text())["lines"]]
    baseline = []
    hist = Counter()
    proper = []
    for triple in combinations(range(len(lines)), 3):
        blockers = blockers_for_triple(lines, *triple)
        if blockers is None:
            continue
        hist[len(blockers)] += 1
        if not blockers:
            baseline.append(triple)
        else:
            proper.append((triple, blockers))

    if wall.exact_score(lines) != 93 or len(baseline) != 93:
        raise SystemExit("protected 93 seed drift")

    support = Counter(i for triple in baseline for i in triple)
    two = []
    for triple, blockers in proper:
        if len(blockers) != 2:
            continue
        routes = [target_route(lines, triple, blocker) for blocker in blockers]
        affected = {
            tri
            for tri in baseline
            if any(blocker in tri for blocker in blockers)
        }
        two.append(
            {
                "support_triple": list(triple),
                "blockers": blockers,
                "blocker_face_support_counts": [support[x] for x in blockers],
                "baseline_faces_incident_to_either_blocker": len(affected),
                "blocker_routes": [
                    {
                        "line": route["line"],
                        "target_vertex_pair": route["target_vertex_pair"],
                        "minimum_additional_event_changes": route["minimum_additional_event_changes"],
                    }
                    for route in routes
                ],
            }
        )

    positive = [k for k in hist if k > 0]
    out = {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-14-NEAR-MISS-ATLAS",
        "campaign_id": "OPENMATH-2026",
        "hill_slot": "OM26-H1",
        "obligation": "H1-14",
        "seed": {"candidate": "RH_BADER_RECONSTRUCTION_093", "score": 93},
        "proper_support_triples": sum(hist.values()),
        "degenerate_support_triples": len(list(combinations(range(len(lines)), 3))) - sum(hist.values()),
        "baseline_triangles": len(baseline),
        "nonface_blocker_histogram": {str(k): v for k, v in sorted(hist.items())},
        "minimum_positive_blocker_count": min(positive),
        "two_blocker_target_count": len(two),
        "targets": two,
        "claim_boundary": (
            "Exact local/combinatorial route data around one protected 93 arrangement only; "
            "not an upper bound and not exhaustive over higher-dimensional deformations."
        ),
    }
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "baseline_triangles": len(baseline),
        "minimum_positive_blocker_count": min(positive),
        "two_blocker_target_count": len(two),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
