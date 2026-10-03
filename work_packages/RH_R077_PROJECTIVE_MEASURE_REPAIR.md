# RH-R077-PROJECTIVE-MEASURE-REPAIR-001

Campaign: RH-001

Route: Forward Route C — critical-strip determinant route

Role: integrity repair + projective-measure reframing

Status: ADMISSION_CANDIDATE

Solve coordination:
- route tracker: grandchallenge/MATHSOLVE#414
- bounded tranche: grandchallenge/MATHSOLVE#742

Protected Solve base:
grandchallenge/MATHSOLVE@1716d39a228e71b2b9f16f902dda32694d62557a

Protected dependencies:
- RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001
- RH-R037-QW-SECTOR-GALERKIN-001
- RH-R053-COMPACT-TRANSFORM-STABILITY-001
- RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001
- RH-R068-STRIP-NORMAL-FAMILY-001
- RH-R071-LIMIT-IDENTIFICATION-001
- RH-R074-EIGENVECTOR-ERROR-TRANSFER-001
- MATHFORGE RH-R038 Krein-Rutman claim audit at
  grandchallenge/MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a

Sanity replay:
scripts/rh_r077_projective_measure_check.py

No global positivity / cofinal admissibility / determinant convergence / RH /
novelty / priority / publication-readiness / certification claim.

---

## 1. Executive disposition

Exact-head review found three defects in the protected Route C chain.

### 1.1 R068 is conditional on a missing positivity premise

R068 proves its strip modulus theorem from the pointwise premise

\[
\xi_{\lambda,N}(x)\ge 0.
\]

That premise is not supplied by the protected finite CCM simple-even theorem.
R037 proves parity-sector Galerkin convergence, not pointwise positivity.
R040 proves a local small-a spectral statement, not a global theorem that
finite CCM ground-state trigonometric polynomials are pointwise nonnegative.
The protected Forge R038 audit explicitly rejected the prior
Krein-Rutman/positive-kernel route as a global closure.

Therefore the analytic implication

\[
\xi_{\lambda,N}\ge0
\Longrightarrow
|F_{\lambda,N}(z)|\le\frac12
\quad (|\operatorname{Im}z|\le1/2)
\]

is valid, but its application to every admitted CCM pair is not presently
protected.

Route C obligation C4 is consequently reclassified:

\[
\boxed{\text{C4 = CONDITIONAL\_ON\_POINTWISE\_POSITIVITY}.}
\]

### 1.2 The boundary anchor does not prevent the zero limit

R056 fixes

\[
F_{\lambda,N}(i/2)=\frac12.
\]

But \(i/2\) lies on the boundary of the normal-family domain

\[
U:=\{z:|\operatorname{Im}z|<1/2\}.
\]

Compact-open convergence on \(U\) does not preserve a boundary value.

The explicit family

\[
\boxed{
E_n(z):=
\frac12\,\frac{\cos(nz)}{\cosh(n/2)}
}
\tag{1.1}
\]

has all of the following properties:

- entire and even;
- every zero is real;
- \(E_n(i/2)=1/2\);
- \(|E_n(z)|\le1/2\) for \(|\operatorname{Im}z|\le1/2\);
- \(E_n\to0\) locally uniformly on \(U\).

Thus a boundary anchor plus strip boundedness and real zeros does not exclude
the identically-zero interior limit.

The R068 non-triviality inference from the boundary anchor and the R071
identity \(\Phi(i/2)=1\) for an arbitrary compact-open interior limit are
withdrawn.

### 1.3 R074's exponential periodic Fourier-tail theorem is not established

R074 Lemma 3.1 asserts that holomorphic extension of a function on \([-a,a]\)
to a horizontal strip implies exponential decay of coefficients in the
periodic basis

\[
e_j(x)=(2a)^{-1/2}e^{i\pi jx/a}.
\]

This is false without endpoint matching / periodic analytic continuation.
Shifting the horizontal integration contour produces vertical-side integrals
unless the endpoint contributions cancel.

The entire function \(f(x)=x\) is an explicit counterexample. For
\(j\ne0\),

\[
c_j
=
\frac1{\sqrt{2a}}\int_{-a}^a
x e^{-i\pi jx/a}\,dx
=
\frac{2ia^2(-1)^j}{\pi j\sqrt{2a}},
\]

hence

\[
|c_j|
=
\frac{\sqrt2\,a^{3/2}}{\pi|j|}.
\tag{1.2}
\]

So strip analyticity alone gives no bound of the form
\(\exp(-\pi|j|\rho/a)\).

Accordingly:

- R074's orthogonal projection inequality remains valid;
- R074's finite-dimensional Rayleigh-to-eigenvector inequality remains valid;
- R074's analytic-tail theorem is withdrawn;
- the claimed \(N(\lambda)\asymp(\log\lambda)^2\) C1 sufficiency theorem is
  withdrawn;
- the R074 master convergence theorem is not established.

---

## 2. Correct projective object

The R056 normalization is scalar-invariant after phase removal. The natural
state variable is therefore not an absolutely normalized vector but a
projective positive measure.

Let \(a>0\) and let \(f\in L^1([0,a])\) satisfy

\[
f(x)\ge0
\quad\text{a.e.},\qquad
f\not\equiv0.
\]

Extend \(f\) evenly to \([-a,a]\). Define

\[
A_f
:=
\int_0^a f(x)\cosh(x/2)\,dx
>0
\]

and the probability measure

\[
\boxed{
d\nu_f(x)
:=
\frac{f(x)\cosh(x/2)}{A_f}\,dx,
\qquad 0\le x\le a.
}
\tag{2.1}
\]

Positive scalar rescaling \(f\mapsto cf\), \(c>0\), leaves \(\nu_f\)
unchanged.

Define the strip kernel

\[
\boxed{
K_z(x):=
\frac{\cos(zx)}{\cosh(x/2)}.
}
\tag{2.2}
\]

For the R056 transform normalization,

\[
\widehat f(z)
=
2\int_0^a f(x)\cos(zx)\,dx,
\qquad
\widehat f(i/2)=2A_f,
\]

and therefore

\[
\boxed{
F_f(z)
:=
\frac{\widehat f(z)}{2\widehat f(i/2)}
=
\frac12\int_0^a K_z(x)\,d\nu_f(x).
}
\tag{2.3}
\]

This is the projective-measure representation.

---

## 3. Strip kernel theorem

Let \(z=t+is\).

### Theorem 3.1 — closed-strip contraction

For every \(x\ge0\) and every \(z\) with \(|s|\le1/2\),

\[
\boxed{|K_z(x)|\le1.}
\tag{3.1}
\]

Proof. The exact identity

\[
|\cos((t+is)x)|^2
=
\cos^2(tx)+\sinh^2(sx)
\]

gives

\[
|\cos((t+is)x)|^2
\le
1+\sinh^2(x/2)
=
\cosh^2(x/2).
\]

Divide by \(\cosh^2(x/2)\). \(\square\)

Consequently, conditional on \(f\ge0\),

\[
|F_f(z)|\le\frac12
\quad (|\operatorname{Im}z|\le1/2).
\]

This recovers the analytic content of R068 without asserting the missing CCM
positivity premise.

### Theorem 3.2 — interior kernel decay

Fix \(0\le\delta<1/2\). For all \(x\ge0\) and all
\(|\operatorname{Im}z|\le\delta\),

\[
\boxed{
|K_z(x)|
\le
2e^{-(1/2-\delta)x}.
}
\tag{3.2}
\]

Proof. Use

\[
|\cos(zx)|\le\cosh(\delta x)\le e^{\delta x}
\]

and

\[
\cosh(x/2)\ge\frac12e^{x/2}.
\]

Thus \(K_z(x)\to0\) uniformly for \(z\) in every compact subset of \(U\).

This identifies the zero-limit mechanism: projective mass can escape to
\(x=\infty\) while the boundary anchor remains fixed.

---

## 4. Exact zero-collapse counterexample

For \(n\ge1\), define \(E_n\) by (1.1). It is the transform associated with
the point probability measure \(\delta_n\):

\[
E_n(z)=\frac12\int K_z(x)\,d\delta_n(x).
\]

Its zeros are

\[
z=\frac{\pi/2+k\pi}{n},
\qquad k\in\mathbb Z,
\]

hence all are real.

At the boundary anchor,

\[
E_n(i/2)
=
\frac12\frac{\cosh(n/2)}{\cosh(n/2)}
=
\frac12.
\]

Theorem 3.1 gives the closed-strip bound. If \(K\Subset U\), choose
\(\delta<1/2\) with \(K\subset\{|\operatorname{Im}z|\le\delta\}\).
Then by Theorem 3.2,

\[
\sup_{z\in K}|E_n(z)|
\le
e^{-(1/2-\delta)n}
\longrightarrow0.
\]

Therefore

\[
\boxed{E_n\to0\text{ locally uniformly on }U.}
\tag{4.1}
\]

This is a theorem-grade counterexample to boundary-anchor noncollapse.

---

## 5. Scale-free projective transfer

Let \(\nu,\mu\) be finite signed or complex measures on \([0,\infty)\), and
write

\[
F_\nu(z)=\frac12\int K_z\,d\nu,
\qquad
F_\mu(z)=\frac12\int K_z\,d\mu.
\]

Use the total-variation norm

\[
\|\sigma\|_{\mathrm{TV}}:=|\sigma|([0,\infty)).
\]

### Theorem 5.1 — TV contraction

For every \(z\) in the closed strip,

\[
\boxed{
|F_\nu(z)-F_\mu(z)|
\le
\frac12\|\nu-\mu\|_{\mathrm{TV}}.
}
\tag{5.1}
\]

Hence

\[
\boxed{
\sup_{|\operatorname{Im}z|\le1/2}
|F_\nu(z)-F_\mu(z)|
\le
\frac12\|\nu-\mu\|_{\mathrm{TV}}.
}
\tag{5.2}
\]

Proof. Combine Theorem 3.1 with the defining inequality for the variation
measure. \(\square\)

Unlike the raw \(L^2\) transfer in R053/R071, this estimate has no
\(\lambda^\delta\), \(\lambda^{1/2}\), or boundary-denominator loss. It is
the natural scale-free interface if the true and candidate projective states
can be compared in this topology.

No claim is made here that the CCM candidate satisfies this convergence.

---

## 6. Non-escape criterion

For a positive projective state \(\nu_j\),

\[
F_j(0)
=
\frac12\int_0^\infty
\frac{1}{\cosh(x/2)}\,d\nu_j(x).
\tag{6.1}
\]

Since the kernel \(1/\cosh(x/2)\) lies in \(C_0([0,\infty))\), escape of all
mass to infinity forces \(F_j(0)\to0\).

Conversely, a lower bound

\[
\limsup_j F_j(0)>0
\tag{6.2}
\]

is a sufficient witness that some interior mass remains visible. It is not
equivalent to tightness of the entire probability sequence, and no such
equivalence is claimed.

The correct anti-collapse observable is therefore an interior value, not
the boundary anchor.

---

## 7. Minimal subsequential Xi closure

Let

\[
U=\{z:|\operatorname{Im}z|<1/2\}.
\]

### Theorem 7.1 — non-escape + projective shape implies a nonzero Xi subsequence

Let \((F_j)\) be holomorphic functions on \(U\) satisfying:

1. \((F_j)\) is a normal family on \(U\);
2. every zero of every \(F_j\) in \(U\) is real;
3. \(\limsup_j F_j(0)>0\);
4. there is a nonempty real interval \(I\) such that, for every \(t\in I\),

\[
\frac{F_j(t)}{F_j(0)}
\longrightarrow
\frac{\Xi(t)}{\Xi(0)}.
\tag{7.1}
\]

Then there is a subsequence \(F_{j_k}\) and a constant \(c\ne0\) such that

\[
\boxed{
F_{j_k}
\longrightarrow
c\,\Xi
}
\tag{7.2}
\]

locally uniformly on \(U\).

Proof. From (3), choose a subsequence with
\(|F_{j_k}(0)|\ge\varepsilon>0\). By normality, pass to a further subsequence
converging locally uniformly to \(F_\infty\). Pass again if necessary so that
\(F_{j_k}(0)\to c_0\); boundedness at \(0\) follows from local normality and
\(|c_0|\ge\varepsilon\).

For every \(t\in I\),

\[
F_\infty(t)
=
c_0\frac{\Xi(t)}{\Xi(0)}.
\]

Both sides are holomorphic on connected \(U\), and \(I\) has accumulation
points in \(U\). The identity theorem yields

\[
F_\infty(z)
=
\frac{c_0}{\Xi(0)}\Xi(z).
\]

Set \(c=c_0/\Xi(0)\ne0\). \(\square\)

### Corollary 7.2 — full-sequence C6 is not required by the terminal Hurwitz argument

Under the hypotheses of Theorem 7.1, the locally uniform subsequential limit
\(c\Xi\) has only real zeros in \(U\), by the same localized
Hurwitz/Rouché argument protected in R068. Because \(c\ne0\), \(c\Xi\) and
\(\Xi\) have identical zero multisets.

Thus the terminal critical-line implication requires only one admissible
nonzero Xi-shaped subsequential limit.

A theorem asserting full convergence of the whole family is stronger than the
terminal logic requires.

No terminal RH claim is admitted in this ordinary MATHSOLVE package.

---

## 8. Corrected Route C obligation state

After this repair:

- C0 — normalization: DISCHARGED by R056.
- C1 — cofinal admissible schedule: OPEN. R074's quadratic sufficiency
  theorem is withdrawn; R062 remains only a theorem about the obsolete R059
  trace mechanism.
- C2 — raw compact transform stability: DISCHARGED by R053.
- C3 — true/candidate approximation: OPEN. R074's finite Rayleigh
  inequality remains available, but no valid analytic truncation rate is yet
  protected. The preferred new interface is projective-measure convergence,
  e.g. TV or a weaker kernel-determining topology.
- C4 — normality: CONDITIONAL_ON_POINTWISE_POSITIVITY. The implication
  from positivity to strip normality is valid; the CCM positivity premise is
  not protected globally.
- C5 — identification: OPEN in the actual CCM campaign. R071's claimed
  conditional discharge is withdrawn. Theorem 7.1 supplies the corrected
  abstract identification gate.
- C6 — full convergence: OPTIONAL for the terminal logic. A nonzero
  \(c\Xi\) subsequential limit already suffices for the localized Hurwitz gate.
- C7 — localized Hurwitz: protected as a conditional terminal bridge; do
  not invoke until the hypotheses are actually met.

---

## 9. What remains mathematically hard

The repair isolates three genuine tasks instead of one over-strong convergence
problem.

### P1 — positivity or replacement

Prove that the relevant finite CCM ground states are pointwise nonnegative on
a cofinal admitted family, or obtain normality by a different exact theorem.

### P2 — projective candidate transfer

Show that the true projective state and the source candidate have the same
limiting shape in a topology that controls

\[
\int K_z\,d\nu.
\]

TV convergence is sufficient but may be stronger than necessary. Tight weak
convergence plus a kernel-determining argument is an admissible alternative.

### P3 — admissible cofinality

Prove existence of a cofinal sequence \((\lambda_j,N_j)\) on which the finite
CCM simple-even hypotheses required by Theorem 5.10 actually hold. Do not
replace this with a truncation-rate estimate.

These are now the only active structural gates before the terminal
subsequence argument.

---

## 10. False-proof firewall

Reject:

1. a boundary value at \(i/2\) as proof that an interior compact-open limit is
   nonzero;
2. pointwise ground-state positivity inferred from simple-evenness alone;
3. numerical positivity as a Jentzsch/Krein-Rutman theorem;
4. exponential decay of periodic Fourier coefficients from strip analyticity
   alone without endpoint matching;
5. the R074 quadratic schedule as a proved C1 theorem;
6. a raw \(L^2\) vector estimate as projective normalized-transform control
   without denominator/gauge analysis;
7. full-sequence convergence as a necessary terminal requirement;
8. invocation of the terminal RH implication before an actual admissible
   nonzero Xi-shaped subsequence is proved.

---

## 11. Admission disposition

Terminal candidate disposition:

RH-R077_INTEGRITY_REPAIR__PROJECTIVE_MEASURE_CLOSURE_PROVED__
POSITIVITY_PROJECTIVE_TRANSFER_COFINALITY_OPEN
