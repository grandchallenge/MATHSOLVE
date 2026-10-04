GCL-CONTRIBUTION-RESULT/1
dispatch_id: CMDG-P3M-N3-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-CMDG-N3-C
assignment: CMDG-P3M-N3-WP-C
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement

No concrete protected-type counterexample survives the five requested loss mechanisms. In the protected chain, N3 reduces exactly to one generic coefficient-transport identity.

Write
F := measurePointFunctional X μ
and
L := measurePointIntegralFunctional X μ
   = liftedIntFunctionalDown X F.

The first remaining proof obligation is the generic bridge

  ULift.up
    (liftedIntFunctionalDown X F
      ((locallyConstantIntegralLiftEquiv X).symm v))
  =
  F v

for arbitrary
  X : Profinite,
  F : LocallyConstant X R →ₗ[R] R,
  v : LocallyConstant X R.

Once this bridge is compiled, protected N2 gives directly, for every μ, j, q,

  weightedFiniteBooleanCoefficient X
      (fun i => L (integralBasis X i)) j q
      (fun _ => true)
  =
  F (finiteDeltaPullbackR X j q).

Thus no additional finite-delta descent lemma, Boolean-cube identification lemma, or sign/order correction is needed for N3.

## Derivation

1. Boolean-cube mismatch is eliminated by the protected definitions themselves. The codomain of weightedFiniteBooleanCoefficient is packaged as LocallyConstant (basisBooleanCube X) R, but its definition immediately and successfully changes this to the literal type LocallyConstant (IntegralBasisIndex X → Bool) R before applying weightedBasisBooleanPairingR. Therefore the all-true selector used by the weighted pairing is the literal function fun _ => true at the relevant evaluation site; this is not an unproved identification of two unrelated spaces.

2. The R-valued weighted pairing is exact transport, not a separately implemented formula:
   weightedBasisBooleanPairingR X a v
   is basisBooleanIntegralLiftEquiv X applied to
   weightedBasisBooleanPairing X a
     (locallyConstantIntegralDownEquiv X v).
The output transport is pointwise ULift.up, while locallyConstantIntegralDownEquiv is the inverse of the protected integral lift equivalence.

3. Let a i := L (integralBasis X i). For an arbitrary v : LocallyConstant X R, all-true evaluation of weightedBasisBooleanPairingR X a v therefore reduces to

   ULift.up
     (weightedBasisBooleanPairing X
       (fun i => L (integralBasis X i))
       (locallyConstantIntegralDownEquiv X v)
       (fun _ => true)).

Protected N2 applies to the arbitrary integral argument locallyConstantIntegralDownEquiv X v and gives

   ULift.up (L (locallyConstantIntegralDownEquiv X v)).

No basis-coordinate, order, or sign information remains after this rewrite.

4. Substituting L = liftedIntFunctionalDown X F leaves exactly

   ULift.up
     (liftedIntFunctionalDown X F
       (locallyConstantIntegralDownEquiv X v))
   =
   F v.

Since locallyConstantIntegralDownEquiv X is definitionally the inverse of locallyConstantIntegralLiftEquiv X, this is the generic bridge stated above.

5. Now take v := finiteDeltaPullbackR X j q. The finite delta is used only as an arbitrary R-valued locally constant function. Therefore there is no separate requirement that finiteDeltaPullbackR first be identified with some independently defined integral delta. Any such possible mismatch is bypassed structurally by descending the actual finiteDeltaPullbackR through the protected inverse equivalence.

6. The protected finite-quotient source supplies an independent consistency check in the evaluation-weight specialization: its all-true coefficient theorem changes to the same transported integer pairing and closes after the protected all-true reconstruction theorem followed by rfl. This is consistent with, and does not add to, the generic residual above.

## Assumptions beyond bootstrap

None. The audit used only the protected packet, the five explicitly listed protected source blobs, and standard equational reasoning. Protected N2 was treated as discharged and was not reopened.

The body of liftedIntFunctionalDown itself is not among the five exposed protected blobs, so I do not promote the generic bridge from an exact residual to a formally compiled theorem in this return.

## Verification / falsification hooks

Primary compile hook:

  theorem liftedIntFunctionalDown_down_inverse
      (X : Profinite)
      (F : LocallyConstant X R →ₗ[R] R)
      (v : LocallyConstant X R) :
      ULift.up
        (liftedIntFunctionalDown X F
          ((locallyConstantIntegralLiftEquiv X).symm v)) =
        F v := by
    -- unfold only the protected lift/down definitions and close by the
    -- ULift up/down inverse law plus the ring-equivalence inverse law.

After that theorem is available, instantiate v with finiteDeltaPullbackR X j q. The N3 coefficient statement should reduce by one change/unfold step, one use of protected N2, and the generic bridge.

Small genuine protected-space sanity check:
  X := Profinite.of PUnit,
  F := LocallyConstant.evalₗ R PUnit.unit,
  v := LocallyConstant.const _ (ULift.up 1).
The generic bridge must evaluate to ULift.up 1 = ULift.up 1. Bool gives the analogous two-point check with either characteristic function.

A falsification of the generic bridge for any genuine X, F, v would immediately falsify N3 upstream of finiteDeltaPullbackR. No such failure is exhibited by the protected material.

## Claim boundary

This return does not claim the generic bridge has been compiled, does not claim N3 itself is formally discharged, and makes no claim of d = 0, mapping-out injectivity, coefficient solidity, P3 completion, or CM4 completion.

## Next residual

Compile the single generic theorem liftedIntFunctionalDown_down_inverse against the protected definition of liftedIntFunctionalDown. If it succeeds, instantiate it with
F = measurePointFunctional X μ
and
v = finiteDeltaPullbackR X j q;
protected N2 then closes the N3 all-true finite-coefficient identity without any further mathematical lemma.