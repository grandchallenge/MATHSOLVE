import PNPAbove.WP23Probe

/-!
Exact original MIPRE source cost witness for the native CHSH decider.
The runtime bound is derived from actual original source Eval reductions.
-/
namespace PNPAbove.WP23B
open MIPRE MIPRE.Cost PNPAbove.WP21 PNPAbove.WP22
set_option maxRecDepth 8192
set_option maxHeartbeats 1000000

/-- An accepted original-source execution occurs within an explicit,
source-syntactic and input-size-sensitive step budget. This is not inferred
from mathematical parity alone: it uses the verified original Eval machine. -/
theorem native_acceptance_within_explicit_cost (n : Nat) (x y ap bp : BitStr)
    (hacc : maskedParityDecider.Accepts n x y ap bp) :
    ∃ t, t ≤ inspectionSteps maskedParityDeciderProg *
        ((WP08.sample n x y ap bp).size +
          literalCeiling maskedParityDeciderProg + 1) ∧
        Eval [WP08.sample n x y ap bp] maskedParityDeciderProg
          (encode true) t := by
  obtain ⟨r, t, hrun, hbound⟩ :=
    decider_raw_linear (WP08.sample n x y ap bp)
  obtain ⟨u, haccRun⟩ := hacc
  have hres : r = encode true := (Eval.deterministic hrun haccRun).1
  exact ⟨t, hbound, hres ▸ hrun⟩

/-- An entirely explicit Cook--Levin time parameter, sufficient for the
actual accepted source execution and all original validity side conditions.
The bit lengths and original machine execution cost are visible. -/
def nativeTimeParameter (n : Nat) (x y ap bp : BitStr) : Nat :=
  max (max (2 * Nat.size n) (max x.length y.length))
    (max (max ap.length bp.length)
      (inspectionSteps maskedParityDeciderProg *
        ((WP08.sample n x y ap bp).size +
          literalCeiling maskedParityDeciderProg + 1)))

end PNPAbove.WP23B
