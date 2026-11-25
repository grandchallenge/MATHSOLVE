"""FIGURATE WP09-022: exact Pell seeds for three more locally compatible orders."""
from __future__ import annotations
import argparse
import json

# k: base X,S; norm-one unit U,V; seed steps; exact s,t,d; unit order; next d digits.
CASES = {
    308: (7521856,429996,35,2,1,
          49173,860168,369944066839,612,2270),
    340: (18592,1068,114243,6214,8,
          11423817684781477108531933830301694263727175,
          210024332750642484748486106183948953202007676,
          22055110173676298711853052417255546283873851842341288791785952330313175104651322552060223,
          52,646),
    356: (30800,1676,258065,13716,32,
          1504699175711065838545810739621546414075173402601182922297946649529406030599934525304843746212948910534739063336262843490746949935379315752643229820190642759031366538474817891572918891,
          28310746046730887754276264183444936494431225824953708096748139660266943479349467842325013732113325958668456801885031571068528490872704349886026004149581313743303522144747989411694575404,
          400749170861244294657713664277790654885026802109356000545437704103819727217408006938307289707716852386075417895044484644972147329057081727230022277377747386716231343146949861171138906096651353752252092374331177905029455032677534403983871399033119357528777809592397662723973078140250811576316509887623046621428256348426978817656495932258870392977774352222156809812844119,
          118,1717),
}
OFFSET=2


def polygonal(k,n):
    if k<3 or n<1:raise ValueError("require k>=3 and n>=1")
    return ((k-2)*n*n-(k-4)*n)//2


def pell_multiply(d,x,y,u,v):
    return u*x+d*v*y,v*x+u*y


def pell_power(d,u,v,exponent):
    if d<2 or exponent<0:raise ValueError("require d>=2 and exponent>=0")
    x,y=1,0
    bx,by=u,v
    e=exponent
    while e:
        if e&1:x,y=pell_multiply(d,x,y,bx,by)
        bx,by=pell_multiply(d,bx,by,bx,by)
        e>>=1
    return x,y


def unit_order_mod(d,u,v,modulus):
    if modulus<2 or u*u-d*v*v!=1:raise ValueError("require norm-one unit and modulus>=2")
    x,y=1,0
    for exponent in range(1,modulus**4+1):
        x,y=pell_multiply(d,x,y,u,v)
        x%=modulus;y%=modulus
        if (x,y)==(1,0):return exponent
    raise ArithmeticError("finite matrix-group order bound exceeded")


def construct_seed(k):
    if k not in CASES:raise ValueError("supported orders are 308, 340, 356")
    x0,y0,u,v,steps,expected_s,expected_t,expected_d,expected_order,next_digits=CASES[k]
    a,b,r=1,k-2,2
    D=a*b;R=2*(k-2);L=k-4
    delta=8*(k-2)*OFFSET+L*L
    norm=a*(a-b)*delta
    if x0*x0-D*y0*y0!=norm:raise ArithmeticError("base norm failure")
    if u*u-D*v*v!=1:raise ArithmeticError("unit norm failure")
    x,y=x0,y0
    for _ in range(steps):x,y=pell_multiply(D,x,y,u,v)
    if x%(a*R)!=(-a*L)%(a*R) or y%R!=(-L)%R:raise ArithmeticError("index lattice failure")
    s=(y+L)//R
    if x%a:raise ArithmeticError("first-entry divisibility failure")
    tnum=x//a+L
    if tnum%R:raise ArithmeticError("third index divisibility failure")
    t=tnum//R
    d=polygonal(k,s)-OFFSET
    if (s,t,d)!=(expected_s,expected_t,expected_d):raise ArithmeticError("seed mismatch")
    if d<=0 or len({a,b,d})!=3:raise ArithmeticError("entry positivity/distinctness failure")
    outputs=(polygonal(k,r),polygonal(k,s),polygonal(k,t))
    if (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET)!=outputs:raise ArithmeticError("Type B equations failed")
    M=2*a*R
    order=unit_order_mod(D,u,v,M)
    if order!=expected_order:raise ArithmeticError("amplification order mismatch")
    return {"order":k,"offset":OFFSET,"entries":(a,b,d),"indices":(r,s,t),
            "pair_outputs":outputs,"pell_coordinates":(x,y),
            "base_pell_coordinates":(x0,y0),"unit":(u,v),"seed_steps":steps,
            "norm":norm,"lattice_modulus":M,"unit_order":order,
            "next_family_entry_digits":next_digits}


def construct_next_family_member(k):
    seed=construct_seed(k)
    a,b,_=seed["entries"];D=a*b
    u,v=seed["unit"];e=seed["unit_order"];M=seed["lattice_modulus"]
    ue,ve=pell_power(D,u,v,e)
    if (ue%M,ve%M)!=(1,0):raise ArithmeticError("unit power not identity modulo lattice")
    x0,y0=seed["pell_coordinates"]
    x,y=pell_multiply(D,x0,y0,ue,ve)
    R=2*(k-2);L=k-4
    s=(y+L)//R;t=(x//a+L)//R;d=polygonal(k,s)-OFFSET
    if (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET)!=(polygonal(k,2),polygonal(k,s),polygonal(k,t)):
        raise ArithmeticError("amplified Type B equations failed")
    if d<=seed["entries"][2]:raise ArithmeticError("family member did not increase")
    return {"order":k,"entries":(a,b,d),"indices":(2,s,t),
            "pell_coordinates":(x,y),"unit_exponent":e,"lattice_modulus":M}


def main():
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,choices=tuple(CASES),default=308)
    p.add_argument("--next-family-member",action="store_true")
    args=p.parse_args()
    z=construct_next_family_member(args.order) if args.next_family_member else construct_seed(args.order)
    print(json.dumps(z,sort_keys=True))

if __name__=="__main__":main()
