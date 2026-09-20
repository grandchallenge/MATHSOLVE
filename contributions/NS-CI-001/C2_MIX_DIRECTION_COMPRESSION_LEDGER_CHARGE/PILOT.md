# NS-CI Independent Contributor Intake Pilot

Status: PILOT_ACTIVE__DISPATCH_ISSUED

## Authority

This is the bounded pilot authorized by Human Steward `fyremael` for
`GI-COUNCIL-INDEPENDENT-CONTRIBUTOR-INTAKE-001`.

Controlling protected records:

- Council protected merge: `grandchallenge/INTELLECT@242d3b6a4130c24214a56978d7237dc85883c946`
- Council disposition:
  `governance/council_matters/GI-COUNCIL-INDEPENDENT-CONTRIBUTOR-INTAKE-001/disposition.json`
- Human Steward authorization protected merge:
  `grandchallenge/INTELLECT@cacfe1f749b91a335e1d1734352cecff56bad7c1`
- Human Steward record:
  `governance/council_matters/GI-COUNCIL-INDEPENDENT-CONTRIBUTOR-INTAKE-001/human_steward_disposition.json`

The authorization is pilot-only. It does not establish organization-wide policy,
persistent coordination, mathematical certification, or contributor protected-state authority.

## Purpose

Test a clean boundary between:

1. sealed independent dispatch;
2. immutable raw contribution intake;
3. mechanically checkable intake receipt;
4. later GCL adjudication;
5. optional protected incorporation through existing MATHSOLVE/MATHCERT routes.

The independent contributor is a contributing entity, not a temporary GCL role-holder.
The contributor's argument is evidence. Intake does not convert it into accepted mathematics.

## Source mathematical handoff

The pilot source is:

`handoffs/NS-CI-001/C2_MIX_DIRECTION_COMPRESSION_LEDGER_CHARGE_ZERO_CONTEXT.md`

Dispatch records will bind the exact protected commit and blob identity after this pilot
setup is protected. The handoff itself contains all mathematical hydration.

## Pilot concurrency modes

- `independent_blind`: same sealed assignment may be sent to multiple contributors;
  no contribution from the cohort may be disclosed to another cohort member before closure.
- `cooperative_claimed`: bounded work is claimed to avoid accidental duplication.
- `adversarial_replay`: an existing result is intentionally challenged or reproduced;
  the disclosed evidence surface must be explicit.

## Blind cohort lifecycle

A blind cohort has the state machine:

`OPEN -> CLOSED_FOR_BLINDNESS -> SYNTHESIS_ALLOWED`

No cross-contribution synthesis is allowed before durable closure.
Late returns remain preserved evidence with `late_for_cohort` status and do not silently
alter a completed blind comparison.

## Durable return rule

Durability is mandatory. Repository access is not.

An external contributor returns one complete Independent Contribution Record (ICR).
If the contributor has no authorized repository write path, the full ICR is returned
verbatim through the available transport. The receiving GCL intake process persists the
original bytes before normalization, summary, adjudication, or synthesis.

If a proposal-only inbox write is separately authorized, the contributor may write only
to the designated raw inbox path named by its dispatch. It may not edit canonical
handoffs, work packages, campaign ledgers, protected branches, receipts, or adjudication.

## Raw evidence rule

Raw contribution bytes and attachments are immutable after intake.

- corrections create new linked contribution records;
- no return overwrites another return;
- transport replay of identical bytes is idempotent;
- derived summaries and normalized metadata cite the raw digest;
- executable content is data and is not automatically executed.

## Independence rule

The pilot records separately:

- declared context class;
- authenticated producer/provenance evidence, when available;
- later adjudicated independence strength.

Different sessions, model names, filenames, or self-declared identities do not by
themselves prove independence.

## Mechanical versus review-bound classification

Mechanical:

- byte identity;
- exact dispatch binding;
- schema validity;
- explicit supersession links;
- observable repository freshness.

Review-bound:

- semantic duplication;
- plagiarism/copying;
- mathematical conflict meaning;
- independence strength;
- mathematical correctness.

## Pilot acceptance evidence

The pilot must collect evidence for:

1. exact raw preservation before synthesis;
2. receipt binding to exact dispatch and raw digest;
3. zero overwrite;
4. zero contributor canonical mutation;
5. blind-cohort non-disclosure before closure;
6. stale-return preservation without silent live-state rebinding;
7. safe handling of executable/instruction-bearing payloads;
8. idempotent transport replay;
9. identifier collision handling;
10. truncated and late return handling;
11. separation of intake from adjudication;
12. executor feedback on overhead, ambiguity, usefulness, and concurrency defects.

Pilot evidence returns to full Council review before broader institutionalization.

## Current boundary

Exact dispatch records are now issued against protected MATHSOLVE merge
`490bb2da6b6d315193c86ae934a49241735d027c` and handoff blob
`e49bf0c5b88567ea50a91e655b631cdc4f83daeb`.

Open blind cohort: `NSCI-C2-A-BLIND-COHORT-001`.

Ready dispatches:

- `NSCI-C2-A-BLIND-001`: Assignment A, `independent_blind`;
- `NSCI-C2-A-BLIND-002`: Assignment A, `independent_blind`;
- `NSCI-C2-B-COOP-001`: Assignment B, `cooperative_claimed`.

No contribution has yet been received or adjudicated. Blind-cohort synthesis remains
forbidden until durable cohort closure.
