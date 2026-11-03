"""FIGURATE WP06: admissibility-preserving modular filter and count-only census.

No proof of a new Diophantine theorem is implied. The filter is a necessary
local condition. Modular rejection can never discard a genuine exact edge.

CLI:
  python3 -m research.figurate_residue_sieve --kind B --k 3 --offset 1 --limit 120 --size 3
"""
from __future__ import annotations

import argparse
import itertools
import json
from functools import lru_cache
from math import isqrt
from research.figurate_census import polygonal_index

DEFAULT_MODULI = (8, 9, 5, 7, 11)


@lru_cache(maxsize=None)
def allowed_residues(kind: str, k: int, modulus: int) -> frozenset[int]:
    """Exact complete residue image of the target sequence modulo modulus.

    For polygonals, t -> t + 2m preserves P_k(t) modulo m, so positive
    t=1,...,2m covers all residue classes. Squares need t=0,...,m-1.
    """
    if modulus < 2 or k < 3 or kind not in ("A", "B", "C"):
        raise ValueError("invalid residue specification")
    if kind == "A":
        return frozenset((r * r) % modulus for r in range(modulus))
    return frozenset(
        (((k - 2) * t * t - (k - 4) * t) // 2) % modulus
        for t in range(1, 2 * modulus + 1)
    )


def local_possible(a: int, b: int, kind: str, k: int, offset: int,
                   moduli: tuple[int, ...] = DEFAULT_MODULI) -> bool:
    z = a * b + offset
    return all(z % m in allowed_residues(kind, k, m) for m in moduli)


def exact_pair(a: int, b: int, kind: str, k: int, offset: int) -> bool:
    z = a * b + offset
    if kind == "A":
        if z < 0:
            return False
        r = isqrt(z)
        return r * r == z
    return polygonal_index(k, z) is not None


def census_summary(kind: str, k: int, offset: int, limit: int, size: int,
                   moduli: tuple[int, ...] = DEFAULT_MODULI) -> dict:
    if kind not in ("A", "B", "C") or k < 3 or limit < 1 or size < 2:
        raise ValueError("invalid census parameters")
    if any(m < 2 for m in moduli):
        raise ValueError("moduli must be >=2")
    domain = [a for a in range(1, limit + 1)
              if kind == "B" or polygonal_index(k, a) is not None]
    adjacency = {a: set() for a in domain}
    possible_pairs = len(domain) * (len(domain) - 1) // 2
    residue_rejected = 0
    exact_calls = 0
    accepted_edges = 0
    for a, b in itertools.combinations(domain, 2):
        if not local_possible(a, b, kind, k, offset, moduli):
            residue_rejected += 1
            continue
        exact_calls += 1
        if exact_pair(a, b, kind, k, offset):
            adjacency[a].add(b)
            accepted_edges += 1

    count = 0
    first = None

    def extend(prefix: tuple[int, ...], candidates: list[int]) -> None:
        nonlocal count, first
        if len(prefix) == size:
            count += 1
            if first is None:
                first = list(prefix)
            return
        required = size - len(prefix)
        if len(candidates) < required:
            return
        for i, value in enumerate(candidates):
            rest = [other for other in candidates[i + 1:]
                    if other in adjacency[value]]
            if len(rest) + 1 < required:
                continue
            extend(prefix + (value,), rest)

    extend((), domain)
    return {"scheme": "FIGURATE-SIEVED-CENSUS/1", "kind": kind,
            "k": k, "offset": offset, "limit": limit, "size": size,
            "moduli": list(moduli), "vertices": len(domain),
            "candidate_pairs": possible_pairs, "residue_rejected": residue_rejected,
            "exact_pair_checks": exact_calls, "edges": accepted_edges,
            "count": count, "first_values": first}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", choices=("A", "B", "C"), required=True)
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--size", type=int, default=3)
    args = parser.parse_args()
    print(json.dumps(census_summary(args.kind, args.k, args.offset,
                                    args.limit, args.size), sort_keys=True))


if __name__ == "__main__":
    main()
