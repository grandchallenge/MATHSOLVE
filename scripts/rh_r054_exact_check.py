#!/usr/bin/env python3
"""Exact arithmetic checker for RH-R054.

No floating-point arithmetic is used.
"""

from fractions import Fraction as F


def atanh_lower_from_u(u: F, terms: int = 7) -> F:
    z = u * u
    s = z / (F(2) - z)
    return sum(F(2, 2 * j + 1) * s ** (2 * j + 1) for j in range(terms))


midpoints = [F(2 * i + 1, 24) for i in range(12)]
upper = [
    F(7481, 5000),
    F(7327, 5000),
    F(879, 625),
    F(2647, 2000),
    F(6111, 5000),
    F(11081, 10000),
    F(9863, 10000),
    F(4303, 5000),
    F(917, 1250),
    F(6053, 10000),
    F(4723, 10000),
    F(637, 2000),
]

for u, bound in zip(midpoints, upper):
    denominator_lower = F(2, 3) + atanh_lower_from_u(u)
    assert F(1) / denominator_lower < bound

midpoint_integral_upper = sum(upper, F(0)) / 12
assert midpoint_integral_upper == F(7499, 7500)
assert midpoint_integral_upper < 1

# Protected q' envelope at the new endpoint t = 9/25.
t = F(9, 25)
b_star = F(3, 5) * (
    F(1, 24) + t / F(9) - t * t / F(30) + t**4 / F(2835)
)
sinh_upper = F(900, 4919)
qprime_upper = b_star + sinh_upper

assert b_star == F(25381319, 546875000)
assert qprime_upper == F(617038208161, 2690078125000)
assert qprime_upper < F(23, 100)

# Revalidate the protected h'' <= 0 sign criterion on t <= 9/25.
sign_polynomial = F(12) - 8 * t * t - t**4
assert sign_polynomial == F(4275939, 390625)
assert sign_polynomial > 0

# Exact quartic trial formulas.
c = F(13, 20)
d = -F(2, 25)

norm = F(2, 315) * (
    63 * c * c
    - 90 * c * d
    - 210 * c
    + 35 * d * d
    + 126 * d
    + 315
)
mass = F(2, 15) * (15 - 5 * c + 3 * d)
h_num = F(2, 99225) * (
    43659 * c * c
    - 70200 * c * d
    - 88200 * c
    + 30625 * d * d
    + 60858 * d
    + 99225
)
j_num = F(8, 10395) * (
    495 * c * c
    - 616 * c * d
    - 2772 * c
    + 189 * d * d
    + 1782 * d
    + 3465
)

limiting_rational = h_num / norm
distance_ratio = j_num / norm
linear = F(7, 4) * mass * mass / norm
residual = F(23, 100) * distance_ratio

assert norm == F(399883, 315000)
assert mass == F(1151, 750)
assert limiting_rational == F(23727475, 25192629)
assert distance_ratio == F(70520764, 65980695)
assert linear == F(64915249, 19994150)
assert residual == F(405494393, 1649517375)

# Endpoint certificates at a = 9/50 with log(2) > 693/1000.
a = F(9, 50)
log2_lower = F(693, 1000)
odd_bonus = F(1, 6)
odd_remainder = F(18653, 100000)
even_remainder = F(23, 50)

parity_gap = (
    2 * log2_lower
    + odd_bonus
    - limiting_rational
    - linear * a
    - (residual + odd_remainder) * a * a
)
even_internal_gap = (
    log2_lower
    + 1
    - limiting_rational
    - linear * a
    - (residual + even_remainder) * a * a
)

assert parity_gap == F(859636202320933, 69279729750000000)
assert even_internal_gap == F(12460054441577, 86599662187500)
assert parity_gap > 0
assert even_internal_gap > 0

# No-prime condition.
assert F(9, 25) < F(693, 1000)

print("midpoint_integral_upper =", midpoint_integral_upper)
print("qprime_endpoint_upper =", qprime_upper)
print("parity_gap_lower =", parity_gap)
print("even_internal_gap_lower =", even_internal_gap)
print("no_prime_check =", F(9, 25), "<", F(693, 1000))
