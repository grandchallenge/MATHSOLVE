import PNPAbove.WP23NativeConst

namespace PNPAbove.WP23
open MIPRE PNPAbove.WP21 PNPAbove.WP22
open scoped Classical

/-- Existing original-source gap-compression SOUNDNESS promise cannot
apply to the source cyclic Bell verifier: its quantum value is strictly
above 1/2 at every nonzero index and every one-bit-capable answer budget. -/
theorem cyclic_never_quantum_sound (n T : Nat)
    (hn : n ≠ 0) (hT : 1 ≤ T) :
    ¬ cyclicVerifier.valStar n T ≤ (1/2 : ℝ) := by
  have h := (native_strict_gap n T hn hT).1
  change (81/100 : ℝ) ≤ cyclicVerifier.valStar n T at h
  linarith

/-- In particular, EVERY power-of-two source index, at the original
polynomially bounded canonical answer budget, violates the <=1/2
soundness antecedent of MIPRE.GapCompression.soundness. -/
theorem cyclic_power_two_no_soundness (k lam : Nat) :
    ¬ cyclicVerifier.valStar (2 ^ k) ((2 ^ k) ^ lam) ≤ (1/2 : ℝ) := by
  have hn : (2 ^ k) ≠ 0 := by positivity
  have hT : 1 ≤ (2 ^ k) ^ lam := by
    have hp : 0 < (2 ^ k) ^ lam := by positivity
    omega
  exact cyclic_never_quantum_sound (2 ^ k) ((2 ^ k) ^ lam) hn hT


/-- The native quantum value is fully index-and-answer-budget invariant:
each instance is exactly the value of one fixed masked binary game. -/
theorem cyclic_quantum_index_invariant
    (n m T U : Nat) (hn : n ≠ 0) (hm : m ≠ 0)
    (hT : 1 ≤ T) (hU : 1 ≤ U) :
    quantumValue (cyclicVerifier.game n T) =
      quantumValue (cyclicVerifier.game m U) := by
  rw [native_quantum_eq_binary n T hn hT,
      native_quantum_eq_binary m U hm hU]

/-- The native exact classical optimum is likewise index-and-budget invariant. -/
theorem cyclic_classical_index_invariant
    (n m T U : Nat) (hn : n ≠ 0) (hm : m ≠ 0)
    (hT : 1 ≤ T) (hU : 1 ≤ U) :
    nativeClassicalValue n T = nativeClassicalValue m U := by
  rw [native_classical_exact_three_quarters n T hn hT,
      native_classical_exact_three_quarters m U hm hU]

end PNPAbove.WP23
