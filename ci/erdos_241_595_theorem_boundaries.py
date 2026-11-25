#!/usr/bin/env python3
"""Finite hostile checks of two EXACT conditional theorem families.

Proofs are in contributions/ERDOS-OPEN-001/CATALOGUE_LOCAL_REPLAY_002/
EXACT_THEOREMS.md. This checks bounded finite examples, not the infinite
quantifiers, primary sources, Lean kernel, or an Erdős conjecture.
"""
from __future__ import annotations
import json
from itertools import combinations_with_replacement


def b_h(A: list[int], h: int, m: int | None = None) -> bool:
    vals = [sum(t) for t in combinations_with_replacement(A, h)]
    if m is not None:
        vals = [v % m for v in vals]
    return len(vals) == len(set(vals))


def positive_differences(A: list[int], h: int) -> set[int]:
    sums = sorted({sum(t) for t in combinations_with_replacement(A, h)})
    return {b - a for i, a in enumerate(sums) for b in sums[i+1:]}


def check_b_h() -> dict:
    sets = 0
    modulus_checks = 0
    for h in range(1, 5):
        for n in range(2, 8):
            for bits in range(1 << n):
                A = [i + 1 for i in range(n) if (bits >> i) & 1]
                diameter = max(A) - min(A) if A else 0
                integral = b_h(A, h)
                differences = positive_differences(A, h) if integral else set()
                for m in range(1, h * (n - 1) + 3):
                    modular = b_h(A, h, m)
                    if m > h * diameter:
                        assert modular == integral, (h, n, A, m, "width")
                    if integral:
                        # Exact necessary AND sufficient modular safety test.
                        assert modular == all(delta % m for delta in differences), (
                            h, n, A, m, "difference criterion"
                        )
                    else:
                        assert not modular, (h, n, A, m, "cannot repair collision")
                    modulus_checks += 1
                sets += 1
    # Sharpness of M > h*diameter: when A={a,b}, M=h(b-a)
    # collides the h copies of a and h copies of b.
    sharp_cases = 0
    for h in range(1, 10):
        for diameter in range(1, 12):
            A = [3, 3 + diameter]
            assert b_h(A, h)
            assert not b_h(A, h, h * diameter)
            sharp_cases += 1
    assert b_h([1, 4], 3, 4) and not b_h([1, 4], 3, 3)
    return {
        "status": "PASS",
        "finite_sets_checked": sets,
        "set_modulus_pairs_checked": modulus_checks,
        "sharp_two_point_cases": sharp_cases,
        "example": {"A": [1, 4], "h": 3, "safe_modulus": 4,
                    "universal_safe_bound": 10},
    }


def chromatic_number(n: int, edges: list[tuple[int, int]]) -> int:
    neighbours = [set() for _ in range(n)]
    for u, v in edges:
        neighbours[u].add(v)
        neighbours[v].add(u)
    for k in range(1, n + 1):
        colours = [-1] * n

        def search(i: int) -> bool:
            if i == n:
                return True
            for c in range(k):
                if all(colours[j] != c for j in neighbours[i]):
                    colours[i] = c
                    if search(i + 1):
                        return True
                    colours[i] = -1
            return False

        if search(0):
            return k
    raise AssertionError("nonempty finite graph must be colourable")


def check_graph_cover() -> dict:
    graphs = 0
    cover_tests = 0
    for n in range(1, 6):
        pairs = [(u, v) for u in range(n) for v in range(u + 1, n)]
        # Independently enumerate ALL two-colour cuts, with first
        # vertex assigned colour zero to remove complement duplicates.
        cuts = []
        for choice in range(1 << (n - 1)):
            colouring = [0] + [(choice >> (v - 1)) & 1 for v in range(1, n)]
            cuts.append(sum(1 << i for i, (u, v) in enumerate(pairs)
                            if colouring[u] != colouring[v]))
        # Union of <= t bipartite edge-layers (cut intersections).
        unions = [{0}]
        for t in range(1, 4):
            unions.append({base | cut for base in unions[-1] for cut in cuts})
        for edge_mask in range(1 << len(pairs)):
            E = [e for i, e in enumerate(pairs) if (edge_mask >> i) & 1]
            chi = chromatic_number(n, E)
            for t in range(4):
                has_cover = any((edge_mask & support) == edge_mask
                                for support in unions[t])
                assert has_cover == (chi <= (1 << t)), (n, edge_mask, t, chi)
                cover_tests += 1
            graphs += 1
    return {"status": "PASS", "graphs_checked": graphs,
            "cover_vs_chromatic_checks": cover_tests,
            "vertex_range": [1, 5], "layer_range": [0, 3]}


def verify() -> dict:
    return {"ERDOS-241": check_b_h(), "ERDOS-595": check_graph_cover()}


if __name__ == "__main__":
    print(json.dumps(verify(), sort_keys=True, indent=2))
