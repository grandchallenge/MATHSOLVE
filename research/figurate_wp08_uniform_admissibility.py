"""FIGURATE WP08: classification of orders uniformly immune to 2-adic triple obstructions.

For every integer offset c, a FIXED distinct positive integer triple passes
all 2-power Type B polygonal-output congruences if and only if
    4 does not divide k OR k == 4 modulo 16.
This concerns local solvability over Z_2, NOT actual integer Type B triples.
For the excluded order classes c=2 has a certified local obstruction.

The new constructive case k=4 mod16 uses A=k/2-1 == 1 mod8,
and C=(A*c+q*q)/A in Z_2. Since A is a Z_2-unit square,
formal b*=t*t-C, d*=(t+1)**2-C give three 2-adic square outputs.
Finite-precision positive integer approximations preserve nonzero squares.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_wp08_2adic import lift_polygonal_index
from research.figurate_wp08_square_normal_form import (
    normal_form, polygonal_local_possible,
)


def order_is_uniformly_admissible(k: int) -> bool:
    if k < 3:
        raise ValueError("polygonal order must be at least 3")
    return k % 4 != 0 or k % 16 == 4


def v2_nonzero(z: int) -> int:
    if z == 0:
        raise ValueError("2-adic valuation undefined at zero")
    z = abs(z)
    return (z & -z).bit_length() - 1


def constructive_witness(k: int, offset: int) -> dict:
    """Fixed ordinary positive entries satisfying ALL 2-adic local tests.

    For 4∤k polygonal output residues are universally represented.
    For k=4 mod16, select t in {2,3} so 2-adic square roots of
    b+C, d+C, bd+C are nonzero. Choose precision N>2v2(root).
    """
    if not order_is_uniformly_admissible(k):
        raise ValueError("this order is not admissible for every offset")
    if k % 4 != 0:
        return {"order": k, "offset": offset, "entries": (1, 2, 3),
                "method": "surjective-polygonal-image",
                "precision": None, "seed_index": None}
    A, q = normal_form(k)
    assert A % 8 == 1
    D = A * offset + q*q
    t = 2 if D != 6*A else 3
    f = A*(t*t+t) - D
    assert f != 0
    N = max(4, 2*v2_nonzero(t)+3, 2*v2_nonzero(t+1)+3,
            2*v2_nonzero(f)+3)
    M = 1 << N
    C_residue = (D * pow(A, -1, M)) % M
    b = M + ((t*t - C_residue) % M)
    d = 2*M + (((t+1)*(t+1) - C_residue) % M)
    return {"order": k, "offset": offset, "entries": (1, b, d),
            "method": "split-square-normal-form",
            "precision": N, "seed_index": t}


def local_triple_holds(k: int, offset: int, entries: tuple[int,int,int],
                       exponent: int) -> bool:
    if exponent < 1:
        raise ValueError("exponent must be positive")
    if len(entries) != 3 or len(set(entries)) != 3 or min(entries) < 1:
        raise ValueError("distinct positive entries required")
    a, b, d = entries
    outputs = (a*b+offset, a*d+offset, b*d+offset)
    if k % 4 == 0:
        return all(polygonal_local_possible(k, z, exponent)
                   for z in outputs)
    # For non-4-divisible orders, constructive binary lift witnesses
    # polygonal image membership for arbitrary target residue.
    return all(
        (lift_polygonal_index(k, z, exponent) >= 1) for z in outputs
    )


def counterexample_offset(k: int) -> int | None:
    """For all other k, c=2 has no locally compatible triple mod 16.

    The finite modulo-16 obstruction is proved in WP08 tranche 003.
    """
    return None if order_is_uniformly_admissible(k) else 2


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--k", required=True, type=int)
    p.add_argument("--offset", required=True, type=int)
    p.add_argument("--exponent", type=int, default=64)
    args = p.parse_args()
    admissible = order_is_uniformly_admissible(args.k)
    result = {
        "scheme": "FIGURATE-WP08-UNIFORM-2ADIC-ORDER/1",
        "order": args.k, "offset": args.offset,
        "uniform_all_offsets": admissible,
        "counterexample_offset_if_not_uniform": (
            counterexample_offset(args.k)),
    }
    if admissible:
        witness = constructive_witness(args.k, args.offset)
        result.update(witness=witness,
                      passes_checked_exponent=local_triple_holds(
                          args.k, args.offset, tuple(witness["entries"]),
                          args.exponent),
                      checked_exponent=args.exponent)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
