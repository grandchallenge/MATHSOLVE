import MathSolve.PNP.PolyBoundBridge
import Mathlib.Tactic

/-!
# PNP quantitative simulation overhead

This file supplies the quantitative transfer lemma needed by
`PNP-BRIDGE-MODEL-001`.

A concrete machine translator must still prove its execution simulation. Once
it supplies an affine bound in exact input length and source transition count,
this file proves that the translated runtime remains polynomial under the
already-closed `PNP-BRIDGE-POLYBOUND-001` presentation equivalence.

No machine-model equivalence is asserted here.
-/

namespace MathSolve.PNP

/--
An affine runtime overhead on the exact binary carrier.

`startup` is input-independent setup/termination work, `inputFactor` charges
linear initialization in `input.length`, and `stepFactor` charges a fixed number
of target transitions per source transition.
-/
def AffineSimulationOverhead (source target : BinaryRuntimeCost) : Prop :=
  ∃ startup inputFactor stepFactor : Nat, ∀ input,
    target input ≤
      startup + inputFactor * input.length + stepFactor * source input

/--
Affine overhead preserves the protected Programme polynomial-time bound.

The proof routes through the exact `Polynomial Nat` bridge already established
for `PNP-BRIDGE-POLYBOUND-001`: if `p` bounds the source cost, then

`startup + inputFactor * X + stepFactor * p`

bounds the translated cost on every input length, including the finite prefix.
-/
theorem affineSimulationOverhead_preserves_programmePolynomialBound
    {source target : BinaryRuntimeCost}
    (hsource : ProgrammePolynomialBound source)
    (hoverhead : AffineSimulationOverhead source target) :
    ProgrammePolynomialBound target := by
  rcases programmePolynomialBound_to_importedPolynomialBound hsource with ⟨p, hp⟩
  rcases hoverhead with ⟨startup, inputFactor, stepFactor, hoverhead⟩
  apply importedPolynomialBound_to_programmePolynomialBound
  refine ⟨Polynomial.C startup + Polynomial.C inputFactor * Polynomial.X +
    Polynomial.C stepFactor * p, ?_⟩
  intro input
  calc
    target input ≤
        startup + inputFactor * input.length + stepFactor * source input :=
      hoverhead input
    _ ≤ startup + inputFactor * input.length + stepFactor * p.eval input.length := by
      gcongr
      exact hp input
    _ = (Polynomial.C startup + Polynomial.C inputFactor * Polynomial.X +
        Polynomial.C stepFactor * p).eval input.length := by
      simp

/-- The zero-startup, no-input-scan special case used by direct step simulations. -/
theorem fixedStepOverhead_preserves_programmePolynomialBound
    {source target : BinaryRuntimeCost} {stepFactor : Nat}
    (hsource : ProgrammePolynomialBound source)
    (hoverhead : ∀ input, target input ≤ stepFactor * source input) :
    ProgrammePolynomialBound target := by
  apply affineSimulationOverhead_preserves_programmePolynomialBound hsource
  exact ⟨0, 0, stepFactor, fun input => by simpa using hoverhead input⟩

#print axioms affineSimulationOverhead_preserves_programmePolynomialBound
#print axioms fixedStepOverhead_preserves_programmePolynomialBound

end MathSolve.PNP
