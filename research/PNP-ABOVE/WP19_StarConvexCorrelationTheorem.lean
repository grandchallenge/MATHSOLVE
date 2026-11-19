import PNPAbove.WP19Envelope

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

variable {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq X] [DecidableEq A] [Nonempty A]

/-- The exact source game payoff, with joint correlation outcomes factored
inside the outer question distribution. -/
noncomputable def correlatedPayoff (G : SynchronousGame X A)
    (p : X → X → A → A → ℝ) : ℝ :=
  ∑ x, ∑ y, G.μ x y * outcomeWin G p x y

/-- Same finite sum for a dimension-one deterministic original strategy. -/
noncomputable def deterministicPayoff (G : SynchronousGame X A)
    (c : X) (v : A) : ℝ :=
  ∑ x, ∑ y, G.μ x y * selectedWin G c v x y

theorem deterministicPayoff_source (G : SynchronousGame X A)
    (c : X) (v : A) :
    deterministicPayoff G c v =
      (WP16.chosenStrategy G (starAnswer G c v)).value := by
  rw [WP16.chosenStrategy_value]
  rfl

/-- Interchange the finite centre-response sum with the two question sums.
No asymptotic, compactness, or operator-algebra assumption is used. -/
theorem weighted_sum_comm (G : SynchronousGame X A) (c : X)
    (p : X → X → A → A → ℝ) :
    (∑ x, ∑ y, G.μ x y *
       (∑ v, centreMarginal p c v * selectedWin G c v x y)) =
    ∑ v, centreMarginal p c v * deterministicPayoff G c v := by
  unfold deterministicPayoff
  calc
    (∑ x, ∑ y, G.μ x y *
       (∑ v, centreMarginal p c v * selectedWin G c v x y)) =
    ∑ x, ∑ y, ∑ v,
       centreMarginal p c v * (G.μ x y * selectedWin G c v x y) := by
        apply Finset.sum_congr rfl
        intro x _
        apply Finset.sum_congr rfl
        intro y _
        rw [Finset.mul_sum]
        apply Finset.sum_congr rfl
        intro v _
        ring
    _ = ∑ v, ∑ x, ∑ y,
       centreMarginal p c v * (G.μ x y * selectedWin G c v x y) := by
        calc
          (∑ x, ∑ y, ∑ v, centreMarginal p c v *
             (G.μ x y * selectedWin G c v x y)) =
          ∑ x, ∑ v, ∑ y, centreMarginal p c v *
             (G.μ x y * selectedWin G c v x y) := by
              apply Finset.sum_congr rfl
              intro x _
              rw [Finset.sum_comm]
          _ = _ := by rw [Finset.sum_comm]
    _ = ∑ v, centreMarginal p c v *
       (∑ x, ∑ y, G.μ x y * selectedWin G c v x y) := by
        apply Finset.sum_congr rfl
        intro v _
        simp only [Finset.mul_sum]

/-- Star plus disjoint diagonal support: every normalized no-signalling
correlation is upper-bounded by the original finite-dimensional synchronous
supremum, with a dimension-one classical strategy already available. -/
theorem star_correlation_le_syncValue (G : SynchronousGame X A) (c : X)
    (hstar : StarMatching G c)
    (p : X → X → A → A → ℝ) (hp : CentreCorrelation p c) :
    correlatedPayoff G p ≤ syncValue G := by
  classical
  unfold correlatedPayoff
  calc
    (∑ x, ∑ y, G.μ x y * outcomeWin G p x y)
        ≤ ∑ x, ∑ y, G.μ x y *
            (∑ v, centreMarginal p c v * selectedWin G c v x y) := by
          apply Finset.sum_le_sum
          intro x _
          apply Finset.sum_le_sum
          intro y _
          exact pair_win_upper G c hstar p hp x y
    _ = ∑ v, centreMarginal p c v * deterministicPayoff G c v :=
        weighted_sum_comm G c p
    _ ≤ ∑ v, centreMarginal p c v * syncValue G := by
          apply Finset.sum_le_sum
          intro v _
          rw [deterministicPayoff_source]
          exact mul_le_mul_of_nonneg_left
            (le_ciSup (WP15.source_strategies_bddAbove G)
              (WP16.chosenStrategy G (starAnswer G c v)))
            (centreMarginal_nonneg p c hp v)
    _ = syncValue G := by
          rw [← Finset.sum_mul, centreMarginal_sum_one p c hp, one_mul]

/-- MIPRE's native source tensor-product/commuting values are written as
finite question and outcome sums, so this equality bridges the generic
correlation payoff without changing the definition of strategy or value. -/
theorem correlatedPayoff_source (G : SynchronousGame X A)
    (p : X → X → A → A → ℝ) :
    correlatedPayoff G p =
      ∑ x, ∑ y, ∑ a, ∑ b, G.μ x y *
        (if G.D x y a b then (1:ℝ) else 0) * p x y a b := by
  unfold correlatedPayoff outcomeWin
  apply Finset.sum_congr rfl
  intro x _
  apply Finset.sum_congr rfl
  intro y _
  simp only [Finset.mul_sum, mul_assoc]

end PNPAbove.WP19
