"""FIGURATE WP08: complete modulo-8 local obstruction of Type B triples.

For every order class and offset modulo 8, enumerate all unordered
three-entry residue multisets, *including repeated residue classes*.
An empty list is a necessary-residue impossibility theorem, not
an experimental bound. A nonempty list does not imply integer existence.

Independent source: research.figurate_census.polygonal for the image.
"""
from __future__ import annotations

import argparse
import itertools
import json
from research.figurate_census import polygonal


def polygonal_image(k: int, modulus: int) -> tuple[int, ...]:
    if k < 3 or modulus < 2:
        raise ValueError("require order>=3 and modulus>=2")
    return tuple(sorted({polygonal(k, t) % modulus
                         for t in range(1, 2 * modulus + 1)}))


def local_triples(k: int, offset: int, modulus: int = 8
                  ) -> tuple[tuple[int, int, int], ...]:
    """Complete locally compatible triples of entry residues, with repeats."""
    image = set(polygonal_image(k, modulus))
    return tuple(values for values in
                 itertools.combinations_with_replacement(range(modulus), 3)
                 if all((values[i] * values[j] + offset) % modulus in image
                        for i, j in ((0, 1), (0, 2), (1, 2))))


def mod8_classification() -> dict[int, dict]:
    """All order classes and offsets: excluded offsets and local witnesses.

    A 3-tuple of residues is not necessarily a positive-integer Type B
    triple; the function is a *necessary local* decision procedure.
    """
    table = {}
    for k in range(8, 16):
        row = {}
        for c in range(8):
            compatible = local_triples(k, c, 8)
            row[c] = {"count": len(compatible),
                      "first": list(compatible[0]) if compatible else None}
        table[k % 8] = row
    return table


def exclusions() -> dict[int, tuple[int, ...]]:
    return {r: tuple(c for c, data in row.items() if data["count"] == 0)
            for r, row in mod8_classification().items()}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--k", type=int)
    p.add_argument("--offset", type=int)
    p.add_argument("--modulus", type=int, default=8)
    args = p.parse_args()
    if (args.k is None) != (args.offset is None):
        p.error("--k and --offset must be specified together")
    if args.k is None:
        output = {"scheme": "FIGURATE-WP08-TRIPLE-MOD8/1",
                  "modulus": 8, "exclusions": exclusions(),
                  "classes": mod8_classification()}
    else:
        triples = local_triples(args.k, args.offset, args.modulus)
        output = {"scheme": "FIGURATE-WP08-TRIPLE-MOD8/1",
                  "k": args.k, "offset": args.offset, "modulus": args.modulus,
                  "polygonal_image": polygonal_image(args.k, args.modulus),
                  "local_triple_count": len(triples),
                  "first_local_triple": triples[0] if triples else None}
    print(json.dumps(output, sort_keys=True))


if __name__ == "__main__":
    main()
