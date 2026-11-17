#!/usr/bin/env python3
"""PNP-ABOVE transfer negative control: succinct diagonal games vs
the *specific explicit-table* strategy-to-CNF compiler of WP01.

This proves an unavoidable output-size blowup for that compiler, not
a circuit lower bound or a complexity-theoretic separation.

Source contract: WP01_EXPLICIT_CLASSICAL_TRANSFER_AND_SOURCE_AUDIT.md.
Stdlib only. With m encoded in unary, game constructor is uniform O(m);
the always-empty local strategy is constant size.
"""
from __future__ import annotations
import argparse
import json

def compact_game(m: int) -> dict:
    if m < 1:
        raise ValueError("m must be positive")
    # Sampler draws a uniform m-bit z and sends (z,z).
    # Both provers return the sole allowed answer: the empty string.
    # Only the sampler support, not the Cartesian square, enters WP01's CNF.
    q = 1 << m
    return {"m": m, "questions_each": q, "support_pairs": q,
            "answer_choices_each": 1,
            "formula_variables": 2 * q,
            "formula_clauses": 2 * q}

def verifier(m: int, x: int, y: int, a: str, b: str) -> bool:
    bound = 1 << m
    return 0 <= x < bound and 0 <= y < bound and x == y and a == "" and b == ""

def perfect_strategy(_: int) -> str:
    return ""

def expand_wp01_cnf(m: int) -> tuple[int, list[tuple[int, ...]]]:
    """Exactly the one-hot schema from WP01 on supported question pairs.

    All legal answer sets are {empty}, so only one positive unit clause
    per question per prover remains. No losing-pair clause occurs.
    """
    if not 1 <= m <= 12:
        raise ValueError("explicit enumeration capped at m=12")
    q = 1 << m
    # Alice: literals 1..q; Bob: q+1..2q.
    return 2*q, [(i,) for i in range(1, 2*q+1)]

def check(m: int) -> dict:
    g = compact_game(m)
    q = 1 << m
    assert q == 2**m
    assert g["formula_variables"] == 2**(m+1)
    assert g["formula_clauses"] == 2**(m+1)
    variables, clauses = expand_wp01_cnf(m)
    assert variables == g["formula_variables"] == len(clauses)
    assert all(len(c) == 1 and 1 <= c[0] <= variables for c in clauses)
    # The all-true assignment satisfies every clause; each prover
    # has a uniform, constant-size winning strategy.
    assert all(c[0] > 0 for c in clauses)
    for z in range(q):
        assert verifier(m, z, z, perfect_strategy(z), perfect_strategy(z))
    assert not verifier(m, 0, q - 1, "", "") if m > 1 else True
    assert not verifier(m, 0, 0, "0", "")
    assert not verifier(m, 0, 0, "", "0")
    return g

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--max-m", type=int, default=9)
    a = p.parse_args()
    if not 1 <= a.max_m <= 12:
        p.error("max-m must be 1..12; larger sizes are symbolic only")
    for m in range(1, a.max_m + 1):
        print(json.dumps(check(m), sort_keys=True))
    print("PASS: exact one-hot CNF size and uniform winning strategy")

if __name__ == "__main__":
    main()
