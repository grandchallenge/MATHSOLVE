# H1-12 q=4 profile 3333 — blocked-target normal form

**State:** `SOLVE_SOURCE_CONDITIONAL_NORMAL_FORM__FINITE_REPLAYED__NOT_CERTIFIED`

## Scope

Continue from the protected H1-12 reductions for a normalized `n=18,T=95` arrangement with exactly four finite multiple points.

All four-core multiplicity profiles except

```
(3,3,3,3)
```

have now been excluded conditional on the named source-scoped fan and clean-line premises.

For profile `3333`,

```
I = 12,
S = 12,
delta = 3,
U = D1 + D2 - 9.
```

The protected saturated-core replay leaves 344 labeled finite arithmetic/core-graph states before the additional local refinement below.

## Blocked D1 targets

The protected transverse-line lemma gives:

> if a shared `D1` radial segment is adjacent in cyclic order to a `D2` radial segment at its multiple endpoint, then the transverse line through its ordinary endpoint contains another multiple point. The `D1` segment therefore cannot receive a clean-line charge.

Every core here is triple, so there are six cyclic radial rays. The named local fan premise forbids two consecutive `D1` rays.

For each local pair `(d1,d2)`, the companion replay exhausts the six-ray cyclic words and computes the minimum number of `D1` rays that must touch a `D2` ray.

The only positive minima occurring in the protected state set are

```
(d1,d2)=(2,2) -> at least 1 blocked D1 target,
(d1,d2)=(3,3) -> all 3 D1 targets blocked.
```

All other occurring local count pairs have lower bound zero at this level of information.

Let `B` be the sum of these local blocked-target lower bounds. Because every `D1` segment has exactly one multiple endpoint, these local blocked targets are distinct globally.

The clean-line lower bound is

```
18-h >= 18-(I-D2) = 6+D2.
```

After removing the blocked `D1` targets, the maximum clean-line charge capacity is

```
2U + D1 - B.
```

Thus every realizable state must satisfy

```
6+D2 <= 2U + D1 - B.
```

## Finite replay

Applying this necessary condition to the 344 protected labeled `3333` states leaves exactly 108.

The surviving `D2` histogram is

| D2 | labeled states |
|---:|---:|
| 1 | 6 |
| 2 | 15 |
| 3 | 36 |
| 4 | 39 |
| 5 | 12 |
| 6 | 0 |

In particular, the complete core graph `D2=6` is excluded already by the local blocked-target capacity refinement.

Quotienting the 108 states by all permutations of the four triple cores yields exactly 12 normal forms.

## Twelve normal forms

Here `cap` denotes `2U+D1-B` and `clean` denotes `6+D2`.

| # | D2 | core graph | local d1 by degree-normal form | D1 | U | B | clean | cap | labeled |
|---:|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1 | 1 | single edge | 2,2,2,2 | 8 | 0 | 0 | 7 | 8 | 6 |
| 2 | 2 | P3 + isolated | 2,2,2,2 | 8 | 1 | 1 | 8 | 9 | 12 |
| 3 | 2 | 2K2 | 2,2,2,2 | 8 | 1 | 0 | 8 | 10 | 3 |
| 4 | 3 | K1,3 | 1,2,2,2 | 7 | 1 | 0 | 9 | 9 | 4 |
| 5 | 3 | K1,3, saturated hub | 3,1,2,2 | 8 | 2 | 3 | 9 | 9 | 12 |
| 6 | 3 | K1,3, saturated hub | 3,2,2,2 | 9 | 3 | 3 | 9 | 12 | 4 |
| 7 | 3 | K3 + isolated | 2,2,2,2 | 8 | 2 | 3 | 9 | 9 | 4 |
| 8 | 3 | P4 | 2,2,2,2 | 8 | 2 | 2 | 9 | 10 | 12 |
| 9 | 4 | paw, saturated hub | 3,1,2,2 | 8 | 3 | 4 | 10 | 10 | 24 |
| 10 | 4 | paw, saturated hub | 3,2,2,2 | 9 | 4 | 5 | 10 | 12 | 12 |
| 11 | 4 | C4 | 2,2,2,2 | 8 | 3 | 4 | 10 | 10 | 3 |
| 12 | 5 | K4-e, saturated core | 1,3,2,2 | 8 | 4 | 5 | 11 | 11 | 12 |

The canonical vertex labels used by the replay retain the exact edge set, core degree, and local `d1` assignment; the table names only the graph shape and displayed canonical local counts.

## Equality surface

Six normal forms saturate the present charge inequality exactly:

- D2=3 non-saturated star;
- D2=3 saturated-star lower-count form;
- D2=3 triangle plus isolated core;
- D2=4 paw lower-count form;
- D2=4 four-cycle;
- D2=5 K4 minus one edge.

These equality forms are the highest-value next targets because every available charge slot is already forced to be used. Any additional unavailable `D1` target, any reduction in `U) endpoint capacity, or any stronger core-line incidence count excludes the form immediately.

The D2=5 form is especially constrained: it contains a saturated triple core and is already at equality.

## Result

Conditional on the protected source-scoped local fan and clean-line charging premises, the q=4 score-95 residual has been reduced to 12 profile-3333 normal forms. No `D2=6` state remains.

The companion replay `ci/validate_openmath_h1_12_3333_normal_form.py` reconstructs the 344-to-108 filter and the exact 12-orbit quotient from protected predecessor code.

## Next step

Resolve the tight equality strata first, beginning with the D2=5 `K4-e` form, then the D2=4 paw/C4 forms and the tight D2=3 forms. Keep the positive-slack forms separate.

The q>=5 residual remains independent of this four-core tranche.

## Claim boundary

The finite cyclic enumeration, blocked-target accounting, and symmetry quotient are independently reconstructed.

The reduction remains source-conditional because the local no-two-consecutive-`D1` premise and clean-line charging map retain their protected source scope. This artifact does not prove `T<=94`, does not certify optimality of the 93 construction, and has no MATHCERT effect.
