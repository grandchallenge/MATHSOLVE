# RH-001 — Handoff

## Target repository and authority

Target work repository: grandchallenge/MATHSOLVE.

INTELLECT work-package phase: not applicable; this is a mathematics-domain campaign. MATHSOLVE owns theorem development. MATHFORGE owns source/prior-art evidence. MATHCERT alone may render a later bounded certification disposition.

## Purpose

Advance the Solve-native spectral route beyond the qualified RH interface while preserving the open RH claim boundary and requiring exact operator-class audits before selection.

## Parallel forward route packs

Three durable zero-context execution packs are maintained under:

- handoffs/RH-001/routes/ROUTE_A_LOCAL_ANALYTIC_CONTINUATION.md
- handoffs/RH-001/routes/ROUTE_B_HERGLOTZ_CONTINUATION.md
- handoffs/RH-001/routes/ROUTE_C_DETERMINANT_CONVERGENCE.md

Index and coordination rules:

- handoffs/RH-001/routes/README.md

Copy-ready zero-context prompts:

- handoffs/RH-001/routes/prompts/ROUTE_A_ZERO_CONTEXT.txt
- handoffs/RH-001/routes/prompts/ROUTE_B_ZERO_CONTEXT.txt
- handoffs/RH-001/routes/prompts/ROUTE_C_ZERO_CONTEXT.txt

Long-lived coordination trackers:

- grandchallenge/MATHSOLVE#411 — Route A, local analytic simple-even continuation
- grandchallenge/MATHSOLVE#412 — Route B, Herglotz margin continuation
- grandchallenge/MATHSOLVE#414 — Route C, determinant convergence to Xi

Independent agents should enter through the relevant route pack, claim one bounded subproblem in the corresponding tracker, re-fetch protected state, and protect reusable intermediate results before another route depends on them.

Routes A and B are parallel mechanisms for the CCM simple-even obstruction. Route C attacks the determinant-convergence terminal bridge directly and may consume quantitative spectral-gap results from A/B, but it must not assume global simple-evenness from the current local theorem.

## Current protected lineage

- RH-T-000: open and unproved.
- MATHCERT: qualified_interface_only for the canonical statement interface.
- RH-D-009 route audit: grandchallenge/MATHFORGE@da746ee38823e408321b9e417649f5b837ec5627.
- RH-R030-SPECTRAL-UNBOUNDED-001: proved in work_packages/RH_R030_SPECTRAL_UNBOUNDED.md.
- Exact half-line Berry–Keating audit: grandchallenge/MATHFORGE@a6a2e7d65adef8eaf977d77bbacbd05786d7da47.
- RH-R031-BK-HALFLINE-LEBESGUE-001: proved in work_packages/RH_R031_BK_HALFLINE_LEBESGUE.md.
- Exact fixed finite-interval Berry–Keating audit: grandchallenge/MATHFORGE@c49d7507dd45338f6328141c7d708acb5806e702.
- RH-R032-BK-FINITE-INTERVAL-WEYL-001: proved in work_packages/RH_R032_BK_FINITE_INTERVAL_WEYL.md.
- Exact symmetric Berry–Keating T log T audit: grandchallenge/MATHFORGE@d0365dba53e20395bbd2c3b6b17959cde94b6fbe.
- RH-R033-SYMMETRIC-BK-TLOGT-001: proved in work_packages/RH_R033_SYMMETRIC_BK_TLOGT.md.
- Exact Rindler prime-mirror fixed-domain audit: grandchallenge/MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a.
- RH-R034-RINDLER-PRIME-FIXED-DOMAIN-001: proved in work_packages/RH_R034_RINDLER_PRIME_FIXED_DOMAIN.md.
- Exact Zeta Spectral Triples limiting-contract audit: grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790.
- RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001: proved in work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md.
- Exact Weil-form parity substrate audit: grandchallenge/MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d.
- RH-R036-QW-PARITY-GAP-REDUCTION-001: proved in work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md.
- Exact finite parity/Galerkin substrate audit: grandchallenge/MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b.
- RH-R037-QW-SECTOR-GALERKIN-001: proved in work_packages/RH_R037_QW_SECTOR_GALERKIN.md.
- Claimed Krein–Rutman closure audit: grandchallenge/MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a.
- RH-R039-QW-PARITY-GAP-EVIDENCE-001: executed in work_packages/RH_R039_QW_PARITY_GAP_EVIDENCE/.
- Small-a full-operator source audit: grandchallenge/MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320.
- RH-R040-EFFECTIVE-SMALL-A-SIMPLE-EVEN-001: proved in work_packages/RH_R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN.md.
- RH-R045-PARITY-SENSITIVE-REMAINDER-001: proved in work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md.
- Pole/resolvent provider interface: grandchallenge/MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648.
- RH-R053-COMPACT-TRANSFORM-STABILITY-001: proved in work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md.

No operator construction satisfying the Hilbert–Pólya contract, RH implication, novelty, or priority claim is admitted.

## Current substantive result

The spectral route now has three exact necessary-condition / no-go results and three positive-control / frontier-isolation results.

1. No bounded operator can have spectrum containing all positive zeta-zero ordinates. Any exact raw-ordinate Hilbert–Pólya operator must therefore be unbounded.
2. The canonical half-line Berry–Keating dilation generator

\[
H_{BK}^+=-i\left(x\frac{d}{dx}+\frac12\right)
\]

on \(L^2((0,\infty),dx)\) is unitarily equivalent under \(y=\log x\) to momentum on \(L^2(\mathbb R)\). Its spectrum is all of \(\mathbb R\), purely absolutely continuous with multiplicity one, and its point spectrum is empty. It therefore fails the discrete raw-ordinate eigenvalue contract despite satisfying the mandatory unboundedness condition.
3. A fixed finite-interval self-adjoint Berry–Keating realization has arithmetic spectrum and positive counting

\[
N_H(T)=\frac{\log(b/a)}{2\pi}T+O(1),
\]

whereas Riemann–von Mangoldt requires leading growth \(T\log T/(2\pi)\). Thus fixed finite-interval compactification restores discreteness but cannot reproduce the raw zeta-zero ordinate multiset.
4. Berry and Keating's 2011 symmetric cutoff-free model supplies a fixed self-adjoint discrete operator family whose source-derived smooth count reproduces the first two Riemann counting terms under the source normalization: the \(t\log t\) term and the linear \(-t\) term. The source's later smooth corrections differ, and its periodic dynamics do not supply the prime-labelled orbit family associated with the oscillatory zeta term. This is a positive control for the smooth-counting gate, not an exact zeta realization.
5. Sierra's Rindler mirror construction supplies independently specified prime-labelled arithmetic structure through mirror geometry and Möbius reflection data, including \(\log p\) orbit periods. Its published exact-zero point-state construction nevertheless fine-tunes the self-adjoint boundary phase to the target zero and therefore does not establish one fixed all-zero operator. The source's RH-like conclusion also retains RH-conditional, simple-zero, formal-residue, and limiting assumptions.
6. Connes–Consani–Moscovici's Zeta Spectral Triples construction supplies zero-list-independent, prime-built finite self-adjoint spectral approximants with real spectra and an exact regularized-determinant formula under the source's simple-even hypothesis. The exact missing boundary is convergence. A locally uniform normalized-determinant convergence theorem to \(\Xi\) would already force RH by Rouché/Hurwitz; one limiting self-adjoint operator is sufficient but not logically necessary for that bridge.
7. Inversion symmetry of the full semilocal Weil form propagates to its canonical self-adjoint operator \(A_\lambda\), which splits into even and odd reducing sectors. The source's first missing theorem, 'simple-even ground state,' is exactly equivalent to two narrower obligations: simplicity of the lowest even eigenvalue and the strict parity gap \(\epsilon_+(\lambda)<\epsilon_-(\lambda)\).
8. The exact finite parity blocks form sector-wise Galerkin approximants: \(\epsilon_{\pm,N}(\lambda)\downarrow\epsilon_\pm(\lambda)\), hence finite gaps \(g_N\to g\). Finite parity calculations now have a rigorous interpretation, but positivity of finitely many gaps is not a proof of the full gap without a certified tail bound.
9. R039 implements the protected CCM finite matrices at 50/80 digits with 96/128/160-point high-precision quadrature. For \(\lambda^2=13,14\), all retained gaps through \(N=12\) are positive and stable far beyond their displayed scale, but they collapse rapidly: at \(N=12\), \(g_N\approx1.46\times10^{-26}\) and \(1.84\times10^{-27}\), respectively. This is controlled finite evidence only and supplies no positive tail certificate.
10. The full localized Weil operator is now controlled analytically near \(\lambda=1\). RH-R040 gives an explicit simple-even interval \(0<a=\log\lambda\le1/16\) and strict positivity through \(a\le1/50\). RH-R045 sharpens the structural interval to \(0<a\le2/15\). RH-R046 reaches \(a\le1/7\), RH-R047 reaches \(a\le3/20\), RH-R048 reaches \(a\le1/6\), RH-R049 reaches \(a\le17/100\), and RH-R050 reaches \(a\le171/1000\). RH-R051 proves an exact rank-one coercivity theorem (\(\mu_{-,1}>\log 2+3/20\)) and a sharp parity-specific remainder bound (\(\|K_{a,-}\|\le (8/\pi^2)L a^2 < (811/1000)La^2\)), extending the full simple-even theorem through
\[
0<a\le\frac{178}{1000}.
\]
Uniformly on that interval,
\[
\epsilon_-(e^a)-\epsilon_+(e^a)>\frac{55428698889}{23675000000000},
\]
and
\[
\epsilon_{+,2}(e^a)-\epsilon_{+,1}(e^a)>\frac{1783634369}{11837500000}.
\]
Thus the first CCM simple-even obstruction is fully discharged through \(a=178/1000\).

This sharpens the protected operator contract:

\[
\text{unbounded}
\not\Rightarrow
\text{useful discrete spectrum},
\]

and

\[
\text{spectral containment}
\neq
\text{point-spectrum correspondence}
\neq
\text{complete discrete spectral realization}.
\]

## Authoritative pointers

- grandchallenge/INTELLECT:CONSTITUTION.md
- grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json
- grandchallenge/INTELLECT:governance/handoffs/README.md
- grandchallenge/MATHSOLVE:AGENTS.md
- grandchallenge/MATH-PROGRAMME#163
- grandchallenge/MATH-PROGRAMME:campaigns/riemann_hypothesis/WP02_THEOREM_LEDGER/02_THEOREM_LEDGER.json
- grandchallenge/MATH-PROGRAMME:campaigns/riemann_hypothesis/WP01_FALSE_PROOF_ATLAS/01_ATLAS.json
- grandchallenge/MATHFORGE@da746ee38823e408321b9e417649f5b837ec5627:reports/discovery/rh_001/rh_d009_r030_prior_art.md
- grandchallenge/MATHFORGE@a6a2e7d65adef8eaf977d77bbacbd05786d7da47:reports/discovery/rh_001/rh_r031_bk_halfline_prior_art.md
- grandchallenge/MATHFORGE@c49d7507dd45338f6328141c7d708acb5806e702:reports/discovery/rh_001/rh_r032_bk_finite_interval_prior_art.md
- grandchallenge/MATHFORGE@d0365dba53e20395bbd2c3b6b17959cde94b6fbe:reports/discovery/rh_001/rh_r033_bk_symmetric_tlogt_prior_art.md
- grandchallenge/MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a:reports/discovery/rh_001/rh_r034_rindler_prime_fixed_domain.md
- grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md
- grandchallenge/MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d:reports/discovery/rh_001/rh_r036_qw_parity_substrate.md
- grandchallenge/MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b:reports/discovery/rh_001/rh_r037_finite_parity_galerkin.md
- grandchallenge/MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a:reports/discovery/rh_001/rh_r038_krein_rutman_claim_audit.md
- grandchallenge/MATHSOLVE#257
- grandchallenge/MATHSOLVE#345
- grandchallenge/MATHSOLVE#347
- grandchallenge/MATHSOLVE#351
- grandchallenge/MATHSOLVE#358
- grandchallenge/MATHSOLVE#363
- grandchallenge/MATHSOLVE#366
- grandchallenge/MATHSOLVE#369
- grandchallenge/MATHSOLVE#376
- work_packages/RH_R030_SPECTRAL_UNBOUNDED.md
- work_packages/RH_R031_BK_HALFLINE_LEBESGUE.md
- work_packages/RH_R032_BK_FINITE_INTERVAL_WEYL.md
- work_packages/RH_R033_SYMMETRIC_BK_TLOGT.md
- work_packages/RH_R034_RINDLER_PRIME_FIXED_DOMAIN.md
- work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- work_packages/RH_R037_QW_SECTOR_GALERKIN.md
- work_packages/RH_R039_QW_PARITY_GAP_EVIDENCE/README.md
- work_packages/RH_R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN.md
- work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- work_packages/RH_R042_PARITY_BOTTOM_PARAMETER_CONTINUITY.md
- work_packages/RH_R043_HERGLOTZ_MARGIN_CONTINUITY.md
- work_packages/RH_R044_EXPLICIT_INITIAL_HERGLOTZ_MARGINS.md
- work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- work_packages/RH_R046_ODD_LOWER_BOUND_EXTENSION.md
- work_packages/RH_R047_INTEGRATED_REMAINDER_EXTENSION.md
- work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- work_packages/RH_R049_HIGHER_ODD_COERCIVITY.md
- work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- work_packages/RH_R051_RANK_ONE_COERCIVITY_EXTENSION.md
- work_packages/RH_R052_REFRESHED_HERGLOTZ_MARGINS.md
- work_packages/RH_R053_COMPACT_TRANSFORM_STABILITY.md
- work_packages/RH_R039_QW_PARITY_GAP_EVIDENCE/evidence.json
- work_packages/RH_R039_QW_PARITY_GAP_EVIDENCE/evidence.csv
- scripts/rh_r039_qw_parity_gap.py
- MathSolve/RH/SpectralUnbounded.lean

## Smallest safe next tranche

The finite-evidence question has been overtaken by stronger full-operator theorems near \(\lambda=1\). The current explicit structural boundary is

\[
a=\log\lambda=\frac{178}{1000}.
\]

The continuation machinery is now in place:

1. RH-R041 gives the exact odd rank-one Herglotz trichotomy;
2. RH-R042 proves continuity of the even/odd spectral bottoms and of the full parity gap;
3. RH-R043 proves continuity of the pole-localization margin \(d(a)\) and the Herglotz margin \(\Delta_H(a)\) on their natural domain and classifies first failure through \(d=0\) or \(\Delta_H=0\);
4. RH-R044 supplies explicit positive continuation margins through \(a=2/15\);
5. RH-R046 reaches \(a=1/7\);
6. RH-R047 reaches \(a=3/20\);
7. RH-R048 reaches \(a=1/6\);
8. RH-R049 reaches \(a=17/100\);
9. RH-R050 retains the \(u^8/4\) logarithmic-potential term and reweights the positive even trial to reach \(a=171/1000\);
10. RH-R051 proves an exact rank-one coercivity theorem and sharp parity-specific remainder bound to reach \(a=178/1000\);
11. RH-R052 refreshes explicit positive Herglotz continuation margins \(d(a)>\frac{55428698889}{23675000000000}\) and \(\Delta_H(a)\ge\frac{1210515093544258}{12367528439608125}\) through \(a=178/1000\);
12. RH-R053 discharges C2 of Route C by proving exact compact-set transform stability bounds \(\sup_{z\in K}|\lambda^{-iz}\widehat{\xi}-\lambda^{-iz}\widehat{\psi}|\le e^{\sigma_{\max}a}\sqrt{\mathcal{H}_a(H)}\|\xi-\psi\|_{L^2}\), an even-parity refinement, Rayleigh-quotient to eigenvector error transfer, and the rate dichotomy showing bare \(L^2\) bounds require C4 normal families for full complex-plane convergence.

The explicit parity-gap margin at the new endpoint is positive but very small. Further retuning of the same one-parameter trial family is therefore not a preferred research direction. The smallest useful next theorem should make a structural improvement, preferably one of:

- a genuinely richer positive even trial space with an analytic upper bound;
- a stronger odd-sector coercivity inequality not based only on truncating the logarithmic series;
- a quantitative variation theorem for the protected \(d/\Delta_H\) Herglotz continuation interface.

The R039 finite-Galerkin route remains an independent diagnostic at larger \(a\), but it is not the smallest next theorem.

The determinant route remains an exact sufficient terminal bridge: locally uniform convergence of normalized finite determinants, whose zeros are real, to \(\Xi\) forces RH.

## Material dependencies and boundaries

RH-R030 imports the classical Riemann–von Mangoldt conclusion that positive zero ordinates are unbounded and the standard bounded-spectrum theorem.

RH-R031 imports standard momentum/Fourier spectral theory. Its source status and exact prior-art boundary are fixed by the protected Forge audit. RH-R032 imports the classical Riemann–von Mangoldt counting interface and elementary finite-interval momentum spectral theory; its exact source boundary is protected at MATHFORGE@c49d7507dd45338f6328141c7d708acb5806e702. RH-R033 imports the Berry–Keating 2011 operator-theoretic and asymptotic results from the protected provider audit at MATHFORGE@d0365dba53e20395bbd2c3b6b17959cde94b6fbe; Solve proves only the governed comparison and design consequence. RH-R034 imports Sierra's Rindler mirror source analysis from the protected audit at MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a; Solve records the fixed-domain and circularity consequences without certifying the limiting source construction. RH-R035 imports the finite Zeta Spectral Triples theorem and the source's named missing steps from MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790; Solve adds the standard Rouché/Hurwitz determinant-convergence bridge and isolates the minimal sufficient convergence target. RH-R036 imports inversion symmetry, canonical self-adjoint representation, and discreteness from MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d; Solve proves operator commutation and the exact parity-gap reduction. RH-R037 imports exact finite parity matrices and the full form core from MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b; Solve proves parity-sector core density, monotone sector-minimum convergence, and finite-gap convergence. R039 uses only those protected CCM formulas for finite high-precision parity-gap evidence; MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a separately rejects a claimed Krein–Rutman closure as insufficient to supersede the protected frontier. R040 imports Suzuki's full-operator small-a structure from MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320 and derives an explicit effective regime. R045 sharpens that regime using parity-sensitive control of the same source remainder. R046 strengthens the limiting odd-sector coercivity and extends the no-prime analytic route through a=1/7. R047 refines the integrated smooth-remainder control and extends the same route through a=3/20. R048 strengthens the limiting even and odd coercivity estimates and extends the route through a=1/6. R049 retains the next positive logarithmic-potential term and extends the route through a=17/100. R050 combines the next logarithmic term with a reweighted positive even trial and reaches a=171/1000. R051 combines exact rank-one coercivity with a sharp parity-specific remainder bound and reaches a=178/1000. R052 refreshes explicit Herglotz continuation margins through a=178/1000. RH-R053 discharges C2 of Route C by proving exact compact-set transform stability bounds, an even-parity refinement, Rayleigh-to-eigenvector error transfer, and the rate dichotomy proving bare L2 bounds require C4 normal families on C. MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648 binds the exact CCM pole split used by R041-R044. No numerical zero fitting is used.

MATHCERT interaction is not presently material. A later Cert route is appropriate only for a bounded new mathematical claim with an exact proof/checker surface.

## Reserved authority / stop conditions

Stop for a material change to the canonical RH normalization, a source contradiction that changes the selected spectral target, a route strengthening beyond the protected Forge audit, a request to claim RH/novelty/priority/publication readiness, or an actual reserved INTELLECT transition.

Routine theorem development, source audit, testing, non-authoring audit passes, protected merge, and readback remain delegated.

## Notes intentionally omitted

This handoff intentionally omits the WP00–WP02 history, generic constitutional doctrine, the complete theorem ledger, CI transcripts, and the old review ceremony. Those records remain authoritative at their existing locations.
