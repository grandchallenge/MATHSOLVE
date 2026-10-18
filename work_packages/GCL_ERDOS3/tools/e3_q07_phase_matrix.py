#!/usr/bin/env python3
"""Exact phase-matrix certificate for E3-Q07.

The certificate uses the ten-family E3-L01 core and one Q04 triple branch per
family.  It proves the resulting ten one-scale Fourier phase equations are
surjective in the twelve physical-fibre mode phases: an explicit 10x10 minor
has determinant -3.

Pure Python. No floating point and no external solver.
"""

from fractions import Fraction

CORE = {
    1:  (0, 0, (0, 0, 1, 1)),
    2:  (0, 0, (0, 1, 1, 1)),
    3:  (1, 0, (0, 0, 0, 1)),
    4:  (1, 0, (0, 0, 1, 1)),
    6:  (2, 0, (0, 0, 0, 1)),
    7:  (2, 0, (0, 0, 1, 1)),
    9:  (0, 0, (0, 1, 1, 2)),
    10: (1, 0, (0, 1, 1, 2)),
    15: (0, 0, (0, 1, 2, 3)),
    16: (0, 1, (0, 0, 0, 0)),
}

TRIPLE = {
    1:  (0, 1, 2),
    2:  (0, 1, 2),
    3:  (0, 1, 2),
    4:  (0, 1, 2),
    6:  (0, 1, 2),
    7:  (0, 2, 3),
    9:  (0, 1, 3),
    10: (0, 1, 3),
    15: (0, 1, 3),
    16: (0, 2, 3),
}

VARS = [(j, k) for j in range(4) for k in (1, 2, 3)]
VID = {v: i for i, v in enumerate(VARS)}
FAMILY_ORDER = list(CORE)

def block_word(fam):
    i, q, c = fam
    return tuple(i + t*q + c[t] for t in range(4))

def phase_row(fam, triple):
    """Coefficient row for physical phases theta[j,k].

    For positions t1<t2<t3 the triple Fourier frequencies are
      (t2-t3)r, (t3-t1)r, (t1-t2)r.
    Real-valued conjugacy is built in by using -theta[j,k] at negative modes.
    """
    b = block_word(fam)
    t1, t2, t3 = triple
    mult = {
        t1: t2 - t3,
        t2: t3 - t1,
        t3: t1 - t2,
    }
    row = [0] * len(VARS)
    for t, m in mult.items():
        row[VID[(b[t], abs(m))]] += 1 if m > 0 else -1
    return row

def det_bareiss(a):
    """Exact integer determinant via Bareiss elimination."""
    m = [list(map(int, row)) for row in a]
    n = len(m)
    sign = 1
    prev = 1
    for k in range(n - 1):
        pivot = next((r for r in range(k, n) if m[r][k] != 0), None)
        if pivot is None:
            return 0
        if pivot != k:
            m[k], m[pivot] = m[pivot], m[k]
            sign *= -1
        p = m[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                m[i][j] = (m[i][j] * p - m[i][k] * m[k][j]) // prev
            m[i][k] = 0
        prev = p
    return sign * m[-1][-1]

A = [phase_row(CORE[f], TRIPLE[f]) for f in FAMILY_ORDER]

# Columns:
# theta_01, theta_02, theta_11, theta_12, theta_13,
# theta_21, theta_22, theta_23, theta_31, theta_32.
MINOR_COLS = [0, 1, 3, 4, 5, 6, 7, 8, 9, 10]
M = [[row[c] for c in MINOR_COLS] for row in A]
DET = det_bareiss(M)
assert DET == -3, DET

print("variables", VARS)
print("family_triples")
for f in FAMILY_ORDER:
    print(f"  F{f}: blocks={block_word(CORE[f])} triple={TRIPLE[f]} row={A[FAMILY_ORDER.index(f)]}")
print("minor_columns", [VARS[c] for c in MINOR_COLS])
print("minor_determinant", DET)
print("rank_certificate", 10)
print("conclusion", "phase map R^12 -> R^10 is surjective")
