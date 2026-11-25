import PNPAbove.WP19Global

namespace PNPAbove.WP19
open MIPRE MIPRE.CL MIPRE.Cost Kronecker Matrix
open scoped Classical

variable {X A : Type*} [Fintype X] [Fintype A]
    [DecidableEq X] [DecidableEq A] [Nonempty A]
variable (G : SynchronousGame X A)

/-- The original Born-rule probabilities of a tensor-product MIPRE strategy,
without changing the upstream source definition. -/
noncomputable def tensorCorr (S : TensorProductStrategy G.toGame) :
    X → X → A → A → ℝ :=
  fun x y a b =>
    (star S.ψ ⬝ᵥ ((S.PA.M x a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)).re

/-- Alice's tensor-product outcome marginal does not depend on Bob's
question, by the original PB.normalized projective measurement identity. -/
theorem tensor_left_ns (S : TensorProductStrategy G.toGame)
    (c y : X) (a : A) :
    ∑ b, tensorCorr G S c y a b = ∑ b, tensorCorr G S c c a b := by
  have hmat (y : X) :
      (∑ b, S.PA.M c a ⊗ₖ S.PB.M y b) =
      S.PA.M c a ⊗ₖ (1 : Matrix (Fin S.dB) (Fin S.dB) ℂ) := by
    ext ij kl
    have heval := congrArg
      (fun B : Matrix (Fin S.dB) (Fin S.dB) ℂ =>
        (S.PA.M c a ij.1 kl.1) * B ij.2 kl.2)
      (S.PB.normalized y)
    simpa only [Matrix.sum_apply, kroneckerMap_apply, Finset.mul_sum] using heval
  have hval (y : X) :
      (∑ b, star S.ψ ⬝ᵥ
        ((S.PA.M c a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)) =
      star S.ψ ⬝ᵥ
        ((S.PA.M c a ⊗ₖ (1 : Matrix (Fin S.dB) (Fin S.dB) ℂ)) *ᵥ S.ψ) := by
    calc
      (∑ b, star S.ψ ⬝ᵥ
        ((S.PA.M c a ⊗ₖ S.PB.M y b) *ᵥ S.ψ)) =
        star S.ψ ⬝ᵥ
        ((∑ b, S.PA.M c a ⊗ₖ S.PB.M y b) *ᵥ S.ψ) := by
          simp_rw [Matrix.sum_mulVec, dotProduct_sum]
      _ = _ := by rw [hmat]
  have h := congrArg Complex.re ((hval y).trans (hval c).symm)
  simpa [tensorCorr, Complex.re_sum] using h

theorem tensor_centre_corr (S : TensorProductStrategy G.toGame) (c : X) :
    CentreCorrelation (tensorCorr G S) c where
  nonneg x y a b := S.re_dotProduct_nonneg x y a b
  normalized x y := by
    simpa [tensorCorr, Complex.re_sum] using
      congrArg Complex.re (S.sum_dotProduct_kronecker x y)
  nonsignalling y a := tensor_left_ns G S c y a

/-- The original tracial commuting probabilities, with the upstream C*-state
and projective measurements left unchanged. -/
noncomputable def commCorr (S : CommutingStrategy G) :
    X → X → A → A → ℝ :=
  fun x y a b => (S.τ (S.P.M x a * S.P.M y b)).re

theorem comm_left_ns (S : CommutingStrategy G) (c y : X) (a : A) :
    ∑ b, commCorr G S c y a b = ∑ b, commCorr G S c c a b := by
  have hval (y : X) :
      (∑ b, S.τ (S.P.M c a * S.P.M y b)) = S.τ (S.P.M c a) := by
    rw [← map_sum, ← Finset.mul_sum, S.P.normalized, mul_one]
  have h := congrArg Complex.re ((hval y).trans (hval c).symm)
  simpa [commCorr, Complex.re_sum] using h

theorem comm_centre_corr (S : CommutingStrategy G) (c : X) :
    CentreCorrelation (commCorr G S) c where
  nonneg x y a b :=
    S.τ.re_nonneg_mul (S.P.selfAdjoint x a) (S.P.projective x a)
      (S.P.selfAdjoint y b) (S.P.projective y b)
  normalized x y := by
    have hval :
        (∑ a, ∑ b, S.τ (S.P.M x a * S.P.M y b)) = 1 := by
      have h1 : ∀ a, (∑ b, S.τ (S.P.M x a * S.P.M y b)) =
          S.τ (S.P.M x a) := fun a => by
        rw [← map_sum, ← Finset.mul_sum, S.P.normalized, mul_one]
      simp_rw [h1]
      rw [← map_sum, S.P.normalized, S.τ.map_one]
    simpa [commCorr, Complex.re_sum] using congrArg Complex.re hval
  nonsignalling y a := comm_left_ns G S c y a

/-- The original native strategy value is exactly the abstract correlation
score, not an alternative or simulated game. -/
theorem tensor_value_corr (S : TensorProductStrategy G.toGame) :
    S.value = correlatedPayoff G (tensorCorr G S) := by
  rw [correlatedPayoff_source]
  rfl

theorem comm_value_corr (S : CommutingStrategy G) :
    S.value = correlatedPayoff G (commCorr G S) := by
  rw [correlatedPayoff_source]
  rfl

/-- No tensor-product quantum strategy can outperform the original
dimension-one deterministic synchronous strategies on star+matching support. -/
theorem tensor_star_upper (c : X) (hstar : StarMatching G c)
    (S : TensorProductStrategy G.toGame) :
    S.value ≤ syncValue G := by
  rw [tensor_value_corr G S]
  exact star_correlation_le_syncValue G c hstar _ (tensor_centre_corr G S c)

/-- The same universal upper bound for the original tracial commuting
strategy model, independently of finite tensor-product approximations. -/
theorem commuting_star_upper (c : X) (hstar : StarMatching G c)
    (S : CommutingStrategy G) :
    S.value ≤ syncValue G := by
  rw [comm_value_corr G S]
  exact star_correlation_le_syncValue G c hstar _ (comm_centre_corr G S c)

/-- For arbitrary synchronous acceptance predicates on a star+isolated-
diagonal distribution, original quantum and commuting values are both
exactly the *deterministic* synchronous optimum. -/
theorem star_no_advantage (c : X) (hstar : StarMatching G c) :
    quantumValue G.toGame = syncValue G ∧ commValue G = syncValue G := by
  have hnonneg : (0:ℝ) ≤ syncValue G :=
    Real.iSup_nonneg (fun S : SyncStrategy G => S.value_nonneg)
  constructor
  · exact le_antisymm
      (Real.iSup_le (fun S => tensor_star_upper G c hstar S)
        hnonneg)
      (syncValue_le_quantumValue G)
  · exact le_antisymm
      (Real.iSup_le (fun S => commuting_star_upper G c hstar S)
        hnonneg)
      (syncValue_le_commValue G)

end PNPAbove.WP19
