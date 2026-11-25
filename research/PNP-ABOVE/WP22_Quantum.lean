import PNPAbove.WP22Classical
import MIPRE.Foundations.GameTransport

namespace PNPAbove.WP22
open MIPRE MIPRE.CL MIPRE.Cost PNPAbove.WP20 PNPAbove.WP21 Finset
open scoped Classical
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The binary-answer restriction of the new executable source game.
The cyclic sampler's full question distribution is unchanged. -/
noncomputable def maskedBinaryGame : Game Questions Questions Bool Bool where
  μ := parityGame.μ
  μ_nonneg := parityGame.μ_nonneg
  μ_sum_one := parityGame.μ_sum_one
  D := maskedParityAccept

/-- A genuine injection into source answers of length at most T. -/
def binaryEmbedding (T : Nat) (hT : 1 ≤ T) :
    Bool ↪ Verifier.Answers T where
  toFun := binaryAnswer T hT
  inj' := by
    intro a b h
    have hs := congrArg Subtype.val h
    cases a <;> cases b <;> simp [binaryAnswer] at hs ⊢

/-- All original non-binary answer labels are rejected, so the imported
answer-extension theorem identifies the complete quantum value with that
of the masked binary game. -/
theorem native_quantum_eq_binary (n T : Nat) (hn : n ≠ 0)
    (hT : 1 ≤ T) :
    quantumValue (cyclicVerifier.game n T) =
      quantumValue maskedBinaryGame := by
  apply quantumValue_extendAnswers maskedBinaryGame (cyclicVerifier.game n T)
    (binaryEmbedding T hT) (binaryEmbedding T hT)
  · intro x y
    rfl
  · intro x y a b
    exact native_game_binary n T hn hT x y a b
  · intro x y a b h
    have hacc : maskedParityDecider.Accepts n
        (CL.toBits x) (CL.toBits y) a.1 b.1 := by
      change decide (maskedParityDecider.Accepts n
        (CL.toBits x) (CL.toBits y) a.1 b.1) = true at h
      simpa only [decide_eq_true_eq] using h
    obtain ⟨_,_,_,ha,hb,_⟩ :=
      (native_accepts_iff n (CL.toBits x) (CL.toBits y) a.1 b.1).mp hacc
    constructor
    · refine ⟨a.1[0]!, ?_⟩
      apply Subtype.ext
      exact (singleton_of_length_one a.1 ha).symm
    · refine ⟨b.1[0]!, ?_⟩
      apply Subtype.ext
      exact (singleton_of_length_one b.1 hb).symm

end PNPAbove.WP22
