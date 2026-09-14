#!/usr/bin/env python3
"""Exact finite certificate for BSD-R2-A1 WP60J.

Checks the finite residual group-cohomology input used in the theorem:
  * GL_2(F_2) has order 6 and the natural module V=F_2^2 has no invariants;
  * H^1(GL_2(F_2), V)=0;
  * for G=GL_2(F_2) x C_2, with C_2 acting trivially on V,
    H^1(G,V)=0.

The calculation is exhaustive and uses only integer arithmetic.
"""

from itertools import product
import json

I = (1, 0, 0, 1)
S = (0, 1, 1, 0)
T = (1, 1, 0, 1)
C = 1


def mul2(a, b):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) & 1
        for i in range(2)
        for j in range(2)
    )


def det2(a):
    return (a[0] * a[3] - a[1] * a[2]) & 1


def act2(a, v):
    return (
        (a[0] * v[0] + a[1] * v[1]) & 1,
        (a[2] * v[0] + a[3] * v[1]) & 1,
    )


def add2(u, v):
    return (u[0] ^ v[0], u[1] ^ v[1])


def gl2_f2():
    return {
        a
        for a in product(range(2), repeat=4)
        if det2(a) == 1
    }


def generate_group(gens, mul, identity):
    seen = {identity}
    todo = [identity]
    while todo:
        g = todo.pop()
        for x in gens:
            h = mul(g, x)
            if h not in seen:
                seen.add(h)
                todo.append(h)
    return seen


def propagate_cocycles(group, gens, action, mul, identity):
    vectors = list(product(range(2), repeat=2))
    valid = []
    for values in product(vectors, repeat=len(gens)):
        z = {identity: (0, 0)}
        todo = [identity]
        ok = True
        while todo and ok:
            g = todo.pop()
            for x, zx in zip(gens, values):
                h = mul(g, x)
                candidate = add2(z[g], action(g, zx))
                if h in z:
                    if z[h] != candidate:
                        ok = False
                        break
                else:
                    z[h] = candidate
                    todo.append(h)
        if ok:
            assert set(z) == group
            valid.append((values, z))
    return valid


def coboundaries(group, action):
    keys = sorted(group)
    out = set()
    for v in product(range(2), repeat=2):
        out.add(tuple(add2(action(g, v), v) for g in keys))
    return out


def main():
    gl = gl2_f2()
    assert len(gl) == 6
    assert generate_group((S, T), mul2, I) == gl

    invariants = [
        v for v in product(range(2), repeat=2)
        if all(act2(g, v) == v for g in gl)
    ]
    assert invariants == [(0, 0)]

    z_gl = propagate_cocycles(gl, (S, T), act2, mul2, I)
    b_gl = coboundaries(gl, act2)
    assert len(z_gl) == 4
    assert len(b_gl) == 4
    keys_gl = sorted(gl)
    assert {tuple(z[g] for g in keys_gl) for _, z in z_gl} == b_gl

    identity = (I, 0)
    gens = ((S, 0), (T, 0), (I, C))

    def mul_prod(x, y):
        return (mul2(x[0], y[0]), x[1] ^ y[1])

    def act_prod(x, v):
        return act2(x[0], v)

    gp = {(g, e) for g in gl for e in (0, 1)}
    assert len(gp) == 12
    assert generate_group(gens, mul_prod, identity) == gp

    z_gp = propagate_cocycles(gp, gens, act_prod, mul_prod, identity)
    b_gp = coboundaries(gp, act_prod)
    assert len(z_gp) == 4
    assert len(b_gp) == 4
    keys_gp = sorted(gp)
    assert {tuple(z[g] for g in keys_gp) for _, z in z_gp} == b_gp

    print(json.dumps({
        "GL2_F2_order": len(gl),
        "V_invariants": invariants,
        "Z1_GL2_F2_size": len(z_gl),
        "B1_GL2_F2_size": len(b_gl),
        "H1_GL2_F2_order": 1,
        "product_group": "GL_2(F_2) x C_2",
        "product_group_order": len(gp),
        "Z1_product_size": len(z_gp),
        "B1_product_size": len(b_gp),
        "H1_product_order": 1,
        "conclusion": "H^1(GL_2(F_2) x C_2, F_2^2)=0",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
