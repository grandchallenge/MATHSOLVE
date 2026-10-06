#!/usr/bin/env python3
"""Exact semialgebraic bridge for OM26-H1 score-94 construction search.

This module does not certify mathematics.  It:
- reconstructs a deterministic near-miss atlas around the protected 93 seed;
- scores abstract orientation cells obtained by explicit determinant-sign flips;
- emits Wolfram Language FindInstance queries for exact rational feasibility.

Any candidate >=94 still requires the independent GCL direct oracle and the
ordinary campaign replay/adjudication path.
"""
from __future__ import annotations

import argparse
import json
import math
from itertools import combinations
from pathlib import Path

import search_94_coordinate_sweep as wall

ROOT = Path(__file__).resolve().parent
DEFAULT_SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"


def _perm_sign(values):
    inv = 0
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] > values[j]:
                inv += 1
    return -1 if inv % 2 else 1


def _pair_signs(lines):
    return {
        (i, j): wall.sign(wall.det2(lines[i], lines[j]))
        for i, j in combinations(range(len(lines)), 2)
    }


def _triple_signs(lines):
    return {
        t: wall.sign(wall.det3(lines[t[0]], lines[t[1]], lines[t[2]]))
        for t in combinations(range(len(lines)), 3)
    }


def _d2_sign(pair_signs, a, b):
    if a < b:
        return pair_signs[(a, b)]
    return -pair_signs[(b, a)]


def _d3_sign(triple_signs, a, b, c):
    ordered = (a, b, c)
    key = tuple(sorted(ordered))
    return _perm_sign(ordered) * triple_signs[key]


def score_with_flips(lines, flips):
    """Score the abstract orientation cell obtained by flipping named triple signs.

    Pairwise parallel/nonparallel signs are held fixed.  This is a combinatorial
    prefilter only; realizability must be checked separately.
    """
    pair_signs = _pair_signs(lines)
    triple_signs = _triple_signs(lines)
    for key in {tuple(sorted(x)) for x in flips}:
        if triple_signs[key] == 0:
            raise ValueError(f"cannot flip zero determinant wall {key}")
        triple_signs[key] *= -1

    total = 0
    n = len(lines)
    for i, j, k in combinations(range(n), 3):
        wij = _d2_sign(pair_signs, i, j)
        wjk = _d2_sign(pair_signs, j, k)
        wki = _d2_sign(pair_signs, k, i)
        if 0 in (wij, wjk, wki):
            continue
        if _d3_sign(triple_signs, i, j, k) == 0:
            continue
        crossed = False
        for m in range(n):
            if m in (i, j, k):
                continue
            vals = (
                _d3_sign(triple_signs, m, i, j) * wij,
                _d3_sign(triple_signs, m, j, k) * wjk,
                _d3_sign(triple_signs, m, k, i) * wki,
            )
            if 1 in vals and -1 in vals:
                crossed = True
                break
        if not crossed:
            total += 1
    return total


def blockers(lines, triple):
    i, j, k = triple
    li, lj, lk = lines[i], lines[j], lines[k]
    wij = wall.det2(li, lj)
    wjk = wall.det2(lj, lk)
    wki = wall.det2(lk, li)
    if wij == 0 or wjk == 0 or wki == 0 or wall.det3(li, lj, lk) == 0:
        return None
    out = []
    for m, lm in enumerate(lines):
        if m in triple:
            continue
        vals = (
            wall.sign(wall.det3(lm, li, lj) * wij),
            wall.sign(wall.det3(lm, lj, lk) * wjk),
            wall.sign(wall.det3(lm, lk, li) * wki),
        )
        if 1 in vals and -1 in vals:
            out.append((m, vals))
    return out


def required_flip_key(triple, blocker, vals):
    i, j, k = triple
    edges = ((i, j), (j, k), (k, i))
    positives = vals.count(1)
    negatives = vals.count(-1)
    if positives == negatives or 0 in vals:
        raise ValueError(f"no unique one-wall exit for blocker={blocker}, vals={vals}")
    minority = -1 if negatives < positives else 1
    edge = edges[vals.index(minority)]
    return tuple(sorted((blocker, edge[0], edge[1])))


def wall_coefficients(lines, moving, flip_key):
    """Return A,B,C for det([m,-1000,b], Lj, Lk)/1000 = A*m+B*b+C."""
    if lines[moving][1] != -1000:
        raise ValueError("seed normalization requires moving line second coefficient -1000")
    fixed = [x for x in flip_key if x != moving]
    if len(fixed) != 2:
        raise ValueError("flip key must contain moving line and two fixed lines")
    j, k = fixed
    aj, bj, cj = lines[j]
    ak, bk, ck = lines[k]
    if bj != -1000 or bk != -1000:
        raise ValueError("wall coefficient shortcut requires fixed second coefficients -1000")
    return (cj - ck, ak - aj, aj * ck - cj * ak)


def wall_distance(lines, moving, flip_key):
    A, B, C = wall_coefficients(lines, moving, flip_key)
    m0, _, b0 = lines[moving]
    numerator = abs(A * m0 + B * b0 + C)
    norm_sq = A * A + B * B
    approx = numerator / math.sqrt(norm_sq)
    return numerator, norm_sq, approx


def build_atlas(lines):
    distribution = {}
    proper_triangles = 0
    improper = 0
    two_blocker = []

    for triple in combinations(range(len(lines)), 3):
        bs = blockers(lines, triple)
        if bs is None:
            improper += 1
            continue
        if not bs:
            proper_triangles += 1
            continue
        distribution[str(len(bs))] = distribution.get(str(len(bs)), 0) + 1
        if len(bs) != 2:
            continue

        flip_keys = [required_flip_key(triple, m, vals) for m, vals in bs]
        distances = []
        for (m, vals), key in zip(bs, flip_keys):
            num, norm_sq, approx = wall_distance(lines, m, key)
            distances.append(
                {
                    "moving_line": m,
                    "blocking_pattern": list(vals),
                    "required_flip_key": list(key),
                    "wall_abs_numerator": num,
                    "wall_norm_sq": norm_sq,
                    "wall_distance_approx": approx,
                    "single_flip_abstract_score": score_with_flips(lines, [key]),
                }
            )

        two_blocker.append(
            {
                "target_triple": list(triple),
                "blockers": distances,
                "minimal_two_flip_abstract_score": score_with_flips(lines, flip_keys),
                "distance_sum_approx": sum(x["wall_distance_approx"] for x in distances),
                "distance_max_approx": max(x["wall_distance_approx"] for x in distances),
            }
        )

    two_blocker.sort(
        key=lambda x: (
            x["distance_sum_approx"],
            x["distance_max_approx"],
            x["target_triple"],
        )
    )
    return {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-14-NEAR-MISS-ATLAS",
        "seed_score": wall.exact_score(lines),
        "proper_triangle_count": proper_triangles,
        "improper_triple_count": improper,
        "proper_nonface_blocker_distribution": dict(sorted(distribution.items(), key=lambda kv: int(kv[0]))),
        "two_blocker_count": len(two_blocker),
        "one_blocker_count": distribution.get("1", 0),
        "two_blocker_cases": two_blocker,
        "claim_boundary": (
            "Deterministic local combinatorial atlas around the protected 93 seed. "
            "Abstract cell scores are not realizability or optimality claims."
        ),
    }


def _wl_line(lines, index, moving_names):
    if index in moving_names:
        m, b = moving_names[index]
        return "{" + f"{m},-1000,{b}" + "}"
    a, bb, c = lines[index]
    return "{" + f"{a},{bb},{c}" + "}"


def _wl_det3(lines, i, j, k, moving_names):
    return "Det[{" + ",".join(_wl_line(lines, x, moving_names) for x in (i, j, k)) + "}]"


def wolfram_query(lines, moving_names, flips, rational=True):
    """Emit exact FindInstance query preserving all seed signs except declared flips."""
    flips = {tuple(sorted(x)) for x in flips}
    constraints = []
    movers = set(moving_names)

    for i, j in combinations(range(len(lines)), 2):
        if i not in movers and j not in movers:
            continue
        ai = moving_names[i][0] if i in movers else str(lines[i][0])
        aj = moving_names[j][0] if j in movers else str(lines[j][0])
        expr = f"({aj}-({ai}))"
        s = wall.sign(wall.det2(lines[i], lines[j]))
        constraints.append(f"{expr}==0" if s == 0 else f"{expr}{'>' if s > 0 else '<'}0")

    for i, j, k in combinations(range(len(lines)), 3):
        if not any(x in movers for x in (i, j, k)):
            continue
        key = (i, j, k)
        s = wall.sign(wall.det3(lines[i], lines[j], lines[k]))
        expr = _wl_det3(lines, i, j, k, moving_names)
        if s == 0:
            constraints.append(f"{expr}==0")
        else:
            positive = s > 0
            if key in flips:
                positive = not positive
            constraints.append(f"{expr}{'>' if positive else '<'}0")

    variables = []
    for index in sorted(moving_names):
        m, b = moving_names[index]
        variables.extend((m, b))
        constraints.extend((f"-50000<{m}<50000", f"-10000<{b}<10000"))

    domain = "Rationals" if rational else "Reals"
    return "FindInstance[" + "&&".join(constraints) + ",{" + ",".join(variables) + f"}},{domain},1]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--seed", type=Path, default=DEFAULT_SEED)
    sub = ap.add_subparsers(dest="command", required=True)

    atlas = sub.add_parser("atlas")
    atlas.add_argument("--output", type=Path)

    query = sub.add_parser("query")
    query.add_argument("--moving", action="append", required=True, help="INDEX:MVAR:BVAR")
    query.add_argument("--flip", action="append", required=True, help="i,j,k")
    query.add_argument("--reals", action="store_true")

    args = ap.parse_args()
    lines = wall.load_solution(args.seed)
    if wall.exact_score(lines) != 93:
        raise SystemExit("protected seed score drift")

    if args.command == "atlas":
        result = build_atlas(lines)
        text = json.dumps(result, indent=2, sort_keys=True) + "\n"
        if args.output:
            args.output.write_text(text)
        else:
            print(text, end="")
        return

    moving_names = {}
    for spec in args.moving:
        index, m, b = spec.split(":", 2)
        moving_names[int(index)] = (m, b)
    flips = [tuple(int(x) for x in spec.split(",")) for spec in args.flip]
    print(wolfram_query(lines, moving_names, flips, rational=not args.reals))


if __name__ == "__main__":
    main()
