import PNPAbove.WP21Length
import PNPAbove.WP20Bounded

namespace PNPAbove.WP21
open MIPRE MIPRE.CL MIPRE.Cost

/-- A genuinely source-native nine-level verifier with two-sided CL sampler
and an answer-sensitive executable original Cost.Prog decider. The original
sampler and the exact question-length acceptance contract are source-proved.
TimeBoundAt, original IsBounded, full answer-budget payoff transfer and
source-executable synchrony are separate obligations. -/
def cyclicVerifier : Verifier 9 where
  sampler := WP20.cyclicSampler
  decider := maskedParityDecider
  accepts_length := by
    intro n x y a b ha
    exact decider_accepts_length n x y a b ha

theorem cyclicVerifier_sampler :
    cyclicVerifier.sampler = WP20.cyclicSampler := rfl

theorem cyclicVerifier_decider :
    cyclicVerifier.decider = maskedParityDecider := rfl

/-- Source semantics of accepted verifier inputs enforce canonical questions
of the actual original sampler dimension, not just sampled shape tests. -/
theorem cyclicVerifier_accepted_questions (n : Nat) (x y a b : BitStr)
    (ha : cyclicVerifier.decider.Accepts n x y a b) :
    x.length = cyclicVerifier.sampler.dim n ∧
      y.length = cyclicVerifier.sampler.dim n :=
  cyclicVerifier.accepts_length n x y a b ha

end PNPAbove.WP21
