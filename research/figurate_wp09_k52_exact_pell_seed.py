"""FIGURATE WP09-013: exact 52-gonal Type B seed and Pell orbit.

The positive seed (2,25,703) has indices (2,8,27) at offset 2.
The unit 99+14*sqrt(50), raised to the 200th power, fixes
all needed index and divisibility congruences modulo 400.
This yields an infinite exact family without novelty/certification claims.
"""
from __future__ import annotations
import argparse
import json


def polygonal(k: int, n: int) -> int:
    if k < 3 or n < 1:
        raise ValueError("order k>=3 and index n>=1 required")
    return ((k - 2) * n * n - (k - 4) * n) // 2


def verify(entries: tuple[int, int, int],
           indices: tuple[int, int, int]) -> bool:
    a, b, d = entries
    r, s, t = indices
    return (min(*entries, *indices) > 0
            and len(set(entries)) == 3
            and (a*b + 2, a*d + 2, b*d + 2)
            == tuple(polygonal(52, n) for n in indices))


def multiply_unit(X: int, S: int) -> tuple[int, int]:
    """Multiply X+S sqrt(50) by the norm-one unit 99+14 sqrt(50)."""
    return 99*X + 700*S, 14*X + 99*S


def unit_modulus_check() -> bool:
    """Prove (99+14sqrt(50))^200 = 1 mod 400 in Z[sqrt(50)]."""
    x, y = 1, 0
    for _ in range(200):
        x, y = (99*x + 700*y) % 400, (14*x + 99*y) % 400
    return (x, y) == (1, 0)


def exact_member(step: int = 0) -> dict:
    if step < 0:
        raise ValueError("step must be nonnegative")
    assert unit_modulus_check()
    a, b, r = 2, 25, 2
    R, L, D = 100, 48, 3104
    X, S = a*(R*27 - L), R*8 - L
    norm = a*(a-b)*D  # -142784
    for _ in range(200*step):
        X, S = multiply_unit(X, S)
    if X*X - a*b*S*S != norm:
        raise AssertionError("Pell norm not preserved")
    if X % a or (X//a + L) % R or (S+L) % R:
        raise AssertionError("polygonal index integrality not preserved")
    t, s = (X//a + L)//R, (S+L)//R
    ps = polygonal(52, s)
    if (ps-2) % a:
        raise AssertionError("entry divisibility not preserved")
    d = (ps-2)//a
    entries, indices = (a,b,d), (r,s,t)
    if not verify(entries, indices):
        raise AssertionError("exact Type B identity not satisfied")
    return {"order":52, "offset":2, "entries":entries, "indices":indices,
            "pell_step":step, "unit_power_per_step":200}


def bounded_triangles(max_entry: int = 2000) -> list[tuple[int,int,int]]:
    """Complete exhaustive search for triples with max(entry)<=max_entry.

    Edge a--b iff ab+2=P_52(n) for some positive n.
    Each triple is a triangle in this undirected arithmetic graph.
    """
    if not 3 <= max_entry <= 2000:
        raise ValueError("bounded audit requires 3 <= max_entry <= 2000")
    edges: dict[int,set[int]] = {}
    n=1
    from math import isqrt
    while True:
        v=polygonal(52,n)-2
        if v>max_entry*max_entry:
            break
        if v>0:
            for a in range(1,isqrt(v)+1):
                if v%a:
                    continue
                b=v//a
                if b<=max_entry and a!=b:
                    edges.setdefault(a,set()).add(b)
                    edges.setdefault(b,set()).add(a)
        n+=1
    triangles=set()
    for a, near in edges.items():
        for b in near:
            if b>a:
                for d in near.intersection(edges[b]):
                    if d>b:
                        triangles.add((a,b,d))
    return sorted(triangles)


def main() -> None:
    parser=argparse.ArgumentParser()
    parser.add_argument("--step",type=int,default=0)
    args=parser.parse_args()
    print(json.dumps(exact_member(args.step),sort_keys=True))


if __name__=="__main__":
    main()
