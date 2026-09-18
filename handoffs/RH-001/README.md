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

No operator construction satisfying the Hilbert–Pólya contract, RH implication, novelty, or priority claim is admitted.

## Current substantive result

The spectral route now has two exact necessary-condition / no-go results.

1. No bounded operator can have spectrum containing all positive zeta-zero ordinates. Any exact raw-ordinate Hilbert–Pólya operator must therefore be unbounded.
2. The canonical half-line Berry–Keating dilation generator

\[
H_{BK}^+=-i\left(x\frac{d}{dx}+\frac12\right)
\]

on \(L^2((0,\infty),dx)\) is unitarily equivalent under \(y=\log x\) to momentum on \(L^2(\mathbb R)\). Its spectrum is all of \(\mathbb R\), purely absolutely continuous with multiplicity one, and its point spectrum is empty. It therefore fails the discrete raw-ordinate eigenvalue contract despite satisfying the mandatory unboundedness condition.

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
- grandchallenge/MATHSOLVE#257
- grandchallenge/MATHSOLVE#345
- work_packages/RH_R030_SPECTRAL_UNBOUNDED.md
- work_packages/RH_R031_BK_HALFLINE_LEBESGUE.md
- MathSolve/RH/SpectralUnbounded.lean

## Smallest safe next tranche

Audit one exact discretized Berry–Keating class before any numerical fitting.

The minimal candidate is \(H_{BK}\) on a finite interval \([a,b]\subset(0,\infty)\) with a self-adjoint quasi-periodic boundary condition. Under logarithmic coordinates this is momentum on a finite interval. The next proof-quality question is whether its exact eigenvalue counting law can satisfy Riemann–von Mangoldt.

A compact interval, compact quantum graph, altered boundary condition, modified Hilbert space, or rigged-space construction is a new operator class and requires its own exact MATHFORGE audit before Solve selection.

## Material dependencies and boundaries

RH-R030 imports the classical Riemann–von Mangoldt conclusion that positive zero ordinates are unbounded and the standard bounded-spectrum theorem.

RH-R031 imports standard momentum/Fourier spectral theory. Its source status and exact prior-art boundary are fixed by the protected Forge audit. No numerical zero data are used.

MATHCERT interaction is not presently material. A later Cert route is appropriate only for a bounded new mathematical claim with an exact proof/checker surface.

## Reserved authority / stop conditions

Stop for a material change to the canonical RH normalization, a source contradiction that changes the selected spectral target, a route strengthening beyond the protected Forge audit, a request to claim RH/novelty/priority/publication readiness, or an actual reserved INTELLECT transition.

Routine theorem development, source audit, testing, non-authoring audit passes, protected merge, and readback remain delegated.

## Notes intentionally omitted

This handoff intentionally omits the WP00–WP02 history, generic constitutional doctrine, the complete theorem ledger, CI transcripts, and the old review ceremony. Those records remain authoritative at their existing locations.
