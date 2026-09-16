#!/usr/bin/env python3
"""Exact-arithmetic verifier for RH-R030-L001.

This checker proves only the elementary arithmetic/envelope prerequisites for the
imported one-stroke reduction at L = 161/200.  It does not evaluate the Weil
matrix and does not prove RH-R030 or RH.

The sole imported mathematical fact not checked here is the classical bound
pi < 22/7.  Everything else below is rational arithmetic, including the
exponential-series enclosures used to turn logarithmic comparisons into exact
finite inequalities.
"""

from fractions import Fraction
from math import factorial


def exp_lower(x: Fraction, n: int) -> Fraction:
    """Lower bound e^x > sum_{k=0}^n x^k/k! for x > 0."""
    assert x > 0 and n >= 0
    return sum((x**k) / factorial(k) for k in range(n + 1))


def exp_upper(x: Fraction, n: int) -> Fraction:
    """Upper bound from the positive exponential series and a geometric tail."""
    assert x > 0 and n >= 0
    partial = exp_lower(x, n)
    first_tail = (x ** (n + 1)) / factorial(n + 1)
    ratio_bound = x / (n + 2)
    assert 0 <= ratio_bound < 1
    return partial + first_tail / (1 - ratio_bound)


def main() -> None:
    two_L = Fraction(161, 100)

    # 5 < exp(1.61) < 6. Hence integers n with log n < 1.61 are exactly n <= 5.
    # Among n=2,3,4,5 all and only these have nonzero von Mangoldt weight.
    assert exp_lower(two_L, 7) > 5
    assert exp_upper(two_L, 7) < 6
    active_prime_powers = (2, 3, 4, 5)

    # Safe logarithm upper bounds, proved by lower exponential-series bounds.
    # e^0.694 > 2, e^1.099 > 3, e^1.61 > 5.
    assert exp_lower(Fraction(694, 1000), 4) > 2
    assert exp_lower(Fraction(1099, 1000), 6) > 3
    assert exp_lower(Fraction(161, 100), 7) > 5

    # Safe radical coefficient bounds, proved by exact squaring.
    # sqrt(2) < 1.415, 2/sqrt(3) < 1.155, 2/sqrt(5) < 0.895.
    assert Fraction(1415, 1000) ** 2 > 2
    assert 3 * Fraction(1155, 1000) ** 2 > 4
    assert 5 * Fraction(895, 1000) ** 2 > 4

    # A_L = sqrt(2)log2 + (2/sqrt(3))log3 + log2 + (2/sqrt(5))log5.
    # Apply the safe coefficient/log bounds above.
    A_upper = (
        Fraction(1415, 1000) * Fraction(694, 1000)
        + Fraction(1155, 1000) * Fraction(1099, 1000)
        + Fraction(694, 1000)
        + Fraction(895, 1000) * Fraction(161, 100)
    )
    assert A_upper == Fraction(877261, 200000)  # 4.386305

    # Imported classical bound pi < 22/7 gives
    #   600/(2*pi) > 600/(44/7) = 1050/11.
    # Exact exponential-series enclosure proves e^4.55 < 1050/11, hence
    # log(600/(2*pi)) > 4.55.
    assert exp_upper(Fraction(455, 100), 7) < Fraction(1050, 11)

    # Therefore beta* = log(600/(2*pi)) - 1/600 - A_L has the exact lower bound:
    beta_lower = Fraction(455, 100) - Fraction(1, 600) - A_upper
    assert beta_lower == Fraction(97217, 600000)
    assert beta_lower > 0

    print("RH-R030-L001: PASS")
    print(f"active_prime_powers={active_prime_powers}")
    print(f"A_L < {A_upper} = {float(A_upper):.6f}")
    print(f"beta* > {beta_lower} = {float(beta_lower):.12f}")
    print("boundary=one-stroke prerequisite only; RH-R030 and RH remain unproved")


if __name__ == "__main__":
    main()
