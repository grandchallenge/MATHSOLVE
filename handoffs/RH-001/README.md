# RH-001 — Handoff

## Target repository and authority

Target work repository: grandchallenge/MATHSOLVE.

INTELLECT work-package phase: not applicable; this is a mathematics-domain campaign. MATHSOLVE owns theorem development. MATHFORGE owns source/prior-art evidence. MATHCERT alone may render a later bounded certification disposition.

## Purpose

Advance the Solve-native spectral route beyond the qualified RH interface while preserving the open RH claim boundary and requiring exact operator-class audits before selection.

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

No operator construction satisfying the Hilbert–Pólya contract, RH implication, novelty, or priority claim is admitted.

## Current substantive result

The spectral route now has three exact necessary-condition / no-go results and two positive-control results.

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
- grandchallenge/MATHSOLVE#257
- grandchallenge/MATHSOLVE#345
- grandchallenge/MATHSOLVE#347
- grandchallenge/MATHSOLVE#351
- grandchallenge/MATHSOLVE#358
- work_packages/RH_R030_SPECTRAL_UNBOUNDED.md
- work_packages/RH_R031_BK_HALFLINE_LEBESGUE.md
- work_packages/RH_R032_BK_FINITE_INTERVAL_WEYL.md
- work_packages/RH_R033_SYMMETRIC_BK_TLOGT.md
- work_packages/RH_R034_RINDLER_PRIME_FIXED_DOMAIN.md
- MathSolve/RH/SpectralUnbounded.lean

## Smallest safe next tranche

Select the next spectral class by fixed-domain arithmetic selection, not by individual level fit. RH-R033 shows the smooth \(T\log T-T\) count can arise from one fixed self-adjoint model, and RH-R034 shows prime-labelled \(\log p\) structure can be specified independently of the zero list. The missing composition is now one fixed energy-independent self-adjoint domain plus a rigorous limiting operator whose point spectrum is selected noncircularly by that arithmetic structure.

Before Solve selection, MATHFORGE must audit current literature for either a fixed-domain repair of the Rindler/prime-mirror route or a different fixed self-adjoint construction with prime-labelled trace/orbit structure and no zero-dependent parameters. Hard-coding the known zero ordinates, spectral determinant, or Riemann–Siegel phase into adjustable domain data does not satisfy this gate.

## Material dependencies and boundaries

RH-R030 imports the classical Riemann–von Mangoldt conclusion that positive zero ordinates are unbounded and the standard bounded-spectrum theorem.

RH-R031 imports standard momentum/Fourier spectral theory. Its source status and exact prior-art boundary are fixed by the protected Forge audit. RH-R032 imports the classical Riemann–von Mangoldt counting interface and elementary finite-interval momentum spectral theory; its exact source boundary is protected at MATHFORGE@c49d7507dd45338f6328141c7d708acb5806e702. RH-R033 imports the Berry–Keating 2011 operator-theoretic and asymptotic results from the protected provider audit at MATHFORGE@d0365dba53e20395bbd2c3b6b17959cde94b6fbe; Solve proves only the governed comparison and design consequence. RH-R034 imports Sierra's Rindler mirror source analysis from the protected audit at MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a; Solve records the fixed-domain and circularity consequences without certifying the limiting source construction. No numerical zero fitting is used.

MATHCERT interaction is not presently material. A later Cert route is appropriate only for a bounded new mathematical claim with an exact proof/checker surface.

## Reserved authority / stop conditions

Stop for a material change to the canonical RH normalization, a source contradiction that changes the selected spectral target, a route strengthening beyond the protected Forge audit, a request to claim RH/novelty/priority/publication readiness, or an actual reserved INTELLECT transition.

Routine theorem development, source audit, testing, non-authoring audit passes, protected merge, and readback remain delegated.

## Notes intentionally omitted

This handoff intentionally omits the WP00–WP02 history, generic constitutional doctrine, the complete theorem ledger, CI transcripts, and the old review ceremony. Those records remain authoritative at their existing locations.
