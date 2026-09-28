# OM26-H2-SOURCE-ACQ — zero-context source-acquisition work package

**Campaign:** `OPENMATH-2026`  
**CEX operation:** `OM26-H2-H7-SOURCE-ACQ`  
**Assignment ID:** `OM26-H2-SOURCE-ACQ`  
**Slot:** `OM26-H2`  
**Class:** `SOURCE_ACQUISITION`

## Execution gate

This document is the complete GCL work-set for this assignment.

Before doing substantive work, read protected `main:.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json`.

Proceed only if the record for `OM26-H2-SOURCE-ACQ` has:
- `state = LEASED`;
- `lease.dispatch_id` equal to the dispatch ID supplied in your launch message;
- `lease.agent_ref` equal to your launch identity.

Otherwise return exactly `NO_ACTIVE_LEASE: OM26-H2-SOURCE-ACQ` and stop.

Do not self-claim this assignment. Do not substitute another slot.

## Known state

`OM26-H2` is an unresolved OpenMath 2026 hill slot. GCL has not admitted an exact hill identity, title, statement, version, or evaluator for this slot.

That absence is a constraint, not an invitation to infer the missing content.

The canonical organizer list is:

`https://app.autolab.ai/lists/alejandrozu/openmath`

The documented CLI query is:

`autolab lists show alejandrozu/openmath`

An authorized runner may provide `AUTOLAB_TOKEN`. Never print, log, quote, or persist the token.

## Objective

Acquire organizer-authoritative evidence sufficient for MATHFORGE to source-lock exactly one hill to `OM26-H2`, or return a precise external acquisition blocker.

A successful acquisition should establish, from authoritative evidence:
- exact organizer hill ID;
- exact title;
- exact statement body or authenticated render/export;
- external version identifier, if exposed, otherwise an observation timestamp;
- evaluator/checker identity and operative semantics when available;
- authoritative source references;
- remaining semantic or provenance hazards.

## Required method

1. Perform non-mutating reconnaissance first.
2. Obtain the organizer-authoritative OpenMath list and relevant hill record.
3. Do not map `OM26-H2` by list position, memory, event prose, search snippets, title similarity, or another agent's inference.
4. Establish the exact external identity before treating any hill body as belonging to this slot.
5. Capture authoritative bytes or an authenticated render/export where available.
6. Preserve unknown fields as unknown.
7. Prepare evidence suitable for the MATHFORGE source-lock packet.
8. Do not start hill-specific proof, construction search, optimization, or theorem attack.

## Completion dispositions

Return one of:

- `ACQUIRED_AUTHORITATIVE_SOURCE_RECORD`: the exact hill identity and statement evidence are sufficient for Forge source-lock construction.
- `PRECISE_EXTERNAL_ACQUISITION_BLOCKER`: name the exact inaccessible source, authentication boundary, or evidentiary ambiguity and what was attempted.

A plausible guess is not a third disposition.

## Prohibited actions

- Do not work on OM26-H1.
- Do not infer an unresolved title or statement.
- Do not assume the organizer list order defines GCL slot order.
- Do not reuse another hill's evaluator semantics by analogy.
- Do not claim theorem truth, novelty, optimality, competition acceptance, or MATHCERT certification.
- Do not submit a competition entry.
- Do not mutate the assignment registry.

## Return

Use only the exact GitHub return surface and exact result grammar named by the protected lease/dispatch record. If those are absent, stop with `NO_ACTIVE_LEASE: OM26-H2-SOURCE-ACQ`.

The returned object is evidence for later GCL adjudication. Receipt does not change canonical mathematical claim state.

## Successor gate

No hill-specific mathematical CEX package for `OM26-H2` may be released until a protected MATHFORGE source lock for this exact slot exists and MATHSOLVE has rebound the lane.

## Claim boundary

This assignment can establish source identity and a precise acquisition blocker. It cannot establish mathematical correctness, novelty, certification, or competition acceptance.
