#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, math
from fractions import Fraction
from itertools import combinations
from pathlib import Path

MAX_BYTES=65536
MAX_COEFF=10**30

class OracleInputError(ValueError): pass

def _pairs_unique(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise OracleInputError(f"duplicate JSON key: {k}")
        out[k]=v
    return out

def _bad_float(text): raise OracleInputError(f"floating-point JSON number is invalid: {text}")
def _bad_constant(text): raise OracleInputError(f"non-finite JSON constant is invalid: {text}")

def _normalize(a,b,c):
    g=math.gcd(math.gcd(abs(a),abs(b)),abs(c))
    if g: a,b,c=a//g,b//g,c//g
    for value in (a,b,c):
        if value:
            if value<0: a,b,c=-a,-b,-c
            break
    return (a,b,c)

def load_lines(path:Path, expected_n=None):
    if path.is_symlink(): raise OracleInputError("solution.json must not be a symlink")
    raw=path.read_bytes()
    if len(raw)>MAX_BYTES: raise OracleInputError("solution.json exceeds 65,536 bytes")
    try: text=raw.decode("utf-8")
    except UnicodeDecodeError as exc: raise OracleInputError("solution.json is not UTF-8") from exc
    try:
        obj=json.loads(text,object_pairs_hook=_pairs_unique,parse_float=_bad_float,parse_constant=_bad_constant)
    except (json.JSONDecodeError,OracleInputError) as exc:
        raise OracleInputError(str(exc)) from exc
    if type(obj) is not dict or set(obj)!={"lines"}: raise OracleInputError("top-level object must contain exactly 'lines'")
    triples=obj["lines"]
    if type(triples) is not list: raise OracleInputError("'lines' must be a list")
    if expected_n is not None and len(triples)!=expected_n: raise OracleInputError(f"expected {expected_n} lines, got {len(triples)}")
    if not 3<=len(triples)<=100: raise OracleInputError("line count must be in 3..100")
    lines=[]; seen=set()
    for idx,triple in enumerate(triples):
        if type(triple) is not list or len(triple)!=3: raise OracleInputError(f"lines[{idx}] must contain three values")
        if any(type(v) is not int for v in triple): raise OracleInputError(f"lines[{idx}] coefficients must be JSON integers")
        a,b,c=triple
        if max(abs(a),abs(b),abs(c))>MAX_COEFF: raise OracleInputError(f"lines[{idx}] coefficient exceeds 10^30")
        if a==0 and b==0: raise OracleInputError(f"lines[{idx}] is not a line")
        line=_normalize(a,b,c)
        if line in seen: raise OracleInputError(f"lines[{idx}] duplicates another geometric line")
        seen.add(line); lines.append(line)
    return lines,hashlib.sha256(raw).hexdigest()

def intersect(first,second):
    a,b,c=first; d,e,f=second
    det=a*e-d*b
    if det==0: return None
    return (Fraction(b*f-e*c,det),Fraction(c*d-a*f,det))

def _value(line,point):
    a,b,c=line; x,y=point
    return a*x+b*y+c

def direct_faces(lines):
    faces=[]
    for i,j,k in combinations(range(len(lines)),3):
        p=intersect(lines[i],lines[j]); q=intersect(lines[j],lines[k]); r=intersect(lines[k],lines[i])
        if p is None or q is None or r is None: continue
        vertices=(p,q,r)
        if len(set(vertices))!=3: continue
        area2=(q[0]-p[0])*(r[1]-p[1])-(q[1]-p[1])*(r[0]-p[0])
        if area2==0: continue
        crossed=False
        for idx,line in enumerate(lines):
            if idx in (i,j,k): continue
            vals=tuple(_value(line,v) for v in vertices)
            if any(v<0 for v in vals) and any(v>0 for v in vals):
                crossed=True; break
        if not crossed: faces.append((i,j,k))
    return faces

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("solution",type=Path); ap.add_argument("--n",type=int,default=None)
    ap.add_argument("--expect",type=int,default=None); ap.add_argument("--output",type=Path,default=None)
    args=ap.parse_args()
    try:
        lines,digest=load_lines(args.solution,args.n); faces=direct_faces(lines)
    except OracleInputError as exc:
        print(json.dumps({"passed":False,"reason":str(exc)},sort_keys=True)); raise SystemExit(2) from exc
    result={"passed":True,"n":len(lines),"solution_sha256":digest,"triangles":len(faces),"supporting_line_triples":[list(x) for x in faces]}
    rendered=json.dumps(result,indent=2,sort_keys=True)+"\n"
    if args.output: args.output.write_text(rendered,encoding="utf-8")
    print(rendered,end="")
    if args.expect is not None and len(faces)!=args.expect: raise SystemExit(f"expected {args.expect} triangles, got {len(faces)}")
if __name__=="__main__": main()
