# H1-12 q=4 profile 3334 — D2=4 exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3334 normal form and D2=3 exclusion for a normalized `n=18,T=95` arrangement.

The remaining `D2=4` role-types are:

1. a non-saturated four-cycle;
2. a saturated T-hub star plus a TT outer edge;
3. a saturated T-hub star plus a TQ outer edge;
4. a saturated Q-hub star plus a TT outer edge.

This note excludes all four role-types conditional on the already named local no-long-run fan premise and clean-line charging map.

It reuses the independently reconstructed transverse-line lemma from the protected D2=3 tranche:

> a shared D1 segment whose cyclic neighbor at its multiple endpoint is a D2 spoke has a non-clean transverse line at its ordinary endpoint and is therefore unavailable as a clean-line charge target.

## Local cyclic lemma

At a core, call a shared D1 ray **blocked for charging** when it is adjacent in the cyclic ray order to a D2 ray. By the transverse-line lemma, every such D1 segment is unavailable as a clean-line charge target.

Two finite cyclic consequences of the local fan premise are used below.

### Triple core with d1=2, d2=2

There are six radial rays. Two are D1, two are D2, and two are other rays.

The local fan premise forbids two consecutive D1 rays. Exhausting the cyclic placements under these counts shows that at least one D1 ray is adjacent to a D2 ray.

Hence at least one D1 segment at such a triple core is unavailable for charging.

### Quadruple core with d1=4, d2=2

There are eight radial rays. Four are D1, two are D2, and two are other rays.

The local fan premise forbids three consecutive D1 rays. Exhausting the cyclic placements under these counts again shows that at least one D1 ray is adjacent to a D2 ray.

Hence at least one D1 segment at such a quadruple core is unavailable for charging.

The companion replay checks both finite cyclic statements exhaustively.

## Case A — non-saturated four-cycle

The protected normal form gives

```
core degrees = (2,2,2,2),
D1 = 10,
U = 0.
```

The three triple cores have local counts

```
d2=2, d1=2,
```

and the quadruple core has

```
d2=2, d1=4.
```

By the local cyclic lemma, each of the four cores contributes at least one unavailable D1 segment. These are four distinct global D1 segments because a D1 segment has exactly one multiple endpoint.

For profile 3334, `I=13`. Therefore

```
h <= I-D2 = 9,
```

so at least nine arrangement lines are clean.

But `U=0`, and at most

```
D1 - 4 = 6
```

D1 charge targets remain available. The charging map would require nine targets.

Contradiction.

Thus the non-saturated four-cycle is impossible under the named premises.

## Case B — saturated Q-hub star plus TT edge

At the quadruple hub,

```
r=4, d2=3, d1=5.
```

As in the protected D2=3 tranche, the no-three-consecutive-D1 premise forces every hub D1 ray to be adjacent to a D2 ray. All five hub D1 segments are therefore unavailable for clean-line charging.

The protected finite states have either

```
(D1,U) = (10,0)
```

or

```
(D1,U) = (11,1).
```

Again `h<=I-D2=9`, so at least nine lines are clean.

The maximum remaining charge capacities are respectively

```
(10-5) + 2*0 = 5,
(11-5) + 2*1 = 8.
```

Both are below nine.

Contradiction.

Thus the Q-hub star-plus-edge role-type is impossible.

## Case C — saturated T-hub star plus outer edge

The two T-hub roles differ only in whether the extra outer D2 edge is TT or TQ.

At the triple hub,

```
r=3, d2=3, d1=3.
```

The local fan premise forces the six rays to alternate D2,D1. As in the protected D2=3 tranche:

- all three hub D1 segments are unavailable for charging;
- the transverse lines of those three hub D1 segments force arrangement lines through all three leaf pairs.

The three spoke lines reduce the core-line count by at least three. The leaf-pair constraints reduce it by at least two more, whether the leaves are collinear or not. Hence

```
h <= I-5 = 8,
```

and at least ten lines are clean.

### Subcase (D1,U)=(10,0)

After removing the three unavailable hub D1 targets, the charge capacity is at most

```
10-3 = 7,
```

below the ten required clean-line charges.

Contradiction.

### Subcase (D1,U)=(11,1)

The outer D2 edge has at least one triple leaf endpoint in both role-types:

- TT has two;
- TQ has one.

That triple leaf has `d2=2`. In the `D1=11` state the protected local counts saturate its triple-point cap, so `d1=2`. By the local cyclic lemma, at least one of those leaf D1 segments is adjacent to D2 and is also unavailable for charging.

Thus at least four D1 targets are unavailable in total: three at the hub and one at a triple leaf.

Including the one unused segment, the maximum charge capacity is

```
(11-4) + 2*1 = 9,
```

below the ten required clean-line charges.

Contradiction.

Therefore both T-hub star-plus-edge role-types are impossible.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, profile 3334 has no `D2=4` realization at `n=18,T=95`.

Together with the protected D2=3 exclusion, the profile-3334 residual is reduced to the three `D2=5` K4-minus-one-edge role-types.

The companion replay `ci/validate_openmath_h1_12_3334_d2_4.py` checks the cyclic adjacency minima and all charge-capacity inequalities used above.

## Claim boundary

The finite cyclic enumeration, transverse-line use, and strengthened T-hub core-line count are independently reconstructed.

The conclusion remains source-conditional because it invokes the protected local no-long-run fan premise and clean-line charging map. It does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
