GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-A02-IA-001
assignment: E3-A02
agent_ref: INDEPENDENT-AGENT-E3-A02-001
disposition: COUNTEREXAMPLE
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Naive multiplicative cross-scale bootstrapping is false, and interval partitioning alone cannot improve the known logarithmic exponent.

Write
[
a_n:=rac{r_4(2^n)}{2^n}.
]

1. Literal submultiplicativity fails:
[
r_4(MN)le r_4(M)r_4(N)
]
is already false at (M=N=4). Since (r_4(4)=3), while
[
S={1,2,4,7,8,9,11,12,14,15}subset[16]
]
has 10 elements and contains no nontrivial 4-term arithmetic progression,
[
r_4(16)ge10>9=r_4(4)^2.
]
Equivalently,
[
a_4gerac{10}{16}>left(rac34ight)^2=a_2^2.
]

2. More strongly, there is no fixed (C<infty) and threshold (J) for which
[
a_{m+n}le C,a_ma_n
]
holds for all (m,nge J). Such an eventual fixed-constant quasi-submultiplicativity would force exponential decay in the dyadic index, contradicting known lower-bound constructions for (r_4).

3. The elementary partition inequality
[
r_4(N)le q,r_4(M)+r_4(s),qquad N=qM+s,quad 0le s<M,
]
is valid. In the exact dyadic case it gives only
[
a_nle a_mqquad(m<n).
]
Combining this with the Green–Tao pointwise estimate at a shorter scale (M=N^	heta) yields
[
rac{r_4(N)}Nll (log M)^{-c}
=	heta^{-c}(log N)^{-c},
]
so the logarithmic exponent is unchanged. Repeating the partition does not multiply density gains; it merely reduces to the density bound at the terminal shorter scale.

4. A useful sharp obstruction for power-type diagonal recurrences is the following. O'Bryant's (k=4) lower construction gives, for all sufficiently large (j),
[
a_jge c_0,j^{1/4}2^{-2sqrt2,sqrt j}
]
for some (c_0>0). Therefore any eventual recurrence
[
a_{2n}le C a_n^p
]
with fixed (C) and (p>sqrt2) is impossible. The lower construction by itself does not rule out (1<p<sqrt2); such a recurrence would nevertheless already force stretched-exponential decay in (n) and hence (sum_n a_n<infty). The endpoint (p=sqrt2) is a constant-sensitive boundary not decided by this asymptotic comparison.

## Derivation / evidence

For the finite counterexample, (r_4(4)=3) because ([4]) itself is a 4-AP and deleting any one point leaves a 3-element 4-AP-free set. For the displayed set (Ssubset[16]), direct enumeration of the possible 4-APs (a,a+d,a+2d,a+3d) with (d=1,dots,5) shows that each meets ([16]setminus S={3,5,6,10,13,16}). Hence (S) is 4-AP-free.

For the fixed-(C) obstruction, suppose (a_{m+n}le C a_ma_n) eventually. Green–Tao give (a_nll n^{-c}), hence (a_n	o0). Choose (n_0) in the recurrence range with (x_0:=Ca_{n_0}<1), and set (x_t:=C a_{2^t n_0}). Then
[
x_{t+1}le x_t^2,
]
so
[
a_{2^t n_0}le C^{-1}x_0^{2^t}
le C^{-1}exp(-lambda,2^t)
= C^{-1}exp(-lambda' j_t),
qquad j_t=2^t n_0.
]
O'Bryant's (k=4) construction, evaluated at (N=2^{j_t}), instead gives
[
a_{j_t}ge c_0,j_t^{1/4}2^{-2sqrt2sqrt{j_t}},
]
which is asymptotically much larger than (exp(-lambda'j_t)). Contradiction.

More generally, if (a_{2n}le C a_n^p), put (K=C^{1/(p-1)}) and (x_n=Ka_n). Once (x_{n_0}<1),
[
x_{2^t n_0}le x_{n_0}^{p^t}
=exp!left(-lambda (2^t)^{log_2 p}ight)
=exp!left(-lambda' j_t^{log_2 p}ight).
]
This contradicts the (e^{-O(sqrt j)}) lower construction whenever (log_2p>1/2), i.e. (p>sqrt2).

For partitioning, if (Asubset[N]) is 4-AP-free, then its intersection with every consecutive interval of length (M), translated back to ([M]), is also 4-AP-free. Summing the block cardinalities gives the stated partition inequality. No cross-block constraint is used, so no multiplicative density improvement can arise from this argument alone.

## Adversarial checks

- **Naive submultiplicativity (r_4(MN)le r_4(M)r_4(N)):** false by the explicit (4	imes4) counterexample above.
- **Naive normalized submultiplicativity (a_{m+n}le a_ma_n):** false at (m=n=2).
- **Fixed-constant eventual quasi-submultiplicativity (a_{m+n}le C a_ma_n):** impossible by Green–Tao decay plus the O'Bryant lower construction.
- **Partition a dyadic interval into shorter intervals and reapply the same pointwise estimate:** valid but exponent-neutral; it reproduces ((log N)^{-c}) up to a constant when the shorter scale is (N^	heta).
- **Diagonal power recurrence (a_{2n}le C a_n^p):** ruled out by the known lower construction for every (p>sqrt2); not ruled out by that construction for (1<p<sqrt2). Any fixed (p>1), if proved in the compatible range, would be strong enough to imply series convergence.
- **Fixed-ratio linear contraction (a_{2n}leho a_n):** not excluded by the lower construction. If (ho<1/2), monotonicity gives convergence by grouping the series over index blocks ([2^t,2^{t+1})). Thus this remains a logically viable cross-scale form, but it is not supplied by interval partitioning.

## First defect

The first concrete defect is the failure of literal submultiplicativity at (M=N=4):
[
r_4(16)ge10>r_4(4)^2=9.
]

## Frontier effect

This does not alter the equivalence in E3-B02 and does not certify the parent conjecture. It eliminates the most naive multiplicative and fixed-constant quasi-multiplicative cross-scale upgrades, and shows that plain interval partitioning cannot bootstrap the Green–Tao logarithmic exponent. The surviving region requires genuinely new cross-block information, for example a sufficiently strong linear contraction across index doubling, an averaged contraction, or a nonlinear recurrence in the lower-bound-compatible power range.

## Next residual

Evidence only: the cleanest surviving target class is a theorem-grade cross-scale inequality that is stronger than monotonicity but weaker than the ruled-out multiplicative laws. Examples include (a_{2n}leho a_n) with (ho<1/2), an averaged analogue that contracts dyadic index-block mass, or (a_{2n}le C a_n^p) with (1<p<sqrt2). None is established here.

## Sources

- Ben Green and Terence Tao, *New bounds for Szemerédi's theorem, III: A polylogarithmic bound for (r_4(N))*, arXiv:1705.01703, https://arxiv.org/abs/1705.01703 . Used for (r_4(N)ll N(log N)^{-c}) and hence (a_n	o0).
- Kevin O'Bryant, *Sets of integers that do not contain long arithmetic progressions*, arXiv:0811.3057 (v3, 2010; Electronic Journal of Combinatorics 18 (2011), P59), https://arxiv.org/abs/0811.3057 . Used for the (k=4) constructive lower bound, which at (N=2^j) has normalized size (c_0 j^{1/4}2^{-2sqrt2sqrt j}) up to a positive constant.

