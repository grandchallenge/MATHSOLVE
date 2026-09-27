#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path

def sign_correction(n,row,l1,l2):
    a=l1+n if l1<row else l1
    b=l2+n if l2<row else l2
    s=1 if l1>l2 else -1
    if a<b: s*=-1
    return s

def f_raw(li,lj,lk):
    ai,bi,ci=li; aj,bj,cj=lj; ak,bk,ck=lk
    return (
        ci*(bk*aj-ak*bj)
        + cj*(bi*ak-ai*bk)
        + ck*(bj*ai-aj*bi)
    )

def proportional(x,y):
    a,b,c=x; d,e,f=y
    return a*e==d*b and a*f==d*c and b*f==e*c

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("table",type=Path)
    ap.add_argument("solution",type=Path)
    args=ap.parse_args()
    src=json.loads(args.table.read_text())
    sol=json.loads(args.solution.read_text())
    rows=src["rows"]; lines=[tuple(x) for x in sol["lines"]]; n=len(lines)
    if n!=src["lines"]: raise SystemExit(f"line-count drift: {n}")
    failures=[]; checked=0; margins=[]
    for i,row in enumerate(rows):
        missing=set(range(1,n+1))-{i+1}-set(row)
        for j in missing:
            if not proportional(lines[i],lines[j-1]):
                failures.append({"kind":"expected_parallel","line":i+1,"other":j})
        for m in range(len(row)-1):
            j=row[m]-1; k=row[m+1]-1
            val=sign_correction(n,i+1,j+1,k+1)*f_raw(lines[i],lines[j],lines[k])
            checked+=1; margins.append(-val)
            if val>=0:
                failures.append({"kind":"order","row":i+1,"left":j+1,"right":k+1,"signed_f":val})
    report={
      "passed":not failures,
      "adjacency_constraints_checked":checked,
      "minimum_positive_integer_margin":min(margins) if margins else None,
      "parallel_pairs":src["parallel_pairs"],
      "failures":failures
    }
    print(json.dumps(report,indent=2,sort_keys=True))
    if failures: raise SystemExit(1)
if __name__=="__main__": main()
