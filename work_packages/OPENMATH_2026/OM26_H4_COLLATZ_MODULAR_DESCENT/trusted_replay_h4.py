#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CANDIDATE = ROOT / "work_packages/OPENMATH_2026/CONTEST_CANDIDATES/H4/solution.json"

def v2(n:int)->int:
    if n <= 0:
        raise ValueError("v2 domain")
    return (n & -n).bit_length()-1

def trajectory_check(k:int,r:int,es:tuple[int,...]):
    if not (2 <= k <= 32 and 0 < r < 2**k and r & 1 and 1 <= len(es) <= 24):
        return None
    if any(not (1 <= e <= 32) for e in es):
        return None
    if k < 1 + sum(es):
        return None
    x=r
    trace=[]
    for e in es:
        z=3*x+1
        if v2(z)!=e:
            return None
        x=z//(2**e)
        trace.append(x)
    E=sum(es); s=len(es)
    if not (3**s < 2**E and x < r):
        return None
    return x, tuple(trace), Fraction(2**E-3**s,2**E)

def affine_check(k:int,r:int,es:tuple[int,...]):
    if k < 1 + sum(es):
        return None
    A,B,D=1,0,1
    x=r
    for e in es:
        z=3*x+1
        if v2(z)!=e:
            return None
        x=z//(2**e)
        A,B,D=3*A,3*B+D,D*(2**e)
    if D*x != A*r+B:
        raise AssertionError("affine identity")
    if not (A < D and B < (D-A)*r):
        return None
    # This is the exact all-members proof. For n=r+t*2^k:
    # C^s(n)-C^s(r)=3^s*t*2^(k-E), and k>=E+1 preserves every valuation.
    return (A,B,D,x,Fraction(D-A,D))

def enumerate_valid():
    valid=[]
    for k in range(2,9):
        for r in range(1,2**k,2):
            x=r
            es=[]
            for _depth in range(1,5):
                z=3*x+1
                e=v2(z)
                x=z//(2**e)
                es.append(e)
                t=trajectory_check(k,r,tuple(es))
                a=affine_check(k,r,tuple(es))
                if (t is None)!=(a is None):
                    raise AssertionError(("implementation disagreement",k,r,tuple(es),t,a))
                if t is not None:
                    valid.append((k,r,tuple(es)))
    return valid

def reduce_catalog(valid):
    def margin(t):
        k,r,es=t
        return affine_check(k,r,es)[4]
    ordered=sorted(valid,key=lambda t:(t[0],len(t[2]),-margin(t),t[1],t[2]))
    selected=[]
    for t in ordered:
        k,r,_=t
        if not any(k>=qk and r%(2**qk)==qr for qk,qr,_ in selected):
            selected.append(t)
    return sorted(selected)

def main():
    data=json.loads(CANDIDATE.read_text())
    candidate=[(x["modulus_power"],x["residue"],tuple(x["exponents"])) for x in data["rules"]]
    if len(candidate)!=len(set(candidate)):
        raise AssertionError("duplicate candidate rule")
    for rule in candidate:
        if trajectory_check(*rule) is None or affine_check(*rule) is None:
            raise AssertionError(("invalid candidate rule",rule))

    valid=enumerate_valid()
    selected=reduce_catalog(valid)
    if selected != sorted(candidate):
        raise AssertionError({"catalog_mismatch":{"expected":selected,"candidate":sorted(candidate)}})

    raw=json.dumps([[k,r,list(es)] for k,r,es in valid],separators=(",",":"))
    digest=hashlib.sha256(raw.encode()).hexdigest()
    coverage_union_weight=sum(2**(-k) for k,_,_ in selected)
    out={
      "state":"PASS",
      "candidate_rules":len(candidate),
      "bounded_prefixes_checked":sum((2**(k-1))*4 for k in range(2,9)),
      "valid_bounded_rules":len(valid),
      "selected_catalog_rules":len(selected),
      "catalog_exact_match":True,
      "dual_implementation_concordance":True,
      "full_catalog_sha256":digest,
      "expected_catalog_sha256":"951521f5064f0842993e895648b2b8bde2b29dda0d47c9d586ddac498bfa4f55",
      "claim":"Each retained rule is an exact stable accelerated-Collatz residue-class descent certificate; the 23-rule payload is exactly the deterministic reduction of the independently reconstructed k<=8, depth<=4 valid catalog.",
      "boundary":"No claim of Collatz convergence, hidden-target coverage, novelty, organizer score, or competition acceptance."
    }
    if digest != out["expected_catalog_sha256"]:
        raise AssertionError(("catalog digest drift",digest))
    print(json.dumps(out,indent=2,sort_keys=True))

if __name__=="__main__":
    main()
