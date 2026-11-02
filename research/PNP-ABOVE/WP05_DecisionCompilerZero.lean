import MIPRE.Background.Introspection.DecisionCompiler
/-!
PNP-ABOVE WP05: direct theorem-level use of the built upstream
MIPRE.Introspection.DecisionCompiler, source revision
5926bdff5db621f44682a101007ef2fe3ae8d970.
This does not evaluate a positive-parameter quantum compression.
-/
namespace PNPAbove.WP05
open MIPRE MIPRE.Cost MIPRE.Introspection

#check DecisionCompiler.compute
#check DecisionCompiler.compute_apply
#check DecisionCompiler.compute_closed
#check DecisionCompiler.zeroProg

example (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    DecisionCompiler.compute c U ((S, D), 0) = DecisionCompiler.zeroProg := by
  simp only [DecisionCompiler.compute_apply, if_pos rfl]

example (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    (DecisionCompiler.compute c U ((S, D), 0)).WellScoped 1 :=
  DecisionCompiler.compute_closed c U S D 0

end PNPAbove.WP05
