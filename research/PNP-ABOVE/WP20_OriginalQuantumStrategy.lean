import PNPAbove.WP20Aggregation

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Matrix Finset
open scoped Classical

/-- Original MIPRE synchronous game with the actual CL source distribution
and a genuinely answer-sensitive synchronous Bell predicate. -/
noncomputable def parityGame : SynchronousGame Questions Bool where
  μ := clDist aliceCL.eval bobCL.eval
  μ_nonneg := clDist_nonneg _ _
  μ_sum_one := sum_clDist _ _
  D := parityAccept
  synchronous := parityAccept_synchronous

/-- Original two-dimensional quantum SyncStrategy with explicit rational
projective measurements; no fictitious table of scalar correlations. -/
noncomputable def rationalStrategy : SyncStrategy parityGame where
  d := 2
  d_pos := by omega
  P := quantumMeasurement

/-- A single source seed's original-model tracial strategy win mass. -/
noncomputable def quantumSeedWin (z : Questions) : ℝ :=
  ∑ a : Bool, ∑ b : Bool,
    (if parityAccept (aliceCL.eval z) (bobCL.eval z) a b then
       (1:ℝ) else 0) *
    ((measured (aliceCL.eval z) a *
      measured (bobCL.eval z) b).trace.re / 2)

/-- The native original trace measurement is exactly our rational CHSH
matrix payoff on each actual source seed. -/
theorem quantumSeedWin_matrix (z : Questions) :
    quantumSeedWin z =
      matrixParityWin (selectedProjector (aliceCL.eval z))
        (selectedProjector (bobCL.eval z))
        (bit (z 0) && bit (z 8)) := by
  unfold quantumSeedWin matrixParityWin measured
  simp_rw [parityAccept_source z]
  simp only [decide_eq_true_eq]

theorem alice_projector (z : Questions) :
    selectedProjector (aliceCL.eval z) =
      if z 0 = 1 then pAlice else pCenter := by
  simp [selectedProjector, alice_eval]

theorem bob_projector (z : Questions) :
    selectedProjector (bobCL.eval z) =
      if z 8 = 1 then pBob else pCenter := by
  simp [selectedProjector, bob_eval]

/-- The original quantum strategy's sample payoff depends only on the two
player-private setting bits, not the seven shared context bits. -/
theorem quantumSeedWin_formula (z : Questions) :
    quantumSeedWin z =
      if bit (z 0) then
        (if bit (z 8) then (16/25:ℝ) else 4/5)
      else (if bit (z 8) then (4/5:ℝ) else 1) := by
  rw [quantumSeedWin_matrix, alice_projector, bob_projector]
  by_cases ha : z 0 = 1 <;> by_cases hb : z 8 = 1 <;>
    simp [bit, ha, hb, center_center_value, center_bob_value,
      alice_center_value, alice_bob_value]

/-- Every original 128-component CHSH square has exactly the same rational
quantum total value 81/25 over its four native question edges. -/
theorem quantum_each_square (m : Shared) :
    (∑ a : 𝔽₂, ∑ b : 𝔽₂,
      quantumSeedWin (assemble m a b)) = (81/25:ℝ) := by
  rw [sum_f2, sum_f2, sum_f2]
  simp only [quantumSeedWin_formula, extract_assemble_left, extract_assemble_right]
  norm_num [bit]

/-- Source-uniform quantum win probability on ALL 512 original source seeds,
not a four-edge extrapolation: precisely 81/100. -/
theorem quantum_all_512 :
    ((∑ z : Questions, quantumSeedWin z) / 512) = (81/100:ℝ) := by
  rw [sum_over_seeds]
  simp_rw [quantum_each_square]
  simp [shared_card]
  norm_num

/-- Actual original MIPRE.SyncStrategy value, not an invented correlation
metric: the explicit qubit measurements win 81/100 under CL.clDist. -/
theorem original_quantum_value :
    rationalStrategy.value = (81/100:ℝ) := by
  rw [SyncStrategy.value_eq]
  change
    (∑ x : Questions, ∑ y : Questions, ∑ a : Bool, ∑ b : Bool,
      clDist aliceCL.eval bobCL.eval x y *
        (if parityAccept x y a b then (1:ℝ) else 0) *
        ((measured x a * measured y b).trace.re / 2)) = _
  have heq :
      (∑ x : Questions, ∑ y : Questions, ∑ a : Bool, ∑ b : Bool,
        clDist aliceCL.eval bobCL.eval x y *
          (if parityAccept x y a b then (1:ℝ) else 0) *
          ((measured x a * measured y b).trace.re / 2)) =
      ∑ x : Questions, ∑ y : Questions,
        clDist aliceCL.eval bobCL.eval x y *
          (∑ a : Bool, ∑ b : Bool,
            (if parityAccept x y a b then (1:ℝ) else 0) *
              ((measured x a * measured y b).trace.re / 2)) := by
    apply Finset.sum_congr rfl
    intro x _
    apply Finset.sum_congr rfl
    intro y _
    simp only [Finset.mul_sum]
    apply Finset.sum_congr rfl
    intro a _
    apply Finset.sum_congr rfl
    intro b _
    ring
  rw [heq, clDist_payoff]
  exact quantum_all_512

/-- The real original MIPRE quantum and tracial commuting supremal values
both exceed the classical four-square barrier, via existing upstream
synchronous-to-quantum and synchronous-to-commuting embeddings. -/
theorem original_quantum_lower :
    (81/100:ℝ) ≤ quantumValue parityGame.toGame ∧
    (81/100:ℝ) ≤ commValue parityGame := by
  constructor
  · calc
      (81/100:ℝ) = rationalStrategy.value := original_quantum_value.symm
      _ ≤ syncValue parityGame := by
        have hb : BddAbove
            (Set.range (fun S : SyncStrategy parityGame => S.value)) :=
          ⟨1, by rintro r ⟨S,rfl⟩; exact S.value_le_one⟩
        exact le_ciSup hb rationalStrategy
      _ ≤ quantumValue parityGame.toGame := syncValue_le_quantumValue _
  · calc
      (81/100:ℝ) = rationalStrategy.value := original_quantum_value.symm
      _ ≤ syncValue parityGame := by
        have hb : BddAbove
            (Set.range (fun S : SyncStrategy parityGame => S.value)) :=
          ⟨1, by rintro r ⟨S,rfl⟩; exact S.value_le_one⟩
        exact le_ciSup hb rationalStrategy
      _ ≤ commValue parityGame := syncValue_le_commValue _

end PNPAbove.WP20
