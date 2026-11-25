"""FIGURATE WP09-005: uniform odd-prime-square Type B obstruction.

Sufficient all-triples impossibility; no originality/certification claim.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt


def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("k>=3 and positive index required")
    return t + (k - 2) * t * (t - 1) // 2


def is_prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def legendre(a: int, p: int) -> int:
    if p < 3 or p % 2 == 0 or not is_prime(p):
        raise ValueError("odd prime required")
    value = pow(a % p, (p - 1) // 2, p)
    return -1 if value == p - 1 else value


def uniform_obstruction(k: int, c: int, p: int) -> bool:
    """The proved sufficient p^2 obstruction, not a general equivalence."""
    if k < 3:
        raise ValueError("k>=3 required")
    if p < 3 or p % 2 == 0 or not is_prime(p):
        raise ValueError("odd prime required")
    if (k - 2) % p == 0:
        return False
    coefficient = (k - 2) * pow(2, -1, p) % p
    if legendre(coefficient, p) != -1:
        return False
    delta = 8 * (k - 2) * c + (k - 4) ** 2
    return delta % p == 0 and delta % (p * p) != 0


def local_image(k: int, modulus: int) -> frozenset[int]:
    if modulus < 3 or modulus % 2 == 0:
        raise ValueError("odd modulus>=3 required")
    return frozenset(polygonal(k, t) % modulus
                     for t in range(1, modulus + 1))


def local_witness(k: int, c: int, modulus: int) -> tuple[int, int, int] | None:
    """Exact residue test allowing repeats: distinct entries may be congruent."""
    allowed = {(v - c) % modulus for v in local_image(k, modulus)}
    neighbors = [{b for b in range(modulus) if a * b % modulus in allowed}
                 for a in range(modulus)]
    for a in range(modulus):
        for b in neighbors[a]:
            common = neighbors[a].intersection(neighbors[b])
            if common:
                return a, b, min(common)
    return None


def theorem_count(p: int) -> int:
    if p < 3 or p % 2 == 0 or not is_prime(p):
        raise ValueError("odd prime required")
    return p * (p - 1) ** 2 // 2


def full_audit(p: int) -> dict[str, int]:
    modulus = p * p
    predicted = actual = extra = 0
    for k in range(3, modulus + 3):
        for c in range(modulus):
            obstruction = uniform_obstruction(k, c, p)
            absent = local_witness(k, c, modulus) is None
            predicted += obstruction
            actual += absent
            extra += absent and not obstruction
            if obstruction and not absent:
                raise AssertionError(("false theorem", p, k, c))
    return {"prime": p, "cells": modulus ** 2, "predicted": predicted,
            "locally_excluded": actual, "additional_exclusions": extra}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=7)
    parser.add_argument("--order", type=int)
    parser.add_argument("--offset", type=int)
    parser.add_argument("--audit", action="store_true")
    args = parser.parse_args()
    if args.audit:
        result = full_audit(args.prime)
    else:
        if args.order is None or args.offset is None:
            parser.error("provide --order and --offset, or --audit")
        result = {"prime": args.prime, "order": args.order,
                  "offset": args.offset,
                  "obstructed": uniform_obstruction(args.order, args.offset, args.prime),
                  "local_witness": local_witness(args.order, args.offset, args.prime ** 2)}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
