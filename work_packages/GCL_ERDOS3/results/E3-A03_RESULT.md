GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-A03-IA-001
assignment: E3-A03
agent_ref: INDEPENDENT-AGENT-E3-A03-001
disposition: NO_COUNTEREXAMPLE_IN_DECLARED_FAMILY
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Let
\[
a_n:=\frac{r_4(2^n)}{2^n}.
\]

I found the following theorem-grade lower transfer. For all integers \(N,M\ge 1\),
\[
r_4\!\bigl((2N-1)M-N+1\bigr)\ge r_4(N)\,r_4(M).
\]
In particular,
\[
r_4(2NM)\ge r_4(N)r_4(M),
\]
and hence for dyadic \(N=2^n\), \(M=2^m\),
\[
a_{n+m+1}\ge \frac12 a_n a_m.
\]
Thus for every fixed \(L\ge2\),
\[
a_{n+L}\ge \frac{a_{L-1}}2\,a_n,
\]
while for \(L=1\) the trivial inclusion gives \(a_{n+1}\ge a_n/2\).

This lower transfer does not refute the promoted fixed-step density-loss route
\[
a_{n+L}\le a_n(1-c a_n^\theta),\qquad 0<\theta<1,
\]
because its lower ratio is a fixed constant \(q_L<1\), whereas \(1-ca_n^\theta\to1\).

The strongest pointwise lower construction found in the permitted primary-source audit is currently inherited from the 2024 Elsholtz–Hunter–Proske–Sauermann improvement for \(r_3\):
\[
r_4(N)\ge r_3(N)\ge N\,2^{-(C_*+o(1))\sqrt{\log_2N}},
\qquad
C_*=2\sqrt{\log_2(24/7)}\approx2.666539.
\]
Therefore
\[
a_n\ge 2^{-(C_*+o(1))\sqrt n}.
\]
This strengthens the power-recurrence obstruction exactly as follows: if, for some fixed \(C_0<\infty\), \(p>1\), and all sufficiently large \(n\),
\[
a_{2n}\le C_0a_n^p,
\]
then necessarily
\[
p\le\sqrt2.
\]
Hence every such recurrence with \(p>\sqrt2\) is impossible. The critical case \(p=\sqrt2\) is not excluded by the available lower constructions.

No valid construction found here produces
\[
a_n-a_{n+L}=o(a_n^{1+\theta})
\]
for any fixed \(L\) and \(0<\theta<1\). The promoted density-loss parameter region \(L\ge1,\ c>0,\ 0<\theta<1\) is therefore not reduced by this audit.

## Derivation / evidence

The immutable packet was read at commit
266b0857f3e13524ea9e69e2ef3bf4cd422503b5.

Verified blob identities:

- work_packages/GCL_ERDOS3/work_packages/E3-A03.md: 6564ccb50f984f17a9ab498a4043e0a9a7d672de;
- work_packages/GCL_ERDOS3/E3-TRANCHE-03.json: b3bc9a04a4b041da8fe311bbf69f607df6fee870;
- work_packages/GCL_ERDOS3/E3-TRANCHE-03_REPRESENTATION.md: 03314f5581731850cf7c507325e988f3d54842c0;
- work_packages/GCL_ERDOS3/FRONTIER.json: 66c453978eab0f192673f247542e19b43b83e3ca;
- work_packages/GCL_ERDOS3/results/E3-X01_RESULT.md: 16fb1935607c4f0391221606b7a48f5e5b61dbc6.

### 1. Exact carry-safe product construction

Translate extremizers so that
\[
A\subseteq\{0,\dots,N-1\},\qquad
B\subseteq\{0,\dots,M-1\},
\]
with \(|A|=r_4(N)\), \(|B|=r_4(M)\). Put
\[
Q:=2N-1,\qquad
S:=\{a+Qb:a\in A,\ b\in B\}.
\]
Then
\[
S\subseteq
\{0,\dots,(N-1)+Q(M-1)\},
\]
so its ambient interval has length
\[
H=(2N-1)M-N+1.
\]

Suppose
\[
x_t=a_t+Qb_t\qquad(t=0,1,2,3)
\]
is a four-term arithmetic progression in \(S\). The two second-difference equations are
\[
(a_0-2a_1+a_2)+Q(b_0-2b_1+b_2)=0,
\]
\[
(a_1-2a_2+a_3)+Q(b_1-2b_2+b_3)=0.
\]
For \(a_i\in[0,N-1]\),
\[
|a_i-2a_{i+1}+a_{i+2}|\le2N-2<Q.
\]
Hence each equation forces both its \(a\)-part and \(b\)-part to vanish separately. Thus \((a_t)\) and \((b_t)\) are each four-term arithmetic progressions. Since \(A\) and \(B\) are 4-AP-free, both coordinate progressions are constant, so \((x_t)\) is constant. Therefore \(S\) contains no nontrivial 4-AP and
\[
r_4(H)\ge |S|=r_4(N)r_4(M).
\]

Since \(H<2NM\), monotonicity in the ambient interval gives
\[
r_4(2NM)\ge r_4(N)r_4(M).
\]
Substituting \(N=2^n\), \(M=2^m\) gives
\[
a_{n+m+1}\ge\frac12a_na_m.
\]

### 2. Why this does not produce a near-plateau

For fixed \(L\ge2\), take \(m=L-1\):
\[
\frac{a_{n+L}}{a_n}\ge q_L:=\frac{a_{L-1}}2>0.
\]
This is only a fixed positive floor. It yields at best
\[
0\le D_{L,n}:=a_n-a_{n+L}\le(1-q_L)a_n,
\]
which is not of the required scale \(o(a_n^{1+\theta})\); after division by \(a_n^{1+\theta}\), the available upper bound is \((1-q_L)a_n^{-\theta}\), which diverges as \(a_n\to0\).

Conversely, the proposed density-loss upper ratio is
\[
\frac{a_{n+L}}{a_n}\le1-ca_n^\theta.
\]
For every fixed \(q_L<1\), \(c>0\), and \(\theta>0\), one has \(1-ca_n^\theta>q_L\) for all sufficiently large \(n\). Hence the exact product lower transfer and the promoted upper transfer are asymptotically compatible.

### 3. Audit of pointwise lower constructions

Behrend gives a 3-AP-free construction of density \(\exp(-O(\sqrt{\log N}))\). Since every 3-AP-free set is 4-AP-free,
\[
r_4(N)\ge r_3(N).
\]

Rankin generalized the geometric construction to longer arithmetic progressions. O'Bryant later combined the Rankin generalization with the Elkin/Green–Wolf refinement and obtained explicit general-\(k\) lower bounds; for \(k=4\) these remain of stretched-exponential \(\sqrt{\log N}\) type. These are pointwise constructions at one ambient size, not relations between an arbitrary \(r_4(N)\)-extremizer and \(r_4(MN)\).

Elkin improved Behrend in lower-order factors. The 2024 Elsholtz–Hunter–Proske–Sauermann construction gives the first improvement of the leading Behrend constant:
\[
r_3(N)\ge N\,2^{-(C_*+o(1))\sqrt{\log_2N}},
\qquad
C_*=2\sqrt{\log_2(24/7)}.
\]
By \(r_4\ge r_3\), this is the strongest pointwise lower bound from the audited family relevant here. It remains a pointwise lower bound only and gives no fixed-step near-plateau relation.

### 4. Exact obstruction for power recurrences

Assume
\[
a_{2n}\le C_0a_n^p
\]
eventually, with \(p>1\). Since the protected Green–Tao upper bound gives \(a_n\to0\), choose a sufficiently large starting \(n\) and set
\[
n_j:=2^j n,\qquad b_j:=-\log_2 a_{n_j}.
\]
Then
\[
b_{j+1}\ge p\,b_j-\log_2C_0.
\]
After choosing the start far enough into the tail, iteration gives
\[
b_j\ge c\,p^j
\]
for some \(c>0\).

The 2024 lower construction gives on the same subsequence
\[
b_j\le(C_*+o(1))\sqrt{n_j}
=(C_*+o(1))\sqrt n\,2^{j/2}.
\]
Therefore \(p^j\ll2^{j/2}\), forcing
\[
p\le\sqrt2.
\]
The improved 2024 leading constant sharpens the pointwise lower bound but does not move this exponent threshold, because the governing scale is still \(\sqrt n\).

### 5. Compatibility with the promoted density-loss law

The promoted law with \(0<\theta<1\) implies
\[
a_n=O(n^{-1/\theta}).
\]
The audited lower bound is
\[
a_n\ge2^{-(C_*+o(1))\sqrt n}.
\]
Since a stretched exponential \(2^{-C\sqrt n}\) is eventually smaller than every negative power of \(n\), these two bounds are compatible for every \(0<\theta<1\). Thus no value of \(L\), \(c\), or \(\theta\) in the declared parameter region is excluded by the pointwise lower constructions.

## Adversarial checks

- Carry check: the product proof does not reduce modulo the radix and does not assume carries away. It uses the strict bound \(|\Delta^2 a|<Q\) to force the high- and low-digit second differences to vanish separately.
- Radix-boundary check: replacing \(Q=2N-1\) by \(Q=2N-2\) is genuinely unsafe in this generic family. Take the 4-AP-free digit sets \(A=\{0,N-1\}\), \(B=\{0,1,2\}\). The product then contains
  \[
  N-1,\ 2N-2,\ 3N-3,\ 4N-4,
  \]
  a nontrivial 4-AP, represented respectively by digit pairs
  \[
  (N-1,0),(0,1),(N-1,1),(0,2).
  \]
- Direction check: all pointwise lower bounds transfer as \(r_4(N)\ge r_3(N)\), because a 3-AP-free set is automatically 4-AP-free.
- Pointwise-versus-transfer check: Behrend-, Rankin-, Elkin-, O'Bryant-, and Elsholtz–Hunter–Proske–Sauermann-type estimates lower-bound \(r_k(N)\) at a single scale. They do not by themselves bound \(a_{n+L}/a_n\).
- Near-plateau check: a fixed lower ratio \(q_L>0\) is far weaker than \(a_{n+L}/a_n=1-o(a_n^\theta)\). No implication between them was used.
- Power-threshold check: the contradiction for \(a_{2n}\le C_0a_n^p\) uses only \(p>\sqrt2\). At \(p=\sqrt2\), the growth rates match at order \(\sqrt n\), so the available lower bound does not give a universal contradiction.
- Density-loss check: the proposed law produces only polynomial decay in the dyadic index; the available lower constructions decay stretched-exponentially in that index and therefore do not conflict.

## First defect

The most promising counterexample mechanism fails at the exact point needed for falsification: an arbitrary-extremizer product can be made carry-safe, but the carry-safe embedding incurs a fixed radix/separation cost. Consequently the resulting lower transfer preserves only a fixed fraction of density at a fixed scale jump and does not force the ratio \(a_{n+L}/a_n\) to approach \(1\). The audited pointwise lower constructions likewise contain no arbitrary-extremizer inter-scale coupling, so they cannot manufacture the required near-plateaux.

## Frontier effect

E3-Q4-DENSITY-LOSS survives this declared adversarial family.

A valid lower-transfer boundary is now available:
\[
r_4((2N-1)M-N+1)\ge r_4(N)r_4(M),
\qquad
a_{n+m+1}\ge\tfrac12a_na_m.
\]
It is compatible with every declared density-loss parameter triple \((L,c,\theta)\) with \(L\ge1\), \(c>0\), \(0<\theta<1\), and therefore does not reduce that parameter region.

Separately, the lower-construction audit sharpens the previously broad power-recurrence obstruction to the exact exponent statement
\[
a_{2n}\le C_0a_n^p\ \text{eventually}
\quad\Longrightarrow\quad
p\le\sqrt2.
\]
No parent-theorem conclusion follows.

## Next residual

The residual is not another pointwise lower bound: it is a construction or theorem forcing \(a_{n+L}/a_n\) to approach \(1\) fast enough that \(1-a_{n+L}/a_n=o(a_n^\theta)\), or a proof that such persistence cannot occur. Generic no-carry tensor/Freiman embeddings lose a fixed density fraction and therefore cannot supply that behavior. No successor task is created here.

## Sources

1. F. A. Behrend, “On Sets of Integers Which Contain No Three Terms in Arithmetical Progression,” Proceedings of the National Academy of Sciences 32 (1946), 331–332. DOI: 10.1073/pnas.32.12.331. Primary full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC1078964/
2. R. A. Rankin, “Sets of Integers Containing not more than a Given Number of Terms in Arithmetical Progression,” Proceedings of the Royal Society of Edinburgh, Section A 65 (1961/62), 332–344. DOI: 10.1017/S0080454100017726. Publisher record: https://www.cambridge.org/core/journals/proceedings-of-the-royal-society-of-edinburgh-section-a-mathematics/article/abs/xxivsets-of-integers-containing-not-more-than-a-given-number-of-terms-in-arithmetical-progression/7CB49707304932619FC2F3FB4A6BDE81
3. Michael Elkin, “An Improved Construction of Progression-Free Sets,” arXiv:0801.4310; Proceedings of SODA 2010, 886–905. DOI: 10.1137/1.9781611973075.72. Primary preprint: https://arxiv.org/abs/0801.4310
4. Kevin O'Bryant, “Sets of integers that do not contain long arithmetic progressions,” Electronic Journal of Combinatorics 18 (2011), Paper P59. Primary preprint: https://arxiv.org/abs/0811.3057
5. Christian Elsholtz, Zach Hunter, Laura Proske, Lisa Sauermann, “Improving Behrend's construction: Sets without arithmetic progressions in integers and over finite fields,” arXiv:2406.12290 (2024). Primary preprint: https://arxiv.org/abs/2406.12290
6. Ben Green and Terence Tao, “New bounds for Szemerédi's theorem, III: A polylogarithmic bound for \(r_4(N)\),” Mathematika 63 (2017), 944–1040. Primary preprint: https://arxiv.org/abs/1705.01703