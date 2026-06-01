# WP03: Union-Closed Sets Source Audit and Known-Bounds Synthesis

## 1. Lay executive companion

Frankl's conjecture remains open. Recent work has produced dimension-free lower
bounds and several structural or restricted results, but none reaches the
conjectured half-frequency threshold in general. This package maps those routes
before the programme selects an original restricted target.

## 2. Certification boundary

This is a literature audit, not a proof package. Each entry below is
`LITERATURE_DERIVED`. Numerical and conditional improvements remain qualified
exactly as stated by their sources.

## 3. Primary-source map

| Claim ID | Source | Classification | Programme use |
|---|---|---|---|
| UC-WP03-C001 | [Gilmer, 2022](https://arxiv.org/abs/2211.09055) | Theorem: first constant `0.01` lower bound via an information-theoretic method. | Starting point for the constant-bound line. |
| UC-WP03-C002 | [Sawin, 2022](https://arxiv.org/abs/2211.11504) | Theorem: improvement to `(3 - sqrt(5)) / 2`; source also sketches a strictly stronger route. | Separate proved threshold from sketched extension. |
| UC-WP03-C003 | [Yu, 2022](https://arxiv.org/abs/2212.00658) | Optimization formulation and numerical evaluation around `0.38234`. | Record numerical status conservatively. |
| UC-WP03-C004 | [Liu, 2023](https://arxiv.org/abs/2306.08824) | Conditionally IID coupling; approximate `0.38271` improvement under numerically verified hypotheses. | Do not promote beyond the stated hypotheses. |
| UC-WP03-C005 | [Bouchard, 2025](https://arxiv.org/abs/2503.00277) | Structural result: necessary conditions for a minimum-size lattice counterexample. | Candidate source for a lattice restricted-target corridor. |
| UC-WP03-C006 | [Hachimori and Kashiwabara, 2025](https://arxiv.org/abs/2504.13454) | Restricted formalized result: ideal families satisfy average rarity; Lean 4 proof reported. | Evaluate representation reuse before duplicating formalization. |
| UC-WP03-C007 | [Hachimori and Kashiwabara, 2025](https://arxiv.org/abs/2511.19833) | Restricted formalized result: functional-preorder order ideals are average-rare; Lean 4 proof reported. | Candidate extension branch after ideal-family comparison. |

## 4. Next analytic target

The public artifact for the ideal-family paper is
[`kashiwabarakenji/frankl_lean`](https://github.com/kashiwabarakenji/frankl_lean).
Its README reports a complete Lean 4.24 formalization of average rarity for
ideal families, organized around deletion, trace, contraction, incidence
double-counting, and normalized degree sum.

This workspace should not duplicate that development. The external project uses
a predicate-based family over a ground finset, while MATHCERT currently uses an
explicit `Finset (Finset α)`. If the ideal-family branch becomes active, first
build a small translation layer and replay the external project separately
against its pinned toolchain.

The selected first original corridor is WP05: reconstruct Bouchard's
lattice-minimal-counterexample conditions and choose one condition for a
Lean-ready restricted theorem statement.
