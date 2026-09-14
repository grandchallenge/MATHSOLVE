#!/usr/bin/env python3
"""Exact finite certificate for BSD WP60L.

Checks only finite algebra used by the theorem:
- GL_2(Z/4) has 96 elements and S,T,D generate it;
- the protected WP60K nonzero cocycle extends consistently and satisfies
  the cocycle identity on all 96^2 ordered pairs;
- its value at the primitive transvection U=T is not a coboundary on <U>;
- A[2] has no GL_2(Z/4)-invariants, so the extra C2 auxiliary-field
  inflation-restriction term vanishes;
- diag(5,1) is identity mod 4 but has determinant 5 mod 8, the finite
  matrix witness used to separate Q(E[4]) from Q(mu_8).
"""

from collections import deque
from itertools import product

M = 4


def mm(a, b, m=M):
    return (
        (a[0] * b[0] + a[1] * b[2]) % m,
        (a[0] * b[1] + a[1] * b[3]) % m,
        (a[2] * b[0] + a[3] * b[2]) % m,
        (a[2] * b[1] + a[3] * b[3]) % m,
    )


def mv(a, v, m=M):
    return (
        (a[0] * v[0] + a[1] * v[1]) % m,
        (a[2] * v[0] + a[3] * v[1]) % m,
    )


def det(a, m=M):
    return (a[0] * a[3] - a[1] * a[2]) % m


def inv(a, m=M):
    di = pow(det(a, m), -1, m)
    return (
        a[3] * di % m,
        -a[1] * di % m,
        -a[2] * di % m,
        a[0] * di % m,
    )


def vadd(a, b, m=M):
    return ((a[0] + b[0]) % m, (a[1] + b[1]) % m)


G = [a for a in product(range(M), repeat=4) if det(a) % 2 == 1]
assert len(G) == 96

I = (1, 0, 0, 1)
S = (0, 3, 1, 0)
T = (1, 1, 0, 1)
D = (3, 0, 0, 1)

# WP60K representative.
zgen = {S: (0, 0), T: (0, 2), D: (2, 2)}

edges = []
for g, zg in zgen.items():
    edges.append((g, zg))
    gi = inv(g)
    t = mv(gi, zg)
    edges.append((gi, ((-t[0]) % M, (-t[1]) % M)))

z = {I: (0, 0)}
queue = deque([I])
while queue:
    a = queue.popleft()
    for g, zg in edges:
        b = mm(a, g)
        candidate = vadd(z[a], mv(a, zg))
        if b in z:
            assert z[b] == candidate
        else:
            z[b] = candidate
            queue.append(b)

assert len(z) == 96  # S,T,D generate all of G.

for a in G:
    for b in G:
        assert z[mm(a, b)] == vadd(z[a], mv(a, z[b]))

# Primitive-transvection restriction is nonzero in H^1(<T>,A).
assert z[T] == (0, 2)
coboundary_values_at_T = set()
for v in product(range(M), repeat=2):
    Tv = mv(T, v)
    coboundary_values_at_T.add(((Tv[0] - v[0]) % M, (Tv[1] - v[1]) % M))
assert coboundary_values_at_T == {(0, 0), (1, 0), (2, 0), (3, 0)}
assert z[T] not in coboundary_values_at_T

# The inflation-restriction error term Hom(C2,A)^G=A[2]^G vanishes.
A2 = [(0, 0), (2, 0), (0, 2), (2, 2)]
invariants = [v for v in A2 if all(mv(g, v) == v for g in G)]
assert invariants == [(0, 0)]

# Full 2-adic image supplies this lift: it fixes E[4] but not mu_8.
lift_mod_8 = (5, 0, 0, 1)
assert tuple(x % 4 for x in lift_mod_8) == I
assert (lift_mod_8[0] * lift_mod_8[3] - lift_mod_8[1] * lift_mod_8[2]) % 8 == 5

print("WP60L certificate PASS")
print("|GL2(Z/4)| =", len(G))
print("z(T) =", z[T], "is not a coboundary on <T>")
print("A[2]^G = 0")
print("diag(5,1) fixes mod 4 and has determinant 5 mod 8")
