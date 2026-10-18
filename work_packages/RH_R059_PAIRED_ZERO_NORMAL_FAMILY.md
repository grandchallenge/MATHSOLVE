# RH-R059-PAIRED-ZERO-NORMAL-FAMILY-001

Campaign: RH-001

Route: Forward Route C, obligation C4

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#714

Protected Solve base:
grandchallenge/MATHSOLVE@0bd614f27b22c3a5350347cbda51b0267ddf29ec

Protected dependencies:
- grandchallenge/MATHSOLVE@0bd614f27b22c3a5350347cbda51b0267ddf29ec:work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@0bd614f27b22c3a5350347cbda51b0267ddf29ec:work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- grandchallenge/MATHSOLVE@0bd614f27b22c3a5350347cbda51b0267ddf29ec:work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- grandchallenge/MATHFORGE@a900e5170c6d77a9e557b6159cf5feb40bcee222:
  reports/discovery/rh_001/rh_r056_determinant_normalization.md

Exact algebraic replay:
scripts/rh_r059_normal_family_check.py

No determinant-convergence / cofinal simple-evenness / RH / novelty / priority /
publication-readiness / certification claim.

## 1. Purpose

Protected RH-R056 fixes, on every admitted finite CCM pair, one even entire
function \(F_{\lambda,N}\) with

\[
F_{\lambda,N}(i/2)=\frac12
\]

and exactly the same zero multiset as the source regularized determinant.
Every such finite zero is real.

Those facts do **not** imply that a varying family is locally bounded. C4
therefore needs a genuinely uniform growth input before Montel can be used.

This package proves two complementary statements.

1. Evenness, real zeros, and the R056 anchor alone are insufficient for local
   boundedness.
2. A uniform bound on one paired reciprocal-square zero energy is sufficient
   for an explicit compact-disc bound, hence for normality.

For the admitted CCM finite family, the zero energy becomes an exact spectral
resolvent sum. Thus R059 converts the vague C4 requirement "prove local
boundedness" into one concrete quantitative target.

## 2. R056 properties alone are insufficient

Fix the protected anchor

\[
\eta=\frac12,\qquad c=\frac12.
\]

For \(n\ge1\), define

\[
F_n(z)
=
\frac12
\left(
\frac{1-z^2}{1+\eta^2}
\right)^n
=
\frac12
\left(
\frac{4(1-z^2)}5
\right)^n.
\]

Then every \(F_n\) is an even entire function. Its only zeros are

\[
z=\pm1,
\]

each with multiplicity \(n\), so all zeros are real. At the fixed nonreal
anchor,

\[
F_n(i/2)
=
\frac12
\left(
\frac{1+1/4}{1+1/4}
\right)^n
=
\frac12.
\]

Nevertheless, at \(z=2\),

\[
|F_n(2)|
=
\frac12
\left(\frac{12}{5}\right)^n
\longrightarrow\infty.
\]

Hence the family is not locally bounded at \(2\). Therefore the R056
properties alone do not supply the local-boundedness hypothesis required by
the planned Montel route.

### Consequence

The following data, by themselves, cannot discharge C4:

- entire;
- even;
- only real zeros;
- fixed value \(F(i/2)=1/2\).

Any valid C4 theorem needs an additional **uniform** input.

## 3. Paired Hadamard factorization

Let \(F\not\equiv0\) be an even entire function of order at most one, with
only real zeros, and assume

\[
F(i\eta)=c\ne0
\qquad(\eta>0).
\]

Let the zero at the origin have multiplicity \(2m_0\). Enumerate the positive
nonzero zeros as \(x>0\), with multiplicities \(m_x\). Evenness gives the
same multiplicity at \(-x\).

By the standard Hadamard factorization theorem for an entire function of order
at most one,

\[
F(z)
=
z^{2m_0}e^{az+b}
\prod_{x>0}
\left[
E_1\!\left(\frac z x\right)
E_1\!\left(-\frac z x\right)
\right]^{m_x},
\]

where

\[
E_1(w)=(1-w)e^w.
\]

The paired primary factors satisfy exactly

\[
E_1(z/x)E_1(-z/x)
=
1-\frac{z^2}{x^2}.
\]

Thus

\[
F(z)
=
z^{2m_0}e^{az+b}
\prod_{x>0}
\left(1-\frac{z^2}{x^2}\right)^{m_x}.
\]

The product apart from \(e^{az+b}\) is even. Since \(F\) is even,

\[
e^{-az+b}=e^{az+b}
\]

where the product is nonzero, hence by analyticity

\[
e^{-2az}\equiv1.
\]

Therefore

\[
a=0.
\]

So the only residual zero-free factor is a nonzero constant:

\[
\boxed{
F(z)
=
C\,z^{2m_0}
\prod_{x>0}
\left(1-\frac{z^2}{x^2}\right)^{m_x},
\qquad C\ne0.
}
\]

Because \(F\) has order at most one, the paired product converges locally
uniformly; in particular

\[
\sum_{x>0}\frac{m_x}{x^2}<\infty.
\]

Dividing by the nonzero anchor value gives the exact normalized product

\[
\boxed{
\frac{F(z)}{c}
=
\left(\frac{z}{i\eta}\right)^{2m_0}
\prod_{x>0}
\left(
\frac{1-z^2/x^2}{1+\eta^2/x^2}
\right)^{m_x}.
}
\]

## 4. Paired zero energy

Define

\[
\boxed{
Q_\eta(F)
:=
\frac{m_0}{\eta^2}
+
\sum_{x>0}
\frac{m_x}{x^2+\eta^2}.
}
\]

The sum is finite for every individual \(F\) in Section 3.

The quantity is designed to control the normalized product directly at the
anchor \(i\eta\).

## 5. Explicit compact-disc bound

### Theorem 5.1 — zero-energy local bound

Fix \(\eta>0\), \(c\ne0\), and \(C_Q<\infty\). Let \(\mathcal F\) be any
family of even entire functions of order at most one, all of whose zeros are
real, such that

\[
F(i\eta)=c
\]

and

\[
Q_\eta(F)\le C_Q
\]

for every \(F\in\mathcal F\).

Then for every \(R>0\),

\[
\boxed{
\sup_{\substack{F\in\mathcal F\\ |z|\le R}}
|F(z)|
\le
|c|
\exp\!\left(
2\eta^2C_Q\log_+\frac R\eta
+
(R^2-\eta^2)_+C_Q
\right),
}
\]

where

\[
\log_+u:=\max(\log u,0),
\qquad
v_+:=\max(v,0).
\]

#### Proof

Use the normalized product from Section 3.

For a positive zero \(x\) and \(|z|\le R\),

\[
\left|
\frac{1-z^2/x^2}{1+\eta^2/x^2}
\right|
=
\frac{|x^2-z^2|}{x^2+\eta^2}
\le
\frac{x^2+R^2}{x^2+\eta^2}.
\]

If \(R\le\eta\), the last ratio is at most \(1\). If \(R>\eta\),

\[
\frac{x^2+R^2}{x^2+\eta^2}
=
1+
\frac{R^2-\eta^2}{x^2+\eta^2}
\le
\exp\!\left(
\frac{R^2-\eta^2}{x^2+\eta^2}
\right).
\]

Therefore, in both cases,

\[
\left|
\frac{1-z^2/x^2}{1+\eta^2/x^2}
\right|^{m_x}
\le
\exp\!\left(
\frac{m_x(R^2-\eta^2)_+}{x^2+\eta^2}
\right).
\]

For the zero at the origin,

\[
\left|
\frac{z}{i\eta}
\right|^{2m_0}
\le1
\]

when \(R\le\eta\). When \(R>\eta\),

\[
\left|
\frac{z}{i\eta}
\right|^{2m_0}
\le
\exp\!\left(
2m_0\log\frac R\eta
\right).
\]

Since

\[
\frac{m_0}{\eta^2}\le Q_\eta(F)\le C_Q,
\]

we have

\[
m_0\le\eta^2C_Q.
\]

Multiplying the partial-product estimates, using

\[
\sum_{x>0}\frac{m_x}{x^2+\eta^2}
\le
Q_\eta(F)
\le C_Q,
\]

and then passing to the locally uniform product limit gives

\[
|F(z)|
\le
|c|
\exp\!\left(
2\eta^2C_Q\log_+\frac R\eta
+
(R^2-\eta^2)_+C_Q
\right).
\]

This is uniform over \(F\in\mathcal F\). \(\square\)

## 6. Normal-family corollary

### Corollary 6.1 — paired-zero Montel criterion

Under the hypotheses of Theorem 5.1, \(\mathcal F\) is locally bounded on
\(\mathbb C\). Therefore, by Montel's theorem, every sequence in
\(\mathcal F\) has a subsequence converging locally uniformly on
\(\mathbb C\) to an entire function.

This is a C4 normal-family theorem. It does not identify the subsequential
limit; that remains C5.

## 7. The counterexample is detected exactly

For the family in Section 2, the positive zero \(x=1\) has multiplicity \(n\)
and there is no zero at the origin. Hence

\[
Q_{1/2}(F_n)
=
\frac{n}{1+1/4}
=
\boxed{\frac{4n}{5}}.
\]

Thus the sufficient quantity diverges exactly in the example that destroys
local boundedness.

The criterion does not merely restate the anchor condition; it measures a
missing uniform concentration of zeros.

## 8. Specialization to the R056-normalized CCM family

Protected RH-R053 gives the compact-support transform growth needed to place
each admitted finite transform in the order-at-most-one class. Multiplication
by the R056 scalar normalization does not change order or exponential type.

Protected RH-R056 gives, for each admitted finite pair \((\lambda,N)\),

\[
F_{\lambda,N}(i/2)=\frac12,
\]

and identifies the zeros of \(F_{\lambda,N}\), with multiplicity, with the
zeros of the source determinant. The protected finite CCM theorem identifies
that zero multiset with the real spectrum of the associated finite
self-adjoint spectral approximant.

Write the symmetric spectrum as

\[
0\quad\text{with multiplicity }2m_0,
\]

and

\[
\pm x,\qquad x>0,
\]

with multiplicity \(m_x\) at each sign. Then

\[
\boxed{
Q_{1/2}(F_{\lambda,N})
=
4m_0+
\sum_{x>0}\frac{m_x}{x^2+1/4}.
}
\]

Spectrally,

\[
\operatorname{Tr}
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}
=
8m_0+
2\sum_{x>0}\frac{m_x}{x^2+1/4},
\]

so

\[
\boxed{
Q_{1/2}(F_{\lambda,N})
=
\frac12
\operatorname{Tr}
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}.
}
\]

Accordingly, the following is a concrete sufficient C4 target:

> Prove one uniform constant \(C_Q\) along the selected admitted cofinal family
> such that
> \[
> \operatorname{Tr}
> \left(
> (D_{\log}^{(\lambda,N)})^2+\frac14I
> \right)^{-1}
> \le 2C_Q.
> \]

If that bound is proved, Theorem 5.1 gives local boundedness of the
R056-normalized determinants on every compact subset of \(\mathbb C\), and
Montel gives subsequential locally uniform convergence.

### Important boundary

R059 does **not** prove that the CCM family satisfies this uniform trace bound.

It proves that such a bound is sufficient and identifies it exactly as one
operator-side quantity that would close the normal-family part of C4.

## 9. Relationship to C1, C3, C5, and C6

R059 is deliberately modular.

- C1 still must specify an admitted cofinal family.
- C3 still must provide sufficiently strong eigenvector/transform
  approximation information.
- R059 supplies a sufficient route to C4 if its uniform spectral sum is
  established on that family.
- C5 must identify every subsequential entire limit with \(\Xi\), or with an
  explicitly allowed zero-free multiple.
- C6 must then promote subsequential information to full local-uniform
  convergence.

No step above uses pointwise convergence as a substitute for normality.

## 10. Theorem

### RH-R059-PAIRED-ZERO-NORMAL-FAMILY-001

Let \(\eta>0\), \(c\ne0\), and let \(\mathcal F\) be a family of even entire
functions of order at most one, all of whose zeros are real, with common
anchor

\[
F(i\eta)=c.
\]

If

\[
\sup_{F\in\mathcal F}Q_\eta(F)\le C_Q<\infty,
\]

then \(\mathcal F\) is locally bounded, with the explicit bound

\[
\sup_{\substack{F\in\mathcal F\\ |z|\le R}}
|F(z)|
\le
|c|
\exp\!\left(
2\eta^2C_Q\log_+\frac R\eta
+
(R^2-\eta^2)_+C_Q
\right).
\]

Hence \(\mathcal F\) is a normal family in the compact-open holomorphic sense.

For the R056-normalized admitted finite CCM determinants at \(\eta=1/2\), the
sufficient paired-zero energy is exactly one half of the spectral sum of
\((D_{\log}^2+\frac14I)^{-1}\).

The R056 properties alone are insufficient for the required local boundedness:
the explicit family in Section 2 has the same even/real-zero/anchor properties
but is not locally bounded.

## 11. False-proof firewall

Reject:

1. claiming that the R056 normalization itself implies local boundedness;
2. treating real zeros plus a fixed nonreal anchor as a local-boundedness
   theorem;
3. omitting multiplicities in \(Q_\eta\);
4. omitting a possible zero at the origin;
5. using an unpaired genus-one product while silently discarding its
   exponential factors;
6. claiming that the CCM family has a uniform resolvent-trace bound merely
   because each individual trace is finite;
7. promoting normality to identification of the limit with \(\Xi\);
8. promoting a subsequential limit to convergence of the full family;
9. inferring determinant convergence, global simple-evenness, RH, novelty,
   priority, publication readiness, or certification.

## 12. Claim boundary

This package proves an abstract sufficient C4 criterion and an exact
specialization target. It does not prove:

- a cofinal admitted CCM family;
- a uniform CCM paired-zero/resolvent-trace bound;
- C3 eigenvector convergence;
- C5 limit identification;
- C6 full locally uniform convergence;
- global simple-evenness;
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 13. Admission dependency

Before protected admission:

1. compose the candidate onto the then-current protected main if main moves;
2. run non-authoring Adversary and Referee passes on the exact candidate head;
3. require exact-head Solve/GCL green checks;
4. merge through protected controls;
5. perform protected readback and update the Route C coordination surfaces.

Terminal candidate disposition:

RH-R059_ABSTRACT_C4_CRITERION_PROVED__UNIFORM_CCM_ZERO_ENERGY_REMAINS_OPEN
