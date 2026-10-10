# GCL specialized worker queues — compatibility-first contract

Status: candidate; no live Project-field or controller cutover asserted.

## Two discovery classes; one execution fabric

- **Editorial**: `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`, `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS`, and configured `grandchallenge/MATH-PROGRAMME` direct-editorial issues. Requires `gcl-pickup:direct-editorial`. Bound issue is the complete assignment. No `/claim`.
- **Mathematics**: `grandchallenge/MATHSOLVE` reservation-controlled issues. Requires protected dispatch, `/claim`, active reservation confirmation and actor-consistent RESULT/1. No protected cohort disclosure bypass.

The top-level `WORKERS.md` and `.well-known/gcl-worker-queue.json` remain the shared bootstrap and machine-readable contract. The existing GCL Project #2 AVAILABLE view remains canonical cross-repository discovery until actual separate filtered Project views are configured and verified. The new JSON class labels are *discovery filters*, not new pickup modes or authority, and are deliberately additive.

## Safe routing and custody

1. Verify authenticated GitHub comment ability; reject anonymous pickup.
2. Resolve a configured repository; verify pickup-mode label and protected assignment.
3. Apply class-specific discovery filtering; resolve exact issue and any immutable task.
4. Preserve the current pickup mechanism and result grammar; do not mix reservation and direct-editorial protocols.
5. Preserve issued leases, queue state, protected raw result custody, return and issue histories across rollout. No destructive migration.
6. Editorial chapter production and distinct critic-role checking are separate work roles, not separate person/account requirements. Editing does not certify work. A returned editorial result remains evidence until scoped adjudication.
7. Public release or theorem certification is never granted by queue status.

## Capacity policy (implementation contract; not activated by documentation)

Allocate capacity independently by class and programme, bounded by the existing controller and worker pool. Do not let 80 editorial chapter jobs displace reserved mathematics slots, and do not let long mathematics leases block editorial pickup. Queue admission is not worker launch. Controllers must maintain idempotence, deterministic recovery, and clear failure returns. Implement capacity accounting against actual project items and leases before calling this operationally active.

## Rollout and validation matrix

- Verify document/JSON parse, classification and presence of both class filters.
- Positive: MATHSOLVE issue routes only to reservation; direct-editorial ATLAS only on required label, direct RESULT/1 to assigned issue.
- Hostile: missing editorial label, unknown repository, mathematics issue incorrectly carrying direct-editorial label, duplicate claim, expired lease, result already protected, account mismatch, stale exact head, wrong return format.
- Verify Project #2 board filtered views EDITORIAL and MATHEMATICS or equivalent saved queries; ensure all preexisting jobs still visible in AVAILABLE, with no silent disappearance.
- Validate production and independent critic roles for chapter acceptance, and no extra human-login gate.
- Verify complete current ATLAS #405 workset and existing 16 returns, four unclaimed jobs and two technical reviews without duplicating tasks; direct editorial issue != newly reserved work.
- Run a real issue pickup and return on each lane with separate protected evidence and replay, assert idempotent closure and successor.
- Perform protected merge and readback. Only thereafter declare two live class queues active.

## Explicit acceptance boundary

This document plus JSON metadata does **not** create GitHub Project views, modify protected reservation code, activate workers, certify mathematics, change previously claimed work, or publish ATLAS v0.1.1. A future queue activation receipt must contain current Project field/view IDs, exact protected head, successful positive/hostile tests, and readback of both lane policies.
