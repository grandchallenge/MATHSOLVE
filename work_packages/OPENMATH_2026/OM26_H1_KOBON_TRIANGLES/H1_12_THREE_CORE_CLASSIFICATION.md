# H1-12 three-core classification and exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_REDUCTION__ARITHMETIC_INDEPENDENTLY_REPLAYED__NOT_CERTIFIED`

## Scope

Assume an admissible `n=18` hill arrangement has `T=95` counted bounded triangular faces. Apply the protected H1-12 projective reduction so that all line pairs meet finitely while the selected counted faces are preserved.

This note studies the residual case in which the normalized arrangement has exactly three finite multiple points.

The conclusion is conditional on the global clean-line charging and local fan premises recorded in protected MATHFORGE reconnaissance from `alejandrozu/kobon-proof@22d1165f6c455fe45e461baef4410f6d5c78a014`. The integer deduction below is independently reconstructed and replayed in GCL; the source's unfinished arrangement-to-fan extraction is **not** promoted to an independent GCL theorem.

## Notation and admitted premises

Let the three multiple-point multiplicities be `r_1,r_2,r_3 >= 3`. Put

```
S = sum r_i(r_i-2)
I = sum r_i
delta = 18*16 - 3T = 3
```

Let:

- `U` be the number of bounded elementary segments incident to no counted triangle;
- `D1` be the number of elementary segments incident to two triangles with exactly one multiple endpoint;
- `D2` be the number of such double-used segments with two multiple endpoints;
- `h` be the number of arrangement lines containing at least one multiple point;
- `d1(v)`, `d2(v)` be the corresponding local counts at a multiple point `v`.

The source-scoped geometric premises used here are:

1. **defect identity:** `delta = S + U - D1 - D2`;
2. **clean-line charging:** `18-h <= 2U + D1`;
3. **core incidence:** `h <= I-D2`;
4. **fan bounds:** if `d2(v)<=1`, then `d1(v)<=2r-4`; always `d1(v)<=2r-3`;
5. **triple refinement:** at a triple point `d1(v)<=3`, and `d1(v)=3` forces `d2(v)>=3`;
6. **triple fan adjacency:** two consecutive radial rays with ordinary other endpoints cannot both be counted by `d1`;
7. **charging-map refinement:** the clean-line argument assigns one charge from every clean line to a transverse bounded segment. An unused segment can receive at most two clean-line charges, one through each ordinary endpoint; a `D1` segment can receive at most one, through its unique ordinary endpoint; a `D2` segment receives none.

With exactly three multiple points, a core-to-core elementary segment is determined by an unordered pair of core points. Hence `D2<=3`, and every local `d2(v)<=2`. Premise 5 therefore sharpens every triple point to `d1(v)<=2`.

A purely local observation used below is also elementary: around an `r`-fold point there are `2r` cyclic sectors, and a radial elementary segment is shared by two triangular faces exactly when both adjacent sectors are triangular. Consequently exactly `2r-1` shared radial segments is impossible: if every sector is triangular there are `2r` shared rays; otherwise a nontriangular sector makes both of its boundary rays nonshared, leaving at most `2r-2`.

## Step 1 — D2 cannot be 0 or 1

From premises 1 and 2,

```
2 delta >= 18 + 2S - h - 3D1 - 2D2.
```

If `D2<=1`, every core has `d2<=1`, so the local fan bound gives

```
D1 <= 2I - 12.
```

Using `h<=I-D2` gives

```
2 delta >= 18 + sum_i (2r_i^2 - 11r_i + 12) - D2.
```

For every integer `r>=3`,

```
2r^2 - 11r + 12 >= -3,
```

with equality at `r=3`. Thus the right-hand side is at least

```
18 - 9 - 1 = 8,
```

whereas `2 delta = 6`. Contradiction.

Therefore a three-core 95 witness must have `D2=2` or `D2=3`.

## Step 2 — D2=2 is impossible

Two core-core shared segments form a path on the three core points, with local core degrees `1,2,1`.

Ignoring the sharper triple refinement for a moment, the endpoint fan bounds and the universal middle bound give

```
D1 <= 2I - 11.
```

The defect identity and `U>=0` give

```
D1 >= S - 5.
```

Hence

```
sum_i r_i(r_i-4) = S-2I <= -6.
```

For `r>=3`, the values begin

```
r=3: -3
r=4:  0
r=5:  5
```

and then increase. Therefore the only possible multiplicity multisets are `(3,3,3)` and `(3,3,4)`.

### Pattern (3,3,3)

Every core is triple and has `d2<=2`, so the triple refinement gives `D1<=6`.

The defect identity gives `U=D1-4`. Also `h<=I-D2=7`, so at least 11 lines are clean. Clean-line charging would require

```
11 <= 2(D1-4)+D1 = 3D1-8,
```

hence `D1>=7`, contradicting `D1<=6`.

### Pattern (3,3,4)

The two triple points contribute at most 2 each to `D1`. The fourfold point contributes at most 5 if it is the degree-2 middle of the path, and at most 4 if it is an endpoint. Thus `D1<=9`.

The defect identity gives `U=D1-9`; nonnegativity forces `D1=9` and `U=0`. But `h<=I-D2=8`, so at least 10 lines are clean, while charging gives only

```
10 <= 2U+D1 = 9,
```

a contradiction.

Therefore `D2=2` is impossible.

## Step 3 — D2=3 leaves only one rigid template

Now the core graph is the triangle on the three multiple points. Every core has local `d2=2`.

The universal fan bound gives `D1<=2I-9`, while the defect identity gives `D1>=S-6`. Hence

```
sum_i r_i(r_i-4) <= -3.
```

The only multiplicity multisets are

```
(3,3,3), (3,3,4), (3,4,4).
```

### Pattern (3,4,4)

The triple contributes at most 2 to `D1`; each fourfold point contributes at most 5. Thus `D1<=12`. The defect identity requires `D1>=S-6=13`. Impossible.

### Pattern (3,3,4)

The two triples contribute at most 2 each and the fourfold point at most 5, so `D1<=9`.

Here `U=D1-8` and `h<=I-D2=7`. Thus at least 11 lines are clean, and charging gives

```
11 <= 2(D1-8)+D1 = 3D1-16.
```

Therefore `D1>=9`, so necessarily

```
D1=9, U=1.
```

All three local fan caps are saturated. In particular the fourfold point has

```
d1=5, d2=2,
```

so seven of its eight radial elementary segments would be shared. The cyclic-sector observation above forbids exactly seven shared rays. Therefore `(3,3,4)` is impossible.

### Pattern (3,3,3)

Every triple has `d1<=2`, hence `D1<=6`.

Now `U=D1-3` and `h<=I-D2=6`. At least 12 lines are clean, so charging gives

```
12 <= 2(D1-3)+D1 = 3D1-6.
```

Thus `D1>=6`. Therefore every inequality saturates:

```
r_1=r_2=r_3=3
D2=3
D1=6
U=3
h=6
d1(v)=2 and d2(v)=2 at each core
18-h = 12 = 2U+D1
```

The three `D2` segments are the three pairwise core connectors, so the core points are noncollinear and form a core triangle.

At each triple point there are six cyclic sectors and exactly `d1+d2=4` shared rays. A six-cycle has four shared boundary rays only when exactly one sector is nontriangular. Hence **five of the six sectors at each core must be triangular**.

## Step 4 — the saturated template cannot realize the clean-line charge map

The preceding arithmetic used only the aggregate charging inequality. The source proof supplies more structure: every clean line chooses one transverse charge target, and the bounds `2U+D1` arise from endpoint capacities.

Fix one of the three triple cores, say `A`. Let the two core-triangle sides through `A` be `AB` and `AC`, and let `L_A` be the third arrangement line through `A`.

Because the three `D2` core connectors are elementary shared sides, their three elementary segments bound the core triangle `ABC`. No arrangement line can enter its interior without crossing one of those elementary boundary segments, except through a core vertex; at a core vertex, the third incident line would then have to leave through the opposite elementary core side. Hence `ABC` is itself a triangular face. In particular, the third line `L_A` cannot enter the interior angle of `ABC`: doing so would cross the opposite elementary core side. Thus, in cyclic order around `A`, the two inward core rays are adjacent, and the two rays of `L_A` sit immediately outside them.

We already know that exactly one of the six sectors at `A` is nontriangular. The two inward core rays are `D2`, so the sectors on both sides of each are triangular. Hence the unique nontriangular sector lies among the three exterior sectors.

If it is either exterior sector adjacent to a spoke ray and an outward core-side ray, the two remaining `D1` rays are consecutive. Premise 6 forbids this. Therefore the unique nontriangular sector must be the middle exterior sector, between the two outward continuations of `AB` and `AC`.

Consequently the two `D1` rays at `A` are **exactly the two opposite rays of `L_A`**. The same holds at `B` and `C`.

Now inspect the exterior triangle adjacent to the shared core edge `AB`. On the side opposite the core triangle, its side through `A` must be `L_A`, and its side through `B` must be `L_B`. Therefore the `D1` segment on the relevant ray of `L_A` ends at the ordinary point

```
L_A ∩ L_B.
```

It cannot end earlier, because then the exterior triangle adjacent to the elementary segment `AB` would be cut. Its unique transverse line at that ordinary endpoint is `L_B`.

But `L_B` is **not clean**: it contains the multiple point `B`. Thus this `D1` segment cannot receive a charge from any clean line. Repeating the argument for both rays at all three cores shows that **none of the six `D1` segments is chargeable by a clean line**.

The saturated arithmetic template has

```
18-h = 12 clean lines,
U = 3,
D1 = 6.
```

Every clean line must emit one charge. Since no `D1` target can receive a clean-line charge, only the three unused segments remain, with total capacity at most `2U=6`. Twelve required charges cannot fit into six available slots. Contradiction.

Therefore the three-core case is impossible, conditional on the named charging/fan premises.

## Result

Conditional on the named source-scoped geometric premises, any `n=18`, `T=95` arrangement with exactly three finite multiple points is forced into one rigid template:

- exactly three finite triple points;
- noncollinear core points;
- all three pairwise core elementary segments are shared by two triangles;
- exactly two additional ordinary-endpoint shared rays at each core;
- exactly five triangular sectors out of six at each core;
- `D1=6`, `D2=3`, `U=3`, `h=6`;
- the clean-line charging inequality is saturated.

Step 4 excludes that saturated template using the endpoint-level charge map. Therefore, conditional on the named source-scoped geometric premises, **any `n=18`, `T=95` witness must have at least four finite multiple points after no-parallel normalization**.

The companion validator `ci/validate_openmath_h1_12_three_core.py` independently enumerates every possible multiplicity triple `3<=r_i<=18`, every simple core-shared graph on three vertices, every local `d1` count allowed by the stated fan bounds, and the clean-line/defect inequalities. It returns exactly the saturated template as the unique arithmetic survivor. Step 4 is the subsequent geometric exclusion. The validator checks the arithmetic implication only; it does not prove the geometric charging/fan premises.

## Claim boundary

This is a Solve-level strict residual reduction, not a hill-global upper bound and not a MATHCERT disposition. The arithmetic classification is independently reconstructed and replayed. Conditional on the source-scoped endpoint-level charging map and local fan premises, the entire q=3 case is excluded. Those geometric premises remain source-scoped until independently proved or certified inside GCL. No conclusion `T<=94` follows from this artifact alone because q>=4 remains open.
