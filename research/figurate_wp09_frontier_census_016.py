"""FIGURATE WP09-016: complete bounded Type B census for unresolved local pairs.

This enumerates all unordered positive integer Type B triples with entries
<= B, not all global integer triples. Fully exact divisor graph, no float.
"""
from __future__ import annotations
import argparse
import json
from math import isqrt

TARGETS=((84,2),(100,2))

def polygonal(k:int,n:int)->int:
    if k<3 or n<1:raise ValueError("require k>=3 and n>=1")
    return ((k-2)*n*n-(k-4)*n)//2

def primes_up_to(bound:int)->list[int]:
    sieve=bytearray(b"\x01")*(bound+1)
    sieve[:2]=b"\x00\x00"
    for p in range(2,isqrt(bound)+1):
        if sieve[p]:
            sieve[p*p::p]=b"\x00"*((bound-p*p)//p+1)
    return [p for p in range(2,bound+1) if sieve[p]]

def positive_divisors(value:int,primes:list[int])->list[int]:
    if value<=0:raise ValueError("positive integer required")
    remaining=value
    divisors=[1]
    for p in primes:
        if p*p>remaining:break
        if remaining%p==0:
            power=1
            while remaining%p==0:
                remaining//=p
                power*=p
            previous=divisors[:]
            q=p
            while q<=power:
                divisors.extend(q*d for d in previous)
                q*=p
    if remaining>1:
        divisors.extend(remaining*d for d in divisors[:])
    return divisors

def complete_census(k:int,c:int,bound:int)->dict:
    """Complete for 1<=a<b<d<=bound; never infer global absence."""
    if (k,c) not in TARGETS or not 3<=bound<=300000:
        raise ValueError("supported (k,c) and entry bound 3..300000 required")
    primes=primes_up_to(bound)
    adjacency:dict[int,set[int]]={}
    index:dict[tuple[int,int],int]={}
    n=1
    while True:
        product=polygonal(k,n)-c
        if product>bound*bound:break
        if product>0:
            for a in positive_divisors(product,primes):
                b=product//a
                if a<b<=bound:
                    adjacency.setdefault(a,set()).add(b)
                    adjacency.setdefault(b,set()).add(a)
                    index[a,b]=n
        n+=1
    triples=[]
    for a,near in adjacency.items():
        for b in near:
            if a<b:
                for d in near.intersection(adjacency[b]):
                    if b<d:
                        r,s,t=index[a,b],index[a,d],index[b,d]
                        if (a*b+c,a*d+c,b*d+c)!=(polygonal(k,r),
                                                 polygonal(k,s),
                                                 polygonal(k,t)):
                            raise ArithmeticError("non-exact graph witness")
                        triples.append((a,b,d,r,s,t))
    triples.sort()
    return {"order":k,"offset":c,"entry_bound":bound,
            "max_polygonal_index_examined":n-1,
            "edge_count":len(index),"triangle_count":len(triples),
            "exact_triples":triples,
            "global_nonexistence_proved":False}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--entry-bound",type=int,default=300000)
    p.add_argument("--order",type=int,choices=(84,100),default=84)
    args=p.parse_args()
    print(json.dumps(complete_census(args.order,2,args.entry_bound),
                     sort_keys=True))
if __name__=="__main__":main()
