import MIPRE.Background.Introspection.DecisionCompiler

/-!
PNP-ABOVE WP07: source-faithful size-budget complement to WP06 erasure.
Pinned upstream vidick/MIPRE-formalization 5926bdff5db621f44682a101007ef2fe3ae8d970.
This is a theorem about the compiled DECIDER's source metadata.
It neither computes positive-lambda output bytes nor proves full-game injectivity.
-/

namespace PNPAbove.WP07
open MIPRE
open MIPRE.Cost
open MIPRE.Introspection
open MIPRE.Introspection.DecisionCompiler

/-- The actual upstream source-clamp preserves both input programs when
the supplied source-description budget dominates both encoded sizes. -/
theorem adequate_size_preserves_clamp
    (S D : Prog) (lam : Nat)
    (hS : esize S ≤ lam) (hD : esize D ≤ lam) :
    SourceDescriptionCompiler.clamp ((S,D),lam) = ((S,D),lam) := by
  exact SourceDescriptionCompiler.clamp_eq_self S D lam hS hD

/-- The positive compiler receives its original source metadata when
lambda is both positive and large enough for both source descriptions. -/
theorem adequate_size_keeps_compiler_metadata
    (c : Nat) (U : ClockedUniversalMachine)
    (S D : Prog) (lam : Nat) (hl : lam ≠ 0)
    (hS : esize S ≤ lam) (hD : esize D ≤ lam) :
    compute c U ((S,D),lam) =
      zeroWrap (positiveCompiler c U ((S,D),lam)) := by
  rw [compute_apply]
  rw [if_neg hl]
  rw [adequate_size_preserves_clamp S D lam hS hD]

/-- A constructive INPUT-DESCRIPTION size budget.
This says nothing yet about other boundedness/time conditions. -/
theorem size_budget_max_plus_one
    (c : Nat) (U : ClockedUniversalMachine) (S D : Prog) :
    compute c U ((S,D),max (esize S) (esize D) + 1) =
      zeroWrap (positiveCompiler c U
        ((S,D),max (esize S) (esize D) + 1)) := by
  apply adequate_size_keeps_compiler_metadata
  · omega
  · omega
  · omega

end PNPAbove.WP07
