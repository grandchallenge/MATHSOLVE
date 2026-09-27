# OPENMATH-2026 Solve orchestration

**Solve tracker:** `grandchallenge/MATHSOLVE#454`  
**Programme tracker:** `grandchallenge/MATH-PROGRAMME#1072`  
**Programme bootstrap:** `grandchallenge/MATH-PROGRAMME#1073`  
**Current state:** `OM26-H1_ACTIVE__FIVE_HILLS_PENDING_FORGE_LOCK`

## Purpose

Operate the tactical research layer for the OpenMath 2026 six-hill sprint. MATHSOLVE owns decomposition, route selection, failure accounting, exact screens, restricted targets, CEI handoffs, and certification packets. It does not certify results.

## Release rule

A hill lane is released only when its MATHFORGE source-lock packet identifies the exact external hill statement and provenance.

OM26-H1 (`alejandrozu/kobon-triangles`) is now released under protected MATHFORGE commit `73f1890387eec56eb6be31f8c00f10b6a5a56383`. OM26-H2 through OM26-H6 remain blocked; unresolved hill content must not be guessed.

## First active hill

The durable work package is `work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES/`. Its first gate is independent exact reproduction of the displayed `n=18` baseline score 16, followed by agreement with the AutoLab local evaluator. Final competition submission is separately blocked on live hill concordance.

## Proof-quality checkpoint rule

Before starting another expensive route, record exact counterexamples, reusable lemmas, reduced targets, missing-hypothesis diagnoses, replayable certificates, library gaps, and route-killing obstructions. Negative information is campaign output.

## Submission boundary

An OpenMath checker result, competition acceptance, CI success, or external contribution does not create a MATHCERT disposition. Every claim-bearing result must state its exact claim, dependencies, source lock, producer provenance, replay path, semantic-fidelity risks, and requested Cert modality.
