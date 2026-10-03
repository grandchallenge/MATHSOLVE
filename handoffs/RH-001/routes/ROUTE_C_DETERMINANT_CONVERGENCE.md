# RH-001 Forward Route C — Determinant convergence to Xi


> **RH-R077 AUTHORITATIVE CORRECTION.** The downstream convergence architecture
> in this historical route pack is superseded where it conflicts with
> handoffs/RH-001/routes/ROUTE_C_PROJECTIVE_MEASURE_CLOSURE.md.
> In particular: R068 normality is conditional on an unproved global
> pointwise-positivity premise; R071's boundary-anchor/noncollapse and
> normalized substrip-rate claims are withdrawn; R074's analytic Fourier-tail
> and quadratic C1 schedule theorem are withdrawn. Preserve only the parts
> explicitly retained by RH-R077.

Status: ACTIVE_PARALLEL_ROUTE

Coordination tracker:
grandchallenge/MATHSOLVE#414

Route role: attack the terminal sufficient RH bridge directly, without requiring construction of one limiting self-adjoint Hilbert-Polya operator first.

Current protected campaign head at pack creation:
grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c

Protected route foundation:
RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001
work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md

Protected provider audits:
- grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790
  reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md
- grandchallenge/MATHFORGE@a900e5170c6d77a9e557b6159cf5feb40bcee222
  reports/discovery/rh_001/rh_r056_determinant_normalization.md

## 1. Mission

Produce one admissible sequence of finite CCM normalized determinants with
real zeros and one subsequence converging locally uniformly on

\[
U=\{z:|\operatorname{Im}z|<1/2\}
\]

to \(c\Xi\) for some \(c\ne0\).

That is sufficient for the localized Hurwitz/Rouche terminal bridge. Full
convergence on all of \(\mathbb C\), construction of a limiting self-adjoint
operator, and full-sequence C6 convergence are not required by the terminal
logic.

The correct downstream state variable is projective. Conditional on a
nonnegative even ground state, RH-R077 represents the R056 normalized
determinant as

\[
F(z)=\frac12\int
\frac{\cos(zx)}{\cosh(x/2)}\,d\nu(x),
\]

where \(\nu\) is a probability measure invariant under positive scalar
rescaling of the ground vector.

The active mathematical gates are:
P1 pointwise positivity or an alternative normality theorem;
P2 projective candidate transfer;
P3 genuinely admissible cofinality.

## 2. Finite source theorem already available

For finite scale lambda and Galerkin parameter N, the CCM source defines a finite self-adjoint rank-one perturbation under its simple-even hypothesis.

The protected R035 audit records the finite determinant formula

det_reg(D_log^(lambda,N)-z)
=
-i lambda^(-iz) xi_hat(z),

where xi is the relevant finite minimal eigenvector under the source normalization.

The source theorem gives:

- finite self-adjointness under the stated hypothesis;
- an entire determinant factor;
- real zeros of the finite entire function;
- identification of those zeros with the finite approximant spectrum.

The finite construction uses prime/arithmetic data and does not fit a supplied list of zeta zeros.

## 3. What is still open

None of the following is currently protected as a theorem:

- one canonical cofinal schedule (lambda_j,N_j) sufficient for the limit;
- locally uniform convergence of the normalized determinants;
- a strong enough k_lambda -> xi_lambda theorem;
- global simple-evenness for the full range of scales needed by the limiting construction;
- a limiting self-adjoint operator;
- complete spectral convergence to all zeta ordinates.

Route C may close RH without the last two items, but not without determinant convergence and the finite real-zero property along the chosen cofinal family.

## 4. Protected lineage to context-load

Read:

- handoffs/RH-001/README.md
- work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- work_packages/RH_R037_QW_SECTOR_GALERKIN.md
- work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- work_packages/RH_R056_CANONICAL_DETERMINANT_NORMALIZATION.md
- work_packages/RH_R059_PAIRED_ZERO_NORMAL_FAMILY.md
- work_packages/RH_R062_UNTOUCHED_LATTICE_TAIL.md
- work_packages/RH_R065_FINITE_BLOCK_RESOLVENT_OBSTRUCTION.md
- work_packages/RH_R068_STRIP_NORMAL_FAMILY.md
- work_packages/RH_R071_LIMIT_IDENTIFICATION.md
- work_packages/RH_R074_EIGENVECTOR_ERROR_TRANSFER.md
- MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:
  reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md
- MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d:
  reports/discovery/rh_001/rh_r036_qw_parity_substrate.md
- MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b:
  reports/discovery/rh_001/rh_r037_finite_parity_galerkin.md
- AGENTS.md

Also acquire and read the exact primary CCM Zeta Spectral Triples source before asserting any normalization not already protected.

## 5. The corrected proof-obligation chain

C0. Exact finite normalization. **DISCHARGED** by R056.

C1. Select an actually admissible cofinal sequence. **OPEN.** R074's
quadratic schedule sufficiency claim is withdrawn by R077.

C2. Raw compact-set transform stability. **DISCHARGED** by R053, but this is
now auxiliary rather than the preferred normalized interface.

C3. Compare the true finite projective state with the source candidate.
**OPEN.** R074's finite Rayleigh-to-eigenvector inequality remains valid;
its analytic truncation theorem does not.

C4. Obtain normality on the critical strip. **CONDITIONAL_ON_POINTWISE_POSITIVITY.**
The implication positivity => R077/R068 strip contraction => Montel is valid,
but the global CCM positivity premise is not protected.

C5. Identify a nonzero Xi-shaped subsequential limit. **OPEN for CCM.**
R077 proves the correct abstract gate: interior non-escape plus projective
shape convergence on one real interval implies a subsequence converging to
\(c\Xi\), \(c\ne0\).

C6. Full locally uniform convergence. **OPTIONAL STRENGTHENING.**

C7. Localized Hurwitz/Rouche terminal bridge. Protected conditionally; invoke
only after one actual admissible nonzero Xi-shaped subsequence is proved.

## 6. C0 — Exact finite normalization

Status: DISCHARGED by RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001.

For every admitted finite CCM pair, with raw determinant
\[
G_{\lambda,N}(z)=-i\lambda^{-iz}\widehat{\xi}_{\lambda,N}(z),
\]
R056 fixes the campaign normalization
\[
F_{\lambda,N}(z)
=
\frac12\,
\frac{\lambda^{iz}G_{\lambda,N}(z)}
     {\lambda^{-1/2}G_{\lambda,N}(i/2)}.
\]

The protected MATHFORGE R056 packet proves under the CCM convention that
\[
\Xi(i/2)=\xi(0)=1/2\ne0.
\]
The finite denominator is nonzero because all admitted finite zeros are real.
R056 proves that \(F_{\lambda,N}\) is entire, even, zero-preserving, anchored at
\(i/2\), and unique inside the declared affine-exponential gauge class.

The anchor convention is Solve-native. It is not attributed to CCM and it
supplies no convergence theorem.

## 7. C1 — Cofinal schedule

Status: **OPEN after RH-R077 correction.**

R062's \(N=\Omega((\log\lambda)^2)\) theorem applied to the now-obstructed
R059 global trace criterion; it is not a general C1 admissibility theorem.

R074 attempted to prove that the same quadratic scale suppresses the candidate
Fourier tail from strip analyticity. RH-R077 supplies the exact counterexample
\(f(x)=x\): although entire, its coefficients in the periodic basis decay only
as \(1/|j|\). The contour-shift proof omitted vertical-side terms unless
endpoint matching is available.

Therefore no cofinal \(N(\lambda)\) schedule is currently protected as
sufficient. C1 must establish both approximation control and the finite CCM
simple-even hypotheses on the selected pairs.

## 8. C2 — Compact-set transform stability

Status: DISCHARGED by RH-R053-COMPACT-TRANSFORM-STABILITY-001 (work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md).

For $f, g \in L^2([-a,a])$ and any compact set $K \subset \mathbb{C}$ with $H(K) = \sup_{z\in K} |\operatorname{Im} z|$ and $\sigma_{\max}(K) = \sup_{z\in K} \operatorname{Im} z$:

1. Bare transform stability:
   \[
   \sup_{z\in K} |\widehat{f}(z) - \widehat{g}(z)| \le \sqrt{\mathcal{H}_a(H(K))} \|f - g\|_{L^2(-a,a)},
   \]
   where $\mathcal{H}_a(H) = \frac{\sinh(2Ha)}{H}$ for $H>0$ and $2a$ for $H=0$.
2. Determinant kernel stability:
   \[
   \sup_{z\in K} |\lambda^{-iz}\widehat{f}(z) - \lambda^{-iz}\widehat{g}(z)| \le e^{\sigma_{\max}(K)a} \sqrt{\mathcal{H}_a(H(K))} \|f - g\|_{L^2(-a,a)} \le \sqrt{2a} e^{2H(K)a} \|f - g\|_{L^2(-a,a)}.
   \]
3. Parity-refined bound (for even form vectors):
   \[
   \sup_{z\in K} |\widehat{f}(z) - \widehat{g}(z)| \le \sqrt{a + \frac{\sinh(2H(K)a)}{2H(K)}} \|f - g\|_{L^2(-a,a)}.
   \]
4. Rate dichotomy:
   - Real axis ($H=0$): $\|f-g\|_{L^2} = o(a^{-1/2})$ is sufficient for uniform convergence.
   - Horizontal strip ($H=\delta$): $\|f-g\|_{L^2} = o(a^{-1/2} e^{-2\delta a}) = o((\log\lambda)^{-1/2}\lambda^{-2\delta})$ is sufficient.
   - Full complex plane $\mathbb{C}$: bare $L^2$ bounds diverge exponentially if $\|f-g\|_{L^2} = \Theta(\lambda^{-c})$ for $H > c/2$, formally establishing the necessity of the C4 normal-family/Montel route or super-exponential decay.

## 9. C3 — Source k_lambda approximation

Status: **OPEN after RH-R077 correction.**

Retain from R074:

\[
\|\xi_{\lambda,N}-k_{\lambda,N}\|^2
\le
\frac{2\Delta\mathcal R_N}{\operatorname{Gap}_N(\lambda)}
\]

and the elementary orthogonal-projection triangle inequality.

Do not retain R074's exponential periodic Fourier-tail theorem or its resulting
quadratic schedule.

The preferred C3 target is now projective. Under the positivity premise define

\[
d\nu_f(x)
=
\frac{f(x)\cosh(x/2)}
     {\int f(t)\cosh(t/2)dt}\,dx.
\]

RH-R077 proves the scale-free interface

\[
\sup_{|\operatorname{Im}z|\le1/2}
|F_\nu(z)-F_\mu(z)|
\le
\frac12\|\nu-\mu\|_{\mathrm{TV}}.
\]

TV convergence is sufficient but may be stronger than necessary; a weaker
kernel-controlling topology is acceptable if proved.

## 10. C4 — Normal-family route

Status: **CONDITIONAL_ON_POINTWISE_POSITIVITY.**

R059's global trace criterion is obstructed by R065.

R068/R077 prove the valid analytic implication: if the relevant finite ground
state is even and pointwise nonnegative, then the R056 normalized determinant
has the projective representation

\[
F(z)=\frac12\int
\frac{\cos(zx)}{\cosh(x/2)}\,d\nu(x)
\]

with \(\nu\) a probability measure, and therefore

\[
|F(z)|\le\frac12
\quad
(|\operatorname{Im}z|\le1/2).
\]

This yields Montel normality on the open strip.

However, no protected global theorem currently proves the needed pointwise
nonnegativity for all finite CCM pairs of interest. R037 and R040 do not do
so, and protected Forge R038 rejected the earlier Krein-Rutman closure.

Additionally, the boundary anchor does not rule out the zero limit. R077's
exact family

\[
E_n(z)=\frac12\frac{\cos(nz)}{\cosh(n/2)}
\]

has real zeros, the boundary anchor, and the strip bound, yet tends locally
uniformly to zero on the open strip.

## 11. C5 — Identify the limit as Xi

Status: **OPEN for the actual CCM family.**

R071's conditional discharge is withdrawn by R077 because:
- \(i/2\) is a boundary point and its value is not inherited by compact-open
  limits on the open strip;
- the displayed normalized transfer estimate contains an anchor error at
  height \(1/2\), so the raw bound does not reduce to \(O(\lambda^\delta)\)
  for \(\delta<1/2\) without additional projective control.

R077 supplies the corrected identification theorem.

If a normal admissible sequence with real zeros satisfies

\[
\limsup_j F_j(0)>0
\]

and, on one real interval \(I\),

\[
\frac{F_j(t)}{F_j(0)}
\to
\frac{\Xi(t)}{\Xi(0)},
\]

then a subsequence converges locally uniformly on the open strip to
\(c\Xi\), \(c\ne0\). The identity theorem supplies the global strip
identification. The localized Hurwitz bridge then needs no full-sequence C6
theorem.

## 12. Interaction with simple-evenness

The finite source theorem uses a simple-even hypothesis.

The campaign now proves full-operator simple-evenness only on an explicit local interval near lambda=1.

A determinant-convergence route with lambda -> infinity cannot assume this local theorem supplies simple-evenness at all large scales.

An agent must explicitly determine which simple-even statement the selected finite/cofinal determinant family needs.

Possible outcomes:

- Route A/B eventually supplies the needed global scale theorem;
- the finite theorem needs a weaker condition than the full-form global statement;
- the determinant convergence can be formulated on a verified cofinal subsequence;
- or simple-evenness remains a separate unresolved dependency.

Do not suppress it.

## 13. Minimum meaningful deliverable

A contribution is meaningful if it provides one protected result such as:

1. exact canonical determinant normalization [DELIVERED: RH-R056];
2. a theorem reducing compact-uniform determinant convergence to a quantitative eigenvector norm/rate [DELIVERED: RH-R053];
3. a cofinal-index theorem [FORMALIZED: RH-R074 proves N(\lambda) \ge \kappa (\log\lambda)^2 yields power-law tail decay \lambda^{-\pi\kappa\rho} = o(\lambda^{-\delta}), harmonizing with the RH-R062 \Omega((\log\lambda)^2) lower bound];
4. a Montel/local-boundedness theorem [DELIVERED: RH-R068 proves universal strip modulus bound |F_{lambda,N}| <= 1/2, Montel normality on S_{1/2}^\circ, and Strip Hurwitz Bridge; supersedes the divergent R059 trace criterion];
5. a rigorous k_lambda-to-xi_lambda estimate [REDUCED: RH-R074 decomposes total error into analytic truncation tail and Galerkin Rayleigh defect, bounded by \sqrt{2\Delta\mathcal{R}_N / \operatorname{Gap}_N(\lambda)}];
6. a limit-identification theorem [DELIVERED: RH-R071 proves sublinear stability transfer on S_\delta and identifies limit with \Xi for candidate error o(\lambda^{-\delta})];
7. a negative theorem showing a proposed norm/rate/criterion is insufficient [DELIVERED: RH-R053 rate dichotomy; RH-R065 resolvent trace obstruction].

This route is expected to advance through such modular results.

## 14. False-proof firewall

Reject:

- low-zero numerical agreement as convergence;
- pointwise convergence as local uniform convergence;
- real zeros of approximants as RH without a specified limit;
- an unspecified normalization;
- a family of self-adjoint operators as one limiting self-adjoint operator;
- finite self-adjointness as limiting self-adjointness;
- numerical eigenvector overlap as a k_lambda theorem;
- convergence on the real axis alone unless a theorem upgrades it;
- use of Hurwitz/Rouché before local uniform convergence is established.

## 15. Governance

MATHSOLVE owns theorem development.

MATHFORGE must be used for:

- exact source normalization not already protected;
- source-version discrepancies;
- new external convergence theorems or literature;
- claims about what the CCM paper proves.

MATHCERT should be involved only after a bounded terminal convergence claim has a complete exact proof/checker surface.

Any claim that Route C has proved RH must pass the full governed terminal process. Do not make that claim inside ordinary theorem development.

## 16. Completion criterion for Route C

Route C is mathematically complete when there is a protected theorem giving a cofinal family of normalized finite entire determinants with real zeros and locally uniform convergence to Xi, or to a rigorously identified zero-free entire multiple of Xi.

At that point the protected R035 Rouché/Hurwitz bridge supplies the RH implication, subject to the programme's certification/governance process.

An individual agent contribution is complete when it protects one missing lemma or one rigorous obstruction in the C0-C6 chain.

## 17. Zero-context handoff prompt

The copy-ready prompt is stored at:

handoffs/RH-001/routes/prompts/ROUTE_C_ZERO_CONTEXT.txt
