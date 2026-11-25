import PNPAbove.WP20Expectation

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

theorem f2_univ : (Finset.univ : Finset 𝔽₂) = {0, 1} := by
  ext x
  constructor
  · intro _
    fin_cases x
    · exact Finset.mem_insert_self _ _
    · exact Finset.mem_insert_of_mem (Finset.mem_singleton_self _)
  · intro _
    exact Finset.mem_univ _

theorem sum_f2 (f : 𝔽₂ → ℝ) :
    (∑ a : 𝔽₂, f a) = f 0 + f 1 := by
  change (∑ a ∈ (Finset.univ : Finset 𝔽₂), f a) = _
  rw [f2_univ]
  simp [Finset.sum_insert]

/-- The original 512 source seeds are a perfect product of 128 shared
seven-bit labels and exactly two two-bit private setting choices. -/
theorem sum_over_seeds (f : Questions → ℝ) :
    (∑ z : Questions, f z) =
    ∑ m : Shared, ∑ a : 𝔽₂, ∑ b : 𝔽₂,
       f (assemble m a b) := by
  calc
    (∑ z : Questions, f z) =
      ∑ p : Shared × (𝔽₂ × 𝔽₂), f (seedsEquiv.symm p) :=
        (Equiv.sum_comp seedsEquiv.symm f).symm
    _ = _ := by
      simp only [Fintype.sum_prod_type]
      rfl

/-- The deterministic classical payoff on one original random source seed. -/
def classicalSeedWin (fA fB : Questions → Bool) (z : Questions) : ℝ :=
  if parityAccept (aliceCL.eval z) (bobCL.eval z)
       (fA (aliceCL.eval z)) (fB (bobCL.eval z))
  then 1 else 0

/-- Exact four-square classical bound for each *individual* shared-register
context, not just one selected square. -/
theorem shared_classical_four (fA fB : Questions → Bool) (m : Shared) :
    (∑ a : 𝔽₂, ∑ b : 𝔽₂,
       classicalSeedWin fA fB (assemble m a b)) ≤ 3 := by
  rw [sum_f2, sum_f2, sum_f2]
  unfold classicalSeedWin
  simp only [alice_assemble, bob_assemble]
  have h00 : parityAccept (leftQ m 0) (rightQ m 0)
      (fA (leftQ m 0)) (fB (rightQ m 0)) =
      decide ((fA (leftQ m 0)).xor (fB (rightQ m 0)) = false) := by
    rw [← alice_assemble m 0 0, ← bob_assemble m 0 0,
      parityAccept_source, extract_assemble_left, extract_assemble_right]
    rfl
  have h01 : parityAccept (leftQ m 0) (rightQ m 1)
      (fA (leftQ m 0)) (fB (rightQ m 1)) =
      decide ((fA (leftQ m 0)).xor (fB (rightQ m 1)) = false) := by
    rw [← alice_assemble m 0 1, ← bob_assemble m 0 1,
      parityAccept_source, extract_assemble_left, extract_assemble_right]
    rfl
  have h10 : parityAccept (leftQ m 1) (rightQ m 0)
      (fA (leftQ m 1)) (fB (rightQ m 0)) =
      decide ((fA (leftQ m 1)).xor (fB (rightQ m 0)) = false) := by
    rw [← alice_assemble m 1 0, ← bob_assemble m 1 0,
      parityAccept_source, extract_assemble_left, extract_assemble_right]
    rfl
  have h11 : parityAccept (leftQ m 1) (rightQ m 1)
      (fA (leftQ m 1)) (fB (rightQ m 1)) =
      decide ((fA (leftQ m 1)).xor (fB (rightQ m 1)) = true) := by
    rw [← alice_assemble m 1 1, ← bob_assemble m 1 1,
      parityAccept_source, extract_assemble_left, extract_assemble_right]
    rfl
  simpa only [h00, h01, h10, h11, decide_eq_true_eq, add_assoc] using
    (chsh_four_classical_bound
      (fA (leftQ m 0)) (fA (leftQ m 1))
      (fB (rightQ m 0)) (fB (rightQ m 1)))

/-- Global original CL source classical win fraction is at most 3/4 over
all 512 equally likely seeds, for every deterministic answer function. -/
theorem source_classical_upper (fA fB : Questions → Bool) :
    ((∑ z : Questions, classicalSeedWin fA fB z) / 512) ≤ (3/4:ℝ) := by
  rw [sum_over_seeds]
  have h := Finset.sum_le_sum (s := Finset.univ) (fun m (_ : m ∈ Finset.univ) =>
    shared_classical_four fA fB m)
  have hc : (∑ _ : Shared, (3:ℝ)) = 128*3 := by
    simp [shared_card]
  rw [hc] at h
  apply (div_le_iff₀ (by norm_num : (0:ℝ)<512)).mpr
  norm_num
  linarith

end PNPAbove.WP20
