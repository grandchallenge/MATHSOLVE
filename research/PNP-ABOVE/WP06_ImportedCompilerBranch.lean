import MIPRE.Background.Introspection.DecisionCompiler

/-!
PNP-ABOVE WP06: imported compiler-branch proof replay.
Primary upstream: vidick/MIPRE-formalization at
5926bdff5db621f44682a101007ef2fe3ae8d970.
No source definitions are copied. These proofs distinguish the zero-index
and zero-parameter branch from the positive-parameter quantum compiler.
-/
namespace PNPAbove.WP06
open MIPRE
open MIPRE.Cost
open MIPRE.Introspection.DecisionCompiler

theorem zero_parameter_compiles_to_zeroProg
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    compute c U ((S,D),0) = zeroProg := by
  rw [compute_apply]
  rfl

theorem zero_parameter_well_scoped
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    (compute c U ((S,D),0)).WellScoped 1 :=
  compute_closed c U S D 0

theorem zero_parameter_always_runs
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (n : Nat) (d : Data) :
    ∃ t, (decider c U S D 0).prog.Runs
      (.cons (encode n) d) (encode (zeroTest d)) t := by
  exact zero_runs c U S D 0 n (Or.inl rfl) d

theorem zero_parameter_exact_acceptance
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (n : Nat) (x y a b : BitStr) :
    (decider c U S D 0).Accepts n x y a b ↔
      x = [] ∧ y = [] ∧ a.length ≤ 2 ∧ b.length ≤ 2 := by
  exact accepts_zero c U S D 0 n (Or.inl rfl) x y a b

theorem zero_parameter_accepts_empty
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) (n : Nat) :
    (decider c U S D 0).Accepts n ([] : BitStr) [] [] [] := by
  exact (zero_parameter_exact_acceptance c U S D n [] [] [] []).2
    ⟨rfl, rfl, by decide, by decide⟩

theorem zero_parameter_rejects_nonempty_x
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) (n : Nat) :
    ¬ (decider c U S D 0).Accepts n ([true] : BitStr) [] [] [] := by
  intro h
  have hx := (zero_parameter_exact_acceptance c U S D n [true] [] [] []).1 h
  cases hx.1


/-- At a positive parameter, the actual source chooses the zero-wrapped,
clamped, positive-parameter compiler. This proves interface selection;
it does not execute the produced program on a concrete verifier. -/
theorem positive_parameter_compiler_shape
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (lam : Nat) (hl : lam ≠ 0) :
    compute c U ((S,D),lam) =
      zeroWrap (positiveCompiler c U
        (SourceDescriptionCompiler.clamp ((S,D),lam))) := by
  rw [compute_apply]
  simp [hl]

/-- Imported source theorem: the positive-parameter generated decider has
a terminating execution with output specified by the source kernel. -/
theorem positive_parameter_run_specification
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    {lam n : Nat} (hl : 1 ≤ lam) (hn : 1 ≤ n) (d : Data) :
    ∃ t, (decider c U S D lam).prog.Runs (.cons (encode n) d)
      (encode (untypedKernel U (DecisionPreparation.kernelInput c
        (SourceDescriptionCompiler.clamp ((S,D),lam)) (.cons (encode n) d)))) t := by
  exact positive_runs c U S D hl hn d

end PNPAbove.WP06
