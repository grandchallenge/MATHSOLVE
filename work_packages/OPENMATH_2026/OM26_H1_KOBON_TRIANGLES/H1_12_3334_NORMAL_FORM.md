# H1-12 q=4 profile 3334 — graph and role normal form

**State:** `SOLVE_SOURCE_CONDITIONAL_NORMAL_FORM__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Assume the protected H1-12 hypotheses for a normalized `n=18, T=95` arrangement with exactly four finite multiple points and multiplicity profile

```
(3,3,3,4).
```

The protected saturated-core reduction leaves exactly 67 finite arithmetic/core-graph states for this profile. This note quotients those states by permutation of the three triple points and records the geometric consequences that follow from elementary-segment planarity and the already named local fan premise.

The result is a small set of role-types, not a proof that the profile is impossible.

## Two independent facts used here

### 1. D2 segments do not cross in their interiors

Every `D2` edge is an elementary arrangement segment joining two finite multiple points.

If two distinct `D2` segments crossed in their relative interiors, their supporting arrangement lines would meet at that crossing. The crossing would then be an arrangement vertex lying in the relative interior of both purported elementary segments, contradiction.

Therefore the straight-line graph formed by the `D2` segments is noncrossing.

This observation is independent of the source-scoped fan premise.

### 2. A saturated core is not an extreme core

The corrected saturated-core lemma proves, conditional on the named local no-long-run fan premise, that a convex-hull vertex cannot be saturated.

For four noncollinear cores, at least three cores are extreme. Hence at most one core can be saturated. A unique saturated core, when present, is the unique non-extreme core. It may be strictly interior to the triangle of the other three cores, or it may lie between two extreme cores on a hull edge; this tranche does **not** identify which.

## Exact profile identities

For `3334`,

```
I = 3+3+3+4 = 13,
S = 3+3+3+8 = 17,
delta = 3.
```

The defect identity is

```
3 = 17 + U - D1 - D2,
```

so

```
U = D1 + D2 - 14.
```

The protected finite replay and saturated-core reduction leave only

```
D2 in {3,4,5}.
```

## D2 = 3 — a three-spoke star

There are exactly four labeled finite states, collapsing to two role-types under permutation of the three triple cores.

The `D2` graph is necessarily the star `K_{1,3}`.

Its center is the unique saturated core and therefore, conditional on the local fan premise, the unique non-extreme core. The three leaves are extreme.

Two role-types remain:

1. **T-hub star** — a triple core is the saturated degree-3 hub; the quadruple core is a leaf.
2. **Q-hub star** — the quadruple core is the saturated degree-3 hub; all three leaves are triple cores.

In every `D2=3` state,

```
D1 = 11,
U = 0.
```

Thus every bounded elementary segment is incident to at least one counted triangle.

## D2 = 4 — cycle or star plus one outer edge

There are 51 labeled finite states. Their `D2` graphs have only two graph shapes.

### 4-cycle

The degree sequence is

```
(2,2,2,2).
```

No core is saturated. Up to permutation of the triple cores this is one role-type.

The exact local counts are

```
triple cores: d2=2, d1=2
quadruple core: d2=2, d1=4
D1=10
U=0.
```

The four `D2` segments form a noncrossing straight-line 4-cycle.

### Star plus one additional edge

The degree sequence is a permutation of

```
(3,2,2,1).
```

The degree-3 vertex is the unique saturated core. Conditional on the local fan premise it is the unique non-extreme core. Its three incident `D2` edges form the three spokes to the extreme cores; the fourth `D2` edge joins two of those extreme cores.

There are three role-types:

1. **T-hub + TT outer edge**;
2. **T-hub + TQ outer edge**;
3. **Q-hub + TT outer edge**.

Across these states,

```
(D1,U) is either (10,0) or (11,1).
```

The finite replay retains the exact local `d1` alternatives rather than collapsing them into an unsupported geometric equivalence.

## D2 = 5 — K4 minus one outer pair

There are 12 labeled finite states.

The `D2` graph is `K4` with one missing edge. Every state has exactly one saturated degree-3 core, hence conditionally one non-extreme core.

Because that saturated hub is adjacent by `D2` to all three other cores, the missing `K4` edge is between two of the three extreme cores.

There are three role-types:

1. **T-hub, missing TQ outer pair**;
2. **T-hub, missing TT outer pair**;
3. **Q-hub, missing TT outer pair**.

Every `D2=5` state has

```
D1 = 10,
U = 1.
```

The missing outer pair is not asserted to lack a common arrangement line; it is only absent from `D2`, i.e. its core-to-core segment is not a double-used elementary triangular side.

## Nine role-types

The 67 labeled finite states therefore collapse to exactly nine role-types:

| D2 | role-type |
|---:|---|
| 3 | T-hub star |
| 3 | Q-hub star |
| 4 | non-saturated 4-cycle |
| 4 | T-hub star + TT outer edge |
| 4 | T-hub star + TQ outer edge |
| 4 | Q-hub star + TT outer edge |
| 5 | T-hub K4-e, missing TQ outer pair |
| 5 | T-hub K4-e, missing TT outer pair |
| 5 | Q-hub K4-e, missing TT outer pair |

The companion replay `ci/validate_openmath_h1_12_3334_normal_form.py` recomputes this quotient directly from the protected q=4 enumerator and saturated-core filter.

## What this buys us

The `3334` residual is no longer “all four-core arrangements with these multiplicities.” It is a nine-type geometric problem.

The next proof work can be split cleanly:

1. **D2=3 star:** exploit `U=0` and a unique non-extreme saturated hub.
2. **D2=4 cycle:** analyze the noncrossing 4-cycle with no saturated core and `U=0`.
3. **D2=4 star-plus-edge:** separate the three hub/outer-edge role-types and the `U=0` versus `U=1` subcases.
4. **D2=5:** analyze the three `K4-e` role-types with exactly one unused bounded segment.

This is a finite proof programme. A construction search, if used at all, can target one role-type at a time rather than the unconstrained singular space.

## Claim boundary

The graph noncrossing lemma and the finite quotient are independently reconstructed.

The statement that a saturated hub is non-extreme remains conditional on the named local no-long-run fan premise. The broader clean-line/fan extraction used to reach the finite `3334` state set also remains source-scoped.

This artifact does not prove `3334` impossible, does not prove `T<=94`, and has no MATHCERT effect.
