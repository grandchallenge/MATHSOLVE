#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,random
from pathlib import Path
import kobon_scorer

ROOT=Path(__file__).resolve().parent
def baseline_lines(): return [(2*i,-1,-(i*i)) for i in range(18)]
def score(lines):
    if len(set(lines))!=len(lines): return -1
    return kobon_scorer.score(lines)["triangles"]

def route_d(iterations=3000,seed=3):
    rng=random.Random(seed); current=baseline_lines(); current_score=score(current)
    best_lines=list(current); best_score=current_score; ladder=[{"iteration":-1,"triangles":current_score}]
    for iteration in range(iterations):
        candidate=[list(line) for line in current]; idx=rng.randrange(18)
        if rng.random()<0.8:
            da=rng.choice([-3,-2,-1,1,2,3]); dc=rng.randint(-20,20)
        else:
            da=rng.randint(-10,10); dc=rng.randint(-100,100)
        candidate[idx][0]+=da; candidate[idx][2]+=dc; candidate=[tuple(x) for x in candidate]
        s=score(candidate)
        if s<0: continue
        if s>=current_score or rng.random()<0.01: current,current_score=candidate,s
        if s>best_score:
            best_score=s; best_lines=candidate; ladder.append({"iteration":iteration,"triangles":s})
    return {"route":"R-D","seed":seed,"iterations":iterations,"triangles":best_score,"lines":[list(x) for x in best_lines],"ladder":ladder}

def structured(alpha,beta):
    return [(2*i,-1,-(i*i)+alpha*((-1)**i)*i+beta*((i%3)-1)) for i in range(18)]

def route_g():
    best=None; evaluated=0
    for alpha in range(-12,13):
        for beta in range(-20,21,2):
            lines=structured(alpha,beta); s=score(lines); evaluated+=1
            if best is None or s>best["triangles"]:
                best={"route":"R-G","alpha":alpha,"beta":beta,"triangles":s,"lines":[list(x) for x in lines]}
    best["evaluated"]=evaluated; return best

def load(path): return json.loads(path.read_text(encoding="utf-8"))["lines"]
def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--verify-committed",action="store_true"); ap.add_argument("--output",type=Path,default=None); args=ap.parse_args()
    rd=route_d(); rg=route_g()
    if rd["triangles"]!=86: raise SystemExit(f"R-D replay drift: {rd['triangles']} != 86")
    if rg["triangles"]!=58: raise SystemExit(f"R-G replay drift: {rg['triangles']} != 58")
    if args.verify_committed:
        if rd["lines"]!=load(ROOT/"candidates/RD_LOCAL_MUTATION_086/solution.json"): raise SystemExit("R-D committed candidate drift")
        if rg["lines"]!=load(ROOT/"candidates/RG_STRUCTURED_FAMILY_058/solution.json"): raise SystemExit("R-G committed candidate drift")
    report={"schema_version":"1.0.0","baseline_triangles":16,"routes":[{k:v for k,v in rd.items() if k!="lines"},{k:v for k,v in rg.items() if k!="lines"}],"claim_boundary":"Proposal-generator scores require H1-07 independent replay before promotion."}
    rendered=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(rendered,encoding="utf-8")
    print(rendered,end="")
if __name__=="__main__": main()
