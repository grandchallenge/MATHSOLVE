"""FIGURATE WP09-017: exact seed-existence index/gcd descent (integer arithmetic)."""
from __future__ import annotations
from math import gcd, isqrt
import argparse,json

TARGETS=((84,2),(100,2))
CONTROL=(68,6,10,44033,128739,116,198,13107)

def polygonal(k:int,n:int)->int:
    if k<3 or n<1:raise ValueError("k>=3, n>=1")
    return ((k-2)*n*n-(k-4)*n)//2

def inverse_polygonal(k:int,value:int)->int|None:
    if k<3:raise ValueError("k>=3")
    if value<1:return None
    R=2*(k-2);L=k-4;D=8*(k-2)*value+L*L
    root=isqrt(D)
    if root*root!=D or (root+L)%R:return None
    n=(root+L)//R
    return n if n>=1 and polygonal(k,n)==value else None

def recover_entries_from_products(A:int,B:int,C:int)->tuple[int,int,int]|None:
    if min(A,B,C)<=0:return None
    T=isqrt(A*B*C)
    if T*T!=A*B*C or any(T%v for v in (A,B,C)):return None
    entries=(T//C,T//B,T//A)
    if len(set(entries))!=3:return None
    if (entries[0]*entries[1],entries[0]*entries[2],entries[1]*entries[2])!=(A,B,C):
        raise ArithmeticError("product recovery failed")
    return entries

def divisors(n:int)->list[int]:
    if n<1:raise ValueError("positive input required")
    low=[]; high=[]
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            low.append(d)
            if d*d!=n:high.append(n//d)
    return low+high[::-1]

def seed_from_two_indices(k:int,c:int,r:int,s:int)->list[dict]:
    """Complete for fixed r<s; a runs over divisors of gcd(A,B)."""
    if not(k>=3 and 1<=r<s):raise ValueError("k>=3 and 1<=r<s")
    A=polygonal(k,r)-c;B=polygonal(k,s)-c
    if min(A,B)<=0:return []
    result=[]
    for a in divisors(gcd(A,B)):
        b=A//a;d=B//a
        if min(a,b,d)<=0 or len({a,b,d})!=3:continue
        t=inverse_polygonal(k,b*d+c)
        if t is None:continue
        if recover_entries_from_products(A,B,b*d)!=(a,b,d):
            raise ArithmeticError("square-class check failed")
        result.append({"entries":(a,b,d),"indices":(r,s,t),
                       "products":(A,B,b*d),
                       "first_pair_nonsquare":isqrt(A)**2!=A})
    return result

def index_window(k:int,c:int,max_r:int,max_s:int)->dict:
    if k<3 or max_r<1 or max_s<2:raise ValueError("positive bounds required")
    seeds=[]
    for r in range(1,max_r+1):
        for s in range(r+1,max_s+1):
            seeds.extend(seed_from_two_indices(k,c,r,s))
    return {"order":k,"offset":c,"max_r":max_r,"max_s":max_s,
            "searched_index_pairs":sum(max(0,max_s-r) for r in range(1,max_r+1)),
            "seeds":seeds,"global_nonexistence_proved":False}

def fixed_pair_norm(k:int,c:int,a:int,b:int,r:int)->dict:
    if not(k>=3 and a>0 and b>0 and a!=b and r>=1
           and a*b+c==polygonal(k,r)):
        raise ValueError("exact first pair required")
    R=2*(k-2);L=k-4;D=8*(k-2)*c+L*L
    return {"q":a*b,"R":R,"L":L,"D":D,"N":a*(a-b)*D}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,default=84)
    p.add_argument("--offset",type=int,default=2)
    p.add_argument("--max-r",type=int,default=120)
    p.add_argument("--max-s",type=int,default=220)
    x=p.parse_args()
    print(json.dumps(index_window(x.order,x.offset,x.max_r,x.max_s),sort_keys=True))
if __name__=="__main__":main()
