# RH-001 Route C — Projective Measure Closure Architecture

Status: ACTIVE_CANONICAL_REFRAME

Introduced by:
RH-R077-PROJECTIVE-MEASURE-REPAIR-001

Extended by:
RH-R080-SIGNED-PROJECTIVE-NORMALITY-001

Coordination:
grandchallenge/MATHSOLVE#414
grandchallenge/MATHSOLVE#742

This file is the authoritative Route C architecture after RH-R077.  Where older
Route C material conflicts with this file, RH-R077 controls.

## 1. Terminal objective

The terminal argument does not require convergence on all of C and does not
require full-sequence convergence.

Let

\[
U=\{z\in\mathbb C:|\operatorname{Im}z|<1/2\}.
\]

It is sufficient to produce one admissible sequence of finite CCM normalized
determinants \(F_j\), all with real zeros, and one subsequence such that

\[
F_{j_k}\longrightarrow c\,\Xi
\]

locally uniformly on \(U\), for some \(c\ne0\).

The localized Hurwitz/Rouche argument then transfers zero reality to \(\Xi\)
inside \(U\).  Under \(s=1/2+iz\), \(U\) is exactly the Riemann critical strip.

Full C6 convergence is therefore optional strengthening, not a terminal
logical requirement.

## 2. Correct state variable

After R056 phase removal and scalar normalization, the relevant state is
projective.

For any real even form state \(f\) with nonzero boundary anchor
\[
A(f)=\int_0^a f(x)\cosh(x/2)\,dx\ne0,
\]
RH-R080 defines the signed projective measure
\[
d\mu_f(x)
=
\frac{f(x)\cosh(x/2)}{A(f)}\,dx,
\qquad
\mu_f([0,a])=1.
\]
Then
\[
F_f(z)
=
\frac12\int
K_z(x)\,d\mu_f(x),
\qquad
K_z(x)=\frac{\cos(zx)}{\cosh(x/2)}.
\]

The positive probability-measure representation from R077 is the special
sign-definite case.  The signed representation:

- removes arbitrary nonzero real scalar normalization;
- separates pointwise positivity from the actual normal-family requirement;
- measures cancellation through the variation of the normalized signed state;
- retains the R077 kernel and projective-transfer viewpoint.

## 3. Kernel facts

For \(|\operatorname{Im}z|\le1/2\),

\[
|K_z(x)|\le1.
\]

For every \(\delta<1/2\),

\[
\sup_{|\operatorname{Im}z|\le\delta}|K_z(x)|
\le
2e^{-(1/2-\delta)x}.
\]

Hence mass moving to \(x=\infty\) becomes invisible on compact subsets of the
open strip while remaining visible at the boundary anchor.

The exact counterexample is

\[
E_n(z)=\frac12\frac{\cos(nz)}{\cosh(n/2)}.
\]

It has only real zeros, \(E_n(i/2)=1/2\), and the R068 strip modulus bound, yet
\(E_n\to0\) locally uniformly on \(U\).

Therefore \(F(i/2)=1/2\) is not an anti-collapse theorem.

## 4. Minimal identification gate

The preferred terminal-facing theorem is:

If an admissible sequence \(F_j\)

1. is locally bounded on \(U\) (hence normal);
2. has only real zeros;
3. satisfies \(F_j(0)\ne0\) and \(\limsup |F_j(0)|>0\);
4. satisfies projective shape convergence on one real interval \(I\),
   \[
   \frac{F_j(t)}{F_j(0)}
   \to
   \frac{\Xi(t)}{\Xi(0)},
   \]

then a subsequence converges locally uniformly to \(c\Xi\), \(c\ne0\).

The identity theorem upgrades interval identification to the full connected
strip.  No boundary anchor is used.

## 5. Preferred transfer topology

For finite signed/complex measures \(\nu,\mu\),

\[
\sup_{|\operatorname{Im}z|\le1/2}
|F_\nu(z)-F_\mu(z)|
\le
\frac12\|\nu-\mu\|_{\mathrm{TV}}.
\]

Thus total-variation convergence of projective measures is sufficient for
uniform transform convergence on the entire closed strip.

TV may be stronger than necessary.  A weaker tight/vague or
kernel-determining topology is acceptable if proved to control the family
\(K_z\).

Raw \(L^2\) convergence is no longer the preferred interface because scalar
normalization and the boundary denominator must be controlled separately.

## 6. Corrected obligation map

C0 — finite canonical normalization:
DISCHARGED by RH-R056.

C1 — cofinal admissible schedule:
OPEN.
R074's claimed analytic Fourier-tail proof is withdrawn by R077 because strip
analyticity does not imply exponential decay of periodic Fourier coefficients
without endpoint matching.

C2 — raw transform stability:
DISCHARGED by RH-R053.
Useful as an auxiliary theorem, not the preferred projective interface.

C3 — true/candidate state transfer:
OPEN.
The finite Rayleigh-to-eigenvector inequality from R074 remains valid.
The preferred output is projective-measure convergence.

C4 — normal-family control:
REDUCED BY RH-R080 TO SIGNED-PROJECTIVE CONTROL; ACTUAL CCM BOUND OPEN.
For
\[
\kappa_\delta(f)
=
\frac{\int_0^a|f(x)|\cosh(\delta x)\,dx}
     {|A(f)|},
\qquad 0\le\delta\le1/2,
\]
RH-R080 proves
\[
\sup_{|\operatorname{Im}z|\le\delta}|F_f(z)|
\le\frac12\kappa_\delta(f).
\]
Therefore C4 follows if, on an admitted cofinal family,
\[
\forall\delta<1/2,\quad
\sup\kappa_\delta(\xi_{\lambda,N})<\infty.
\]
Pointwise sign-definiteness is only the extremal boundary case
\(\kappa_{1/2}=1\), not a necessary C4 hypothesis.

C5 — limit identification:
OPEN for the actual CCM family.
R077 provides the correct abstract gate: non-escape + projective shape
convergence on a real interval.

C6 — full local-uniform convergence:
OPTIONAL STRENGTHENING.
Not needed if one admissible nonzero Xi-shaped subsequence is obtained.

C7 — localized Hurwitz:
PROTECTED AS A CONDITIONAL TERMINAL BRIDGE.
Invoke only after its actual hypotheses are met.

## 7. Three active mathematical gates

### P1 — signed-projective normality

RH-R080 proves the exact hierarchy:

- **P1a:** pointwise sign-definiteness, equivalently
  \(\kappa_{1/2}=1\) after orienting the ground-state ray;
- **P1b:** a uniform closed-strip condition number
  \(\sup\kappa_{1/2}<\infty\);
- **P1c:** the weakest currently protected signed-projective C4 target,
  \[
  \forall\delta<1/2,\quad \sup\kappa_\delta<\infty.
  \]

Any of P1a/P1b/P1c on an admitted cofinal family yields the corresponding
normality conclusion; P1c already suffices on the open critical strip.
Actual CCM sign control remains open.

The RH-R080 blind cohort independently tests pointwise positivity,
counterexamples, and the positivity-free criterion.

### P2 — projective candidate transfer

Prove that the true finite projective state approaches the source candidate in
TV or a weaker proven kernel-controlling topology.

A Rayleigh-defect theorem is useful only if it can be converted into this
projective statement without hidden normalization assumptions.

### P3 — admissible cofinality

Produce a cofinal \((\lambda_j,N_j)\) sequence satisfying the finite CCM
simple-even hypotheses.

A truncation-rate choice for \(N(\lambda)\) is not by itself an admissibility
theorem.

## 8. Route A / B interface

Routes A and B matter to Route C only through concrete dependencies:

- isolation/simplicity of the desired ground-state ray;
- parity ordering needed for CCM finite admissibility;
- spectral-gap estimates that support projective candidate transfer.

Endpoint micro-extension has low priority unless it advances one of these
interfaces.

## 9. Next Route C lane

RH-R080 supplies the positivity-free signed-projective C4 theorem and staffs a
blind proof/falsification cohort for actual CCM pointwise positivity.

After RH-R080 protection, the next collision-free Route C identifier is
RH-R083.

Do not allocate R083 until the RH-R080 blind returns have been checked or the
native R080 theorem has been protected and the controller has selected the
smallest actual-family residual.  Likely successors are:

1. source-specific control of \(\kappa_\delta(\xi_{\lambda,N})\);
2. projective candidate-transfer estimates feeding P2; or
3. a certified finite positivity counterexample follow-up if WP-B returns one.

## 10. False-proof firewall

Reject:

- boundary-anchor preservation under compact-open convergence on the open strip;
- pointwise positivity from simple-evenness alone;
- numerical positivity as a Perron/Jentzsch theorem;
- exponential periodic Fourier decay from analyticity alone;
- R074's quadratic schedule as an admitted C1 theorem;
- full-sequence convergence as a necessary terminal condition;
- raw vector closeness without projective/gauge control;
- terminal claims before an admissible nonzero Xi-shaped subsequence is proved.
