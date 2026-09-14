# BSD-R2-A1 WP60G — self-dual literal-`p=2` pairwise localization

## Purpose

Attack WP60F boundary F1 at its first exact obstruction: the one-primal/one-dual use of BSS Lemma 3.9 when the residue characteristic is `2`.

The package proves a self-dual literal-`2` replacement for that pairwise localization step under BSS Hypothesis 3.2. It then identifies the first remaining unrepaired graph-connectivity step: the `s=2` use of BSS Lemma 5.15 in Corollary 5.16.

This package does **not** prove full BSS core-vertex connectivity, the literal-`2` BSS Fitting theorem, or the selected BSD target.

## Protected inputs

- MATHSOLVE base: `813156baf3fa57989ddce891f355e2648e99c008`.
- MATHFORGE WP60F: `eaaf7b8c660f3f07030608b3af1334ece5598586`.
- MATHFORGE WP60G affine-fiber interface: `7da6813fcde7eb5f9badd7c86946f58691ed6f0d`.
- Programme tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Main results

### G1 — two affine index-two fibers

For a group `G`, nonzero characters

`chi_1,chi_2:G->F_2`

and constants `a_1,a_2 in F_2`, the two affine fibers

`chi_1^{-1}(a_1)` and `chi_2^{-1}(a_2)`

cover `G` if and only if

`chi_1=chi_2` and `a_1 != a_2`.

Thus two distinct nonzero characters can never produce a covering pair.

### G2 — self-dual BSS pairwise replacement

Let `A` be an `F_2[G_K]`-module satisfying BSS Hypothesis 3.2 and suppose there is a `G_K`-equivariant isomorphism

`iota:A -> A^*(1)`.

Then for every nonzero

`c in H^1(K,A)` and `c^* in H^1(K,A^*(1))`,

the two BSS bad fibers attached to `c` and `c^*` do not cover `G_{K(A)_2}`. Hence the BSS Chebotarev construction produces a positive-density set of primes where both localizations are nonzero.

### G3 — selected elliptic residual self-duality

For an elliptic curve `E/Q`, the Weil pairing gives a `G_Q`-equivariant perfect pairing

`E[2] x E[2] -> mu_2`,

hence a canonical isomorphism

`E[2] ~= E[2]^*(1)`.

Therefore the self-duality condition in G2 is automatic for the selected residual elliptic representation.

Application still requires the BSS Hypothesis 3.2 input; WP60F boundary F2 remains unresolved and may be needed to verify the relevant hypotheses uniformly in the selected lane.

## Exact progress on F1

The published `s+t<p` count is no longer the obstruction for one primal plus one dual class in the self-dual residual elliptic case.

This repairs the pairwise use of Lemma 3.9, including the localization pattern used in BSS Lemma 5.14 and the pairwise step appearing in Lemma 5.17, whenever the remaining BSS hypotheses are available.

It does not repair BSS Lemma 5.15 with `s=2`, which requires one prime to satisfy two primal and two dual nonvanishing constraints simultaneously and is used in Corollary 5.16 to connect two minimal core vertices.

Record the refined live graph boundary

`MISSING_P2_TWO_CORE_VERTEX_SIMULTANEOUS_LOCALIZATION_OR_REPLACEMENT_CONNECTIVITY`.

## Highest-value successor

Analyze the `s=2` four-fiber problem and Corollary 5.16 itself. Do not assume that the four affine index-two fibers fail to cover. Either:

1. derive structural relations among the four BSS characters/affine constants that rule out covering in the selected self-dual lane; or
2. replace the common-prime construction of Corollary 5.16 by a different minimal-core-vertex connectivity proof.

If neither is possible, protect an explicit obstruction and retire only this BSS connectivity subroute.

## Claim firewall

Do not infer:

- full BSS graph connectivity at `p=2`;
- BSS Theorem 5.20 or Theorem 5.2 at `p=2`;
- F1 or F2 fully resolved;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
