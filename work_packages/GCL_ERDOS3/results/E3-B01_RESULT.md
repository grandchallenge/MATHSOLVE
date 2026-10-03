# E3-B01 — dyadic scale-local bridge

Frontier node: `E3-B-SCALE-LOCAL`.

Disposition: **PROVED_NATIVE_PENDING_INDEPENDENT_VERIFY**.

## Definitions

Work in the positive integers. For (jge 0), let

[
I_j=[2^j,2^{j+1})capmathbb N,
qquad
c_j(A)=|Acap I_j|,
qquad
delta_j(A)=rac{c_j(A)}{2^j}.
]

Let

[
H_j(A)=sum_{nin Acap I_j}rac1n.
]

For (kge2), let (r_k(N)) denote the maximum cardinality of a subset of ({1,ldots,N}) containing no non-trivial (k)-term arithmetic progression.

## Theorem B01.1 — dyadic mass sandwich

For every (Asubseteqmathbb N_{>0}) and every (jge0),

[
rac12,delta_j(A)le H_j(A)le delta_j(A).
]

Consequently,

[
sum_{ain A}rac1a=infty
quadLongleftrightarrowquad
sum_{jge0}delta_j(A)=infty.
]

### Proof

If (nin I_j), then (2^jle n<2^{j+1}), hence

[
2^{-(j+1)}le rac1nle 2^{-j}.
]

Summing over the (c_j(A)) elements of (Acap I_j) gives the displayed sandwich. The dyadic blocks partition the positive integers, and all summands are non-negative, so the reciprocal series is the sum of the block masses. The factor-two comparison gives the equivalence. ∎

## Theorem B01.2 — summable-threshold forcing

Let ((	heta_j)_{jge0}) be non-negative with

[
sum_j	heta_j<infty.
]

If (A) has divergent reciprocal sum, then

[
delta_j(A)>	heta_j
]

for infinitely many (j).

### Proof

Otherwise there is (J) such that (delta_j(A)le	heta_j) for all (jge J). The finite prefix contributes finitely, while the tail is dominated by the summable series (sum_{jge J}	heta_j). Thus (sum_jdelta_j(A)<infty), contradicting B01.1. ∎

## Theorem B01.3 — AP-free extremal reduction

Fix (kge2). If

[
sum_{jge0}rac{r_k(2^j)}{2^j}<infty,
]

then every (Asubseteqmathbb N_{>0}) with divergent reciprocal sum contains a non-trivial (k)-term arithmetic progression.

### Proof

Assume (A) contains no non-trivial (k)-term arithmetic progression. Translation preserves arithmetic progressions. Translating (Acap I_j) by (-(2^j-1)) produces a (k)-AP-free subset of ({1,ldots,2^j}). Hence

[
c_j(A)le r_k(2^j)
]

and therefore

[
delta_j(A)le rac{r_k(2^j)}{2^j}.
]

The assumed dyadic extremal series is summable, so (sum_jdelta_j(A)<infty). B01.1 then implies convergence of (sum_{ain A}1/a), contradiction. ∎

## Three-term instantiation

Bloom and Sisask prove that for some absolute (c>0),

[
r_3(N)ll rac{N}{(log N)^{1+c}}.
]

Substituting (N=2^j) gives

[
rac{r_3(2^j)}{2^j}ll j^{-(1+c)},
]

which is summable. Thus B01.3 reproduces the known three-term case of the Erdős conjecture.

Primary source: Thomas F. Bloom and Olof Sisask, *Breaking the logarithmic barrier in Roth's theorem on arithmetic progressions*, arXiv:2007.03528.

## Exact remaining frontier

For each fixed (kge4), this route is closed by any theorem-grade sequence (eta_k(j)) such that

[
rac{r_k(2^j)}{2^j}leeta_k(j)
quad	ext{and}quad
sum_jeta_k(j)<infty.
]

No such (kge4) estimate is asserted by this result. Failure to obtain one does not refute the parent conjecture; it only blocks this blockwise-density route.

## Frontier disposition

- `E3-B-SCALE-LOCAL`: **PROVED**.
- New reduction `E3-B-AP-THRESHOLD`: **PROVED**.
- Parent `E3-B-AP`: **OPEN**.
- Frontier action: **INDEPENDENT_VERIFY** for B01 once, then **ADVANCE_FRONTIER** to `E3-B-AP`.


## Current four-term calibration

The maintained Erdős Problems record gives
(r_k(N)ll_k N/[(log N)(loglog N)^2]) as an example of a sufficient estimate for the parent conjecture. Under (N=2^j), this is exactly a summable normalized dyadic envelope.

By contrast, the current cited four-term theorem of Green–Tao gives only
(r_4(N)ll N(log N)^{-c}) for a small (c>0). Its dyadic envelope is (O(j^{-c})), so the present quantitative theory does not discharge B01.3 for (k=4). This is consistent with Green's 2026 survey statement that the reciprocal-sum conjecture remains far from established even at length four.

Sources:
- Erdős Problems, Problem 3, current record checked 2026-10-03.
- Ben Green and Terence Tao, *New bounds for Szemerédi's theorem, III: A polylogarithmic bound for r_4(N)*, Mathematika 63 (2017), DOI 10.1112/S0025579317000316.
- Ben Green, *Arithmetic progressions at the Journal of the LMS* (2026).
