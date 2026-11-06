"""FIGURATE WP09-014: exact 52-gonal Type B family at offset six.

Complete finite graph census with bounded positive entries; finite absence
never implies global nonexistence. All arithmetic is integer-exact.
"""
from __future__ import annotations
from math import isqrt
import argparse
import json

K, C = 52, 6
SEED_ENTRIES = (2, 2279, 4757)
SEED_INDICES = (14, 20, 659)


def polygonal(n: int) -> int:
    if n < 1:
        raise ValueError("positive index required")
    return 25*n*n - 24*n


def index_for(value: int) -> int | None:
    """Inverse 52-gonal index, requiring positive exact integer equality."""
    if value < 1:
        return None
    delta = 100*value + 576
    root = isqrt(delta)
    if root*root != delta or (root+24) % 50:
        return None
    n = (root+24)//50
    return n if n >= 1 and polygonal(n) == value else None


def exact_tuple(entries: tuple[int,int,int]) -> dict | None:
    a,b,d = entries
    if min(entries) <= 0 or len(set(entries)) != 3:
        return None
    pair_outputs = (a*b+C,a*d+C,b*d+C)
    indices = tuple(index_for(z) for z in pair_outputs)
    if any(n is None for n in indices):
        return None
    return {"order":K,"offset":C,"entries":entries,
            "indices":indices,"pair_outputs":pair_outputs}


def graph_census(entry_bound: int) -> dict:
    """Enumerate every unordered triple 1<=a<b<d<=entry_bound.

    Each permitted edge ab comes from a positive P_52(n)-6<=bound^2.
    For each n the complete factor-pair enumeration populates all edges.
    The graph triangles are exactly the Type B triples in the bound.
    """
    if not 3 <= entry_bound <= 10000:
        raise ValueError("entry bound must lie in 3..10000")
    adj: dict[int,set[int]] = {}
    indices_by_edge: dict[tuple[int,int],int] = {}
    n = 1
    while True:
        product = polygonal(n)-C
        if product > entry_bound*entry_bound:
            break
        if product > 0:
            for a in range(1,min(entry_bound,isqrt(product))+1):
                if product % a:
                    continue
                b = product//a
                if a < b <= entry_bound:
                    adj.setdefault(a,set()).add(b)
                    adj.setdefault(b,set()).add(a)
                    indices_by_edge[(a,b)] = n
        n += 1
    triples = []
    for a in sorted(adj):
        for b in sorted(v for v in adj[a] if v>a):
            for d in sorted(v for v in adj[a].intersection(adj[b]) if v>b):
                indices=(indices_by_edge[(a,b)],indices_by_edge[(a,d)],
                         indices_by_edge[(b,d)])
                record=exact_tuple((a,b,d))
                if record is None or record["indices"]!=indices:
                    raise ArithmeticError("invalid triangle")
                triples.append(record)
    return {"order":K,"offset":C,"entry_bound":entry_bound,
            "index_count":n-1,"edge_count":len(indices_by_edge),
            "triple_count":len(triples),"triples":triples,
            "global_nonexistence_proved":False}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--entry-bound",type=int,default=10000)
    args=p.parse_args()
    print(json.dumps(graph_census(args.entry_bound),sort_keys=True))


if __name__=="__main__":
    main()
