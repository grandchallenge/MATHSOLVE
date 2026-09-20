# WP07 Proof Debt Register

Date: 2026-09-20

| Debt ID | Obligation | Status | Evidence / remaining gate |
|---|---|---|---|
| WP07-D001 | Reconcile, independently build, and audit the selected `kashiwabarakenji/avg-rare` revision. | Closed | Selected `21451877e9996a295bbc1ec25856d07fa302d48c`; historical pin preserved; two-commit delta is comment-only; Lean 4.23.0 / mathlib v4.23.0; `lake update` and 879-job `lake build` pass; no active `sorry`/`admit`; no explicit source `axiom`; `AvgRare.MainStatement.main_nds_nonpos` axiom report is `[propext, Classical.choice, Quot.sound]`. |
| WP07-D002 | Formalize the finite functional-chain obstruction to direct `IsIdealFamilyOn` reuse. | Closed | `functional_three_chain_not_IsIdealFamilyOn`; exact four-member family checked by `chain_idealFamily_eq_expected`. |
| WP07-D003 | Define a local functional-preorder order-ideal family predicate over `Family α`. | Closed | `IsFunctionalPreorderIdealFamilyOn`; explicit finite carrier and extensional family equality; source-shaped `FuncSetup`, reachability, and order-ideal semantics. |
| WP07-D004 | Prove or port average rarity for the local functional-preorder predicate. | Closed locally | `sourceShapedMainNDS` proves `SourceShapedMainNDSStatement`; `d004_averageRarity` proves `D004AverageRarityStatement`. The source proof cone is compiled inside MATHSOLVE and connected to D003 by explicit family/NDS equalities. |
| WP07-D005 | Connect local functional-preorder average rarity to complement abundance. | Open / next | Define the exact complement family on the D003 carrier, prove union closure and rarity-to-abundance transfer, and keep the conclusion restricted to complements of functional-preorder ideal families. |

## D004 trust boundary

The external declaration `AvgRare.MainStatement.main_nds_nonpos` remains source
and proof provenance. D004 is locally governed because the required proof cone
is present and compiled as MATHSOLVE source, while
`FunctionalPreorderD004.lean` proves the semantic correspondence from the
protected D003 representation to that compiled theorem surface.

The transport did not add an external trusted dependency. Relative to the
audited source revision, the port changes module import paths and applies only
Lean-4.29 proof/API compatibility edits. The mathematical theorem statements
used by D004 are unchanged.

The former conditional chain

```text
SourceShapedMainNDSStatement
  -> D004AverageRarityStatement
```

is now discharged by the checked local theorem `sourceShapedMainNDS`.

## Remaining campaign debt

D005 is the next restricted mathematical obligation. Its closure does not imply
`UC-P04` and cannot promote `UC-FRANKL`: a separate representation theorem
for arbitrary union-closed families would still be required.
