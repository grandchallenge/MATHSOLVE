# E3-Q16 — intrinsic carry-shape de-windowing

Disposition: **PROVED_NATIVE_CARRY_KERNEL_DEWINDOWING**.

This is native GCL work. It refines the corrected prime-lifted Q14 representation by separating:

1. the unrestricted prime-group component;
2. the common parameter-square window;
3. the intrinsic shape of the exact D01 carry cell inside that square.

The purpose is to avoid attributing deterministic parameter-window structure to family-specific carry geometry.

## Setup

Let
\[
G=\mathbb Z/P\mathbb Z,
\qquad
8N<P<16N,
\]
and let
\[
S_N(u,v)
:=
1_{[0,N-1]^2}(u,v)
\]
be the common parameter-square indicator embedded in \(G^2\).

For one D01 carry cell define
\[
K_c:=1_{\Omega_c(N)}.
\]

Let
\[
\rho_c
:=
\frac{|\Omega_c(N)|}{N^2}
\]
be the density of the carry cell **inside the parameter square**, and let
\[
q_N
:=
\frac{N^2}{P^2}
=
\mathbb E_{G^2}S_N.
\]

Then
\[
\mathbb E_{G^2}K_c
=
\rho_cq_N.
\]

Define the **intrinsic carry-shape fluctuation**
\[
L_c
:=
K_c-\rho_cS_N.
\]

## Strongest exact statement

The carry kernel has the exact three-level decomposition

\[
\boxed{
K_c
=
\rho_cq_N
+
\rho_c(S_N-q_N)
+
L_c.
}
\]

Here:

- \(\rho_cq_N\) is the full-group constant component;
- \(\rho_c(S_N-q_N)\) is the common parameter-square window component;
- \(L_c\) is the intrinsic carry-shape component.

Moreover,

\[
\boxed{
\mathbb E_{G^2}L_c=0.
}
\]

The \(L^2\) energy of the intrinsic carry-shape component is exactly

\[
\boxed{
\mathbb E_{G^2}|L_c|^2
=
q_N\rho_c(1-\rho_c).
}
\]

For every L01 core carry and every dyadic
\[
N\ge16,
\]
protected Q15 gives
\[
\rho_c\ge\frac{21}{256},
\qquad
\rho_c<\frac14.
\]

Since
\[
P<16N,
\]
\[
q_N>\frac1{256}.
\]

Therefore

\[
\boxed{
\mathbb E|L_c|^2
>
\frac{63}{262144}.
}
\]

Thus the intrinsic carry-cell shape retains uniformly positive energy even after the common parameter-square window is removed.

## Fourier form

Let
\[
\widehat S_N(a,b),
\qquad
\widehat K_c(a,b),
\qquad
\widehat L_c(a,b)
\]
denote normalized \(G^2\) Fourier transforms.

Then

\[
\boxed{
\widehat L_c(a,b)
=
\widehat K_c(a,b)
-
\rho_c\widehat S_N(a,b).
}
\]

Because
\[
\widehat L_c(0,0)=0,
\]
all intrinsic carry-shape energy lies at nonzero frequencies:

\[
\boxed{
\sum_{(a,b)\ne(0,0)}
|\widehat L_c(a,b)|^2
=
q_N\rho_c(1-\rho_c)
>
\frac{63}{262144}.
}
\]

This is stronger conceptually than the centered-full-group kernel
\[
K_c-\mathbb EK_c,
\]
because the latter still contains the deterministic square-window fluctuation
\[
\rho_c(S_N-q_N).
\]

## Proof of the energy identity

Inside the parameter square \(S_N=1\),

\[
L_c
=
\begin{cases}
1-\rho_c,&(u,v)\in\Omega_c,\\
-\rho_c,&(u,v)\in[0,N-1]^2\setminus\Omega_c.
\end{cases}
\]

Outside the square,
\[
L_c=0.
\]

Hence

\[
\mathbb E|L_c|^2
=
\frac1{P^2}
\left(
|\Omega_c|(1-\rho_c)^2
+
(N^2-|\Omega_c|)\rho_c^2
\right).
\]

Since
\[
|\Omega_c|=\rho_cN^2,
\]
this becomes

\[
\frac{N^2}{P^2}
\left(
\rho_c(1-\rho_c)^2
+
(1-\rho_c)\rho_c^2
\right)
=
q_N\rho_c(1-\rho_c).
\]

The mean is

\[
\mathbb EL_c
=
\frac{|\Omega_c|-\rho_cN^2}{P^2}
=0.
\]

Parseval gives the Fourier-energy statement.

## Exact partition relation

The eight D01 carry cells partition the parameter square:

\[
\sum_{c\in\mathcal C_8}K_c
=
S_N,
\]
where
\[
\mathcal C_8
=
\{
0000,0001,0011,0012,
0111,0112,0122,0123
\}.
\]

Also

\[
\sum_{c\in\mathcal C_8}\rho_c=1.
\]

Therefore

\[
\boxed{
\sum_{c\in\mathcal C_8}L_c=0
}
\]
pointwise, and hence

\[
\boxed{
\sum_{c\in\mathcal C_8}\widehat L_c(a,b)=0
}
\]
at every frequency.

Thus the eight intrinsic carry-shape spectra satisfy an exact family-coupling relation.

The six L01 core carries omit only
\[
0012,\qquad0122.
\]

Hence the sum of the six core intrinsic kernels is exactly

\[
-\bigl(L_{0012}+L_{0122}\bigr).
\]

This is a concrete cross-family identity unavailable in the unrestricted cyclic quotient.

## Three-way decomposition of Q14 correlations

Use the prime-lifted Q14 notation.

For one selected factor set \(S\), define

\[
g_S(u,v)
:=
\prod_{t\in S}
H_t(u+tv-c_tN).
\]

Then

\[
\mathcal C_{c,S}
=
\mathbb E K_cg_S.
\]

Substitute the three-level kernel decomposition:

\[
\boxed{
\mathcal C_{c,S}
=
\rho_cq_N\Lambda_S^{\mathrm{prime}}
+
\rho_c\mathcal W_S
+
\mathcal I_{c,S},
}
\]

where

\[
\Lambda_S^{\mathrm{prime}}
:=
\mathbb Eg_S,
\]

\[
\mathcal W_S
:=
\mathbb E(S_N-q_N)g_S,
\]

and

\[
\mathcal I_{c,S}
:=
\mathbb EL_cg_S.
\]

Interpretation:

- \(\Lambda_S^{\mathrm{prime}}\): universal prime-group aligned component;
- \(\mathcal W_S\): common parameter-square window component;
- \(\mathcal I_{c,S}\): intrinsic carry-shape component.

The only cell-specific spectral kernel in the final term is
\[
L_c.
\]

## Quantitative trichotomy

Q15 sharpens Q12 to

\[
|T_{F,S}^{\mathrm{loc}}|
\ge
\delta_\beta,
\qquad
\delta_\beta:=\frac{7}{1280}\beta^4.
\]

Corrected Q14 gives

\[
|\mathcal C_{c,S}|
\ge
\frac{N^2}{P^2}\delta_\beta
>
\frac{\delta_\beta}{256}.
\]

Hence

\[
|\mathcal C_{c,S}|
>
\frac{7}{327680}\beta^4.
\]

From the exact three-way decomposition, at least one of

\[
|\rho_cq_N\Lambda_S^{\mathrm{prime}}|,
\qquad
|\rho_c\mathcal W_S|,
\qquad
|\mathcal I_{c,S}|
\]

is at least one third of this:

\[
\boxed{
\max\{
|\rho_cq_N\Lambda_S^{\mathrm{prime}}|,
|\rho_c\mathcal W_S|,
|\mathcal I_{c,S}|
\}
>
\frac{7}{983040}\beta^4.
}
\]

Thus every large localized Q12/Q15 multi-correlation yields at least one of three exact witness types:

1. **aligned prime witness**;
2. **parameter-window witness**;
3. **intrinsic carry-shape witness**.

## Relation to Q09

Q09 showed that globally centered fibre structure can be contaminated by the physical support window.

Q16 is the exact parameter-space analogue:

> A centered carry kernel can be contaminated by the common parameter-square support window.

Therefore future spectral arguments must distinguish
\[
S_N-q_N
\]
from
\[
L_c.
\]

Only \(L_c\) represents the internal geometry of the D01 carry cell.

## Claim boundary

Q16 does not prove:
- that the parameter-window branch is impossible;
- that the intrinsic carry-shape branch aligns across families;
- concentration of \(\widehat L_c\);
- a deletion bound;
- or the four-fibre deficit theorem.

It is an exact de-windowing and trichotomy theorem.

## First defect

The corrected kernel lane reduces to two smaller residuals in addition to the already named aligned-prime branch:

> **E3-B-PARAMETER-WINDOW-INCOMPATIBILITY.**  
> Show that the common square-window terms \(\mathcal W_S\), together with the family-specific carry translations, cannot support all required localized correlations for four near-extremal internally 4-AP-free fibres without the target deletion cost.

and

> **E3-B-INTRINSIC-CARRY-SHAPE-INCOMPATIBILITY.**  
> Use the uniformly nonzero intrinsic spectra \(\widehat L_c\), their exact eight-cell sum-to-zero relation, and the L01 core structure to force aligned fibre witnesses or the target deletion cost.

The latter is now the genuinely carry-geometric spectral problem.

## Frontier effect

- New lemma \`E3-B-CARRY-KERNEL-DEWINDOWING\`: **PROVED_NATIVE**.
- \`E3-B-CENTERED-CARRY-KERNEL-INCOMPATIBILITY\`: **REDUCED**.
- New residuals:
  - \`E3-B-PARAMETER-WINDOW-INCOMPATIBILITY\`;
  - \`E3-B-INTRINSIC-CARRY-SHAPE-INCOMPATIBILITY\`.
- The existing \`E3-B-PRIME-ALIGNED-WITNESS-AMPLIFICATION\` branch remains open.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q14 corrected prime-lifted carry-kernel Fourier representation.
- E3-Q15 exact carry-cell cardinalities.
