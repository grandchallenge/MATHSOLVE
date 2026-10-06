# E3-Q16 — additive alignment of the repeated-triplet derivative-shift sets

Disposition: **PROVED_NATIVE_COMMON_DIFFERENCE_ALIGNMENT**.

This is native GCL work. It sharpens the high-order residual left by E3-Q15 using only elementary additive energy on the two positive-density derivative-shift sets forced for the same physical fibre \(B_1\). No external theorem is used.

## Strongest exact statement

Assume the high-order alternatives of both repeated-triplet core families
\[
F_2=(B_0,B_1,B_1,B_1),
\qquad
F_3=(B_1,B_1,B_1,B_2)
\]
from E3-Q15.

Let
\[
E_2,E_3\subseteq G=\mathbb Z/P\mathbb Z
\]
be the corresponding **physical derivative-shift sets** after Q15's \(k\in\{1,2\}\) reparameterization, so that both sets refer to complete multiplicative derivatives of the same de-windowed physical fluctuation
\[
b:=h_{B_1}.
\]

Write
\[
\delta_\beta:=\frac{\beta^4}{15\cdot16^4},
\qquad
\rho_\beta:=\frac{\delta_\beta}{2}
=
\frac{\beta^4}{30\cdot16^4}.
\]

Q15 gives
\[
|E_2|,\ |E_3|
\ge
\rho_\beta P.
\]

For a set \(E\subseteq G\), define
\[
r_E(h):=
|\{(e,e')\in E^2:e'-e=h\}|.
\]

Then the mixed additive energy identity gives
\[
\boxed{
\sum_{h\in G}r_{E_2}(h)r_{E_3}(h)
\ge
\frac{|E_2|^2|E_3|^2}{P}
\ge
\rho_\beta^4P^3.
}
\]

Consequently the common-difference support
\[
H:=
\{h\in G:r_{E_2}(h)>0,\ r_{E_3}(h)>0\}
\]
satisfies
\[
\boxed{
|H|
\ge
\frac{|E_2||E_3|}{P}
\ge
\rho_\beta^2P.
}
\]

Since \(0\in H\), the nonzero common-difference set
\[
H^\ast:=H\setminus\{0\}
\]
obeys
\[
\boxed{
|H^\ast|
\ge
\rho_\beta^2P-1.
}
\]

Thus for every
\[
h\in H^\ast
\]
there exist shifts
\[
e_2,e_2+h\in E_2,
\qquad
e_3,e_3+h\in E_3.
\]

Equivalently, Q15's two a priori unrelated \(B_1\) derivative-shift systems contain a family of **matched shift-parameter parallelograms**
\[
(e_2,e_2+h;\ e_3,e_3+h)
\]
for at least
\[
\rho_\beta^2P-1
=
\frac{\beta^8}{(30\cdot16^4)^2}P-1
\]
distinct nonzero increments \(h\).

Moreover, if
\[
\rho_\beta^2P\ge2,
\]
then the number of matched quadruples with nonzero common difference satisfies
\[
\boxed{
\sum_{h\ne0}r_{E_2}(h)r_{E_3}(h)
\ge
\frac12\rho_\beta^4P^3.
}
\]

In particular, for some **single nonzero** common difference \(h_\ast\),
\[
\boxed{
r_{E_2}(h_\ast),\ r_{E_3}(h_\ast)
\ge
\frac12\rho_\beta^3P.
}
\]

Thus one may freeze a common increment \(h_\ast\ne0\) and retain at least
\[
\frac12\rho_\beta^3P
=
\Omega(\beta^{12}P)
\]
starting shifts in **each** carry geometry.

In the asymptotic near-extremal campaign regime the auxiliary size condition holds eventually.

This does **not** yet align the Fourier frequencies selected inside the derivative-product overlaps. It replaces the raw shift-intersection problem by an additive shift-parameter compatibility problem on a positive-density family of matched differences.

## Proof

### 1. Mixed additive energy

Put
\[
A:=E_2,\qquad B:=E_3.
\]

Let
\[
r_{A-B}(x)
:=
|\{(a,b)\in A\times B:a-b=x\}|.
\]

Then
\[
\sum_x r_{A-B}(x)=|A||B|.
\]

By Cauchy-Schwarz over the \(P\) possible differences,
\[
\sum_x r_{A-B}(x)^2
\ge
\frac{|A|^2|B|^2}{P}.
\]

The exact double-counting identity is
\[
\sum_x r_{A-B}(x)^2
=
\sum_h r_A(h)r_B(h).
\]

Indeed both sides count quadruples
\[
(a,a',b,b')\in A^2\times B^2
\]
with
\[
a-b=a'-b',
\]
equivalently
\[
a'-a=b'-b.
\]

Therefore
\[
\sum_h r_A(h)r_B(h)
\ge
\frac{|A|^2|B|^2}{P}.
\]

Using
\[
|A|,|B|\ge\rho_\beta P
\]
gives
\[
\sum_h r_A(h)r_B(h)
\ge
\rho_\beta^4P^3.
\]

### 2. Common-difference support

For every \(h\),
\[
r_A(h)\le|A|,
\qquad
r_B(h)\le|B|.
\]

Hence
\[
r_A(h)r_B(h)\le|A||B|.
\]

Only \(h\in H\) contribute to the mixed energy, so
\[
\frac{|A|^2|B|^2}{P}
\le
\sum_h r_A(h)r_B(h)
\le
|H|\,|A||B|.
\]

Canceling \(|A||B|>0\),
\[
|H|
\ge
\frac{|A||B|}{P}
\ge
\rho_\beta^2P.
\]

Since \(r_A(0)=|A|\) and \(r_B(0)=|B|\), one has \(0\in H\). Therefore
\[
|H^\ast|
\ge
\rho_\beta^2P-1.
\]

For every \(h\in H^\ast\), positivity of both representation functions gives
\[
e_2,e_2+h\in E_2
\]
and
\[
e_3,e_3+h\in E_3
\]
for suitable \(e_2,e_3\).

### 3. Nonzero matched-quadruple count and a popular common difference

The \(h=0\) contribution is exactly
\[
r_A(0)r_B(0)=|A||B|.
\]

Thus
\[
\sum_{h\ne0}r_A(h)r_B(h)
\ge
\frac{|A|^2|B|^2}{P}-|A||B|.
\]

Put
\[
X:=|A||B|.
\]

Then
\[
\frac{X^2}{P}-X
=
\frac{X^2}{P}\left(1-\frac{P}{X}\right).
\]

Since
\[
X\ge\rho_\beta^2P^2,
\]
the condition
\[
\rho_\beta^2P\ge2
\]
implies
\[
X/P\ge2
\]
and hence
\[
1-\frac{P}{X}\ge\frac12.
\]

Therefore
\[
\sum_{h\ne0}r_A(h)r_B(h)
\ge
\frac{X^2}{2P}
\ge
\frac12\rho_\beta^4P^3.
\]

Averaging over the at most \(P-1\) nonzero differences, there exists
\[
h_\ast\ne0
\]
with
\[
r_A(h_\ast)r_B(h_\ast)
\ge
\frac{X^2}{2P^2}.
\]

Since
\[
r_A(h_\ast)\le |A|,
\qquad
r_B(h_\ast)\le |B|,
\]
we obtain separately
\[
r_A(h_\ast)
\ge
\frac{X^2}{2P^2|B|}
=
\frac{|A|^2|B|}{2P^2}
\ge
\frac12\rho_\beta^3P,
\]
and symmetrically
\[
r_B(h_\ast)
\ge
\frac12\rho_\beta^3P.
\]

### 4. Eventual applicability

Protected E3-A03 gives
\[
a_n\ge2^{-(C_\ast+o(1))\sqrt n}.
\]

In the near-extremal contradiction regime used throughout tranche 04 one may take
\[
\beta\ge\frac12a_n.
\]

The cyclic embedding has
\[
P>8N,
\qquad N=2^n.
\]

Hence
\[
P\rho_\beta^2
\asymp
P\beta^8
\ge
2^{\,n-O(\sqrt n)}
\to\infty.
\]

So
\[
\rho_\beta^2P\ge2
\]
eventually.

## What this changes

Q15 explicitly warned that the two good-shift sets for \(F_2\) and \(F_3\) need not intersect because each has density only \(O(\beta^4)\).

Q16 shows that direct intersection is the wrong additive object to demand.

Even if
\[
E_2\cap E_3=\varnothing,
\]
the two sets necessarily have many matched **difference increments**:
\[
|(E_2-E_2)\cap(E_3-E_3)|
\ge
\rho_\beta^2P
\]
in the representation-support sense proved above. Eventually one may moreover freeze a single nonzero common increment \(h_\ast\) with \(\Omega(\rho_\beta^3P)\) representations in each system.

Thus the same physical fibre \(B_1\) is constrained at four derivative parameters
\[
e_2,\ e_2+h_\ast,\ e_3,\ e_3+h_\ast
\]
for many choices of \(e_2,e_3\).

This creates a concrete additive compatibility object on which to compare the Q15 derivative spectra.

## Claim boundary

Q16 does not prove:

- that \(E_2\cap E_3\ne\varnothing\);
- that the Fourier frequencies selected by Q15 agree at \(e_2\) and \(e_3\);
- that frequencies are transported coherently when a shift parameter is changed by \(h_\ast\);
- that the matched-difference configurations integrate to a common quadratic phase;
- or any deletion bound with effective exponent below \(2\).

The exponent in the common-difference density is currently
\[
\rho_\beta^2\asymp\beta^8,
\]
so cardinality alone is quantitatively insufficient.

## First defect

The high-order residual reduces from raw shift-set compatibility to:

> **E3-B-INTERIOR-DERIVATIVE-DIFFERENCE-COMPATIBILITY.**
>
> For the positive-density family of nonzero increments \(h\) supplied by Q16—and in particular for a popular fixed increment \(h_\ast\)—compare the derivative spectra of the same physical fluctuation \(B_1\) at
> \[
> e_2,\ e_2+h_\ast
> \]
> in the \(F_2\) carry geometry and at
> \[
> e_3,\ e_3+h_\ast
> \]
> in the \(F_3\) carry geometry.
>
> Prove either:
> 1. coherent frequency transport across enough matched differences, yielding a joint quadratic witness; or
> 2. failure of such transport forces a deletion/density-increment cost with effective exponent \(p<2\).

This is strictly narrower than E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY because common shift-parameter increments are now guaranteed.

## Frontier effect

- \`E3-Q4-DENSITY-LOSS\`: **OPEN**.
- \`E3-B-FOUR-FIBRE-DEFICIT\`: **OPEN_NATIVE_SUBTARGET**.
- \`E3-B-REPEATED-TRIPLET-DERIVATIVE-FORCING\`: remains **PROVED_NATIVE**.
- New lemma \`E3-B-INTERIOR-DERIVATIVE-COMMON-DIFFERENCES\`: **PROVED_NATIVE**.
- \`E3-B-INTERIOR-DERIVATIVE-COMPATIBILITY\`: **REDUCED**.
- New smallest high-order residual: \`E3-B-INTERIOR-DERIVATIVE-DIFFERENCE-COMPATIBILITY\`.
- No parent theorem or gluing-radius candidate is promoted.

## Protected basis

- E3-Q15 repeated-triplet derivative forcing.
- E3-A03 pointwise lower construction, used only for eventual applicability of the auxiliary size condition.
