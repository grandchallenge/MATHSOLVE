import PNPAbove.WP22Native

namespace PNPAbove.WP22
open MIPRE MIPRE.CL MIPRE.Cost PNPAbove.WP20 PNPAbove.WP21
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Canonical original CL nine-bit conversion preserves every coordinate. -/
theorem toBits_nth (x : Questions) (i : Fin 9) :
    (CL.toBits x)[i.val]! = bit (x i) := by
  fin_cases i <;> simp [CL.toBits, bit]


/-- For every nonzero index, binary original-source answers realize exactly
the globally synchronous support-masked CHSH predicate on all questions. -/
theorem binary_accepts_iff (n : Nat) (hn : n ≠ 0)
    (x y : Questions) (a b : Bool) :
    maskedParityDecider.Accepts n (CL.toBits x) (CL.toBits y) [a] [b] ↔
      maskedParityAccept x y a b = true := by
  rw [native_accepts_iff]
  simp [hn, CL.toBits, bit, leafRule,
    maskedParityAccept]
  intro h8 h0
  by_cases hp : a.xor b = (decide (x 0 = 1) && decide (y 8 = 1))
  · simp [hp]
  · simp [hp]


/-- The original source game Boolean acceptance bit matches the mathematical
masked rule on all original nine-bit questions, not just sampler support. -/
theorem binary_decision_eq (n : Nat) (hn : n ≠ 0)
    (x y : Questions) (a b : Bool) :
    decide (maskedParityDecider.Accepts n (CL.toBits x) (CL.toBits y) [a] [b]) =
      maskedParityAccept x y a b := by
  cases hp : maskedParityAccept x y a b with
  | true =>
      have hh := (binary_accepts_iff n hn x y a b).mpr hp
      simp [hh]
  | false =>
      have hh : ¬ maskedParityDecider.Accepts n (CL.toBits x) (CL.toBits y) [a] [b] := by
        intro hv
        have ht := (binary_accepts_iff n hn x y a b).mp hv
        rw [hp] at ht
        cases ht
      simp [hh]

/-- Embed a one-bit Boolean answer into the source's answer strings of
length up to T. -/
def binaryAnswer (T : Nat) (hT : 1 ≤ T) (a : Bool) :
    Verifier.Answers T :=
  ⟨[a], by simpa using hT⟩

/-- Exact original Verifier.game acceptance on every binary answer and
every nine-dimensional question. -/
theorem native_game_binary (n T : Nat) (hn : n ≠ 0) (hT : 1 ≤ T)
    (x y : Questions) (a b : Bool) :
    (cyclicVerifier.game n T).D x y
      (binaryAnswer T hT a) (binaryAnswer T hT b) =
      maskedParityAccept x y a b := by
  change decide (maskedParityDecider.Accepts n
    (CL.toBits x) (CL.toBits y) [a] [b]) = maskedParityAccept x y a b
  exact binary_decision_eq n hn x y a b

/-- On every positive-mass original cyclic source pair, native game binary
acceptance equals the exact WP20 synchronous CHSH acceptance predicate. -/
theorem native_game_sampled (n T : Nat) (hn : n ≠ 0) (hT : 1 ≤ T)
    (z : Questions) (a b : Bool) :
    (cyclicVerifier.game n T).D (aliceCL.eval z) (bobCL.eval z)
      (binaryAnswer T hT a) (binaryAnswer T hT b) =
      parityAccept (aliceCL.eval z) (bobCL.eval z) a b := by
  rw [native_game_binary n T hn hT]
  exact maskedParity_source z a b

/-- In the entire original game, every answer with an incorrect length
loses, regardless of question or the other player's answer. -/
theorem native_game_bad_left (n T : Nat) (x y : Questions)
    (a b : Verifier.Answers T) (ha : a.1.length ≠ 1) :
    (cyclicVerifier.game n T).D x y a b = false := by
  change decide (maskedParityDecider.Accepts n
    (CL.toBits x) (CL.toBits y) a.1 b.1) = false
  apply decide_eq_false_iff_not.mpr
  intro hv
  have hh := (native_accepts_iff n (CL.toBits x) (CL.toBits y) a.1 b.1).mp hv
  exact ha hh.2.2.2.1

theorem native_game_bad_right (n T : Nat) (x y : Questions)
    (a b : Verifier.Answers T) (hb : b.1.length ≠ 1) :
    (cyclicVerifier.game n T).D x y a b = false := by
  change decide (maskedParityDecider.Accepts n
    (CL.toBits x) (CL.toBits y) a.1 b.1) = false
  apply decide_eq_false_iff_not.mpr
  intro hv
  have hh := (native_accepts_iff n (CL.toBits x) (CL.toBits y) a.1 b.1).mp hv
  exact hb hh.2.2.2.2.1

end PNPAbove.WP22
