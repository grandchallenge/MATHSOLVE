"""FIGURATE WP09-021: exact Pell seeds for four locally compatible orders."""
from __future__ import annotations
import argparse
import json

# k: (base_X, base_S, norm_one_unit_U, norm_one_unit_V, seed_unit_steps,
#     expected_s, expected_t, expected_d, amplification_order, next_d_digits)
CASES = {
    164: (72416,5692,19601,1540,10,
          150559512094191202263080416902498580002799945223,
          1916309735530931053564867150002683761037880788624,
          1836121501245313459201105265351598082818875949658621767286039188898783862293751029833171846480207,
          162,1585),
    196: (4828080,346636,195,14,57,
          4380883947136402700586746790958792422295427646187932484676301736278832263491460430483284850945583202509843690587848188211493815154022913478915407484929,
          61018652612998764549054276449065927822082955343561839406306767388371576134998015687440456690641764810756378102205851485520882945774726786004854529584936,
          1861637983352910478332422493090790557754819720194059827736039781602322511404658713751540177183098120083143518905342241076032583581843605923512027394894416748969526982684022665941082186809473450846814976522255962913193828554794179112082417778780391375417967908151141282000170817541090432836063745008545791,
          388,2314),
    228: (10227632,680332,451,30,20,
          191294518888718325116085513250154542769546032200994618246324203,
          2875787198012357090297283648222837808215328100704980620737262228,
          4135076004125881964081534678574280030936826509978897581237657996084488167501078896386290481361116732493241541812463627556817879,
          452,2799),
    244: (11376,772,19601,1260,44,
          19802750110523620886422909562876709287688831270665377691020462345437437471227800880131611725827348155662406201301558860059460728708283212065565050541843635291693356286838295235063190626883400844453566053,
          308058495564465927576011172313248943740213758117809647465817511615842005459106585517859363501213795922962354612058250760679901185870977779744448500550177643366536563947676258166298092540026347361370558264,
          47450018344721036787155891543128483176999156028998762109548545160501040074695804477514545890135739315114460797122999239048236001346664660993872431380065259126031051673515589630601691668616512134260494202370291229455892350663635486105782528376894321430827196039254726763428551070043145699501831461292915993983146916027429654517062393043447408713347871648328691981559886218373490162934671966131873706085929527,
          242,2630),
}
OFFSET = 2


def polygonal(k: int, n: int) -> int:
    if k < 3 or n < 1:
        raise ValueError("require k>=3 and n>=1")
    return ((k-2)*n*n-(k-4)*n)//2


def pell_multiply(d: int, x: int, y: int, u: int, v: int) -> tuple[int,int]:
    return u*x+d*v*y, v*x+u*y


def pell_power(d: int, u: int, v: int, exponent: int) -> tuple[int,int]:
    if d < 2 or exponent < 0:
        raise ValueError("require d>=2 and exponent>=0")
    x,y=1,0
    bx,by=u,v
    e=exponent
    while e:
        if e&1:
            x,y=pell_multiply(d,x,y,bx,by)
        bx,by=pell_multiply(d,bx,by,bx,by)
        e>>=1
    return x,y


def unit_order_mod(d: int,u: int,v: int,modulus: int) -> int:
    if modulus<2 or u*u-d*v*v!=1:
        raise ValueError("require modulus>=2 and norm-one unit")
    x,y=1,0
    for exponent in range(1,modulus**4+1):
        x,y=pell_multiply(d,x,y,u,v)
        x%=modulus
        y%=modulus
        if (x,y)==(1,0):
            return exponent
    raise ArithmeticError("finite matrix-group order bound exceeded")


def construct_seed(k: int) -> dict:
    if k not in CASES:
        raise ValueError("supported orders are 164, 196, 228, 244")
    base_x,base_s,u,v,steps,expected_s,expected_t,expected_d,expected_order,next_digits=CASES[k]
    a,b=1,k-2
    r=2
    R=2*(k-2)
    L=k-4
    delta=8*(k-2)*OFFSET+L*L
    norm=a*(a-b)*delta
    D=a*b
    if base_x*base_x-D*base_s*base_s!=norm:
        raise ArithmeticError("base point does not satisfy the norm equation")
    if u*u-D*v*v!=1:
        raise ArithmeticError("Pell multiplier is not norm one")
    x,y=base_x,base_s
    for _ in range(steps):
        x,y=pell_multiply(D,x,y,u,v)
    if x<=0 or y<=0:
        raise ArithmeticError("Pell coordinates must be positive")
    if x%(a*R)!=(-a*L)%(a*R) or y%R!=(-L)%R:
        raise ArithmeticError("Pell point misses the polygonal index lattice")
    s=(y+L)//R
    if x%a:
        raise ArithmeticError("first entry does not divide X")
    t_num=x//a+L
    if t_num%R:
        raise ArithmeticError("third polygonal index is not integral")
    t=t_num//R
    d=polygonal(k,s)-OFFSET
    if d<=0 or d%a:
        raise ArithmeticError("third entry is not a positive integer")
    if (s,t,d)!=(expected_s,expected_t,expected_d):
        raise ArithmeticError("exact output differs from pinned seed")
    if len({a,b,d})!=3:
        raise ArithmeticError("entries must be pairwise distinct")
    outputs=(polygonal(k,r),polygonal(k,s),polygonal(k,t))
    if (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET)!=outputs:
        raise ArithmeticError("Type B equations failed")
    order=unit_order_mod(D,u,v,2*a*R)
    if order!=expected_order:
        raise ArithmeticError("unexpected amplification unit order")
    return {
        "order":k,"offset":OFFSET,"entries":(a,b,d),"indices":(r,s,t),
        "pair_outputs":outputs,"pell_coordinates":(x,y),
        "base_pell_coordinates":(base_x,base_s),"unit":(u,v),
        "seed_unit_steps":steps,"delta":delta,"norm":norm,
        "amplification_modulus":2*a*R,"amplification_unit_order":order,
        "next_family_entry_digits":next_digits,
    }


def construct_next_family_member(k: int) -> dict:
    seed=construct_seed(k)
    a,b,_=seed["entries"]
    D=a*b
    u,v=seed["unit"]
    e=seed["amplification_unit_order"]
    ue,ve=pell_power(D,u,v,e)
    M=seed["amplification_modulus"]
    if (ue%M,ve%M)!=(1,0):
        raise ArithmeticError("unit power is not identity modulo lattice modulus")
    x0,y0=seed["pell_coordinates"]
    x,y=pell_multiply(D,x0,y0,ue,ve)
    R=2*(k-2);L=k-4
    s=(y+L)//R
    t=(x//a+L)//R
    d=polygonal(k,s)-OFFSET
    if (a*b+OFFSET,a*d+OFFSET,b*d+OFFSET)!=(
        polygonal(k,2),polygonal(k,s),polygonal(k,t)
    ):
        raise ArithmeticError("amplified exact Type B equations failed")
    if d<=seed["entries"][2]:
        raise ArithmeticError("amplified entry did not increase")
    return {"order":k,"entries":(a,b,d),"indices":(2,s,t),
            "pell_coordinates":(x,y),"unit_exponent":e,
            "lattice_modulus":M}


def main() -> None:
    p=argparse.ArgumentParser()
    p.add_argument("--order",type=int,choices=tuple(CASES),default=164)
    p.add_argument("--next-family-member",action="store_true")
    args=p.parse_args()
    result=(construct_next_family_member(args.order) if args.next_family_member
            else construct_seed(args.order))
    print(json.dumps(result,sort_keys=True))


if __name__=="__main__":
    main()
