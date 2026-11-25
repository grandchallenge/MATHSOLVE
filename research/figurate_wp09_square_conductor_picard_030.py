"""FIGURATE WP09-030: narrow Picard groups for square-A conductor family.

For A=f^2, f positive odd, O=Z[f*sqrt(2)] subset Z[sqrt(2)].
Because the maximal order has narrow class number 1, the conductor
sequence gives Pic^+(O) = (O_K/f)^* / ((Z/f)^* <(1+sqrt 2)^2>).

All finite group laws are exact over Z/f. This computes the entire
narrow Picard group for this infinite conductor subfamily, and the
ORDER of the full oriented ray group when combined with WP09-029's
ray kernel. It does NOT compute the full ray extension/group law.
"""
from __future__ import annotations

from math import gcd

from research.figurate_wp09_ray_kernel_029 import prime_factors, ray_kernel
from research.figurate_wp09_ray_class_conductor_027 import order_data

Pair = tuple[int, int]


def ring_mul(f: int, z: Pair, w: Pair) -> Pair:
    """Product in (Z/f)[sqrt(2)] in the integral maximal-order basis."""
    if f < 1:
        raise ValueError("positive modulus required")
    return ((z[0]*w[0]+2*z[1]*w[1]) % f,
            (z[0]*w[1]+z[1]*w[0]) % f)


def ring_pow(f: int, z: Pair, exponent: int) -> Pair:
    if exponent < 0:
        raise ValueError("nonnegative exponent required")
    out = (1 % f, 0)
    while exponent:
        if exponent & 1:
            out = ring_mul(f, out, z)
        z = ring_mul(f, z, z)
        exponent >>= 1
    return out


def ring_is_unit(f: int, z: Pair) -> bool:
    if f < 1:
        raise ValueError("positive modulus required")
    return gcd(z[0]*z[0]-2*z[1]*z[1], f) == 1


def legendre_two(p: int) -> int:
    """Quadratic character (2/p) for odd prime p."""
    if p < 3 or p % 2 != 1:
        raise ValueError("odd prime required")
    return 1 if p % 8 in (1, 7) else -1


def theoretical_projective_order(f: int) -> int:
    """Number of maximal-order units modulo f, divided by scalar units."""
    if f < 1 or f % 2 == 0:
        raise ValueError("f must be positive and odd")
    n = f
    for p in prime_factors(f):
        n = n * (p-legendre_two(p)) // p if n*(p-legendre_two(p))%p==0 else None
        if n is None:
            raise ArithmeticError("nonintegral conductor formula")
    return n


def _unit_scalar_exponent(f: int, unit: Pair) -> int:
    """Order of unit in projective residue group modulo scalar units."""
    identity = (1 % f, 0)
    z = identity
    limit = f*f+1
    for exponent in range(1, limit + 1):
        z = ring_mul(f, z, unit)
        if z[1] == 0:
            if not ring_is_unit(f, z):
                raise ArithmeticError("scalar not a unit")
            return exponent
    raise ArithmeticError("projective unit order exceeded finite group")


def _torsion_invariants(f: int, representatives: list[Pair],
                        subgroup: set[Pair]) -> list[int]:
    qorder = len(representatives)
    if qorder == 1:
        return []
    elementary: dict[int,list[int]] = {}
    for p,valuation in prime_factors(qorder).items():
        previous = 0
        increments: list[int] = []
        size = 1
        for exponent in range(1,valuation+1):
            size *= p
            killed = sum(ring_pow(f,z,size) in subgroup for z in representatives)
            rank = 0
            x = killed
            while x > 1 and x % p == 0:
                rank += 1
                x //= p
            if x != 1:
                raise ArithmeticError("torsion count not prime power")
            increments.append(rank-previous)
            previous = rank
            if killed == qorder:
                break
        increments.append(0)
        powers = []
        for i in range(len(increments)-1):
            count = increments[i]-increments[i+1]
            if count < 0:
                raise ArithmeticError("invalid torsion sequence")
            powers.extend([i+1]*count)
        elementary[p] = powers
    width = max(map(len,elementary.values()),default=0)
    factors = [1]*width
    for p,powers in elementary.items():
        for i,e in enumerate(powers,start=width-len(powers)):
            factors[i] *= p**e
    product = 1
    for factor in factors:
        product *= factor
    if product != qorder or any(b%a for a,b in zip(factors,factors[1:])):
        raise ArithmeticError("inconsistent invariant factors")
    return factors


def narrow_picard_square_conductor(
    f: int, *, max_residues: int | None = 200000
) -> dict:
    """Full narrow Picard group for O=Z[f sqrt(2)] at odd conductor f.

    The finite-group computation exhausts the O_K/f residue group, and
    never returns a partial result if max_residues is exceeded.
    """
    if f < 1 or f % 2 == 0:
        raise ValueError("f must be positive odd")
    if max_residues is not None and f*f > max_residues:
        raise ValueError("complete residue computation exceeds guard")

    m = (f*f-1)//8
    data = order_data(m)
    if data["A"] != f*f or data["f"] != f or data["squarefree_d"] != 2:
        raise ArithmeticError("quadratic-order conductor mismatch")

    all_units = [(x,y) for x in range(f) for y in range(f)
                 if ring_is_unit(f,(x,y))]
    scalars = [(x,0) for x in range(f) if gcd(x,f)==1]
    e = (1%f,1%f)         # 1+sqrt(2), norm -1
    eplus = (3%f,2%f)     # e^2 totally positive, norm +1
    ordinary_period = _unit_scalar_exponent(f,e)
    narrow_period = _unit_scalar_exponent(f,eplus)
    if narrow_period != ordinary_period//gcd(ordinary_period,2):
        raise ArithmeticError("positive unit index identity failed")

    positive_powers = []
    z = (1%f,0)
    while z not in positive_powers:
        positive_powers.append(z)
        z = ring_mul(f,z,eplus)
    if z != (1%f,0):
        raise ArithmeticError("positive unit subgroup not periodic")

    subgroup = {ring_mul(f, s,u) for s in scalars
                for u in positive_powers}
    if len(subgroup) != len(scalars)*narrow_period:
        raise ArithmeticError("subgroup cosets overlap")

    seen = set()
    representatives = []
    for candidate in [(1%f,0)] + all_units:
        if candidate in seen:
            continue
        coset = {ring_mul(f,candidate,h) for h in subgroup}
        if len(coset) != len(subgroup) or any(x in seen for x in coset):
            raise ArithmeticError("coset collision")
        seen.update(coset)
        representatives.append(min(coset))
    if len(seen) != len(all_units):
        raise ArithmeticError("incomplete narrow Picard quotient")

    theoretical = theoretical_projective_order(f)
    if theoretical != len(all_units)//len(scalars):
        raise ArithmeticError("conductor norm class-number formula failed")
    if theoretical % narrow_period or theoretical % ordinary_period:
        raise ArithmeticError("unit order fails to divide projective order")
    narrow_order = len(representatives)
    if narrow_order != theoretical//narrow_period:
        raise ArithmeticError("narrow class-number mismatch")
    ordinary_order = theoretical//ordinary_period
    if narrow_order != ordinary_order*gcd(ordinary_period,2):
        raise ArithmeticError("narrow versus ordinary mismatch")
    factors = _torsion_invariants(f,representatives,subgroup)
    return {
        "f":f,"m":m,"A":f*f,"field_discriminant":8,
        "order_discriminant":8*f*f,
        "maximal_residue_unit_count":len(all_units),
        "projective_unit_group_order":theoretical,
        "fundamental_negative_unit_projective_order":ordinary_period,
        "positive_unit_projective_order":narrow_period,
        "ordinary_picard_order":ordinary_order,
        "narrow_picard_order":narrow_order,
        "narrow_picard_invariant_factors":factors,
        "narrow_picard_group_complete":True,
        "full_oriented_ray_group_complete":False
    }


def full_ray_order_square_conductor(
    f:int,*,max_residues:int|None=200000,
    max_ray_states:int|None=250000
) -> dict:
    """Exact full ray GROUP ORDER (not invariant factors / extension law)."""
    p=narrow_picard_square_conductor(f,max_residues=max_residues)
    k=ray_kernel(p["m"],max_states=max_ray_states)
    return {
        **p,
        "ray_kernel_invariant_factors":k["kernel_invariant_factors"],
        "ray_kernel_order":k["kernel_order"],
        "full_oriented_ray_group_order":
            p["narrow_picard_order"]*k["kernel_order"],
        "full_oriented_ray_group_complete":f in (1,3),
        "full_oriented_ray_invariant_factors":(
            [] if f==1 else [6] if f==3 else None
        ),
        "extension_law_computed":f in (1,3)
    }
