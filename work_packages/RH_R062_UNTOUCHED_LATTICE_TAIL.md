# RH-R062-UNTOUCHED-LATTICE-TAIL-001

Campaign: RH-001

Route: Forward Route C — determinant convergence to Xi

Obligations: C1/C4 interface — cofinal schedule versus normal-family control

Status:
ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#726

Protected Solve base:
grandchallenge/MATHSOLVE@41e90f5c534bc3b58e3296762d9eee370ac2ca31

Protected dependencies:
- grandchallenge/MATHSOLVE@41e90f5c534bc3b58e3296762d9eee370ac2ca31:
  work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- grandchallenge/MATHSOLVE@41e90f5c534bc3b58e3296762d9eee370ac2ca31:
  work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- grandchallenge/MATHSOLVE@41e90f5c534bc3b58e3296762d9eee370ac2ca31:
  work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- grandchallenge/MATHSOLVE@41e90f5c534bc3b58e3296762d9eee370ac2ca31:
  work_packages/RH_R059_PAIRED_ZERO_NORMAL_FAMILY.md

Primary source:
Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples*,
arXiv:2511.22755v1 (2025-11-27), especially §5.6 and Theorem 5.10.

Sanity replay:
scripts/rh_r062_lattice_tail_check.py

No cofinal admissibility / full C4 / C5 / C6 / determinant convergence /
global simple-evenness / RH / novelty / priority / publication-readiness /
certification claim.

## 1. Purpose

Protected RH-R059 proves that one sufficient condition for local boundedness of
the R056-normalized finite determinants is a uniform bound on

\[
Q_{\lambda,N}
:=
Q_{1/2}(F_{\lambda,N})
=
\frac12
\operatorname{Tr}
\left(
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}
\right).
\tag{1.1}
\]

R059 does not prove such a bound.

The CCM operator has an important source-fixed feature that already constrains
any schedule on which (1.1) could remain uniformly bounded.  The rank-one
finite modification acts only on the finite span \(E_N\); on the orthogonal
complement \(E_N^\perp\), the operator remains the original periodic scaling
operator.

This package isolates that untouched contribution and proves an exact schedule
law.

Set

\[
a:=\log\lambda>0,
\qquad
L=2a.
\]

The untouched positive complement eigenvalues are

\[
\frac{2\pi j}{L}
=
\frac{\pi j}{a},
\qquad
j=N+1,N+2,\ldots.
\]

Define the positive-complement tail

\[
\boxed{
T_{a,N}
:=
\sum_{j=N+1}^{\infty}
\frac{1}
     {(\pi j/a)^2+1/4}.
}
\tag{1.2}
\]

The theorem below proves that the quadratic scale

\[
N\asymp a^2=(\log\lambda)^2
\]

is the exact transition scale for this untouched contribution.

## 2. Exact source decomposition

CCM Theorem 5.10 acts on the direct sum

\[
E_N'\oplus E_N^\perp,
\qquad
E_N'=E_N/\mathbb C\xi.
\]

Its proof factors the regularized determinant into

\[
\det_{\rm reg}
(D_{\log}^{(\lambda,N)}-z)
=
\operatorname{Det}
\left(
D_{\log}^{(\lambda,N)}|_{E_N'}-z
\right)
\,
\det_{\rm reg}
\left(
D_{\log}^{(\lambda)}|_{E_N^\perp}-z
\right).
\tag{2.1}
\]

The same proof identifies the zeros of the second factor as

\[
\left\{
\frac{2\pi j}{L}:
j\in\mathbb Z,\ |j|>N
\right\}.
\tag{2.2}
\]

Because the full operator is the direct sum of the finite block and this
untouched complement, the positive operator

\[
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}
\]

also decomposes as a direct sum.

Protected RH-R059 establishes that its trace is finite for every admitted
finite pair.

## 3. The unavoidable complement contribution

### Proposition 3.1

For every admitted finite CCM pair \((\lambda,N)\) with \(N\ge1\),

\[
\boxed{
Q_{\lambda,N}
\ge
T_{a,N},
\qquad
a=\log\lambda.
}
\tag{3.1}
\]

### Proof

By (1.1), \(Q_{\lambda,N}\) is one half of the trace of the positive resolvent
function of the full self-adjoint direct sum.

On \(E_N^\perp\), the eigenvalues are

\[
\pm\frac{\pi j}{a},
\qquad
j>N.
\]

Therefore the complement contribution to the full trace is

\[
2
\sum_{j=N+1}^{\infty}
\frac{1}
     {(\pi j/a)^2+1/4}
=
2T_{a,N}.
\]

The finite \(E_N'\) block contributes a nonnegative trace.  Dividing the full
trace by two gives (3.1).

QED.

### Consequence 3.2

Any uniform R059 bound

\[
Q_{\lambda,N}\le C_Q
\]

on a family of admitted finite pairs necessarily implies

\[
T_{a,N}\le C_Q
\]

on the same family.

Thus the untouched lattice tail supplies a source-fixed necessary schedule
condition before any analysis of the finite modified block begins.

## 4. Exact integral bracket

For fixed \(a>0\), define

\[
f_a(x)
:=
\frac{1}
     {(\pi x/a)^2+1/4},
\qquad
x>0.
\]

The function \(f_a\) is positive and strictly decreasing.

### Lemma 4.1

For \(N\ge1\),

\[
\boxed{
\int_{N+1}^{\infty}f_a(x)\,dx
\le
T_{a,N}
\le
\int_N^{\infty}f_a(x)\,dx.
}
\tag{4.1}
\]

### Proof

This is the standard integral comparison for a positive decreasing function:
for each integer \(j>N\),

\[
\int_j^{j+1} f_a(x)\,dx
\le
f_a(j)
\le
\int_{j-1}^{j}f_a(x)\,dx.
\]

Summing over \(j=N+1,N+2,\ldots\) gives (4.1).

QED.

### Lemma 4.2 — exact antiderivative

For every \(X>0\),

\[
\boxed{
\int_X^{\infty}
\frac{dx}{(\pi x/a)^2+1/4}
=
\frac{2a}{\pi}
\arctan
\left(
\frac{a}{2\pi X}
\right).
}
\tag{4.2}
\]

### Proof

Set

\[
u=\frac{2\pi x}{a}.
\]

Then

\[
dx=\frac{a}{2\pi}\,du,
\qquad
(\pi x/a)^2+\frac14
=
\frac14(1+u^2).
\]

Hence

\[
\int_X^\infty f_a(x)\,dx
=
\frac{2a}{\pi}
\int_{2\pi X/a}^{\infty}
\frac{du}{1+u^2}.
\]

Using

\[
\int_y^\infty\frac{du}{1+u^2}
=
\frac\pi2-\arctan y
=
\arctan(1/y)
\qquad(y>0)
\]

gives (4.2).

QED.

Combining Lemmas 4.1 and 4.2 yields the exact bracket

\[
\boxed{
\frac{2a}{\pi}
\arctan
\left(
\frac{a}{2\pi(N+1)}
\right)
\le
T_{a,N}
\le
\frac{2a}{\pi}
\arctan
\left(
\frac{a}{2\pi N}
\right).
}
\tag{4.3}
\]

## 5. Useful elementary corollaries

Since

\[
\arctan y\le y
\qquad(y\ge0),
\]

the upper bound in (4.3) gives

\[
\boxed{
T_{a,N}
\le
\frac{a^2}{\pi^2N}.
}
\tag{5.1}
\]

For \(0\le y\le1\),

\[
\arctan y\ge \frac y2,
\]

while for \(y\ge1\),

\[
\arctan y\ge\frac\pi4.
\]

Therefore, from the lower bound in (4.3),

\[
\boxed{
T_{a,N}
\ge
\min
\left\{
\frac{a^2}{2\pi^2(N+1)},
\frac a2
\right\}.
}
\tag{5.2}
\]

Equation (5.2) is not asymptotically sharp at every scale, but it is sufficient
to prove the subquadratic obstruction without any hidden regularity assumption
on the schedule.

## 6. Schedule trichotomy

Let

\[
a\to\infty
\]

and let \(N=N(a)\ge1\) be integer-valued.

### Theorem 6.1 — subquadratic obstruction

If

\[
\frac{N(a)}{a^2}\longrightarrow0,
\]

then

\[
\boxed{
T_{a,N(a)}\longrightarrow\infty.
}
\tag{6.1}
\]

Consequently,

\[
Q_{\lambda,N(\lambda)}
\longrightarrow\infty
\]

along every admitted family with

\[
N(\lambda)
=
o((\log\lambda)^2).
\]

In particular, the R059 sufficient normal-family criterion cannot hold on such
a schedule.

### Proof

From (5.2),

\[
T_{a,N(a)}
\ge
\min
\left\{
\frac{a^2}{2\pi^2(N(a)+1)},
\frac a2
\right\}.
\]

Under \(N(a)/a^2\to0\),

\[
\frac{a^2}{N(a)+1}\to\infty,
\qquad
a\to\infty.
\]

Both entries of the minimum therefore tend to \(+\infty\), proving (6.1).
Proposition 3.1 then gives the statement for \(Q_{\lambda,N}\).

QED.

### Theorem 6.2 — critical quadratic scale

If

\[
\frac{N(a)}{a^2}\longrightarrow\kappa
\qquad
\text{for some }
\kappa\in(0,\infty),
\]

then

\[
\boxed{
T_{a,N(a)}
\longrightarrow
\frac{1}{\pi^2\kappa}.
}
\tag{6.2}
\]

### Proof

The hypothesis implies

\[
N(a)\to\infty,
\qquad
\frac{a}{N(a)}\to0.
\]

Set

\[
y_a:=\frac{a}{2\pi N(a)},
\qquad
\widetilde y_a
:=
\frac{a}{2\pi(N(a)+1)}.
\]

Then

\[
y_a,\widetilde y_a\to0,
\qquad
\frac{\arctan y_a}{y_a}\to1,
\qquad
\frac{\arctan\widetilde y_a}{\widetilde y_a}\to1.
\]

The upper bound in (4.3) can be written

\[
\frac{2a}{\pi}\arctan y_a
=
\frac{a^2}{\pi^2N(a)}
\frac{\arctan y_a}{y_a}
\longrightarrow
\frac{1}{\pi^2\kappa}.
\]

Similarly, the lower bound is

\[
\frac{2a}{\pi}\arctan\widetilde y_a
=
\frac{a^2}{\pi^2(N(a)+1)}
\frac{\arctan\widetilde y_a}{\widetilde y_a}
\longrightarrow
\frac{1}{\pi^2\kappa}.
\]

The squeeze theorem proves (6.2).

QED.

### Theorem 6.3 — superquadratic disappearance of the complement tail

If

\[
\frac{N(a)}{a^2}\longrightarrow\infty,
\]

then

\[
\boxed{
T_{a,N(a)}\longrightarrow0.
}
\tag{6.3}
\]

### Proof

By (5.1),

\[
0\le T_{a,N(a)}
\le
\frac{a^2}{\pi^2N(a)}
\longrightarrow0.
\]

QED.

## 7. Exact necessary schedule scale for the R059 mechanism

### Corollary 7.1

Suppose \(\mathcal I\) is an admitted family of finite CCM pairs with
\(a=\log\lambda\to\infty\), and suppose the R059 quantity is uniformly bounded:

\[
\sup_{(\lambda,N)\in\mathcal I}
Q_{\lambda,N}
<
\infty.
\tag{7.1}
\]

Then necessarily

\[
\boxed{
N(\lambda)
=
\Omega((\log\lambda)^2).
}
\tag{7.2}
\]

Equivalently, there are constants \(c>0\) and \(\lambda_0>1\) such that every
pair in the family with \(\lambda\ge\lambda_0\) satisfies

\[
N\ge c(\log\lambda)^2.
\]

### Proof

If (7.2) failed, there would exist a sequence in the family with
\(a\to\infty\) and

\[
\frac{N}{a^2}\to0.
\]

Theorem 6.1 would force

\[
T_{a,N}\to\infty.
\]

By Proposition 3.1,

\[
Q_{\lambda,N}\ge T_{a,N},
\]

contradicting (7.1).

QED.

### Corollary 7.2 — a sufficient scale for the complement only

If for some fixed \(\kappa>0\),

\[
N(a)\ge\kappa a^2
\]

for all sufficiently large \(a\), then

\[
\boxed{
T_{a,N(a)}
\le
\frac{1}{\pi^2\kappa}
}
\tag{7.3}
\]

for all sufficiently large \(a\).

This bounds only the untouched complement contribution.

It does **not** bound the finite \(E_N'\) contribution to
\(Q_{\lambda,N}\).

## 8. Interpretation for Route C

R059 converted C4 into a positive resolvent-trace target.

R062 shows that this target is already sensitive to the two-parameter schedule
before any hard finite-block analysis begins.

The source-fixed untouched complement enforces the following design rule:

\[
\boxed{
\text{For the R059 C4 mechanism, }
N
\text{ cannot grow subquadratically in }
\log\lambda.
}
\]

More precisely:

- \(N=o((\log\lambda)^2)\): impossible for uniform R059 control because the
  untouched tail diverges;
- \(N\sim\kappa(\log\lambda)^2\): the untouched tail tends to the positive
  constant \(1/(\pi^2\kappa)\);
- \(N\gg(\log\lambda)^2\): the untouched tail vanishes.

This is a necessary schedule theorem, not a cofinal admissibility theorem.

It does not say that a quadratic or superquadratic schedule satisfies the
finite simple-even hypothesis, nor that the finite modified block has bounded
resolvent trace.

## 9. The remaining positive burden

Write the direct-sum half trace as

\[
Q_{\lambda,N}
=
B_{\lambda,N}
+
T_{a,N},
\tag{9.1}
\]

where

\[
B_{\lambda,N}
:=
\frac12
\operatorname{Tr}_{E_N'}
\left(
\left(
(D_{\log}^{(\lambda,N)}|_{E_N'})^2+\frac14I
\right)^{-1}
\right)
\ge0.
\tag{9.2}
\]

R062 controls and classifies the second term exactly.

The unresolved C4 burden is therefore sharpened to:

> Find an admitted cofinal schedule satisfying at least
> \(N=\Omega((\log\lambda)^2)\), and prove a uniform bound on the finite-block
> contribution \(B_{\lambda,N}\); or prove a weaker local-boundedness theorem
> that does not require the full R059 trace criterion.

The next Route C lane R065 is reserved for this finite-block / weaker-criterion
frontier unless tracker #414 records a different collision-free allocation.

## 10. Relationship to C1

R062 gives a necessary condition on any C1 schedule intended to use R059.

It does not by itself specify a complete cofinal directed set.

In particular, C1 must still address:

- how \(\lambda\to\infty\);
- how \(N\to\infty\);
- whether the finite CCM simple-even hypothesis holds for every selected pair;
- whether the chosen schedule supports C3 and C5 as well as C4.

A schedule chosen only to satisfy \(N\gtrsim(\log\lambda)^2\) is not yet an
admitted cofinal family.

## 11. Interaction with C3 and R053

The quadratic schedule requirement can make direct C3 transform estimates more
demanding computationally or analytically, because the finite-dimensional
truncation grows at least like \((\log\lambda)^2\) if one uses the R059
criterion.

R062 does not alter the R053 rate dichotomy.

It only proves that any future combined C1/C3/C4 strategy using R059 must be
compatible with this lower growth rate in \(N\).

## 12. False-proof firewall

Reject:

1. finite \(T_{a,N}\) for each pair \(\Rightarrow\) a uniform family bound;
2. \(N\to\infty\) without comparison to \((\log\lambda)^2\);
3. \(N\asymp(\log\lambda)^2\) \(\Rightarrow\) full R059 trace bounded;
4. vanishing untouched tail \(\Rightarrow\) finite block bounded;
5. a schedule satisfying (7.2) \(\Rightarrow\) finite CCM simple-evenness;
6. a necessary schedule scale \(\Rightarrow\) C1 fully discharged;
7. the abstract R059 criterion \(\Rightarrow\) actual CCM normality;
8. normality \(\Rightarrow\) limit identification;
9. subsequential convergence \(\Rightarrow\) full convergence;
10. any use of R035's terminal Rouché/Hurwitz bridge before C6;
11. determinant convergence, RH, novelty, priority, publication readiness, or
    certification claims.

## 13. Theorem

### RH-R062-UNTOUCHED-LATTICE-TAIL-001

For every admitted finite CCM pair \((\lambda,N)\) with

\[
a=\log\lambda,
\qquad
N\ge1,
\]

the R059 paired-zero energy satisfies

\[
Q_{\lambda,N}
\ge
T_{a,N}
:=
\sum_{j=N+1}^{\infty}
\frac1{(\pi j/a)^2+1/4}.
\]

The tail obeys

\[
\frac{2a}{\pi}
\arctan\frac{a}{2\pi(N+1)}
\le
T_{a,N}
\le
\frac{2a}{\pi}
\arctan\frac{a}{2\pi N}.
\]

Consequently, for any schedule \(a\to\infty\):

\[
\frac{N(a)}{a^2}\to0
\quad\Longrightarrow\quad
T_{a,N(a)}\to\infty;
\]

\[
\frac{N(a)}{a^2}\to\kappa\in(0,\infty)
\quad\Longrightarrow\quad
T_{a,N(a)}\to\frac1{\pi^2\kappa};
\]

\[
\frac{N(a)}{a^2}\to\infty
\quad\Longrightarrow\quad
T_{a,N(a)}\to0.
\]

Therefore a uniformly bounded R059 paired-zero energy along an admitted family
with \(\lambda\to\infty\) requires

\[
\boxed{
N(\lambda)
=
\Omega((\log\lambda)^2).
}
\]

This is necessary for the R059 mechanism and controls only the untouched
scaling complement.  The finite modified block remains an independent
nonnegative contribution.

## 14. Claim boundary

This package proves:

- an exact positive lower bound on the R059 quantity from the untouched source
  spectrum;
- exact integral brackets for that tail;
- the sharp subcritical/critical/supercritical schedule trichotomy;
- the necessary quadratic \(N\)-versus-\(\log\lambda\) scale for any use of the
  R059 criterion.

This package does not prove:

- that any schedule is CCM-admissible at all large scales;
- that \(N\asymp(\log\lambda)^2\) is sufficient for the full R059 trace;
- a uniform bound on the finite \(E_N'\) block;
- C1 in full;
- C3 eigenvector approximation;
- actual CCM C4 normality;
- C5 limit identification;
- C6 local-uniform convergence;
- global simple-evenness;
- determinant convergence;
- RH;
- novelty or priority;
- a MATHCERT disposition.

## 15. Admission dependency

Before protected admission:

1. re-fetch protected main and recompose if it moves;
2. run the bounded sanity replay;
3. record exact-head non-authoring/read-only Adversary and Referee passes;
4. require exact-head Solve/GCL green checks;
5. merge only through protected controls;
6. perform protected readback;
7. update #726, #414, and the canonical RH handoff.

Terminal candidate disposition:

RH-R062_UNTOUCHED_LATTICE_TAIL_TRICHOTOMY_PROVED__SUBQUADRATIC_SCHEDULES_RULED_OUT_FOR_R059__FINITE_BLOCK_BURDEN_OPEN
