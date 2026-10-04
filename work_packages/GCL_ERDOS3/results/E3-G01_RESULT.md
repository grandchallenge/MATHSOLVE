GCL-CONTRIBUTION-RESULT/1
dispatch_id: GCL-ERDOS3-E3-G01-IA-001
assignment: E3-G01
agent_ref: INDEPENDENT-AGENT-E3-G01-001
disposition: SMALLER_GLUE_LEMMA
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED

## Strongest exact statement

Write
\[
N=2^n,\qquad m=2^L,\qquad a_s=\frac{r_4(2^s)}{2^s},\qquad D_{L,n}=a_n-a_{n+L}.
\]

I prove two exact reductions.

### 1. Exact extremizer-tree concentration

Let \(A\subseteq[0,m^tN-1]\) be a 4-AP-free extremizer, so
\[
|A|=r_4(m^tN),\qquad \frac{|A|}{m^tN}=a_{n+tL}.
\]
Recursively partition the ambient interval into \(m\) equal consecutive children at each level. At depth \(j\in\{0,\dots,t\}\), every node has length
\[
2^{s_j},\qquad s_j=n+(t-j)L.
\]
For a node \(v\) at depth \(j\), let \(\rho(v)\) be the density of \(A\) in that node and define its local extremality deficit
\[
\delta(v):=a_{s_j}-\rho(v)\ge 0.
\]

If \(V_j\) is a uniformly random depth-\(j\) node, then exactly
\[
\mathbb E\,\delta(V_j)=a_{s_j}-a_{n+tL}.
\]
Consequently, if \(V_1,\dots,V_t\) are the nodes on a uniformly random root-to-leaf path, then
\[
S_{L,n,t}:=
\mathbb E\sum_{j=1}^t\delta(V_j)
=
\sum_{k=0}^{t-1}\bigl(a_{n+kL}-a_{n+tL}\bigr)
=
\sum_{h=0}^{t-1}(h+1)D_{L,n+hL},
\]
and therefore
\[
S_{L,n,t}\le t\bigl(a_n-a_{n+tL}\bigr).
\]

Hence, for arbitrary thresholds \(\lambda_j>0\),
\[
\Pr\!\left(\exists j:\delta(V_j)>\lambda_j\right)
\le
\sum_{j=1}^t
\frac{a_{s_j}-a_{n+tL}}{\lambda_j}.
\]
In particular, for a common threshold \(\lambda>0\), at least
\[
m^t\max\!\left\{0,1-\frac{S_{L,n,t}}{\lambda}\right\}
\]
root-to-leaf paths are \(\lambda\)-near-extremal at every level.

More generally, if
\[
B_\lambda:=\#\{j\in\{1,\dots,t\}:\delta(V_j)>\lambda\},
\]
then for every integer \(q\ge1\),
\[
\Pr(B_\lambda\ge q)\le \frac{S_{L,n,t}}{q\lambda}.
\]
Thus at least a fraction
\[
1-\frac{S_{L,n,t}}{q\lambda}
\]
of paths have fewer than \(q\) bad levels. No uniform-in-node conclusion is used at depth \(>1\).

At one level, however, the fixed branching factor gives a stronger exact statement. If \(A\subseteq[0,mN-1]\) is an extremizer and \(A_i\subseteq[0,N-1]\) are its \(m\) fibers, with \(\rho_i=|A_i|/N\), then
\[
D_{L,n}
=
\frac1m\sum_{i=0}^{m-1}(a_n-\rho_i).
\]
Since every summand is nonnegative,
\[
\#\{i:a_n-\rho_i>\lambda\}\le \frac{mD_{L,n}}{\lambda},
\qquad
\max_i(a_n-\rho_i)\le mD_{L,n}.
\]
This is the precise justified conversion from average to one-level uniform near-extremality.

### 2. Exact finite/local gluing radius

Define the integer uniform gluing slack
\[
H_{L,n}:=
\min\Bigl\{
h\in\mathbb Z_{\ge0}:
\exists B_0,\dots,B_{m-1}\subseteq[0,N-1]
\text{ such that }
|B_i|\ge r_4(N)-h\ \forall i,
\]
\[
\hspace{42mm}
\text{and }
\bigcup_{i=0}^{m-1}(iN+B_i)
\text{ is 4-AP-free}
\Bigr\},
\]
and normalize
\[
\Gamma_{L,n}:=\frac{H_{L,n}}{N}.
\]

Then exactly
\[
\boxed{D_{L,n}\le \Gamma_{L,n}\le mD_{L,n}.}
\]

Therefore the promoted density-loss target is equivalent, up to the fixed factor \(m=2^L\), to the single finite/local gluing theorem
\[
\Gamma_{L,n}\ge \kappa a_n^{1+\theta}
\]
for some fixed \(L\ge1\), \(\kappa>0\), \(0<\theta<1\), and all sufficiently large \(n\).

More precisely:

- if \(D_{L,n}\ge c a_n^{1+\theta}\), then \(\Gamma_{L,n}\ge c a_n^{1+\theta}\);
- if \(\Gamma_{L,n}\ge \kappa a_n^{1+\theta}\), then
  \[
  D_{L,n}\ge \frac{\kappa}{m}a_n^{1+\theta}.
  \]

Thus the remaining theorem-grade arithmetic content can be isolated as:

> **Uniform near-extremizer gluing lemma.** For some fixed \(L\), \(\theta\in(0,1)\), and \(\kappa>0\), one must delete at least \(\kappa N a_n^{1+\theta}\) points from the row budget \(r_4(N)\) before \(m=2^L\) mutually positioned fibers can satisfy all cross-fiber 4-AP constraints.

This lemma is not proved here. The proved advance is the exact constant-factor equivalence between it and E3-Q4-DENSITY-LOSS, together with the exact multilevel concentration theorem above.

## Derivation / evidence

### Protected packet verification

The immutable files were read only at commit
266b0857f3e13524ea9e69e2ef3bf4cd422503b5.

Verified blob identities:

- work_packages/GCL_ERDOS3/work_packages/E3-G01.md:
  c0dffd18ba0e0f341630b125ef856624fe54ad8a;
- work_packages/GCL_ERDOS3/E3-TRANCHE-03.json:
  b3bc9a04a4b041da8fe311bbf69f607df6fee870;
- work_packages/GCL_ERDOS3/E3-TRANCHE-03_REPRESENTATION.md:
  03314f5581731850cf7c507325e988f3d54842c0;
- work_packages/GCL_ERDOS3/FRONTIER.json:
  66c453978eab0f192673f247542e19b43b83e3ca;
- work_packages/GCL_ERDOS3/results/E3-X01_RESULT.md:
  16fb1935607c4f0391221606b7a48f5e5b61dbc6.

No tranche-03 contributor return, intake issue, later repository state, discussion thread, or unpublished note was inspected.

### A. One-step deficit identity

Let \(A\subseteq[0,mN-1]\) be a global extremizer and define
\[
A_i=\{u\in[0,N-1]:iN+u\in A\}.
\]
Every \(A_i\) is 4-AP-free, so
\[
|A_i|\le r_4(N),\qquad \rho_i:=|A_i|/N\le a_n.
\]
Because the \(m\) blocks partition the ambient interval,
\[
\frac1m\sum_i\rho_i=\frac{|A|}{mN}=a_{n+L}.
\]
Therefore
\[
\frac1m\sum_i(a_n-\rho_i)
=a_n-a_{n+L}
=D_{L,n}.
\]

### B. Iterated tree identity

At depth \(j\), all blocks have equal length, so their mean density is still the root density \(a_{n+tL}\). Each depth-\(j\) restriction is 4-AP-free in an interval of length \(2^{s_j}\), hence its density is at most \(a_{s_j}\). This gives
\[
\mathbb E\,\delta(V_j)=a_{s_j}-a_{n+tL}.
\]

Summing over \(j\) and reindexing,
\[
S_{L,n,t}
=
\sum_{k=0}^{t-1}(a_{n+kL}-a_{n+tL}).
\]
Since
\[
a_{n+kL}-a_{n+tL}
=
\sum_{h=k}^{t-1}D_{L,n+hL},
\]
interchanging the finite sums gives
\[
S_{L,n,t}
=
\sum_{h=0}^{t-1}(h+1)D_{L,n+hL}.
\]
The path concentration inequalities then follow from Markov's inequality and the union bound. The "most levels" statement follows from
\[
\lambda B_\lambda
\le
\sum_{j=1}^t\delta(V_j).
\]

### C. Proof of \(D_{L,n}\le\Gamma_{L,n}\le mD_{L,n}\)

Let \(h=H_{L,n}\), witnessed by fibers \(B_i\). Their glued union is 4-AP-free and has size at least
\[
m(r_4(N)-h).
\]
Hence
\[
r_4(mN)\ge m(r_4(N)-h).
\]
After division by \(mN\),
\[
a_{n+L}\ge a_n-\frac hN,
\]
so
\[
D_{L,n}\le \frac hN=\Gamma_{L,n}.
\]

For the reverse inequality, take a global extremizer \(A\subseteq[0,mN-1]\) and let
\[
h_i:=r_4(N)-|A_i|\ge0.
\]
The one-step identity in cardinality form is
\[
\sum_{i=0}^{m-1}h_i
=
mr_4(N)-r_4(mN)
=
mND_{L,n}.
\]
Thus
\[
\max_i h_i\le mND_{L,n}.
\]
The same extremizer fibers witness feasibility in the definition of \(H_{L,n}\) with \(h=\max_i h_i\). Therefore
\[
H_{L,n}\le mND_{L,n},
\]
which gives
\[
\Gamma_{L,n}\le mD_{L,n}.
\]

### D. Exact digit/carry form of the local gluing theorem

The quantity \(H_{L,n}\) is a finite 0-1 feasibility problem.

Let \(x_{i,u}=1_{B_i}(u)\). Every positive common difference has a unique decomposition
\[
d=qN+v,\qquad q\ge0,\quad 0\le v<N.
\]
For a starting point \(x=iN+u\), define, for \(t=0,1,2,3\),
\[
c_t=\left\lfloor\frac{u+tv}{N}\right\rfloor,
\qquad
w_t=u+tv-c_tN,
\qquad
b_t=i+tq+c_t.
\]
Then exactly
\[
x+td=b_tN+w_t.
\]

Therefore the glued set is 4-AP-free if and only if, for every choice with \(d>0\) and all \(b_t\in\{0,\dots,m-1\}\),
\[
x_{b_0,w_0}+x_{b_1,w_1}+x_{b_2,w_2}+x_{b_3,w_3}\le3.
\]
Validity automatically bounds \(q\) (in particular \(3q\le m-1\)), so this is finite for fixed \(L,n\).

Thus \(H_{L,n}\) is the least integer \(h\) for which the above carry constraints admit a binary solution satisfying
\[
\sum_{u=0}^{N-1}x_{i,u}\ge r_4(N)-h
\qquad\text{for every }i.
\]
This is an exact local formulation; it does not invoke any unpublished digit/carry return.

## Adversarial checks

1. **Average versus uniform.** At one level, uniform control is legitimate only because the \(m\) deficits are nonnegative and their sum is exactly \(mD_{L,n}\). At deeper levels I do not make that replacement; the result is only path/node concentration with the explicit bounds above.

2. **Direction of the gluing-radius inequalities.** A feasible uniformly near-extremal packet gives a lower bound on \(r_4(mN)\), hence an upper bound on \(D_{L,n}\), which yields \(D_{L,n}\le\Gamma_{L,n}\). A true global extremizer gives one feasible packet with maximum child deficit at most the sum of all deficits, yielding \(\Gamma_{L,n}\le mD_{L,n}\). The directions are not interchangeable.

3. **All cross-block progressions are represented.** The Euclidean decomposition \(d=qN+v\) and the carry formula reconstruct every term \(x+td\) exactly. Conversely every valid tuple in the displayed carry system is an ordinary integer 4-AP. No probabilistic or Fourier surrogate is used.

4. **Exact-extremizer incompatibility would be too weak by itself.** Merely proving \(H_{L,n}\ge1\) would give only
   \[
   D_{L,n}\ge \frac1{mN},
   \]
   an exponentially small scale decrement. The missing theorem needs a stability radius of order \(N a_n^{1+\theta}\), not just exclusion of perfect gluing.

5. **Small-scale zero-defect example.** Any universal positive gluing gap is false without an eventual-scale qualification. For \(n=2\), \(L=1\), \(N=4\), \(m=2\),
   \[
   r_4(4)=3.
   \]
   Take
   \[
   B_0=\{0,1,3\},\qquad B_1=\{0,2,3\}.
   \]
   Both are extremal in \([0,3]\), and the glued set
   \[
   \{0,1,3,4,6,7\}\subseteq[0,7]
   \]
   is 4-AP-free. For \(d=1\), every length-four window misses \(2\) or \(5\); for \(d=2\), the only candidates \(\{0,2,4,6\}\) and \(\{1,3,5,7\}\) miss \(2\) and \(5\), respectively. Hence
   \[
   H_{1,2}=0,\qquad \Gamma_{1,2}=0,\qquad D_{1,2}=0.
   \]
   This does not refute the promoted eventual density-loss route, but it rules out any scale-free claim that cross-block compatibility always forces a positive defect.

6. **Parent-theorem boundary.** No lower bound of the required order is proved for \(\Gamma_{L,n}\), so neither E3-Q4-DENSITY-LOSS, the dyadic extremal series, nor Erdős Problem 3 is certified here.

## First defect

The first genuinely arithmetic defect is now isolated exactly: the protected information supplies no lower bound of order
\[
\Gamma_{L,n}\gtrsim a_n^{1+\theta},\qquad \theta<1.
\]
Averaging and extremizer-tree concentration can force many near-extremal nodes when the total defect is already small, but they cannot by themselves show that a uniformly near-extremal sibling packet violates one of the finite digit/carry constraints. The missing content is therefore a quantitative **stability radius for cross-fiber compatibility**, not another averaging argument and not merely non-gluability of exact extremizers.

## Frontier effect

E3-Q4-DENSITY-LOSS is not closed, but it is reduced to one exact finite/local theorem.

For fixed \(L\), define the gluing radius \(\Gamma_{L,n}\) above. Then
\[
D_{L,n}\asymp_L \Gamma_{L,n}
\]
with explicit constants \(1\) and \(2^L\). Therefore it is sufficient and, up to that fixed factor, necessary to prove
\[
\Gamma_{L,n}\ge \kappa a_n^{1+\theta}
\]
eventually for some \(0<\theta<1\).

Equivalently: the frontier is now a finite carry-constrained near-extremizer feasibility problem asking how much uniform row slack is necessary before any compatible gluing exists. The extremizer-tree theorem additionally gives the exact multiscale consequence of small accumulated defect, with no unjustified uniformity upgrade.

## Next residual (maximum three sentences; evidence only)

The residual is to lower-bound the finite gluing radius \(\Gamma_{L,n}\) by \(\kappa a_n^{1+\theta}\) for one fixed \(L\) and some \(\theta<1\), using the explicit carry inequalities above. A proof only that \(\Gamma_{L,n}>0\) is quantitatively insufficient; the required stability radius is polynomial in the current extremal density. The small example \(\Gamma_{1,2}=0\) shows that any such theorem must be genuinely eventual or density-sensitive.

## Sources with exact primary-source identifiers/links used

No external primary mathematical source was used in the theorem-grade derivation above. All substantive claims were derived directly from the protected packet at commit 266b0857f3e13524ea9e69e2ef3bf4cd422503b5 and elementary arithmetic/combinatorial identities.