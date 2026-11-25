GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-R01-IA-001
assignment: E3-R01
agent_ref: INDEPENDENT-AGENT-E3-R01-001
disposition: PROVED_REPRESENTATION_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Let \((a_n)_{n\ge1}\) be the protected sequence
\[
a_n=\frac{r_4(2^n)}{2^n}.
\]
From the protected packet, \(0<a_n\le1\) and \(a_n\) is nonincreasing. Fix \(L\ge1\) and \(\theta>0\), and define
\[
D_{L,n}=a_n-a_{n+L},\qquad U_\theta(n)=a_n^{-\theta},
\]
and, for \(0<\alpha\le1\),
\[
P(\alpha)=\#\{n\ge1:a_n\ge\alpha\}.
\]

The exact representation dictionary is:

1. **Layer cake, with exact endpoint convention.**
   \[
   \sum_{n\ge1}a_n=\int_{(0,1]}P(\alpha)\,d\alpha
   \]
   in the extended nonnegative sense. The convention \(a_n\ge\alpha\), equivalently \(\alpha\le a_n\), is the exact indicator convention. The value assigned to \(P(0)\) is irrelevant because \(\{0\}\) has Lebesgue measure zero.

2. **Density loss and gluing defect are literally equivalent.** For any \(c>0\),
   \[
   a_{n+L}\le a_n(1-ca_n^\theta)
   \quad\Longleftrightarrow\quad
   D_{L,n}\ge c\,a_n^{1+\theta}.
   \]

3. **Density loss implies uniform reciprocal-potential drift without any additional small-density assumption.** If the density-loss inequality holds at \(n\), positivity of \(a_{n+L}\) automatically forces \(ca_n^\theta<1\), and
   \[
   U_\theta(n+L)-U_\theta(n)\ge \theta c.
   \]
   The constant \(\theta c\) is the best uniform constant obtainable over arbitrarily small positive densities from this hypothesis alone.

4. **Uniform reciprocal drift has an exact nonlinear converse.** If
   \[
   U_\theta(n+L)-U_\theta(n)\ge\delta>0,
   \]
   then exactly
   \[
   a_{n+L}\le a_n(1+\delta a_n^\theta)^{-1/\theta},
   \]
   hence
   \[
   D_{L,n}\ge
   a_n\Bigl[1-(1+\delta a_n^\theta)^{-1/\theta}\Bigr].
   \]
   If one knows \(0<a_n\le A\), then this implies the power-form density loss
   \[
   D_{L,n}\ge c_A a_n^{1+\theta},
   \]
   with the best constant guaranteed solely from that range
   \[
   c_A=
   \frac{1-(1+\delta A^\theta)^{-1/\theta}}{A^\theta}>0.
   \]
   In particular, for the protected density range \(A=1\),
   \[
   c_1=1-(1+\delta)^{-1/\theta}.
   \]
   Moreover reciprocal drift itself forces \(a_n\to0\); therefore for every
   \[
   0<c<\delta/\theta
   \]
   the simpler density-loss inequality \(D_{L,n}\ge c a_n^{1+\theta}\) holds eventually. In general \(c=\delta/\theta\) cannot be demanded: it is the limiting small-density constant, not an attained converse constant.

Thus, for bounded positive sequences and fixed \((L,\theta)\), **existence of a uniform positive \(U_\theta\)-drift is quantitatively equivalent to existence of a power-form density loss**, although the constants change.

5. **Persistence consequence.** If
   \[
   U_\theta(n+L)-U_\theta(n)\ge\delta
   \qquad(n\ge n_0),
   \]
   then
   \[
   P(\alpha)\le n_0+L-1+L\Bigl\lfloor\frac{\alpha^{-\theta}}{\delta}\Bigr\rfloor
   \]
   is a valid coarse uniform bound, hence
   \[
   P(\alpha)=O(\alpha^{-\theta}).
   \]
   More sharply, writing \(u_r=U_\theta(n_0+r)\), \(0\le r<L\),
   \[
   P(\alpha)\le n_0-1+
   \sum_{r=0}^{L-1}
   \max\!\left(
     0,\,
     1+\left\lfloor\frac{\alpha^{-\theta}-u_r}{\delta}\right\rfloor
   \right).
   \]
   Therefore a density loss with constant \(c\) gives
   \[
   P(\alpha)=O(\alpha^{-\theta})
   \]
   with asymptotic coefficient at most \(L/(\theta c)\) at the representation level. The exponent is sharp for these hypotheses.

6. **Persistence and pointwise polynomial decay are equivalent for a positive nonincreasing sequence.** For fixed \(\theta>0\),
   \[
   P(\alpha)=O(\alpha^{-\theta})
   \quad\Longleftrightarrow\quad
   a_n=O(n^{-1/\theta}).
   \]

7. **Series criterion.**
   \[
   \sum_n a_n<\infty
   \quad\Longleftrightarrow\quad
   P\in L^1((0,1]).
   \]
   Hence \(P(\alpha)=O(\alpha^{-\theta})\) with \(0<\theta<1\) is sufficient, because \(\alpha^{-\theta}\) is integrable at \(0\). This power condition is not necessary.

The implication diagram is therefore
\[
\boxed{\text{density loss}}
\Longleftrightarrow
\boxed{\text{defect lower bound}}
\Longleftrightarrow_{\text{constants change}}
\boxed{\text{uniform reciprocal drift}}
\Longrightarrow
\boxed{P(\alpha)=O(\alpha^{-\theta})}
\Longleftrightarrow
\boxed{a_n=O(n^{-1/\theta})}
\Longrightarrow_{\theta<1}
\boxed{P\in L^1}
\Longleftrightarrow
\boxed{\sum_n a_n<\infty}.
\]
The arrows from persistence/pointwise polynomial decay back to local drift/defect are false, and the arrow from series convergence back to any fixed subcritical persistence power is false.

Accordingly, the weakest exact representation-level theorem that still implies the series is simply
\[
P\in L^1((0,1]),
\]
equivalently an integrable majorant \(P(\alpha)\le Q(\alpha)\) near \(0\) with \(\int_0 Q(\alpha)\,d\alpha<\infty\). A power law with exponent \(<1\) is one stronger sufficient specialization, not the exact frontier.

No claim here proves the protected combinatorial density-loss inequality for \(r_4\), and no claim certifies E3-Q4-SERIES or Erdős Problem 3.

## Derivation / evidence

The immutable packet was read only at commit
266b0857f3e13524ea9e69e2ef3bf4cd422503b5.

Verified blob identities:

- E3-R01.md: 87f8b9619f62447b1425e2b71d3b374d5488220e
- E3-TRANCHE-03.json: b3bc9a04a4b041da8fe311bbf69f607df6fee870
- E3-TRANCHE-03_REPRESENTATION.md: 03314f5581731850cf7c507325e988f3d54842c0
- FRONTIER.json: 66c453978eab0f192673f247542e19b43b83e3ca
- E3-X01_RESULT.md: 16fb1935607c4f0391221606b7a48f5e5b61dbc6

### Layer cake

For each \(n\), because \(0\le a_n\le1\),
\[
a_n=\int_{(0,1]}\mathbf 1_{\{\alpha\le a_n\}}\,d\alpha.
\]
All summands are nonnegative, so Tonelli's theorem in its elementary nonnegative form gives
\[
\sum_{n\ge1}a_n
=
\int_{(0,1]}
\sum_{n\ge1}\mathbf 1_{\{\alpha\le a_n\}}\,d\alpha
=
\int_{(0,1]}P(\alpha)\,d\alpha.
\]
Both sides may equal \(+\infty\). Inclusion of the equality endpoint \(\alpha=a_n\) matches the declared \(a_n\ge\alpha\) convention; changing finitely or countably many single \(\alpha\)-points would not change the integral, but the displayed convention is exact.

### Density loss to drift

From
\[
a_{n+L}\le a_n(1-ca_n^\theta)
\]
and \(a_{n+L}>0\), necessarily \(x:=ca_n^\theta<1\). Therefore
\[
U_\theta(n+L)
\ge
a_n^{-\theta}(1-x)^{-\theta}.
\]
Convexity of \(x\mapsto(1-x)^{-\theta}\) on \([0,1)\) gives
\[
(1-x)^{-\theta}\ge1+\theta x,
\]
so
\[
U_\theta(n+L)-U_\theta(n)
\ge
a_n^{-\theta}\theta c a_n^\theta
=
\theta c.
\]
As \(x\downarrow0\),
\[
\frac{(1-x)^{-\theta}-1}{x}\to\theta,
\]
so no larger uniform multiple than \(\theta c\) is forced over arbitrarily small densities.

### Drift to exact density loss

If
\[
a_{n+L}^{-\theta}-a_n^{-\theta}\ge\delta,
\]
then
\[
a_{n+L}^{-\theta}
\ge
a_n^{-\theta}(1+\delta a_n^\theta),
\]
hence
\[
a_{n+L}
\le
a_n(1+\delta a_n^\theta)^{-1/\theta}.
\]

Set
\[
F(t)=1-(1+\delta t)^{-1/\theta}.
\]
Then \(F(0)=0\), \(F'(t)>0\), and \(F''(t)<0\), so \(F\) is strictly concave and \(F(t)/t\) decreases on \(t>0\). Thus for \(0<t\le A^\theta\),
\[
F(t)\ge
\frac{F(A^\theta)}{A^\theta}t,
\]
which is exactly the stated \(c_A\). Also
\[
\lim_{t\downarrow0}\frac{F(t)}t=\frac{\delta}{\theta}.
\]
Strict concavity gives \(F(t)<(\delta/\theta)t\) for every \(t>0\), explaining why \(\delta/\theta\) is only the limiting eventual constant.

### Drift to persistence

For each residue \(r\in\{0,\dots,L-1\}\),
\[
U_\theta(n_0+r+jL)\ge u_r+j\delta.
\]
If \(a_{n_0+r+jL}\ge\alpha\), then
\[
U_\theta(n_0+r+jL)\le\alpha^{-\theta},
\]
so
\[
j\le\frac{\alpha^{-\theta}-u_r}{\delta}.
\]
Counting admissible nonnegative integers \(j\) gives the displayed residuewise persistence bound and therefore \(P(\alpha)=O(\alpha^{-\theta})\).

The exponent is sharp. For example, with \(L=1\),
\[
a_n=(u_0+n\delta)^{-1/\theta}
\]
has exact drift
\[
U_\theta(n+1)-U_\theta(n)=\delta
\]
and
\[
P(\alpha)\asymp \delta^{-1}\alpha^{-\theta}.
\]

For the density-loss formulation, the equality recursion
\[
b_{j+1}=b_j(1-cb_j^\theta)
\]
has
\[
b_{j+1}^{-\theta}-b_j^{-\theta}
=
\theta c+O(b_j^\theta),
\]
and the lower drift bound already gives \(b_j^\theta=O(1/j)\). Hence
\[
b_j^{-\theta}=\theta cj+O(\log j),
\]
so the persistence exponent \(\theta\), and the leading representation-level scale \(1/(\theta c)\), cannot be improved uniformly from the power-loss hypothesis alone.

### Persistence to pointwise decay and back

If \(P(\alpha)\le C\alpha^{-\theta}\) for small \(\alpha\), then monotonicity gives
\[
n\le P(a_n)\le C a_n^{-\theta},
\]
hence
\[
a_n\le (C/n)^{1/\theta}.
\]

Conversely, if \(a_n\le K n^{-1/\theta}\) and \(a_n\ge\alpha\), then
\[
n\le (K/\alpha)^\theta,
\]
so
\[
P(\alpha)\le (K/\alpha)^\theta.
\]

### Power persistence to the series

If \(P(\alpha)\le C\alpha^{-\theta}\) near \(0\) with \(0<\theta<1\), then
\[
\int_0^{\alpha_0}P(\alpha)\,d\alpha
\le
C\int_0^{\alpha_0}\alpha^{-\theta}\,d\alpha
=
\frac{C}{1-\theta}\alpha_0^{1-\theta}<\infty.
\]
The remaining interval is finite because \(P(\alpha_0)<\infty\). Layer cake then gives \(\sum_n a_n<\infty\).

## Adversarial checks

1. **Persistence power does not imply local drift or defect.** Fix \(0<\theta<1\). For \(k\ge1\), let
   \[
   \ell_k=\lceil2^{k\theta}\rceil
   \]
   and make a nonincreasing block sequence with \(\ell_k\) consecutive terms equal to \(2^{-k}\). Then
   \[
   P(2^{-k})=\sum_{j\le k}\ell_j=O(2^{k\theta}),
   \]
   and therefore \(P(\alpha)=O(\alpha^{-\theta})\). Also
   \[
   \sum_n a_n
   =
   \sum_k \ell_k2^{-k}
   <
   \infty.
   \]
   But the block lengths tend to infinity. For every fixed \(L\), infinitely many blocks contain indices \(n\) with
   \[
   a_{n+L}=a_n.
   \]
   Hence \(D_{L,n}=0\) and \(U_\theta(n+L)-U_\theta(n)=0\) infinitely often. No eventual positive fixed-step defect lower bound or reciprocal drift follows from the persistence power law.

2. **Series convergence does not imply any power persistence \(P(\alpha)=O(\alpha^{-\eta})\) with \(\eta<1\).** Let
   \[
   \ell_k=\left\lceil\frac{2^k}{k^2}\right\rceil
   \]
   and again take \(\ell_k\) consecutive terms equal to \(2^{-k}\). Then
   \[
   \sum_n a_n
   =
   \sum_k\ell_k2^{-k}
   \le
   \sum_k\left(\frac1{k^2}+2^{-k}\right)
   <
   \infty.
   \]
   However
   \[
   P(2^{-k})\ge\ell_k\ge\frac{2^k}{k^2}.
   \]
   For every fixed \(\eta<1\),
   \[
   \frac{P(2^{-k})}{(2^{-k})^{-\eta}}
   \ge
   \frac{2^{k(1-\eta)}}{k^2}\to\infty.
   \]
   Thus no subcritical power exponent is necessary for convergence.

3. **The threshold \(\theta<1\) is sharp for a bare power-persistence implication.** The sequence
   \[
   a_n=1/n
   \]
   has
   \[
   P(\alpha)=\lfloor1/\alpha\rfloor=O(\alpha^{-1})
   \]
   but
   \[
   \sum_n a_n=\infty.
   \]

4. **The limiting converse constant \(\delta/\theta\) is not generally attained.** The exact-drift sequence
   \[
   a_n=(u_0+n\delta)^{-1/\theta}
   \]
   satisfies drift \(\delta\), but strict concavity gives at every positive density
   \[
   1-(1+\delta a_n^\theta)^{-1/\theta}
   <
   (\delta/\theta)a_n^\theta.
   \]
   So drift does not imply the density-loss constant \(c=\delta/\theta\) pointwise.

5. **No hidden combinatorial inference.** Every statement above is an elementary consequence of positivity, boundedness, monotonicity, and the declared representations. Nothing here proves that the protected \(r_4\) sequence satisfies density loss, reciprocal drift, a persistence power law, or any new cross-block compatibility property.

## First defect

The first false equivalence occurs at the persistence/local-dynamics interface: \(P(\alpha)=O(\alpha^{-\theta})\) is equivalent to a global pointwise polynomial envelope for a nonincreasing sequence, but it does **not** imply any fixed-step positive gluing defect or reciprocal-potential drift. Arbitrarily long plateaus provide an explicit obstruction.

## Frontier effect

This result does not close E3-Q4-DENSITY-LOSS, but it removes redundancy from the representation programme.

The gluing-defect inequality and density-loss inequality are identical statements. Uniform \(U_\theta\)-drift is not merely a heuristic consequence: on the protected bounded density range it is quantitatively equivalent, with an exact nonlinear converse and explicit constants. Therefore proving either local formulation is essentially the same frontier-strength result.

By contrast, persistence is strictly weaker. To close E3-Q4-SERIES it is unnecessary to recover local drift: it is enough, and in persistence coordinates exactly necessary, to prove
\[
P\in L^1((0,1]).
\]
A bound \(P(\alpha)=O(\alpha^{-\theta})\) for some \(\theta<1\) is a convenient stronger target, but not a necessary form of the theorem.

No parent-theorem conclusion follows.

## Next residual

The smallest representation-level target is an integrable persistence estimate for the actual extremal sequence, i.e. prove \(P(\alpha)\le Q(\alpha)\) near \(0\) for some explicit \(Q\in L^1(0,1)\). Any attempt to recover the stronger local density-loss/drift law must use genuine cross-block 4-AP structure, because persistence or pointwise decay alone cannot supply it.

## Sources

No external mathematical source was required; all proofs above are elementary and use only the protected packet at commit 266b0857f3e13524ea9e69e2ef3bf4cd422503b5.

Protected source identifiers used:

1. E3-R01 immutable task, blob 87f8b9619f62447b1425e2b71d3b374d5488220e:
   https://github.com/grandchallenge/MATHSOLVE/blob/266b0857f3e13524ea9e69e2ef3bf4cd422503b5/work_packages/GCL_ERDOS3/work_packages/E3-R01.md

2. E3-TRANCHE-03 manifest, blob b3bc9a04a4b041da8fe311bbf69f607df6fee870:
   https://github.com/grandchallenge/MATHSOLVE/blob/266b0857f3e13524ea9e69e2ef3bf4cd422503b5/work_packages/GCL_ERDOS3/E3-TRANCHE-03.json

3. E3-TRANCHE-03 representation note, blob 03314f5581731850cf7c507325e988f3d54842c0:
   https://github.com/grandchallenge/MATHSOLVE/blob/266b0857f3e13524ea9e69e2ef3bf4cd422503b5/work_packages/GCL_ERDOS3/E3-TRANCHE-03_REPRESENTATION.md

4. FRONTIER.json, blob 66c453978eab0f192673f247542e19b43b83e3ca:
   https://github.com/grandchallenge/MATHSOLVE/blob/266b0857f3e13524ea9e69e2ef3bf4cd422503b5/work_packages/GCL_ERDOS3/FRONTIER.json

5. Promoted E3-X01 result, blob 16fb1935607c4f0391221606b7a48f5e5b61dbc6:
   https://github.com/grandchallenge/MATHSOLVE/blob/266b0857f3e13524ea9e69e2ef3bf4cd422503b5/work_packages/GCL_ERDOS3/results/E3-X01_RESULT.md
