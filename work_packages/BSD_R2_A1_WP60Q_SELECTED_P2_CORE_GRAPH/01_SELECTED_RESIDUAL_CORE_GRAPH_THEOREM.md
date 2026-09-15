# WP60Q theorem — selected literal-p=2 residual core graph is connected

## 1. Selected residual setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class and put

`A:=E[2]`.

Let `Fcan` denote the exact Mazur–Rubin/Burns–Sakamoto–Sano canonical Selmer structure propagated to `A`.

Protected MATHSOLVE WP60N proves full residual core-graph connectivity at characteristic two under five hypotheses:

1. residual self-duality;
2. the relevant residual BSS restriction-injectivity interface;
3. cartesianness;
4. core rank one;
5. residual coisotropy.

We verify these hypotheses from protected selected-lane interfaces and then apply WP60N.

## 2. Residual self-duality and restriction injectivity

The Weil pairing identifies

`E[2] ~= E[2]^*(1)`.

Protected MATHSOLVE WP60J proves, for every selected curve, BSS II Hypotheses 3.2 and 3.3 at the residual specialization `A=E[2]`. In particular,

`H^1(Q(E[2])Q(i)/Q,E[2])=0`

and the same vanishing holds for the Tate dual. This is exactly the residual restriction-injectivity input used by the protected WP60G/WP60H/WP60N localization interfaces.

Thus hypotheses 1 and 2 of WP60N hold for the selected canonical residual lane.

## 3. Cartesian and core-rank-one hypotheses

Protected MATHFORGE WP60P at

`280646bf69cba8fbb77ba47eb97dda0fb495baa6`

admits the Mazur–Rubin source interfaces showing that the exact canonical structure on `T_2(E)` is cartesian on all finite quotients and that

`chi(T_2(E),Fcan)=1`.

The same core rank is carried by the residual quotient `E[2]`.

Hence the selected residual canonical structure is cartesian and has core rank one.

Thus hypotheses 3 and 4 of WP60N hold.

## 4. Residual coisotropy

Protected MATHFORGE WP60O, retained in the protected provider history ending at

`280646bf69cba8fbb77ba47eb97dda0fb495baa6`,

proves place by place that the exact canonical residual local condition `L_v` contains the ordinary mod-2 Kummer image `K_v` and that `K_v` is self-annihilating under local Tate duality. Therefore

`L_v^perp subset K_v^perp=K_v subset L_v`

for every place `v`.

Under the fixed Weil self-duality this is precisely

`Fcan* subset Fcan`.

Thus hypothesis 5 of WP60N holds.

## 5. Selected residual core-graph connectivity

### Theorem `BSD-A1-WP60Q-SELECTED-CORE-GRAPH-001`

For every selected `BSD-R2-A1` curve, the residual BSS core graph attached to the exact canonical structure on `E[2]` is connected at literal `p=2`.

### Proof

Sections 2–4 verify every hypothesis of protected MATHSOLVE Theorem `BSD-A1-WP60N-CORE-GRAPH-CONNECTIVITY-004` for the selected canonical residual structure. Apply that theorem. QED.

Record

`BSS_LITERAL_P2_SELECTED_RESIDUAL_CORE_GRAPH_CONNECTED`.

The earlier applicability boundary

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`

is therefore retired.

## 6. Compatibility with the protected higher-level obstructions

This result does not contradict either of the following protected facts.

1. WP60K proves unchanged formal finite BSS Hypothesis 3.2(iii) fails already at `E[4]`.
2. WP60I proves the standard infinite BSS III H3 condition fails.

WP60Q applies the residual `E[2]` theorem. At higher finite levels, protected WP60L/WP60M prove that the nonzero formal cohomological defect is excluded from every actual canonical modified primal and dual Selmer group, yielding the Selmer-restricted restriction-injectivity/coefficient-reduction interface. Full formal higher-level cohomology vanishing is not asserted.

## 7. Exact next proof-dependency

The residual graph-connectivity layer of the published `p>3` Kolyvagin-system/Fitting-control mechanism has now been replaced on the selected literal-`2` lane.

It does not follow merely from this fact that BSS II Theorem 5.20 or Theorem 5.2 holds at `p=2`. The next bounded obligation is an exact proof replay of those theorems using:

- WP60Q for selected residual core-graph connectivity;
- WP60G for pairwise residual localization;
- WP60M for all-level Selmer-restricted restriction injectivity and coefficient reduction;
- the protected BSS transition/control interfaces already admitted by MATHFORGE.

Every remaining direct use of `p>3`, full Hypothesis 3.2(iii), or an unrepaired localization lemma must be isolated before any theorem-level Fitting claim can be promoted.

Record

`MISSING_LITERAL_P2_BSS_THEOREM_5_20_5_2_REPLAY_AFTER_REPLACEMENTS`.

## 8. Claim firewall

WP60Q does not establish:

- BSS II Theorem 5.20, Theorem 5.2, Theorem 5.25, or Corollary 6.15 at literal `p=2`;
- formal higher-level BSS Hypothesis 3.2(iii);
- infinite BSS III H3;
- Kato/Fitting divisibility at the height-one prime `(2)`;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
