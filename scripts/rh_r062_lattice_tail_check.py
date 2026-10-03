#!/usr/bin/env python3
"""Sanity replay for RH-R062 untouched-lattice tail bounds.

The theorem is analytic and proved in the work package.  This script checks the
displayed integral bracket and the three scaling regimes numerically for a
bounded deterministic sample.
"""

from math import atan, pi

def term(a: float, j: int) -> float:
    return 1.0 / ((pi * j / a) ** 2 + 0.25)

def integral_tail(a: float, x: float) -> float:
    return (2.0 * a / pi) * atan(a / (2.0 * pi * x))

def partial_with_remainder_bracket(a: float, n: int, m: int = 200000):
    partial = sum(term(a, j) for j in range(n + 1, m + 1))
    lower = partial + integral_tail(a, m + 1)
    upper = partial + integral_tail(a, m)
    return lower, upper

samples = [
    (10.0, 20),
    (20.0, 400),
    (50.0, 2500),
    (80.0, 6400),
]

for a, n in samples:
    theorem_lower = integral_tail(a, n + 1)
    theorem_upper = integral_tail(a, n)
    numeric_lower, numeric_upper = partial_with_remainder_bracket(a, n)
    assert theorem_lower <= numeric_upper + 1e-12
    assert numeric_lower <= theorem_upper + 1e-12
    assert theorem_lower <= theorem_upper
    print(
        f"a={a:g} N={n} "
        f"theorem=[{theorem_lower:.12g},{theorem_upper:.12g}] "
        f"numeric=[{numeric_lower:.12g},{numeric_upper:.12g}]"
    )

# Critical scaling N ~ kappa a^2 with kappa=1.
for a in (20.0, 40.0, 80.0, 160.0):
    n = int(a * a)
    lo = integral_tail(a, n + 1)
    hi = integral_tail(a, n)
    target = 1.0 / (pi * pi)
    assert lo <= target * 1.2
    assert hi >= target * 0.8
    print(
        f"critical a={a:g} bracket_mid={(lo+hi)/2:.12g} "
        f"target={target:.12g}"
    )

# Subquadratic example N ~ a^(3/2): lower bound must grow.
sub = []
for a in (25.0, 100.0, 400.0):
    n = max(1, int(a ** 1.5))
    sub.append(integral_tail(a, n + 1))
assert sub[0] < sub[1] < sub[2]

# Superquadratic example N ~ a^3: upper bound must decay.
sup = []
for a in (10.0, 20.0, 40.0):
    n = max(1, int(a ** 3))
    sup.append(integral_tail(a, n))
assert sup[0] > sup[1] > sup[2]

print("subquadratic_lower_bounds =", sub)
print("superquadratic_upper_bounds =", sup)
print("RH-R062 sanity replay: PASS")
