# RH-R080-SIGNED-PROJECTIVE-NORMALITY-001

Campaign: RH-001

Route: Forward Route C — critical-strip determinant route

Obligation: P1 / C4 normal-family control without assuming pointwise positivity

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#753
- blind contribution cohort: handoffs/RH-001/r080/README.md

Protected Solve base:
grandchallenge/MATHSOLVE@33f28e7de9d6fae540bc503e11bc5079b554107f

Protected dependencies:
- RH-R053-COMPACT-TRANSFORM-STABILITY-001
- RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001
- RH-R077-PROJECTIVE-MEASURE-REPAIR-001
- MATHFORGE RH-R037 finite parity/Galerkin source audit
- MATHFORGE RH-R038 rejected Krein-Rutman closure audit
- CCM, *Zeta Spectral Triples*, arXiv:2511.22755v1, especially Theorem 5.10

Sanity replay:
scripts/rh_r080_signed_projective_check.py

No claim of global CCM pointwise positivity, actual-family C4 discharge,
cofinal admissibility, determinant convergence, RH, novelty, priority,
publication-readiness, or certification.

---

## 1. Source boundary and purpose

CCM Theorem 5.10 assumes that the smallest eigenvalue of the finite
\(QW_\lambda^N\) block is simple and that its corresponding eigenvector is
even. It does not state pointwise nonnegativity of that eigenvector.

RH-R077 therefore correctly reclassified the R068 normal-family result as
conditional on pointwise positivity.

R080 proves that pointwise positivity is stronger than necessary.

The correct positivity-free quantity is the total variation of the normalized
signed projective state. More generally, on each strict substrip one needs
only a weaker substrip-weighted cancellation ratio.

---

## 2. Signed projective normalization

Fix \(a>0\). Let \(f\in L^1([-a,a])\) be real-valued and even. Define

\[
A(f)
:=
\int_0^a f(x)\cosh(x/2)\,dx.
\tag{2.1}
\]

Assume

\[
A(f)\ne0.
\tag{2.2}
\]

The Fourier transform in the Route C coordinate is

\[
\widehat f(z)
=
2\int_0^a f(x)\cos(zx)\,dx.
\tag{2.3}
\]

The R056-type normalized transform is

\[
F_f(z)
:=
\frac{\widehat f(z)}
     {2\widehat f(i/2)}
=
\frac{1}{2A(f)}
\int_0^a f(x)\cos(zx)\,dx.
\tag{2.4}
\]

Define the signed projective measure

\[
\boxed{
d\mu_f(x)
:=
\frac{f(x)\cosh(x/2)}{A(f)}\,dx.
}
\tag{2.5}
\]

Then

\[
\mu_f([0,a])=1.
\tag{2.6}
\]

For

\[
K_z(x)
:=
\frac{\cos(zx)}{\cosh(x/2)},
\tag{2.7}
\]

one has the exact representation

\[
\boxed{
F_f(z)
=
\frac12\int_0^a K_z(x)\,d\mu_f(x).
}
\tag{2.8}
\]

If \(c\in\mathbb R\setminus\{0\}\), then

\[
\mu_{cf}=\mu_f,
\qquad
F_{cf}=F_f.
\tag{2.9}
\]

Thus both are invariants of the real projective ray.

---

## 3. Global signed condition number

Define

\[
\boxed{
\kappa_{1/2}(f)
:=
\|\mu_f\|_{\rm TV}
=
\frac{
\int_0^a |f(x)|\cosh(x/2)\,dx
}{
|A(f)|
}.
}
\tag{3.1}
\]

The triangle inequality gives

\[
\kappa_{1/2}(f)\ge1.
\tag{3.2}
\]

### Proposition 3.1 — exact equality case

For real \(f\) satisfying (2.2),

\[
\boxed{
\kappa_{1/2}(f)=1
}
\tag{3.3}
\]

if and only if \(f\) has one sign almost everywhere on \([0,a]\).

Equivalently, after multiplying the projective representative by
\(\operatorname{sgn}A(f)\), equality holds if and only if the oriented
representative is nonnegative almost everywhere.

Proof. Set
\(g(x)=f(x)\cosh(x/2)\).
Since the weight is strictly positive,

\[
|A(f)|
=
\left|\int_0^a g(x)\,dx\right|
\le
\int_0^a |g(x)|\,dx.
\]

Equality in the real triangle inequality occurs exactly when \(g\) has one
sign almost everywhere. Since \(\cosh(x/2)>0\), this is equivalent to \(f\)
having one sign almost everywhere. \(\square\)

Hence R077 positivity is precisely the extremal case
\(\kappa_{1/2}=1\), up to the irrelevant overall sign of the eigenvector.

---

## 4. Positivity-free closed-strip bound

RH-R077 proved

\[
|K_z(x)|\le1
\qquad
(|\operatorname{Im}z|\le1/2).
\tag{4.1}
\]

### Theorem 4.1 — signed-projective strip contraction

For every real even \(f\) satisfying \(A(f)\ne0\),

\[
\boxed{
\sup_{|\operatorname{Im}z|\le1/2}
|F_f(z)|
\le
\frac12\kappa_{1/2}(f).
}
\tag{4.2}
\]

Proof. From (2.8), variation domination, and (4.1),

\[
|F_f(z)|
\le
\frac12
\int_0^a |K_z(x)|\,d|\mu_f|(x)
\le
\frac12\|\mu_f\|_{\rm TV}.
\]

Use (3.1). \(\square\)

### Corollary 4.2 — uniform TV implies C4

Let \((f_j)\) be real even states with \(A(f_j)\ne0\). If

\[
\sup_j\kappa_{1/2}(f_j)<\infty,
\tag{4.3}
\]

then \((F_{f_j})\) is uniformly bounded on the closed strip
\(|\operatorname{Im}z|\le1/2\), hence is a normal family on the open strip

\[
U=\{z:|\operatorname{Im}z|<1/2\}.
\tag{4.4}
\]

This discharges the analytic C4 normality implication under a strictly weaker
hypothesis than pointwise positivity.

It does not prove that the actual CCM eigenvectors satisfy (4.3).

---

## 5. Strict-substrip criterion: weaker than global TV

For \(0\le\delta\le1/2\), define

\[
\boxed{
\kappa_\delta(f)
:=
\frac{
\int_0^a |f(x)|\cosh(\delta x)\,dx
}{
|A(f)|
}.
}
\tag{5.1}
\]

Since \(\cosh(\delta x)\le\cosh(x/2)\),

\[
\kappa_\delta(f)
\le
\kappa_{1/2}(f).
\tag{5.2}
\]

### Theorem 5.1 — exact substrip bound

For every \(0\le\delta\le1/2\),

\[
\boxed{
\sup_{|\operatorname{Im}z|\le\delta}
|F_f(z)|
\le
\frac12\kappa_\delta(f).
}
\tag{5.3}
\]

Proof. If \(z=t+is\) and \(|s|\le\delta\), then

\[
|\cos(zx)|
\le
\cosh(sx)
\le
\cosh(\delta x).
\]

Apply this directly to (2.4). \(\square\)

### Corollary 5.2 — local C4 criterion

A family \((F_{f_j})\) is locally bounded on \(U\), and therefore normal, if

\[
\boxed{
\forall\delta<1/2,\qquad
\sup_j\kappa_\delta(f_j)<\infty.
}
\tag{5.4}
\]

This is weaker than a uniform bound on \(\kappa_{1/2}\).

Indeed, every compact \(K\Subset U\) lies in a closed substrip
\(|\operatorname{Im}z|\le\delta_K\) for some \(\delta_K<1/2\), and (5.3)
supplies a uniform bound on \(K\).

Thus the exact C4 target need not control the full boundary-weighted variation.
It is enough to control cancellation at every fixed interior height.

---

## 6. Sign-defect decomposition

Because the projective ray is invariant under nonzero real scaling, orient
\(f\) so that

\[
A(f)>0.
\tag{6.1}
\]

Write

\[
f=f_+-f_-,
\qquad
f_\pm\ge0,
\qquad
f_+f_-=0\ \text{a.e.}
\tag{6.2}
\]

and set, with \(w(x)=\cosh(x/2)\),

\[
P(f)
=
\int_0^a f_+(x)w(x)\,dx,
\qquad
N(f)
=
\int_0^a f_-(x)w(x)\,dx.
\tag{6.3}
\]

Then

\[
A(f)=P(f)-N(f)>0
\tag{6.4}
\]

and

\[
\kappa_{1/2}(f)
=
\frac{P(f)+N(f)}{P(f)-N(f)}.
\tag{6.5}
\]

Hence

\[
\boxed{
\kappa_{1/2}(f)
=
1+
2\frac{N(f)}{A(f)}.
}
\tag{6.6}
\]

Therefore a uniform closed-strip condition number bound is exactly equivalent
to a uniform bound on the boundary-weighted negative-mass ratio

\[
\frac{N(f)}{A(f)}.
\tag{6.7}
\]

Pointwise positivity is the special case \(N(f)=0\).

This converts P1 from a qualitative cone-membership problem into a quantitative
sign-cancellation problem.

---

## 7. Transfer from a sign-definite reference state

Let \(g\in L^1([-a,a])\) be real, even, and after orientation satisfy

\[
g(x)\ge0,
\qquad
A(g)>0.
\tag{7.1}
\]

Let \(f\) be real and even, and define the boundary-weighted error

\[
E(f,g)
:=
\int_0^a
|f(x)-g(x)|\cosh(x/2)\,dx.
\tag{7.2}
\]

### Theorem 7.1 — relative weighted error controls signed condition number

If

\[
E(f,g)<A(g),
\tag{7.3}
\]

then \(A(f)>0\) and

\[
\boxed{
\kappa_{1/2}(f)
\le
\frac{A(g)+E(f,g)}
     {A(g)-E(f,g)}.
}
\tag{7.4}
\]

Proof. First,

\[
A(f)
=
A(g)+
\int_0^a(f-g)w
\ge
A(g)-E(f,g)>0.
\tag{7.5}
\]

Also

\[
\int_0^a |f|w
\le
\int_0^a g\,w
+
\int_0^a|f-g|w
=
A(g)+E(f,g).
\tag{7.6}
\]

Divide (7.6) by (7.5). \(\square\)

### Corollary 7.2 — uniform relative reference approximation implies C4

If along a family

\[
\frac{E(f_j,g_j)}{A(g_j)}
\le
\rho<1
\tag{7.7}
\]

uniformly, then

\[
\boxed{
\kappa_{1/2}(f_j)
\le
\frac{1+\rho}{1-\rho}
}
\tag{7.8}
\]

uniformly, and C4 follows from Corollary 4.2.

This is an exact route from approximation to normality that does not require
the true state \(f_j\) itself to be pointwise positive.

No claim is made here that the CCM candidate \(k_\lambda\), or any other
source candidate, satisfies the sign-definite reference hypothesis (7.1).

---

## 8. What simple-evenness does and does not imply

Finite simple-evenness supplies:

- a simple lowest eigenvalue;
- an even ground-state ray.

It does not, as a matter of linear algebra alone, imply pointwise
nonnegativity of the associated even trigonometric polynomial.

An arbitrary real symmetric parity-preserving finite operator can have a
simple even ground eigenvector represented by a sign-changing even
trigonometric polynomial.

Therefore any proof of actual CCM pointwise positivity must use additional
source-specific structure beyond simple-evenness.

The RH-R080 blind WP-A and WP-B dispatches test exactly that additional
structure.

---

## 9. Corrected P1/C4 target

R080 replaces the single qualitative P1 question

> Is the finite CCM ground state pointwise nonnegative?

with the following hierarchy.

### P1a — strongest

Prove pointwise sign-definiteness of the actual finite CCM ground-state ray.

Equivalent analytic condition:

\[
\kappa_{1/2}(\xi_{\lambda,N})=1.
\]

### P1b — sufficient closed-strip replacement

Prove

\[
\sup_{(\lambda,N)\in\mathcal A}
\kappa_{1/2}(\xi_{\lambda,N})
<\infty
\tag{9.1}
\]

on an admitted cofinal family \(\mathcal A\).

### P1c — weakest local-normality replacement

For every fixed \(\delta<1/2\), prove

\[
\sup_{(\lambda,N)\in\mathcal A}
\kappa_\delta(\xi_{\lambda,N})
<\infty.
\tag{9.2}
\]

P1c already yields Montel normality on the exact critical-strip domain needed
by Route C.

Thus a finite positivity counterexample would kill P1a but leave P1b/P1c
entirely viable.

---

## 10. Practical certification interface

For a finite CCM even eigenvector, the state is a finite trigonometric
polynomial. R080 therefore recommends that future exact computation report,
in addition to spectral data:

\[
A(\xi)
=
\int_0^a \xi(x)\cosh(x/2)\,dx,
\tag{10.1}
\]

\[
M_\delta(\xi)
=
\int_0^a |\xi(x)|\cosh(\delta x)\,dx,
\tag{10.2}
\]

and

\[
\kappa_\delta(\xi)=\frac{M_\delta(\xi)}{|A(\xi)|}.
\tag{10.3}
\]

A proof-quality finite sign-change certificate should isolate all real zeros
of the trigonometric polynomial on the physical interval and integrate the
signed pieces with rigorous interval control.

A numerical plot alone is not proof evidence.

---

## 11. Current disposition

Native R080 result:

\[
\boxed{
\text{POINTWISE POSITIVITY NOT REQUIRED FOR C4;}
\quad
\{\kappa_\delta\}_{\delta<1/2}
\text{ IS THE EXACT SIGNED-PROJECTIVE NORMALITY INTERFACE.}
}
\]

Remaining actual-family questions:

1. Does the CCM finite simple-even ground-state ray satisfy P1a?
2. If not, are P1b or P1c uniformly bounded on an admitted cofinal family?
3. Can a source candidate provide the relative weighted approximation in
   Theorem 7.1?
4. Independent WP-A/WP-B/WP-C returns remain to be synthesized when available.

Terminal candidate disposition:

RH-R080_SIGNED_PROJECTIVE_NORMALITY_PROVED__
ACTUAL_CCM_SIGN_CONTROL_OPEN
