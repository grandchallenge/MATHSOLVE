# E3-Q14 — exact Fourier representation of carry-localized correlations

Disposition: **PROVED_NATIVE_CARRY_KERNEL_FOURIER_REPRESENTATION**.

This is native GCL work. It gives an exact harmonic representation for the Q12 carry-localized terms while preserving D01 family identity.

## Strongest exact statement

Fix one exact D01 family
\[
F=(i,q,c)
\]
with carry vector
\[
c=(c_0,c_1,c_2,c_3)
\]
and exact carry cell
\[
\Omega_c(N)
\subseteq
\mathbb Z_N^2.
\]

Let
\[
K_c(u,v):=1_{\Omega_c(N)}(u,v).
\]

For \(f:\mathbb Z_N\to\mathbb C\), use normalized Fourier transform
\[
\widehat f(\xi)
:=
\mathbb E_{x\in\mathbb Z_N}
f(x)e_N(-\xi x),
\qquad
e_N(x):=e^{2\pi i x/N}.
\]

For \(K:\mathbb Z_N^2\to\mathbb C\), use
\[
\widehat K(a,b)
:=
\mathbb E_{u,v\in\mathbb Z_N}
K(u,v)e_N(-au-bv).
\]

Let
\[
S\subseteq\{0,1,2,3\}
\]
be nonempty, and let \(h_t:\mathbb Z_N\to\mathbb C\) for \(t\in S\).

Define the exact carry-localized multilinear form
\[
\mathcal T_{c,S}(h)
:=
\frac1{N^2}
\sum_{(u,v)\in\Omega_c(N)}
\prod_{t\in S}
h_t(u+tv-c_tN).
\]

Because subtraction by \(c_tN\) is zero in \(\mathbb Z_N\),
\[
h_t(u+tv-c_tN)
=
h_t(u+tv).
\]

Then
\[
\boxed{
\mathcal T_{c,S}(h)
=
\sum_{(\xi_t)_{t\in S}}
\left(
\prod_{t\in S}\widehat h_t(\xi_t)
\right)
\widehat K_c
\left(
-\sum_{t\in S}\xi_t,\,
-\sum_{t\in S}t\xi_t
\right).
}
\]

For the actual Q12 term,
\[
T_{F,S}^{\mathrm{loc}}
=
\left(\prod_{t\notin S}\alpha_t\right)
\mathcal T_{c,S}(h).
\]

Thus every family-specific localized witness is encoded by the same physical one-dimensional Fourier coefficients together with the **two-dimensional Fourier kernel of the exact carry cell**.

## Proof

Fourier inversion gives
\[
h_t(u+tv)
=
\sum_{\xi_t\in\mathbb Z_N}
\widehat h_t(\xi_t)
e_N(\xi_tu+t\xi_tv).
\]

Multiplying over \(t\in S\),
\[
\prod_{t\in S}h_t(u+tv)
=
\sum_{(\xi_t)}
\left(\prod_{t\in S}\widehat h_t(\xi_t)\right)
e_N
\left(
\left(\sum_{t\in S}\xi_t\right)u
+
\left(\sum_{t\in S}t\xi_t\right)v
\right).
\]

Average against \(K_c(u,v)\):
\[
\mathcal T_{c,S}(h)
=
\sum_{(\xi_t)}
\left(\prod_{t\in S}\widehat h_t(\xi_t)\right)
\mathbb E_{u,v}
K_c(u,v)
e_N(Au+Bv),
\]
where
\[
A=\sum_{t\in S}\xi_t,
\qquad
B=\sum_{t\in S}t\xi_t.
\]

By the Fourier-transform convention,
\[
\mathbb E K_c(u,v)e_N(Au+Bv)
=
\widehat K_c(-A,-B).
\]

This proves the identity.

## Important special cases

### Singleton

For
\[
S=\{j\},
\]
\[
\mathcal T_{c,\{j\}}(h_j)
=
\sum_{\xi}
\widehat h_j(\xi)
\widehat K_c(-\xi,-j\xi).
\]

Because the locally centered fluctuation has
\[
\widehat h_j(0)=0,
\]
only nonzero frequencies contribute.

Thus the Q12 singleton geometry weight is exactly the inverse Fourier manifestation of the one-dimensional kernel slice
\[
\xi
\longmapsto
\widehat K_c(-\xi,-j\xi).
\]

Q13 attacks this branch in physical space via bounded variation and density increment.

### Two fluctuations

For
\[
S=\{a,b\},
\]
\[
\mathcal T_{c,\{a,b\}}
=
\sum_{\xi,\eta}
\widehat h_a(\xi)\widehat h_b(\eta)
\widehat K_c
\bigl(
-(\xi+\eta),
-(a\xi+b\eta)
\bigr).
\]

The unrestricted cyclic constraint
\[
\xi+\eta=0,
\qquad
a\xi+b\eta=0
\]
would force only the trivial solution when \(a\ne b\).

The exact carry kernel replaces that hard delta constraint by a nontrivial spectral weight. This is precisely where family-localized two-fibre interactions live.

### Three fluctuations

For
\[
S=\{a,b,c\},
\]
\[
\mathcal T_{c,S}
=
\sum_{\xi,\eta,\zeta}
\widehat h_a(\xi)
\widehat h_b(\eta)
\widehat h_c(\zeta)
\widehat K_c
\bigl(
-(\xi+\eta+\zeta),
-(a\xi+b\eta+c\zeta)
\bigr).
\]

When \(K_c\equiv1\), the kernel transform is supported only at
\[
(0,0),
\]
and the familiar Q04 aligned three-frequency relations reappear.

For a genuine carry cell, off-origin kernel spectrum allows controlled violations of the two exact frequency equations.

### Four fluctuations

For
\[
S=\{0,1,2,3\},
\]
\[
\mathcal T_{c,S}
=
\sum_{\xi_0,\xi_1,\xi_2,\xi_3}
\left(\prod_{t=0}^{3}\widehat h_t(\xi_t)\right)
\widehat K_c
\left(
-\sum_t\xi_t,
-\sum_tt\xi_t
\right).
\]

Again, the unrestricted cyclic model is recovered by replacing the carry kernel with the constant function.

## Q11 recovered exactly

If
\[
K_c\equiv1
\]
on all of \(\mathbb Z_N^2\), then
\[
\widehat K_c(a,b)
=
1_{(a,b)=(0,0)}.
\]

The Q14 formula collapses to the two hard equations
\[
\sum_{t\in S}\xi_t=0,
\qquad
\sum_{t\in S}t\xi_t=0.
\]

That quotient depends only on the physical labelled positions and forgets which integer carry cell generated them.

This is the harmonic form of Q11's coarse-step/carry gauge equivalence.

By contrast, the exact
\[
\widehat K_c(a,b)
\]
retains the D01 family.

## Parseval data for the carry kernel

Since
\[
K_c^2=K_c,
\]
two-dimensional Parseval gives
\[
\sum_{a,b\in\mathbb Z_N}
|\widehat K_c(a,b)|^2
=
\mathbb E_{u,v}K_c(u,v)
=
\frac{|\Omega_c(N)|}{N^2}.
\]

For every L01 core carry, Q09 gives
\[
\frac{|\Omega_c(N)|}{N^2}
\ge
\frac1{256}.
\]

Also
\[
\widehat K_c(0,0)
=
\frac{|\Omega_c(N)|}{N^2}.
\]

Thus the exact carry kernel has a quantitatively nontrivial \(L^2\) spectrum, and all family-specific information is contained in how that spectral mass is distributed away from the origin and along the linear slices sampled by Q14.

No useful lower bound on a specific nonzero kernel coefficient is claimed here.

## Why this is the right localized object

Q12 proves that some localized term has magnitude at least
\[
\frac{\beta^4}{3840}.
\]

Q14 rewrites that term exactly as
\[
\text{physical fibre spectra}
\quad\times\quad
\text{carry-cell spectral kernel}.
\]

Therefore the multi-correlation lane no longer requires an ad hoc localized inverse theorem as its first step.

The concrete missing question becomes:

> How can a polygonal D01 carry-cell kernel \(\widehat K_c\) support a \(\beta^4\)-scale localized correlation for many mandatory/core families when the physical fibres are all near-extremal and internally 4-AP-free?

This is both family-specific and compatible with the Q11 warning.

## Claim boundary

Q14 does not prove:
- concentration of \(\widehat K_c\) on any useful low-dimensional set;
- a large common physical Fourier coefficient;
- alignment of different carry kernels;
- a deletion bound;
- or the four-fibre deficit theorem.

It is an exact representation theorem.

## First defect

The localized multi-correlation branch reduces to:

> **E3-B-CARRY-KERNEL-SPECTRAL-INCOMPATIBILITY.**  
> Using the exact Q14 kernels \(\widehat K_c\) for the L01 core, prove that the Q12 localized correlations of size at least
> \[
> \beta^4/3840
> \]
> cannot all be supported by the spectra of four near-extremal internally 4-AP-free fibres unless one obtains either:
> 1. a Q13-type density increment that amplifies across scales; or
> 2. enough aligned nonzero fibre frequencies / derivative witnesses to force
> \[
> \gtrsim\beta^{1+\theta}N
> \]
> deletion cost for some \(0<\theta<1\).

The immediate next calculation is to determine the spectral geometry of the six distinct core carry kernels
\[
0000,\ 0001,\ 0011,\ 0111,\ 0112,\ 0123.
\]

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- New lemma \`E3-B-CARRY-KERNEL-FOURIER-REPRESENTATION\`: **PROVED_NATIVE**.
- The Q12 multi-correlation branch is reduced to \`E3-B-CARRY-KERNEL-SPECTRAL-INCOMPATIBILITY\`.
- The Q13 density-increment branch remains open for amplification.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-D01 exact carry compiler.
- E3-Q11 carry-gauge equivalence.
- E3-Q12 exact carry-localized cancellation.
- E3-Q13 carry-geometry density increment.
