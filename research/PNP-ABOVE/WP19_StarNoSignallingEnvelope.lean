import PNPAbove.WP19Choice
import PNPAbove.WP19Scalar

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost
open scoped Classical

variable {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq X] [DecidableEq A] [Nonempty A]

/-- Joint correlation mass on the accepted answers to one sampled pair. -/
noncomputable def outcomeWin (G : SynchronousGame X A)
    (p : X → X → A → A → ℝ) (x y : X) : ℝ :=
  ∑ a, ∑ b, (if G.D x y a b then (1:ℝ) else 0) * p x y a b

/-- Value of the original deterministic synchronous source strategy
selected by the centre answer `v`, on a single pair. -/
noncomputable def selectedWin (G : SynchronousGame X A)
    (c : X) (v : A) (x y : X) : ℝ :=
  if G.D x y (starAnswer G c v x) (starAnswer G c v y) then 1 else 0

/-- First-question answer marginal in a chosen centre-pair experiment. -/
noncomputable def centreMarginal
    (p : X → X → A → A → ℝ) (c : X) (a : A) : ℝ :=
  ∑ b, p c c a b

/-- All properties needed to glue a star-shaped bipartite correlation:
positivity, per-edge normalization and no-signalling of Alice's centre
marginal. This abstract source-facing contract does *not* assume quantum
mechanics, so its consequence is strictly stronger than a Bell no-go. -/
structure CentreCorrelation (p : X → X → A → A → ℝ) (c : X) : Prop where
  nonneg : ∀ x y a b, 0 ≤ p x y a b
  normalized : ∀ x y, ∑ a, ∑ b, p x y a b = 1
  nonsignalling : ∀ y a, ∑ b, p c y a b = centreMarginal p c a

theorem centreMarginal_nonneg
    (p : X → X → A → A → ℝ) (c : X)
    (hp : CentreCorrelation p c) (a : A) :
    0 ≤ centreMarginal p c a := by
  unfold centreMarginal
  exact Finset.sum_nonneg (fun b _ => hp.nonneg c c a b)

theorem centreMarginal_sum_one
    (p : X → X → A → A → ℝ) (c : X)
    (hp : CentreCorrelation p c) :
    ∑ a, centreMarginal p c a = 1 :=
  hp.normalized c c

/-- A single star spoke has a classical success upper bound with exactly
the shared centre-response marginal as its mixing weights. -/
theorem spoke_win_upper (G : SynchronousGame X A) (c : X)
    (p : X → X → A → A → ℝ) (hp : CentreCorrelation p c)
    (y : X) (hy : G.μ c y ≠ 0) :
    outcomeWin G p c y ≤
      ∑ v, centreMarginal p c v * selectedWin G c v c y := by
  have hresponse : ∀ a b, G.D c y a b = true →
      G.D c y a (starAnswer G c a y) = true := by
    intro a b h
    have hw := starAnswer_spoke_win G c a b y hy h
    simpa [starAnswer_center] using hw
  unfold outcomeWin
  calc
    (∑ a, ∑ b, (if G.D c y a b then (1:ℝ) else 0) * p c y a b)
      ≤ ∑ a, (∑ b, p c y a b) *
          (if G.D c y a (starAnswer G c a y) then (1:ℝ) else 0) := by
          apply Finset.sum_le_sum
          intro a _
          exact accepted_row_upper (G.D c y) (p c y)
            (hp.nonneg c y) (fun a => starAnswer G c a y) hresponse a
    _ = ∑ v, centreMarginal p c v * selectedWin G c v c y := by
      apply Finset.sum_congr rfl
      intro a _
      rw [hp.nonsignalling y a]
      simp [selectedWin, starAnswer_center]

/-- A sampled noncentral diagonal question is isolated from the star, so a
feasible equal answer is optimal irrespective of its joint correlation. -/
theorem diag_win_upper (G : SynchronousGame X A) (c : X)
    (p : X → X → A → A → ℝ) (hp : CentreCorrelation p c)
    (x : X) (hx : x ≠ c) (hcx : G.μ c x = 0) :
    outcomeWin G p x x ≤
      ∑ v, centreMarginal p c v * selectedWin G c v x x := by
  have hwin : ∀ a b, G.D x x a b = true →
      G.D x x (WP17.chooseAnswer G x) (WP17.chooseAnswer G x) = true := by
    intro a b hD
    have hab : a = b := by
      by_contra h
      have hd := G.synchronous x a b h
      rw [hd] at hD
      cases hD
    exact WP17.chooseAnswer_spec G x ⟨a, by simpa [hab] using hD⟩
  have hbound := accepted_diagonal_upper (G.D x x)
    (G.synchronous x) (WP17.chooseAnswer G x) hwin (p x x)
    (hp.nonneg x x) (hp.normalized x x)
  have hconst : ∀ v, selectedWin G c v x x =
      (if G.D x x (WP17.chooseAnswer G x) (WP17.chooseAnswer G x)
        then (1:ℝ) else 0) := by
    intro v
    simp [selectedWin, starAnswer, hx, hcx]
  unfold outcomeWin
  calc
    (∑ a, ∑ b, (if G.D x x a b then (1:ℝ) else 0) * p x x a b)
      ≤ (if G.D x x (WP17.chooseAnswer G x) (WP17.chooseAnswer G x)
          then (1:ℝ) else 0) := hbound
    _ = ∑ v, centreMarginal p c v * selectedWin G c v x x := by
      simp_rw [hconst]
      rw [← Finset.sum_mul, centreMarginal_sum_one p c hp, one_mul]

/-- For each original question pair, the quantum/no-signalling win mass is
bounded by a convex combination of actual deterministic synchronous wins. -/
theorem pair_win_upper (G : SynchronousGame X A) (c : X)
    (hstar : StarMatching G c)
    (p : X → X → A → A → ℝ) (hp : CentreCorrelation p c)
    (x y : X) :
    G.μ x y * outcomeWin G p x y ≤
      G.μ x y * (∑ v, centreMarginal p c v * selectedWin G c v x y) := by
  by_cases hμ : G.μ x y = 0
  · simp [hμ]
  · apply mul_le_mul_of_nonneg_left ?_ (G.μ_nonneg x y)
    rcases hstar x y hμ with hc | ⟨hxy, hcx⟩
    · subst x
      exact spoke_win_upper G c p hp y hμ
    · subst y
      have hx : x ≠ c := by
        intro hc
        subst x
        exact hμ hcx
      exact diag_win_upper G c p hp x hx hcx

end PNPAbove.WP19
