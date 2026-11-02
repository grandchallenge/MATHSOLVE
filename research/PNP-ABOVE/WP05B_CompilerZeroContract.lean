import MIPRE.Background.Introspection.DecisionCompiler
/-! PNP-ABOVE WP05B. Imported upstream compiler zero-parameter
contract and totality witness. This is a theorem-level test, not a
positive-parameter evaluation or construction of gapCompression.
External source: vidick/MIPRE-formalization at commit
5926bdff5db621f44682a101007ef2fe3ae8d970. -/
namespace PNPAbove.WP05B
open MIPRE MIPRE.Cost MIPRE.Introspection

example (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    DecisionCompiler.compute c U ((S,D),0) = DecisionCompiler.zeroProg := by
  rw [DecisionCompiler.compute_apply]
  rfl

example (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    (DecisionCompiler.compute c U ((S,D),0)).WellScoped 1 :=
  DecisionCompiler.compute_closed c U S D 0

example (c : Nat) (U : ClockedUniversalMachine)
    (S D : Prog) (n : Nat) (payload : Data) :
    ∃ t, (DecisionCompiler.decider c U S D 0).prog.Runs
        (.cons (encode n) payload)
        (encode (DecisionCompiler.zeroTest payload)) t := by
  exact DecisionCompiler.zero_runs c U S D 0 n (Or.inl rfl) payload

end PNPAbove.WP05B
