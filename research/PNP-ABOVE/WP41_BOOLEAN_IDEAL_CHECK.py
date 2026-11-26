#!/usr/bin/env python3
"""Exhaustive finite checks for the SCC Boolean-ring research candidate."""
from itertools import product


def candidate(cs, g, one):
    prefix = one
    a = []
    for c in cs:
        a.append(g & prefix)
        prefix &= one ^ c
    return one ^ prefix, a


def dot(a, b):
    ans = 0
    for x, y in zip(a, b, strict=True):
        ans ^= x & y
    return ans


def check():
    if not __debug__:
        raise RuntimeError("assertions required")
    one = 15
    count = 0
    for m in range(4):
        for cs in product(range(one + 1), repeat=m):
            for g in range(one + 1):
                v, a = candidate(cs, g, one)
                assert all(c & v == c for c in cs)
                assert g ^ dot(a, cs) == g & (one ^ v)
                assert (dot(a, cs) == g) == (g & v == g)
                assert (dot(candidate(cs, one, one)[1], cs) == one) == (v == one)
                count += 1
    print(f"Boolean ideal and coefficient identities: {count} cases")
    one = 3
    count = 0
    for c1, c2, g, k1, k2, t in product(range(one + 1), repeat=6):
        cs = (c1, c2)
        k = (k1, k2)
        v, a = candidate(cs, g, one)
        b = tuple(x ^ (t & y) for x, y in zip(k, a, strict=True))
        assert tuple(x ^ (t & y) for x, y in zip(b, a, strict=True)) == k
        assert dot(b, cs) ^ (t & g) == dot(k, cs) ^ (t & g & (one ^ v))
        if g & v == g:
            assert (dot(b, cs) ^ (t & g) == 0) == (dot(k, cs) == 0)
        count += 1
    print(f"Shear and residual identities: {count} cases")


if __name__ == "__main__":
    check()
