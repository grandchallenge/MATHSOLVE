# HC-WP02 — Higher-dimensional known-case and construction ledger

**Campaign:** `HC-001`  
**State:** `CURRENT_FOR_HC-R021_SELECTION`  
**Audit date:** 2026-09-16  
**Executable ledger:** `campaign_ledgers/HC-001/known_case_construction_ledger.json`

## Objective

Reconstruct the algebraic-cycle mechanism, rather than only theorem names, for the higher-dimensional families that materially constrain HC-R021 selection.

This ledger is current enough for the present selection gate. It is not represented as a comprehensive bibliography of every known Hodge case.

## Material source update

The July 24 Forge ledger is not sufficient by itself for current target selection.

Markman's 2025-2026 secant-sheaf work changes the abelian-variety frontier materially:

- Weil classes on abelian fourfolds are theorem terrain;
- the split-Weil sixfold construction is theorem terrain;
- the current account records the Hodge conjecture for abelian varieties of dimension at most five as a consequence of the fourfold result and known Hodge-ring structure;
- a companion CM-field paper constructs explicit coherent secant sheaves on a genus-four Jacobian with real quadratic multiplication. For the associated abelian eightfold, the Fourier-Mukai object has nonzero rank, its normalized class remains Hodge under Weil-type deformation, and its degree-four component has a nonzero Weil projection. The paper explicitly leaves semiregularity of that object unresolved.

Mostaed's 2026 sixfold analysis independently leaves the non-split sixfold Weil terrain open but does not expose an equally concrete cycle-construction/deformation object there.

## Candidate set and disposition

The selection gate considered three nearby open lanes:

- non-split Weil sixfolds: smaller dimension, but no executable general construction bridge found;
- Markman's degree-four-CM genus-four construction: dimension eight, codimension two, explicit coherent sheaves and nonzero Weil projection already source-proved, semiregularity open;
- Markman's speculative quadratic-CM higher-dimensional secant complex: dimension eight, codimension four, but more construction obligations remain unresolved.

The selected lane is therefore:

```text
HC-R021-A8-CM4-C2
```

restricted to the Hodge-generic locus of the Markman deformation component. This is a source-adjacent research target; novelty and priority are not claimed.

## Source locators

- Eyal Markman, *Secant sheaves on abelian n-folds with real multiplication and Weil classes on abelian 2n-folds with complex multiplication*, arXiv:2509.23079v1: Introduction 1.1, Proposition 8.0.1, Proposition 10.2.1, Example 11.2.7, Lemma 11.2.8, and the Section 11.2 semiregularity question.
- Eyal Markman, *Secant sheaves and Weil classes on abelian varieties*, arXiv:2509.23403v2: Theorem 1.2, Corollary 1.3, Question 11.4, Section 12.
- Eyal Markman, *Cycles on abelian 2n-folds of Weil type from secant sheaves on abelian n-folds*, arXiv:2502.03415v2.
- Amir Mostaed, *McMullen's Curve, the Weil Locus, and the Hodge Conjecture for Abelian Sixfolds*, arXiv:2603.20268.
- Steven Zucker, *The Hodge conjecture for cubic fourfolds*, Compositio Mathematica 34 (1977), 199-209.

## Claim boundary

The source refresh rejects stale candidate targets and exposes an exact open algebraicity-transport obstruction. It does not establish a new known case, novelty, priority, or any claim beyond the literature-derived boundaries recorded in the executable ledger.
