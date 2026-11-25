import PNPAbove.WP20Native

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

/-- The same constant-zero answers win exactly three of four private-bit
setting combinations on every one of the 128 source components. -/
theorem constant_false_seed (z : Questions) :
    classicalSeedWin (fun _ => false) (fun _ => false) z =
      if bit (z 0) && bit (z 8) then (0:ℝ) else 1 := by
  unfold classicalSeedWin
  rw [parityAccept_source]
  simp [Bool.xor]
  cases h0 : bit (z 0) <;> cases h8 : bit (z 8) <;>
    simp [h0, h8]

theorem constant_false_four (m : Shared) :
    (∑ a : 𝔽₂, ∑ b : 𝔽₂,
      classicalSeedWin (fun _ => false) (fun _ => false)
        (assemble m a b)) = (3:ℝ) := by
  rw [sum_f2, sum_f2, sum_f2]
  simp only [constant_false_seed, extract_assemble_left,
    extract_assemble_right]
  norm_num [bit]

theorem constant_false_global :
    deterministicValue (fun _ => false) (fun _ => false) =
      (3/4:ℝ) := by
  rw [deterministicValue_source, sum_over_seeds]
  simp_rw [constant_false_four]
  simp [shared_card]
  norm_num

/-- The exact unrestricted local classical optimum for the original 512
source question distribution; no mixed local randomness improves it. -/
theorem exact_classical_value :
    classicalValue = (3/4:ℝ) := by
  apply le_antisymm classicalValue_le_three_quarters
  unfold classicalValue
  calc
    (3/4:ℝ) = deterministicValue (fun _ => false) (fun _ => false) :=
      constant_false_global.symm
    _ ≤ ⨆ fB : Questions → Bool,
        deterministicValue (fun _ => false) fB := by
          have hb : BddAbove (Set.range
            (fun fB : Questions → Bool =>
              deterministicValue (fun _ => false) fB)) := by
            refine ⟨1, ?_⟩
            rintro r ⟨g,rfl⟩
            exact (every_classical_strategy_le_three_quarters
              (fun _ => false) g).trans (by norm_num)
          exact le_ciSup hb (fun _ => false)
    _ ≤ ⨆ fA : Questions → Bool,
        ⨆ fB : Questions → Bool, deterministicValue fA fB := by
          have hb : BddAbove (Set.range
            (fun fA : Questions → Bool =>
              ⨆ fB : Questions → Bool, deterministicValue fA fB)) := by
            refine ⟨1, ?_⟩
            rintro r ⟨g,rfl⟩
            apply Real.iSup_le (fun fB =>
              (every_classical_strategy_le_three_quarters g fB).trans
                (by norm_num)) (by norm_num)
          exact le_ciSup hb (fun _ => false)

/-- The sharper final statement: source-native quantum value is at least
81/100 and the exact local classical optimum is 3/4, yielding 3/50 gap. -/
theorem exact_game_gap :
    (3/50:ℝ) ≤ quantumValue parityGame.toGame - classicalValue ∧
    classicalValue = (3/4:ℝ) := by
  exact ⟨original_source_quantum_classical_gap.1, exact_classical_value⟩

end PNPAbove.WP20
