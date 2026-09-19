import Mathlib.Analysis.Normed.Algebra.Spectrum

/-!
# RH-R030 spectral boundedness obstruction

This file formalizes the operator-theoretic composition step used by
`RH-R030-SPECTRAL-UNBOUNDED-001`.

The analytic input that positive ordinates of nontrivial zeta zeros are
unbounded is intentionally supplied as a hypothesis. In the work package it is
provided by the classical Riemann--von Mangoldt zero-counting theorem. This
file does not formalize that analytic theorem and does not prove RH.
-/

namespace MathSolve.RH

/-- A real sequence is unbounded above. -/
def UnboundedAboveRealSequence (gamma : ℕ → ℝ) : Prop :=
  ∀ R : ℝ, ∃ n : ℕ, R < gamma n

/--
No element of a complete complex normed algebra can have an unbounded real
sequence contained in its spectrum.

For bounded operators, apply this theorem in the Banach algebra of bounded
continuous linear endomorphisms. Self-adjointness is not needed for this
obstruction; therefore the result applies a fortiori to bounded self-adjoint
Hilbert--Polya candidates.
-/
theorem no_bounded_spectrum_contains_unbounded_real_sequence
    {A : Type*} [NormedRing A] [NormedAlgebra ℂ A]
    [CompleteSpace A] [NormOneClass A]
    (a : A) (gamma : ℕ → ℝ)
    (hunbounded : UnboundedAboveRealSequence gamma)
    (hmem : ∀ n : ℕ, (gamma n : ℂ) ∈ spectrum ℂ a) :
    False := by
  obtain ⟨n, hn⟩ := hunbounded ‖a‖
  have hspec : ‖(gamma n : ℂ)‖ ≤ ‖a‖ :=
    spectrum.norm_le_norm_of_mem (hmem n)
  have hle : gamma n ≤ ‖(gamma n : ℂ)‖ := by
    simpa [Complex.norm_real, Real.norm_eq_abs] using (le_abs_self (gamma n))
  exact (not_lt_of_ge (hle.trans hspec)) hn

end MathSolve.RH
