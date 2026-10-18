#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from collections import Counter
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
PROPOSAL = HERE / "H4_EXTENDED_107_PROPOSED_SOLUTION.json"
EXPECTED_VALID_SHA = "65a215b170d65d7c8f66e14117cab7c7b4a3cdc8802a7a677898163c1c8adab3"
EXPECTED_PROPOSAL_SHA = "5dfcd9fb0f691cc8892c9782f3d26c6c008043c43bca54118c37baa7305873ba"

def v2(n):
    if n <= 0: raise ValueError(n)
    return (n & -n).bit_length() - 1

def rule(k, r, es):
    x=r; A=1; B=0; D=1
    for e in es:
        z=3*x+1
        if v2(z) != e: return None
        x=z >> e
        A,B,D=3*A,3*B+D,D*(1<<e)
    if D*x != A*r+B: raise AssertionError("affine identity")
    valid = k >= sum(es)+1 and A < D and B < (D-A)*r
    return {"k":k,"r":r,"es":tuple(es),"margin":Fraction(D-A,D),"valid":valid}

def enumerate_valid(kmax=12, depthmax=8):
    valid=[]
    prefixes=0
    for k in range(2,kmax+1):
        for r in range(1,1<<k,2):
            x=r; es=[]
            for _ in range(depthmax):
                e=v2(3*x+1); x=(3*x+1)>>e; es.append(e); prefixes += 1
                p=rule(k,r,tuple(es))
                if p and p["valid"]: valid.append(p)
    return prefixes,valid

def valid_digest(valid):
    arr=[[p["k"],p["r"],list(p["es"])] for p in sorted(valid,key=lambda p:(p["k"],p["r"],len(p["es"]),p["es"]))]
    return hashlib.sha256(json.dumps(arr,separators=(",",":")).encode()).hexdigest()

def maximal_coverage_nodes(valid):
    ordered=sorted(valid,key=lambda p:(p["k"],len(p["es"]),-p["margin"],p["r"],p["es"]))
    out=[]
    for p in ordered:
        if not any(p["k"]>=q["k"] and p["r"]%(1<<q["k"])==q["r"] for q in out):
            out.append(p)
    return sorted({(p["k"],p["r"]) for p in out})

def target_envelope(rules):
    env={}
    for K in range(8,13):
        for R in range(1,1<<K,2):
            ms=[p["margin"] for p in rules if p["k"]<=K and R%(1<<p["k"])==p["r"]]
            if ms: env[(K,R)] = max(ms)
    return env

def main():
    prefixes,valid=enumerate_valid()
    assert prefixes == 32752
    assert len(valid) == 10641
    assert valid_digest(valid) == EXPECTED_VALID_SHA

    raw=PROPOSAL.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == EXPECTED_PROPOSAL_SHA
    data=json.loads(raw)
    parsed=[]
    for item in data["rules"]:
        p=rule(item["modulus_power"],item["residue"],tuple(item["exponents"]))
        assert p and p["valid"]
        parsed.append(p)
    assert len(parsed)==107 and len({(p["k"],p["r"],p["es"]) for p in parsed})==107

    nodes=maximal_coverage_nodes(valid)
    assert len(nodes)==107
    assert sorted((p["k"],p["r"]) for p in parsed)==nodes

    by_node={}
    for p in valid:
        by_node.setdefault((p["k"],p["r"]),[]).append(p)
    for p in parsed:
        assert p["margin"] == max(q["margin"] for q in by_node[(p["k"],p["r"])])

    full=target_envelope(valid)
    prop=target_envelope(parsed)
    assert set(prop)==set(full)
    assert len(full)==3352
    assert Counter(K for K,_ in full)==Counter({8:94,9:203,10:421,11:869,12:1765})
    assert min(full.values())==Fraction(13,256)
    assert min(prop.values())==Fraction(13,256)
    assert sum(v==Fraction(13,256) for v in full.values())==77

    print(json.dumps({
      "state":"PASS",
      "prefixes_checked":prefixes,
      "valid_rules":len(valid),
      "valid_catalog_sha256":EXPECTED_VALID_SHA,
      "selected_rules":len(parsed),
      "proposal_sha256":EXPECTED_PROPOSAL_SHA,
      "reachable_public_target_classes":len(full),
      "reachable_by_power":dict(sorted(Counter(K for K,_ in full).items())),
      "robust_min_margin":[13,256],
      "unavoidable_min_margin_targets_in_full_catalog":77,
      "selection_policy":"one maximum-margin certificate on every maximal coverage residue class",
      "claim_boundary":"Finite exact replay only; no hidden-target score, organizer acceptance, novelty, or competition submission."
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
