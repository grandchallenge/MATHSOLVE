import PNPAbove.WP22Gap

namespace PNPAbove.WP23
open MIPRE MIPRE.CL MIPRE.Cost PNPAbove.WP20 PNPAbove.WP21 PNPAbove.WP22 Finset
open scoped Classical

/-- Every source-input-index-invariant binary local strategy has the
same payoff as the old WP20 Boolean game on the 512 source edges. -/
theorem native_binary_det_eq (n T : Nat) (hn : n ≠ 0) (hT : 1 ≤ T)
    (fA fB : Questions → Bool) :
    nativeDeterministicValue n T
        (fun x => binaryAnswer T hT (fA x))
        (fun y => binaryAnswer T hT (fB y)) =
      deterministicValue fA fB := by
  unfold nativeDeterministicValue deterministicValue
  simp_rw [native_game_binary n T hn hT]
  change
    (∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y *
        (if maskedParityAccept x y (fA x) (fB y) then (1:ℝ) else 0)) =
    (∑ x : Questions, ∑ y : Questions,
      clDist aliceCL.eval bobCL.eval x y *
        (if parityAccept x y (fA x) (fB y) then (1:ℝ) else 0))
  apply Finset.sum_congr rfl
  intro x hx
  apply Finset.sum_congr rfl
  intro y hy
  rcases zero_mass_or_equal_decision x y with hzero | hpred
  · simp [hzero]
  · rw [hpred (fA x) (fB y)]

/-- The native game has a value-3/4 deterministic local response strategy,
for every nonzero source index and source answer budget permitting one bit. -/
theorem native_constant_false_three_quarters (n T : Nat)
    (hn : n ≠ 0) (hT : 1 ≤ T) :
    nativeDeterministicValue n T
        (fun _ => binaryAnswer T hT false)
        (fun _ => binaryAnswer T hT false) = (3/4:ℝ) := by
  rw [native_binary_det_eq n T hn hT]
  exact constant_false_global


/-- The native unrestricted local classical optimum is EXACTLY 3/4,
not merely at most 3/4. This holds for all nonzero indices and budgets
with one-bit answers. No special strategy class was silently removed. -/
theorem native_classical_exact_three_quarters (n T : Nat)
    (hn : n ≠ 0) (hT : 1 ≤ T) :
    nativeClassicalValue n T = (3/4:ℝ) := by
  apply le_antisymm (native_classical_le_three_quarters n T hn)
  unfold nativeClassicalValue
  let f : Questions → Verifier.Answers T :=
    fun _ => binaryAnswer T hT false
  calc
    (3/4:ℝ) = nativeDeterministicValue n T f f :=
      (native_constant_false_three_quarters n T hn hT).symm
    _ ≤ ⨆ fB : Questions → Verifier.Answers T,
        nativeDeterministicValue n T f fB := by
          have hb : BddAbove (Set.range
              (fun fB : Questions → Verifier.Answers T =>
                nativeDeterministicValue n T f fB)) := by
            refine ⟨1, ?_⟩
            rintro v ⟨g,rfl⟩
            exact (native_every_classical_le n T hn f g).trans (by norm_num)
          exact le_ciSup hb f
    _ ≤ ⨆ fA : Questions → Verifier.Answers T,
        ⨆ fB : Questions → Verifier.Answers T,
          nativeDeterministicValue n T fA fB := by
          have hb : BddAbove (Set.range
              (fun fA : Questions → Verifier.Answers T =>
                ⨆ fB : Questions → Verifier.Answers T,
                  nativeDeterministicValue n T fA fB)) := by
            refine ⟨1, ?_⟩
            rintro v ⟨g,rfl⟩
            exact Real.iSup_le
              (fun fB => (native_every_classical_le n T hn g fB).trans
                (by norm_num)) (by norm_num)
          exact le_ciSup hb f

end PNPAbove.WP23
