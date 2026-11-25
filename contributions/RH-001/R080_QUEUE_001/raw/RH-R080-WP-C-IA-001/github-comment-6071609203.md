GCL-CONTRIBUTION-RESULT/1
dispatch_id: RH-R080-WP-C-IA-001
agent_ref: INDEPENDENT-AGENT-RH-R080-C
assignment: RH-R080-WP-C
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
1. Exact Signed Projective Representation and Modulus Bound:
Let a > 0, and let f in L^1([-a, a]) be real-valued and even. Assume the anchor integral
A(f) := int_0^a f(x) cosh(x/2) dx != 0.
Define the normalized signed projective measure on [0, a]:
dmu_f(x) := (f(x) cosh(x/2) / A(f)) dx,  satisfying  mu_f([0, a]) = 1,
and the signed condition number:
kappa(f) := ||mu_f||_TV = int_0^a |f(x)| cosh(x/2) dx / |A(f)|.
With the protected projective kernel K_z(x) := cos(zx) / cosh(x/2), the normalized transform
F_f(z) := widehat{f}(z) / (2 widehat{f}(i/2)) = (1 / (2 A(f))) int_0^a f(x) cos(zx) dx
admits the exact representation:
F_f(z) = (1/2) int_0^a K_z(x) dmu_f(x).
Because |K_z(x)| <= 1 on the closed strip |Im(z)| <= 1/2, the exact uniform modulus bound holds:
sup_{|Im(z)| <= 1/2} |F_f(z)| <= (1/2) kappa(f).

2. Montel Normality without Pointwise Positivity:
Let S = {z in C : |Im(z)| < 1/2}. If a sequence of real even states (f_j)_{j=1}^infty in L^1([-a_j, a_j]) satisfies
sup_j kappa(f_j) <= M < infinity,
then (F_{f_j})_{j=1}^infty is uniformly bounded on S by M/2.
By Montel's Theorem, (F_{f_j}) is a normal family on S: every subsequence has a subsequence converging locally uniformly on S to a holomorphic function F_infty.
Furthermore, the normalization anchor F_{f_j}(i/2) = 1/2 implies F_infty(i/2) = 1/2, strictly preventing escape to the zero function (F_infty not identically 0).

3. Exact Positivity Characterization and Sign-Defect Identity:
(a) For every admissible f, kappa(f) >= 1.
(b) Equality kappa(f) = 1 holds if and only if f has definite sign almost everywhere on [0, a] (i.e. f(x) >= 0 a.e. if A(f) > 0, or f(x) <= 0 a.e. if A(f) < 0).
(c) The exact sign-defect identity is:
    kappa(f) = 1 + (2 / |A(f)|) int_{f(x) sgn(A(f)) < 0} |f(x)| cosh(x/2) dx.
Thus kappa(f) smoothly quantifies the total relative cancellation caused by negative sectors.

4. Source-Specific Reduction to Discharge C4:
Pointwise nonnegativity xi_N(x) >= 0 is strictly stronger than needed to establish critical-strip Montel normality.
To discharge obligation C4 for the CCM Galerkin family (xi_N)_{N=1}^infty, it is sufficient that:
limsup_{N -> infinity} kappa(xi_N) < infinity,
which requires only that the weighted negative-sector mass does not asymptotically overwhelm the anchor integral A(xi_N).

## Derivation

1. Kernel Bound on the Critical Strip:
For z = t + is with |s| <= 1/2 and x in [0, a]:
|cos(zx)|^2 = cos(tx)^2 cosh(sx)^2 + sin(tx)^2 sinh(sx)^2 = cos(tx)^2 + sinh(sx)^2 <= 1 + sinh(sx)^2 = cosh(sx)^2.
Since |s| <= 1/2 and x >= 0, the function s -> cosh(sx) is convex and even, so cosh(sx) <= cosh(x/2).
Therefore:
|K_z(x)| = |cos(zx)| / cosh(x/2) <= cosh(sx) / cosh(x/2) <= 1.

2. Modulus Bound:
Using the total variation of the measure mu_f:
|F_f(z)| = |(1/2) int_0^a K_z(x) dmu_f(x)| <= (1/2) int_0^a |K_z(x)| |dmu_f(x)| <= (1/2) sup_{x in [0, a]} |K_z(x)| ||mu_f||_TV <= (1/2) kappa(f).
This bound is sharp: at z = i/2, K_{i/2}(x) = cosh(x/2)/cosh(x/2) = 1, giving F_f(i/2) = (1/2) int_0^a 1 dmu_f(x) = 1/2. When kappa(f) = 1, |F_f(i/2)| = 1/2 = (1/2) kappa(f).

3. Characterization of Extremal Rays (kappa = 1):
Since int_0^a dmu_f(x) = 1, the triangle inequality gives:
1 = |int_0^a dmu_f(x)| <= int_0^a |dmu_f(x)| = kappa(f).
Equality holds in L^1 iff dmu_f(x) has a constant complex phase a.e., which for real measures means dmu_f(x) >= 0 a.e.
By definition, dmu_f(x) = f(x) cosh(x/2) / A(f). Since cosh(x/2) > 0, dmu_f(x) >= 0 a.e. iff f(x) / A(f) >= 0 a.e.
If A(f) > 0, this means f(x) >= 0 a.e. If A(f) < 0, this means f(x) <= 0 a.e.
Thus kappa(f) = 1 characterizes precisely the projective rays of definite sign.
Splitting f = f_+ - f_- where f_+, f_- >= 0 have disjoint support:
If A(f) > 0: A(f) = int f_+ cosh - int f_- cosh = P - N.
Then int |f| cosh = P + N = (P - N) + 2N = A(f) + 2N.
Dividing by A(f) yields kappa(f) = 1 + 2 N / A(f), proving the sign-defect formula.

4. Strict Substrip Sharpening:
On a strict substrip S_delta = {z : |Im(z)| <= delta} with 0 <= delta < 1/2:
|K_z(x)| <= cosh(delta * x) / cosh(x/2) <= 1.
Define kappa_delta(f) := (1 / |A(f)|) int_0^a |f(x)| cosh(delta * x) dx.
Then sup_{z in S_delta} |F_f(z)| <= (1/2) kappa_delta(f) <= (1/2) kappa(f).
Locally uniform boundedness on S requires only that kappa_delta(f_j) is bounded for each delta in [0, 1/2).

5. Separation of Normality and Anti-Collapse:
Montel's theorem requires only equicontinuity / local uniform boundedness (supplied by kappa_j <= M).
Non-triviality of the limit F_infty is guaranteed independently by the boundary anchor:
For every j, F_{f_j}(i/2) = 1/2.
If F_{f_{j_k}} -> F_infty locally uniformly on S, evaluating at the fixed point z = i/2 in S gives F_infty(i/2) = 1/2.
Hence F_infty cannot be identically zero. No separate anti-collapse condition is required.

## Assumptions beyond bootstrap
NONE. Relies entirely on the protected packet (CCM Theorem 5.10, Galerkin parity definitions, RH-R077 projective kernel K_z), standard L^1 measure theory, and classical complex analysis (Montel's theorem).

## Verification / falsification hooks
1. Sanity Replay Script:
   Execute python scripts/rh_r080_signed_projective_check.py to verify:
   (a) piecewise_f_integral satisfies |F_f(z)| <= (1/2) kappa(f) across test points in the strip;
   (b) sign-defect identity kappa = 1 + 2N/A holds to machine precision;
   (c) projective invariance under non-zero scalar scaling f -> c * f.
2. Analytic Check:
   Verify that |cos(zx)|^2 = cos(tx)^2 + sinh(sx)^2 <= cosh(sx)^2 <= cosh(x/2)^2 for |s| <= 1/2.
3. Falsification Criterion:
   Any real even function f with A(f) != 0 and a point z with |Im(z)| <= 1/2 where |F_f(z)| > (1/2) kappa(f) would immediately falsify the theorem.

## Claim boundary
This return proves that bounded signed condition number kappa(f_j) <= M is mathematically sufficient for Montel normality of normalized Fourier transforms on the critical strip, completely bypassing pointwise nonnegativity.
It does NOT prove that the actual continuum CCM ground state has bounded kappa as N -> infinity, nor does it certify the Riemann Hypothesis or global determinant convergence.

## Next residual
Compute kappa(xi_N) on the finite CCM Galerkin ground states for increasing N to confirm whether kappa(xi_N) remains empirically bounded near 1 as N increases.
