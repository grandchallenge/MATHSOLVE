import PNPAbove.WP22Quantum
import PNPAbove.WP20ClassicalExact

namespace PNPAbove.WP22
open MIPRE MIPRE.CL MIPRE.Cost PNPAbove.WP20 PNPAbove.WP21 Finset Matrix Kronecker
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Off the 512 source edges, the original game has exactly zero mass.
On each source edge, the masked native binary predicate agrees identically
with the WP20 synchronous CHSH predicate. -/
theorem zero_mass_or_equal_decision (x y : Questions) :
    clDist aliceCL.eval bobCL.eval x y = 0 ∨
      (∀ a b : Bool, maskedParityAccept x y a b = parityAccept x y a b) := by
  by_cases h : ∃ z : Questions, aliceCL.eval z = x ∧ bobCL.eval z = y
  · right
    obtain ⟨z,hx,hy⟩ := h
    intro a b
    rw [← hx, ← hy]
    exact maskedParity_source z a b
  · left
    exact unsupported_zero x y h

/-- A tensor-product strategy has exactly the same native binary payoff as
in WP20: the sole predicate differences occur on zero-probability pairs. -/
theorem tensor_value_copy_eq (S : TensorProductStrategy parityGame.toGame) :
    (S.copy maskedBinaryGame).value = S.value := by
  unfold TensorProductStrategy.value
  change
    (∑ x : Questions, ∑ y : Questions, ∑ a : Bool, ∑ b : Bool,
      clDist aliceCL.eval bobCL.eval x y *
        (if maskedParityAccept x y a b then (1:ℝ) else 0) *
        (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)).re) =
    (∑ x : Questions, ∑ y : Questions, ∑ a : Bool, ∑ b : Bool,
      clDist aliceCL.eval bobCL.eval x y *
        (if parityAccept x y a b then (1:ℝ) else 0) *
        (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)).re)
  apply Finset.sum_congr rfl
  intro x hx
  apply Finset.sum_congr rfl
  intro y hy
  rcases zero_mass_or_equal_decision x y with hzero | hpred
  · simp [hzero]
  · apply Finset.sum_congr rfl
    intro a ha
    apply Finset.sum_congr rfl
    intro b hb
    simp [hpred a b]


/-- The exact WP20 rational qubit strategy survives in the masked binary
game, because every predicate difference is at zero source mass. -/
theorem masked_quantum_lower :
    (81/100:ℝ) ≤ quantumValue maskedBinaryGame := by
  calc
    (81/100:ℝ) = rationalStrategy.value := original_quantum_value.symm
    _ = (rationalStrategy.toTensorProductStrategy).value := by simp
    _ = ((rationalStrategy.toTensorProductStrategy).copy maskedBinaryGame).value :=
      (tensor_value_copy_eq _).symm
    _ ≤ quantumValue maskedBinaryGame :=
      le_ciSup (TensorProductStrategy.bddAbove_range_value maskedBinaryGame)
        ((rationalStrategy.toTensorProductStrategy).copy maskedBinaryGame)

/-- A strictly positive game-value gap for the actual original bounded,
source-native executable verifier. The original source answer alphabet is
unrestricted up to T, and no artificial one-bit restriction is imposed. -/
theorem native_strict_gap (n T : Nat) (hn : n ≠ 0) (hT : 1 ≤ T) :
    (81/100:ℝ) ≤ quantumValue (cyclicVerifier.game n T) ∧
    nativeClassicalValue n T ≤ (3/4:ℝ) ∧
    (3/50:ℝ) ≤ quantumValue (cyclicVerifier.game n T) -
      nativeClassicalValue n T := by
  have hq : (81/100:ℝ) ≤ quantumValue (cyclicVerifier.game n T) := by
    rw [native_quantum_eq_binary n T hn hT]
    exact masked_quantum_lower
  have hc := native_classical_le_three_quarters n T hn
  exact ⟨hq, hc, by linarith⟩

/-- The original bounded verifier's canonical polynomial answer budget
also inherits the strict native Bell gap at every index n ≥ 2. -/
theorem bounded_native_strict_gap (n : Nat) (hn : 2 ≤ n) :
    (3/50:ℝ) ≤ quantumValue (cyclicVerifier.game n (n ^ boundLam)) -
      nativeClassicalValue n (n ^ boundLam) := by
  have hT : 1 ≤ n ^ boundLam := by
    have hnpos : 0 < n := by omega
    have hp := pow_pos hnpos boundLam
    omega
  exact (native_strict_gap n (n ^ boundLam) (by omega) hT).2.2

end PNPAbove.WP22
