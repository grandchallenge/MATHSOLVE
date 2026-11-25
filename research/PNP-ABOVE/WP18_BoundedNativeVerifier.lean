import PNPAbove.WP18Native

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Exact original source per-index time bound for the player-aware sampler.
This bounds *every* raw input, not just the four canonical query families. -/
theorem asymmetricSampler_timeBoundAt (n : Nat) :
    asymmetricSampler.TimeBoundAt n
      (WP14.staticBuildCost asymmetricSamplerProg * (esize n + 2)) 1 := by
  intro d
  obtain ⟨r,t,hr,hcost⟩ := asymmetric_time_bound_raw n d
  have hsize : (Data.cons (encode n) d).size + 1 ≤
      (esize n + 2) * (d.size + 1) := by
    simp only [Data.size_cons, esize]
    nlinarith [Nat.zero_le ((encode n).size * d.size)]
  have hmul := Nat.mul_le_mul_left
    (WP14.staticBuildCost asymmetricSamplerProg) hsize
  refine ⟨r,t,?_,hr⟩
  simp only [pow_one]
  calc
    t ≤ WP14.staticBuildCost asymmetricSamplerProg *
        ((Data.cons (encode n) d).size + 1) := hcost
    _ ≤ WP14.staticBuildCost asymmetricSamplerProg *
        ((esize n + 2) * (d.size + 1)) := hmul
    _ = (WP14.staticBuildCost asymmetricSamplerProg * (esize n + 2)) *
        (d.size + 1) := by ring

#guard WP14.staticBuildCost asymmetricSamplerProg == 53

/-- Conservative n^10 envelope, not an asymptotically optimized constant. -/
theorem sampler_coefficient_le_pow (n : Nat) (hn : 2 ≤ n) :
    WP14.staticBuildCost asymmetricSamplerProg * (esize n + 2) ≤ n ^ 10 := by
  have hbit : esize n ≤ 4 * n + 1 := by
    have hs := esize_nat_le n
    have hnsize := WP13.size_le_index n
    omega
  have hpow9 : 512 ≤ n ^ 9 := by
    simpa only [show (2:Nat)^9 = 512 from by decide] using
      (Nat.pow_le_pow_left hn 9)
  have hcoef : WP14.staticBuildCost asymmetricSamplerProg = 53 := by decide
  rw [hcoef]
  calc
    53 * (esize n + 2) ≤ 53 * (4 * n + 3) := by omega
    _ ≤ 512 * n := by omega
    _ ≤ n ^ 9 * n := Nat.mul_le_mul_right n hpow9
    _ = n ^ 10 := by ring

/-- The original typed source verifier with the new asymmetric sampler and
the unchanged original (deliberately easy) identity decider. -/
def asymmetricVerifier : Verifier 9 where
  sampler := asymmetricSampler
  decider := WP08.identityDecider
  accepts_length := WP14.conditionalVerifier.accepts_length

def boundLam : Nat := asymmetricVerifier.size + 10

/-- Native MIPRE.Verifier.IsBounded; this includes input-time, dimension and
both source program description sizes. -/
theorem asymmetricVerifier_isBounded : asymmetricVerifier.IsBounded boundLam := by
  have hLam : 10 ≤ boundLam := by
    dsimp [boundLam]
    omega
  constructor
  · intro n hn
    have hpow : n ^ 10 ≤ n ^ boundLam :=
      Nat.pow_le_pow_right (by omega : 1 ≤ n) hLam
    have hpow9 : 512 ≤ n ^ 9 := by
      simpa only [show (2:Nat)^9 = 512 from by decide] using
        (Nat.pow_le_pow_left hn 9)
    have h512 : 512 ≤ n ^ boundLam := by
      have h10 : 512 ≤ n ^ 10 := by
        calc
          512 ≤ 512 * n := by omega
          _ ≤ n ^ 9 * n := Nat.mul_le_mul_right n hpow9
          _ = n ^ 10 := by ring
      omega
    refine ⟨?_, ?_, ?_⟩
    · change 9 ≤ n ^ boundLam
      omega
    · change asymmetricSampler.TimeBoundAt n (n ^ boundLam) boundLam
      apply Sampler.TimeBoundAt.mono (asymmetricSampler_timeBoundAt n)
      · exact (sampler_coefficient_le_pow n hn).trans hpow
      · omega
    · change WP08.identityDecider.TimeBoundAt n (n ^ boundLam) boundLam
      apply Decider.TimeBoundAt.mono (WP13.decider9_timeBoundAt n)
      · omega
      · omega
  · dsimp only [boundLam]
    omega

/-- Original upstream synchrony law; identical-decider semantics. -/
theorem asymmetricVerifier_synchronous (n : Nat) :
    asymmetricVerifier.IsSynchronousAt n :=
  WP14.conditionalVerifier_synchronous n

/-- The old decider accepts the same empty answers regardless of which
question distribution the sampler uses. This blocks sampler-only hardness. -/
theorem asymmetricVerifier_accepts_empty (n : Nat) (hn : n ≠ 0)
    (x y : Fin 9 → 𝔽₂) :
    asymmetricVerifier.decider.Accepts n (toBits x) (toBits y) [] [] :=
  WP14.conditionalVerifier_accepts_empty n hn x y

#eval asymmetricSampler.size
#eval asymmetricVerifier.size
#eval boundLam

end PNPAbove.WP18
