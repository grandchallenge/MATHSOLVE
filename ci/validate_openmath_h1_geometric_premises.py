#!/usr/bin/env python3
"""Exact geometric evidence for the fan and clean-line premises; no Cert effect."""
from __future__ import annotations
import hashlib
import importlib.util
import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PACKET=ROOT/'work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES'
spec=importlib.util.spec_from_file_location('h1_direct_geometry',PACKET/'kobon_direct_oracle.py')
oracle=importlib.util.module_from_spec(spec)
spec.loader.exec_module(oracle)

def through(p,q):
    a=p[1]-q[1]; b=q[0]-p[0]; c=p[0]*q[1]-q[0]*p[1]
    return oracle._normalize(a,b,c)

def fixture(multiplicities,seed):
    centers=[(0,0),(31,2),(8,37),(9,10),(19,12),(13,23)]
    edges=[(0,1),(1,2),(2,0),(3,4),(4,5),(5,3),(0,3),(1,4),(2,5)]
    lines=[through(centers[a],centers[b]) for a,b in edges]
    assert len(set(lines))==9
    for a,b in itertools.combinations(lines,2):assert a[0]*b[1]!=b[0]*a[1]
    def allowed(candidate):
        if candidate in lines:return False
        if any(candidate[0]*b-candidate[1]*a==0 for a,b,_ in lines):return False
        for i,j in itertools.combinations(range(len(lines)),2):
            point=oracle.intersect(lines[i],lines[j])
            if oracle._value(candidate,point)==0 and point not in centers:return False
        return True
    cursor=seed+41
    for index,mult in enumerate(multiplicities):
        assert mult>=3
        for _ in range(mult-3):
            while True:
                cursor+=1
                x,y=centers[index]
                candidate=oracle._normalize(cursor,1,-cursor*x-y)
                if allowed(candidate):break
            lines.append(candidate)
    while len(lines)<18:
        cursor+=1
        candidate=oracle._normalize(cursor,1,-(cursor*cursor+17*seed+3))
        if any(oracle._value(candidate,p)==0 for p in centers):continue
        if allowed(candidate):lines.append(candidate)
    assert len(lines)==18
    return lines

def audit(lines):
    # Vertices and elementary segments are reconstructed directly from exact data.
    vertex_lines={}
    per_line=[set() for _ in lines]
    for i,j in itertools.combinations(range(len(lines)),2):
        p=oracle.intersect(lines[i],lines[j])
        assert p is not None,'This profile requires pairwise nonparallel lines'
        vertex_lines.setdefault(p,set()).update((i,j))
        per_line[i].add(p);per_line[j].add(p)
    core={p for p,inc in vertex_lines.items() if len(inc)>=3}
    segments={}
    incident={p:[] for p in vertex_lines}
    for i,points in enumerate(per_line):
        ordered=sorted(points)
        for p,q in zip(ordered,ordered[1:]):
            key=(i,p,q)
            segments[key]=0
            incident[p].append(key);incident[q].append(key)
    faces=oracle.direct_faces(lines)
    for i,j,k in faces:
        points=[oracle.intersect(lines[i],lines[j]),oracle.intersect(lines[j],lines[k]),oracle.intersect(lines[k],lines[i])]
        for line,p,q in [(j,points[0],points[1]),(k,points[1],points[2]),(i,points[2],points[0])]:
            p,q=sorted((p,q));segments[(line,p,q)]+=1
    assert all(u<=2 for u in segments.values())
    h=sum(any(p in core for p in ps) for ps in per_line)
    clean=[i for i,ps in enumerate(per_line) if not any(p in core for p in ps)]
    unused=[k for k,u in segments.items() if u==0]
    d1=[k for k,u in segments.items() if u==2 and sum(p in core for p in k[1:])==1]
    d2=[k for k,u in segments.items() if u==2 and all(p in core for p in k[1:])]
    assert len(d1)+len(d2)==sum(u==2 for u in segments.values())
    S=sum(len(vertex_lines[p])*(len(vertex_lines[p])-2) for p in core)
    delta=len(lines)*(len(lines)-2)-3*len(faces)
    assert delta==S+len(unused)-len(d1)-len(d2)
    blocked=set()
    fan=[]
    # Exact angular sorting by half-plane and cross product, no atan/tolerance.
    from functools import cmp_to_key
    def direction_cmp(a,b):
        x,y=a[0];u,v=b[0]
        side=lambda x,y:0 if y>0 or (y==0 and x>0) else 1
        if side(x,y)!=side(u,v):return -1 if side(x,y)<side(u,v) else 1
        cross=x*v-y*u
        return -1 if cross>0 else 1 if cross<0 else 0
    for center in sorted(core):
        r=len(vertex_lines[center]);rays=[]
        for line in sorted(vertex_lines[center]):
            a,b,_=lines[line]
            for direction in [(b,-a),(-b,a)]:
                target=None
                for key in incident[center]:
                    if key[0]!=line:continue
                    other=key[1] if key[2]==center else key[2]
                    vector=(other[0]-center[0],other[1]-center[1])
                    if vector[0]*direction[0]+vector[1]*direction[1]>0:target=key
                label=1 if target in d1 else 2 if target in d2 else 0
                rays.append((direction,label,target))
        rays.sort(key=cmp_to_key(direction_cmp))
        word=[x[1] for x in rays]
        assert all(not all(word[(i+j)%(2*r)]==1 for j in range(r-1)) for i in range(2*r))
        for i,(_,label,key) in enumerate(rays):
            if label==1 and (word[i-1]==2 or word[(i+1)%(2*r)]==2):blocked.add(key)
        fan.append({'multiplicity':r,'word':word})
    charges=[]
    for clean_line in clean:
        choices=[]
        for point in per_line[clean_line]:
            assert len(vertex_lines[point])==2
            for key in incident[point]:
                if key[0]!=clean_line and segments[key] in (0,2):choices.append((point,key))
        assert choices,'Clean line lacks a chargeable transverse elementary segment'
        point,key=min(choices)
        assert key not in blocked
        charges.append((clean_line,point,key))
    loads={}
    for _,point,key in charges:
        loads.setdefault(key,[]).append(point)
    for key,points in loads.items():
        assert len(set(points))==len(points)
        assert len(points)<= (2 if segments[key]==0 else 1)
    assert len(clean)<=2*len(unused)+len(d1)-len(blocked)
    def point_json(p):return [str(z) for z in p]
    return {'n':len(lines),'triangles':len(faces),'q':len(core),'multiplicities':sorted(len(vertex_lines[p]) for p in core),
            'h':h,'clean_lines':len(clean),'U':len(unused),'D1':len(d1),'D2':len(d2),'blocked':len(blocked),
            'delta':delta,'fan_words':fan,
            'charges':[{'clean_line':line,'ordinary_endpoint':point_json(point),'target_line':key[0],'segment':[point_json(p) for p in key[1:]],'triangle_use':segments[key]} for line,point,key in charges]}

def replay():
    examples=[]
    for profile in [(3,3,3,3,3,3),(3,3,3,4,4,4)]:
        for seed in [0,17,83,211]:
            lines=fixture(profile,seed)
            result=audit(lines)
            assert result['q']==6 and result['multiplicities']==list(profile)
            assert result['clean_lines']==(9 if sum(profile)==18 else 6)
            examples.append({'seed':seed,'lines':[list(x) for x in lines],**result})
    return {'record_id':'OM26-H1-SIX-CORE-PREMISE-AUDIT-001',
            'source_solve_commit':'ecd9f022f51ed0ad4645ae579e79fa386c4a0cdd',
            'executor':'CURRENT_CONTEXT_INTERNAL; not independent Cert or external lease',
            'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'oracle_sha256':hashlib.sha256((PACKET/'kobon_direct_oracle.py').read_bytes()).hexdigest(),
            'examples':examples,'finite_test_result':'PASS',
            'claim_boundary':'Eight exact examples support face-to-fan extraction and charging. General validity rests on the accompanying paper proof, not test coverage. No T=95 realization, global upper bound or Cert disposition.'}

if __name__=='__main__':
    print(json.dumps(replay(),indent=2,sort_keys=True))
