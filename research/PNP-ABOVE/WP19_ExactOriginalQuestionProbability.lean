import PNPAbove.WP19Support

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

/-- The actual WP18 Alice output as a function of Bob's question. -/
def aliceOfBob (y : Questions) : Questions :=
  if y 0 = 1 then y else center

/-- Every original CL fiber is a singleton because Bob's map is identity.
This is stronger than merely knowing there is some off-diagonal mass. -/
theorem fiber_singleton (x y : Questions) :
    (Finset.univ.filter (fun z : Questions =>
      WP14.conditionalNineCL.eval z = x ∧ WP18.bobNineCL.eval z = y)) =
    (if aliceOfBob y = x then {y} else ∅) := by
  classical
  ext z
  simp only [Finset.mem_filter, Finset.mem_univ, true_and]
  rw [alice_eval, bob_eval]
  by_cases h : z = y
  · subst z
    have haux : aliceOfBob y = x ↔
        y ∈ (if aliceOfBob y = x then ({y} : Finset Questions) else ∅) := by
      by_cases ht : aliceOfBob y = x <;> simp [ht]
    simpa [aliceOfBob, center] using haux
  · by_cases ht : aliceOfBob y = x <;> simp [ht, h]

/-- Exact original source question probability: every supported pair has
one seed in a space of cardinality 512; all others have probability zero. -/
theorem exact_probability (n : Nat) (x y : Questions) :
    WP18.asymmetricSampler.dist n x y =
      if aliceOfBob y = x then
        (1:ℝ) / Fintype.card Questions else 0 := by
  change clDist WP14.conditionalNineCL.eval WP18.bobNineCL.eval x y = _
  rw [clDist, fiber_singleton]
  split_ifs with h
  · simp
  · simp

/-- The sample law is exactly 512 uniform pairs. -/
theorem questions_card : Fintype.card Questions = 512 := by
  have hc : Fintype.card 𝔽₂ = 2 := by decide
  simp [Questions, Fintype.card_fun, hc]

theorem exact_probability_512 (n : Nat) (x y : Questions) :
    WP18.asymmetricSampler.dist n x y =
      if aliceOfBob y = x then (1/512:ℝ) else 0 := by
  rw [exact_probability, questions_card]
  norm_num

end PNPAbove.WP19
