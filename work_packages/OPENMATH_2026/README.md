# OPENMATH-2026 Solve orchestration

**Solve tracker:** `grandchallenge/MATHSOLVE#454`  
**Programme tracker:** `grandchallenge/MATH-PROGRAMME#1072`  
**Programme bootstrap:** `grandchallenge/MATH-PROGRAMME#1073`  
**Current state:** `HILL_SPECIFIC_WORK_BLOCKED_PENDING_FORGE_LOCK`

## Purpose

Operate the tactical research layer for the OpenMath 2026 six-hill sprint.

MATHSOLVE owns decomposition, theorem spines, route selection, failure accounting, exact screens, restricted targets, CEI handoffs, and certification packets. It does not certify results.

## Release rule

A hill lane is released only when the corresponding MATHFORGE source-lock packet identifies the exact external hill statement and provenance.

Until that point, shared orchestration work may proceed, but no hill-specific theorem statement is to be guessed.

## Standard live hill graph

```text
source/semantic lock
        |
        +--> S0 semantic fidelity
        +--> S1 formalization prerequisites
        +--> R1 representation / reduction
        +--> R2 restricted-case theorem
        +--> R3 exact-computational route
        +--> R4 falsification / counterexample
        +--> R5 independent CEI contribution
        |
        v
candidate claim graph
        |
        v
adjudication
        |
        v
MATHCERT handoff
```

Parallelism should diversify obligations, not duplicate the same full-problem prompt.

## Proof-quality checkpoint rule

Before starting another expensive route, durably record any:

- exact counterexample;
- reusable formal lemma;
- reduced equivalent target;
- missing-hypothesis diagnosis;
- replayable certificate;
- formal-library gap;
- route-killing obstruction.

Negative information is campaign output.

## Submission boundary

An OpenMath checker result, competition acceptance, CI success, or a plausible external contribution does not create a MATHCERT disposition.

Every claim-bearing result must state its exact claim, dependencies, source lock, producer provenance, replay path, semantic-fidelity risks, and requested Cert modality.
