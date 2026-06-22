# WP07 Proof Debt Register

Date: 2026-06-22

| Debt ID | Obligation | Status | Promotion Gate |
|---|---|---|---|
| WP07-D001 | Build/audit `kashiwabarakenji/avg-rare` at `49c3f1d96ca8518d16e203fd0429ac1216838a4f`. | Open | Record toolchain, dependencies, build result, theorem names, and placeholder scan. |
| WP07-D002 | Formalize the finite functional-chain obstruction to direct `IsIdealFamilyOn` reuse. | Open | Lean theorem compiles locally with no new axioms or placeholders. |
| WP07-D003 | Define a local functional-preorder order-ideal family predicate over `Family alpha`. | Open | Predicate preserves finite carrier conventions and does not alter WP06 public representation. |
| WP07-D004 | Prove or port average rarity for the local preorder-order-ideal predicate. | Deferred | Requires either a checked local proof or audited/ported external proof surface. |
| WP07-D005 | Connect local preorder-order-ideal average rarity to union-closed complement abundance. | Deferred | Requires D003 and D004, plus a checked complement-duality statement for the new predicate. |

## Non-Debt

WP07 does not reopen the checked WP06 ideal-family NDS proof. It uses WP06 as a
comparison point and possible duality pattern, not as a theorem that already
solves the functional-preorder branch.

