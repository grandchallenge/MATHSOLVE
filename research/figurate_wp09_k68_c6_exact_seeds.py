"""FIGURATE WP09-015: exact order-68 offset-six Type B witnesses.

Five independently verifiable seeds and a complete finite entry-bounded
factor graph census; no global nonexistence claim.
"""
from __future__ import annotations
from math import isqrt

K,C=68,6
WITNESSES=(
 (10,44033,128739,116,198,13107),
 (22,13117,168855,94,336,8193),
 (55,4085,265746,83,666,5736),
 (61,55575,102610,321,436,13146),
 (102145,629950,746915,44158,48083,119408),
)

def polygonal(n:int)->int:
    if n<1:raise ValueError("positive polygonal index required")
    return 33*n*n-32*n

def exact_witness(w:tuple[int,...])->bool:
    a,b,d,r,s,t=w
    return min(w)>0 and len({a,b,d})==3 and (
        a*b+C,a*d+C,b*d+C)==(polygonal(r),polygonal(s),polygonal(t))

def primes_up_to(bound:int)->list[int]:
    sieve=bytearray(b"\x01")*(bound+1)
    sieve[:2]=b"\x00\x00"
    for p in range(2,isqrt(bound)+1):
        if sieve[p]:
            sieve[p*p::p]=b"\x00"*((bound-p*p)//p+1)
    return [p for p in range(2,bound+1) if sieve[p]]

def divisors(n:int,primes:list[int])->list[int]:
    if n<1:raise ValueError("positive integer required")
    remaining,factorization=n,[]
    for p in primes:
        if p*p>remaining:break
        if remaining%p==0:
            e=0
            while remaining%p==0:
                remaining//=p;e+=1
            factorization.append((p,e))
    if remaining>1:factorization.append((remaining,1))
    answer=[1]
    for p,e in factorization:
        previous=answer[:];q=1
        for _ in range(e):
            q*=p
            answer.extend(q*d for d in previous)
    return answer

def complete_entry_bounded_census(bound:int)->dict:
    """Exhaustive for 1<=a<b<d<=bound, 3<=bound<=100000.

    Every permitted edge is a factorization of P_68(n)-6<=bound**2,
    and every Type B triple is a graph triangle.
    """
    if not 3<=bound<=100000:
        raise ValueError("supported complete census bound is 3..100000")
    primes=primes_up_to(bound)
    adjacent:dict[int,set[int]]={}
    edge_index:dict[tuple[int,int],int]={}
    n=1
    while True:
        value=polygonal(n)-C
        if value>bound*bound:break
        if value>0:
            for a in divisors(value,primes):
                b=value//a
                if a<b<=bound:
                    adjacent.setdefault(a,set()).add(b)
                    adjacent.setdefault(b,set()).add(a)
                    edge_index[(a,b)]=n
        n+=1
    triangles=[]
    for a,near in adjacent.items():
        for b in near:
            if a<b:
                for d in near.intersection(adjacent[b]):
                    if b<d:
                        item=(a,b,d,edge_index[(a,b)],
                              edge_index[(a,d)],edge_index[(b,d)])
                        if not exact_witness(item):
                            raise ArithmeticError("graph triangle failed verification")
                        triangles.append(item)
    return dict(bound=bound,indices_examined=n-1,edges=len(edge_index),
                witnesses=sorted(triangles),global_nonexistence_proved=False)

def main():
    import argparse,json
    p=argparse.ArgumentParser()
    p.add_argument("--entry-bound",type=int,default=100000)
    args=p.parse_args()
    assert all(exact_witness(w) for w in WITNESSES)
    print(json.dumps({"witnesses":WITNESSES,
                      "census":complete_entry_bounded_census(args.entry_bound)},sort_keys=True))

if __name__=="__main__":main()
