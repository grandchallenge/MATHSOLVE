"""FIGURATE WP09-029: exact ray-unit kernel in quadratic orders.

O=Z[sqrt(2A)], A=8m+1. Modulo A, sqrt(2A)^2=0.
The residue unit group is (Z/A)^* x (Z/A,+), via
 x+y sqrt(2A) -> (x, y/x). The positive norm-one unit image
 generates the subgroup divided out by the oriented ray kernel.

Does NOT compute Pic^+(O), the rest of the full ray class group.
Resource guard raises before building a truncated quotient.
"""
from __future__ import annotations
from math import gcd
from research.figurate_wp09_uniform_pell_lattice_023 import fundamental_unit
from research.figurate_wp09_ray_class_conductor_027 import order_data

def prime_factors(n:int)->dict[int,int]:
    if n<1:raise ValueError("n positive")
    ans={};p=2
    while p*p<=n:
        while n%p==0:
            ans[p]=ans.get(p,0)+1;n//=p
        p+=1 if p==2 else 2
    if n>1:ans[n]=ans.get(n,0)+1
    return ans

def residue_map(A:int,x:int,y:int)->tuple[int,int]:
    """Unit residue as multiplicative x and normalized nilpotent t=y/x."""
    if A<1 or gcd(x,A)!=1:raise ValueError("nonunit residue")
    if A==1:return (0,0)
    return (x%A,(y*pow(x,-1,A))%A)

def residue_product(A:int,p:tuple[int,int],q:tuple[int,int])->tuple[int,int]:
    if A<1:raise ValueError("A positive")
    if A==1:return (0,0)
    return ((p[0]*q[0])%A,(p[1]+q[1])%A)

def residue_power(A:int,p:tuple[int,int],e:int)->tuple[int,int]:
    if e<0:raise ValueError("nonnegative exponent only")
    if A==1:return (0,0)
    return (pow(p[0],e,A),(p[1]*e)%A)

def expected_residue_group_size(A:int)->int:
    if A<1:raise ValueError("A positive")
    return A*sum(gcd(x,A)==1 for x in range(A))

def _log_exact_power(value:int,p:int)->int:
    k=0
    while value>1 and value%p==0:
        value//=p;k+=1
    if value!=1:raise ArithmeticError("p-torsion count not a power")
    return k

def _invariant_factors(A:int, reps:list[tuple[int,int]],
                       classes:dict[tuple[int,int],int],
                       quotient_order:int)->list[int]:
    """Recover invariant factors from exact p^e torsion cardinalities."""
    elementary={}
    for p,valuation in prime_factors(quotient_order).items():
        prev=0; increments=[]
        for e in range(1,valuation+1):
            power=p**e
            killed=sum(classes[residue_power(A,rep,power)]==0 for rep in reps)
            rank=_log_exact_power(killed,p)
            increments.append(rank-prev)
            prev=rank
            if killed==quotient_order:break
        increments.append(0)
        elementary[p]=[]
        for j in range(len(increments)-1):
            c=increments[j]-increments[j+1]
            if c<0:raise ArithmeticError("inconsistent abelian quotient")
            elementary[p].extend([j+1]*c)
    width=max((len(v) for v in elementary.values()),default=0)
    factors=[1]*width
    for p,exps in elementary.items():
        for i,e in enumerate(exps,start=width-len(exps)):
            factors[i]*=p**e
    if any(b%a for a,b in zip(factors,factors[1:])):
        raise ArithmeticError("invariant factor divisibility failed")
    prod=1
    for x in factors:prod*=x
    if prod!=quotient_order:raise ArithmeticError("group cardinality mismatch")
    return factors

def ray_kernel(m:int,max_states:int|None=250000)->dict:
    """Finite positive-unit residue quotient with full group structure."""
    if m<0:raise ValueError("m nonnegative")
    data=order_data(m)
    A=data["A"]; D=data["D"]
    bound=expected_residue_group_size(A)
    if max_states is not None and bound>max_states:
        raise ValueError(f"complete residue cardinality {bound} exceeds guard {max_states}")
    U,V=fundamental_unit(D)
    unit=residue_map(A,U,V)
    identity=(1%A,0)
    subgroup=[];point=identity
    while point not in subgroup:
        subgroup.append(point)
        point=residue_product(A,point,unit)
    if point!=identity:raise ArithmeticError("unit orbit not a subgroup")
    order=len(subgroup)
    if bound%order:raise ArithmeticError("unit orbit size does not divide unit group")
    states=[(x,t) for x in range(A) if gcd(x,A)==1 for t in range(A)]
    classes={};reps=[]
    for state in states:
        if state in classes:continue
        coset=[residue_product(A,state,s) for s in subgroup]
        cid=len(reps)
        for element in coset:
            if element in classes:raise ArithmeticError("overlapping cosets")
            classes[element]=cid
        reps.append(min(coset))
    if len(classes)!=bound or len(reps)*order!=bound:
        raise ArithmeticError("incomplete quotient enumeration")
    # Set identity coset index 0 for the invariant-factor counter.
    if classes[identity]!=0:
        raise ArithmeticError("identity must be enumerated first")
    factors=_invariant_factors(A,reps,classes,len(reps))
    r=(A+1)//2
    target=residue_map(A,r,r)
    # Explicit target coset and norm-one unit stabilizer.
    return {"m":m,"A":A,"D":D,"conductor":data["f"],
            "group_coordinates":"(unit constant x, normalized nilpotent y/x)",
            "residue_group_size":bound,
            "fundamental_positive_unit":(U,V),
            "unit_residue":unit,
            "positive_unit_residue_order":order,
            "kernel_order":len(reps),
            "kernel_invariant_factors":factors,
            "target_ray_coset":classes[target],
            "target_ray_is_unit_coset":classes[target]==0,
            "full_ray_class_group_computed":False,
            "narrow_picard_group_computed":False,
            "ray_kernel_complete":True,
            "general_parameter_classification_proved":False}
