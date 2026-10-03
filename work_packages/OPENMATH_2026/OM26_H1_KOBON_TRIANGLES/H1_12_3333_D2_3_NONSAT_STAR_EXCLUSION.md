# H1-12 q=4 profile 3333 — non-saturated D2=3 star exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3333 residual after the D2=4 C4 exclusion.

One of the three remaining charge-equality forms is the non-saturated D2=3 star:

```
core graph = K1,3
hub: d2=3, d1=1
leaves: d2=1, d1=2
D1=7
U=1
I=12
D2=3
clean lower bound = 9
charge capacity upper bound = 9.
```

This note excludes that form conditional on the named triple-point local fan premise and clean-line charging map.

## Equality forces zero blocked D1 targets

The protected blocked-target normal form gives equality:

```
clean = capacity = 9.
```

Any additional unavailable D1 charge target would lower capacity below nine. Therefore every D1 segment in a realization of this form must be chargeable by a clean transverse line.

In particular, the hub's unique D1 ray is not adjacent in cyclic order to a D2 ray.

## Hub cyclic consequence

At the triple hub there are six cyclic rays:

```
3 D2 rays,
1 D1 ray,
2 other rays.
```

For the unique D1 ray to avoid adjacency to D2, its two cyclic neighbors must be exactly the two other rays.

Therefore the remaining three positions form one consecutive block of D2 rays.

Hence at least two pairs of D2 spokes are cyclically adjacent.

## Adjacent D2 spokes force an additional core-pair arrangement line

Take two adjacent D2 spokes from the hub H to leaf cores A and B.

A D2 elementary segment is incident to triangular faces on both sides. Therefore the sector between the adjacent spokes HA and HB is a triangular face. Its third side lies on the arrangement line through A and B.

Thus AB is an arrangement line containing two leaf cores.

This line is not one of the two hub spokes HA or HB. If it coincided with a hub-spoke line, H,A,B would be collinear and the two elementary D2 spokes at H would lie on the same or antipodal ray, contrary to their distinct adjacent positions.

Therefore AB contributes an additional repeated core incidence beyond the three star-spoke D2 segments.

## Strict core-incidence contradiction

The ordinary core-incidence bound gives

```
h <= I-D2 = 9.
```

Charge equality requires equality here: h=9 and exactly nine clean lines.

But the additional leaf-pair arrangement line makes the incidence saving strictly larger than D2 alone, so

```
h <= 8.
```

Hence

```
clean = 18-h >= 10.
```

The protected charge capacity of this normal form is only 9.

Contradiction.

## Result

Conditional on the named source-scoped triple-point local fan premise and clean-line charging map, the non-saturated profile-3333 D2=3 star cannot realize `n=18,T=95`.

The profile-3333 residual is reduced from

```
7 normal forms / 45 labeled states
```

to

```
6 normal forms / 41 labeled states.
```

The remaining charge-equality forms are:

1. the higher-count saturated D2=3 star;
2. the D2=3 triangle plus isolated core.

The companion replay `ci/validate_openmath_h1_12_3333_nonsat_star.py` checks the hub cyclic classification and the strict clean-line/capacity inequality.

## Claim boundary

The hub cyclic implication and strict core-incidence refinement are independently reconstructed.

The conclusion remains source-conditional because equality is inherited from the protected local fan/blocked-target analysis and the contradiction uses the protected clean-line charging map. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
