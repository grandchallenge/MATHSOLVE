# E3-Q14 — exact prime-lifted Fourier representation of carry-localized correlations

Disposition: **PROVED_NATIVE_CARRY_KERNEL_FOURIER_REPRESENTATION**.

This is native GCL work. It gives an exact harmonic representation for the Q12 carry-localized terms while preserving D01 family identity and retaining the prime ambient group used by protected Q02.

## Why the prime lift is necessary

The physical fibre length is
\[
N=2^n.
\]

Working directly on \(\mathbb Z_N\) gives a valid Fourier identity, but \(\mathbb Z_N\) has \(2\)-torsion. For labelled positions separated by \(2\), the equations
\[
\xi+\eta=0,\qquad
a\xi+b\eta=0
\]
can have nonzero torsion solutions. Therefore one must not silently import the prime-group Q04/Q02 frequency interpretation into \(\mathbb Z_N\).

Q14 instead uses the protected Q02 prime
\[
8N<P<16N.
\]

This keeps every coefficient \(1,2,3\) invertible and makes the unrestricted comparison exact.

## Setup

Fix one exact D01 family
\[
F=(i,q,c),
\qquad
c=(c_0,c_1,c_2,c_3),
\]
with exact carry cell
\[
\Omega_c(N)
\subseteq
[0,N-1]^2.
\]

Embed \([0,N-1]\) and \(\Omega_c(N)\) in
\[
G=\mathbb Z/P\mathbb Z,
\qquad
G^2.
\]

Define the prime-lifted carry kernel
\[
K_c(u,v):=1_{\Omega_c(N)}(u,v)
\]
on \(G^2\), extended by zero outside the integer cell.

For each physical fibre occurrence define
\[
H_t(x)
:=
\begin{cases}
1_{B_{j_t}}(x)-\alpha_t,&0\le x<N,\\
0,&\text{otherwise in }G,
\end{cases}
\]
where
\[
\alpha_t=\frac{|B_{j_t}|}{N}.
\]

Because
\[
\sum_{x=0}^{N-1}
(1_{B_{j_t}}(x)-\alpha_t)
=0,
\]
the zero-extended function still satisfies
\[
\widehat H_t(0)=0
\]
in \(G\).

Use normalized Fourier transforms
\[
\widehat H(\xi)
=
\mathbb E_{x\in G}
H(x)e_P(-\xi x),
\]
and
\[
\widehat K(a,b)
=
\mathbb E_{u,v\in G}
K(u,v)e_P(-au-bv),
\]
where
\[
e_P(x):=e^{2\pi i x/P}.
\]

## Exact representation theorem

For nonempty
\[
S\subseteq\{0,1,2,3\},
\]
define the prime-normalized carry-localized form
\[
\mathcal C_{c,S}
:=
\mathbb E_{u,v\in G}
K_c(u,v)
\prod_{t\in S}
H_t(u+tv-c_tN).
\]

Because \(K_c\) is supported on the exact D01 cell, every argument
\[
u+tv-c_tN
\]
lies in \([0,N-1]\), so this is exactly the desired integer residue evaluation.

Then

\[
\boxed{
\mathcal C_{c,S}
=
\sum_{(\xi_t)_{t\in S}}
\left(
\prod_{t\in S}\widehat H_t(\xi_t)
\right)
e_P\!\left(
-N\sum_{t\in S}c_t\xi_t
\right)
\widehat K_c
\left(
-\sum_{t\in S}\xi_t,\,
-\sum_{t\in S}t\xi_t
\right).
}
\]

The actual Q12 term is

\[
\boxed{
T_{F,S}^{\mathrm{loc}}
=
\left(\prod_{t\notin S}\alpha_t\right)
\frac{P^2}{N^2}
\mathcal C_{c,S}.
}
\]

Thus every family-specific Q12 witness is exactly a convolution of:
1. physical fibre spectra;
2. explicit carry-translation phases; and
3. the two-dimensional spectrum of the exact D01 carry-cell kernel.

## Proof

Fourier inversion gives
\[
H_t(u+tv-c_tN)
=
\sum_{\xi_t\in G}
\widehat H_t(\xi_t)
e_P\bigl(\xi_tu+t\xi_tv-c_tN\xi_t\bigr).
\]

Multiplying over \(t\in S\),
\[
\prod_{t\in S}H_t(u+tv-c_tN)
=
\sum_{(\xi_t)}
\left(\prod_{t\in S}\widehat H_t(\xi_t)\right)
e_P\!\left(
Au+Bv-N\sum_{t\in S}c_t\xi_t
\right),
\]
where
\[
A=\sum_{t\in S}\xi_t,
\qquad
B=\sum_{t\in S}t\xi_t.
\]

Average against \(K_c(u,v)\). By the Fourier convention,
\[
\mathbb E_{u,v}
K_c(u,v)e_P(Au+Bv)
=
\widehat K_c(-A,-B).
\]

This proves the prime-normalized identity.

Finally,
\[
\mathcal C_{c,S}
=
\frac1{P^2}
\sum_{(u,v)\in\Omega_c}
\prod_{t\in S}h_t(r_t(u,v)),
\]
whereas Q12 uses \(1/N^2\). Therefore
\[
T_{F,S}^{\mathrm{loc}}
=
\left(\prod_{t\notin S}\alpha_t\right)
\frac{P^2}{N^2}\mathcal C_{c,S}.
\]

## Unrestricted prime-group comparison

Replace \(K_c\) by the constant function \(1\) on \(G^2\).

Then
\[
\widehat K(a,b)=1_{(a,b)=(0,0)}.
\]

The only surviving tuples satisfy
\[
\sum_{t\in S}\xi_t=0,
\qquad
\sum_{t\in S}t\xi_t=0.
\]

Because \(P>3\) is prime, the coefficients \(1,2,3\) are invertible.

This exactly recovers the Q02/Q04 prime-group frequency algebra.

### Two fluctuations

For
\[
S=\{a,b\},
\qquad a\ne b,
\]
the two equations give
\[
\xi+\eta=0,
\qquad
a\xi+b\eta=0.
\]

Hence
\[
(a-b)\xi=0.
\]

Since
\[
0<|a-b|\le3<P,
\]
one gets
\[
\xi=\eta=0.
\]

But
\[
\widehat H_a(0)=\widehat H_b(0)=0.
\]

Therefore the unrestricted prime-group two-fluctuation average is exactly zero.

So every nonzero Q12 two-fluctuation localized correlation is **purely carry-kernel-specific**.

### Three fluctuations

For
\[
S=\{t_1<t_2<t_3\},
\]
the two equations leave a one-dimensional frequency family. Solving gives the familiar Q04 multipliers proportional to
\[
(t_2-t_3)r,\qquad
(t_3-t_1)r,\qquad
(t_1-t_2)r.
\]

Thus the unrestricted component of a localized three-fluctuation correlation is exactly an aligned Q04-type Fourier witness.

### Four fluctuations

For
\[
S=\{0,1,2,3\},
\]
the unrestricted component is the standard four-balanced prime-group 4-AP correlation.

The exact carry cell adds off-origin kernel modes to this universal component.

## Centered carry kernel

Let
\[
p_c^{(P)}
:=
\mathbb E_{G^2}K_c
=
\frac{|\Omega_c(N)|}{P^2},
\]
and define
\[
K_c^\circ
:=
K_c-p_c^{(P)}.
\]

Then
\[
\widehat K_c^\circ(0,0)=0,
\]
and
\[
K_c
=
p_c^{(P)}+K_c^\circ.
\]

Therefore every prime-normalized localized correlation splits exactly into

\[
\boxed{
\mathcal C_{c,S}
=
p_c^{(P)}
\Lambda_S^{\mathrm{prime}}
+
\mathcal R_{c,S},
}
\]
where
\[
\Lambda_S^{\mathrm{prime}}
:=
\mathbb E_{u,v\in G}
\prod_{t\in S}H_t(u+tv-c_tN)
\]
is the unrestricted prime-group component and
\[
\mathcal R_{c,S}
:=
\mathbb E_{u,v}
K_c^\circ(u,v)
\prod_{t\in S}H_t(u+tv-c_tN)
\]
is the genuinely family-specific centered-kernel remainder.

For \(|S|=1\) or \(2\),
\[
\Lambda_S^{\mathrm{prime}}=0
\]
because every \(H_t\) has zero mean and, in the two-factor case, the prime linear system has only the zero-frequency solution.

Hence singleton and two-fluctuation localized correlations are entirely carried by
\[
K_c^\circ.
\]

For \(|S|=3\) or \(4\), a large localized correlation must come from an unrestricted aligned prime-group witness, a carry-specific centered-kernel remainder, or both.

## Q11 recovered correctly

Q11's gauge equivalence occurs when one discards the exact carry-cell restriction and keeps only the unrestricted prime-group average.

In the decomposition above, that means retaining
\[
\Lambda_S^{\mathrm{prime}}
\]
and discarding
\[
\mathcal R_{c,S}.
\]

The family-specific information is therefore exactly the centered carry-kernel term.

This identifies the precise harmonic object that Q11 showed was missing.

## Prime-lifted kernel energy

Since
\[
K_c^2=K_c,
\]
prime-group Parseval gives
\[
\sum_{a,b\in G}
|\widehat K_c(a,b)|^2
=
p_c^{(P)}.
\]

The nonzero spectral energy is
\[
\sum_{(a,b)\ne(0,0)}
|\widehat K_c(a,b)|^2
=
p_c^{(P)}(1-p_c^{(P)}).
\]

Q15 proves, for every core carry and \(N\ge16\),
\[
|\Omega_c(N)|
\ge
\frac{21}{256}N^2.
\]

Since
\[
P<16N,
\]
\[
p_c^{(P)}
>
\frac{21}{65536}.
\]

Also
\[
p_c^{(P)}<\frac14.
\]

Therefore
\[
\boxed{
\sum_{(a,b)\ne(0,0)}
|\widehat K_c(a,b)|^2
>
\frac{63}{262144}.
}
\]

Thus the prime-lifted family-specific kernel has uniformly positive nonzero spectral energy.

## Consequence for the Q12 multi-fluctuation branch

Using the sharpened Q15 bound, Q12 supplies a localized term with
\[
|T_{F,S}^{\mathrm{loc}}|
\ge
\delta_\beta,
\qquad
\delta_\beta:=\frac{7}{1280}\beta^4.
\]

Therefore
\[
|\mathcal C_{c,S}|
\ge
\frac{N^2}{P^2}\delta_\beta.
\]

Because
\[
P<16N,
\]
\[
\boxed{
|\mathcal C_{c,S}|
>
\frac{\delta_\beta}{256}
=
\frac{7}{327680}\beta^4.
}
\]

If \(|S|=2\), this entire quantity is centered-kernel-specific.

If \(|S|=3\) or \(4\), the exact decomposition is
\[
\mathcal C_{c,S}
=
p_c^{(P)}\Lambda_S^{\mathrm{prime}}
+
\mathcal R_{c,S}.
\]

Thus either
\[
|p_c^{(P)}\Lambda_S^{\mathrm{prime}}|
\ge
\frac12|\mathcal C_{c,S}|
\]
or
\[
|\mathcal R_{c,S}|
\ge
\frac12|\mathcal C_{c,S}|.
\]

The first branch is an ordinary aligned prime-group Fourier/fourfold witness. The second is a genuinely carry-specific centered-kernel witness.

## Claim boundary

Q14 does not prove:
- that the centered-kernel remainder is incompatible with near-extremal fibres;
- concentration of \(\widehat K_c^\circ\) on useful frequencies;
- cross-family alignment;
- a deletion bound;
- or the four-fibre deficit theorem.

It is an exact representation and decomposition theorem.

## First defect

The localized multi-correlation branch reduces to:

> **E3-B-CENTERED-CARRY-KERNEL-INCOMPATIBILITY.**  
> For the Q14/Q15 core carry kernels, either amplify the unrestricted aligned prime-group branch into enough common physical Fourier/derivative witnesses, or show that the centered-kernel remainders
> \[
> \mathcal R_{c,S}
> \]
> of size \(\Omega(\beta^4)\) across the mandatory/core families cannot be supported by four near-extremal internally 4-AP-free fibres without
> \[
> \gtrsim\beta^{1+\theta}N
> \]
> deletions for some \(0<\theta<1\).

The immediate spectral question is the distribution of
\[
\widehat K_c^\circ(a,b)
\]
for the six core carries.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-CARRY-KERNEL-FOURIER-REPRESENTATION\`: **PROVED_NATIVE**, now explicitly prime-lifted.
- The localized multi-correlation branch reduces further to \`E3-B-CENTERED-CARRY-KERNEL-INCOMPATIBILITY\`.
- The Q13 density-increment branch remains open for amplification.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q02 prime cyclic embedding.
- E3-D01 exact carry compiler.
- E3-Q11 carry-gauge equivalence.
- E3-Q12 exact carry-localized cancellation.
- E3-Q15 exact carry-cell cardinalities.
