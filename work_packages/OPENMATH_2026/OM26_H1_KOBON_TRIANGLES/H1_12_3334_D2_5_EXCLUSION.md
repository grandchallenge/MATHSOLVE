# H1-12 q=4 profile 3334 — D2=5 exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3334 normal form and the protected exclusions of `D2=3` and `D2=4`.

Every remaining `D2=5` state has:

```
D1 = 10,
U = 1,
I = 13,
```

a `K4`-minus-one-outer-edge core graph, and exactly one saturated degree-3 hub.

Up to the protected role quotient there are three cases:

1. T-hub, missing TQ outer pair;
2. T-hub, missing TT outer pair;
3. Q-hub, missing TT outer pair.

The missing outer pair does not affect the charge-capacity argument below.

This note reuses the protected transverse-line lemma:

> a shared D1 segment adjacent to a D2 spoke at its multiple endpoint has a non-clean transverse line at its ordinary endpoint and is unavailable as a clean-line charge target.

## Clean-line lower bound

For profile 3334,

```
I = 13.
```

With `D2=5`, the protected core-incidence inequality gives

```
h <= I-D2 = 8.
```

Hence at least

```
18-h >= 10
```

arrangement lines are clean.

The clean-line charging map therefore requires at least ten charge targets.

## Case A — saturated triple hub

At a saturated triple hub,

```
r=3,
d2=3,
d1=3.
```

The named local no-long-run fan premise forbids two consecutive D1 rays. With three D1 and three D2 rays on a six-cycle, the pattern must alternate.

Thus every hub D1 ray is adjacent to D2, so all three hub D1 segments are unavailable for charging by the transverse-line lemma.

The total remaining charge capacity is at most

```
(D1-3) + 2U
= (10-3) + 2
= 9.
```

But there are at least ten clean lines.

Contradiction.

Therefore both T-hub `D2=5` role-types are impossible under the named premises.

## Case B — saturated quadruple hub

At a saturated quadruple hub,

```
r=4,
d2=3,
d1=5.
```

The local fan premise forbids three consecutive D1 rays. With five D1 and three D2 rays on an eight-cycle, every D1 ray must be adjacent to at least one D2 ray; otherwise it would lie in the middle of three consecutive D1 rays.

Hence all five hub D1 segments are unavailable for charging.

The remaining charge capacity is at most

```
(D1-5) + 2U
= (10-5) + 2
= 7,
```

again below the ten required clean-line charges.

Contradiction.

Therefore the Q-hub `D2=5` role-type is impossible.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, profile `3334` has no realization at `n=18,T=95`.

Together with the protected q=4 multiplicity and saturated-core reductions, the entire four-core score-95 residual is now reduced to profile

```
3333.
```

The companion replay `ci/validate_openmath_h1_12_3334_d2_5.py` verifies the hub cyclic patterns and charge-capacity inequalities.

## Claim boundary

The finite cyclic deductions and charge-capacity arithmetic are independently reconstructed.

The conclusion remains source-conditional because it invokes the protected local no-long-run fan premise and clean-line charging map. It does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
