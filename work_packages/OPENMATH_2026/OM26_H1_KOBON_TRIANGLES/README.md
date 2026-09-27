# OM26-H1 — Kobon triangles

**Campaign:** `OPENMATH-2026`  
**Hill:** `alejandrozu/kobon-triangles`  
**Forge lock:** `grandchallenge/MATHFORGE@73f1890387eec56eb6be31f8c00f10b6a5a56383`  
**State:** `ACTIVE__SOURCE_LOCK_BOUND`  
**Primary sprint setting:** `n=18`

## Objective

Produce actual rational straight-line arrangements with a higher exact evaluator-verified number of bounded triangular faces than the displayed 18-line baseline score of 16.

The campaign does not need an optimality proof to make progress. A higher verified construction is a useful result. An optimality claim is a different object and requires a separate upper-bound route and certification.

## Non-negotiable semantics

- exactly `n` distinct straight lines;
- submitted as integer triples `[a,b,c]` for `a*x+b*y+c=0`;
- proportional triples are duplicates and invalid;
- bounded nonzero-area triangular faces only;
- a triangle crossed or subdivided in its interior does not count;
- shared vertices, parallel lines, and three-or-more-line concurrence are allowed;
- all evaluator geometry is exact rational arithmetic;
- scores are compared only at the same `n`.

## Operating sequence

1. reproduce the displayed baseline under an independent exact scorer;
2. cross-check that result with the AutoLab local evaluator;
3. prove or falsify the internal face-count criterion used by the scorer;
4. build small-`n` reconnaissance and route diagnostics;
5. run diversified construction search at `n=18`;
6. independently replay every candidate score before promotion;
7. preserve a monotone campaign-best ladder without calling it literature-best;
8. perform a live hill concordance check immediately before any final submission;
9. route claim-bearing outputs through MATHCERT independently of AutoLab acceptance.

## Core clarity

The object is not a picture and not a pseudoline combinatorics score. It is a concrete list of rational straight lines. Search may use continuous or combinatorial surrogates, but every surviving candidate must return to that exact object.
