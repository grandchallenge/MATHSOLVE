"""FIGURATE WP08: exact 2-adic square normal form for polygonal orders 4|k.

For k=4h, set A=2h-1 (odd), q=h-1. Then
  A*P_k(t)+q*q = (A*t-q)**2.
Since multiplication by A is invertible modulo 2**n, all t residues
run over all square-root residues, and polygonal membership modulo 2**n
is equivalent to a 2-adic square condition.

An exact congruence condition is necessary, not sufficient, for positive
integer polygonal index membership without the index congruence/sign check.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_census import polygonal


def normal_form(k: int) -> tuple[int, int]:
    if k < 4 or k % 4:
        raise ValueError("normal form requires polygonal order k divisible by 4")
    return k // 2 - 1, k // 4 - 1


def square_mod_power_two(value: int, exponent: int) -> bool:
    """Exact quadratic-residue predicate modulo 2**exponent, all exponent>=1.

    For nonzero x modulo 2**n, write x=2**v*u, u odd.
    A square requires v even. For r=n-v remaining unit bits:
      r=1: automatic; r=2: u=1 mod4; r>=3: u=1 mod8.
    Includes x=0 as a square.
    """
    if exponent < 1:
        raise ValueError("exponent must be positive")
    m = 1 << exponent
    x = value % m
    if x == 0:
        return True
    v = (x & -x).bit_length() - 1
    if v & 1:
        return False
    unit = x >> v
    remaining = exponent - v
    if remaining == 1:
        return True
    if remaining == 2:
        return unit % 4 == 1
    return unit % 8 == 1


def polygonal_local_possible(k: int, output: int, exponent: int) -> bool:
    """Complete local membership condition modulo 2**n for 4|k."""
    a, q = normal_form(k)
    return square_mod_power_two(a * output + q * q, exponent)


def polynomial_local_possible(k: int, output: int, exponent: int) -> bool:
    """Source-independent slow baseline (testing only)."""
    if exponent < 1:
        raise ValueError("exponent must be positive")
    m = 1 << exponent
    return output % m in {polygonal(k, t) % m
                          for t in range(1, 2 * m + 1)}


def triple_local_possible(k: int, offset: int,
                          entries: tuple[int, int, int],
                          exponent: int) -> bool:
    """Necessary and exact local power-of-two condition for Type B triples."""
    if len(entries) != 3:
        raise ValueError("three entries required")
    a, b, d = entries
    return all(polygonal_local_possible(k, x * y + offset, exponent)
               for x, y in ((a, b), (a, d), (b, d)))


def obstruction_witness(k: int, offset: int,
                        exponent: int) -> tuple[int, int, int] | None:
    """Lexicographically first local triple, repetition allowed."""
    m = 1 << exponent
    image = {x for x in range(m)
             if polygonal_local_possible(k, x, exponent)}
    masks = [sum(1 << b for b in range(m)
                 if (a * b + offset) % m in image)
             for a in range(m)]
    for a in range(m):
        for b in range(a, m):
            if masks[a] & (1 << b):
                shared = (masks[a] & masks[b]) >> b
                if shared:
                    low = shared & -shared
                    return a, b, b + low.bit_length() - 1
    return None


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--k", required=True, type=int)
    p.add_argument("--exponent", required=True, type=int)
    p.add_argument("--output", type=int)
    p.add_argument("--offset", type=int)
    args = p.parse_args()
    a, q = normal_form(args.k)
    if (args.output is None) == (args.offset is None):
        p.error("specify exactly one of --output and --offset")
    result = {"scheme": "FIGURATE-WP08-2ADIC-SQUARE-NORMAL-FORM/1",
              "k": args.k, "exponent": args.exponent,
              "A": a, "q": q}
    if args.output is not None:
        result["output"] = args.output
        result["transformed_value"] = a * args.output + q * q
        result["local_possible"] = polygonal_local_possible(
            args.k, args.output, args.exponent)
    else:
        witness = obstruction_witness(args.k, args.offset, args.exponent)
        result.update(offset=args.offset, first_local_triple=witness,
                      global_type_b_triple_obstruction=(witness is None))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
