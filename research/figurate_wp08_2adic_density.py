"""FIGURATE WP08: exact 2-adic offset density and coherent local Type B witnesses.

For 4|k, A=k/2-1 odd, q=k/4-1:
  c is in the polygonal image of Z_2 iff D=A*c+q*q is a 2-adic square.
The image count mod 2**n is (2**n + 8)/6 for even n and
(2**n + 10)/6 for odd n (integer, n>=1).

When D is a nonzero 2-adic square, a *fixed* integer triple of distinct
positive entries has all three Type B pair outputs locally polygonal at
every 2-adic precision. This is NOT integer polygonal tuple existence.
"""
from __future__ import annotations

import argparse
import json

from research.figurate_wp08_square_normal_form import (
    normal_form, polygonal_local_possible,
)


def valuation_two(integer: int) -> int:
    if integer == 0:
        raise ValueError("valuation undefined at zero")
    return (abs(integer) & -abs(integer)).bit_length() - 1


def two_adic_square(integer: int) -> bool:
    """True precisely when the mathematical integer is a square in Z_2."""
    if integer == 0:
        return True
    v = valuation_two(integer)
    return v % 2 == 0 and (integer // (1 << v)) % 8 == 1


def offset_immune_to_all_two_power_tests(k: int, offset: int) -> bool:
    """Sufficient local witness condition, not global integer existence."""
    a, q = normal_form(k)
    return two_adic_square(a * offset + q * q)


def fixed_coherent_triple(k: int, offset: int) -> tuple[int, int, int]:
    """One positive distinct integer triple passing every 2^n local test.

    For nonzero D=2^(2j)*u, u=1 mod8, pairs are divisible by
    2^(2j+5). Adding them preserves the square's odd unit mod8.
    D=0 is possible for integer c only at k=4,c=0 (gcd(A,q)=1).
    In that case (1,4,16) gives three *actual* square pair outputs.
    """
    a, q = normal_form(k)
    d_value = a * offset + q * q
    if not two_adic_square(d_value):
        raise ValueError("offset is not polygonal in Z_2")
    if d_value == 0:
        if (k, offset) != (4, 0):
            raise AssertionError("integer D=0 possible only for k=4,c=0")
        return (1, 4, 16)
    j = valuation_two(d_value) // 2
    return (1 << (j + 2), 1 << (j + 3), 1 << (j + 4))


def square_residue_count(exponent: int) -> int:
    """Number of distinct quadratic residues modulo 2**n."""
    if exponent < 1:
        raise ValueError("exponent>=1 required")
    m = 1 << exponent
    return (m + (8 if exponent % 2 == 0 else 10)) // 6


def polygonal_residue_count(k: int, exponent: int) -> int:
    normal_form(k)
    return square_residue_count(exponent)


def triple_passes_precision(k: int, offset: int, triple: tuple[int,int,int],
                            exponent: int) -> bool:
    a, b, d = triple
    return all(polygonal_local_possible(k, x*y + offset, exponent)
               for x,y in ((a,b),(a,d),(b,d)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--k", type=int, required=True)
    p.add_argument("--offset", type=int, required=True)
    p.add_argument("--exponent", type=int, default=12)
    args = p.parse_args()
    a, q = normal_form(args.k)
    D = a * args.offset + q*q
    immune = offset_immune_to_all_two_power_tests(args.k, args.offset)
    triple = fixed_coherent_triple(args.k, args.offset) if immune else None
    print(json.dumps({
        "scheme": "FIGURATE-WP08-COHERENT-2ADIC/1",
        "k": args.k, "offset": args.offset, "A": a, "q": q,
        "transformed_offset": D,
        "offset_is_two_adically_polygonal": immune,
        "fixed_coherent_triple": triple,
        "tested_exponent": args.exponent,
        "triple_local_at_tested_exponent": (
            triple_passes_precision(args.k,args.offset,triple,args.exponent)
            if triple else None),
        "polygonal_image_count": polygonal_residue_count(
            args.k, args.exponent),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
