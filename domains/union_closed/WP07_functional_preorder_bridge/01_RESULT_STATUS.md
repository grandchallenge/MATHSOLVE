# WP07 Result Status

Date: 2026-09-20

| Field | Status |
|---|---|
| Work package | WP07 functional-preorder bridge |
| Result status | D001-D004 checked locally; D005 is the next open restricted bridge |
| Source branch | `UC-WP03-C007`, functional-preorder order ideals |
| Primary source | Hachimori and Kashiwabara, "Average-Rare Order Ideals in Functional Preorders", arXiv:2511.19833 |
| Historical source pin | `kashiwabarakenji/avg-rare@49c3f1d96ca8518d16e203fd0429ac1216838a4f` |
| Selected source revision | `kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c` |
| Source drift | Exactly two commits after the historical pin; audited delta is comment-only |
| Source toolchain | `leanprover/lean4:v4.23.0`; mathlib `v4.23.0` resolved to `37df177aaa770670452312393d4e84aaad56e7b6` |
| Local transport toolchain | MATHSOLVE `leanprover/lean4:v4.29.1`; mathlib `5e932f97dd25535344f80f9dd8da3aab83df0fe6` |
| Independent source build | `lake update` and `lake build` pass; 879 jobs built |
| Source theorem | `AvgRare.MainStatement.main_nds_nonpos` |
| Source theorem contract | `(S : AvgRare.FuncSetup α) : S.idealFamily.NDS ≤ 0` |
| Source theorem axiom report | `[propext, Classical.choice, Quot.sound]` |
| Placeholder audit | No active `sorry` or `admit`; no explicit source `axiom` declaration found by the exact-revision workflow |
| MATHFORGE provenance | Protected source identity record admitted at `sources/UC-001/AVG_RARE_WP07_SOURCE_PROVENANCE.md` |
| D003 theorem surface | `MathSolve/UnionClosed/FunctionalPreorderBridge.lean` |
| D004 transport surface | `MathSolve/UnionClosed/FunctionalPreorderD004.lean` plus `MathSolve/UnionClosed/AvgRarePort/` |
| Strongest supported local claim | Every family satisfying `IsFunctionalPreorderIdealFamilyOn F U` is average-rare: `d004_averageRarity : D004AverageRarityStatement α` |
| Not claimed | No D005 complement theorem; no representation theorem for arbitrary union-closed families; no unrestricted Frankl theorem |
| Foundation route | `R0`, finite and computable |
| Next executable step | D005: prove complement duality and abundance for the exact D003 class, then compare only that restricted result against WP05/UC-P04 |

## Checked local movement

D002 proves on the exact three-element functional chain that preorder-downward
closure is not WP06's subset-downward `IsIdealFamilyOn` condition.

D003 defines `IsFunctionalPreorderIdealFamilyOn` with the finite ground,
source-shaped self-map, generated reachability relation, order-ideal condition,
and extensional family equality explicit.

D004 is now closed locally. The audited theorem dependency cone from
`avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c` is compiled as ordinary
MATHSOLVE source under `MathSolve/UnionClosed/AvgRarePort/`. The source copy is
not an external build-time dependency. The only post-copy proof edits are
Lean-4.29 compatibility adaptations: import-safe provenance comments,
nonpositive-add simplification, current `Finset.card_sdiff` use, and explicit
subtype-value extensionality.

`FunctionalPreorderD004.lean` then proves the semantic boundary explicitly:

```text
local FuncSetup
  -> carrier-preserving toAuditedPort
  -> identical reachability
  -> identical order-ideal predicate
  -> local idealFamily = ported edgeFinset
  -> local FunctionalPreorderNDS = ported NDS
  -> ported main_nds_nonpos
  -> local SourceShapedMainNDSStatement
  -> local D004AverageRarityStatement.
```

The checked theorems `sourceShapedMainNDS` and `d004_averageRarity` therefore
remove the former D004 proof debt without identifying source and local
definitions merely by name.

## Claim firewall

```text
UC-FRANKL = OPEN_PROBLEM
UC-P04 = OPEN
WP07-D004 = CLOSED_LOCAL
WP07-D005 = OPEN
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

WP07 remains a restricted theorem-development lane. Nothing in this package
asserts that every union-closed family is a functional-preorder order-ideal
family or the complement of one.
