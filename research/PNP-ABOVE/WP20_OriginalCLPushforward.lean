import PNPAbove.WP20Decomp

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

/-- Exact finite pushforward identity: game payoffs under the original
MIPRE.CL.clDist distribution are expectations over the real nine-bit
source seeds, not an alternate or simulated game. -/
theorem clDist_payoff (F : Questions → Questions → ℝ) :
    (∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y * F x y) =
      (∑ z : Questions, F (aliceCL.eval z) (bobCL.eval z)) / 512 := by
  classical
  have hc (x y : Questions) :
      (((Finset.univ.filter (fun z : Questions =>
          aliceCL.eval z = x ∧ bobCL.eval z = y)).card : Nat) : ℝ) =
        ∑ z : Questions,
          if aliceCL.eval z = x ∧ bobCL.eval z = y then (1:ℝ) else 0 := by
    calc
      _ = ∑ z ∈ (Finset.univ.filter (fun z : Questions =>
          aliceCL.eval z = x ∧ bobCL.eval z = y)), (1:ℝ) := by simp
      _ = _ := by rw [Finset.sum_filter]
  have hpair (x y : Questions) :
      clDist aliceCL.eval bobCL.eval x y * F x y =
        ∑ z : Questions,
          if aliceCL.eval z = x ∧ bobCL.eval z = y
          then F x y / 512 else 0 := by
    unfold clDist
    rw [hc, WP19.questions_card]
    rw [div_mul_eq_mul_div, Finset.sum_mul, Finset.sum_div]
    apply Finset.sum_congr rfl
    intro z _
    split_ifs <;> ring
  simp_rw [hpair]
  calc
    (∑ x : Questions, ∑ y : Questions, ∑ z : Questions,
      if aliceCL.eval z = x ∧ bobCL.eval z = y
      then F x y / 512 else 0) =
    ∑ z : Questions, ∑ x : Questions, ∑ y : Questions,
      if aliceCL.eval z = x ∧ bobCL.eval z = y
      then F x y / 512 else 0 := by
        calc
          _ = ∑ x : Questions, ∑ z : Questions, ∑ y : Questions,
              if aliceCL.eval z = x ∧ bobCL.eval z = y
              then F x y / 512 else 0 := by
                apply Finset.sum_congr rfl
                intro x _
                rw [Finset.sum_comm]
          _ = _ := by rw [Finset.sum_comm]
    _ = ∑ z : Questions, F (aliceCL.eval z) (bobCL.eval z) / 512 := by
        apply Finset.sum_congr rfl
        intro z _
        calc
          (∑ x : Questions, ∑ y : Questions,
            if aliceCL.eval z = x ∧ bobCL.eval z = y
            then F x y / 512 else 0) =
            ∑ x : Questions,
              if aliceCL.eval z = x then F x (bobCL.eval z) / 512 else 0 := by
                apply Finset.sum_congr rfl
                intro x _
                by_cases hx : aliceCL.eval z = x
                · simp [hx]
                · simp [hx]
          _ = F (aliceCL.eval z) (bobCL.eval z) / 512 := by simp
    _ = _ := by rw [Finset.sum_div]

end PNPAbove.WP20
