# H1-12 q=4 profile 3333 — higher-count saturated-star exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3333 residual after exclusion of the non-saturated D2=3 star.

The remaining saturated equality form is

```
core graph = K1,3
hub: d2=3, d1=3
leaves: d2=1, d1=2
D1=9
U=3
clean = 12
charge capacity = 12.
```

The protected saturated-hub separator reduction already proves:

- the hub fan alternates `D2,D1,D2,D1,D2,D1`;
- for each pair of leaf cores `A,B`, the corresponding hub D1 ray meets the leaf-pair line at an ordinary point `P_AB` strictly between `A` and `B`;
- all six core-pair arrangement lines are distinct;
- `h=6`, hence there are exactly twelve clean lines.

This note excludes the remaining equality form conditional on the named triple-point local fan premise and clean-line charging map.

## 1. The saturated hub lies inside the leaf triangle

Let the three leaf cores be `A,B,C`.

At the saturated triple hub `H`, D2 and D1 rays alternate around the six-ray fan. Opposite rays are separated by three cyclic positions, so every hub D1 ray is opposite one of the three D2 spokes.

Consider the D1 separator ray from `H` to `P_AB`, lying between spokes `HA` and `HB`. Its opposite ray is the remaining D2 spoke `HC`.

Therefore `C,H,P_AB` are collinear with `H` between `C` and `P_AB`.

The separator lemma gives `P_AB` strictly inside segment `AB`. Thus `H` lies strictly inside triangle `ABC`. The same conclusion is consistent cyclically for the other two separator points.

## 2. Charge equality forbids any additional blocked leaf D1 target

The protected blocked-target count for this normal form is exactly the three hub D1 segments. Its charge capacity is

```
2U + D1 - B
= 2*3 + 9 - 3
= 12,
```

equal to the exact twelve clean lines.

Therefore every remaining leaf D1 segment must be chargeable. In particular, no leaf D1 ray may be adjacent to its D2 spoke toward the hub; otherwise the protected transverse-line lemma would make it unavailable as a clean-line charge target and reduce total capacity below twelve.

## 3. Leaf ray geometry

Fix leaf `A`.

Because `H` lies inside triangle `ABC`, the inward ray `AH` lies strictly between the inward side rays `AB` and `AC`.

The three arrangement lines through the triple core `A` are exactly

```
AB, AH, AC,
```

by the protected six-core-pair-line result.

Hence the six cyclic rays at `A` have the order

```
AB_in, AH_in, AC_in, AB_out, AH_out, AC_out
```

up to reversal and cyclic rotation.

Here `AH_in` is the unique D2 ray at `A`.

The leaf has exactly two D1 rays. Exact charge equality forbids either D1 ray from occupying `AB_in` or `AC_in`, since those are the two rays adjacent to `AH_in`.

The named triple-point fan premise also forbids two consecutive D1 rays.

Among the three remaining positions

```
AB_out, AH_out, AC_out,
```

the only two-position choice with no consecutive D1 rays is

```
AB_out and AC_out.
```

Therefore the two leaf D1 segments lie on the outward continuations of the two leaf-pair side lines.

## 4. Those two D1 segments force a third D1 segment

Let `AX` be the D1 elementary segment on `AB_out`, and let `AY` be the D1 elementary segment on `AC_out`.

Let `R` be the first arrangement vertex on the ray `AH_out`.

Because `AX` is D1, both sectors adjacent to the ray `AB_out` are triangular. One of those sectors is bounded by `AB_out` and `AH_out`, so `AR` is a side of a triangular face.

Because `AY` is D1, both sectors adjacent to the ray `AC_out` are triangular. One of those sectors is bounded by `AH_out` and `AC_out`, so the same elementary segment `AR` is a side of a second triangular face on its other side.

Thus `AR` is shared by two triangular faces.

Its other endpoint `R` is ordinary. There are exactly four finite multiple points in this tranche, and the other three cores do not lie on the line `AH`: the protected saturated-hub reduction proves all six core-pair lines are distinct, while `H` lies on the opposite ray `AH_in`.

Therefore `AR` is a D1 segment.

But the leaf already has the two D1 segments `AX` and `AY`. Hence

```
d1(A) >= 3,
```

contradicting the protected normal-form value

```
d1(A)=2.
```

## Result

Conditional on the named source-scoped triple-point local fan premise and clean-line charging map, the higher-count saturated D2=3 star cannot realize `n=18,T=95`.

The profile-3333 residual is reduced from

```
6 normal forms / 41 labeled states
```

to

```
5 normal forms / 37 labeled states.
```

The only remaining charge-equality form is the D2=3 triangle plus isolated core.

The companion replay `ci/validate_openmath_h1_12_3333_saturated_equality.py` checks the leaf six-ray consequence: once the unique D2 ray is flanked by the two inward side rays, charge equality and the no-consecutive-D1 premise force the two D1 rays to the two outward side positions, both adjacent to the opposite hub ray.

## Claim boundary

The interior-hub consequence, leaf ray-order argument, and forced-third-D1 contradiction are independently reconstructed from the protected separator geometry.

The conclusion remains source-conditional because it invokes the named local fan premise and clean-line charging map to obtain the alternating hub pattern and exact no-additional-blocking equality. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
