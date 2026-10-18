#!/usr/bin/env python3
"""Exact q=6 necessary-state replay; no geometric or Cert promotion."""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path

EDGES = tuple(itertools.combinations(range(6), 2))
EXPECTED = {
    '333333': {3:260,4:1095,5:2412,6:4945,7:6345,8:6435,9:4990,10:3003,11:1365,12:455},
    '333334': {5:1110,6:2175,7:5265,8:5310,9:4750,10:2643,11:1340,12:395},
    '333335': {7:60,8:540,9:250,10:525},
    '333344': {6:327,7:765,8:2464,9:1510,10:1077},
    '333444': {9:70},
}

@lru_cache(None)
def local_states(r, degree):
    n = 2*r
    full = (1 << n)-1
    def rotate(mask):
        return ((mask << 1) & full) | (mask >> (n-1))
    out = set()
    for sectors in range(1 << n):
        shared = sectors & rotate(sectors)
        positions = [i for i in range(n) if (shared >> i) & 1]
        for chosen in itertools.combinations(positions, degree):
            two = sum(1 << i for i in chosen)
            one = shared ^ two
            run = one
            shifted = one
            for _ in range(r-2):
                shifted = rotate(shifted)
                run &= shifted
            if run:
                continue
            adjacent = rotate(two) | (two >> 1) | ((two & 1) << (n-1))
            out.add((one.bit_count(), (one & adjacent).bit_count()))
    return tuple(sorted(out))

@lru_cache(None)
def combined_states(pairs):
    totals = {(0,0)}
    for r,d in pairs:
        options = local_states(r,d)
        totals = {(a+c,b+e) for a,b in totals for c,e in options}
    return tuple(sorted(totals))

def graph(mask):
    neighbors = [set() for _ in range(6)]
    for index,(a,b) in enumerate(EDGES):
        if mask & (1 << index):
            neighbors[a].add(b)
            neighbors[b].add(a)
    return neighbors

def cubic_certificate(neighbors):
    """Return complete K3,3 partition or two triangles and matching (prism)."""
    assert all(len(n)==3 for n in neighbors)
    vertices = set(range(6))
    for triple in itertools.combinations(range(6),3):
        left = set(triple)
        right = vertices-left
        if all(neighbors[v]==right for v in left) and all(neighbors[v]==left for v in right):
            return {'class':'K3_3','parts':[sorted(left),sorted(right)]}
        if all(left-{v} <= neighbors[v] for v in left) and all(right-{v} <= neighbors[v] for v in right):
            matching = sorted((v,next(iter(neighbors[v]&right))) for v in left)
            assert len({w for _,w in matching})==3
            return {'class':'TRIANGULAR_PRISM','triangles':[sorted(left),sorted(right)],'matching':matching}
    raise AssertionError('Unclassified labeled cubic graph')

def replay():
    # Derived bound: S <= 3 + (2I-18) + 15 = 2I, so sum r(r-4)<=0.
    # r>=7 would contribute >=21 against at most five contributions of -3.
    profiles = [p for p in itertools.combinations_with_replacement(range(3,7),6)
                if sum(r*(r-4) for r in p)<=0]
    assert len(profiles)==14
    counts = {''.join(map(str,p)):Counter() for p in profiles}
    uncapped = Counter()
    cubic = []
    star = None
    # Directly visit each graph, rather than multiplying grouped degree counts.
    for mask in range(1 << len(EDGES)):
        neighbors = graph(mask)
        degree = tuple(map(len,neighbors))
        d2 = mask.bit_count()
        for p in profiles:
            key = ''.join(map(str,p))
            I = sum(p)
            S = sum(r*(r-2) for r in p)
            valid = []
            for d1,blocked in combined_states(tuple(sorted(zip(p,degree)))):
                unused = 3-S+d1+d2
                if unused>=0 and 18-I+d2<=2*unused+d1-blocked:
                    valid.append((d1,blocked,unused))
            if not valid:
                continue
            if key=='333333':
                uncapped[d2]+=1
                if degree==(3,1,1,1,0,0):
                    star = {'mask':mask,'degree':list(degree),'states':[list(s) for s in valid]}
            if d2>12:
                continue
            counts[key][d2]+=1
            if key=='333444':
                assert degree==(3,3,3,3,3,3)
                assert valid==[(24,24,3)]
                cubic.append({'mask':mask,**cubic_certificate(neighbors)})
    survivors = {k:dict(sorted(v.items())) for k,v in counts.items() if v}
    assert survivors==EXPECTED,(survivors,EXPECTED)
    assert star is not None and [12,7,0] in star['states']
    classes = Counter(x['class'] for x in cubic)
    assert classes=={'K3_3':10,'TRIANGULAR_PRISM':60}
    return {
        'record_id':'OM26-H1-Q6-INTERNAL-REPLAY-001',
        'producer':'CURRENT_CONTEXT_GCL_INTERNAL_EXECUTOR',
        'independent_zero_context_return':False,
        'source_solve_commit':'99757ce4a816a2f845609d74d31fc0f86a7355a2',
        'source_task':'handoffs/OPENMATH-2026/launch/OM26-H1-WP02.md',
        'replay_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'labeled_graphs_visited':1 << len(EDGES),
        'coarse_profiles':[''.join(map(str,p)) for p in profiles],
        'counts_with_euler_bound':survivors,
        'all_triple_without_euler_bound':dict(sorted(uncapped.items())),
        'all_triple_star':star,
        'profile_333444':{'local_totals':{'D1':24,'B':24,'U':3},
                          'graph_classes':dict(classes),'certificates':cubic,
                          'planar_graph_candidates_remaining':60},
        'unresolved':['six-core clean-line charging map validity',
                      'six-core no-long-run local fan validity',
                      'global opposite-ray matching and straight-line realizability',
                      'all other surviving profiles and q>=7'],
        'claim_boundary':'Exact finite replay of the declared necessary-state relaxation; K3,3 graph candidates excluded by planarity. No geometric realization, unconditional score bound, independent Cert disposition, external-agent lease consumption or competition submission.',
    }

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--verify-receipt',type=Path)
    args=parser.parse_args()
    receipt=replay()
    if args.verify_receipt:
        assert json.loads(json.dumps(receipt))==json.loads(args.verify_receipt.read_text()),'Stored replay receipt differs'
    print(json.dumps(receipt,indent=2,sort_keys=True))

if __name__=='__main__':
    main()
