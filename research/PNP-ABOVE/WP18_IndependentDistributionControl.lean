import PNPAbove.WP18Sampler

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost

/-! # Strong negative control on the repaired non-diagonal CL distribution -/

/-- Original upstream synchronous game using the genuinely off-diagonal
nine-stage CL law and the *unchanged* original WP14/identity decision
predicate. This game exists independently of whether the full source
Sampler.Query compiler has been universally discharged. -/
noncomputable def asymDistributionIdentityGame (n T : Nat) :
    SynchronousGame (WP14.conditionalVerifier.Questions n) (Verifier.Answers T) where
  μ := clDist WP14.conditionalNineCL.eval bobNineCL.eval
  μ_nonneg := clDist_nonneg _ _
  μ_sum_one := sum_clDist _ _
  D := (WP15.wp14Game n T).D
  synchronous := (WP15.wp14Game n T).synchronous

/-- The original source game distribution is non-diagonal for every n and
every answer budget, even though the old predicate is classically easy. -/
theorem asymGame_off_diagonal_mass (n T : Nat) :
    0 < (asymDistributionIdentityGame n T).μ
      (WP14.conditionalNineCL.eval offDiagonalSeed)
      (bobNineCL.eval offDiagonalSeed) := by
  exact original_cl_dist_positive

theorem asymGame_accepts_empty (n T : Nat) (hn : n ≠ 0)
    (x y : WP14.conditionalVerifier.Questions n) :
    (asymDistributionIdentityGame n T).D x y
      (WP15.emptyAnswer T) (WP15.emptyAnswer T) = true := by
  exact WP15.every_question_accepts_empty n T hn x y

/-- Exact original synchronous/tensor/commuting values, *even after*
fixing the diagonal-support defect but retaining the current decider. -/
theorem nonDiagonal_identity_decider_values_one (n T : Nat) (hn : n ≠ 0) :
    syncValue (asymDistributionIdentityGame n T) = 1 ∧
    quantumValue (asymDistributionIdentityGame n T).toGame = 1 ∧
    commValue (asymDistributionIdentityGame n T) = 1 := by
  have h := asymGame_accepts_empty n T hn
  exact ⟨WP15.syncValue_eq_one_of_constant _ (WP15.emptyAnswer T) h,
    WP15.quantumValue_eq_one_of_constant _ (WP15.emptyAnswer T) h,
    WP15.commValue_eq_one_of_constant _ (WP15.emptyAnswer T) h⟩

end PNPAbove.WP18
