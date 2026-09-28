# OM26-SRC-COLLATZ-MODULAR-DESCENT — zero-context source-acquisition work package

**Campaign:** `OPENMATH-2026`  
**CEX operation:** `OM26-H2-H7-SOURCE-ACQ`  
**Assignment ID:** `OM26-SRC-COLLATZ-MODULAR-DESCENT`  
**Organizer hill ID:** `alejandrozu/collatz-modular-descent`  
**Class:** `SOURCE_ACQUISITION`

## Execution gate

This document is the complete GCL work-set for this assignment.

Before doing substantive work, read protected `main:.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json`.

Proceed only if the record for `OM26-SRC-COLLATZ-MODULAR-DESCENT` has:
- `state = LEASED`;
- `lease.dispatch_id` equal to the dispatch ID supplied in your launch message;
- `lease.agent_ref` equal to your launch identity.

Otherwise return exactly `NO_ACTIVE_LEASE: OM26-SRC-COLLATZ-MODULAR-DESCENT` and stop.

Do not self-claim this assignment. Do not substitute another organizer hill.

## Known state

An authenticated AutoLab list receipt observed at `2026-09-28T10:05:25Z` establishes `alejandrozu/collatz-modular-descent` as one of the six unresolved OpenMath organizer hill IDs.

It does **not** establish which placeholder slot OM26-H2 through OM26-H7 this hill will eventually occupy. List position is not slot identity.

Canonical organizer list:

`https://app.autolab.ai/lists/alejandrozu/openmath`

Authenticated receipt in GCL:

`work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json`

## Objective

Acquire organizer-authoritative evidence sufficient for MATHFORGE to source-lock `alejandrozu/collatz-modular-descent`, or return a precise external acquisition blocker.

A successful acquisition should establish, from authoritative evidence:
- exact title;
- exact statement body or authenticated render/export;
- external version identifier, if exposed, otherwise an observation timestamp;
- evaluator/checker identity and operative semantics when available;
- authoritative source references;
- remaining semantic or provenance hazards.

## Required method

1. Perform non-mutating reconnaissance first.
2. Acquire the exact organizer record for `alejandrozu/collatz-modular-descent`.
3. Capture authoritative bytes or an authenticated render/export where available.
4. Capture evaluator/checker semantics when available.
5. Preserve any unavailable field as unknown.
6. Prepare evidence suitable for the MATHFORGE source-lock packet.
7. Do not assign this hill to an H2-H7 slot.
8. Do not start proof, construction search, optimization, or theorem attack.

## Completion dispositions

Return one of:

- `ACQUIRED_AUTHORITATIVE_SOURCE_RECORD`: the exact hill statement and provenance evidence are sufficient for Forge source-lock construction.
- `PRECISE_EXTERNAL_ACQUISITION_BLOCKER`: name the exact inaccessible source, authentication boundary, or evidentiary ambiguity and what was attempted.

A plausible reconstruction is not a third disposition.

## Prohibited actions

- Do not work on `alejandrozu/kobon-triangles` / OM26-H1.
- Do not map `alejandrozu/collatz-modular-descent` to H2-H7 by list position, name similarity, memory, or event prose.
- Do not reuse another hill's evaluator semantics by analogy.
- Do not claim theorem truth, novelty, optimality, competition acceptance, or MATHCERT certification.
- Do not submit a competition entry.
- Do not mutate the assignment registry.

## Return

Use only the exact GitHub return surface and exact result grammar named by the protected lease/dispatch record. If those are absent, stop with `NO_ACTIVE_LEASE: OM26-SRC-COLLATZ-MODULAR-DESCENT`.

The returned object is evidence for later GCL adjudication. Receipt does not change canonical mathematical claim state.

## Successor gate

After MATHFORGE protects a source lock for `alejandrozu/collatz-modular-descent`, GCL may explicitly bind it to one free OM26-H2 through OM26-H7 slot. Only after that protected binding may hill-specific mathematical CEX packages be instantiated.

## Claim boundary

This assignment can establish source identity or a precise acquisition blocker. It cannot establish mathematical correctness, novelty, certification, slot identity, or competition acceptance.
