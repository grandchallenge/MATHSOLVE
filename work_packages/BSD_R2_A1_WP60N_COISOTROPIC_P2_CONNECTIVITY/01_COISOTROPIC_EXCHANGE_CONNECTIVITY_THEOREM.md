# WP60N theorem — characteristic-two coisotropic core-vertex exchange connectivity

## 1. Protected setup

Work over the residual field `k=F_2` in the protected BSS core-rank-one setting.

Assume:

1. the residual coefficient module is self-dual;
2. the relevant BSS residual restriction-injectivity interface is available;
3. the Selmer structure `F` is cartesian;
4. its core rank is `chi(F)=1`;
5. after the fixed residual self-duality, `F` is residually coisotropic:
   `F* subset F` place by place.

Protected MATHSOLVE WP60G supplies simultaneous localization for every one-primal/one-dual pair at literal `p=2`. Protected WP60H supplies the exact odd-relation criterion for four self-dually identified residual classes. Protected MATHFORGE WP60H supplies the BSS minimal-core transition data. Protected MATHFORGE WP60N at

`39cda156c4ce16ec97cc80f415efa3b8a8716cea`

admits the coisotropic plane decomposition and confirms that the post-minimal arbitrary-core reduction uses only pairwise localization.

This theorem proves connectivity under these hypotheses. It does not prove that the selected elliptic canonical structure is coisotropic.

## 2. Minimal-core notation

Let `n_1,n_2` be minimal core vertices. Thus

`nu(n_i)=lambda*(1)`,

`lambda(n_i)=1`,

`lambda*(n_i)=0`.

Choose distinct primes

`q_i | n_i`

outside `gcd(n_1,n_2)` and put

`m_i:=n_i/q_i`.

Minimality gives

`lambda(m_i)=2`,

`lambda*(m_i)=1`.

Choose nonzero generators

`p_i in H^1_{F(n_i)}`

and

`d_i in H^1_{F*(m_i)}`.

Under the fixed residual self-duality, regard all four as classes in the same global cohomology vector space.

By protected residual coisotropy and the protected MATHFORGE WP60N decomposition,

`H^1_{F(m_i)}
 = <p_i> direct_sum <d_i>`.

Write

`U_i:=H^1_{F(m_i)}=<p_i,d_i>`.

All vector spaces in the relation arguments below are over `F_2`.

## 3. Strict-place separation lemma

### Lemma `BSD-A1-WP60N-STRICT-SEPARATION-001`

For `i != j`, if

`d_j in U_i`,

then

`d_j=d_i`.

Consequently neither relation

`p_1+d_1+d_2=0`

nor

`p_2+d_1+d_2=0`

can occur.

### Proof

Residual coisotropy together with `chi(F)=1` implies that the strict-place set

`E(F):={v : H^1_{F*}(K_v) != H^1_F(K_v)}`

is nonempty. Indeed, if it were empty, the identified residual local conditions `F` and `F*` would agree everywhere and hence the identified global primal and dual Selmer spaces would agree, contradicting core-rank one.

Fix `v in E(F)`.

Suppose `d_j in U_i`. Since `U_i=<p_i,d_i>`, write

`d_j=a p_i+b d_i`,

with `a,b in F_2`.

Both `d_i` and `d_j` satisfy the dual local condition at `v`, because `v` is a base Selmer place and the auxiliary modifications defining `m_i,m_j` occur away from `S(F)`. Hence

`loc_v(d_i), loc_v(d_j) in H^1_{F*}(K_v)`.

Since `n_i` is core,

`H^1_{F*(n_i)}=0`.

Thus the nonzero class `p_i` belongs to

`H^1_{F(n_i)} \ H^1_{F*(n_i)}`.

The protected coisotropic strict-place localization interface, corresponding to Sakamoto Lemma 3.11, gives

`loc_v(p_i) notin H^1_{F*}(K_v)`.

Reducing

`loc_v(d_j)=a loc_v(p_i)+b loc_v(d_i)`

modulo the dual local subspace forces `a=0`. Since `d_j` is nonzero, `b=1`. Hence `d_j=d_i`.

If `p_1+d_1+d_2=0`, then `d_2=p_1+d_1 in U_1`, so the first part gives `d_2=d_1`, forcing `p_1=0`, contradiction. The second displayed relation is symmetric. QED.

## 4. Direct four-class case

Protected WP60H proves that four nonzero residual BSS bad fibers fail to admit a common good element exactly when some three of their source classes sum to zero.

Applied to

`p_1,d_1,p_2,d_2`,

Lemma `BSD-A1-WP60N-STRICT-SEPARATION-001` removes the two relations containing one primal and both dual classes.

Therefore the only possible obstructions are

`p_1+p_2+d_1=0`

or

`p_1+p_2+d_2=0`.

If neither occurs, protected WP60H gives a positive-density set of auxiliary primes `r` at which all four required localizations are nonzero. Protected MATHFORGE WP60H then replays the original BSS minimal-core transition and produces core vertices

`n_1 r/q_1`, `n_2 r/q_2`

path-connected to `n_1,n_2`, respectively.

Because `q_1,q_2` were chosen outside the original gcd and `r` is new,

`nu(gcd(n_1 r/q_1,n_2 r/q_2))
 = nu(gcd(n_1,n_2))+1`.

This is exactly the usual minimal-core induction step.

## 5. Exchange lemma for the first hard relation

### Lemma `BSD-A1-WP60N-EXCHANGE-002`

Assume

`p_1+p_2+d_1=0`.

Then there is a minimal core vertex

`n_1' = n_1 s/q_1`

path-connected to `n_1`, for some new auxiliary prime `s`, such that

`H^1_{F(n_1')}=<p_2>`.

Moreover, the pair `n_1',n_2` admits an unobstructed WP60H four-class common-prime step using the removed primes `s` and `q_2`.

### Proof

Protected WP60G supplies a positive-density set of auxiliary primes `s`, avoiding any prescribed finite set, such that

`loc_s(p_1) != 0`,

`loc_s(d_1) != 0`.

Choose `s` outside `n_1 n_2`.

At an auxiliary BSS prime, the relevant residual finite local target is one-dimensional over `F_2`. Hence the two nonzero localizations are equal. From

`p_2=p_1+d_1`

we obtain

`loc_s(p_2)=0`.

The protected BSS transition interface now gives:

1. because `n_1` is core and `loc_s(p_1)!=0`, the corresponding primal transition is core;
2. because `lambda*(m_1)=1` and `loc_s(d_1)!=0`, the dual dimension drops and `m_1 s` is core;
3. protected pairwise path machinery connects `n_1` to
   `m_1 s=n_1 s/q_1`.

Set

`n_1':=m_1 s`.

It has the same number of prime factors as `n_1`, hence is again minimal.

The relation `p_2=p_1+d_1` and the plane decomposition show

`p_2 in H^1_{F(m_1)}`.

At the new prime `s`, `loc_s(p_2)=0`, and zero satisfies the transverse local condition. Therefore

`p_2 in H^1_{F(m_1 s)}=H^1_{F(n_1')}`.

Since `n_1'` is a core vertex of core rank one, its primal residual Selmer space is one-dimensional. Thus

`H^1_{F(n_1')}=<p_2>`.

Now compare `n_1'` and `n_2`. Remove `s` from `n_1'`; this recovers `m_1`, so the associated dual generator remains `d_1`. Remove `q_2` from `n_2`; the associated dual generator is `d_2`.

The four source classes for the WP60H criterion are therefore

`p_2,d_1,p_2,d_2`.

Any odd three-term relation among these four either reduces to `d_1=0`, to `d_2=0`, or to

`p_2+d_1+d_2=0`.

The first two are impossible by construction. The third is excluded by Lemma `BSD-A1-WP60N-STRICT-SEPARATION-001`, applied to the minimal core pair `n_1',n_2`.

Hence no odd relation exists. Protected WP60H therefore supplies a common auxiliary prime for this aligned pair. QED.

### Symmetric exchange

If instead

`p_1+p_2+d_2=0`,

the same argument exchanges `q_2`, producing a minimal core

`n_2'=n_2 s/q_2`

path-connected to `n_2` with

`H^1_{F(n_2')}=<p_1>`,

after which the aligned four-class problem is unobstructed.

## 6. Minimal-core connectivity

### Theorem `BSD-A1-WP60N-MINIMAL-CORE-CONNECTIVITY-003`

Under the hypotheses of §1, all minimal core vertices lie in one connected component of the residual core graph.

### Proof

Induct on

`lambda*(1)-nu(gcd(n_1,n_2))`.

If the quantity is zero, the two square-free minimal vertices have the same number of prime factors and their gcd has that full cardinality, so `n_1=n_2`.

Assume the quantity is positive. Choose

`q_1 | n_1/gcd(n_1,n_2)`,

`q_2 | n_2/gcd(n_1,n_2)`.

Then `q_1 != q_2`.

Form the four classes `p_1,d_1,p_2,d_2` as above.

- If there is no odd three-term relation, §4 gives a new pair of minimal cores, each path-connected to the original corresponding vertex, whose gcd has one more prime factor.
- If `p_1+p_2+d_1=0`, Lemma `BSD-A1-WP60N-EXCHANGE-002` first replaces `n_1` by a path-connected minimal core with primal line `<p_2>`. The aligned pair then admits an unobstructed common-prime step. Removing the exchange prime and `q_2` and adding the new common prime produces vertices of the form
  `n_1 t/q_1` and `n_2 t/q_2`; their gcd again has one more prime factor than the original gcd.
- If `p_1+p_2+d_2=0`, use the symmetric exchange.
- The remaining two three-term relations are impossible by Lemma `BSD-A1-WP60N-STRICT-SEPARATION-001`.

In every case we obtain paths from the original vertices to a new minimal pair with strictly smaller induction parameter. Apply the induction hypothesis and concatenate paths. QED.

## 7. Full residual core-graph connectivity

### Theorem `BSD-A1-WP60N-CORE-GRAPH-CONNECTIVITY-004`

Under the hypotheses of §1, the full residual BSS core graph is connected at characteristic two.

### Proof

Theorem `BSD-A1-WP60N-MINIMAL-CORE-CONNECTIVITY-003` connects all minimal cores.

Protected MATHFORGE WP60N establishes that the BSS reduction from an arbitrary core vertex to a core vertex with fewer auxiliary prime factors uses only one-primal/one-dual simultaneous localization. Protected MATHSOLVE WP60G supplies exactly that pairwise localization step at literal `p=2` under the present residual self-dual BSS hypotheses.

Hence every core vertex is path-connected to a minimal core vertex. Since all minimal cores are mutually connected, the whole core graph is connected. QED.

Record

`P2_BSS_COISOTROPIC_CORE_GRAPH_CONNECTED`.

## 8. Consequence for the protected F1 boundary

Protected WP60H left

`MISSING_P2_BSS_MINIMAL_CORE_THREE_TERM_RELATION_EXCLUSION_OR_REPLACEMENT_CONNECTIVITY`.

WP60N resolves that obstruction under residual coisotropy. Together with the protected pairwise arbitrary-core reduction, the residual connectivity mechanism itself is no longer blocked by characteristic two on the coisotropic sublane.

Uniform selected-lane application still requires either:

1. a proof that the selected literal-`2` canonical residual Selmer structure is residually coisotropic; or
2. a connectivity argument that does not assume coisotropy.

Record the remaining applicability boundary

`MISSING_SELECTED_P2_RESIDUAL_CANONICAL_COISOTROPY_OR_NONCOISOTROPIC_CONNECTIVITY`.

## 9. Claim firewall

This theorem does not establish:

- residual coisotropy for every selected `BSD-R2-A1` curve;
- full formal BSS Hypothesis 3.2(iii), which remains false at finite levels as a global cohomology statement;
- repair of the protected infinite BSS H3 failure;
- a literal-`p=2` import of Sakamoto's `F_3` localization lemmas;
- BSS Theorem 5.20, Theorem 5.25, or integral Fitting control for the selected class without the remaining applicability and downstream hypotheses;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
