import PNPAbove.WP18Bound

namespace PNPAbove.WP18
open MIPRE MIPRE.CL MIPRE.Cost
set_option maxRecDepth 8192

/-! # Exact game-value negative control on a genuine native asymmetric verifier -/

/-- Original source model, not an alternate hand-written game. -/
noncomputable def asymmetricGame (n T : Nat) :
    SynchronousGame (asymmetricVerifier.Questions n) (Verifier.Answers T) :=
  asymmetricVerifier.syncGame n T (asymmetricVerifier_synchronous n)

/-- Original source CL distribution of this actual normal-form verifier has
positive mass at an unequal pair for every index and answer budget. -/
theorem asymmetricGame_off_diagonal (n T : Nat) :
    0 < (asymmetricGame n T).μ
      (WP14.conditionalNineCL.eval offDiagonalSeed)
      (bobNineCL.eval offDiagonalSeed) := by
  exact asymmetricSampler_off_diagonal_mass n

/-- The native original decider still accepts fixed empty answers for
every question pair at every positive index; non-diagonal sampling alone
cannot overcome the *second* obstruction. -/
theorem asymmetricGame_empty_wins (n T : Nat) (hn : n ≠ 0)
    (x y : asymmetricVerifier.Questions n) :
    (asymmetricGame n T).D x y
      (WP15.emptyAnswer T) (WP15.emptyAnswer T) = true := by
  classical
  change decide (asymmetricVerifier.decider.Accepts n
    (CL.toBits x) (CL.toBits y) [] []) = true
  exact decide_eq_true (asymmetricVerifier_accepts_empty n hn x y)

/-- All three *original* game values equal 1 for the genuine bounded,
asymmetric, non-diagonally supported source verifier with unchanged decider. -/
theorem asymmetricGame_values_one (n T : Nat) (hn : n ≠ 0) :
    syncValue (asymmetricGame n T) = 1 ∧
    quantumValue (asymmetricGame n T).toGame = 1 ∧
    commValue (asymmetricGame n T) = 1 := by
  have h := asymmetricGame_empty_wins n T hn
  exact ⟨WP15.syncValue_eq_one_of_constant _ (WP15.emptyAnswer T) h,
    WP15.quantumValue_eq_one_of_constant _ (WP15.emptyAnswer T) h,
    WP15.commValue_eq_one_of_constant _ (WP15.emptyAnswer T) h⟩

/-- An actual non-diagonal sampler is no substitute for an answer-sensitive
hard-game decider: tensor quantum and synchronous optima coincide exactly. -/
theorem asymmetricGame_zero_quantum_advantage (n T : Nat) (hn : n ≠ 0) :
    quantumValue (asymmetricGame n T).toGame -
      syncValue (asymmetricGame n T) = 0 := by
  rw [(asymmetricGame_values_one n T hn).2.1,
    (asymmetricGame_values_one n T hn).1]
  norm_num

end PNPAbove.WP18
