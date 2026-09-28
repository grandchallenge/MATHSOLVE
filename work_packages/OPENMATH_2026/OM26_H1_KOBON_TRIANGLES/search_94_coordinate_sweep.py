#!/usr/bin/env python3
"""Bounded exact one-line wall search around the verified 93 construction.

The proposal scorer uses only integer determinant signs.  It does not call the
campaign scorer or the independent direct-oracle module.
"""
from __future__ import annotations

import argparse, json, math
from fractions import Fraction
from itertools import combinations
from pathlib import Path

ROOT=Path(__file__).resolve().parent

def det2(x,y):
    return x[0]*y[1]-x[1]*y[0]

def det3(x,y,z):
    return (
        x[0]*(y[1]*z[2]-y[2]*z[1])
        - x[1]*(y[0]*z[2]-y[2]*z[0])
        + x[2]*(y[0]*z[1]-y[1]*z[0])
    )

def sign(x):
    return (x>0)-(x<0)

def normalize(line):
    a,b,c=line
    g=math.gcd(math.gcd(abs(a),abs(b)),abs(c))
    if g: a,b,c=a//g,b//g,c//g
    for v in (a,b,c):
        if v:
            if v<0: a,b,c=-a,-b,-c
            break
    return (a,b,c)

def exact_score(lines):
    n=len(lines)
    total=0
    for i,j,k in combinations(range(n),3):
        li,lj,lk=lines[i],lines[j],lines[k]
        wij=det2(li,lj); wjk=det2(lj,lk); wki=det2(lk,li)
        if wij==0 or wjk==0 or wki==0: continue
        if det3(li,lj,lk)==0: continue
        crossed=False
        for m in range(n):
            if m in (i,j,k): continue
            lm=lines[m]
            vals=(
                sign(det3(lm,li,lj)*wij),
                sign(det3(lm,lj,lk)*wjk),
                sign(det3(lm,lk,li)*wki),
            )
            if 1 in vals and -1 in vals:
                crossed=True
                break
        if not crossed: total+=1
    return total

def intersection(j,k):
    aj,bj,cj=j; ak,bk,ck=k
    w=aj*bk-bj*ak
    if w==0: return None
    return (
        Fraction(bj*ck-cj*bk,w),
        Fraction(cj*ak-aj*ck,w),
    )

def value_for_vertex(line, coeff, point):
    a,b,c=line; x,y=point
    if coeff==0:
        if x==0: return None
        return -(b*y+c)/x
    if coeff==1:
        if y==0: return None
        return -(a*x+c)/y
    return -(a*x+b*y)

def parallel_critical(line, coeff, other):
    a,b,c=line; d,e,f=other
    if coeff==0:
        if e==0: return None
        return Fraction(b*d,e)
    if coeff==1:
        if d==0: return None
        return Fraction(a*e,d)
    return None

def materialize(line, coeff, value):
    vals=[Fraction(x) for x in line]
    vals[coeff]=value
    den=1
    for x in vals: den=math.lcm(den,x.denominator)
    out=[int(x*den) for x in vals]
    if out[0]==0 and out[1]==0: return None
    return normalize(tuple(out))

def critical_values(lines,i,coeff):
    crit=set()
    others=[x for x in range(len(lines)) if x!=i]
    for j,k in combinations(others,2):
        p=intersection(lines[j],lines[k])
        if p is None: continue
        v=value_for_vertex(lines[i],coeff,p)
        if v is not None: crit.add(v)
    if coeff in (0,1):
        for j in others:
            v=parallel_critical(lines[i],coeff,lines[j])
            if v is not None: crit.add(v)
    return sorted(crit)

def samples(crit,current):
    if not crit: return [current]
    vals=set(crit)
    vals.add(crit[0]-1); vals.add(crit[-1]+1)
    for a,b in zip(crit,crit[1:]): vals.add((a+b)/2)
    vals.add(current)
    return sorted(vals)

def load_solution(path):
    return [normalize(tuple(x)) for x in json.loads(path.read_text())["lines"]]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=Path,default=ROOT/"candidates/RH_BADER_RECONSTRUCTION_093/solution.json")
    ap.add_argument("--report",type=Path,default=Path("/tmp/kobon94-search.json"))
    ap.add_argument("--candidate-dir",type=Path,default=Path("/tmp/kobon94-candidate"))
    args=ap.parse_args()

    start=load_solution(args.start)
    start_score=exact_score(start)
    if start_score!=93: raise SystemExit(f"start score drift: {start_score}")

    best_score=start_score; best=list(start); best_move=None
    evaluated=0; score_hist={str(start_score):1}

    # One exact coordinate-wall sweep: for each line, sweep a, b, and c across
    # every event where it passes through an existing vertex, plus parallel
    # events for a/b.  Each open cell and each degenerate wall is sampled.
    for i in range(len(start)):
        for coeff in (2,0,1):
            current=Fraction(start[i][coeff])
            crit=critical_values(start,i,coeff)
            for v in samples(crit,current):
                new_line=materialize(start[i],coeff,v)
                if new_line is None: continue
                cand=list(start); cand[i]=new_line
                if len(set(cand))!=len(cand): continue
                s=exact_score(cand); evaluated+=1
                score_hist[str(s)]=score_hist.get(str(s),0)+1
                if s>best_score:
                    best_score=s; best=cand
                    best_move={"line":i,"coefficient":coeff,"value":[v.numerator,v.denominator],"critical_count":len(crit)}
                if s>=94:
                    break
            if best_score>=94: break
        if best_score>=94: break

    report={
      "schema_version":"1.0.0",
      "route":"H1-13",
      "start_score":start_score,
      "evaluated_candidates":evaluated,
      "best_score":best_score,
      "best_move":best_move,
      "score_histogram":score_hist,
      "found_94":best_score>=94,
      "claim_boundary":"Bounded proposal search only. A found candidate requires independent direct-oracle and AutoLab replay before promotion."
    }
    args.report.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))
    if best_score>=94:
        args.candidate_dir.mkdir(parents=True,exist_ok=True)
        (args.candidate_dir/"solution.json").write_text(json.dumps({"lines":[list(x) for x in best]})+"\n")
        print("H1_13_FOUND_94=true")
    else:
        print("H1_13_FOUND_94=false")

if __name__=="__main__": main()
