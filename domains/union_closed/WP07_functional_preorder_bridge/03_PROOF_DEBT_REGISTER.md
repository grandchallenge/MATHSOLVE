# WP07 Proof Debt Register

Date: 2026-09-16

| Debt ID | Obligation | Status | Evidence / remaining gate |
|---|---|---|---|
| WP07-D001 | Reconcile, independently build, and audit the selected `kashiwabarakenji/avg-rare` revision. | Closed for source/build audit | Selected `21451877e9996a295bbc1ec25856d07fa302d48c`; historical pin preserved; two-commit delta is comment-only; Lean 4.23.0 / mathlib v4.23.0; `lake update` and 879-job `lake build` pass; no active `sorry`/`admit`; no explicit source `axiom`; `AvgRare.MainStatement.main_nds_nonpos` axiom report is `[propext, Classical.choice, Quot.sound]`. |
| WP07-D002 | Formalize the finite functional-chain obstruction to direct `IsIdealFamilyOn` reuse. | Closed in the local integration package | `functional_three_chain_not_IsIdealFamilyOn`; exact four-member family also checked by `chain_idealFamily_eq_expected`. |
| WP07-D003 | Define a local functional-preorder order-ideal family predicate over `Family α`. | Closed in the local integration package | `IsFunctionalPreorderIdealFamilyOn`; explicit finite carrier and extensional family equality; source-shaped `FuncSetup`, reachability, and order-ideal semantics. |
| WP07-D004 | Prove or port average rarity for the local functional-preorder predicate. | In progress | Exact target `D004AverageRarityStatement` frozen. `ndsOn_nonpos_iff_averageRareOn` and `sourceShapedMainNDS_implies_D004` are checked. Remaining substantive debt is a local proof/transport of `SourceShapedMainNDSStatement`. |
| WP07-D005 | Connect local functional-preorder average rarity to complement abundance. | Deferred | Requires local closure of D004 first, then a separate checked complement-duality theorem for this predicate. |

## D004 trust boundary

The external declaration `AvgRare.MainStatement.main_nds_nonpos` is source and
proof provenance. Its independent build does not make it a governed local
MATHSOLVE theorem. D004 closes only when the mathematical content is proved or
semantically transported into the local trusted boundary without importing the
external repository as authority.

The current checked bridge is deliberately conditional:

```text
local SourceShapedMainNDSStatement
  -> local D004AverageRarityStatement.
```

This is substantive semantic movement, but it is not the missing NDS proof.

## Non-Debt

WP07 does not reopen the checked WP06 ideal-family NDS proof. It uses WP06 as a
comparison point and later duality pattern. The D002 theorem establishes why
WP06's subset-downward predicate cannot be reused automatically.
