"""FIGURATE WP08: 2-adic polygonal surjectivity and exact modulo-64 local triples.

This module distinguishes:
 (1) the unbounded constructive theorem P_k(N_+) mod 2^n = all residues
     iff 4 does not divide k, and
 (2) the finite local residue certificate for Type B triples modulo 64.

Nonempty local compatibility is NOT existence of an integer tuple.
"""
from __future__ import annotations

import argparse
import hashlib
import json

from research.figurate_census import polygonal


def lift_polygonal_index(k: int, residue: int, exponent: int) -> int:
    """Construct t>=1 with P_k(t)=residue mod 2**exponent when 4∤k.

    For odd k, increment by 2**(n+1) to toggle bit n.
    For k=2 mod 4, increment by 2**n to toggle bit n.
    Both preserve all lower bits. This is a constructive proof, not search.
    """
    if k < 3 or k % 4 == 0 or exponent < 1:
        raise ValueError("require k>=3, 4 not dividing k, exponent>=1")
    modulus = 1 << exponent
    target = residue % modulus
    t = 1 if target & 1 else (3 if k & 1 else 2)
    for bit in range(1, exponent):
        mod = 1 << (bit + 1)
        if polygonal(k, t) % mod != target % mod:
            t += 1 << (bit + 1 if k & 1 else bit)
        assert polygonal(k, t) % mod == target % mod
    return t


def polygonal_image(k: int, modulus: int) -> frozenset[int]:
    if k < 3 or modulus < 2:
        raise ValueError("require k>=3, modulus>=2")
    return frozenset(polygonal(k, t) % modulus
                     for t in range(1, 2 * modulus + 1))


def local_first_triple(k: int, c: int, modulus: int = 64
                       ) -> tuple[int, int, int] | None:
    """Exact lexicographically first locally viable residue multiset.

    Symmetric adjacency masks provide independent O(m^3) scalar arithmetic
    and O(m^2) machine-word intersections, with repeated residue labels.
    """
    image = polygonal_image(k, modulus)
    c %= modulus
    masks = [sum(1 << b for b in range(modulus)
                 if (a * b + c) % modulus in image)
             for a in range(modulus)]
    for a in range(modulus):
        for b in range(a, modulus):
            if masks[a] & (1 << b):
                common = (masks[a] & masks[b]) >> b
                if common:
                    low_bit = common & -common
                    return (a, b, b + low_bit.bit_length() - 1)
    return None


def complete_table(modulus: int = 64
                   ) -> dict[int, dict[int, tuple[int, int, int] | None]]:
    if modulus < 2:
        raise ValueError("modulus>=2")
    return {k % modulus:
            {c: local_first_triple(k, c, modulus)
             for c in range(modulus)}
            for k in range(modulus, 2 * modulus)}


def exclusions(modulus: int = 64) -> dict[int, tuple[int, ...]]:
    return {k: tuple(c for c, witness in row.items() if witness is None)
            for k, row in complete_table(modulus).items()}


def canonical_sha256(modulus: int = 64) -> str:
    raw = json.dumps(complete_table(modulus), sort_keys=True,
                     separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def newly_excluded_from_32() -> tuple[tuple[int, int], ...]:
    from research.figurate_wp08_mod32 import exclusions as prior
    old = prior(32)
    new = exclusions(64)
    return tuple((k, c) for k in range(64) for c in new[k]
                 if c % 32 not in old[k % 32])


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--k", type=int)
    p.add_argument("--offset", type=int)
    p.add_argument("--exponent", type=int)
    p.add_argument("--residue", type=int)
    args = p.parse_args()
    if args.exponent is not None or args.residue is not None:
        if args.k is None or args.exponent is None or args.residue is None:
            p.error("lifting requires --k, --exponent, --residue")
        index = lift_polygonal_index(args.k, args.residue, args.exponent)
        result = {"scheme": "FIGURATE-WP08-BINARY-LIFT/1",
                  "k": args.k, "residue": args.residue,
                  "exponent": args.exponent, "index": index,
                  "value_residue": polygonal(args.k, index)
                                   % (1 << args.exponent)}
    else:
        if args.k is None and args.offset is None:
            result = {"scheme": "FIGURATE-WP08-MOD64/1",
                      "modulus": 64,
                      "exclusions": exclusions(64),
                      "new_from_mod32": newly_excluded_from_32(),
                      "witness_table_sha256": canonical_sha256(64)}
        elif args.k is not None and args.offset is not None:
            witness = local_first_triple(args.k, args.offset, 64)
            result = {"scheme": "FIGURATE-WP08-MOD64-CELL/1",
                      "k": args.k, "offset": args.offset,
                      "modulus": 64,
                      "first_local_witness": witness,
                      "global_obstruction": witness is None}
        else:
            p.error("cell requires both --k and --offset")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
