# E3-Q15 — forced derivative side in the repeated-triplet L01 core families

Disposition: **PROVED_NATIVE_REPEATED_TRIPLET_DERIVATIVE_FORCING**.

This is native GCL work. It extends the Q10/Q12 de-windowed order analysis from the adjacent \`0011\` \(2+2\) families to the three L01 core families whose physical block pattern is \(1+3\).

No inverse theorem and no external source is used.

## Strongest exact statement

Let
\[
N=2^n,\qquad n\ge4,
\]
and let
\[
B_0,B_1,B_2,B_3\subseteq[0,N-1]
\]
be the four physical fibres of a globally 4-AP-free four-fibre gluing, with
\[
|B_j|\ge\beta N\qquad(j=0,1,2,3).
\]

Use the three protected L01 core families
\[
F_2=(0,0,0111),\qquad
F_3=(1,0,0001),\qquad
F_6=(2,0,0001).
\]

Their physical block patterns are respectively
\[
F_2:(B_0,B_1,B_1,B_1),
\]
\[
F_3:(B_1,B_1,B_1,B_2),
\]
\[
F_6:(B_2,B_2,B_2,B_3).
\]

For one such family write, as in Q09,
\[
1_{C_t}=w_t+h_t,
\qquad
w_t=\alpha_t1_{I_t},
\]
and define
\[
\delta_\beta:=\frac{\beta^4}{15\cdot16^4}.
\]

Then each of \(F_2,F_3,F_6\) satisfies one of the following two alternatives.

### A. Low-order carry-kernel witness

There is a nonempty
\[
S\subseteq\{0,1,2,3\},
\qquad |S|\le2,
\]
whose local-window expansion term obeys
\[
|T_S|>\delta_\beta.
\]

For \(|S|=1\) or \(2\), exactly the same change-of-variables as in Q10 rewrites \(T_S\) as an explicit deterministic singleton or pair carry-kernel correlation of de-windowed physical fluctuations.

### B. Forced repeated-fibre derivative-product witness

There is
\[
S\subseteq\{0,1,2,3\},
\qquad |S|\ge3,
\]
with
\[
|T_S|>\delta_\beta.
\]

Let \(X\) be the physical fibre occurring three times in the family:
\[
X=B_1\quad\text{for }F_2,F_3,
\qquad
X=B_2\quad\text{for }F_6.
\]

Then two labelled positions belonging to \(X\) lie in \(S\). Hence there exist
\[
k\in\{1,2\},
\]
a de-windowed physical fluctuation \(x=h_X\), and a bounded two-factor product
\[
u_d(y)=g_0(y)g_1(y+\ell d),
\]
where every \(g_i\) is one of the appropriate local fluctuation/window factors and **at least one of \(g_0,g_1\) is a de-windowed fluctuation**, such that after affine relabelling
\[
T_S
=
\mathbb E_{d\in G}J_d,
\]
with
\[
J_d
=
\mathbb E_{y\in G}
\Delta_{kd}x(y)\,
u_d(y+\lambda d),
\]
for fixed integers \(\ell,\lambda\) with absolute value at most \(3\).

Here
\[
\Delta_{e}x(y):=x(y)x(y+e).
\]

Choosing the sign
\[
\sigma=\operatorname{sgn}(T_S)
\]
and
\[
D
=
\left\{
d:
\sigma J_d\ge\delta_\beta/2
\right\},
\]
one has
\[
\boxed{
|D|\ge\frac{\delta_\beta}{2}P.
}
\]

Since \(k\in\{1,2\}\) and \(P>3\) is prime, multiplication by \(k\) is a bijection of \(G\). Thus the corresponding derivative-shift set
\[
E:=kD
\]
also satisfies
\[
\boxed{
|E|\ge\frac{\delta_\beta}{2}P.
}
\]

For every \(d\in D\), Fourier expansion yields an exact spectral overlap
\[
J_d
=
\sum_{\xi\in G}
\widehat{\Delta_{kd}x}(\xi)
\widehat{u_d}(-\xi)
e_P(\mu\xi d)
\]
for a fixed integer \(\mu\), and therefore
\[
\boxed{
\sum_{\xi}
\left|\widehat{\Delta_{kd}x}(\xi)\right|
\left|\widehat{u_d}(-\xi)\right|
\ge
\delta_\beta/2.
}
\]

The derivative side is therefore **forced**:

- high-order \(F_2\) gives a positive-density derivative-product overlap family for \(B_1\);
- high-order \(F_3\) gives another positive-density derivative-product overlap family for the same physical fibre \(B_1\);
- high-order \(F_6\) gives one for \(B_2\).

Consequently, if all three repeated-triplet core families land in their high-order arms, the interior fibre \(B_1\) participates as the complete derivative side in two distinct carry geometries, one coupled toward \(B_0\) and one toward \(B_2\).

This is strictly stronger witness identity information than Q12's adjacent \(2+2\) statement, where either member of an adjacent pair may supply the complete derivative.

It does not yet force the two \(B_1\) good-shift sets to intersect or select coherent frequencies.

## Proof

### 1. Every repeated-triplet family has a large nonbaseline term

Q09 applies to every family in the ten-family L01 core.

For the chosen family,
\[
0
=
\Lambda(w_0,w_1,w_2,w_3)
+
\sum_{\varnothing\ne S\subseteq\{0,1,2,3\}}T_S,
\]
while
\[
\Lambda(w_0,w_1,w_2,w_3)
>
\frac{\beta^4}{16^4}.
\]

There are 15 nonbaseline terms, so at least one satisfies
\[
|T_S|>\delta_\beta.
\]

If \(|S|\le2\), alternative A holds.

Assume henceforth
\[
|S|\ge3.
\]

### 2. A high-order subset necessarily contains two repeated-fibre positions

Let
\[
R\subseteq\{0,1,2,3\}
\]
be the three labelled positions occupied by the triply repeated physical fibre \(X\).

There is exactly one labelled position outside \(R\).

Since
\[
|S|\ge3,
\]
one must have
\[
|S\cap R|\ge2.
\]

Choose
\[
p<q,\qquad p,q\in S\cap R.
\]

The separation is
\[
k:=q-p\in\{1,2\};
\]
the value \(3\) cannot occur between two positions from a three-position repeated block pattern in \(F_2,F_3,F_6\).

The two selected factors are translates of the same physical de-windowed fluctuation \(x=h_X\).

### 3. Exact derivative-product representation

Write the term as
\[
T_S
=
\mathbb E_{z,d}
\prod_{t=0}^3 f_t(z+td),
\]
where
\[
f_t=
\begin{cases}
h_t,&t\in S,\\
w_t,&t\notin S.
\end{cases}
\]

Set
\[
y=z+pd.
\]

The two selected repeated-fibre factors become
\[
x(y)x(y+kd)
=
\Delta_{kd}x(y).
\]

The two remaining labelled factors form a product
\[
u_d(y+\lambda d)
\]
after a fixed affine shift, with all offsets bounded by \(3\).

Because \(p,q\in S\), exactly two positions have already been extracted as fluctuations.

- If \(|S|=3\), exactly one of the two remaining factors is a fluctuation and the other is a window factor.
- If \(|S|=4\), both remaining factors are fluctuations.

Thus \(u_d\) always contains at least one genuine de-windowed fluctuation.

Therefore
\[
T_S
=
\mathbb E_d
\mathbb E_y
\Delta_{kd}x(y)u_d(y+\lambda d).
\]

No approximation is used.

### 4. Positive-density derivative shifts

Every local fluctuation/window factor is bounded by \(1\), hence
\[
|J_d|\le1.
\]

Choose
\[
\sigma T_S=|T_S|>\delta_\beta.
\]

Let
\[
p_D:=|D|/P.
\]

On \(D\),
\[
\sigma J_d\le1,
\]
and off \(D\),
\[
\sigma J_d<\delta_\beta/2.
\]

Thus
\[
\delta_\beta
<
\mathbb E_d\sigma J_d
\le
p_D+(1-p_D)\delta_\beta/2.
\]

Hence
\[
p_D
>
\frac{\delta_\beta/2}{1-\delta_\beta/2}
\ge
\delta_\beta/2.
\]

This proves
\[
|D|\ge(\delta_\beta/2)P.
\]

Since \(k=1\) or \(2\) and \(P\) is prime \(>3\), multiplication by \(k\) preserves cardinality, so the physical derivative-shift set \(E=kD\) has the same lower bound.

### 5. Exact Fourier overlap

For fixed \(d\), Fourier-expand
\[
\Delta_{kd}x(y)
\]
and
\[
u_d(y+\lambda d).
\]

Averaging over \(y\) enforces opposite frequencies. Hence
\[
J_d
=
\sum_\xi
\widehat{\Delta_{kd}x}(\xi)
\widehat{u_d}(-\xi)
e_P(-\lambda\xi d),
\]
up to the harmless sign convention induced by the affine relabelling.

For \(d\in D\),
\[
\sigma J_d\ge\delta_\beta/2.
\]

Taking absolute values termwise gives
\[
\sum_\xi
|\widehat{\Delta_{kd}x}(\xi)|
|\widehat{u_d}(-\xi)|
\ge
\delta_\beta/2.
\]

### 6. Identify the forced physical derivative fibres

From D01/L01:

\[
F_2=(0,0,0111)
\]
has physical pattern
\[
(B_0,B_1,B_1,B_1),
\]
so \(X=B_1\).

\[
F_3=(1,0,0001)
\]
has physical pattern
\[
(B_1,B_1,B_1,B_2),
\]
so again \(X=B_1\).

\[
F_6=(2,0,0001)
\]
has physical pattern
\[
(B_2,B_2,B_2,B_3),
\]
so \(X=B_2\).

Therefore high-order \(F_2\) and \(F_3\) constrain the derivative spectra of the **same interior physical fibre \(B_1\)** in two distinct carry families.

## Relation to Q10/Q12

Q10 retained the order of the de-windowed local-window expansion for the adjacent \(2+2\) families.

Q12 showed that a high-order adjacent \(2+2\) term contains a complete derivative, but the derivative side could be either physical fibre.

Q15 uses the \(1+3\) core families to remove that ambiguity:

> in every high-order repeated-triplet family, the triply repeated physical fibre is necessarily the complete derivative side.

This creates an explicit same-physical-fibre compatibility problem across \(F_2\) and \(F_3\).

## Claim boundary

Q15 does not prove:

- that the \(F_2\) and \(F_3\) good-shift sets intersect;
- that their derivative frequencies agree;
- that the two carry geometries integrate to one quadratic phase;
- that the low-order alternative has exponent below \(2\);
- or any deletion bound of order
  \[
  \beta^{1+\theta}N.
  \]

In particular, two subsets of \(G\) of density \(O(\beta^4)\) may be disjoint, so cardinality alone cannot align the \(F_2\) and \(F_3\) derivative shifts.

## First defect

The high-order residual reduces further to:

> **E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY.**
>
> In the regime where the repeated-triplet core families \(F_2,F_3\) are high-order, exploit the fact that both force positive-density derivative-product spectral overlaps with \(B_1\) as the complete derivative side, but in two different carry geometries. Prove that the resulting \(B_1\) derivative-shift/frequency systems either align to a common quadratic witness or their incompatibility forces a deletion cost with effective exponent below \(2\).

If either family instead lands in a low-order arm, it feeds the separate low-order exponent-upgrade residual.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\`: **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-DEWINDOWED-DERIVATIVE-PRODUCT-OVERLAP\`: remains **PROVED_NATIVE**.
- New lemma \`E3-B-REPEATED-TRIPLET-DERIVATIVE-FORCING\`: **PROVED_NATIVE**.
- \`E3-B-DEWINDOWED-DERIVATIVE-PRODUCT-ALIGNMENT\`: **REDUCED**.
- New high-order residual: \`E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY\`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-L01 ten-family core.
- E3-Q09 de-windowed local-window expansion.
- E3-Q10 order dichotomy.
- E3-Q12 derivative-product overlap mechanism.
