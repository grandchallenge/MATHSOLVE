import PNPAbove.WP20BitEquiv

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- The original source-native nine-stage CL sampler, with two independent
private question bits, all nine occupied registers, and exact Cost.Prog
execution on every original four-family query. -/
def cyclicSampler : Sampler 9 where
  prog := cyclicSamplerProg
  closed := cyclicSamplerProg_closed
  dim := fun _ => 9
  cl := fun _ w => match w with
    | .alice => aliceCL
    | .bob => bobCL
  cl_exactlyOn := by
    intro n w
    cases w
    · exact alice_exact
    · exact bob_exact
  runs_dimension := fun n => cyclic_sourceRuns (all_dimension_queries n)
  runs_marginal := by
    intro n w j z hj h9 hz
    cases w
    · have hval :
        toBits ((aliceCL.truncate j).eval (ofBits 9 z)) =
          alicePrefix j z := by
          rw [alice_marginal_bits j hj h9]
          rw [toBits_ofBits hz]
      simpa only [hval] using
        (cyclic_sourceRuns (all_marginal_queries n .alice j z hj h9 hz))
    · have hval :
        toBits ((bobCL.truncate j).eval (ofBits 9 z)) =
          bobPrefix j z := by
          rw [bob_marginal_bits j hj h9]
          rw [toBits_ofBits hz]
      simpa only [hval] using
        (cyclic_sourceRuns (all_marginal_queries n .bob j z hj h9 hz))
  runs_linear := by
    intro n w j u y hj h9 hu hy
    have huLen : u.length = 9 := by
      obtain ⟨x,rfl⟩ := hu
      exact length_toBits _
    cases w
    · have hval :
        toBits ((aliceCL.mapOfPrefix (j-1) (ofBits 9 u)) (ofBits 9 y)) =
          aliceLinearBits j y := by
          rw [alice_linear_bits j hj h9]
          rw [toBits_ofBits hy]
      simpa only [hval] using
        (cyclic_sourceRuns (all_linear_queries n .alice j u y hj h9 huLen hy))
    · have hval :
        toBits ((bobCL.mapOfPrefix (j-1) (ofBits 9 u)) (ofBits 9 y)) =
          bobLinearBits j y := by
          rw [bob_linear_bits j hj h9]
          rw [toBits_ofBits hy]
      simpa only [hval] using
        (cyclic_sourceRuns (all_linear_queries n .bob j u y hj h9 huLen hy))
  runs_factor := by
    intro n w j u hj h9 hu
    cases w
    · have hval :
        indicatorBits (aliceCL.factorOfPrefix (j-1) (ofBits 9 u)) =
          WP14.bitmap (j-1) :=
        alice_factor_bits j hj h9 _
      simpa only [hval, WP14.sourceBitmap] using
        (cyclic_sourceRuns (all_factor_queries n .alice j u hj h9))
    · have hval :
        indicatorBits (bobCL.factorOfPrefix (j-1) (ofBits 9 u)) =
          WP14.bitmap (j-1) :=
        bob_factor_bits j hj h9 _
      simpa only [hval, WP14.sourceBitmap] using
        (cyclic_sourceRuns (all_factor_queries n .bob j u hj h9))
  halts := fun n d => by
    obtain ⟨r,t,hr⟩ := cyclicSamplerProg_halts_raw (.cons (encode n) d)
    exact ⟨r,t,hr⟩

/-- Actual original-native sampler distribution equals the exact 512-edge
CL distribution used to prove the strict rational Bell gap. -/
theorem cyclicSampler_dist (n : Nat) (x y : Questions) :
    cyclicSampler.dist n x y =
      clDist aliceCL.eval bobCL.eval x y := rfl

/-- The positive four-cycle is present in the native `Sampler 9` object. -/
theorem native_four_cycle (n : Nat) (a b : 𝔽₂) :
    0 < cyclicSampler.dist n (left a) (right b) := by
  rw [cyclicSampler_dist]
  exact square_edge_positive a b

/-- An exact original-native stochastic answer-given source game (with
a mathematical, not yet Cost.Prog-executable, synchronous predicate)
has a strict rational quantum/classical gap. -/
noncomputable def sourceGame (n : Nat) : SynchronousGame Questions Bool where
  μ := cyclicSampler.dist n
  μ_nonneg := cyclicSampler.dist_nonneg n
  μ_sum_one := cyclicSampler.sum_dist n
  D := parityAccept
  synchronous := parityAccept_synchronous

theorem sourceGame_eq_parityGame (n : Nat) :
    sourceGame n = parityGame := by
  rfl

theorem all_source_indices_strict_gap (n : Nat) :
    (3/50:ℝ) ≤ quantumValue (sourceGame n).toGame - classicalValue := by
  rw [sourceGame_eq_parityGame]
  exact original_source_quantum_classical_gap.1

end PNPAbove.WP20
