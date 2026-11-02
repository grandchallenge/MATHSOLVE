import MIPRE.Background.Introspection.DecisionCompiler

/-!
PNP-ABOVE WP06 — SOURCE-DERIVED, NOT YET REPLAYED.
Source: vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970.
Lean proof candidates for the zero-parameter and overbudget-input
erasure identities. Do not mark kernel checked without exact Lean replay.
-/

namespace PNPAbove.WP06
open MIPRE
open MIPRE.Cost
open MIPRE.Introspection
open MIPRE.Introspection.DecisionCompiler

theorem zero_erases_source (c : ℕ) (U : ClockedUniversalMachine)
    (S D : Prog) :
    compute c U ((S,D),0) = zeroProg := by
  rw [compute_apply]
  rfl

theorem zero_acceptance_independent_of_source
    (c : ℕ) (U : ClockedUniversalMachine)
    (S D : Prog) (n : ℕ) (x y a b : BitStr) :
    (decider c U S D 0).Accepts n x y a b ↔
      x = [] ∧ y = [] ∧ a.length ≤ 2 ∧ b.length ≤ 2 := by
  exact accepts_zero c U S D 0 n (Or.inl rfl) x y a b

theorem overbudget_clamps_to_nil (S D : Prog) (lam : ℕ)
    (hS : lam < esize S) (hD : lam < esize D) :
    SourceDescriptionCompiler.clamp ((S,D),lam)
      = ((Prog.nil,Prog.nil),lam) := by
  have hSn : ¬ esize S ≤ lam := by omega
  have hDn : ¬ esize D ≤ lam := by omega
  simp [SourceDescriptionCompiler.clamp_apply,
    SourceDescriptionCompiler.clampProgram_apply, hSn, hDn]

theorem overbudget_compiler_collision
    (c : ℕ) (U : ClockedUniversalMachine)
    (S₁ D₁ S₂ D₂ : Prog) (lam : ℕ)
    (hS₁ : lam < esize S₁) (hD₁ : lam < esize D₁)
    (hS₂ : lam < esize S₂) (hD₂ : lam < esize D₂) :
    compute c U ((S₁,D₁),lam) = compute c U ((S₂,D₂),lam) := by
  simp only [compute_apply]
  by_cases hz : lam = 0
  · simp [hz]
  · simp only [if_neg hz]
    rw [overbudget_clamps_to_nil S₁ D₁ lam hS₁ hD₁,
        overbudget_clamps_to_nil S₂ D₂ lam hS₂ hD₂]

end PNPAbove.WP06
