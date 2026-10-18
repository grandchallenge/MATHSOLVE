STATUS: DRAFT_NOT_ACTIVATED
CAMPAIGN: CMDG-CM4
TRANCHE: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
PROPOSED_COHORT: CMDG-P3M-N3-BLIND-COHORT-001
CONTEXT_CLASS: ZERO_CONTEXT
EXTERNAL_SOURCES: PROTECTED_PACKET_ONLY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

You are an independent zero-context mathematical contributor. This document is a complete bounded mathematical work-set, but it is not active until compiled into a GCL launch artifact with a bound return issue and lease identity.

Timebox when activated: 35 minutes of substantive work, then return the strongest exact result reached.

## Protected packet

Work only from this packet and standard mathematics. Do not inspect sibling work packages, cohort returns, campaign discussion threads, pull requests, unpublished notes, or unlisted source revisions.

Protected Programme authority:
`grandchallenge/MATH-PROGRAMME@a2897a270c477ac95ba3d18dd068a13b07d3b853`.

Protected facts:

1. `R = ULift ℤ`.
2. `measurePointFunctional X μ : LocallyConstant X R →ₗ[R] R`.
3. `measurePointIntegralFunctional X μ : LocallyConstant X ℤ →ₗ[ℤ] ℤ` is defined by `liftedIntFunctionalDown X (measurePointFunctional X μ)`.
4. `locallyConstantIntegralLiftEquiv X : LocallyConstant X ℤ ≃+* LocallyConstant X R` is an actual ring equivalence.
5. `locallyConstantIntegralDownEquiv X` is its inverse.
6. Protected N2 is admitted:
```lean
weightedBasisBooleanPairing_functionalWeight_allTrue
    (X : Profinite)
    (L : LocallyConstant X ℤ →ₗ[ℤ] ℤ)
    (v : LocallyConstant X ℤ) :
    weightedBasisBooleanPairing X
        (fun i => L (integralBasis X i)) v
        (fun _ => true) =
      L v
```
7. `weightedBasisBooleanPairingR` is the exact transport of the integral pairing through the coefficient equivalence.
8. `weightedFiniteBooleanCoefficient X a j q` is `weightedBasisBooleanPairingR X a (finiteDeltaPullbackR X j q)`.
9. The parent target remains only `d.hom.app (op Point) = 0`. Do not promote to `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

Protected source blobs:
- `CMDGCondensedCM4P3GPointFunctional.lean`: `1cefae23baacf758680763203abc1a748fe46733`
- `CMDGCondensedCM4P3GBasisBooleanPairing.lean`: `c54c506be4fde0f7aa92d83ab8e84d757520fcd7`
- `CMDGCondensedCM4P3GBasisBooleanPairingR.lean`: `3e580ac2648ed9166f332bac994a6b3763b660c0`
- `CMDGCondensedCM4P3JWeightedBooleanMeasure.lean`: `1e6fa7d520a5d79f931a94c2fabf4b0e95884a90`
- `CMDGCondensedCM4P3MFiniteQuotientBridge.lean`: `2ecf7b6fc546417828fbd7cc9473526042e5a511`

N2 direct axiom readback is `[propext, Classical.choice, Quot.sound]`; no `sorryAx`.

## Return discipline when activated

Return one narrative `GCL-CONTRIBUTION-RESULT/1` only. A theorem-grade reduction, exact Lean-sized blocker, or concrete protected-type counterexample is a successful return if correct. Do not create branches, pull requests, side files, or claim promotions.

# WP-D — weakest downstream closure after N3

PROPOSED_ASSIGNMENT_ID: CMDG-P3M-N3-WP-D
PROPOSED_DISPATCH_ID: CMDG-P3M-N3-WP-D-IA-001
PROPOSED_AGENT_REF: INDEPENDENT-AGENT-CMDG-N3-D

## Exact assignment

Assume N3 exactly as stated in the tranche README. Do not re-prove it.

Determine the shortest theorem-grade route from N3 to the parent target

```lean
d.hom.app (op Point) = 0
```

under the protected hypothesis

```lean
kernelProductFunctional X d = 0.
```

Test, in order, whether the next sufficient bridge can be stated at one of these strengths:

1. equality only after applying `d.hom.app (op Point)`;
2. equality after one-point reweight/evaluation;
3. finite weighted measure-morphism realization;
4. global all-true weighted measure coverage;
5. full one-point measure-section reconstruction.

Prefer the weakest sufficient item.

If the finite/global route is genuinely necessary, materialize a typed dependency ledger beginning with the protected N3 coefficient identity:

```text
N3_POINT_COEFFICIENT_EQUALITY
→ FINITE_COEFFICIENT_FAMILY_RECONSTRUCTION
→ FINITE_MEASURE_SECTION_REALIZATION
→ FINITE_MEASURE_MORPHISM_REALIZATION
→ QUOTIENT_COMPATIBILITY
→ GLOBAL_LIMIT_COVERAGE
→ APPLIED_D_COMPATIBILITY
→ POINT_COMPONENT_VANISHING
```

Identify the first unprotected arrow and write it as an exact Lean-sized proposition.

## Protected downstream facts to exploit

The protected source already contains:

- `weightedFiniteBooleanMeasureSection_coefficientFamily_transport`;
- `weightedFiniteBooleanMeasureSection_smallFree_transport`;
- quotient pushforward compatibility for the weighted finite construction;
- `weightedFiniteBooleanMeasureLimitLift_fac`;
- `weightedFiniteBooleanMeasureLimitLift_point_reweight`;
- `kernelProductSection_reweight_eval`;
- `kernelProductFunctional_eq_zero_of_solidification_kernel`;
- `measureFunctorMapConeIsLimit X`.

Do not demand a new theorem where an existing protected theorem plus a short specialization suffices.

## Verification / falsification hooks

Check whether the older finite-stage equality

```lean
μHom ≫ measureFunctor.map (finiteQuotientMap X j) =
  (Condensed.profiniteFree R).map qtrue ≫
    weightedFiniteBooleanMeasureHom X aμ j
```

is actually needed, or whether the action of `d` can be compared before reconstructing the full measure morphism.

Explicitly separate:

- what is already protected;
- what follows from N3 by finite coordinate extensionality;
- what requires a new hom-ext or limit argument;
- what is unnecessary strength.

## Success criterion

Preferred: a direct minimal compatibility theorem which, together with
`kernelProductFunctional X d = 0`, proves
`d.hom.app (op Point) = 0`.

Otherwise: the unique first missing theorem in the finite/global packaging chain, with exact protected types.

Do not promote beyond Point-component vanishing.
