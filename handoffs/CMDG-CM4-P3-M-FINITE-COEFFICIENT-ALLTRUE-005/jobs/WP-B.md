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

# WP-B — isolate the coefficient-transport bridge

PROPOSED_ASSIGNMENT_ID: CMDG-P3M-N3-WP-B
PROPOSED_DISPATCH_ID: CMDG-P3M-N3-WP-B-IA-001
PROPOSED_AGENT_REF: INDEPENDENT-AGENT-CMDG-N3-B

## Exact assignment

Ignore the weighted Boolean construction. Prove or refute the generic coefficient-transport identity needed by N3.

Preferred target:

```lean
theorem liftedIntFunctionalDown_apply_inverse
    (X : Profinite.{u})
    (F : LocallyConstant X R →ₗ[R] R)
    (v : LocallyConstant X R) :
    ULift.up
        (liftedIntFunctionalDown X F
          ((locallyConstantIntegralLiftEquiv X).symm v)) =
      F v
```

An equivalent formulation using `locallyConstantIntegralDownEquiv X v` is acceptable.

The theorem should use only:

- the definition of `liftedIntFunctionalDown`;
- the fact that `locallyConstantIntegralLiftEquiv X` is an equivalence;
- `R = ULift ℤ`.

Do not use N2, finite quotients, weighted pairings, measure sections, or `d`.

If the generic theorem is too strong for a definitional reason, find the weakest exact specialization sufficient for

```lean
F := measurePointFunctional X μ
v := finiteDeltaPullbackR X j q.
```

## Verification / falsification hooks

Test:

1. inverse laws for `locallyConstantIntegralLiftEquiv X`;
2. whether `ULift.up ((F v).down) = F v` closes by `rfl`, extensionality, or a standard `ULift` theorem;
3. scalar linearity/coercion mismatches between the `ℤ)-linear descended functional and the original `R)-linear functional;
4. whether any topology or local-constancy information is lost during the coefficient equivalence.

## Success criterion

Preferred: a theorem-grade generic bridge that turns the final step of N3 into one rewrite.

Acceptable: an exact specialized bridge for `measurePointFunctional`, or a concrete protected-type refutation.

Do not return packet-local uncertainty as a blocker without checking the actual equivalence laws supplied in the protected packet.
