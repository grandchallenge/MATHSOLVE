# WP07 Result Status

Date: 2026-09-16

| Field | Status |
|---|---|
| Work package | WP07 functional-preorder bridge |
| Result status | D001-D003 checked in the current integration package; first proof-bearing D004 bridge checked; D004 main theorem remains open |
| Source branch | `UC-WP03-C007`, functional-preorder order ideals |
| Primary source | Hachimori and Kashiwabara, "Average-Rare Order Ideals in Functional Preorders", arXiv:2511.19833 |
| Historical source pin | `kashiwabarakenji/avg-rare@49c3f1d96ca8518d16e203fd0429ac1216838a4f` |
| Selected source revision | `kashiwabarakenji/avg-rare@21451877e9996a295bbc1ec25856d07fa302d48c` |
| Source drift | Exactly two commits after the historical pin; audited delta is comment-only |
| Toolchain | `leanprover/lean4:v4.23.0`; mathlib `v4.23.0` resolved to `37df177aaa770670452312393d4e84aaad56e7b6` |
| Independent build | `lake update` and `lake build` pass; 879 jobs built |
| Source theorem | `AvgRare.MainStatement.main_nds_nonpos` |
| Source theorem contract | `(S : AvgRare.FuncSetup α) : S.idealFamily.NDS ≤ 0` |
| Source theorem axiom report | `[propext, Classical.choice, Quot.sound]` |
| Placeholder audit | No active `sorry` or `admit`; no explicit source `axiom` declaration found by the exact-revision workflow |
| MATHFORGE provenance | Protected source identity record admitted at `sources/UC-001/AVG_RARE_WP07_SOURCE_PROVENANCE.md` |
| Local theorem surface | `MathSolve/UnionClosed/FunctionalPreorderBridge.lean` |
| Strongest supported local claim | Functional-preorder downward closure is distinct from `IsIdealFamilyOn`; the three-chain obstruction is checked; the exact D003 predicate is defined; local NDS nonpositivity is checked equivalent to local average rarity; a proof of the exact source-shaped NDS statement would discharge D004 |
| Not claimed | No local proof yet of `SourceShapedMainNDSStatement`; no D004 average-rarity theorem yet; no D005 complement theorem; no unrestricted Frankl theorem |
| Foundation route | `R0`, finite and computable |
| Next executable step | Prove or semantically port the exact source-shaped NDS theorem into the local D003 surface, then close D004 before starting D005 |

## Checked local movement

The exact three-element functional chain

```text
f(a) = b
f(b) = c
f(c) = c
```

has exactly the four preorder order ideals

```text
∅, {a}, {a,b}, {a,b,c}.
```

The local theorem `functional_three_chain_not_IsIdealFamilyOn` proves that this
family is not generally `IsIdealFamilyOn`: the proper member `{a,b}` has subset
`{b}`, but `{b}` is not a preorder order ideal.

The new predicate `IsFunctionalPreorderIdealFamilyOn` keeps the finite ground,
source-shaped self-map, generated reachability relation, order-ideal condition,
and extensional family equality explicit. It does not weaken or overload
`IsIdealFamilyOn`.

The D004 target is frozen as `D004AverageRarityStatement`. The checked lemma
`ndsOn_nonpos_iff_averageRareOn` closes the local NDS-normalization bridge, and
`sourceShapedMainNDS_implies_D004` proves that the exact local analogue of the
audited source theorem is sufficient for D004. The theorem
`SourceShapedMainNDSStatement` itself remains proof debt.

## Claim firewall

```text
UC-FRANKL = OPEN_PROBLEM
UC-P04 = OPEN
MATHEMATICAL_TARGET_PROVED = false
PROMOTION_ELIGIBLE = false
```

WP07 remains a restricted theorem-development lane. Nothing in this package
asserts that every union-closed family is a functional-preorder order-ideal
family or a complement of one.
