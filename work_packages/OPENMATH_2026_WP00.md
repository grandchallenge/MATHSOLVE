# OPENMATH-2026-WP00 — sprint orchestration and hill-release gate

**Solve tracker:** `grandchallenge/MATHSOLVE#454`  
**Programme tracker:** `grandchallenge/MATH-PROGRAMME#1072`  
**Initial state:** `BLOCKED_PER_HILL_PENDING_FORGE_SOURCE_LOCK`

## Purpose

Create the tactical orchestration layer for six OpenMath 2026 hill slots while preserving the existing MATHFORGE -> MATHSOLVE -> MATHCERT authority split.

This Work Package does not restate or infer unresolved hill content. It prepares the machinery that starts once MATHFORGE releases an exact source/status lock.

## Hill lanes

Reserved identities:

- `OM26-H1`
- `OM26-H2`
- `OM26-H3`
- `OM26-H4`
- `OM26-H5`
- `OM26-H6`

A hill transitions from `BLOCKED_PER_HILL_PENDING_FORGE_SOURCE_LOCK` to `READY_FOR_OBLIGATION_DECOMPOSITION` only when its Forge packet contains an exact statement identity, source trail, dated status boundary, and downstream certification-route sketch.

## Per-hill obligation graph

Each released hill should be decomposed into distinct obligations rather than copied wholesale to many agents.

```text
semantic fidelity / source lock
        |
        +--> formal definitions and library prerequisites
        +--> reduction / normal-form route
        +--> restricted-case route
        +--> exact-computational route
        +--> falsification / counterexample route
        +--> zero-context CEI route where fully specifiable
        |
        v
candidate claim graph
        |
        v
adjudication and witness minimization
        |
        v
MATHCERT handoff
```

## Shared sprint work

The following shared work may proceed before hill release:

1. formal prover/certificate environment inventory;
2. submission/checker contract audit;
3. common claim-ledger and provenance templates;
4. CEI dispatch template;
5. common library-gap inventory;
6. exact artifact/disclosure checklist.

No shared artifact may imply a claim about an unresolved hill.

## Route discipline

For each obligation:

- name the exact claim or construction target;
- state imported lemmas and excluded assumptions;
- name the falsification condition;
- bound expensive computation;
- preserve failed routes before disposal;
- checkpoint any proof-quality intermediate result before opening a new expensive branch;
- minimize discovery output into a smaller replayable witness when possible.

## Anti-duplication rule

Parallelism means different obligations or materially different methods, not many agents receiving the same full hill with the same context.

Use duplicate whole-hill attempts only when the purpose is explicitly independent reconstruction or adversarial comparison.

## Claim ledger states

Recommended working states:

- `UNBOUND_EXTERNAL_TARGET`
- `SOURCE_LOCKED`
- `CONJECTURAL_ROUTE`
- `EXACT_EVIDENCE_ONLY`
- `FORMALIZATION_READY`
- `HANDOFF_READY`
- `CERT_PENDING`
- `CERT_QUALIFIED`
- `CERT_REJECTED`

MATHSOLVE may create or advance only the non-certification states. Certification states are read from MATHCERT.

## Completion

WP00 is complete when:

- six exact Forge locks or authoritative list-change dispositions are available;
- a Solve campaign manifest binds exact Programme and Forge identities;
- each released hill has an obligation graph and deterministic next action;
- shared environment/checker/provenance infrastructure is recorded;
- no unresolved hill has been silently promoted into mathematical work.

## Claim boundary

This Work Package organizes work only. It does not prove a hill, establish novelty, certify a formal artifact, or imply competition acceptance.
