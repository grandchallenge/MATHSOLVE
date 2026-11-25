import MIPRE.Background.Introspection.DecisionCompiler

/-!
PNP-ABOVE WP06. Exact upstream source-branch theorem replay.
Source commit: vidick/MIPRE-formalization
5926bdff5db621f44682a101007ef2fe3ae8d970.
This imports actual MIPRE compiler definitions, not copied models.
-/

namespace PNPAbove.WP06
open MIPRE
open MIPRE.Cost
open MIPRE.Introspection.DecisionCompiler

/-- The actual source compiler returns its fixed zero branch at lam=0. -/
theorem zero_parameter_compile
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    compute c U ((S,D),0) = zeroProg := by
  rw [compute_apply]
  rfl

/-- The produced program is a well-scoped native source program. -/
theorem zero_parameter_scoped
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    (compute c U ((S,D),0)).WellScoped 1 :=
  compute_closed c U S D 0

/-- The source Eval relation guarantees a terminating zero-parameter run. -/
theorem zero_parameter_execution
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (n : Nat) (d : Data) :
    ∃ t, (decider c U S D 0).prog.Runs
      (.cons (encode n) d) (encode (zeroTest d)) t := by
  exact zero_runs c U S D 0 n (Or.inl rfl) d

/-- Exact success criterion supplied by the imported source theorem. -/
theorem zero_parameter_criterion
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (n : Nat) (x y a b : BitStr) :
    (decider c U S D 0).Accepts n x y a b ↔
      x = [] ∧ y = [] ∧ a.length ≤ 2 ∧ b.length ≤ 2 := by
  exact accepts_zero c U S D 0 n (Or.inl rfl) x y a b

/-- A completely explicit pair of empty questions is accepted. -/
theorem zero_accepts_empty
    (c : Nat) (U : ClockedUniversalMachine) :
    (decider c U Prog.nil Prog.nil 0).Accepts 1 [] [] [] [] := by
  apply (zero_parameter_criterion c U Prog.nil Prog.nil 1 [] [] [] []).mpr
  simp

/-- A nonempty Alice question is rejected, independently of U. -/
theorem zero_rejects_nonempty
    (c : Nat) (U : ClockedUniversalMachine) :
    ¬ (decider c U Prog.nil Prog.nil 0).Accepts 1 [true] [] [] [] := by
  intro h
  have hx := ((zero_parameter_criterion
    c U Prog.nil Prog.nil 1 [true] [] [] []).mp h).1
  cases hx

/-- The positive-parameter branch remains symbolic: source computes a
zero-wrapped result, not a concrete compressed game in this test. -/
theorem positive_one_branch
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    compute c U ((S,D),1) =
      zeroWrap (positiveCompiler c U
        (MIPRE.Introspection.SourceDescriptionCompiler.clamp ((S,D),1))) := by
  simpa using (compute_apply c U S D 1)

end PNPAbove.WP06
