import PNPAbove.WP18Value

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost

abbrev Questions := Fin 9 → 𝔽₂
def center : Questions := 0

private theorem bit_cases : ∀ a : 𝔽₂, a = 0 ∨ a = 1 := by decide

/-- First seed coordinate controls all other Alice output coordinates. -/
theorem alice_eval (z : Questions) :
    WP14.conditionalNineCL.eval z =
      (if z 0 = 1 then z else (0 : Questions)) := by
  rw [← (CLFun.truncate_self WP14.conditionalNineCL)]
  rw [WP14.conditional_marginal_formula 9 (by omega) (by omega) z]
  by_cases h : z 0 = 1
  · funext i
    simp [WP14.semanticMarginal, h, i.isLt]
  · have hzero : z 0 = 0 := by
      rcases bit_cases (z 0) with hz | hz
      · exact hz
      · exact False.elim (h hz)
    funext i
    fin_cases i <;>
      simp [WP14.semanticMarginal, h, hzero]

/-- The original Bob map is exactly the identity on all seeds. -/
theorem bob_eval (z : Questions) : WP18.bobNineCL.eval z = z := by
  rw [← (CLFun.truncate_self WP18.bobNineCL)]
  rw [WP18.bob_marginal_formula 9 (by omega) (by omega) z]
  funext i
  simp [i.isLt]

/-- Exhaustive original CL support *shape*, with no appeal to finite samples:
either Alice has the zero question and Bob's first bit is zero; or both
players receive the same question whose first bit is one. -/
theorem question_support (n : Nat) (x y : Questions)
    (hμ : WP18.asymmetricSampler.dist n x y ≠ 0) :
    (x = center ∧ y 0 = 0) ∨ (x = y ∧ x 0 = 1) := by
  change clDist WP14.conditionalNineCL.eval WP18.bobNineCL.eval x y ≠ 0 at hμ
  let f : Finset Questions :=
    Finset.univ.filter (fun z => WP14.conditionalNineCL.eval z = x ∧
       WP18.bobNineCL.eval z = y)
  have hcard : 0 < f.card := by
    have hn : f.card ≠ 0 := by
      intro hc
      apply hμ
      simp [clDist, f, hc]
    omega
  obtain ⟨z, hz⟩ := Finset.card_pos.mp hcard
  have hz' : WP14.conditionalNineCL.eval z = x ∧ WP18.bobNineCL.eval z = y := by
    simpa [f] using hz
  rw [alice_eval, bob_eval] at hz'
  by_cases h : z 0 = 1
  · right
    simp [h] at hz'
    exact ⟨hz'.1.symm.trans hz'.2, by simpa [hz'.1] using h⟩
  · left
    have h0 : z 0 = 0 := by
      rcases bit_cases (z 0) with hz | hz
      · exact hz
      · exact False.elim (h hz)
    simp [h, center] at hz'
    exact ⟨hz'.1.symm, by simpa [hz'.2] using h0⟩

/-- In particular WP18 has no question edges between distinct noncentral
Alice questions, and no diagonal mass at the nonzero star leaves. -/
theorem no_leaf_diagonal (n : Nat) (x : Questions)
    (hx : x ≠ center) (h0 : x 0 = 0) :
    WP18.asymmetricSampler.dist n x x = 0 := by
  by_contra h
  rcases question_support n x x h with ⟨hc, _⟩ | ⟨_, h1⟩
  · exact hx hc
  · have : (0 : 𝔽₂) = 1 := h0.symm.trans h1
    exact zero_ne_one this

end PNPAbove.WP19
