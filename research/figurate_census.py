"""FIGURATE-PILOT-001: exact bounded census for polygonal Diophantine tuples.

No novel theorem is inferred from a bounded search.
Run: python3 -m research.figurate_census --kind B --k 3 --offset 1 --limit 100 --size 3
"""
from __future__ import annotations

import argparse
import itertools
import json
from math import isqrt


def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("require k>=3, t>=1")
    return ((k - 2) * t * t - (k - 4) * t) // 2


def square_root_if_square(z: int) -> int | None:
    if z < 0:
        return None
    root = isqrt(z)
    return root if root * root == z else None


def polygonal_index(k: int, z: int) -> int | None:
    """Return index t>=1 precisely when z=P_k(t); includes congruence/sign."""
    if k < 3 or z < 1:
        return None
    d = (k - 4) ** 2 + 8 * (k - 2) * z
    root = square_root_if_square(d)
    if root is None:
        return None
    numerator = root + (k - 4)
    denominator = 2 * (k - 2)
    if numerator < denominator or numerator % denominator:
        return None
    t = numerator // denominator
    return t if polygonal(k, t) == z else None


def pair_witness(a: int, b: int, kind: str, k: int, offset: int) -> int | None:
    value = a * b + offset
    if kind == "A":
        return square_root_if_square(value)
    if kind in ("B", "C"):
        return polygonal_index(k, value)
    raise ValueError("kind must be A, B or C")


def verify_tuple(values: tuple[int, ...], kind: str, k: int, offset: int) -> dict[str, int] | None:
    if not values or any(a < 1 for a in values) or len(set(values)) != len(values):
        return None
    if kind in ("A", "C") and any(polygonal_index(k, a) is None for a in values):
        return None
    if kind not in ("A", "B", "C"):
        raise ValueError("kind must be A, B or C")
    witnesses = {}
    for a, b in itertools.combinations(sorted(values), 2):
        witness = pair_witness(a, b, kind, k, offset)
        if witness is None:
            return None
        witnesses[f"{a},{b}"] = witness
    return witnesses


def census(kind: str, k: int, offset: int, limit: int, size: int) -> list[dict]:
    if kind not in ("A", "B", "C") or k < 3 or limit < 1 or size < 2:
        raise ValueError("invalid census parameters")
    domain = [a for a in range(1, limit + 1)
              if kind == "B" or polygonal_index(k, a) is not None]
    adjacency = {a: set() for a in domain}
    for a, b in itertools.combinations(domain, 2):
        if pair_witness(a, b, kind, k, offset) is not None:
            adjacency[a].add(b)
    results = []

    def extend(prefix: tuple[int, ...], candidates: list[int]) -> None:
        if len(prefix) == size:
            witnesses = verify_tuple(prefix, kind, k, offset)
            assert witnesses is not None
            results.append({"values": list(prefix), "witnesses": witnesses})
            return
        for i, value in enumerate(candidates):
            extend(prefix + (value,), [other for other in candidates[i + 1:]
                                      if other in adjacency[value]])

    extend((), domain)
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("A", "B", "C"), required=True)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--size", type=int, default=3)
    args = parser.parse_args()
    results = census(args.kind, args.k, args.offset, args.limit, args.size)
    print(json.dumps({"scheme": "FIGURATE-CENSUS/1", "parameters": vars(args),
                      "count": len(results), "results": results}, sort_keys=True))


if __name__ == "__main__":
    main()
