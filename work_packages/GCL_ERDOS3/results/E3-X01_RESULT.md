GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-X01-IA-001
assignment: E3-X01
agent_ref: INDEPENDENT-AGENT-E3-X01-001
disposition: SMALLEST_MISSING_LEMMA
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Let
[
a_n:=rac{r_4(2^n)}{2^n}.
]
The following candidate cross-scale upgrades are impossible:

1. **Fixed-step uniform contraction.** There do not exist fixed (Lge 1), (delta>0), and (n_0) such that
[
a_{n+L}le (1-delta)a_nqquad(nge n_0).
]

2. **Fixed-window averaged uniform contraction.** There do not exist fixed (Lge1), (delta>0), and (n_0) such that
[
rac1Lsum_{j=1}^{L}a_{n+j}le(1-delta)a_nqquad(nge n_0).
]

3. **Constant-factor quasi-submultiplicativity.** There do not exist fixed (C_0<infty) and (n_0) such that
[
a_{n+m}le C_0,a_n a_mqquad(n,mge n_0).
]

These failures follow from the Behrend lower-bound construction, because (r_4(N)ge r_3(N)) and therefore, for some absolute (C>0) and all sufficiently large (n),
[
a_nge exp(-Csqrt n).
]

A sufficient cross-scale inequality that survives this obstruction is the following density-dependent loss:

> **Missing renormalization lemma.** There exist fixed (Lge1), (c>0), (n_0), and (0<	heta<1) such that
> [
> a_{n+L}le a_nigl(1-c,a_n^	hetaigr)
> qquad(nge n_0).
> ]

If this lemma holds, then
[
a_n=O(n^{-1/	heta})
]
and hence
[
sum_{nge1}a_n<infty.
]

No such inequality is proved here. The exact advance is therefore a theorem-grade exclusion of broad naive renormalization families together with a quantitatively sufficient smallest missing density-loss lemma.

## Derivation / evidence

### 1. Protected identities and starting point

The immutable task was read at commit
`bf9bc7f448f92d71afeae937fda133b0e1d4de80`.

Verified blob identities:

- `E3-X01.md`: `7d8a282a19768286b47ad13590838fbe8a0c152c`;
- `E3-B02_RESULT.md`: `0c6a3192294f9017a2e6bb18fa1cd4063d78a818`;
- `E3-S02_RESULT.md`: `bf52757797483b09b29292a326f0cecd3779ca9b`;
- `FRONTIER.json`: `464574eb705c841e332035f35a4b44b83d57c296`.

From the protected packet, (a_n) is nonincreasing and the known Green–Tao pointwise estimate gives (a_nll n^{-c_*}) for some absolute (c_*>0), but does not provide a summable exponent.

### 2. Reblocking gives only monotonicity

Partition ([1,2^{n+L}]) into (2^L) consecutive intervals of length (2^n). Any 4-AP-free set restricts on each interval to a 4-AP-free set after translation. Hence
[
r_4(2^{n+L})le 2^L r_4(2^n),
]
so
[
a_{n+L}le a_n.
]
Thus interval localization/reblocking alone has no density-loss factor and cannot improve the logarithmic exponent.

### 3. Behrend lower bound transfers from (r_3) to (r_4)

Every 3-AP-free set is automatically 4-AP-free, because a nontrivial 4-term arithmetic progression contains a nontrivial 3-term arithmetic progression among its first three terms. Therefore
[
r_4(N)ge r_3(N).
]

Behrend's primary construction gives a 3-AP-free subset of ([1,N]) of cardinality
[
Nexp(-O(sqrt{log N})).
]
Consequently, at (N=2^n),
[
a_n=rac{r_4(2^n)}{2^n}ge exp(-Csqrt n)
]
for some absolute (C>0) and all sufficiently large (n).

### 4. Fixed-step contraction is impossible

Assume for contradiction that for fixed (L,delta,n_0),
[
a_{n+L}le(1-delta)a_n
]
for all (nge n_0). Iterating along one residue class modulo (L) gives
[
a_{n_0+jL}le a_{n_0}(1-delta)^j
=exp(-Omega(j)).
]
The Behrend lower bound on the same subsequence is
[
a_{n_0+jL}geexp(-O(sqrt j)),
]
which is eventually larger than every (exp(-Omega(j))). Contradiction.

### 5. Fixed-window averaged contraction is impossible

If
[
rac1Lsum_{j=1}^{L}a_{n+j}le(1-delta)a_n,
]
then monotonicity gives
[
a_{n+L}le rac1Lsum_{j=1}^{L}a_{n+j}
le(1-delta)a_n.
]
This reduces to the already-refuted fixed-step contraction.

### 6. Constant-factor quasi-submultiplicativity is impossible

Assume that
[
a_{n+m}le C_0a_na_m
]
for all sufficiently large (n,m). Since the protected Green–Tao bound implies (a_m	o0), choose one fixed sufficiently large (m) with
[
q:=C_0a_m<1.
]
Then for all sufficiently large multiples (jm),
[
a_{(j+1)m}le q,a_{jm},
]
and iteration yields
[
a_{jm}le Kq^j=exp(-Omega(j)).
]
Again this contradicts the Behrend lower bound
[
a_{jm}geexp(-O(sqrt j)).
]

Thus a genuinely useful renormalization inequality cannot have a scale-independent positive fractional loss, and cannot have constant-factor multiplicative separation of scales.

### 7. A density-dependent loss with exponent (0<	heta<1) is sufficient

Assume instead that for fixed (L,c>0), (0<	heta<1), and all sufficiently large (n),
[
a_{n+L}le a_n(1-ca_n^	heta).
]
After increasing (n_0) if necessary, (0le ca_n^	heta<1).

Fix one residue class modulo (L), and write (b_j=a_{n_0+jL}). Then
[
b_{j+1}le b_j(1-cb_j^	heta).
]
Using ((1-u)^{-	heta}ge1+	heta u) for (0le u<1),
[
b_{j+1}^{-	heta}
ge b_j^{-	heta}(1-cb_j^	heta)^{-	heta}
ge b_j^{-	heta}+	heta c.
]
Hence
[
b_j^{-	heta}ge b_0^{-	heta}+	heta cj,
]
so
[
b_jle (b_0^{-	heta}+	heta cj)^{-1/	heta}
=O(j^{-1/	heta}).
]
Because (1/	heta>1), (sum_j b_j<infty). Monotonicity then bounds each intervening block of (L) terms by a constant multiple of the preceding sampled term, giving
[
sum_n a_n<infty.
]

This loss law is compatible with the Behrend obstruction: polynomial decay in the dyadic index (n) does not contradict the lower bound (exp(-O(sqrt n))).

## Adversarial checks

- **Direction check:** the Behrend argument is a lower bound on (r_3), and the transfer direction is (r_4ge r_3), not the reverse.
- **Iteration check:** fixed-step and quasi-submultiplicative hypotheses are used only in the ranges where they are assumed; a finite initial prefix is absorbed into a constant.
- **Average check:** the averaged-contraction refutation uses monotonicity only to infer (a_{n+L}le L^{-1}sum_{j=1}^L a_{n+j}).
- **Reblocking check:** partitioning a large interval into translated smaller intervals proves exactly (a_{n+L}le a_n); it supplies no strict factor and therefore no new exponent.
- **Sufficiency threshold check:** the proposed density-loss exponent must satisfy (	heta<1). At (	heta=1), the comparison gives only (a_n=O(1/n)), which is not enough for summability.
- **Parent-conjecture check:** no claim is made that the missing density-loss lemma is true, and the parent Erdős conjecture is not certified.

## First defect

Any proposed bounded-step renormalization with a fixed positive fractional contraction is too strong: iterating it forces exponential decay in the dyadic scale index, contradicting the Behrend lower bound inherited by (r_4).

## Frontier effect

The search narrows the viable `E3-Q4-SERIES` mechanism.

- Pure interval localization/reblocking collapses to monotonicity.
- Fixed-step uniform contraction, fixed-window averaged uniform contraction, and constant-factor quasi-submultiplicativity are ruled out.
- A density-dependent contraction is not ruled out.
- The explicit sufficient target is
[
a_{n+L}le a_n(1-ca_n^	heta),qquad 0<	heta<1.
]
Proving any theorem of this strength, or an averaged analogue that yields the same discrete differential inequality, would close the dyadic extremal series.

Disposition remains `SMALLEST_MISSING_LEMMA`; no parent-theorem conclusion follows.

## Next residual

The smallest residual is to derive, from genuine 4-AP structure rather than interval partitioning alone, a bounded-scale density loss quantitatively comparable to (c,a_n^{1+	heta}) with some (	heta<1). Any candidate must avoid implying fixed fractional contraction at small density, which the Behrend lower bound forbids. This is evidence only and carries no scheduling authority.

## Sources

1. Ben Green and Terence Tao, “New bounds for Szemerédi's theorem, III: A polylogarithmic bound for (r_4(N)),” arXiv:1705.01703; Mathematika 63 (2017). Primary preprint: https://arxiv.org/abs/1705.01703
2. F. A. Behrend, “On Sets of Integers Which Contain No Three Terms in Arithmetical Progression,” Proceedings of the National Academy of Sciences 32 (1946), 331–332, DOI 10.1073/pnas.32.12.331. Primary article/PDF: https://pmc.ncbi.nlm.nih.gov/articles/PMC1078964/ ; https://pmc.ncbi.nlm.nih.gov/articles/instance/1078964/pdf/pnas01693-0039.pdf

