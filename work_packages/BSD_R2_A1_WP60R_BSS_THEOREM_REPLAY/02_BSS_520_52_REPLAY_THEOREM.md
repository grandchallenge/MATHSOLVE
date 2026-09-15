# WP60R theorem II — selected finite-level replay of BSS II Theorems 5.20 and 5.2 at literal p=2

## 1. Scope

Fix `m>=1` and the selected finite coefficient datum

`R:=Z/2^m`, `A:=E[2^m]`

with the exact BSS level-`m` auxiliary-prime set.

This theorem replays the proof of Burns–Sakamoto–Sano II, arXiv:1805.08448v1, §5.4, after replacing every small-prime-sensitive use by a protected literal-`2` interface.

It does not assert that the original published Hypothesis 3.2(iii) becomes true. For `m>=2` that statement remains false by protected WP60K/WP60M.

## 2. Dependency ledger

### 2.1 Hypotheses 3.2 and 3.3

At residual level, protected WP60J supplies the selected representation-theoretic hypotheses and residual restriction injectivity.

At higher finite levels, the only use of full Hypothesis 3.2(iii) in the relevant proof chain is to retain linear information after restriction to the BSS auxiliary field. Protected WP60M and WP60R Theorem I replace that use on the exact finite spans of modified-Selmer classes that actually enter the proof.

Hypothesis 3.3 local rank-one/transverse structure is retained on the selected BSS auxiliary-prime sets.

### 2.2 Lemma 3.9

The published `s+t<p` counting theorem is not imported unchanged.

Its uses split into three types:

1. **one-class localization:** valid at literal `2` after WP60M Selmer-restricted restriction injectivity;
2. **one-primal/one-dual localization:** replaced by WP60G and WP60R `LEVELM-PAIRWISE-002`;
3. **multi-class family in Theorem 5.20:** replaced by WP60R `INJECTIVE-FAMILY-003`.

The forbidden `2s<p` minimal-core call in the published connectivity proof is replaced entirely by WP60N/WP60Q and WP60R `ALL-LEVEL-CORE-GRAPH-005`.

### 2.3 Lemma 3.10 and Corollary 5.5

Protected WP60M proves the selected all-level replay of BSS Lemma 3.10 for free modified-Selmer submodules.

For Corollary 5.5, the source first enlarges an arbitrary auxiliary ideal to one with zero dual modified Selmer, then compares residual and full exact sequences. WP60R `DUAL-KILL-004` supplies the required enlargement at literal `2`; WP60R `HYP42-006` supplies freeness at the resulting core vertex; WP60M supplies coefficient reduction. Therefore the Corollary 5.5 coefficient-reduction isomorphism replays at every selected finite level.

Record

`BSS_LITERAL_P2_SELECTED_COROLLARY_5_5_REPLAYED`.

### 2.4 Core graph and Lemma 5.19

WP60R `ALL-LEVEL-CORE-GRAPH-005` replaces BSS Theorem 5.18 at the selected finite level.

Lemma 5.19 uses core-vertex freeness, Lemma 3.10 coefficient reduction, a nonzero residual localization, and global duality to prove the finite-singular maps are isomorphisms along a core edge. All of these inputs are now available at literal `2` from MATHFORGE WP60R, WP60M, WP60R Theorem I, and the unchanged duality argument.

Record

`BSS_LITERAL_P2_SELECTED_LEMMA_5_19_REPLAYED`.

## 3. Theorem 5.20 replay

Let `n` be a selected level-`m` core vertex.

### 3.1 Surjectivity

At a core vertex the dual modified Selmer module vanishes. WP60R `HYP42-006` gives the exact freeness conclusion needed in the split global-duality sequence. Hence the finite-singular exterior-bidual map used as equation (7) in BSS is an isomorphism.

The Stark-system theorem and regulator construction then give surjectivity of

`KS_r(A,F) -> bigcap_R^r H^1_{F(n)}(Q,A) tensor G_n`.

No small-prime localization argument occurs in this part.

### 3.2 Injectivity: core-vertex base case

Let `kappa` be a Kolyvagin system with `kappa_n=0`. The BSS induction is on the residual dual dimension `lambda*(a)`.

When `lambda*(a)=0`, `a` is a core vertex. WP60R `ALL-LEVEL-CORE-GRAPH-005` connects `n` to `a`. Along each edge, the replayed Lemma 5.19 makes the finite-singular transition an isomorphism. The Kolyvagin finite-singular relation therefore propagates vanishing from `kappa_n` to `kappa_a`.

### 3.3 Injectivity: positive dual dimension

Suppose `lambda*(a)>0` and, for contradiction, `kappa_a!=0`.

Let

`V:=H^1_{F(a)}(Q,E[2])`

and choose any nonzero

`d in H^1_{F*(a)}(Q,E[2]^*(1))`.

WP60R `INJECTIVE-FAMILY-003` gives distinct auxiliary primes `q_1,...,q_s`, all outside `a`, such that:

- every primal localization `V -> H^1_f(Q_q,E[2])` is nonzero;
- every `q_i` detects `d` on the dual side;
- the combined primal localization is injective.

The replayed Corollary 5.5 lifts the combined residual injection to the full coefficient module. Dualizing the resulting map and using the unchanged exterior-bidual Corollary 2.6 gives a prime `q_i` for which

`phi_fs_{q_i}(kappa_a) != 0`.

Because the residual primal and dual localization maps at `q_i` are both nonzero, the unchanged global-duality dimension calculation in Proposition 5.7 gives

`lambda*(a q_i)=lambda*(a)-1`.

The induction hypothesis gives `kappa_{a q_i}=0`, while the defining finite-singular relation for a Kolyvagin system gives

`0 = v_{q_i}(kappa_{a q_i}) = phi_fs_{q_i}(kappa_a)`,

a contradiction.

Thus every component of `kappa` vanishes. The projection at `n` is injective.

### Theorem `BSD-A1-WP60R-BSS-520-007`

For every selected finite level `R_m=Z/2^m` and every selected core vertex `n`, the BSS projection

`KS_r(A_m,Fcan) -> bigcap^r_{R_m} H^1_{Fcan(n)}(Q,A_m) tensor G_n`

is an isomorphism. In particular the selected finite-level Kolyvagin-system module is free of rank one.

Record

`BSS_LITERAL_P2_SELECTED_THEOREM_5_20_REPLAYED`.

## 4. Lemma 5.22 replay

The source uses Lemma 3.9 twice.

First, to prove that each modified structure `F(n)` also satisfies Hypothesis 4.2, it chooses an auxiliary ideal that kills the dual modified Selmer group. WP60R `DUAL-KILL-004` and `HYP42-006` provide exactly this construction.

Second, for the reverse Fitting-ideal inclusion under

`Ann_R H^1_{F(n)}(Q,A)=0`,

the source chooses an element `e` with zero annihilator, a generator `x` of `R[2]`, and an auxiliary ideal `a` such that:

- `loc_q(xe)!=0` for every new `q|a`;
- the dual modified Selmer group after adding `a` is zero.

This is exactly the constrained form of WP60R `DUAL-KILL-004`: keep the fixed nonzero residual primal class `xe` and kill one residual dual dimension at a time using pairwise localization. The rest of the source proof is global duality plus Lemma 4.4 and is unchanged.

Therefore Lemma 5.22 and Corollary 5.23 replay at literal `2` on every selected finite level.

Record

`BSS_LITERAL_P2_SELECTED_LEMMA_5_22_COROLLARY_5_23_REPLAYED`.

## 5. Theorem 5.2 replay

### 5.1 Claim (i)

The regulator isomorphism and rank-one freeness follow from the unchanged Stark-system theorem, the replayed Theorem 5.20, and equation (7), whose freeness input is supplied by WP60R `HYP42-006`.

### 5.2 Claim (ii)

Fix an auxiliary ideal `n`. The source enlarges `n` to `a` with zero dual modified Selmer and then applies the global-duality exact sequence and exterior-bidual/Fitting calculation.

WP60R `DUAL-KILL-004` constructs such an `a` in the exact level-`m` prime set; `HYP42-006` gives the freeness ranks used in the exact sequence. The exterior-bidual algebra is characteristic-independent. Hence for every selected finite-level Kolyvagin system `kappa`,

`im(kappa_n) subset Fitt^0_R(H^1_{F*(n)}(Q,A^*(1))^*)`,

with equality when `kappa` is a basis.

### 5.3 Claim (iii)

The replayed Lemma 5.22 and Corollary 5.23 give the same higher-Fitting inclusions as in the source.

Since `R_m=Z/2^m` is a principal ideal ring, it remains only to prove the source's annihilator-zero condition. For each `n`, apply WP60R `DUAL-KILL-004` to enlarge `n` to a dual-zero auxiliary ideal. The same rank comparison used by BSS then embeds a free rank-`r` module in `H^1_{F(n)}(Q,A)`. Hence this Selmer module has zero annihilator, and the higher-Fitting inclusions become equalities for a basis Kolyvagin system.

### Theorem `BSD-A1-WP60R-BSS-52-008`

For every selected finite coefficient level `R_m=Z/2^m`, the three conclusions of BSS II Theorem 5.2 hold for the exact selected canonical structure and exact level-`m` auxiliary-prime set, with the published `p>3` and full higher-level Hypothesis 3.2(iii) uses replaced by the protected literal-`2` interfaces recorded in WP60G–WP60R.

Record

`BSS_LITERAL_P2_SELECTED_THEOREM_5_2_REPLAYED`.

## 6. What was and was not repaired

The replay repairs the theorem proof on the selected finite coefficient lane. It does **not** assert the false formal statement

`H^1(K(A_m)_(2^m)/Q,A_m)=0`

for `m>=2`; protected WP60M proves this group has order two. The actual reason the theorem replay works is narrower: that unique defect is excluded from every selected modified primal/dual Selmer class by the fixed local condition, and hence cannot corrupt the exact finite spans used in localization.

The replay also does not repair the protected infinite H3 failure.

## 7. Next exact boundary

BSS Theorem 5.25 passes from the finite-level modules to an inverse limit and is stated in a subsection that imposes additional inverse-limit hypotheses and compatibility across levels. It is therefore not silently promoted here even though its source proof refers back to Theorem 5.2.

Record

`MISSING_LITERAL_P2_BSS_THEOREM_5_25_INVERSE_LIMIT_REPLAY_AFTER_FINITE_LEVEL_REPLACEMENTS`.

## 8. Claim firewall

WP60R does not establish:

- BSS Theorem 5.25 or Corollary 6.15 at literal `2`;
- the protected infinite BSS H3 condition;
- height-one `(2)` Kato/Fitting divisibility;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
