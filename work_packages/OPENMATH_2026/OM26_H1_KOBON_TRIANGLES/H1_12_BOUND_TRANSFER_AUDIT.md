# H1-12 — 94-bound transfer audit

**State:** `OPEN__DIRECT_IMPORT_REJECTED`

## Question

Does the published 94 upper bound at `n=18` apply directly to the AutoLab hill, whose rules allow parallel lines and intersections of three or more lines?

## Source audit

The Bartholdi–Blanc–Loisel Theorem 1.1 bound is proved for **simple affine arrangements of pseudo-lines**. In that paper an affine arrangement requires every pair of pseudo-lines to intersect exactly once, and `simple` excludes multiple intersections. The proof counts used and unused segments under those hypotheses.

The AutoLab hill is broader: it explicitly permits parallel lines and intersections of three or more lines. Therefore the simple-arrangement theorem cannot be imported directly as a hill-global upper-bound proof.

Current public status sources report `n=18 >= 93, upper bound 94`, but that status report is not itself a proof object for the broader hill semantics. A 2026 source also explicitly distinguishes the classical maximum, where several lines may pass through a point, from the simple-arrangement maximum.

## Disposition

`94` remains a **literature-reported upper bound / research target**, not a GCL-certified hill-global theorem.

To close H1-12, one of the following is sufficient:

1. source and reconstruct a proof whose hypotheses match the hill's allowed degeneracies; or
2. prove a reduction showing that any hill-admissible `n=18` arrangement with `T` counted triangular faces can be transformed into an arrangement satisfying the simple theorem's hypotheses without decreasing `T`.

Failure of a construction search to find 94 is not evidence for the upper bound.

## Immediate search implication

The protected 93 reconstruction leaves only one point to the literature-reported 94 target. H1-13 therefore performs a bounded exact local-wall search around the 93 arrangement while H1-12 remains logically independent.

## Public references

- Bartholdi, Blanc, Loisel, arXiv:0706.0723v1, especially Introduction and Theorem 1.1 proof.
- OEIS A006066 current status entry for `n=18`.
- Liang, Liu, Zhang (2026), terminology distinguishing classical `K(n)` from simple `Kcell(n)`.

**Claim boundary:** this audit rejects an unjustified direct theorem import. It does not assert that 94 is false, true, optimal, or attainable under the hill semantics.
