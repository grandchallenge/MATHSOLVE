#!/usr/bin/env python3
"""Finite F2 certificate for the WP60N relation/exchange combinatorics.

This checks only the finite linear-algebra layer of the theorem. Arithmetic
claims about Selmer membership, localization, core transitions, and paths are
proved in 01_COISOTROPIC_EXCHANGE_CONNECTIVITY_THEOREM.md from protected
interfaces and are not inferred from this script.
"""

from itertools import combinations, product


def add(*vs):
    if not vs:
        return ()
    n = len(vs[0])
    out = [0] * n
    for v in vs:
        assert len(v) == n
        for i, x in enumerate(v):
            out[i] ^= x
    return tuple(out)


def nz_vectors(n):
    return [v for v in product((0, 1), repeat=n) if any(v)]


def odd_triples(classes):
    out = []
    for I in combinations(range(4), 3):
        if not any(add(*(classes[i] for i in I))):
            out.append(I)
    return out


def check_dimension(n):
    vecs = nz_vectors(n)
    checked = 0
    direct = 0
    exchanged_1 = 0
    exchanged_2 = 0
    simultaneous_hard = 0

    for p1 in vecs:
        for d1 in vecs:
            if p1 == d1:  # <p1> direct_sum <d1>
                continue
            for p2 in vecs:
                for d2 in vecs:
                    if p2 == d2:  # <p2> direct_sum <d2>
                        continue

                    # Coisotropic strict-place separation excludes the two
                    # one-primal/two-dual odd relations.
                    if not any(add(p1, d1, d2)):
                        continue
                    if not any(add(p2, d1, d2)):
                        continue

                    checked += 1
                    triples = odd_triples([p1, d1, p2, d2])

                    hard1 = not any(add(p1, p2, d1))
                    hard2 = not any(add(p1, p2, d2))

                    # After the two forbidden relations are removed, every
                    # remaining obstruction is one or both of the two hard
                    # two-primal/one-dual relations. Both can occur exactly
                    # when the two dual generators coincide; either exchange
                    # still resolves the aligned configuration.
                    assert bool(triples) == (hard1 or hard2)
                    if hard1 and hard2:
                        assert d1 == d2
                        simultaneous_hard += 1

                    if not triples:
                        direct += 1
                        continue

                    if hard1:
                        # Exchange the first core. Its new primal generator is
                        # p2, so the aligned four classes are p2,d1,p2,d2.
                        aligned = [p2, d1, p2, d2]
                        assert not odd_triples(aligned)
                        exchanged_1 += 1
                    else:
                        # Symmetric exchange of the second core.
                        aligned = [p1, d1, p1, d2]
                        assert not odd_triples(aligned)
                        exchanged_2 += 1

    return {
        "dimension": n,
        "checked": checked,
        "direct": direct,
        "exchange_first": exchanged_1,
        "exchange_second": exchanged_2,
        "simultaneous_hard": simultaneous_hard,
    }


def main():
    rows = [check_dimension(n) for n in range(2, 5)]
    assert all(r["checked"] > 0 for r in rows)
    assert all(
        r["checked"]
        == r["direct"] + r["exchange_first"] + r["exchange_second"]
        for r in rows
    )
    print("WP60N finite relation/exchange certificate: PASS")
    for r in rows:
        print(r)


if __name__ == "__main__":
    main()
