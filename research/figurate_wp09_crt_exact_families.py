"""FIGURATE WP09-007: finite-prime-power CRT and exact Type B constructions.

A modular witness is not an exact integer tuple. The Pell and Euler
constructors explicitly verify all three exact polygonal identities.
"""
from __future__ import annotations

import argparse
import json
from math import isqrt

from research.figurate_wp08_square_normal_form import obstruction_witness
from research.figurate_wp09_odd_prime_power_complete import (
    common_residue_witness, polygonal,
)


def factor_prime_powers(M: int) -> tuple[tuple[int, int, int], ...]:
    if M < 1:
        raise ValueError("positive modulus required")
    x = M
    factors: list[tuple[int, int, int]] = []
    for p in range(2, isqrt(x) + 1):
        if x % p == 0:
            n = 0
            q = 1
            while x % p == 0:
                x //= p
                n += 1
                q *= p
            factors.append((p, n, q))
    if x > 1:
        factors.append((x, 1, x))
    return tuple(factors)


def _binary_witness(k: int, c: int, n: int) -> tuple[tuple[int, ...], tuple[int, ...]] | None:
    """Complete exact decision for n<=8; no asymptotic or all-2-adic claim."""
    if n < 1 or n > 8:
        raise ValueError("binary exponent outside audited finite range [1,8]")
    q = 1 << n
    image_index: dict[int, int] = {}
    for t in range(1, q + 1):
        image_index.setdefault(polygonal(k, t) % q, t % q)
    if k % 4 == 0:
        entries = obstruction_witness(k, c, n)
    else:
        # WP08 proves binary surjectivity when 4 does not divide k.
        entries = (1 % q, 2 % q, 3 % q)
    if entries is None:
        return None
    a, b, d = entries
    targets = ((a*b+c) % q, (a*d+c) % q, (b*d+c) % q)
    try:
        indices = tuple(image_index[v] for v in targets)
    except KeyError as exc:
        raise AssertionError("binary witness lacks polygonal index") from exc
    return tuple(entries), indices


def _crt(residues: list[int], moduli: list[int]) -> int:
    M = 1
    for q in moduli:
        M *= q
    if not moduli:
        return 0
    total = 0
    for r, q in zip(residues, moduli):
        N = M // q
        total += r * N * pow(N, -1, q)
    return total % M


def finite_modulus_witness(k: int, c: int, M: int) -> dict | None:
    """Exact compatibility decision for odd M, and v2(M)<=8.

    All three entry residues and all three index residues are CRT-glued
    coordinatewise. For M=1 the zero residue is trivially compatible.
    """
    if k < 3 or M < 1:
        raise ValueError("k>=3 and M>=1 required")
    factors = factor_prime_powers(M)
    entry_components: list[tuple[int, int, int]] = []
    index_components: list[tuple[int, int, int]] = []
    moduli: list[int] = []
    for p, n, q in factors:
        if p == 2:
            w = _binary_witness(k, c, n)
            if w is None:
                return None
            entries, indices = w
        else:
            w = common_residue_witness(k, c, p, n)
            if w is None:
                return None
            entries = (w["entry_residue"],)*3
            indices = (w["index_residue"],)*3
        entry_components.append(tuple(entries))
        index_components.append(tuple(indices))
        moduli.append(q)
    entry_residues = tuple(_crt([part[i] for part in entry_components], moduli)
                           for i in range(3))
    index_residues = tuple(_crt([part[i] for part in index_components], moduli)
                           for i in range(3))
    pairs = ((0,1),(0,2),(1,2))
    if not all((entry_residues[i]*entry_residues[j] + c -
                polygonal(k, index_residues[z] + M)) % M == 0
               for z,(i,j) in enumerate(pairs)):
        raise AssertionError("CRT witness fails independent polynomial check")
    return {
        "order": k, "offset": c, "modulus": M,
        "entry_residues": entry_residues,
        "index_residues": index_residues,
        "distinct_positive_entries": tuple(x + (i+1)*M
                                           for i,x in enumerate(entry_residues)),
        "positive_index_representatives": tuple(x+M for x in index_residues),
    }


def exact_type_b(k: int, c: int, entries: tuple[int,int,int],
                 indices: tuple[int,int,int]) -> bool:
    a,b,d = entries
    r,s,t = indices
    return (len({a,b,d}) == 3 and min(entries) > 0 and min(indices) > 0
            and a*b+c == polygonal(k,r)
            and a*d+c == polygonal(k,s)
            and b*d+c == polygonal(k,t))


def euler_square_family(c: int, t: int) -> dict:
    """Exact Type B for k=4 and arbitrary signed c, with t sufficiently large."""
    if t < 2 or t*t-c <= 1 or t*(t+1)-c <= 0:
        raise ValueError("choose a larger positive seed t")
    entries = (1, t*t-c, (t+1)*(t+1)-c)
    indices = (t, t+1, t*(t+1)-c)
    if not exact_type_b(4, c, entries, indices):
        raise AssertionError("Euler exact identity failed")
    return {"order":4, "offset":c, "entries":entries, "indices":indices}


def pell_20_2_family(step: int) -> dict:
    """Infinite exact Type B family at (k,c)=(20,2).

    Write S=9s-4, T=9t-4 and T²-18S²=-578.
    Starting from s=39,t=164, apply the norm-one unit
    17+4*sqrt(18), 18 times per step to preserve T=S=-4 mod9.
    """
    if step < 0:
        raise ValueError("step must be nonnegative")
    T, S = 1472, 347
    for _ in range(18*step):
        T,S = 17*T+72*S, 4*T+17*S
    if (T*T-18*S*S != -578 or (T+4)%9 or (S+4)%9):
        raise AssertionError("Pell invariant or index congruence failed")
    t,s = (T+4)//9, (S+4)//9
    d = polygonal(20,s)-2
    entries = (1,18,d)
    indices = (2,s,t)
    if not exact_type_b(20,2,entries,indices):
        raise AssertionError("exact 20-gonal tuple identity failed")
    return {"order":20,"offset":2,"step":step,"entries":entries,
            "indices":indices,"pell_T":T,"pell_S":S}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--order", type=int, default=20)
    parser.add_argument("--offset", type=int, default=2)
    parser.add_argument("--modulus", type=int, default=225)
    parser.add_argument("--pell-step", type=int)
    parser.add_argument("--euler-seed", type=int)
    args = parser.parse_args()
    if args.pell_step is not None:
        result = pell_20_2_family(args.pell_step)
    elif args.euler_seed is not None:
        result = euler_square_family(args.offset, args.euler_seed)
    else:
        result = finite_modulus_witness(args.order,args.offset,args.modulus)
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
