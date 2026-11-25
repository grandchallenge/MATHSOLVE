GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: CMDG-CM4
TRANCHE: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
ASSIGNMENT_ID: CMDG-P3M-N3-WP-B
DISPATCH_ID: CMDG-P3M-N3-WP-B-IA-001
AGENT_REF: INDEPENDENT-AGENT-CMDG-N3-B
PROTECTED_LEASE_IDENTITY: CMDG-P3M-N3-WP-B :: CMDG-P3M-N3-WP-B-IA-001 :: INDEPENDENT-AGENT-CMDG-N3-B
INTENDED_RETURN: https://github.com/grandchallenge/MATHSOLVE/issues/827
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
EXECUTION_AUTHORIZED: YES
PROTECTED_PROGRAMME_PREDECESSOR: a2897a270c477ac95ba3d18dd068a13b07d3b853
PROTECTED_SOLVE_PLAN: 91725687ef26d01acc4989474b124517221716e3
BLIND_COHORT: CMDG-P3M-N3-BLIND-COHORT-001

Read this entire immutable task. Execute only this bounded assignment. Before substantive work, verify that your environment can post one authenticated GitHub issue comment to INTENDED_RETURN. If it cannot, report RETURN_TRANSPORT_UNAVAILABLE and do not begin substantive work.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: CMDG-P3M-N3-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-B
campaign: CMDG-CM4-N3
work_package: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
assignment: CMDG-P3M-N3-WP-B
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/827

# WP-B — isolate the coefficient-transport bridge

You are an independent zero-context mathematical contributor. This document is your complete bounded work-set.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

## Protected packet

Work only from this packet and standard mathematics. Do not inspect sibling work packages, sibling returns, campaign discussion threads, pull requests, unpublished notes, or unlisted source revisions.

Protected Programme authority is `grandchallenge/MATH-PROGRAMME@a2897a270c477ac95ba3d18dd068a13b07d3b853`.

Protected setting:

```lean
X : Profinite
μ : (measurePresheafObj X).obj (op Point)
d : (Condensed.profiniteSolid R).obj X ⟶ coefficientObject
```

Protected facts and definitions:

1. `R = ULift ℤ`.
2. `measurePointFunctional X μ : LocallyConstant X R →ₗ[R] R`.
3. `measurePointIntegralFunctional X μ : LocallyConstant X ℤ →ₗ[ℤ] ℤ` is defined by
   `liftedIntFunctionalDown X (measurePointFunctional X μ)`.
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
8. `weightedFiniteBooleanCoefficient X a j q` is the weighted lifted pairing applied to `finiteDeltaPullbackR X j q`.
9. `kernelProductFunctional_eq_zero_of_solidification_kernel` is protected.
10. The parent target remains only `d.hom.app (op Point) = 0`.
    Do not promote to `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

Protected source blobs:
- `CMDGCondensedCM4P3GPointFunctional.lean`: `1cefae23baacf758680763203abc1a748fe46733`
- `CMDGCondensedCM4P3GBasisBooleanPairing.lean`: `c54c506be4fde0f7aa92d83ab8e84d757520fcd7`
- `CMDGCondensedCM4P3GBasisBooleanPairingR.lean`: `3e580ac2648ed9166f332bac994a6b3763b660c0`
- `CMDGCondensedCM4P3JWeightedBooleanMeasure.lean`: `1e6fa7d520a5d79f931a94c2fabf4b0e95884a90`
- `CMDGCondensedCM4P3MFiniteQuotientBridge.lean`: `2ecf7b6fc546417828fbd7cc9473526042e5a511`

N2 direct axiom readback is `[propext, Classical.choice, Quot.sound]`; no `sorryAx`.

## Authority boundary

You have no repository mutation, adjudication, certification, merge, publication, or claim-promotion authority. A theorem-grade reduction, exact blocker, or concrete protected-type counterexample is a successful return if correct.

## Required return

Post exactly one narrative-only comment on the intended GitHub issue:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-N3-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-B
assignment: CMDG-P3M-N3-WP-B
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

Use only:

- the definition of `liftedIntFunctionalDown`;
- the equivalence `locallyConstantIntegralLiftEquiv X`;
- `R = ULift ℤ`.

Do not use N2, finite quotients, weighted pairings, measure sections, global limits, or `d`.

If the generic theorem is too strong for a genuine definitional reason, isolate the weakest exact specialization sufficient for

```lean
F := measurePointFunctional X μ
v := finiteDeltaPullbackR X j q.
```

## Verification / falsification hooks

Test separately:

1. both inverse laws of `locallyConstantIntegralLiftEquiv X`;
2. whether `ULift.up ((F v).down) = F v` closes by `rfl` or a standard `ULift` identity;
3. scalar/coercion mismatches between the descended `ℤ`-linear functional and original `R`-linear functional;
4. whether any local-constancy/topology information is lost during the coefficient equivalence.

## Success criterion

Preferred: a generic theorem that turns the final step of N3 into one rewrite.

Acceptable: an exact specialized bridge for `measurePointFunctional`, or a concrete protected-type refutation.

Do not return packet-local uncertainty as a blocker if the protected equivalence laws resolve it.
