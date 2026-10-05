# E3-Q12 — positive-density de-windowed derivative-product overlap

Disposition: **PROVED_NATIVE_DEWINDOWED_DERIVATIVE_PRODUCT_OVERLAP**.

This is native GCL work. It refines the high-order arm of E3-Q10 while preserving the physical-fibre identity and the common derivative shift before any inverse theorem is applied.

## Strongest exact statement

Assume the hypotheses of E3-Q10 for one adjacent \`0011\` family. Its labelled physical pattern is

\[
(A,A,B,B).
\]

Let

\[
a:=1_A-\alpha 1_I
\]

be the de-windowed fluctuation of the first physical fibre in its local window, and let

\[
b:=1_B-\gamma1_J
\]

be the de-windowed fluctuation of the second physical fibre in its translated local window. Write also

\[
v_A:=\alpha1_I,\qquad v_B:=\gamma1_J.
\]

Let

\[
\delta_\beta:=\frac{\beta^4}{15\cdot16^4}.
\]

Suppose this adjacent family lies in the **high-order arm** of Q10. Thus for some

\[
S\subseteq\{0,1,2,3\},
\qquad |S|\ge3,
\]

the corresponding local-window expansion term \(T_S\) obeys

\[
|T_S|>\delta_\beta.
\]

Then one of the two physical fibres, call it \(X\), occurs in both positions of its repeated pair and hence contributes a complete multiplicative derivative. The other physical fibre, call it \(Y\), contributes a same-shift two-factor product containing **at least one de-windowed fluctuation**.

More precisely, there exist real functions

\[
x:=h_X,
\qquad
u_d(y):=g_0(y)g_1(y+d),
\]

where

\[
g_0,g_1\in\{h_Y,v_Y\}
\]

and at least one of \(g_0,g_1\) equals \(h_Y\), such that, after an affine relabelling of the progression variable,

\[
T_S
=
\mathbb E_{d\in G}
J_d,
\]

with

\[
J_d
:=
\mathbb E_{y\in G}
\Delta_d x(y)\,
u_d(y+2d),
\]

and

\[
\Delta_dx(y):=x(y)x(y+d).
\]

Let

\[
\sigma\in\{-1,+1\}
\]

be the sign of \(T_S\), and define

\[
D
:=
\left\{
d\in G:
\sigma J_d\ge\delta_\beta/2
\right\}.
\]

Then

\[
\boxed{
\frac{|D|}{P}
\ge
\frac{\delta_\beta/2}{1-\delta_\beta/2}
\ge
\frac{\delta_\beta}{2}.
}
\]

Hence

\[
\boxed{
|D|
\ge
\frac{\beta^4}{30\cdot16^4}\,P.
}
\]

For every \(d\in D\), normalized Fourier expansion gives the exact signed overlap identity

\[
J_d
=
\sum_{\xi\in G}
\widehat{\Delta_d x}(\xi)\,
\widehat{u_d}(-\xi)\,
e_P(-2\xi d),
\]

and therefore

\[
\boxed{
\operatorname{Re}\left[
\sigma
\sum_{\xi\in G}
\widehat{\Delta_d x}(\xi)\,
\widehat{u_d}(-\xi)\,
e_P(-2\xi d)
\right]
\ge
\frac{\delta_\beta}{2}.
}
\]

In particular,

\[
\boxed{
\sum_{\xi\in G}
\left|\widehat{\Delta_d x}(\xi)\right|
\left|\widehat{u_d}(-\xi)\right|
\ge
\frac{\delta_\beta}{2}.
}
\]

There are only two cases.

### Fully de-windowed fourfold case

If \(|S|=4\), then

\[
u_d=\Delta_d h_Y,
\]

up to the fixed translation of the second physical window. Thus Q12 gives a genuinely de-windowed derivative-spectrum overlap between the two adjacent physical fibres for a positive-density set of common shifts.

### Mixed triple-with-window case

If \(|S|=3\), then

\[
u_d(y)
=
h_Y(y)v_Y(y+d)
\]

or

\[
u_d(y)
=
v_Y(y)h_Y(y+d),
\]

again up to fixed translation.

Thus the only surviving window contamination is explicit and confined to one factor of the adjacent-fibre product. The other side is a complete derivative of a genuinely de-windowed physical fluctuation.

Consequently, in Q10's all-high-order regime across the three adjacent families

\[
(B_0,B_1),\qquad(B_1,B_2),\qquad(B_2,B_3),
\]

each adjacent pair carries a positive-density family of **same-shift derivative-product spectral overlaps** at scale \(\Omega(\beta^4)\).

This does not yet force coherent frequencies across shifts or across adjacent pairs.

## Proof

### 1. Every high-order term contains a complete repeated physical pair

The adjacent physical pattern is

\[
(A,A,B,B).
\]

If

\[
S\subseteq\{0,1,2,3\},
\qquad |S|\ge3,
\]

then by the pigeonhole principle either

\[
\{0,1\}\subseteq S
\]

or

\[
\{2,3\}\subseteq S.
\]

Therefore one physical fibre contributes de-windowed fluctuations in both of its repeated labelled positions.

The other physical fibre contributes at least one de-windowed fluctuation because \(|S|\ge3\).

### 2. Exact derivative-product representation

Suppose first that

\[
\{0,1\}\subseteq S.
\]

For the adjacent \`0011\` carry family, the first two labelled positions are the same physical fluctuation \(a\). The last two labelled factors are functions

\[
g_2,g_3\in\{b,v_B\},
\]

with at least one equal to \(b\).

Hence

\[
T_S
=
\mathbb E_{x,d}
a(x)a(x+d)
g_2(x+2d)g_3(x+3d).
\]

Define

\[
u_d(y):=g_2(y)g_3(y+d).
\]

Then

\[
T_S
=
\mathbb E_d
\mathbb E_x
\Delta_d a(x)\,u_d(x+2d).
\]

This is the desired form.

If instead

\[
\{2,3\}\subseteq S,
\]

set

\[
y=x+2d.
\]

Then the final repeated pair becomes a complete derivative of \(b\), while the first pair becomes a product of two functions chosen from \(\{a,v_A\}\), at least one of which is \(a\). Reversing the direction of \(d\), if necessary, puts the expression in the same displayed form.

No approximation is used.

### 3. Positive-density set of common shifts

Every factor in Q10 is bounded in magnitude by \(1\), so

\[
|J_d|\le1.
\]

Also

\[
T_S=\mathbb E_dJ_d
\]

is real because all functions are real-valued.

Choose \(\sigma\) so that

\[
\sigma T_S=|T_S|>\delta_\beta.
\]

Let

\[
p:=|D|/P.
\]

On \(D\),

\[
\sigma J_d\le1.
\]

Outside \(D\),

\[
\sigma J_d<\delta_\beta/2.
\]

Therefore

\[
\delta_\beta
<
\mathbb E_d\sigma J_d
\le
p+(1-p)\frac{\delta_\beta}{2}.
\]

Solving,

\[
p
>
\frac{\delta_\beta/2}{1-\delta_\beta/2}
\ge
\frac{\delta_\beta}{2}.
\]

This proves the shift-density bound.

### 4. Exact spectral overlap

Use normalized Fourier transform

\[
\widehat f(\xi)
=
\mathbb E_y f(y)e_P(-\xi y).
\]

For fixed \(d\),

\[
\Delta_dx(y)
=
\sum_\xi
\widehat{\Delta_dx}(\xi)e_P(\xi y)
\]

and

\[
u_d(y+2d)
=
\sum_\eta
\widehat{u_d}(\eta)
e_P(\eta y)e_P(2\eta d).
\]

Averaging over \(y\) enforces

\[
\eta=-\xi.
\]

Thus

\[
J_d
=
\sum_\xi
\widehat{\Delta_dx}(\xi)
\widehat{u_d}(-\xi)
e_P(-2\xi d).
\]

For \(d\in D\),

\[
\sigma J_d\ge\delta_\beta/2.
\]

Taking real parts gives the signed overlap statement, and taking absolute values termwise gives the unsigned overlap lower bound.

### 5. Identify the two possible adjacent-fibre products

If all four positions lie in \(S\), then both factors in the adjacent physical pair are de-windowed:

\[
u_d(y)=h_Y(y)h_Y(y+d)=\Delta_dh_Y(y).
\]

If exactly three positions lie in \(S\), the incomplete physical pair contributes one de-windowed factor and one deterministic local-window factor. Hence, depending on which labelled position is omitted,

\[
u_d(y)=h_Y(y)v_Y(y+d)
\]

or

\[
u_d(y)=v_Y(y)h_Y(y+d).
\]

These are the only possibilities.

## Relation to Q06

Q06 proved positive-density derivative spectral overlap for the globally centered Q04 fourfold branch.

Q12 removes the support-window ambiguity identified by Q09:

- in the fully de-windowed fourfold case, the Q06 mechanism now applies directly to intrinsic local fluctuations;
- in the mixed triple case, the exact remaining window factor is exposed rather than hidden inside a globally centered function.

Thus Q12 is a witness-preserving de-windowed interface.

## Claim boundary

Q12 does not prove:

- a single frequency \(\xi_d\) carries polynomial mass for each good shift;
- the selected frequencies form an additive/Freiman graph;
- the three adjacent pairs choose coherent frequency maps;
- the mixed triple-with-window branch can be discarded;
- or any deletion bound with exponent below \(2\).

The overlap may remain spectrally diffuse.

## First defect

The all-four de-windowed alignment residual reduces to:

> **E3-B-DEWINDOWED-DERIVATIVE-PRODUCT-ALIGNMENT.**
>
> Given three adjacent physical pairs, each carrying at least
> \[
> c\beta^4P
> \]
> common shifts with signed derivative-product spectral overlap at least
> \[
> c\beta^4,
> \]
> where the adjacent product is either a full de-windowed derivative or a one-window mixed derivative product, prove one of:
>
> 1. a coherent derivative-frequency graph aligns across enough shifts/pairs to integrate to a joint quadratic witness;
> 2. the mixed window branch forces a separate density increment / deletion cost;
> 3. spectral diffuseness itself forces
>    \[
>    \gtrsim\beta^{1+\theta}N
>    \]
>    deletions for some \(\theta<1\).

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\`: **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-ALLFIBRE-DEWINDOWED-ALIGNMENT\`: **REDUCED**.
- New lemma \`E3-B-DEWINDOWED-DERIVATIVE-PRODUCT-OVERLAP\`: **PROVED_NATIVE**.
- New smallest high-order residual: \`E3-B-DEWINDOWED-DERIVATIVE-PRODUCT-ALIGNMENT\`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q09 de-windowed local fluctuations.
- E3-Q10 high-order de-windowed correlation arm.
- E3-Q06 derivative-overlap mechanism.
