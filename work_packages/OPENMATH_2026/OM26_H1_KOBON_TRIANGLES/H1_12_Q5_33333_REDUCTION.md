# H1-12 q=5 profile 33333 — separator-geometry reduction

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected q=5 reduction after exclusion of profile `33334`.

The only q=5 profile still alive is

```
33333
```

with

```
3 <= D2 <= 7.
```

All five cores are triple points.

This tranche quotients the retained graph/sector states under `S5`, applies the protected saturated-triple separator geometry, and reduces the profile to one exact graph type.

## 1. S5 quotient

The protected q=5 saturation replay leaves 595 labeled graph placements:

```
D2=3:  30
D2=4:  60
D2=5: 210
D2=6: 195
D2=7: 100.
```

Quotienting under permutation of the five equal triple cores gives exactly 15 graph orbits:

```
D2=3: 2
D2=4: 1
D2=5: 4
D2=6: 5
D2=7: 3.
```

The companion replay reconstructs all 15 orbits and their saturation-role sets.

## 2. Saturated-triple separator filter

For every saturated triple core `H`, the protected local separator lemma gives:

- `d2(H)=3`, `d1(H)=3`;
- the three D2 neighbors of `H` are pairwise nonadjacent in the D2 graph;
- the three leaf-pair arrangement lines exist, each with an ordinary separator strictly between the corresponding leaf cores;
- `H` lies strictly inside the triangle formed by its three D2 neighbors.

Applying only the pairwise-neighbor independence condition to the 15 quotient orbits leaves exactly four graph/role cases.

### Case A — D2=3 saturated star plus isolated core

```
edges = H-A, H-B, H-C
```

with fifth core `E` isolated in the D2 graph.

### Case B — D2=3 triangle plus two isolated cores

```
edges = AB, AC, BC
```

with no saturated core.

### Case C — D2=5 saturated star plus two attachments

```
edges = H-A, H-B, H-C, E-A, E-B.
```

### Case D — D2=6 K2,3

Two saturated triple hubs share the same three D2 neighbors.

All other 11 graph orbits violate saturated-neighbor independence and are excluded.

## 3. Case A is impossible by the strengthened core-line count

At the saturated hub `H`, the separator lemma produces all three leaf-pair lines

```
AB, BC, CA.
```

The four cores `H,A,B,C` are triple points, and the six pair lines

```
HA, HB, HC, AB, BC, CA
```

already exhaust their three incident arrangement lines.

The isolated triple core `E` can contribute at most three additional core-containing lines.

Therefore

```
h <= 9,
```

so at least

```
18-h >= 9
```

lines are clean.

The exact retained state in this graph orbit has charge capacity only

```
6.
```

Contradiction.

Hence Case A is impossible.

## 4. Case C is impossible by separator-incidence exhaustion

Again let `H` be the saturated hub with D2 neighbors `A,B,C`. The six lines

```
HA, HB, HC, AB, BC, CA
```

exhaust all incident lines at `A,B,C,H`.

The fifth core `E` is required to have elementary D2 segments to both `A` and `B`.

Thus the line `AE` must be one of

```
AH, AB, AC,
```

and the line `BE` must be one of

```
BH, AB, BC.
```

Intersect the two candidate line families.

Every intersection is one of:

- the already existing cores `H,A,B,C`;
- the ordinary separator `P_BC = AH ∩ BC`;
- the ordinary separator `P_AC = AC ∩ BH`;
- or a point on the common line `AB`.

The first six possibilities cannot be the distinct fifth core `E`.

The remaining possibility `E in AB` is also impossible. The separator lemma supplies an ordinary point `P_AB` strictly between `A` and `B`. No position of a distinct point `E` on line `AB` allows both `AE` and `BE` to be elementary segments:

- if `E` lies between `A` and `B`, one of the two segments contains `P_AB`;
- if `E` lies outside segment `AB`, one of `AE,BE` contains the other core and `P_AB`.

Thus Case C is impossible.

## 5. Case D is impossible by the two-interior-hub crossing argument

The separator-compatible D2=6 graph is exactly

```
K2,3.
```

The degree-3 side consists of the two saturated hubs `H1,H2`; their common neighbors are `A,B,C`.

The separator geometry puts both `H1` and `H2` strictly inside triangle `ABC`.

The three elementary spokes from `H1` partition triangle `ABC` into three subtriangles. The distinct core `H2` lies strictly inside one of them and cannot lie on an H1 spoke.

If, for example,

```
H2 in interior(ABH1),
```

then the elementary D2 segment `H2C` must leave `ABH1`. Since `H2` and `C` lie on the same side of line `AB`, it cannot leave across `AB`; it must cross `H1A` or `H1B`, or pass through `H1`.

Each alternative contradicts elementary D2 status.

Hence Case D is impossible.

## 6. Sole q=5 survivor

Only Case B remains:

```
D2 graph = K3 + 2 isolated vertices
D2 = 3
no saturated cores
D1 = 10
U = 1
blocked D1 = 6
clean lower bound = 6
charge capacity = 6.
```

Thus the q=5 residual has collapsed to a single graph/charge equality type.

Let the D2 triangle cores be `A,B,C`, and the isolated triple cores be `D,E`.

Exact equality additionally forces:

- `h=12`;
- no arrangement line contains any extra pair of cores beyond `AB,BC,CA`;
- the six lines through `D,E` are pairwise distinct and contain no other core;
- each triangle core has local counts `d2=2,d1=2` with both D1 targets blocked;
- each isolated core has `d2=0,d1=2` with both D1 targets unblocked.

This equality geometry is the next target.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, profile `33333` is reduced from 595 labeled graph placements / 15 symmetry orbits to the single graph type

```
K3 + 2 isolated cores
```

at exact charge equality.

The live H1-12 residual is therefore:

1. q=5 in this one equality geometry; or
2. q>=6.

The companion replay `ci/validate_openmath_h1_12_q5_33333.py` reconstructs the 595-state histogram, 15-orbit quotient, saturation-role filter, and the exact four separator-compatible cases.

## Claim boundary

The S5 quotient, saturation-role extraction, strengthened star count, separator-incidence exhaustion, and K2,3 crossing argument are independently reconstructed.

The reduction remains source-conditional because the saturated-triple separator lemma inherits the named local fan premise and the predecessor q=5 state space inherits the clean-line charging map. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
