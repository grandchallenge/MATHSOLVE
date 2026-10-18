# GCL Solve specialist: execution integrity evidence contract

Status: **SOURCE-DOMAIN DESIGN — NO POSITIVE RECEIPT ISSUED**  
Owner: MATHSOLVE; Programme consumer: [MATH-PROGRAMME #1520](https://github.com/grandchallenge/MATH-PROGRAMME/pull/1520)  
Producer work package: [MATHSOLVE #1040](https://github.com/grandchallenge/MATHSOLVE/issues/1040)  
Programme gate: [MATH-PROGRAMME #1251](https://github.com/grandchallenge/MATH-PROGRAMME/issues/1251)

## Responsibility and authority

The `SOLUTION_INTEGRITY` specialist asks whether a particular bounded
worker return was faithfully captured, replayed, and adjudicated, with every
identity and artifact attached to the right dispatch. It does **not** answer
whether the submitted mathematical statement has been independently proved.

GCL authority remains **Forge → Solve → Cert**: MATHFORGE owns source-premise
verification; MATHSOLVE owns provisional-result evaluation and execution
integrity; MATHCERT owns mathematical proof certification; INTELLECT owns
security and constitutional authority. Neither successful replay nor a
specialist GitHub approval promotes a theorem. Routine operational changes
continue under `MP-STREAMLINED-EXECUTION-001` without a generic non-author
human approval ceremony.

## Protected evidence bundle: exact material and provenance

An actual Solve review can lead to a protected Programme specialist receipt
only when all objects already exist on protected MATHSOLVE `main`.
A candidate's labels, issue comment, self-authored assertion, or branch-local
file are not evidence.

1. **Capture** — `GCL_SOLVE_CAPTURE_RECEIPT_V1` JSON: `dispatch_id`,
   `result_ref`, `result_sha256`, plus traceable authenticated return/intake
   provenance. Its JSON Git blob SHA is locked in the binding.
2. **Replay** — `GCL_SOLVE_REPLAY_RECEIPT_V1` JSON: identical `dispatch_id`
   and `result_ref`; `input_result_sha256` exactly equal to capture's
   `result_sha256`; `capture_blob_sha` exactly equal to the protected
   capture blob; and `replay_pass: true`. The actual replay harness and
   deterministic output must be independently inspectable.
3. **Adjudication** — `GCL_SOLVE_ADJUDICATION_RECEIPT_V1` JSON: the same
   dispatch/result identities, locked `replay_blob_sha`,
   `adjudication_id`, `adjudication_disposition:
   REPLAYED_AND_ADJUDICATED`, with no substantive-claim promotion.

All three are distinct JSON files under `contributions/<campaign>/<dispatch>/`
and must have exact Git blob SHAs resolvable from protected MATHSOLVE.
Their inclusion is *not* sufficient to assert mathematical correctness.

The binding named `solve_execution` is duplicated **exactly** in both the
domain-owned review artifact and final domain receipt. Its keys are
`schema_version: 1.0.0`, `dispatch_id`, `result_ref`,
`result_sha256` (lowercase 64-digit hex SHA-256), and three objects
`capture`, `replay`, `adjudication` each containing precisely `path`
and `blob_sha` (40-digit Git SHA-1). The last key is `claim_effects`:
all five effects below must be explicitly false.

- `mathematical_claim_effect: false`
- `certification_effect: false`
- `publication_effect: false`
- `source_semantic_effect: false`
- `security_authority_effect: false`

The adjudication artifact must independently repeat that same
`claim_effects` object. Any mismatch, omitted lock, replay failure,
or other disposition fails closed.

## Domain-owned specialist review and exact Programme target

A review artifact under protected `contributions/` has type
`GCL_DOMAIN_ROLE_SCOPED_REVIEW_V1`. It must bind:
`authority_domain: SOLUTION_INTEGRITY`,
`subject_repository: grandchallenge/MATH-PROGRAMME`, the current exact
Programme PR head `subject_sha`, the normalized complete changed-file
`material_fingerprint` (SHA-256), `review_scope:
SOLVE_EXECUTION_INTEGRITY_ONLY`, `disposition:
ROLE_SCOPED_REVIEW_ACCEPTED`, the identical `solve_execution` binding,
`reviewer_identity`, and
`review_independence: ROLE_SCOPED_NON_AUTHOR_SPECIALIST`.

It also contains `review_anchor`: `source_pr_number`,
`source_pr_head_sha`, `review_id`, and `reviewer_login`. The
consumer verifies GitHub reports that the source PR was merged into
MATHSOLVE `main`, included this exact reviewed review-artifact Git blob,
and had a **real non-author `APPROVED`** from the declared reviewer on
the reviewed head, not superseded by later changes/dismissal. A logical
agent critical pass alone is insufficient as authenticated GitHub
review provenance, and this review is not a MATHCERT proof certificate.

The outer domain receipt under
`governance/material_admission_receipts/MATH-PROGRAMME-<head>.json`
contains `schema_version: 1.0.0`,
`record_type: GCL_PROTECTED_SPECIALIST_ADMISSION_EVIDENCE`,
`authority_domain: SOLUTION_INTEGRITY`,
`source_repository: grandchallenge/MATHSOLVE`, `subject` with exact
Programme `repository`, `head_sha` and `material_fingerprint`,
`verdict: ADMISSIBLE_FOR_PROTECTED_ADMISSION`,
`review_scope: SOLVE_EXECUTION_INTEGRITY_ONLY`,
a `protected_evidence` pointer (`path`, `blob_sha`) to the
independently approved source review file, and the identical
`solve_execution` evidence.

**One implementation constraint:** the domain artifact and receipt are
separate protected objects; do not attempt to declare the receipt certified
by an unmerged candidate PR. The source review blob and receipt must
be independently read back from the protected commit when emitted.

## Minimum acceptance replay

The consumer must replay a *real* positive source-domain receipt, verify
candidate exact-head SHA, full file-manifest fingerprint, protected source
Git blobs, non-author GitHub review, and all three execution artifacts.
It must reject forged data, mismatched result digest, wrong dispatch,
unreplayed outcomes, stale source branch, later-dismissed reviewer status,
and every claim-authority bit set true.

For `pull_request_target` the evidence is bound to exact PR source head.
For `merge_group`, the effective queue candidate and protected base must
be checked independently: a positive PR-level receipt **does not imply**
a positive result on a newly synthesized merge-group SHA. Implement and
test deterministic material identity across the queue before enforcing
any mandatory check. If no valid mapping or source certificate exists,
remain `SPECIALIST_REVIEW_PENDING`.

This repository **does not certify a mathematical theorem** through this
mechanism. Promotion remains gated in MATHCERT. No existing GitHub
protection is weakened; no mandatory Programme `material-admission`
context is authorized until both positive and hostile live gates pass.

## First bounded producer task

Use [#1040](https://github.com/grandchallenge/MATHSOLVE/issues/1040) to
choose a current real result that already has authenticated captured
return, reproducible replay, and an adjudication with zero certification
effect. If any link is missing, implement and protect that producer
mechanism first. Only then generate its exact protected evidence,
obtain the scoped non-author source review, and publish the outer
receipt for an actual Programme target head.

Never fill a protected receipt template with invented replay or theorem
success merely to make a test green.
