GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-N3-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-A
assignment: CMDG-P3M-N3-WP-A
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The protected N3 target reduces directly to the inverse law for the integral/lifted locally-constant-function equivalence and the defining lift/down equation for `liftedIntFunctionalDown`. At the protected types, the following is the direct proof shape:

```lean
theorem weightedFiniteBooleanCoefficient_measurePoint_allTrue
    (X : Profinite.{u})
    (μ : (measurePresheafObj X).obj (op Point))
    (j : DiscreteQuotient X)
    (q : (FiniteQuotientObject X j).obj) :
    weightedFiniteBooleanCoefficient X
        (fun i => measurePointIntegralFunctional X μ (integralBasis X i))
        j q (fun _ => true) =
      measurePointFunctional X μ (finiteDeltaPullbackR X j q) := by
  change
    ULift.up
      (weightedBasisBooleanPairing X
        (fun i => measurePointIntegralFunctional X μ (integralBasis X i))
        (locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q))
        (fun _ => true)) =
      measurePointFunctional X μ (finiteDeltaPullbackR X j q)
  rw [weightedBasisBooleanPairing_functionalWeight_allTrue]
  have hdown :
      locallyConstantIntegralLiftEquiv X
          (locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q)) =
        finiteDeltaPullbackR X j q := by
    change
      locallyConstantIntegralLiftEquiv X
          ((locallyConstantIntegralLiftEquiv X).symm
            (finiteDeltaPullbackR X j q)) =
        finiteDeltaPullbackR X j q
    exact (locallyConstantIntegralLiftEquiv X).apply_symm_apply _
  change
    ULift.up
      ((measurePointFunctional X μ
        (locallyConstantIntegralLiftEquiv X
          (locallyConstantIntegralDownEquiv X
            (finiteDeltaPullbackR X j q)))).down) =
      measurePointFunctional X μ (finiteDeltaPullbackR X j q)
  rw [hdown]
  rfl
```

If the final `change` is rejected solely because `liftedIntFunctionalDown` is not unfolded at the active transparency setting, the unique Lean-sized helper is:

```lean
theorem liftedIntFunctionalDown_integralDown
    (X : Profinite.{u})
    (F : LocallyConstant X R →ₗ[R] R)
    (v : LocallyConstant X R) :
    ULift.up
        (liftedIntFunctionalDown X F
          (locallyConstantIntegralDownEquiv X v)) =
      F v := by
  have h :
      locallyConstantIntegralLiftEquiv X
          (locallyConstantIntegralDownEquiv X v) = v := by
    change locallyConstantIntegralLiftEquiv X
        ((locallyConstantIntegralLiftEquiv X).symm v) = v
    exact (locallyConstantIntegralLiftEquiv X).apply_symm_apply v
  change
    ULift.up
      ((F
        (locallyConstantIntegralLiftEquiv X
          (locallyConstantIntegralDownEquiv X v))).down) =
      F v
  rw [h]
  rfl
```

With that helper, N3 closes after the N2 rewrite by exactly one application of `liftedIntFunctionalDown_integralDown`.

## Derivation

1. Unfolding `weightedFiniteBooleanCoefficient` and `weightedBasisBooleanPairingR` at the all-true selector yields exactly
   `ULift.up (weightedBasisBooleanPairing ... (fun _ => true))`. This normalization is already exhibited at the same protected types by the protected theorem `weightedFiniteBooleanCoefficient_evaluationWeight_allTrue`.
2. Apply protected N2 with
   `L := measurePointIntegralFunctional X μ` and
   `v := locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q)`.
   The left side becomes
   `ULift.up (measurePointIntegralFunctional X μ (locallyConstantIntegralDownEquiv X (finiteDeltaPullbackR X j q)))`.
3. By definition,
   `measurePointIntegralFunctional X μ = liftedIntFunctionalDown X (measurePointFunctional X μ)`.
4. The only transported argument is
   `locallyConstantIntegralLiftEquiv X (locallyConstantIntegralDownEquiv X v)`.
   Since `locallyConstantIntegralDownEquiv X` is definitionally the inverse ring equivalence, `RingEquiv.apply_symm_apply` gives this as `v`.
5. The remaining scalar equality is `ULift.up ((measurePointFunctional X μ v).down) = measurePointFunctional X μ v`, which is the constructor/projection reconstruction for `ULift`.

Thus there is no additional mathematical obstruction between protected N2 and N3.

## Assumptions beyond bootstrap

None. No sibling return, campaign discussion, pull request, unpublished note, or unlisted source revision was inspected. The derivation uses only the protected packet, the five listed protected blobs, and standard Lean equivalence/ULift laws.

## Verification / falsification hooks

- The all-true selector is accepted on the packaged Boolean cube after the same `change` used by the protected finite-stage evaluation-weight theorem.
- `weightedBasisBooleanPairingR` exposes the integral weighted pairing through `basisBooleanIntegralLiftEquiv`; evaluation at all-true is therefore the displayed `ULift.up` expression.
- `locallyConstantIntegralLiftEquiv X (locallyConstantIntegralDownEquiv X v) = v` is not relied on as definitional equality; the proof explicitly uses `apply_symm_apply`.
- The only possible elaboration-sensitive point is unfolding `liftedIntFunctionalDown` in the final `change`. If that transparency step is unavailable, the narrowly scoped helper above is the exact first materialization target and removes it.
- No use is made of finite measure sections, global limits, the solidification-kernel theorem, or Point-component vanishing.

## Claim boundary

This return establishes only the N3 coefficient identity/reduction at one finite quotient point and the all-true Boolean selector. It does not claim `d.hom.app (op Point) = 0`, `d = 0`, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

## Next residual

Materialize the displayed theorem in the protected Lean environment. If the direct final `change` unfolds `liftedIntFunctionalDown`, N3 is closed immediately. Otherwise materialize exactly `liftedIntFunctionalDown_integralDown` and use it after the N2 rewrite; no larger helper is required.