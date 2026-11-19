import PNPAbove.WP17

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost Finset

/-- Bob uses each of the nine singleton registers *unconditionally*.
Alice retains the genuinely prefix-dependent nine-stage CL presentation. -/
def bobNineCL : CLFun 𝔽₂ (Fin 9) 9 :=
  .cons {0} (RegLinear.id {0})
    (fun _ => WP14.tailChain WP14.tailCoordinates true)

theorem bobNineCL_exactlyOn : bobNineCL.ExactlyOn (Finset.univ : Finset (Fin 9)) := by
  change ({0} : Finset (Fin 9)) ⊆ Finset.univ ∧
    ∀ (v : Fin 9 → 𝔽₂), (WP14.tailChain WP14.tailCoordinates true).ExactlyOn (Finset.univ \ {0})
  constructor
  · exact Finset.subset_univ _
  · intro v
    have ht := WP14.tailChain_exactlyOn WP14.tailCoordinates (by decide) true
    have heq : WP14.tailCoordinates.toFinset = Finset.univ \ ({0} : Finset (Fin 9)) := by decide
    simpa only [← heq] using ht

theorem bobNineCL_factor_singleton (j : Nat) (hj : 1 ≤ j) (h9 : j ≤ 9)
    (u : Fin 9 → 𝔽₂) :
    bobNineCL.factorOfPrefix (j-1) u =
      ({⟨j-1, by omega⟩} : Finset (Fin 9)) := by
  interval_cases j <;> simp [bobNineCL, WP14.tailChain, WP14.tailCoordinates]


/-- A concrete shared nine-bit seed: coordinate zero is zero, coordinate one
is one and all other coordinates are zero. -/
def offDiagonalSeed : Fin 9 → 𝔽₂ :=
  fun i => if i = 1 then 1 else 0

/-- The original Alice conditional map suppresses the second bit, whereas
Bob's unconditional map reads it. No 512-input extrapolation is used. -/
theorem alice_seed_bit_one :
    (WP14.conditionalNineCL.eval offDiagonalSeed) (1 : Fin 9) = 0 := by
  decide

theorem bob_seed_bit_one :
    (bobNineCL.eval offDiagonalSeed) (1 : Fin 9) = 1 := by
  decide

theorem semantic_off_diagonal :
    WP14.conditionalNineCL.eval offDiagonalSeed ≠
      bobNineCL.eval offDiagonalSeed := by
  intro h
  have hbit := congrFun h (1 : Fin 9)
  rw [alice_seed_bit_one, bob_seed_bit_one] at hbit
  exact zero_ne_one hbit

/-- At least one seed lies over an unequal pair of original CL questions. -/
theorem original_cl_dist_positive :
    0 < clDist WP14.conditionalNineCL.eval bobNineCL.eval
      (WP14.conditionalNineCL.eval offDiagonalSeed)
      (bobNineCL.eval offDiagonalSeed) := by
  classical
  unfold clDist
  have hmem : offDiagonalSeed ∈
    (Finset.univ.filter (fun x : Fin 9 → 𝔽₂ =>
      WP14.conditionalNineCL.eval x =
        WP14.conditionalNineCL.eval offDiagonalSeed ∧
      bobNineCL.eval x = bobNineCL.eval offDiagonalSeed)) := by
    simp
  have hpos : (0 : ℝ) <
      ((Finset.univ.filter (fun x : Fin 9 → 𝔽₂ =>
        WP14.conditionalNineCL.eval x =
          WP14.conditionalNineCL.eval offDiagonalSeed ∧
        bobNineCL.eval x = bobNineCL.eval offDiagonalSeed)).card : ℝ) := by
    exact_mod_cast Finset.card_pos.mpr ⟨offDiagonalSeed, hmem⟩
  have hden : (0 : ℝ) < Fintype.card (Fin 9 → 𝔽₂) := by
    exact_mod_cast Fintype.card_pos
  exact div_pos hpos hden

end PNPAbove.WP18
