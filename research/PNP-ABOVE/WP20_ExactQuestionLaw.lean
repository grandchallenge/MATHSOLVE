import PNPAbove.WP20Cycle

namespace PNPAbove.WP20
open MIPRE MIPRE.CL MIPRE.Cost Finset
open scoped Classical

/-- The joint output reconstructs every seed coordinate: Alice supplies bit 0,
Bob supplies bit 8, and either supplies the other seven coordinates. -/
theorem pair_injective {z w : Questions}
    (hA : aliceCL.eval z = aliceCL.eval w)
    (hB : bobCL.eval z = bobCL.eval w) : z = w := by
  rw [alice_eval, alice_eval] at hA
  rw [bob_eval, bob_eval] at hB
  funext i
  by_cases hi : i = 8
  · subst i
    simpa using congrFun hB (8 : Fin 9)
  · simpa [hi] using congrFun hA i

/-- Each original CL fiber over a genuinely sampled question pair is
*exactly* the single seed that produced the pair. -/
theorem fiber_singleton (z : Questions) :
    (Finset.univ.filter (fun w : Questions =>
      aliceCL.eval w = aliceCL.eval z ∧ bobCL.eval w = bobCL.eval z)) =
    {z} := by
  ext w
  simp only [Finset.mem_filter, Finset.mem_univ, true_and, Finset.mem_singleton]
  constructor
  · intro h
    exact pair_injective h.1 h.2
  · intro h
    subst w
    exact ⟨rfl,rfl⟩

/-- Every one of the original 512 seeds gives a distinct ordered question
pair of *exactly* 1/512 mass, not merely positive mass. -/
theorem exact_original_mass (z : Questions) :
    clDist aliceCL.eval bobCL.eval (aliceCL.eval z) (bobCL.eval z) =
      (1/512 : ℝ) := by
  unfold clDist
  rw [fiber_singleton]
  simp [WP19.questions_card]

/-- No unsampled pair can carry positive CL distribution mass. -/
theorem unsupported_zero (x y : Questions)
    (h : ¬ ∃ z : Questions, aliceCL.eval z = x ∧ bobCL.eval z = y) :
    clDist aliceCL.eval bobCL.eval x y = 0 := by
  unfold clDist
  have he : (Finset.univ.filter (fun z : Questions =>
      aliceCL.eval z = x ∧ bobCL.eval z = y)) = ∅ := by
    ext z
    constructor
    · intro hz
      exact False.elim (h ⟨z, (Finset.mem_filter.mp hz).2⟩)
    · simp
  rw [he]
  simp

/-- All seed-pairs are distinct. 512 seeds therefore provide all 512
positive edges of the exact original CL distribution. -/
theorem distinct_output_pairs {z w : Questions}
    (h : (aliceCL.eval z, bobCL.eval z) =
        (aliceCL.eval w, bobCL.eval w)) : z = w :=
  pair_injective (congrArg Prod.fst h) (congrArg Prod.snd h)

/-- Each of the four square edges has exactly the same weight as every
other original sampled edge. -/
theorem square_edge_mass (a b : 𝔽₂) :
    clDist aliceCL.eval bobCL.eval (left a) (right b) = (1/512 : ℝ) := by
  rw [← left_seed a b, ← right_seed a b]
  exact exact_original_mass (seed a b)

end PNPAbove.WP20
