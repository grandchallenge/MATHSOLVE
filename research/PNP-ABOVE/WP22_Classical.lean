import PNPAbove.WP22SourceBridge
import PNPAbove.WP20ClassicalExact

namespace PNPAbove.WP22
open MIPRE MIPRE.CL MIPRE.Cost PNPAbove.WP20 PNPAbove.WP21 Finset
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The globally synchronous masked predicate is pointwise no more
permissive than the admitted mathematical parity game. -/
theorem masked_implies_parity (x y : Questions) (a b : Bool)
    (h : maskedParityAccept x y a b = true) :
    parityAccept x y a b = true := by
  have hpar : (a.xor b = (bit (x 0) && bit (y 8))) := by
    simp [maskedParityAccept] at h
    exact h.2
  by_cases hxy : x = y
  · subst y
    have hab : a = b := by
      by_contra hne
      have hfalse := maskedParity_synchronous x a b hne
      rw [hfalse] at h
      cases h
    rw [hab] at hpar
    cases h0 : bit (x 0) <;> cases h8 : bit (x 8) <;>
      simp_all [parityAccept]
  · simp [parityAccept, hxy, hpar]

/-- Every accepted source game result maps to an accepted one-bit response
in the original mathematical game. No invalid source answer can improve it. -/
theorem native_accept_implies_parity (n T : Nat) (hn : n ≠ 0)
    (x y : Questions) (a b : Verifier.Answers T)
    (h : (cyclicVerifier.game n T).D x y a b = true) :
    parityAccept x y (a.1[0]!) (b.1[0]!) = true := by
  have hacc : maskedParityDecider.Accepts n
      (CL.toBits x) (CL.toBits y) a.1 b.1 := by
    change decide (maskedParityDecider.Accepts n
      (CL.toBits x) (CL.toBits y) a.1 b.1) = true at h
    simpa only [decide_eq_true_eq] using h
  obtain ⟨_,_,_,ha,hb,_⟩ :=
    (native_accepts_iff n (CL.toBits x) (CL.toBits y) a.1 b.1).mp hacc
  have has := singleton_of_length_one a.1 ha
  have hbs := singleton_of_length_one b.1 hb
  rw [has, hbs] at hacc
  exact masked_implies_parity x y (a.1[0]!) (b.1[0]!)
    ((binary_accepts_iff n hn x y _ _).mp hacc)

/-- Original native-game success is pointwise dominated by the old Boolean
parity success after projecting arbitrary answer strings onto their first bit. -/
theorem native_payoff_le_parity (n T : Nat) (hn : n ≠ 0)
    (x y : Questions) (a b : Verifier.Answers T) :
    (if (cyclicVerifier.game n T).D x y a b then (1:ℝ) else 0) ≤
      (if parityAccept x y (a.1[0]!) (b.1[0]!) then (1:ℝ) else 0) := by
  cases hwin : (cyclicVerifier.game n T).D x y a b with
  | true =>
      have hpar := native_accept_implies_parity n T hn x y a b hwin
      change (1:ℝ) ≤ if parityAccept x y (a.1[0]!) (b.1[0]!) = true
        then 1 else 0
      rw [hpar]
      norm_num
  | false =>
      simp only [Bool.false_eq_true, ite_false]
      split_ifs <;> norm_num

/-- Deterministic value for arbitrary source answer strings. -/
noncomputable def nativeDeterministicValue (n T : Nat)
    (fA fB : Questions → Verifier.Answers T) : ℝ :=
  ∑ x : Questions, ∑ y : Questions,
    (cyclicVerifier.game n T).μ x y *
    (if (cyclicVerifier.game n T).D x y (fA x) (fB y)
      then (1:ℝ) else 0)

/-- Every source-native classical response pair is dominated by the old
Boolean game with each answer reduced to its first bit. -/
theorem native_det_le_parity (n T : Nat) (hn : n ≠ 0)
    (fA fB : Questions → Verifier.Answers T) :
    nativeDeterministicValue n T fA fB ≤
      deterministicValue (fun x => (fA x).1[0]!)
        (fun y => (fB y).1[0]!) := by
  change (∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y *
      (if (cyclicVerifier.game n T).D x y (fA x) (fB y)
        then (1:ℝ) else 0)) ≤
    ∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y *
      (if parityAccept x y ((fA x).1[0]!) ((fB y).1[0]!)
        then (1:ℝ) else 0)
  apply Finset.sum_le_sum
  intro x hx
  apply Finset.sum_le_sum
  intro y hy
  exact mul_le_mul_of_nonneg_left
    (native_payoff_le_parity n T hn x y (fA x) (fB y))
    (clDist_nonneg aliceCL.eval bobCL.eval x y)

/-- Universal upper bound on every source-native deterministic classical
strategy, even when all source answer strings of length at most T are allowed. -/
theorem native_every_classical_le (n T : Nat) (hn : n ≠ 0)
    (fA fB : Questions → Verifier.Answers T) :
    nativeDeterministicValue n T fA fB ≤ (3/4:ℝ) :=
  (native_det_le_parity n T hn fA fB).trans
    (every_classical_strategy_le_three_quarters _ _)

/-- Unrestricted classical local-source answer supremum. -/
noncomputable def nativeClassicalValue (n T : Nat) : ℝ :=
  ⨆ fA : Questions → Verifier.Answers T,
    ⨆ fB : Questions → Verifier.Answers T,
      nativeDeterministicValue n T fA fB

/-- Source-native classical strategies have maximum value at most 3/4,
including arbitrary malformed or extra answer labels. -/
theorem native_classical_le_three_quarters (n T : Nat) (hn : n ≠ 0) :
    nativeClassicalValue n T ≤ (3/4:ℝ) := by
  unfold nativeClassicalValue
  refine Real.iSup_le (fun fA =>
    Real.iSup_le (fun fB => native_every_classical_le n T hn fA fB)
      (by norm_num)) (by norm_num)

end PNPAbove.WP22
