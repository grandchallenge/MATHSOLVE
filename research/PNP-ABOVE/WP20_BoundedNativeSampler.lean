import PNPAbove.WP20Native

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- Source-native per-index runtime bound on every actual (including
malformed raw) input to the executable cyclic Sampler 9. -/
theorem cyclicSampler_timeBoundAt (n : Nat) :
    cyclicSampler.TimeBoundAt n
      (WP14.staticBuildCost cyclicSamplerProg * (esize n + 2)) 1 := by
  intro d
  obtain ⟨r,t,hr,hcost⟩ := cyclic_time_bound_raw n d
  have hsize : (Data.cons (encode n) d).size + 1 ≤
      (esize n + 2) * (d.size + 1) := by
    simp only [Data.size_cons, esize]
    nlinarith [Nat.zero_le ((encode n).size * d.size)]
  have hmul := Nat.mul_le_mul_left
    (WP14.staticBuildCost cyclicSamplerProg) hsize
  refine ⟨r,t,?_,hr⟩
  simp only [pow_one]
  calc
    t ≤ WP14.staticBuildCost cyclicSamplerProg *
        ((Data.cons (encode n) d).size + 1) := hcost
    _ ≤ WP14.staticBuildCost cyclicSamplerProg *
        ((esize n + 2) * (d.size + 1)) := hmul
    _ = (WP14.staticBuildCost cyclicSamplerProg * (esize n + 2)) *
        (d.size + 1) := by ring

#guard WP14.staticBuildCost cyclicSamplerProg == 51

theorem cyclicSampler_coefficient_le_pow (n : Nat) (hn : 2 ≤ n) :
    WP14.staticBuildCost cyclicSamplerProg * (esize n + 2) ≤ n ^ 10 := by
  have hbit : esize n ≤ 4 * n + 1 := by
    have hs := esize_nat_le n
    have hnsize := WP13.size_le_index n
    omega
  have hpow9 : 512 ≤ n ^ 9 := by
    simpa only [show (2:Nat)^9 = 512 from by decide] using
      (Nat.pow_le_pow_left hn 9)
  have hcoef : WP14.staticBuildCost cyclicSamplerProg = 51 := by decide
  rw [hcoef]
  calc
    51 * (esize n + 2) ≤ 51 * (4 * n + 3) := by omega
    _ ≤ 512 * n := by omega
    _ ≤ n ^ 9 * n := Nat.mul_le_mul_right n hpow9
    _ = n ^ 10 := by ring

/-- The sampler's native programme has a bounded description as well as
uniform polynomial degree-one runtime; the decider component of a Verifier
remains distinct and is *not* inferred from this theorem. -/
theorem cyclic_sampler_polynomial (n : Nat) (hn : 2 ≤ n) :
    cyclicSampler.TimeBoundAt n (n ^ 10) 10 := by
  apply Sampler.TimeBoundAt.mono (cyclicSampler_timeBoundAt n)
  · exact cyclicSampler_coefficient_le_pow n hn
  · omega

end PNPAbove.WP20
