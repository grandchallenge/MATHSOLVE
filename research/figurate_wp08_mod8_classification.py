"""FIGURATE WP08: complete modulus-eight anchored-pair local obstruction classification.

The complete pair witness residue family is b=P_k(t)-c (mod m).
A local obstruction is an empty third-entry compatibility intersection.
All calculations are exact and retain repeated residue classes.
No novelty or global triple classification is claimed.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_wp07_obstructions import (
    pair_extension_residues,
    polygonal_residues,
)


def anchored_obstruction_classes(k: int, modulus: int) -> dict[int, tuple[int, ...]]:
    """For each offset residue c, all obstructed residues b for (1,b).

    Includes only b residues occurring for a *compatible* anchor pair:
    1*b+c=P_k(t) modulo modulus for some t. Any such b is realized
    by infinitely many actual positive integer pairs {1,P_k(t)-c}.
    """
    if k < 3 or modulus < 2:
        raise ValueError("k>=3, modulus>=2 required")
    image = set(polygonal_residues(k, modulus))
    return {
        c: tuple(b for b in range(modulus)
                 if (b + c) % modulus in image
                 and not pair_extension_residues(k, c, 1, b, modulus))
        for c in range(modulus)
    }


def nonempty_obstruction_classes(k: int, modulus: int) -> dict[int, tuple[int, ...]]:
    return {c: residues for c, residues in
            anchored_obstruction_classes(k, modulus).items() if residues}


def modulus_eight_classifier() -> dict[int, dict[int, tuple[int, ...]]]:
    """Exact finite classification of anchored Type B local obstructions mod 8.

    P_k(t)=t+(k-2)*binom(t,2) makes k modulo 8 sufficient.
    Representatives k=8,...,15 realize residues 0,...,7.
    """
    return {k % 8: nonempty_obstruction_classes(k, 8)
            for k in range(8, 16)}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--modulus", type=int, default=8)
    p.add_argument("--k", type=int)
    a = p.parse_args()
    result = (modulus_eight_classifier() if a.k is None
              else nonempty_obstruction_classes(a.k, a.modulus))
    print(json.dumps({
        "scheme": "FIGURATE-WP08-ANCHOR-CLASSIFICATION/1",
        "modulus": a.modulus, "k": a.k, "classes": result
    }, sort_keys=True))


if __name__ == "__main__":
    main()
