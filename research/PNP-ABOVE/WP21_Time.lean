import PNPAbove.WP21Runtime

namespace PNPAbove.WP21
open MIPRE MIPRE.Cost

set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Exact coefficient for source-native decider execution at index n. -/
theorem decider_timeBoundAt (n : Nat) :
    maskedParityDecider.TimeBoundAt n
      (inspectionSteps maskedParityDeciderProg *
        (esize n + literalCeiling maskedParityDeciderProg + 3)) 1 := by
  intro d
  obtain ⟨r,t,he,ht⟩ :=
    decider_raw_linear (Data.cons (encode n) d)
  have hsize : (Data.cons (encode n) d).size +
      literalCeiling maskedParityDeciderProg + 1 ≤
      (esize n + literalCeiling maskedParityDeciderProg + 3) *
      (d.size + 1) := by
    simp only [Data.size_cons, esize]
    nlinarith [Nat.zero_le (d.size *
      ((encode n).size + literalCeiling maskedParityDeciderProg + 3))]
  have hmul := Nat.mul_le_mul_left
    (inspectionSteps maskedParityDeciderProg) hsize
  refine ⟨r,t,?_,he⟩
  simpa only [pow_one, mul_assoc] using ht.trans hmul

#eval inspectionSteps maskedParityDeciderProg
#eval literalCeiling maskedParityDeciderProg
#eval esize maskedParityDeciderProg

end PNPAbove.WP21
