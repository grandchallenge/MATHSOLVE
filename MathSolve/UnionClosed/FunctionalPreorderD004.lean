import MathSolve.UnionClosed.FunctionalPreorderBridge
import MathSolve.UnionClosed.AvgRarePort.Secondary.MainStatement

/-!
# UC-001 WP07 D004 audited source transport

This module closes the semantic gap between the local D003 representation and
the independently audited avg-rare theorem port. The copied proof cone is not
an external trusted dependency: it is compiled as ordinary MATHSOLVE source.

The bridge below is intentionally explicit. Equality of names is not used as
evidence of semantic identity.
-/

namespace MathSolve.UnionClosed.WP07

open Finset
open scoped BigOperators

universe u

variable {α : Type u} [DecidableEq α]

/-- Convert the local D003 functional-preorder datum to the audited port datum.
The fields are intentionally copied without quotienting, relabeling, or changing
the carrier. -/
noncomputable def toAuditedPort (S : FuncSetup α) : AvgRare.FuncSetup α :=
  { ground := S.ground
    nonempty := S.nonempty
    f := S.f }

/-- Local and ported reachability are definitionally the same relation after
the explicit carrier-preserving conversion. -/
theorem toAuditedPort_le_iff (S : FuncSetup α)
    (x y : {z // z ∈ S.ground}) :
    AvgRare.FuncSetup.le (toAuditedPort S) x y ↔ S.le x y := by
  rfl

/-- Ambient reachability agrees exactly across the transport boundary. -/
theorem toAuditedPort_leOn_iff (S : FuncSetup α) (y x : α) :
    AvgRare.FuncSetup.leOn (toAuditedPort S) y x ↔ S.leOn y x := by
  rfl

/-- The local order-ideal predicate and audited-port predicate agree on every
finite subset of the unchanged carrier. -/
theorem toAuditedPort_orderIdeal_iff (S : FuncSetup α) (I : Finset α) :
    AvgRare.SetFamily.isOrderIdealOn
        (AvgRare.FuncSetup.leOn (toAuditedPort S)) S.ground I
      ↔ S.IsOrderIdealOn I := by
  rfl

/-- The D003 finite family is exactly the edge finset of the audited port's
source-shaped ideal family. -/
theorem local_idealFamily_eq_auditedPort_edgeFinset (S : FuncSetup α) :
    S.idealFamily = (toAuditedPort S).idealFamily.edgeFinset := by
  classical
  ext I
  rw [S.mem_idealFamily_iff]
  rw [AvgRare.SetFamily.mem_edgeFinset_iff_sets]
  rw [AvgRare.FuncSetup.sets_iff_isOrderIdeal]
  exact (toAuditedPort_orderIdeal_iff S I).symm

/-- The integer NDS used by D004 is exactly the NDS computed by the audited
ported theorem after the explicit family equality above. -/
theorem functionalPreorderNDS_eq_auditedPort (S : FuncSetup α) :
    FunctionalPreorderNDS S = (toAuditedPort S).idealFamily.NDS := by
  classical
  unfold FunctionalPreorderNDS NDSOn
  unfold AvgRare.SetFamily.NDS AvgRare.SetFamily.totalHyperedgeSize
    AvgRare.SetFamily.numHyperedges
  rw [← local_idealFamily_eq_auditedPort_edgeFinset S]
  rfl

/-- WP07-D004 source-shaped NDS theorem, now proved locally by semantic
transport through the compiled audited proof cone. -/
theorem sourceShapedMainNDS :
    SourceShapedMainNDSStatement α := by
  intro S
  rw [functionalPreorderNDS_eq_auditedPort S]
  exact AvgRare.MainStatement.main_nds_nonpos (toAuditedPort S)

/-- The exact D004 average-rarity target follows from the checked normalization
bridge already established in the D003/D004 interface module. -/
theorem d004_averageRarity :
    D004AverageRarityStatement α :=
  sourceShapedMainNDS_implies_D004 sourceShapedMainNDS

end MathSolve.UnionClosed.WP07
