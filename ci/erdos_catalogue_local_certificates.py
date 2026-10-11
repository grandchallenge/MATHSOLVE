#!/usr/bin/env python3
"""Bounded, exact-arithmetic Erdős catalogue witness replays.

This is independent deterministic arithmetic verification, NOT a Lean kernel
proof, primary-paper referee review, or authority for new Solve dispatches.
"""
from __future__ import annotations
import argparse
from hashlib import sha256
from itertools import combinations_with_replacement, product
from math import gcd, isqrt, lcm

EXPECTED_009 = "a6a8724d608717823af0703a033000e9170d1bf49058f80bb757e69f7f6fc464"
EXPECTED_010 = "a57128e0c303e60e159000f5896751864f6683ae339989b55bb89475c3cee37a"
N010 = 1117175146


def primes_up_to(n: int) -> bytearray:
    a = bytearray(b"\x01") * (n+1)
    a[:2] = b"\x00\x00"
    for p in range(2, isqrt(n)+1):
        if a[p]:
            a[p*p:n+1:p] = b"\x00" * ((n-p*p)//p+1)
    return a


def smallest_factor(n: int) -> int | None:
    if n < 2:
        raise ValueError("not an integer >=2")
    if not n % 2:
        return 2 if n>2 else None
    for f in range(3, isqrt(n)+1, 2):
        if n % f == 0:
            return f
    return None


def check_007() -> dict:
    def uncovered(moduli, residues):
        if len(moduli) != len(residues) or not moduli:
            raise ValueError("nonempty paired covering family required")
        if any(m < 2 or not (0 <= a < m) for a,m in zip(residues,moduli)):
            raise ValueError("invalid congruence")
        span = lcm(*moduli)
        return [r for r in range(span) if all((r-a)%m for m,a in zip(moduli,residues))]
    odd_m = [3,5,7]
    u = uncovered(odd_m,[0,1,2])
    assert len(u) == (3-1)*(5-1)*(7-1) == 48
    assert 4 in u
    assert len(uncovered([2,3,4,6,12],[0,0,1,5,7])) == 0
    # For all residue selections the pairwise-coprime CRT obstruction agrees
    # with exact finite coverage, including overlapping residue choices.
    for a,b,c in product(range(3),range(5),range(7)):
        assert len(uncovered(odd_m,[a,b,c])) == 48
    return {"status":"PASS","odd_uncovered":48,"nonodd_control_uncovered":0,
            "crt_residue_assignments_checked":105}


def check_009() -> dict:
    limit = 200000
    prime = primes_up_to(limit)
    powers = [1<<i for i in range(18)]
    rows = []
    for n in range(5,limit,2):
        # Lexicographic k then l, 0<=k<=l; all possible exponent pairs
        # with summand < n are covered by 0..17 because 2^18 > 200000.
        witness = next(((n-powers[k]-powers[l],k,l)
                        for k in range(18) for l in range(k,18)
                        if n-powers[k]-powers[l] >= 2 and
                        prime[n-powers[k]-powers[l]]),None)
        assert witness is not None, f"missing witness for n={n}"
        p,k,l = witness
        assert p + (1<<k) + (1<<l) == n and prime[p]
        rows.append(f"{n},{p},{k},{l}\n")
    digest = sha256("".join(rows).encode("ascii")).hexdigest()
    assert len(rows) == 99998 and digest == EXPECTED_009
    # Minimal n excludes 1 and 3; 5=3+1+1 is a positive control.
    assert rows[0] == "5,3,0,0\n"
    return {"status":"PASS","rows":len(rows),"sha256":digest,"boundary_first":rows[0].strip()}


def check_010() -> dict:
    # Exactly one-to-three powers of 2 must have ODD sum when n is EVEN
    # and the candidate prime is odd. Every such sum has one 1=2^0
    # after carrying, or has three 1s (sum=3).
    max_power = N010.bit_length()
    offsets = set()
    for k in range(1,4):
        for exps in combinations_with_replacement(range(max_power),k):
            x = sum(1<<e for e in exps)
            if x%2 and x <= N010-3:
                offsets.add(x)
    rows = []
    for x in sorted(offsets):
        p = N010-x
        d = smallest_factor(p)
        assert d is not None and 1 < d < p and p % d == 0
        rows.append(f"{x},{p},{d}\n")
    digest = sha256("".join(rows).encode("ascii")).hexdigest()
    assert len(rows) == 462 and digest == EXPECTED_010
    assert (N010-2).bit_count() > 3  # Handles the even prime p=2.
    prime4 = 1117175107
    assert N010-prime4 == (1+2+4+32) and smallest_factor(prime4) is None
    return {"status":"PASS","offsets":len(rows),"sha256":digest,
            "minimal_power_count_for_fixed_n":4}


def check_138() -> dict:
    colours = "001001122"
    ap = [(a,a+d,a+2*d) for a in range(9) for d in range(1,9) if a+2*d<9]
    assert len(ap) == 16
    assert not any(colours[a]==colours[b]==colours[c] for a,b,c in ap)
    # Every map from three colour labels to two may merge arbitrarily;
    # all eight maps have a monochromatic 3-AP.
    witness_counts=[]
    for mask in range(8):
        w = [((mask >> int(ch)) & 1) for ch in colours]
        witness_counts.append(sum(w[a]==w[b]==w[c] for a,b,c in ap))
    assert min(witness_counts) > 0
    return {"status":"PASS","three_colour_ap":0,
            "binary_relabellings":8,"min_relabelled_monochromatic_ap":min(witness_counts)}


def check_241() -> dict:
    # Independent finite boundary check for sharp no-wrap modulus:
    # integer strong B3 iff modular strong B3 if M>=3N-2.
    from itertools import combinations
    def strong(A, modulus=None):
        sums = {}
        for abc in combinations_with_replacement(A,3):
            s=sum(abc)
            if modulus is not None:s%=modulus
            if s in sums and sums[s]!=abc:
                return False
            sums[s]=abc
        return True
    cases=0
    for n in range(2,10):
        for bits in range(1<<n):
            A=[i+1 for i in range(n) if bits & (1<<i)]
            assert strong(A)==strong(A,3*n-2)
            cases+=1
        assert strong([1,n]) and not strong([1,n],3*n-3)
    return {"status":"PASS","exhaustive_sets":cases,"sharp_boundary_n":list(range(2,10))}


def verify():
    return {"ERDOS-007":check_007(),"ERDOS-009":check_009(),
            "ERDOS-010":check_010(),"ERDOS-138":check_138(),
            "ERDOS-241":check_241()}


if __name__=="__main__":
    import json
    parser=argparse.ArgumentParser()
    parser.add_argument("--check",action="store_true")
    args=parser.parse_args()
    print(json.dumps(verify(),sort_keys=True,indent=2))
