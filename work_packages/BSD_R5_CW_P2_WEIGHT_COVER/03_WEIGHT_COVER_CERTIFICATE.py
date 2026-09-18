#!/usr/bin/env python3
from __future__ import annotations
import json

def units_mod(n, congruence):
    m=1<<n
    r,mod=congruence
    return {x for x in range(1,m,2) if x%mod==r%mod}

def main():
    rows=[]
    for n in range(4,13):
        m=1<<n
        gamma=units_mod(n,(1,4))
        target=units_mod(n,(1,8))
        image={x*x % m for x in gamma}
        if image != target:
            raise SystemExit(f"square image mismatch n={n}")
        fibers={y:0 for y in target}
        for x in gamma:
            fibers[x*x % m]+=1
        if set(fibers.values())!={2}:
            raise SystemExit(f"unexpected finite-level fiber size n={n}")
        rows.append({"n":n,"gamma":len(gamma),"image":len(image),"fiber":2})

    # Closed-point special fibre of Y^2-(1+T): with S=Y-1,
    # the structure map is T -> S^2 in characteristic two.
    # This guardrail records the ramified, non-etale reduction.
    print(json.dumps({
        "status":"PASS",
        "operation":"BSD-R5-CW-P2-WEIGHT",
        "finite_level_square_images":rows,
        "structure_map":"T->2S+S^2",
        "special_fibre":"T->S^2",
        "finite_free_rank":2,
        "candidate_disposition":"CLOSED",
        "next_frontier":"MISSING_P2_COLMEZ_WANG_SQUARE_ROOT_COVER_CHAPTER15_GLOBALIZATION_COMPATIBILITY",
        "r5_res":False,
        "r5_prim":False,
        "bsd_r2_a1":False,
        "mathcert_certification":False,
    },sort_keys=True))

if __name__=="__main__":
    main()
