import MIPRE.Background.Introspection.DecisionCompiler

/-! WP05: imported source compiler regression obligations.
Pinned upstream: vidick/MIPRE-formalization
5926bdff5db621f44682a101007ef2fe3ae8d970.
This file is pending standalone Lean replay; it does not claim
to run the full positive-parameter quantum compression procedure. -/

namespace PNPAbove.WP05
open MIPRE
open MIPRE.Cost
open MIPRE.Introspection.DecisionCompiler

theorem zero_parameter_source_branch
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    compute c U ((S, D), 0) = zeroProg := by
  rw [compute_apply]
  rfl

theorem zero_parameter_closed
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    (compute c U ((S, D), 0)).WellScoped 1 :=
  compute_closed c U S D 0

theorem zero_parameter_runs
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog)
    (n : Nat) (d : Data) :
    ∃ t, (decider c U S D 0).prog.Runs
      (.cons (encode n) d) (encode (zeroTest d)) t := by
  exact zero_runs c U S D 0 n (Or.inl rfl) d

end PNPAbove.WP05
