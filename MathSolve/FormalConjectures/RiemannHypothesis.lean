import Mathlib.NumberTheory.LSeries.RiemannZeta

/-!
# Programme-owned Riemann Hypothesis target

This file gives `RH-001` a stable Lean interface. It does not prove the
Riemann Hypothesis. The target is definitionally equal to mathlib's
`RiemannHypothesis` proposition.
-/

namespace MathSolve.FormalConjectures.RH

/-- The Programme carrier for the meromorphically continued zeta function. -/
noncomputable abbrev ProgrammeZeta : ℂ → ℂ := riemannZeta

/-- A trivial zero has the form `-2 (n + 1)`. -/
def IsTrivialZero (s : ℂ) : Prop :=
  ∃ n : ℕ, s = -2 * ((n : ℂ) + 1)

/-- The Programme zero taxonomy excludes the pole at one and the trivial zeros. -/
def IsNontrivialZero (s : ℂ) : Prop :=
  ProgrammeZeta s = 0 ∧ ¬ IsTrivialZero s ∧ s ≠ 1

/-- The canonical `RH-001` target. -/
def ProgrammeRiemannHypothesis : Prop :=
  ∀ s : ℂ, ProgrammeZeta s = 0 → ¬ IsTrivialZero s → s ≠ 1 → s.re = 1 / 2

/-- The Programme zeta carrier is analytic away from the pole at one. -/
theorem programmeZeta_differentiableAt {s : ℂ} (hs : s ≠ 1) :
    DifferentiableAt ℂ ProgrammeZeta s :=
  differentiableAt_riemannZeta hs

/-- The Programme target is definitionally the mathlib `RiemannHypothesis`. -/
theorem programmeRiemannHypothesis_eq_mathlib :
    ProgrammeRiemannHypothesis = _root_.RiemannHypothesis := by
  rfl

/-- Iff form used by downstream replay packages. -/
theorem programmeRiemannHypothesis_iff_mathlib :
    ProgrammeRiemannHypothesis ↔ _root_.RiemannHypothesis := by
  rfl

end MathSolve.FormalConjectures.RH
