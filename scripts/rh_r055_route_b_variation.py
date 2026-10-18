#!/usr/bin/env python3
from fractions import Fraction as F

a0 = F(89, 500)
A = F(9, 50)
L = F(23, 100)

B = F(3, 5) * (F(1, 24) + F(9, 25) / 9 - F(9, 25) ** 2 / 30 + F(9, 25) ** 4 / 2835)
sinh_9_50 = F(900, 4919)
qprime = B + sinh_9_50
assert qprime == F(617038208161, 2690078125000)
assert qprime < L

C_K = F(7, 2) + 4 * L * A
assert C_K == F(2291, 625)

# Pole-vector derivative bounds.
pointwise = F(19, 16) * F(1800, 19919) + F(17, 80) * F(20000, 19919)
assert pointwise == F(12775, 39838)
L_s = F(99, 70) * pointwise
assert L_s == F(36135, 79676)
assert L_s < F(227, 500)

U = A ** 3 / 6 + A ** 5 / 119
assert U == F(36205299, 37187500000)
assert U < F(1, 1024)

C_P = 4 * F(1, 32) * F(227, 500)
assert C_P == F(227, 4000)

C_mu = F(1, 1) / a0 + C_K
C_beta = C_mu + C_P
C_d = 2 * C_K + C_P
assert C_mu == F(516399, 55625)
assert C_beta == F(16625783, 1780000)
assert C_d == F(147759, 20000)

a1 = F(3561, 20000)
h = a1 - a0
assert h == F(1, 20000)

d0 = F(55428698889, 23675000000000)
d1 = d0 - C_d * h
assert d1 == F(93366426153, 47350000000000)
assert d1 > 0

Delta1 = F(1, 2) - U / d1
assert Delta1 == F(3562843673, 569774600626)
assert Delta1 > 0

gap1 = 2 * d1 * Delta1
assert gap1 == d1 - 2 * U
assert gap1 == F(138950903247, 5634650000000000)
assert gap1 > 0

even0 = F(1783634369, 11837500000)
even1 = even0 - 2 * C_K * h
assert even1 == F(355859043, 2367500000)
assert even1 > 0

print("qprime_bound =", qprime)
print("C_K =", C_K)
print("C_mu =", C_mu)
print("C_beta =", C_beta)
print("C_d =", C_d)
print("d1 =", d1)
print("Delta1 =", Delta1)
print("parity_gap1 =", gap1)
print("even_internal_gap1 =", even1)
print("RH-R055 exact arithmetic: PASS")
