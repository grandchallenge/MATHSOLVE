import PNPAbove.WP21Safety

namespace PNPAbove.WP21
open MIPRE MIPRE.Cost

set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

#guard WP14.loopFreeB maskedParityDeciderProg

theorem maskedParityDecider_loopFree :
    WP11.LoopFree maskedParityDeciderProg := by
  exact WP14.loopFreeB_sound _ (by decide)

theorem truthTree_boolean (is : List Nat) (bits : List Bool) (offset : Nat) :
    WP11.BooleanResult (truthTree is bits offset) := by
  induction is generalizing bits offset with
  | nil =>
      cases h : leafRule bits.reverse <;>
        simp [truthTree, WP11.BooleanResult, h]
  | cons i is ih =>
      change WP11.BooleanResult (truthTree is (false :: bits) offset) ∧
        WP11.BooleanResult (truthTree is (true :: bits) (offset + 2))
      exact ⟨ih _ _, ih _ _⟩

theorem readAndDecide_boolean : WP11.BooleanResult readAndDecide := by
  simpa [readAndDecide, WP11.BooleanResult] using
    truthTree_boolean [0,1,2,3,4,5] [] 0

theorem requireBits_boolean (idx k : Nat) (s : Prog)
    (hs : WP11.BooleanResult s) :
    WP11.BooleanResult (requireBits idx k s) := by
  simp [requireBits, WP11.BooleanResult, reject, hs]

theorem decider_boolean :
    WP11.BooleanResult maskedParityDeciderProg := by
  simp only [maskedParityDeciderProg, WP11.BooleanResult]
  simp [reject, WP11.BooleanResult]
  exact requireBits_boolean 4 9 _
    (requireBits_boolean 5 9 _
      (requireBits_boolean 6 1 _
        (requireBits_boolean 10 1 _ readAndDecide_boolean)))

/-- The original operational semantics terminate on ALL raw input trees. -/
theorem decider_raw_total (input : Data) :
    ∃ r t, Eval [input] maskedParityDeciderProg r t :=
  WP11.loopfree_terminates _ maskedParityDecider_loopFree [input]

/-- Every actual source execution returns a canonical encoded Bool. -/
theorem decider_raw_boolean (input r : Data) (t : Nat)
    (h : Eval [input] maskedParityDeciderProg r t) :
    r = encode true ∨ r = encode false :=
  WP11.eval_boolean_result h decider_boolean

/-- Source interpreter and original timed Cost.Eval agree on each raw input. -/
theorem evalValue_source_raw (input : Data) :
    ∃ t, Eval [input] maskedParityDeciderProg
      (WP12.evalValue maskedParityDeciderProg [input]) t :=
  WP12.evalValue_sound _ _ maskedParityDecider_loopFree

/-- The complete source-native Decider.Accepts relation, with no extra
interpreter as authority, is equivalent to a deterministic value computation. -/
theorem accepts_iff_source_value (n : Nat) (x y a b : BitStr) :
    maskedParityDecider.Accepts n x y a b ↔
      WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b] =
        encode true := by
  obtain ⟨t, h⟩ := evalValue_source_raw (WP08.sample n x y a b)
  constructor
  · rintro ⟨u,hu⟩
    exact (Eval.deterministic h hu).1
  · intro hv
    exact ⟨t, hv ▸ h⟩

end PNPAbove.WP21
