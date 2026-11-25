# CMDG P3-M one-point separation — independent synthesis and native-node selection

Date: 2026-10-03

## Protected inputs

Evidence base: `MATHSOLVE@26e95c754e74af54cee48931cce89100b374f9ef`.

Blind cohort closure: `MATHSOLVE@0c3e2005d65f18f54b85d2d87cc2f03283aedbcf`.

Protected contributor returns:

- WP-A, issue #764, comment `5969485351`, declared `PROVED_REDUCTION`.
- WP-B, issue #765, comment `5969496865`, declared `PROVED_REDUCTION`.
- WP-C, issue #766, comment `5969500125`, declared `COUNTEREXAMPLE`.
- WP-D, issue #767, comment `5969497105`, declared `EXACT_BLOCKER`.

These returns are evidence only. This document is a fresh GCL-owned comparison and node selection. It does not adopt contributor dispositions as authority.

Protected Programme predecessor for the current frontier:
`MATH-PROGRAMME@f7f99e18b83a3015d1a7ef835ee71434d01a9dba`.

Current Programme replay baseline during synthesis:
`MATH-PROGRAMME@b54739bda525f78790dad00a2f59a889522f0034`.

## Comparison of the four returns

### WP-A

WP-A establishes the correct algebraic reduction: values on the protected Nöbeling basis determine the ordinary integral functional
`measurePointIntegralFunctional X μ`.
That does **not** by itself determine the original one-point measure section.

Its remaining requirements are:

1. a construction-side identity showing the weighted one-point realization has the same integral functional as `μ`; and
2. a zero-reflection/injectivity statement for the map from one-point measure sections to that functional.

This correctly rules out treating basis completeness as section-level reconstruction.

### WP-B

WP-B sharpens the one-point geometry. Since `Point = CompHaus.of PUnit`, locally constant families on `Point` are constant and are determined by evaluation at the unique point.

Thus no genuine information loss is forced by the final constant-family/evaluation step. The first possible information-loss boundary lies before that, at
`measurePointProjection`.

WP-B also correctly notes that a separate compatibility bridge is still needed from zero `kernelProductFunctional` data to the relevant one-point measure observable.

### WP-C

WP-C gives a valid logical countermodel to derivability from the dispatch packet alone:

`M = ℤ ⊕ ℤ → ℤ`, `(a,b) ↦ a`.

The vector `(0,1)` is invisible to every downstream observable that factors through this projection.

This proves an important negative statement: **no amount of downstream basis or weighted-family completeness can recover information already discarded by a noninjective first projection.**

It does **not** prove that the concrete Lean object `measurePresheafObj` has such a ghost summand. The countermodel is therefore a falsification hook for the concrete projection, not a concrete campaign counterexample.

### WP-D

WP-D independently identifies the same first unproved arrow:
`measurePointProjection`.

It also identifies the strictly smallest goal-specific theorem needed at this arrow:

```lean
measurePointProjection X μ = 0 → μ = 0
```

This is weaker than full injectivity and is exactly the zero-separation property needed by the current successor route.

## Independent protected-source replay

The concrete Programme definitions are materially stronger than the abstract packet.

At the pinned mathlib commit
`79d0395a1825a6264ad5d269e35e60537518955e`,
`Mathlib/Condensed/Discrete/Module.lean` proves:

- `CondensedMod.LocallyConstant.functorIsoDiscrete`;
- `CondensedMod.LocallyConstant.adjunction`;
- `CondensedMod.LocallyConstant.fullyFaithfulFunctor`;
- `Full` and `Faithful` instances for `CondensedMod.LocallyConstant.functor`.

The protected P2-D construction defines both the source and coefficient presheaves using this locally-constant/discrete interface:

```lean
discreteContinuousPresheaf
coefficientPresheaf
```

and defines

```lean
measurePresheafObj S :=
  functorEnrichedHom (ModuleCat R)
    (discreteContinuousPresheaf.obj (op S))
    coefficientPresheaf
```

The protected P3-G point-functional module defines
`measurePointProjection X μ` by evaluating the enriched-Hom section at the identity object of
`Under (op Point)`.

Therefore WP-C's abstract ghost-summand model is not yet evidence that the concrete projection fails. The concrete source has enough discrete/full-faithful structure that zero-reflection is a plausible theorem and must be tested directly in the pinned formal environment.

No protected theorem currently states this zero-reflection property. It must not be assumed.

## Selected native node

`CMDG-P3M-SEP-N1 — MEASURE_POINT_PROJECTION_ZERO_REFLECTION`

### Exact target

In the protected namespace and pinned environment, prove or refute:

```lean
theorem measurePointProjection_zero_reflects
    (X : Profinite.{u})
    (μ : (measurePresheafObj X).obj (op Point))
    (hμ : measurePointProjection X μ = 0) :
    μ = 0
```

Equivalent stronger formulations such as
`Function.Injective (measurePointProjection X)`
are acceptable only if they fall out naturally; they are not required.

### Native proof route to test first

Use the actual enriched/discrete structure, not the abstract packet:

1. unfold only enough of `measurePresheafObj` to expose the enriched-Hom/end;
2. use the point component `measurePointProjection`;
3. exploit naturality against point probes and/or the full-faithful locally-constant/discrete functor;
4. show every component of the enriched section is forced to zero by the identity-point component;
5. conclude `μ = 0` by end/enriched-Hom extensionality.

### Native falsification route

A refutation must be concrete at the protected types. It must exhibit

```lean
μ : (measurePresheafObj X).obj (op Point)
```

with

```lean
μ ≠ 0
measurePointProjection X μ = 0
```

for some protected `X`.

An abstract additive model such as `ℤ ⊕ ℤ → ℤ` is insufficient for refutation once the actual enriched/discrete definitions are in scope.

## Why N1 is the smallest theorem-grade node

- All four independent returns converge on the first projection as the earliest unresolved information boundary.
- The goal-specific zero-reflection statement is strictly weaker than full reconstruction or full injectivity.
- It is upstream of the weighted-family reconstruction question.
- It can be proved or falsified entirely inside the already protected P2-D/P3-G point-functional interface.
- It directly decides whether WP-C's logical obstruction can occur in the concrete implementation.

## What N1 does not close

Even if N1 is proved, #1162 is not yet complete.

The next residual is the construction/coverage bridge:

for arbitrary
`μ : (measurePresheafObj X).obj (op Point)`,
let

```lean
aμ i := measurePointIntegralFunctional X μ (integralBasis X i)
```

and compare `μ` with the all-true one-point section generated by the protected weighted-Boolean measure construction using `aμ`.

The next theorem should be only as strong as necessary. Preferred form:

```text
the generated weighted one-point section has the same
measurePointProjection as μ
```

or an even weaker statement sufficient after applying the one-point component of `d`.

Only after that bridge and N1 may zero `kernelProductFunctional` data be promoted to zero of the one-point component.

## Advancement rule

- If N1 is **proved**, open the weighted one-point coverage/compatibility node.
- If N1 is **refuted concretely**, stop the current #1162 route and classify the actual kernel of `measurePointProjection`; any successor must add a genuinely separating observable or bypass this projection.
- If N1 is **reduced**, preserve the smallest exact missing extensionality/full-faithfulness lemma and attack only that lemma.

Do not advance directly to `d = 0`, mapping-out injectivity, coefficient-object solidity, P3 completion, or CM4 completion.

## Claim boundary

This synthesis selects a bounded native proof/falsification node. It does not prove zero-reflection, one-point separation, `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.
