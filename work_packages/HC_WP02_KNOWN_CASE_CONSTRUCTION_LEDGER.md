# HC-WP02 — Higher-dimensional known-case and construction ledger

**Campaign:** `HC-001`  
**State:** `CURRENT_FOR_HC-R021_SELECTION`  
**Audit date:** 2026-09-16  
**Executable ledger:** `campaign_ledgers/HC-001/known_case_construction_ledger.json`

## Objective

Reconstruct the algebraic-cycle mechanism, rather than only theorem names, for the higher-dimensional families that materially constrain HC-R021 selection.

This ledger is current enough for the present selection gate. It is not represented as a comprehensive bibliography of every known Hodge case.

## Material source update

The July 24 Forge ledger is no longer sufficient by itself for target selection. Current primary sources record two material developments:

1. Markman's secant-sheaf construction proves algebraicity of Weil classes for all abelian fourfolds of Weil type and for split-Weil abelian sixfolds; combined with the low-dimensional Hodge-ring structure, the Hodge conjecture holds for all abelian varieties of dimension at most five.
2. Markman's current Section 12 gives an explicit higher-dimensional secant object on a principally polarized abelian fourfold and leaves a sharply stated weak-semiregularity question open. This creates a concrete split-Weil eightfold construction lane.

Mostaed's 2026 sixfold analysis independently confirms that outside the split locus the Weil-class problem remains open and identifies missing secant/discriminant control rather than an existing cycle-producing theorem.

## Selection effect

The following candidates are rejected as already-known terrain:

- abelian fourfolds;
- all abelian varieties of dimension at most five;
- algebraicity of Weil classes on split-Weil abelian sixfolds.

The non-split Weil sixfold boundary is retained as mathematically attractive but deferred because the current sources expose no executable cycle-construction mechanism.

The selected lane is therefore:

```text
HC-R021-A8-SW-Q3
```

for the generic Hodge-ring locus in the `K=Q(sqrt(-3))` split-Weil abelian-eightfold component attached to Markman's Section-12 construction.

## Source locators

- Eyal Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403v2: Theorem 1.2, Corollary 1.3, Sections 4, 11.5, 12, and Question 11.4.
- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2.
- Amir Mostaed, *McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds*, arXiv:2603.20268.
- Salvatore Floccari and Lie Fu, *The Hodge conjecture for Weil fourfolds with discriminant 1 via singular OG6-varieties*, arXiv:2504.13607.
- Steven Zucker, *The Hodge conjecture for cubic fourfolds*, Compositio Mathematica 34 (1977), 199-209.

## Claim boundary

The source refresh rejects stale candidate targets and exposes one open construction lane. It does not establish a new known case, novelty, priority, or any claim beyond the exact literature-derived boundaries recorded in the ledger.
