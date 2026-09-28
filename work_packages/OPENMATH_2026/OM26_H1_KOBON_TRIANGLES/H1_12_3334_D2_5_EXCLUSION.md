# H1-12 q=4 profile 3334 — D2=5 exclusion

**State:** `SOLVE_SOURCE_CONDITIONAL_GEOMETRIC_REDUCTION__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected profile-3334 normal form and the protected D2=3 and D2=4 exclusions for a normalized `n=18,T=95` arrangement.

The only remaining profile-3334 role-types have

```
D2 = 5,
D1 = 10,
U = 1,
```

and D2 graph `K4` minus one outer-core edge. The protected normal form gives exactly three role-types:

1. saturated triple hub, missing TQ outer pair;
2. saturated triple hub, missing TT outer pair;
3. saturated quadruple hub, missing TT outer pair.

This note excludes all three conditional on the already named local no-long-run fan premise and clean-line charging map.

It reuses the independently reconstructed transverse-line lemma from the protected D2=3 tranche:

> a shared D1 segment whose cyclic neighbor at its multiple endpoint is a D2 spoke has a non-clean transverse line at its ordinary endpoint and is unavailable as a clean-line charge target.

## Common clean-line lower bound

For profile 3334,

```
I = 13.
```

With `D2=5`, the core-incidence bound gives

```
h <= I-D2 = 8.
```

Therefore at least

```
18-h >= 10
```

arrangement lines are clean.

Every clean line must emit one charge under the protected charging map.

## Case A — saturated triple hub

At a triple hub,

```
r=3,
d2=3,
d1=3.
```

The local no-long-run fan premise forbids two consecutive D1 rays. Since the six saturated rays consist of three D1 and three D2 rays, they must alternate.

Hence every hub D1 ray is adjacent to D2 on both sides. By the transverse-line lemma, all three hub D1 segments are unavailable as clean-line charge targets.

The total possible clean-line charge capacity is therefore at most

```
(D1-3) + 2U
= (10-3) + 2
= 9.
```

But at least ten clean lines require charges.

Contradiction.

This excludes both triple-hub role-types, independently of whether the missing outer pair is TT or TQ.

## Case B — saturated quadruple hub

At a quadruple hub,

```
r=4,
d2=3,
d1=5.
```

The local no-long-run fan premise forbids three consecutive D1 rays. With five D1 and three D2 rays on the saturated eight-ray cycle, every D1 ray must be adjacent to at least one D2 ray; otherwise that D1 would be the middle ray of a forbidden three-D1 block.

Thus all five hub D1 segments are unavailable as clean-line charge targets.

The total capacity is at most

```
(D1-5) + 2U
= (10-5) + 2
= 7,
```

again below the ten required clean-line charges.

Contradiction.

Therefore the quadruple-hub role-type is impossible.

## Result

Conditional on the named source-scoped local fan and clean-line charging premises, profile 3334 has no `D2=5` realization at `n=18,T=95`.

Together with the protected D2=3 and D2=4 exclusions, **profile 3334 is completely excluded** from the four-core score-95 residual.

The four-core residual is therefore reduced to profile

```
3333
```

only.

The companion replay `ci/validate_openmath_h1_12_3334_d2_5.py` checks the cyclic hub consequences and charge-capacity inequalities used above.

## Claim boundary

The finite cyclic deductions and transverse-line use are independently reconstructed.

The conclusion remains source-conditional because it invokes the protected local no-long-run fan premise and clean-line charging map. It does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect. The remaining four-core profile 3333 and all q>=5 cases remain open.
