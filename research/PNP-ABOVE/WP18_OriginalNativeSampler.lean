import PNPAbove.WP18Runs

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-! # A genuine player-asymmetric original MIPRE Sampler 9 -/

/-- All four native query contracts, exact occupied conditional-linear stage
partition, well-scoped code and raw-input termination are supplied *inside*
the original upstream structure. -/
def asymmetricSampler : Sampler 9 where
  prog := asymmetricSamplerProg
  closed := asymmetricSamplerProg_closed
  dim := fun _ => 9
  cl := fun _ w => match w with
    | .alice => WP14.conditionalNineCL
    | .bob => bobNineCL
  cl_exactlyOn := by
    intro n w
    cases w
    · exact WP14.conditionalNineCL_exactlyOn
    · exact bobNineCL_exactlyOn
  runs_dimension := fun n => sourceRuns (eval_dimension_all n)
  runs_marginal := by
    intro n w j z hj hj9 hz
    cases w
    · have hval : toBits ((WP14.conditionalNineCL.truncate j).eval (ofBits 9 z)) =
          WP14.gatedPrefix j z := by
        rw [WP14.conditional_marginal_formula j hj hj9]
        rw [WP14.semantic_marginal_bits j hj hj9]
        rw [toBits_ofBits hz]
      simpa only [hval] using
        (sourceRuns (eval_marginal_all n .alice j z hj hj9 hz))
    · have hval : toBits ((bobNineCL.truncate j).eval (ofBits 9 z)) =
          bobPrefix j z := by
        rw [bob_marginal_bits j hj hj9]
        rw [toBits_ofBits hz]
      simpa only [hval] using
        (sourceRuns (eval_marginal_all n .bob j z hj hj9 hz))
  runs_linear := by
    intro n w j u y hj hj9 hu hy
    have huLen : u.length = 9 := by
      obtain ⟨x,rfl⟩ := hu
      exact length_toBits _
    cases w
    · have hval : toBits ((WP14.conditionalNineCL.mapOfPrefix (j-1)
          (ofBits 9 u)) (ofBits 9 y)) = WP14.gatedLinear j u y := by
        rw [WP14.semantic_linear_bits j hj hj9]
        rw [toBits_ofBits huLen, toBits_ofBits hy]
      simpa only [hval] using
        (sourceRuns (eval_linear_all n .alice j u y hj hj9 huLen hy))
    · have hval : toBits ((bobNineCL.mapOfPrefix (j-1)
          (ofBits 9 u)) (ofBits 9 y)) = bobLinearBits j y := by
        rw [bob_linear_bits j hj hj9]
        rw [toBits_ofBits hy]
      simpa only [hval] using
        (sourceRuns (eval_linear_all n .bob j u y hj hj9 huLen hy))
  runs_factor := by
    intro n w j u hj hj9 hu
    cases w
    · have hval : indicatorBits
          (WP14.conditionalNineCL.factorOfPrefix (j-1) (ofBits 9 u)) =
          WP14.bitmap (j-1) := WP14.semantic_factor_bits j hj hj9 _
      simpa only [hval, WP14.sourceBitmap] using
        (sourceRuns (eval_factor_all n .alice j u hj hj9))
    · have hval : indicatorBits (bobNineCL.factorOfPrefix (j-1) (ofBits 9 u)) =
          WP14.bitmap (j-1) := bob_factor_bits j hj hj9 _
      simpa only [hval, WP14.sourceBitmap] using
        (sourceRuns (eval_factor_all n .bob j u hj hj9))
  halts := fun n d => by
    obtain ⟨r,t,hr⟩ := asymmetricSamplerProg_halts_raw (.cons (encode n) d)
    exact ⟨r,t,hr⟩

/-- The native sampler now has nonzero unequal-question support. This is
a fact about the original MIPRE.Sampler.dist, not a replacement oracle. -/
theorem asymmetricSampler_off_diagonal_mass (n : Nat) :
    0 < asymmetricSampler.dist n
      (WP14.conditionalNineCL.eval offDiagonalSeed)
      (bobNineCL.eval offDiagonalSeed) := by
  exact original_cl_dist_positive

end PNPAbove.WP18
