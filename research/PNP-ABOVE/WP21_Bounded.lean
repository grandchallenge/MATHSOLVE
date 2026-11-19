import PNPAbove.WP21Time

namespace PNPAbove.WP21
open MIPRE MIPRE.CL MIPRE.Cost

set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

theorem decider_coefficient_le_pow (n : Nat) (hn : 2 ≤ n) :
    inspectionSteps maskedParityDeciderProg *
      (esize n + literalCeiling maskedParityDeciderProg + 3) ≤ n ^ 12 := by
  have hbit : esize n ≤ 4 * n + 1 := by
    have hs := esize_nat_le n
    have hnsize := WP13.size_le_index n
    omega
  have hpow11 : 2048 ≤ n ^ 11 := by
    simpa only [show (2:Nat)^11 = 2048 from by decide] using
      (Nat.pow_le_pow_left hn 11)
  have hcoeff : inspectionSteps maskedParityDeciderProg = 146 := by decide
  have hlit : literalCeiling maskedParityDeciderProg = 3 := by decide
  rw [hcoeff, hlit]
  calc
    146 * (esize n + 3 + 3) ≤ 146 * (4 * n + 7) := by omega
    _ ≤ 2048 * n := by omega
    _ ≤ n ^ 11 * n := Nat.mul_le_mul_right n hpow11
    _ = n ^ 12 := by ring

theorem native_decider_polynomial (n : Nat) (hn : 2 ≤ n) :
    maskedParityDecider.TimeBoundAt n (n ^ 12) 12 := by
  apply Decider.TimeBoundAt.mono (decider_timeBoundAt n)
  · exact decider_coefficient_le_pow n hn
  · omega

def boundLam : Nat := cyclicVerifier.size + 12

theorem cyclicVerifier_isBounded : cyclicVerifier.IsBounded boundLam := by
  have hLam : 12 ≤ boundLam := by
    dsimp [boundLam]
    omega
  constructor
  · intro n hn
    have hpow12 : n ^ 12 ≤ n ^ boundLam :=
      Nat.pow_le_pow_right (by omega : 1 ≤ n) hLam
    have hpow10 : n ^ 10 ≤ n ^ boundLam :=
      Nat.pow_le_pow_right (by omega : 1 ≤ n) (by omega)
    have hpow11 : 2048 ≤ n ^ 11 := by
      simpa only [show (2:Nat)^11 = 2048 from by decide] using
        (Nat.pow_le_pow_left hn 11)
    have h9 : 9 ≤ n ^ boundLam := by
      have : 9 ≤ n ^ 11 := by omega
      have hpow11b : n ^ 11 ≤ n ^ boundLam :=
        Nat.pow_le_pow_right (by omega : 1 ≤ n) (by omega)
      omega
    refine ⟨?_, ?_, ?_⟩
    · change 9 ≤ n ^ boundLam
      exact h9
    · change WP20.cyclicSampler.TimeBoundAt n (n ^ boundLam) boundLam
      apply Sampler.TimeBoundAt.mono (WP20.cyclic_sampler_polynomial n hn)
      · exact hpow10
      · omega
    · change maskedParityDecider.TimeBoundAt n (n ^ boundLam) boundLam
      apply Decider.TimeBoundAt.mono (native_decider_polynomial n hn)
      · exact hpow12
      · omega
  · dsimp only [boundLam]
    omega

end PNPAbove.WP21
