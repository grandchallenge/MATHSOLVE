GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: CMDG-P3M-COV-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-B
campaign: CMDG-CM4
work_package: P3-M-WEIGHTED-ONE-POINT-COVERAGE-004
assignment: CMDG-P3M-COV-WP-B
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/801

# WP-B — weakest operational vanishing bridge

You are an independent zero-context mathematical contributor. This document is your complete bounded work-set.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

## Protected packet

Work only from this packet and standard mathematics. Do not inspect other cohort returns, campaign discussion threads, pull requests, unpublished notes, or sibling dispatches.

Protected Programme authority is `grandchallenge/MATH-PROGRAMME@fdd7a3fe3df7b2d699753347080c1cbc2127e02d`.

The protected setting is the CMDG CM4 P3-M one-point separation route. Let
```lean
X : Profinite
μ : (measurePresheafObj X).obj (op Point)
d : (Condensed.profiniteSolid R).obj X ⟶ coefficientObject
```

Protected facts and definitions:

1. `measurePointProjection_zero_reflects` is admitted:
   `measurePointProjection X μ = 0 → μ = 0`.
2. `measurePointFunctional X μ` is obtained by restricting the projected one-point measure to constant one-point coefficient families and evaluating at the unique point.
3. `measurePointIntegralFunctional X μ : LocallyConstant X ℤ →ₗ[ℤ] ℤ` is the protected integer functional derived from `measurePointFunctional`.
4. `integralBasis X` is the protected Nöbeling basis of `LocallyConstant X ℤ`.
5. Define the coordinate vector
   `aμ i := measurePointIntegralFunctional X μ (integralBasis X i)`.
6. `weightedFiniteBooleanMeasureLimitLift X a` is the protected global weighted measure family obtained from compatible finite-stage weighted measure morphisms.
7. `basisBooleanPointProbe X (fun _ => true)` is the all-true point selector.
8. `weightedFiniteBooleanMeasureLimitLift_point_reweight` and `kernelProductSection_reweight_eval` are protected.
9. For a solidification-kernel morphism `d`, the admitted predecessor theorem
   `kernelProductFunctional_eq_zero_of_solidification_kernel`
   gives `kernelProductFunctional X d = 0`.
10. The current parent target remains only
    `d.hom.app (op Point) = 0`.
    Do not promote to `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

Protected source blobs at the Programme predecessor:
- `CMDGCondensedCM4P3GPointFunctional.lean`: `1cefae23baacf758680763203abc1a748fe46733`
- `CMDGCondensedCM4P3LKernelFunctional.lean`: `2cc242f6bbb9a055db0d71b19f5a49973cfb4fbb`
- `CMDGCondensedCM4P3JWeightedBooleanMeasure.lean`: `1e6fa7d520a5d79f931a94c2fabf4b0e95884a90`

The predecessor zero-reflection theorem has direct axiom readback
`[propext, Classical.choice, Quot.sound]`; no `sorryAx`.

## Independence and authority

This dispatch belongs to blind cohort `CMDG-P3M-COV-BLIND-COHORT-001`.

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. A reduction, exact blocker, or counterexample is a successful return if correct.

## Required return

Post exactly one narrative-only comment on the intended GitHub issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-COV-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-COV-B
assignment: CMDG-P3M-COV-WP-B
disposition: <PROVED_REDUCTION|EXACT_CERTIFICATE|FORMAL_LEMMA_PROVED|COUNTEREXAMPLE|NO_MATERIAL_DELTA|EXACT_BLOCKER>
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: <YES|NO>

## Strongest exact statement
...

## Derivation
...

## Assumptions beyond bootstrap
...

## Verification / falsification hooks
...

## Claim boundary
...

## Next residual
...
```

No URLs, attachments, side files, branches, pull requests, or second mathematical comment. The first valid conforming return is the durable contribution.

## Exact assignment

Avoid proving unnecessary reconstruction.

Assume
```lean
hk : kernelProductFunctional X d = 0
```
and attack the exact target
```lean
d.hom.app (op Point) = 0
```
using only the weakest weighted one-point compatibility statement actually required.

A natural route is: for arbitrary one-point measure section `μ`, express or compare the value of the Point component of the protected composite through the weighted all-true family built from
`aμ i := measurePointIntegralFunctional X μ (integralBasis X i)`.
If equality after applying `d` is enough, stop there; do not prove equality of measure sections merely for strength.

Identify the minimal theorem which, together with `hk` and protected N1 zero-reflection if needed, forces the Point component to vanish.

## Required verification / falsification hooks

Explicitly test whether the needed bridge is:
1. full section reconstruction;
2. equality only after `measurePointProjection`;
3. equality only after applying the Point component of `d`;
4. direct equality with `kernelProductFunctional X d aμ`.
Prefer the weakest sufficient item.

## Success criterion

Preferred: a direct theorem-grade derivation of `d.hom.app (op Point) = 0` from `kernelProductFunctional X d = 0`. Otherwise return the unique smallest missing compatibility lemma.
