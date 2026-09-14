#!/usr/bin/env python3
"""Exact finite certificate for BSD-R2-A1 WP60I.

Proves by exhaustive integer arithmetic that:
  * S,T,D generate GL_2(Z/4), of order 96;
  * the prescribed generator values extend to a crossed homomorphism
    z: GL_2(Z/4) -> F_2^2;
  * z satisfies the cocycle identity on every ordered pair;
  * z is not a coboundary because it is nonzero on T^2, which acts
    trivially on F_2^2.

No third-party dependencies.
"""

from itertools import product
import json

MOD = 4
I = (1, 0, 0, 1)
S = (0, 3, 1, 0)  # [[0,-1],[1,0]] mod 4
T = (1, 1, 0, 1)
D = (3, 0, 0, 1)  # diag(-1,1) mod 4
GENS = (S, T, D)
ZGEN = ((0, 0), (0, 1), (1, 1))


def mul(a, b, modulus=MOD):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % modulus
        for i in range(2)
        for j in range(2)
    )


def det(a, modulus=MOD):
    return (a[0] * a[3] - a[1] * a[2]) % modulus


def add2(u, v):
    return ((u[0] + v[0]) & 1, (u[1] + v[1]) & 1)


def act2(a, v):
    return (
        (a[0] * v[0] + a[1] * v[1]) & 1,
        (a[2] * v[0] + a[3] * v[1]) & 1,
    )


def all_gl2_z4():
    return {
        a
        for a in product(range(4), repeat=4)
        if det(a) & 1
    }


def generate_group_and_cocycle():
    """BFS simultaneously generates the group and propagates z(gx)."""
    z = {I: (0, 0)}
    todo = [I]
    while todo:
        g = todo.pop()
        zg = z[g]
        for x, zx in zip(GENS, ZGEN):
            h = mul(g, x)
            candidate = add2(zg, act2(g, zx))
            if h in z:
                assert z[h] == candidate, (
                    "cocycle propagation conflict",
                    g,
                    x,
                    h,
                    z[h],
                    candidate,
                )
            else:
                z[h] = candidate
                todo.append(h)
    return z


def main():
    gl = all_gl2_z4()
    z = generate_group_and_cocycle()

    assert len(gl) == 96
    assert set(z) == gl

    pair_checks = 0
    for g in gl:
        for h in gl:
            gh = mul(g, h)
            rhs = add2(z[g], act2(g, z[h]))
            assert z[gh] == rhs
            pair_checks += 1

    t2 = mul(T, T)
    assert t2 == (1, 2, 0, 1)
    assert tuple(x & 1 for x in t2) == I
    assert z[t2] == (1, 0)

    # Every coboundary delta_v(g)=g.v-v vanishes on an element acting
    # trivially on V. Verify this explicitly for all four v in F_2^2.
    for v in product(range(2), repeat=2):
        delta = add2(act2(t2, v), v)  # subtraction equals addition in F_2
        assert delta == (0, 0)

    result = {
        "group": "GL_2(Z/4)",
        "group_size": len(gl),
        "generators": {
            "S": S,
            "T": T,
            "D": D,
        },
        "generator_cocycle_values": {
            "z(S)": ZGEN[0],
            "z(T)": ZGEN[1],
            "z(D)": ZGEN[2],
        },
        "ordered_pair_cocycle_checks": pair_checks,
        "kernel_witness": {
            "T^2": t2,
            "T^2_mod_2": tuple(x & 1 for x in t2),
            "z(T^2)": z[t2],
        },
        "conclusion": "H^1(GL_2(Z/4), F_2^2) is nonzero",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
