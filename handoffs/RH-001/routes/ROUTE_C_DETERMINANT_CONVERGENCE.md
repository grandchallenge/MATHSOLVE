# RH-001 Forward Route C — Determinant convergence to Xi

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

Prove local uniform convergence on C of a correctly normalized cofinal family of finite Zeta Spectral Triple determinants to the classical Xi function.

The protected terminal bridge is:

If entire functions F_j have only real zeros and

F_j -> Xi

locally uniformly on C, then Xi has only real zeros by Rouché/Hurwitz. Under the standard normalization, RH follows.

Therefore this route does not need to first construct one limiting self-adjoint operator.

This is the smallest exact terminal target presently known in the campaign.

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
- MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:
  reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md
- MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d:
  reports/discovery/rh_001/rh_r036_qw_parity_substrate.md
- MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b:
  reports/discovery/rh_001/rh_r037_finite_parity_galerkin.md
- AGENTS.md

Also acquire and read the exact primary CCM Zeta Spectral Triples source before asserting any normalization not already protected.

## 5. The proof-obligation chain

A useful decomposition is:

C0. Exact finite normalization. [DISCHARGED by RH-R056-CANONICAL-DETERMINANT-NORMALIZATION-001]

C1. Select and justify a cofinal parameter schedule.

C2. Establish a compact-set transform/determinant stability estimate. [DISCHARGED by RH-R053-COMPACT-TRANSFORM-STABILITY-001]

C3. Prove approximation of the true finite/full eigenvector by the source candidate strongly enough to use C2.

C4. Prove local boundedness / normal-family control of the normalized determinants. [DISCHARGED by RH-R068-STRIP-NORMAL-FAMILY-001 via universal strip modulus bound |F_{lambda,N}| <= 1/2 and Montel normality on S_{1/2}^circ]

C5. Identify every subsequential locally uniform limit with Xi. [DISCHARGED CONDITIONALLY on C3 candidate error rate by RH-R071-LIMIT-IDENTIFICATION-001 via sublinear strip stability transfer and zero-free quotient characterization]

C6. Conclude full local uniform convergence.

C7. Apply the already-protected R035 Rouché/Hurwitz bridge.

An agent does not need to solve C0-C7 in one tranche. Clean progress on one dependency is meaningful.

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

Status: PARTIALLY CONSTRAINED by RH-R062-UNTOUCHED-LATTICE-TAIL-001.

The family has two parameters.

Do not write lambda,N -> infinity without specifying what that means.

If the schedule is intended to use the RH-R059 positive-resolvent-trace
criterion for C4, RH-R062 proves the necessary scale
\[
N(\lambda)=\Omega((\log\lambda)^2).
\]
Indeed the untouched scaling complement alone contributes
\[
T_{a,N}
=
\sum_{j>N}\frac1{(\pi j/a)^2+1/4},
\qquad a=\log\lambda,
\]
and \(T_{a,N}\to\infty\) whenever \(N=o(a^2)\).  This does not prove
cofinal admissibility or sufficiency of a quadratic schedule; it only rules out
subquadratic schedules for the R059 mechanism.

Possible outputs:

- prove convergence uniformly for all sufficiently large N=N(lambda);
- identify a source-mandated relation N(lambda);
- prove diagonal extraction is sufficient;
- define a cofinal directed set and formulate the theorem as a net.

The chosen indexing must preserve every hypothesis needed for finite self-adjointness and real zeros.

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

The protected R035 source audit identifies the source's k_lambda approximation as a named missing theorem.

The task is not merely to show

||k_lambda-xi_lambda|| -> 0.

One needs a rate/norm strong enough to feed C2.

A good contribution can be:

- determine the exact required rate from C2;
- prove that a known source estimate is insufficient;
- derive a stronger variational estimate;
- exploit the spectral gap to convert Rayleigh-quotient error into eigenvector error.

This is a natural place where Route A/B can feed Route C: a quantitative simple-even spectral gap can turn energy approximation into vector approximation through Davis-Kahan/min-max style estimates.

## 10. C4 — Normal-family route

Status: PARTIALLY REDUCED by RH-R059-PAIRED-ZERO-NORMAL-FAMILY-001.

R059 first proves that the R056 properties alone are insufficient for the
planned Montel route. At the protected anchor \(\eta=1/2\),

\[
F_n(z)=\frac12\left(\frac{4(1-z^2)}5\right)^n
\]

is even, entire, has only real zeros, and satisfies \(F_n(i/2)=1/2\), but is
not locally bounded at \(z=2\).

R059 then gives a sufficient criterion. For an even entire function of order at
most one with real zeros, write the zero at the origin with multiplicity
\(2m_0\) and positive zeros \(x>0\) with paired multiplicities \(m_x\). Define

\[
Q_\eta(F)
=
\frac{m_0}{\eta^2}
+
\sum_{x>0}\frac{m_x}{x^2+\eta^2}.
\]

For a family with common nonzero anchor \(F(i\eta)=c\), a uniform bound

\[
Q_\eta(F)\le C_Q
\]

implies the explicit compact-disc estimate

\[
\sup_{|z|\le R}|F(z)|
\le
|c|
\exp\!\left(
2\eta^2C_Q\log_+(R/\eta)
+
(R^2-\eta^2)_+C_Q
\right).
\]

Hence the family is locally bounded and Montel applies.

For the R056-normalized admitted CCM determinants at \(\eta=1/2\), the
protected zero/spectrum identification turns the sufficient quantity into

\[
Q_{1/2}(F_{\lambda,N})
=
\frac12
\operatorname{Tr}
\left(
(D_{\log}^{(\lambda,N)})^2+\frac14I
\right)^{-1}.
\]

This does **not** discharge C4 for the CCM family. The concrete remaining C4
obligation is to prove a uniform bound on this paired-zero/resolvent-trace
quantity along an admitted cofinal family, or to replace it with another
uniform condition strong enough to imply local boundedness.

RH-R062 further decomposes the R059 burden.  The untouched complement
\(E_N^\perp\) contributes
\[
T_{a,N}
=
\sum_{j>N}\frac1{(\pi j/a)^2+1/4},
\qquad a=\log\lambda,
\]
with exact bracket
\[
\frac{2a}{\pi}\arctan\frac{a}{2\pi(N+1)}
\le T_{a,N}\le
\frac{2a}{\pi}\arctan\frac{a}{2\pi N}.
\]
Hence \(N=o(a^2)\) is impossible for uniform R059 control,
\(N\sim\kappa a^2\) leaves the positive limit \(1/(\pi^2\kappa)\), and
\(N\gg a^2\) makes only this complement tail vanish.

RH-R065 resolves the finite \(E_N'\) block and the full trace \(Q_{\lambda,N}\).
Due to strict spectral interlacing \(0 < \mu_1 < \pi/a < \dots < \mu_N < \pi N/a\)
with the scaling lattice, the finite block satisfies
\[
B_{a,N} > \sum_{j=1}^N \frac{1}{(\pi j/a)^2+1/4}.
\]
Combined with the untouched complement tail, the exact Mittag-Leffler identity for \(\coth\) gives
\[
Q_{\lambda,N} = B_{a,N} + T_{a,N} > a\coth(a/2) - 2 > \log\lambda - 2.
\]
Thus \(Q_{\lambda,N} \to \infty\) linearly in \(\log\lambda\) along every cofinal family.
The R059 positive resolvent trace condition is structurally too strong for CCM,
and C4 normal-family control must use localized/scale-invariant criteria.

RH-R068 resolves C4 by proving that for the R056-normalized determinants
\(F_{\lambda,N}(z) = \widehat{\xi}_{\lambda,N}(z)/(2\widehat{\xi}_{\lambda,N}(i/2))\),
ground-state positivity \(\xi_{\lambda,N} \ge 0\) and hyperbolic convexity imply
\(|F_{\lambda,N}(z)| \le 1/2\) for all \(z \in S_{1/2} = \{z : |\operatorname{Im} z| \le 1/2\}\)
uniformly in \(\lambda > 1\) and \(N \ge 1\). By Montel's theorem, \(\{F_{\lambda,N}\}\)
forms a normal family on the open strip \(S_{1/2}^\circ = \{z : |\operatorname{Im} z| < 1/2\}\).
Furthermore, the Strip Hurwitz Bridge ensures that all zeros of any non-trivial subsequential
limit in \(S_{1/2}^\circ\) are real, corresponding biholomorphically under \(s = 1/2 + iz\)
to zeros on the critical line \(\operatorname{Re}(s) = 1/2\) in the Riemann critical strip.
Obligation C4 is completely discharged; lane RH-R071 is reserved for C5 limit identification.

## 11. C5 — Identify the limit as Xi

A subsequential entire limit with real zeros is not enough. It must be Xi.

The identification theorem must also control normalization. Multiplying Xi by a nonzero entire exponential factor preserves zeros but is not equality to Xi.

For the RH bridge, convergence to any nonvanishing entire multiple of Xi may be enough if that factor is rigorously known never to vanish. If using this relaxation:

1. state it explicitly;
2. prove the factor is zero-free;
3. update the protected R035 bridge or prove the generalized version.

Do not silently change the target.

RH-R071 proves that on any closed substrip \(S_\delta \subset S_{1/2}^\circ\) (\(0 < \delta < 1/2\)), the transform stability growth is strictly sublinear: \(\sqrt{\mathcal{H}_a(\delta)} = O(\lambda^\delta) = o(\sqrt{\lambda})\). Consequently, any \(L^2\) candidate error \(\|\xi_{\lambda,N} - k_\lambda\|_{L^2} = o(\lambda^{-\delta})\) guarantees that \(F_{\lambda,N} \to \Xi\) uniformly on compact subsets of \(S_\delta\), connecting directly to the CCM §7 prolate convergence theorem (which provides \(O(\lambda^{-2})\)). Furthermore, for any subsequential limit \(F_\infty\), the quotient \(\Phi = F_\infty / \Xi\) is holomorphic, even, and satisfies the anchor \(\Phi(i/2) = 1\); non-vanishing of \(\Phi\) guarantees that all zeros of \(\Xi\) in \(S_{1/2}^\circ\) are real. Lane RH-R074 is reserved for C3 quantitative eigenvector error bounds.

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
3. a cofinal-index theorem [PARTIALLY CONSTRAINED: RH-R062 rules out N=o((log lambda)^2) for the R059 mechanism];
4. a Montel/local-boundedness theorem [DELIVERED: RH-R068 proves universal strip modulus bound |F_{lambda,N}| <= 1/2, Montel normality on S_{1/2}^\circ, and Strip Hurwitz Bridge; supersedes the divergent R059 trace criterion];
5. a rigorous k_lambda-to-xi_lambda estimate;
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
