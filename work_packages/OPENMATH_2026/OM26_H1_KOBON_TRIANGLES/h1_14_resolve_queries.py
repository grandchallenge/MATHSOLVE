#!/usr/bin/env python3
"""Emit exact Wolfram Resolve/FindInstance queries for H1-14 strict event cells.

The strict cell for one moving line preserves every seed pair/triple orientation
relation involving that line except one named target-vertex determinant sign.
This is narrower than the canonical closest-cell search, which is permitted to
cross additional event walls when the strict cell is empty.
"""
from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path

import build_94_near_miss_atlas as atlaslib
import search_94_coordinate_sweep as wall

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"


def form_coeff(lines, j, k):
    aj, _, cj = lines[j]
    ak, _, ck = lines[k]
    return cj - ck, ak - aj, aj * ck - cj * ak


def wall_distance(lines, moving, pair):
    A, B, C = form_coeff(lines, *pair)
    m0, _, b0 = lines[moving]
    num = abs(A * m0 + B * b0 + C)
    return num / math.sqrt(A * A + B * B)


def target_records(lines):
    records = []
    for triple in combinations(range(len(lines)), 3):
        blockers = atlaslib.blockers_for_triple(lines, *triple)
        if blockers is None or len(blockers) != 2:
            continue
        routes = [atlaslib.target_route(lines, triple, blocker) for blocker in blockers]
        records.append({
            "target": triple,
            "blockers": blockers,
            "routes": routes,
            "distance_sum": sum(
                wall_distance(lines, r["line"], tuple(r["target_vertex_pair"]))
                for r in routes
            ),
        })
    records.sort(key=lambda x: (x["distance_sum"], x["target"]))
    return records


def strict_query(lines, moving, target_pair):
    target_key = tuple(sorted((moving, *target_pair)))
    constraints = []

    for j in range(len(lines)):
        if j == moving:
            continue
        sign = wall.sign(wall.det2(lines[moving], lines[j]))
        expr = f"({lines[j][0]}-m)"
        constraints.append(f"{expr}==0" if sign == 0 else f"{expr}{'>' if sign > 0 else '<'}0")

    others = [j for j in range(len(lines)) if j != moving]
    for j, k in combinations(others, 2):
        key = tuple(sorted((moving, j, k)))
        A, B, C = form_coeff(lines, j, k)
        expr = f"({A}*m+{B}*b+{C})"
        sign = wall.sign(wall.det3(lines[moving], lines[j], lines[k]))
        if sign == 0:
            constraints.append(f"{expr}==0")
        else:
            positive = sign > 0
            if key == target_key:
                positive = not positive
            constraints.append(f"{expr}{'>' if positive else '<'}0")

    constraints += ["-50000<m<50000", "-10000<b<10000"]
    body = "&&".join(constraints)
    return f"Resolve[Exists[{{m,b}},{body}],Reals]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=10)
    ap.add_argument("--case", type=int, help="zero-based target rank; omit to list")
    ap.add_argument("--side", type=int, choices=(0, 1), default=0)
    args = ap.parse_args()

    lines = wall.load_solution(SEED)
    if wall.exact_score(lines) != 93:
        raise SystemExit("protected seed score drift")
    records = target_records(lines)[: args.top]

    if args.case is None:
        print(json.dumps([
            {
                "rank": i,
                "target": list(r["target"]),
                "blockers": r["blockers"],
                "routes": [
                    {"line": x["line"], "target_vertex_pair": x["target_vertex_pair"]}
                    for x in r["routes"]
                ],
                "distance_sum_approx": r["distance_sum"],
            }
            for i, r in enumerate(records)
        ], indent=2, sort_keys=True))
        return

    r = records[args.case]
    route = r["routes"][args.side]
    print(strict_query(lines, route["line"], tuple(route["target_vertex_pair"])))


if __name__ == "__main__":
    main()
