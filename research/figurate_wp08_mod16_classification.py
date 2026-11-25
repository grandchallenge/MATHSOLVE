"""FIGURATE WP08: complete local Type B triple obstruction table modulo 16.

This is an exact finite classification of a *necessary* modular condition.
An empty cell proves global impossibility at that order/offset class.
A nonempty cell never proves existence of a positive integer triple.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_wp08_global_mod8 import (
    local_triples,
    polygonal_image,
)


def full_mod16_exclusions() -> dict[int, tuple[int, ...]]:
    """All 16 order-residue classes, each covering infinitely many k>=3."""
    return {
        k % 16: tuple(c for c in range(16)
                      if not local_triples(k, c, 16))
        for k in range(16, 32)
    }


def local_certificate(k: int, offset: int) -> dict:
    triples = local_triples(k, offset, 16)
    return {
        "scheme": "FIGURATE-WP08-MOD16-LOCAL-CERT/1",
        "k": k,
        "offset": offset,
        "order_residue": k % 16,
        "offset_residue": offset % 16,
        "polygonal_image": list(polygonal_image(k, 16)),
        "local_triples": len(triples),
        "first_local_triple": list(triples[0]) if triples else None,
        "global_exclusion_by_mod16": not bool(triples),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--k", type=int)
    p.add_argument("--offset", type=int)
    args = p.parse_args()
    if (args.k is None) != (args.offset is None):
        p.error("specify both --k and --offset, or neither")
    data = ({"scheme": "FIGURATE-WP08-MOD16-TABLE/1",
             "modulus": 16, "exclusions": full_mod16_exclusions()}
            if args.k is None else local_certificate(args.k, args.offset))
    print(json.dumps(data, sort_keys=True))


if __name__ == "__main__":
    main()
