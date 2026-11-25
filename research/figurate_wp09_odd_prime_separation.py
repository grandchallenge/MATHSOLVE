"""FIGURATE WP09: exact odd-prime separation of all-power binary compatibility.

For order k=20, triple (1,242,375), and c=2+640*m for any
integer m, all three transformed outputs 9*(xy+c)+16 are squares
in Z_2, but the first output is 4 mod 5 and cannot be 20-gonal
modulo 5. This disproves the inference from simultaneous 2-adic
compatibility of a fixed triple to exact integer Type B membership.

It does not prove that NO OTHER triple works at those parameters.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_census import polygonal
from research.figurate_wp08_2adic_density import two_adic_square
from research.figurate_wp08_square_normal_form import (
    polygonal_local_possible,
)

ORDER = 20
ENTRIES = (1, 242, 375)
OFFSET_BASE = 2
OFFSET_PERIOD = 640


def offset_at(parameter: int) -> int:
    return OFFSET_BASE + OFFSET_PERIOD * parameter


def pair_outputs(offset: int) -> tuple[int, int, int]:
    a, b, d = ENTRIES
    return (a * b + offset, a * d + offset, b * d + offset)


def transformed_outputs(offset: int) -> tuple[int, int, int]:
    return tuple(9 * z + 16 for z in pair_outputs(offset))


def full_binary_certificate(parameter: int) -> dict:
    """All-power proof by direct signed 2-adic-square valuation criterion."""
    c = offset_at(parameter)
    values = transformed_outputs(c)
    return {
        "k": ORDER, "entries": ENTRIES, "parameter": parameter,
        "offset": c, "outputs": pair_outputs(c),
        "transformed_outputs": values,
        "square_in_Z2": tuple(two_adic_square(z) for z in values),
        "all_powers_binary_compatible": all(two_adic_square(z) for z in values),
    }


def independent_polygonal_residues(k: int, modulus: int) -> frozenset[int]:
    return frozenset(polygonal(k, t) % modulus
                     for t in range(1, 2 * modulus + 1))


def odd_prime_obstruction(parameter: int, prime: int = 5) -> dict:
    c = offset_at(parameter)
    outputs = pair_outputs(c)
    image = independent_polygonal_residues(ORDER, prime)
    return {
        "modulus": prime, "image": tuple(sorted(image)),
        "output_residues": tuple(z % prime for z in outputs),
        "valid_edges": tuple(z % prime in image for z in outputs),
        "first_edge_excluded": outputs[0] % prime not in image,
    }


def complete_certificate(parameter: int) -> dict:
    binary = full_binary_certificate(parameter)
    odd = odd_prime_obstruction(parameter)
    return {
        "scheme": "FIGURATE-WP09-ODD-PRIME-SEPARATION/1",
        "binary": binary, "odd_prime": odd,
        "local_to_global_failure_for_this_fixed_triple": (
            binary["all_powers_binary_compatible"]
            and odd["first_edge_excluded"]),
        "global_nonexistence_for_all_triples_claimed": False,
    }


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--parameter", type=int, default=0)
    args = p.parse_args()
    print(json.dumps(complete_certificate(args.parameter), sort_keys=True))


if __name__ == "__main__":
    main()
