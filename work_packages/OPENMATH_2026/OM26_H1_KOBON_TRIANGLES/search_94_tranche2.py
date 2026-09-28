#!/usr/bin/env python3
"""H1-13 tranche 2: exact coordinated two-line wall search.

Proposal generation reuses the exact integer wall machinery from tranche 1.
Promotion still requires the independent direct oracle and AutoLab replay.
"""
from __future__ import annotations
import argparse, json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

import search_94_coordinate_sweep as wall

ROOT=Path(__file__).resolve().parent

def load(path):
    return wall.load_solution(path)

def one_line_frontier(start, keep_per_line):
    frontier=defaultdict(list)
    evaluated=0
    for i in range(len(start)):
        seen=set()
        for coeff in (2,0,1):
            current=Fraction(start[i][coeff])
            crit=wall.critical_values(start,i,coeff)
            for value in wall.samples(crit,current):
                line=wall.materialize(start[i],coeff,value)
                if line is None or line==start[i] or line in seen:
                    continue
                seen.add(line)
                cand=list(start); cand[i]=line
                if len(set(cand))!=len(cand):
                    continue
                score=wall.exact_score(cand); evaluated+=1
                frontier[i].append((score,line,coeff,value))
        frontier[i].sort(key=lambda x:(x[0],x[1]), reverse=True)
        frontier[i]=frontier[i][:keep_per_line]
    return frontier,evaluated

def coordinated_pairs(start, frontier):
    best_score=wall.exact_score(start)
    best=list(start)
    best_move=None
    evaluated=0
    hist=defaultdict(int)
    for i in range(len(start)):
        for j in range(i+1,len(start)):
            for si,li,ci,vi in frontier[i]:
                for sj,lj,cj,vj in frontier[j]:
                    cand=list(start); cand[i]=li; cand[j]=lj
                    if len(set(cand))!=len(cand):
                        continue
                    score=wall.exact_score(cand); evaluated+=1; hist[score]+=1
                    if score>best_score:
                        best_score=score; best=cand
                        best_move={
                          "line_i":i,"line_j":j,
                          "seed_score_i":si,"seed_score_j":sj,
                          "coefficient_i":ci,"coefficient_j":cj,
                          "value_i":[vi.numerator,vi.denominator],
                          "value_j":[vj.numerator,vj.denominator],
                        }
                    if best_score>=94:
                        return best_score,best,best_move,evaluated,hist
    return best_score,best,best_move,evaluated,hist

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--start",type=Path,default=ROOT/"candidates/RH_BADER_RECONSTRUCTION_093/solution.json")
    ap.add_argument("--keep-per-line",type=int,default=6)
    ap.add_argument("--report",type=Path,default=Path("/tmp/kobon94-tranche2.json"))
    ap.add_argument("--candidate-dir",type=Path,default=Path("/tmp/kobon94-tranche2-candidate"))
    args=ap.parse_args()

    start=load(args.start)
    start_score=wall.exact_score(start)
    if start_score!=93:
        raise SystemExit(f"start score drift: {start_score}")

    frontier,one_eval=one_line_frontier(start,args.keep_per_line)
    best_score,best,best_move,pair_eval,hist=coordinated_pairs(start,frontier)

    report={
      "schema_version":"1.0.0",
      "route":"H1-13-TRANCHE2",
      "method":"coordinated two-line combinations of exact one-line wall-frontier moves",
      "start_score":start_score,
      "keep_per_line":args.keep_per_line,
      "frontier_sizes":{str(k):len(v) for k,v in frontier.items()},
      "one_line_candidates_rescored":one_eval,
      "coordinated_pair_candidates_evaluated":pair_eval,
      "best_score":best_score,
      "best_move":best_move,
      "score_histogram":{str(k):v for k,v in sorted(hist.items())},
      "found_94_or_better":best_score>=94,
      "claim_boundary":"Bounded exact proposal search. Search failure is not an upper bound. A found candidate requires independent direct-oracle and AutoLab replay before promotion."
    }
    args.report.write_text(json.dumps(report,indent=2,sort_keys=True)+"\n")
    print(json.dumps(report,indent=2,sort_keys=True))
    if best_score>=94:
        args.candidate_dir.mkdir(parents=True,exist_ok=True)
        (args.candidate_dir/"solution.json").write_text(json.dumps({"lines":[list(x) for x in best]})+"\n")
        print("H1_13_TRANCHE2_FOUND=true")
    else:
        print("H1_13_TRANCHE2_FOUND=false")

if __name__=="__main__":
    main()
