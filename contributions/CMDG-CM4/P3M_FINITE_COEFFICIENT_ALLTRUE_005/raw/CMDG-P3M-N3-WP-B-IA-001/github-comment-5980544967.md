GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-N3-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-B
assignment: CMDG-P3M-N3-WP-B
disposition: FORMAL_LEMMA_PROVED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

The generic coefficient-transport identity holds for every lifted-coefficient linear functional; no specialization to the measure functional is required.

```lean
theorem liftedIntFunctionalDown_apply_inverse
    (X : Profinite.{u})
    (F : LocallyConstant X R →ₗ[R] R)
    (v : LocallyConstant X R) :
    ULift.up
        (liftedIntFunctionalDown X F
          ((locallyConstantIntegralLiftEquiv X).symm v)) =
      F v := by
  simpa [liftedIntFunctionalDown]
```

Equivalently, writing `e := locallyConstantIntegralLiftEquiv X`, the statement is
`ULift.up (liftedIntFunctionalDown X F (e.symm v)) = F v`.

## Derivation

By definition of `liftedIntFunctionalDown`, for any integral locally constant function `z`,
`liftedIntFunctionalDown X F z = (F (e z)).down`.
Therefore at `z := e.symm v` the left side is
`ULift.up ((F (e (e.symm v))).down)`.

Because `e` is an actual ring equivalence, its inverse law gives
`e (e.symm v) = v`.
The expression therefore becomes
`ULift.up ((F v).down)`, which is exactly `F v` by the `ULift` constructor/projection identity.

The reverse inverse law is also exact: for every `z : LocallyConstant X ℤ`,
`e.symm (e z) = z`. It is not needed for this direction, but confirms that the coefficient transport is genuinely two-sided.

No scalar mismatch survives in the application identity. The descended map is ℤ-linear, but evaluation followed by `.down` is exactly undone by `ULift.up`; no comparison of scalar actions is needed after unfolding.

No local-constancy or topology information is lost: the transport is through a ring equivalence whose source and target are the full `LocallyConstant` objects, so the inverse law applies to the original `v` itself.

## Assumptions beyond bootstrap

None.

## Verification / falsification hooks

1. Check both protected equivalence laws separately:
   `(locallyConstantIntegralLiftEquiv X).apply_symm_apply v` and
   `(locallyConstantIntegralLiftEquiv X).symm_apply_apply z`.
2. After unfolding `liftedIntFunctionalDown` and rewriting the first law, the only residual goal is
   `ULift.up ((F v).down) = F v`; this is the standard `ULift` eta identity and is definitionally trivial after exposing the `ULift` constructor.
3. The compact Lean check is the theorem body `by simpa [liftedIntFunctionalDown]`. If this does not elaborate, the only legitimate failure point is syntactic unfolding/simp registration, not a mathematical obstruction; the expanded proof is exactly the two equalities above.
4. A counterexample would require either failure of an inverse law for the protected ring equivalence or failure of `ULift.up x.down = x`; both contradict the protected types/definitions.

## Claim boundary

This proves only the generic coefficient-transport bridge requested by WP-B. It does not use or establish N2, finite-quotient reconstruction, weighted Boolean pairing, measure-section separation, the parent equality `d.hom.app (op Point) = 0`, `d = 0`, coefficient solidity, P3 completion, or CM4 completion.

## Next residual

In N3, instantiate the lemma with
`F := measurePointFunctional X μ` and
`v := finiteDeltaPullbackR X j q`.
That turns the coefficient descent/re-lift part of the final step into one rewrite. Any remaining N3 obligation is therefore outside coefficient transport.