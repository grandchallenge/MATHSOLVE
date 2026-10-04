GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: CMDG-P3M-N3-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-C
campaign: CMDG-CM4-N3
work_package: P3-M-FINITE-COEFFICIENT-ALLTRUE-005
assignment: CMDG-P3M-N3-WP-C
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/828

# WP-C — adversarial protected-type falsification of N3

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
dispatch_id: CMDG-P3M-N3-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-C
assignment: CMDG-P3M-N3-WP-C
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

Act adversarially against N3.

Search for a concrete failure in the actual protected chain:

```text
measurePointFunctional
→ liftedIntFunctionalDown
→ integral-basis coordinate weights
→ weightedBasisBooleanPairing
→ weightedBasisBooleanPairingR
→ finiteDeltaPullbackR
→ all-true evaluation
```

Protected N2 is discharged and must not be re-opened.

Prioritize:

1. a mismatch between packaged `basisBooleanCube X` and the literal
   `IntegralBasisIndex X → Bool` at all-true evaluation;
2. a lift/down defect in `R = ULift ℤ`;
3. a mismatch between `finiteDeltaPullbackR` and its descended integral form;
4. sign/order/evaluation defects in the weighted coefficient definition;
5. a genuine failure of the generic inverse identity for `liftedIntFunctionalDown`.

Use small genuine protected spaces when useful, such as a one-point profinite space or `Bool`.

Abstract groups, toy additive maps, or generic kernel models do not count.

If no counterexample survives, give a rigorous elimination ledger and identify the smallest remaining theorem that still requires formal compilation.

## Verification / falsification hooks

A valid falsification must specify concrete protected choices of
`X, μ, j, q`,
or for an upstream generic bridge,
`X, F, v`,
and demonstrate an actual inequality or ill-typed claimed equality.

Absence of a named theorem is not a counterexample.

## Success criterion

Preferred: a concrete protected-type counterexample.

Otherwise: a strong adversarial audit eliminating the suspected loss mechanisms and naming the first remaining proof obligation.
