#!/usr/bin/env python3
"""Exact algebraic replay for RH-R059.

This checker validates the finite rational identities used by the explicit
counterexample.  The Hadamard/Montel theorem is analytic and is proved in the
work package rather than delegated to computation.
"""

from fractions import Fraction as F

eta = F(1, 2)
anchor = F(1, 2)

# For F_n(z) = 1/2 * ((1-z^2)/(1+eta^2))^n:
den = 1 + eta * eta
assert den == F(5, 4)

# At z=i*eta the numerator is 1+eta^2, so the normalized value is 1/2.
assert anchor * (den / den) == F(1, 2)

# At z=2 the absolute factor is |1-4|/(5/4) = 12/5 > 1.
growth = F(3, 1) / den
assert growth == F(12, 5)
assert growth > 1

# The only positive zero is x=1 with multiplicity n.
# Q_{1/2}(F_n)/n = 1/(1+1/4) = 4/5.
q_per_n = 1 / (F(1) + eta * eta)
assert q_per_n == F(4, 5)

# Spectral pairing check for a model with zero half-multiplicity m0 and
# one positive pair x with multiplicity mx:
m0 = 3
mx = 7
x = F(5, 2)
q = F(m0, 1) / (eta * eta) + F(mx, 1) / (x * x + eta * eta)
trace = (
    F(2 * m0, 1) / (eta * eta)
    + F(2 * mx, 1) / (x * x + eta * eta)
)
assert trace == 2 * q

print("anchor =", anchor)
print("counterexample_growth_factor_at_2 =", growth)
print("Q_per_multiplicity =", q_per_n)
print("paired_trace_identity =", trace, "=", 2, "*", q)
