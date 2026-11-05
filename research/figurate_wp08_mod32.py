"""FIGURATE WP08: complete necessary Type B triple conditions modulo 32.

The 32-by-32 table is a finite certificate of *local* impossibility.
If no triple of entry residues survives, no positive integer triple can.
The converse is false. Distinct integers may share a residue class, so
the enumeration permits repeated residue classes.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json

from research.figurate_census import polygonal


def polygonal_image(k: int, modulus: int = 32) -> frozenset[int]:
    if k < 3 or modulus < 2:
        raise ValueError("polygonal order >= 3 and modulus >= 2 required")
    return frozenset(polygonal(k, t) % modulus
                     for t in range(1, 2 * modulus + 1))


def first_local_witness(k: int, offset: int, modulus: int = 32
                        ) -> tuple[int, int, int] | None:
    """Lexicographically first compatible residue multiset, if one exists."""
    R = polygonal_image(k, modulus)
    c = offset % modulus
    for a, b, d in itertools.combinations_with_replacement(range(modulus), 3):
        if ((a*b+c) % modulus in R and
            (a*d+c) % modulus in R and
            (b*d+c) % modulus in R):
            return (a, b, d)
    return None


def complete_table(modulus: int = 32) -> dict[int, dict[int, tuple[int,int,int] | None]]:
    """Every order residue and offset residue, with reproducible witnesses."""
    if modulus < 2:
        raise ValueError("modulus >= 2 required")
    return {
        k % modulus: {
            c: first_local_witness(k, c, modulus) for c in range(modulus)
        } for k in range(modulus, 2 * modulus)
    }


def exclusions(modulus: int = 32) -> dict[int, tuple[int, ...]]:
    return {
        k: tuple(c for c, witness in row.items() if witness is None)
        for k, row in complete_table(modulus).items()
    }


def table_sha256(modulus: int = 32) -> str:
    """Canonical JSON commitment to every local witness and exclusion."""
    table = complete_table(modulus)
    raw = json.dumps(table, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--modulus", type=int, default=32)
    parser.add_argument("--k", type=int)
    parser.add_argument("--offset", type=int)
    args = parser.parse_args()
    if (args.k is None) != (args.offset is None):
        parser.error("--k and --offset must both be specified")
    if args.k is None:
        result = {
            "scheme": "FIGURATE-WP08-MOD32-TABLE/1",
            "modulus": args.modulus,
            "exclusions": exclusions(args.modulus),
            "witness_table_sha256": table_sha256(args.modulus),
        }
    else:
        witness = first_local_witness(args.k, args.offset, args.modulus)
        result = {
            "scheme": "FIGURATE-WP08-MOD32-CELL/1",
            "order": args.k, "offset": args.offset,
            "modulus": args.modulus,
            "polygonal_residues": sorted(polygonal_image(args.k, args.modulus)),
            "first_local_witness": witness,
            "global_obstruction": witness is None,
        }
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
