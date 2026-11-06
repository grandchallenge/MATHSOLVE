"""FIGURATE WP09-018: exact 84-gonal Type B seed from a constrained Pell orbit.

All operations use arbitrary-precision integers. This is a producer constructor;
mathematical certification and literature priority remain separate.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt

K, C = 84, 2
A, B, R_INDEX = 2, 41, 2
PELL_D = A * B
BASE_X, BASE_S = 3_585_208, 395_920
UNIT_U, UNIT_V = 163, 18
SEED_STEPS = 6
R = 2 * (K - 2)
L = K - 4
DELTA = 8 * (K - 2) * C + L * L
NORM = A * (A - B) * DELTA
AMPLIFICATION_MODULUS = 2 * A * R


def polygonal(k: int, n: int) -> int:
    if k < 3 or n < 1:
        raise ValueError("require k>=3 and n>=1")
    return ((k - 2) * n * n - (k - 4) * n) // 2


def pell_multiply(d: int, x: int, y: int, u: int, v: int) -> tuple[int, int]:
    """Return (x+y√d)(u+v√d) in integer coordinates."""
    return u * x + d * v * y, v * x + u * y


def pell_power(d: int, u: int, v: int, exponent: int) -> tuple[int, int]:
    if d < 2 or exponent < 0:
        raise ValueError("require d>=2 and exponent>=0")
    x, y = 1, 0
    bx, by = u, v
    e = exponent
    while e:
        if e & 1:
            x, y = pell_multiply(d, x, y, bx, by)
        bx, by = pell_multiply(d, bx, by, bx, by)
        e >>= 1
    return x, y


def unit_order_mod(d: int, u: int, v: int, modulus: int) -> int:
    """Least positive e with (u+v√d)^e == 1 modulo modulus."""
    if modulus < 2 or u * u - d * v * v != 1:
        raise ValueError("require modulus>=2 and a norm-one unit")
    x, y = 1, 0
    for e in range(1, modulus ** 4 + 1):
        x, y = pell_multiply(d, x, y, u, v)
        x %= modulus
        y %= modulus
        if (x, y) == (1, 0):
            return e
    raise ArithmeticError("finite matrix-group order bound exceeded")


def recover_seed(x: int, s_coordinate: int) -> dict:
    """Recover (a,b,d;r,s,t) from the exact constrained norm coordinates."""
    if x <= 0 or s_coordinate <= 0:
        raise ValueError("positive Pell coordinates required")
    if x * x - PELL_D * s_coordinate * s_coordinate != NORM:
        raise ArithmeticError("generalized Pell norm identity failed")
    if s_coordinate % R != (-L) % R:
        raise ArithmeticError("S is outside the polygonal index lattice")
    if x % (A * R) != (-A * L) % (A * R):
        raise ArithmeticError("X is outside the scaled polygonal index lattice")
    s = (s_coordinate + L) // R
    if x % A:
        raise ArithmeticError("a does not divide X")
    t_numerator = x // A + L
    if t_numerator % R:
        raise ArithmeticError("third polygonal index is not integral")
    t = t_numerator // R
    if min(s, t) < 1:
        raise ArithmeticError("polygonal indices must be positive")
    shifted_ad = polygonal(K, s) - C
    if shifted_ad <= 0 or shifted_ad % A:
        raise ArithmeticError("third entry is not a positive integer")
    d = shifted_ad // A
    if len({A, B, d}) != 3:
        raise ArithmeticError("Type B entries must be pairwise distinct")
    if (A * B + C, A * d + C, B * d + C) != (
        polygonal(K, R_INDEX), polygonal(K, s), polygonal(K, t)
    ):
        raise ArithmeticError("recovered tuple does not satisfy all three equations")
    return {
        "order": K, "offset": C, "entries": (A, B, d),
        "indices": (R_INDEX, s, t),
        "shifted_polygonal_values": (
            polygonal(K, R_INDEX), polygonal(K, s), polygonal(K, t)
        ),
        "pell_coordinates": (x, s_coordinate),
        "norm": NORM,
    }


def construct_seed() -> dict:
    if UNIT_U * UNIT_U - PELL_D * UNIT_V * UNIT_V != 1:
        raise ArithmeticError("unit is not norm one")
    if BASE_X * BASE_X - PELL_D * BASE_S * BASE_S != NORM:
        raise ArithmeticError("base point is not on the required norm conic")
    x, y = BASE_X, BASE_S
    for _ in range(SEED_STEPS):
        x, y = pell_multiply(PELL_D, x, y, UNIT_U, UNIT_V)
    result = recover_seed(x, y)
    result.update({
        "base_pell_coordinates": (BASE_X, BASE_S),
        "unit": (UNIT_U, UNIT_V),
        "seed_unit_steps": SEED_STEPS,
        "delta": DELTA,
    })
    return result


def construct_next_family_member() -> dict:
    seed = construct_seed()
    e = unit_order_mod(PELL_D, UNIT_U, UNIT_V, AMPLIFICATION_MODULUS)
    ue, ve = pell_power(PELL_D, UNIT_U, UNIT_V, e)
    if (ue % AMPLIFICATION_MODULUS, ve % AMPLIFICATION_MODULUS) != (1, 0):
        raise ArithmeticError("computed unit power is not identity modulo lattice modulus")
    x0, y0 = seed["pell_coordinates"]
    x1, y1 = pell_multiply(PELL_D, x0, y0, ue, ve)
    next_seed = recover_seed(x1, y1)
    if next_seed["entries"][2] <= seed["entries"][2]:
        raise ArithmeticError("Pell amplification did not increase the third entry")
    next_seed.update({
        "amplification_unit_exponent": e,
        "amplification_modulus": AMPLIFICATION_MODULUS,
        "amplification_unit_power": (ue, ve),
    })
    return next_seed


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--next-family-member", action="store_true")
    args = parser.parse_args()
    result = construct_next_family_member() if args.next_family_member else construct_seed()
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
