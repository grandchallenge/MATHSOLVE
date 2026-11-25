"""FIGURATE WP09-003: exact modulo-25 Type B triple obstructions.

Finite congruence certificates only; no novelty or certification claim.
"""
from __future__ import annotations
import argparse


def polygonal(k: int, t: int) -> int:
    if k < 3 or t < 1:
        raise ValueError("k>=3 and t>=1 required")
    return t + (k - 2) * t * (t - 1) // 2


def image(k: int, modulus: int) -> frozenset[int]:
    if modulus < 2:
        raise ValueError("modulus>=2 required")
    # P_k(t+modulus)-P_k(t) is divisible by modulus when
    # modulus is odd. Here only odd moduli are supported.
    if modulus % 2 == 0:
        raise ValueError("odd modulus required")
    return frozenset(polygonal(k, t) % modulus for t in range(1, modulus + 1))


def allowed_products(k: int, c: int, modulus: int) -> frozenset[int]:
    return frozenset((v - c) % modulus for v in image(k, modulus))


def witness(k: int, c: int, modulus: int) -> tuple[int, int, int] | None:
    """All entry residues, allowing repeated classes (distinct integers may share one)."""
    permitted = allowed_products(k, c, modulus)
    for a in range(modulus):
        for b in range(modulus):
            if a * b % modulus not in permitted:
                continue
            for d in range(modulus):
                if a * d % modulus in permitted and b * d % modulus in permitted:
                    return (a, b, d)
    return None


def obstructed_mod25_formula(k: int, c: int) -> bool:
    r = k % 5
    return (c % 5 == 3 and
            ((r == 1 and c % 25 != (k - 3) % 25) or
             (r == 3 and c % 25 != k % 25)))


def audit() -> dict[str, int]:
    total = 0
    excluded = 0
    for k in range(3, 28):
        for c in range(25):
            got = witness(k, c, 25) is None
            expected = obstructed_mod25_formula(k, c)
            if got != expected:
                raise AssertionError((k, c, got, expected))
            # There is no global triple obstruction modulo five.
            if witness(k, c, 5) is None:
                raise AssertionError(("unexpected mod5 obstruction", k, c))
            excluded += got
            total += 1
    return {"cells": total, "excluded": excluded, "admitted": total - excluded}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=int)
    parser.add_argument("--offset", type=int)
    args = parser.parse_args()
    if (args.k is None) != (args.offset is None):
        parser.error("supply both --k and --offset")
    if args.k is not None:
        print({"k": args.k, "offset": args.offset,
               "mod5_witness": witness(args.k, args.offset, 5),
               "mod25_witness": witness(args.k, args.offset, 25),
               "mod25_excluded": obstructed_mod25_formula(args.k, args.offset)})
    else:
        print(audit())


if __name__ == "__main__":
    main()
