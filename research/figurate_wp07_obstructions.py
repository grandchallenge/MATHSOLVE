"""FIGURATE WP07: exact residue certificates for pair/extension obstructions.

Certificates supply necessary local conditions only. An empty residue set
proves impossibility over all positive integers; nonempty sets do not prove
existence. These elementary observations are not claimed novel/certified.
"""
from __future__ import annotations

import argparse
import json
from research.figurate_census import polygonal, polygonal_index


def polygonal_residues(k: int, modulus: int) -> tuple[int, ...]:
    """Complete image modulo m: t -> t+2m preserves P_k(t) mod m."""
    if k < 3 or modulus < 2:
        raise ValueError("require k>=3, modulus>=2")
    return tuple(sorted({polygonal(k, t) % modulus
                         for t in range(1, 2 * modulus + 1)}))


def pair_extension_residues(k: int, offset: int, a: int, b: int,
                            modulus: int, kind: str = "B") -> tuple[int, ...]:
    """All possible third-entry residue classes, including 0.

    For C impose polygonal membership on the third entry as well.
    Does not assume a,b themselves form a valid pair: call separately.
    """
    if kind not in ("B", "C") or a < 1 or b < 1 or a == b:
        raise ValueError("require B/C and distinct positive fixed entries")
    image = set(polygonal_residues(k, modulus))
    return tuple(d for d in range(modulus)
                 if ((a * d + offset) % modulus in image
                     and (b * d + offset) % modulus in image
                     and (kind == "B" or d in image)))


def type_c_pair_residue_witnesses(k: int, offset: int,
                                  modulus: int) -> tuple[tuple[int, int], ...]:
    """ALL residue-compatible ordered pairs, allowing repeated classes.

    Repeated residues must not be mistaken for identical entries.
    A genuinely valid Type C pair must project into this set.
    """
    image = polygonal_residues(k, modulus)
    return tuple((a, b) for a in image for b in image
                 if (a * b + offset) % modulus in image)


def certificate(k: int, offset: int, modulus: int,
                a: int | None = None, b: int | None = None,
                kind: str = "B") -> dict:
    image = polygonal_residues(k, modulus)
    result = {"scheme": "FIGURATE-WP07-LOCAL-CERT/1", "k": k,
              "offset": offset, "modulus": modulus,
              "polygonal_residues": list(image)}
    if a is None and b is None:
        result.update({"kind": "C", "pair_residue_witnesses":
                       [list(p) for p in type_c_pair_residue_witnesses(
                           k, offset, modulus)]})
        return result
    if a is None or b is None:
        raise ValueError("both fixed entries required")
    if kind not in ("B", "C"):
        raise ValueError("only B/C supported")
    result.update({"kind": kind, "pair": [a, b],
                   "pair_exact_witness": polygonal_index(
                       k, a * b + offset),
                   "extension_residues": list(pair_extension_residues(
                       k, offset, a, b, modulus, kind))})
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int, required=True)
    parser.add_argument("--offset", type=int, required=True)
    parser.add_argument("--modulus", type=int, required=True)
    parser.add_argument("--a", type=int)
    parser.add_argument("--b", type=int)
    parser.add_argument("--kind", choices=("B", "C"), default="B")
    args = parser.parse_args()
    print(json.dumps(certificate(args.k, args.offset, args.modulus,
                                 args.a, args.b, args.kind), sort_keys=True))


if __name__ == "__main__":
    main()
