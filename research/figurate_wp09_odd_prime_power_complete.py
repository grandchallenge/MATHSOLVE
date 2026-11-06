"""FIGURATE WP09-006: complete odd-prime-power Type B local criterion.

For each (k,c,p,n), either a rigorous obstruction or a common entry-residue
witness whose three pairwise outputs are k-gonal modulo p**n.
Local witnesses are NOT exact positive-integer Type B solutions.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt


def prime(p: int) -> bool:
    return p >= 2 and all(p % d for d in range(2, isqrt(p) + 1))


def polygonal(k: int, t: int) -> int:
    return t + (k - 2) * t * (t - 1) // 2


def valuation_mod(z: int, p: int, n: int) -> int:
    z %= p ** n
    v = 0
    while v < n and z % p == 0:
        z //= p
        v += 1
    return v


def nonsquare(a: int, p: int) -> bool:
    return pow(a % p, (p - 1) // 2, p) == p - 1


def obstructed(k: int, c: int, p: int, n: int) -> bool:
    if k < 3 or n < 1 or p < 3 or not prime(p):
        raise ValueError("k>=3, odd prime p and n>=1 required")
    if (k - 2) % p == 0:
        return False
    A = (k - 2) * pow(2, -1, p) % p
    if not nonsquare(A, p):
        return False
    delta = 8 * (k - 2) * c + (k - 4) ** 2
    v = valuation_mod(delta, p, n)
    return v < n and v % 2 == 1


def _lift_conic(A: int, u: int, p: int, m: int) -> tuple[int, int]:
    """Construct X²+u=A Z² modulo p^m, requiring a nonsingular F_p point."""
    q = p ** m
    A %= q
    u %= q
    point = next(((x, z) for x in range(p) for z in range(p)
                  if (x*x + u - A*z*z) % p == 0
                  and (x % p != 0 or (A*z) % p != 0)), None)
    if point is None:
        raise ArithmeticError("missing nonsingular field-conic point")
    x, z = point
    for j in range(1, m):
        F = x*x + u - A*z*z
        assert F % (p ** j) == 0
        if x % p:
            derivative = 2 * x % p
            digit = (-(F // (p ** j)) * pow(derivative, -1, p)) % p
            x += digit * p ** j
        else:
            derivative = -2 * A * z % p
            digit = (-(F // (p ** j)) * pow(derivative, -1, p)) % p
            z += digit * p ** j
    if (x*x + u - A*z*z) % q:
        raise ArithmeticError("conic lift failed")
    return x % q, z % q


def common_residue_witness(k: int, c: int, p: int, n: int) -> dict | None:
    """Construct common entry residue x and output-index residue t modulo p^n."""
    if obstructed(k, c, p, n):
        return None
    q = p ** n
    if (k - 2) % p == 0:
        # P_k(t)=t mod p; derivative is 1 mod p. Lift inverse uniquely.
        t = c % p
        for j in range(1, n):
            difference = (c - polygonal(k, t)) // (p ** j)
            t += (difference % p) * p ** j
        x = 0
    else:
        A = (k - 2) * pow(2, -1, q) % q
        h = (k - 4) * pow(2*(k - 2), -1, q) % q
        delta = 8 * (k - 2) * c + (k - 4) ** 2
        v = delta * pow(8*(k - 2), -1, q) % q
        if v == 0:
            x, z = 0, 0
        else:
            r = valuation_mod(v, p, n)
            if nonsquare(A % p, p) and r > 0:
                # r is necessarily even by unobstructedness.
                assert r % 2 == 0
                scale = p ** (r // 2)
                m = n - r
                x0, z0 = _lift_conic(A, v // (p ** r), p, m)
                x, z = scale * x0, scale * z0
            else:
                x, z = _lift_conic(A, v, p, n)
        t = (z + h) % q
    if (x*x + c - polygonal(k, t)) % q:
        raise ArithmeticError("constructed common residue does not verify")
    # Positive distinct entries a,b,d are x+q, x+2q, x+3q.
    return {"modulus": q, "entry_residue": x % q, "index_residue": t % q,
            "distinct_positive_entries": [x % q + i*q for i in (1, 2, 3)]}


def audit(p: int, n: int) -> dict[str, int]:
    q = p**n
    excluded = 0
    for k in range(3, q+3):
        for c in range(q):
            blocked = obstructed(k, c, p, n)
            w = common_residue_witness(k, c, p, n)
            if (w is None) != blocked:
                raise AssertionError((k, c, p, n))
            excluded += blocked
    return {"prime": p, "exponent": n, "cells": q*q, "excluded": excluded,
            "compatible": q*q-excluded}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--prime", type=int, default=3)
    parser.add_argument("--exponent", type=int, default=2)
    parser.add_argument("--order", type=int)
    parser.add_argument("--offset", type=int)
    parser.add_argument("--audit", action="store_true")
    a = parser.parse_args()
    if a.audit:
        result = audit(a.prime, a.exponent)
    else:
        if a.order is None or a.offset is None:
            parser.error("provide both --order and --offset, or --audit")
        result = {"obstructed": obstructed(a.order, a.offset, a.prime, a.exponent),
                  "witness": common_residue_witness(a.order, a.offset,
                                                     a.prime, a.exponent)}
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
