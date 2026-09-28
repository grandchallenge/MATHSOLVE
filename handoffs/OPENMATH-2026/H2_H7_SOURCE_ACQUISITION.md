# OPENMATH-2026 H2-H7 source acquisition — CEX cold start

**CEX subcampaign:** `OPENMATH-2026-SOURCE-ACQ`  
**Operation:** `OM26-H2-H7-SOURCE-ACQ`  
**Parent campaign:** `OPENMATH-2026`  
**Programme tracker:** `grandchallenge/MATH-PROGRAMME#1072`  
**Forge tracker:** `grandchallenge/MATHFORGE#282`  
**Solve tracker:** `grandchallenge/MATHSOLVE#454`

## Core clarity

The mathematics of OM26-H2 through OM26-H7 is not yet admitted.

The task is to acquire the exact organizer-authoritative hill records and protect them in MATHFORGE. Six lanes may run concurrently because they have disjoint source identities, but no lane may infer content from another lane, list ordering, event prose, search snippets, or conversational history.

OM26-H1 Kobon triangles is outside this operation and remains unchanged.

## Authoritative unresolved source pool

An authenticated AutoLab list receipt now establishes the six exact unresolved organizer hill IDs:

- `alejandrozu/clique-cluster-ramsey-multiplicity`
- `alejandrozu/matrix-multiplication-tensor-3x3`
- `alejandrozu/grothendieck-constant-witnesses`
- `alejandrozu/collatz-modular-descent`
- `alejandrozu/busy-beaver-6-certificates`
- `ottogin/erdos-3`

Receipt: `work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json`.

These are authoritative pool identities, not H2-H7 slot assignments. Source acquisition is dispatched by exact organizer hill ID. Slot binding happens only after a protected source lock.

## CEX pickup front door

The canonical machine pickup surface is `.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json`. The human discovery surface is `handoffs/OPENMATH-2026/CEX_JOB_BOARD.md`.

External workers do not choose or self-claim jobs. A worker is launched with one `dispatch_id`, resolves the unique protected lease naming that dispatch, verifies `state = LEASED` and its `agent_ref`, then loads exactly the referenced work package.

If no matching protected lease exists, return `NO_ACTIVE_LEASE` and stop.

## Exact preparation bind

- MATHSOLVE: `78dfb7479ca521f468d068beeea34c07dc1d0cd0`
- MATHFORGE: `eb5af08b1bb0ae7742dc46786019fe7b034b04ee`
- MATH-PROGRAMME: `6fae2b2df9bc0bb180a63c76fc9752656285da02`
- MATHCERT: `8a2610215989bec15474f0a088945c0a1b6d8172`
- INTELLECT: `cacfe1f749b91a335e1d1734352cecff56bad7c1`
- GCL-CEX-01: `grandchallenge/gcl-standards@efe06a27aa594c63bd0489929ffd9fff1e2daeb9`

A later executor must re-fetch live protected heads before mutation. Drift is classified, not ignored.

## Zero-context bootstrap

You are executing one protected CEX assignment in governed operation `OM26-H2-H7-SOURCE-ACQ`.

1. Read `.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json`.
2. Resolve only the assignment bound to the `dispatch_id` supplied in your launch message.
3. Verify that assignment is `LEASED` to the same dispatch and your `agent_ref`.
4. Load exactly the referenced `work_package`. Treat it as the complete GCL problem world.
5. Execute that bounded package.
6. Return exactly one result through the surface and grammar named by the protected dispatch.
7. Stop.

Do not browse for a different job, self-claim an available assignment, map organizer-list position to H2-H7, or work on H1.

## Return contract

Return one durable result for the selected slot through the existing GitHub intake surfaces.

A successful return identifies:
- slot;
- exact organizer hill ID;
- exact title;
- exact statement capture;
- external version or observation timestamp;
- authoritative source references;
- evaluator/checker identity when available;
- MATHFORGE paths and exact protected commit;
- remaining semantic hazards.

A blocked return names the exact inaccessible source, authentication boundary, or evidentiary boundary and records what was tried. It does not guess missing content.

## H7 boundary

OM26-H7 is known only at Human-Steward level as an additional Erdős problem. That phrase is not the competition statement and is insufficient to map a specific Erdős problem to H7.

## Claim boundary

Source acquisition can release a lane for research. It cannot establish a theorem, novelty, competition acceptance, or MATHCERT certification.
