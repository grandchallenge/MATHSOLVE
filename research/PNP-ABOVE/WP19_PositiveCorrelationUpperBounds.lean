import PNPAbove.WP18Value

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

variable {A : Type*} [Fintype A]

/-- A winning deterministic response to each fixed first answer dominates
every (possibly nonclassical) conditional response distribution on that row.
This statement uses only positivity, not quantum-specific assumptions. -/
theorem accepted_row_upper (D : A → A → Bool) (p : A → A → ℝ)
    (hp : ∀ a b, 0 ≤ p a b) (respond : A → A)
    (hrespond : ∀ a b, D a b = true → D a (respond a) = true)
    (a : A) :
    (∑ b, (if D a b then (1 : ℝ) else 0) * p a b) ≤
    (∑ b, p a b) * (if D a (respond a) then (1 : ℝ) else 0) := by
  by_cases h : D a (respond a) = true
  · simp only [h, ite_true, mul_one]
    apply Finset.sum_le_sum
    intro b _
    by_cases hd : D a b = true
    · simp [hd]
    · have hf : D a b = false := Bool.eq_false_of_ne_true hd
      simpa [hf] using hp a b
  · have hall : ∀ b, D a b = false := by
      intro b
      by_cases hd : D a b = true
      · exact False.elim (h (hrespond a b hd))
      · exact Bool.eq_false_of_ne_true hd
    simp [h, hall]

/-- An isolated synchronous diagonal edge cannot score more than its
best accepted equal-answer decision, regardless of its joint correlation. -/
theorem accepted_diagonal_upper (D : A → A → Bool)
    (hsync : ∀ a b, a ≠ b → D a b = false)
    (w : A) (hwin : ∀ a b, D a b = true → D w w = true)
    (p : A → A → ℝ) (hp : ∀ a b, 0 ≤ p a b)
    (hnorm : ∑ a, ∑ b, p a b = 1) :
    (∑ a, ∑ b, (if D a b then (1 : ℝ) else 0) * p a b) ≤
    (if D w w then (1 : ℝ) else 0) := by
  by_cases hw : D w w = true
  · simp only [hw, ite_true]
    calc
      (∑ a, ∑ b, (if D a b then (1 : ℝ) else 0) * p a b)
          ≤ ∑ a, ∑ b, p a b := by
            apply Finset.sum_le_sum
            intro a _
            apply Finset.sum_le_sum
            intro b _
            by_cases hd : D a b = true
            · simp [hd]
            · have hf : D a b = false := Bool.eq_false_of_ne_true hd
              simpa [hf] using hp a b
      _ = 1 := hnorm
  · have hall : ∀ a b, D a b = false := by
      intro a b
      by_cases hd : D a b = true
      · exact False.elim (hw (hwin a b hd))
      · exact Bool.eq_false_of_ne_true hd
    simp [hw, hall]

end PNPAbove.WP19
