# WP03: Union-Closed Sets Source Audit and Known-Bounds Synthesis

Source audit refreshed: **2026-06-14**.

## 1. Executive conclusion

Frankl's conjecture remains open. The general lower-bound line currently gives
dimension-free constants near `0.382`, not the conjectured `1/2`. The strongest
numbers in this package are not all at the same certification level: Gilmer's
and Sawin's constants are theorem statements, Yu's value is a numerical
evaluation of a finite optimization, and Liu separates an analytic strict
improvement from a larger value that depends on numerically tested structural
hypotheses.

The structural branch now has two useful formalization signals. Bouchard gives
necessary conditions for a minimum-size lattice counterexample. Hachimori and
Kashiwabara provide external Lean developments for average rarity in ideal
families and functional-preorder order ideals. Ho's 2026 Lean development
formalizes a generalized entropy inequality for approximate `k`-union closure,
but does not prove Frankl's conjecture.

## 2. Common entropy pipeline

Let `X` and `Y` be samples supported on a union-closed family, and write `X ∨ Y`
for coordinatewise union.

1. Union closure keeps `X ∨ Y` inside the family.
2. If `X` is uniform, then `H(X ∨ Y) <= H(X)` because the uniform distribution
   maximizes entropy on that finite support.
3. Assume every coordinate has marginal at most `t`.
4. Prove, for a selected coupling of `X` and `Y`, that the coordinatewise
   entropy inequalities force `H(X ∨ Y) > H(X)`.
5. The contradiction shows that some coordinate has frequency greater than
   `t`.

The papers differ mainly in the coupling class and the sharpness or
certifiability of the scalar optimization used in step 4.

## 3. Constant-bound line

| Claim ID | Primary source | Source-grade statement | Certification boundary |
|---|---|---|---|
| `UC-WP03-C001` | [Gilmer, 2022](https://arxiv.org/abs/2211.09055) | Theorem: every nontrivial union-closed family has an element in at least a `0.01` fraction of its members. | Literature-derived theorem; not re-proved locally. |
| `UC-WP03-C002` | [Sawin, 2022](https://arxiv.org/abs/2211.11504) | Theorem: improve the constant to `(3 - sqrt(5)) / 2`. A further strict improvement is sketched separately. | The displayed constant is theorem-grade; the sketched extension is not promoted here. |
| `UC-WP03-C003` | [Yu, 2022](https://arxiv.org/abs/2212.00658) | A coupling optimization is reduced to a computable finite problem and evaluated at about `0.38234`. | The optimization theorem is source-grade; the decimal remains numerical until independently replayed with a certificate. |
| `UC-WP03-C004` | [Liu, 2023](https://arxiv.org/abs/2306.08824) | Theorem 6 gives an analytic strict improvement over the preceding constant. A separate computation suggests about `0.382709` under additional structural assumptions on a nine-dimensional optimizer. | Preserve the distinction between the unconditional strict improvement and the conditional numerical value. |

## 4. Structural and formalized branches

| Claim ID | Primary source | Classification | Programme decision |
|---|---|---|---|
| `UC-WP03-C005` | [Bouchard, 2025](https://arxiv.org/abs/2503.00277) | Structural theorem package: necessary conditions for a minimum-size counterexample in the finite-lattice formulation. | Selected for the WP05 theorem spine. |
| `UC-WP03-C006` | [Hachimori and Kashiwabara, 2025](https://arxiv.org/abs/2504.13454) | Restricted theorem with reported Lean 4 proof: ideal families are average-rare. | Reuse or translate the external development; do not duplicate it blindly. |
| `UC-WP03-C007` | [Hachimori and Kashiwabara, 2025](https://arxiv.org/abs/2511.19833) | Restricted theorem with reported Lean 4 proof: order ideals of functional preorders are average-rare. | Keep as a later extension branch. |
| `UC-WP03-C008` | [Ho, 2026](https://arxiv.org/abs/2601.19327) | Theorem with reported Lean 4 proof: a generalized Boppana entropy inequality for real `k > 1`, implying a result for approximate `k`-union-closed systems. | Useful analytic/formalization reference, not a stronger theorem for ordinary Frankl. |

## 5. Formalization feasibility

| Route | Local prerequisites | Risk | Decision |
|---|---|---|---|
| Gilmer/Sawin entropy proof | Finite probability, Shannon entropy, conditional entropy, chain rule, scalar entropy inequalities | High library and analytic overhead | Documented, not the next Lean target. |
| Yu/Liu numerical constants | Exact optimization specification plus interval or proof-producing global optimization | High certification overhead | No promotion until a replayable certificate exists. |
| Ideal-family average rarity | Translation between predicate families over a ground finset and `Finset (Finset α)` | Moderate, but an external Lean proof exists | Defer duplication; audit and translate only if activated. |
| Bouchard minimum counterexample | Finite lattice, covers, `SupIrred`/`InfIrred`, upper-cone cardinality, deletion lemmas | Moderate and theorem-decomposable | Selected WP05 corridor. |
| Ho generalized inequality | Real analysis and binary entropy; external Lean code is available | Moderate, but peripheral to the ordinary conjecture | Track as reusable external formalization. |

## 6. Reuse decision

The ideal-family artifact is
[`kashiwabarakenji/frankl_lean`](https://github.com/kashiwabarakenji/frankl_lean).
It uses a predicate-based family over a ground finset, whereas MATHCERT exposes
`Family α := Finset (Finset α)`. If this branch is activated, the first task is a
small translation layer and an independent build of the external pinned
toolchain.

WP03 is complete as a source audit. WP05 now owns the exact lattice theorem
spine and target selection.
