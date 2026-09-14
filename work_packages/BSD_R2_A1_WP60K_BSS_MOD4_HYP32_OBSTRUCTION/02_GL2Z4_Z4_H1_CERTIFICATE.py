#!/usr/bin/env python3
"""Exact finite certificate for BSD-R2-A1 WP60K.

Proves by exhaustive integer arithmetic that

    |H^1(GL_2(Z/4), (Z/4)^2)| = 2.

The script:
  * enumerates all 96 elements of GL_2(Z/4);
  * proves S,T,D generate the group;
  * enumerates every consistent generator assignment for a 1-cocycle;
  * verifies the cocycle identity for every ordered group pair for every
    accepted cocycle;
  * enumerates every coboundary;
  * isolates an explicit non-coboundary witness.

No third-party dependencies.
"""

from itertools import product
import json

MOD = 4
I = (1, 0, 0, 1)
S = (0, 3, 1, 0)  # [[0,-1],[1,0]]
T = (1, 1, 0, 1)  # [[1,1],[0,1]]
D = (3, 0, 0, 1)  # diag(-1,1)
GENS = (S, T, D)
WITNESS_VALUES = ((0, 0), (0, 2), (2, 2))
VECTORS = tuple(product(range(MOD), repeat=2))


def mat_mul(a, b):
    return tuple(
        sum(a[2 * i + k] * b[2 * k + j] for k in range(2)) % MOD
        for i in range(2)
        for j in range(2)
    )


def det(a):
    return (a[0] * a[3] - a[1] * a[2]) % MOD


def vec_add(u, v):
    return ((u[0] + v[0]) % MOD, (u[1] + v[1]) % MOD)


def vec_sub(u, v):
    return ((u[0] - v[0]) % MOD, (u[1] - v[1]) % MOD)


def act(a, v):
    return (
        (a[0] * v[0] + a[1] * v[1]) % MOD,
        (a[2] * v[0] + a[3] * v[1]) % MOD,
    )


def all_gl2_z4():
    return {
        a
        for a in product(range(MOD), repeat=4)
        if det(a) % 2 == 1
    }


def generate_group(gens):
    seen = {I}
    todo = [I]
    while todo:
        g = todo.pop()
        for x in gens:
            h = mat_mul(g, x)
            if h not in seen:
                seen.add(h)
                todo.append(h)
    return seen


def propagate_cocycle(generator_values):
    """Return the unique propagated cocycle, or None on a relation conflict."""
    z = {I: (0, 0)}
    todo = [I]
    while todo:
        g = todo.pop()
        zg = z[g]
        for x, zx in zip(GENS, generator_values):
            h = mat_mul(g, x)
            candidate = vec_add(zg, act(g, zx))
            if h in z:
                if z[h] != candidate:
                    return None
            else:
                z[h] = candidate
                todo.append(h)
    return z


def coboundary(v, keys):
    return tuple(vec_sub(act(g, v), v) for g in keys)


def main():
    group = all_gl2_z4()
    assert len(group) == 96
    assert generate_group(GENS) == group
    keys = sorted(group)

    cocycles = []
    witness = None
    pair_checks = 0

    for generator_values in product(VECTORS, repeat=len(GENS)):
        z = propagate_cocycle(generator_values)
        if z is None:
            continue
        assert set(z) == group

        # Verify the actual cocycle identity independently of BFS propagation.
        for g in group:
            for h in group:
                gh = mat_mul(g, h)
                rhs = vec_add(z[g], act(g, z[h]))
                assert z[gh] == rhs
                pair_checks += 1

        encoded = tuple(z[g] for g in keys)
        cocycles.append(encoded)
        if generator_values == WITNESS_VALUES:
            witness = (generator_values, z, encoded)

    assert len(cocycles) == 32
    assert len(set(cocycles)) == 32

    coboundaries = {coboundary(v, keys) for v in VECTORS}
    assert len(coboundaries) == 16
    assert coboundaries.issubset(set(cocycles))
    assert len(cocycles) // len(coboundaries) == 2

    assert witness is not None
    _, witness_z, witness_encoded = witness
    assert witness_encoded not in coboundaries
    assert witness_z[S] == (0, 0)
    assert witness_z[T] == (0, 2)
    assert witness_z[D] == (2, 2)

    # Transparent non-coboundary witness: for every v=(x,y),
    # delta_v(T)=(T-I)v=(y,0), so its second coordinate is zero.
    t_coboundary_values = []
    for v in VECTORS:
        delta_t = vec_sub(act(T, v), v)
        assert delta_t[1] == 0
        t_coboundary_values.append(delta_t)
    assert witness_z[T][1] == 2

    result = {
        "group": "GL_2(Z/4)",
        "group_size": len(group),
        "module": "(Z/4)^2",
        "generators": {"S": S, "T": T, "D": D},
        "Z1_size": len(cocycles),
        "B1_size": len(coboundaries),
        "H1_order": len(cocycles) // len(coboundaries),
        "ordered_pair_cocycle_checks": pair_checks,
        "checks_per_cocycle": len(group) ** 2,
        "witness_generator_values": {
            "z(S)": witness_z[S],
            "z(T)": witness_z[T],
            "z(D)": witness_z[D],
        },
        "witness_non_coboundary_reason": (
            "every coboundary has second coordinate 0 at T; witness z(T)=(0,2)"
        ),
        "conclusion": "H^1(GL_2(Z/4),(Z/4)^2) has order 2",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
