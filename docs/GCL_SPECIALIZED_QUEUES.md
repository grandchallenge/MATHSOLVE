# GCL specialized worker queues — compatibility-first contract

Status (2026-10-11): **semantic Project #2 classification and both saved views VERIFIED** in protected Council Clerk run [#38124664460](https://github.com/grandchallenge/MATH-PROGRAMME/actions/runs/38124664460), SHA `aa61829b88848ab50b009b9a5b2a097e81b8a819`. Project #2 fully re-read **1,308** jobs (**37 Editorial**, **1,271 Mathematics**), with existing AVAILABLE view preserved. Active worker-capacity enforcement, genuine two-lane pickup/RESULT/1 replay, and ATLAS workload reconciliation remain separate gates; issue #1049 stays OPEN.

## Queue class and pickup mode are independent axes

**Queue Class** identifies the substance of a job. **Pickup mode** identifies the mechanism through which a worker acquires and returns that job. Classifying `direct_editorial` as invariably Editorial was an error: `ERDOS-CATALOGUE-NNNN-S01` source-audit tasks in MATH-PROGRAMME are Mathematics, despite using the direct issue-comment protocol. The protected semantic-class checker is `ci/gcl_queue_class_contract.py`; a complete authenticated Project #2 pagination/readback is required to certify or correct actual item fields.

## Two discovery classes; one execution fabric

- **Editorial**: `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS`, `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS`, and configured `grandchallenge/MATH-PROGRAMME` substantive manuscript, documentation and critic tasks (excluding `gcl-role:source-audit`). Requires `gcl-pickup:direct-editorial`. Bound issue is the complete assignment. No `/claim`.
- **Mathematics**: `grandchallenge/MATHSOLVE` proof and research dispatches require protected `/claim` reservation and owner-bound RESULT/1. The additional MATH-PROGRAMME Erdős source audits and critical source/lemma reviews are also Mathematics, but **retain direct issue-bound RESULT/1 with no `/claim`**, because Queue Class and pickup mode are independent. No protected cohort disclosure bypass.

The top-level `WORKERS.md` and `.well-known/gcl-worker-queue.json` remain the shared bootstrap and machine-readable contract. The existing GCL Project #2 AVAILABLE view remains canonical cross-repository discovery until actual separate filtered Project views are configured and verified. The new JSON class labels are *discovery filters*, not new pickup modes or authority, and are deliberately additive.

## Erdős catalogue discovery overlay (no new pickup mode)

The full Erdős catalogue is a **mathematical research-preparation** workstream, although its issues are operationally housed in `grandchallenge/MATH-PROGRAMME` under the existing `direct_editorial` pickup mode. Workers looking for Erdős work must not conclude the queue is empty merely because MATHSOLVE's reserved-dispatch query returns no AVAILABLE issues.

- [Discover AVAILABLE Erdős catalogue assignments](https://github.com/grandchallenge/MATH-PROGRAMME/issues?q=is%3Aissue+is%3Aopen+label%3Agcl-job+label%3Agcl-state%3Aavailable+label%3Agcl-pickup%3Adirect-editorial+ERDOS-CATALOGUE). Filter by the actual `gcl-state:available` and `gcl-pickup:direct-editorial` labels and by the `ERDOS-CATALOGUE` issue title prefix; inspect the issue's exact `GCL State` Issue Field before execution.
- A catalogue issue is a scoped source/status audit, provenance check or bounded research-task design, not an unrestricted licence to attempt a parent conjecture. It returns `RESULT/1` to the bound Programme issue without `/claim`.
- Research-proof dispatches remain in MATHSOLVE with the protected `/claim` reservation controller and `GCL-CONTRIBUTION-RESULT/1` return. Do not relabel catalogue issues as MATHSOLVE work or alter leases, custody, or certification authority.
- This is a discovery overlay over the two existing classes; no Project saved view, new route, or controller activation is claimed by this document.

## Safe routing and custody

1. Verify authenticated GitHub comment ability; reject anonymous pickup.
2. Resolve a configured repository; verify pickup-mode label and protected assignment.
3. Apply class-specific discovery filtering; resolve exact issue and any immutable task.
4. Preserve the current pickup mechanism and result grammar; do not mix reservation and direct-editorial protocols.
5. Preserve issued leases, queue state, protected raw result custody, return and issue histories across rollout. No destructive migration.
6. Editorial chapter production and distinct critic-role checking are separate work roles, not separate person/account requirements. Editing does not certify work. A returned editorial result remains evidence until scoped adjudication.
7. Public release or theorem certification is never granted by queue status.

## Verified operational classification receipt

The authenticated [Council Clerk #2563 receipt](https://github.com/grandchallenge/MATH-PROGRAMME/issues/2563) records exact Project V2 metadata:

- Queue Class field: `PVTSSF_lADOB9Ao_c4BlwurzhlJkjI`.
- EDITORIAL saved view: `PVTV_lADOB9Ao_c4BlwurzgMAfZU`.
- MATHEMATICS saved view: `PVTV_lADOB9Ao_c4BlwurzgMAfZY`.
- The original global AVAILABLE view remains `PVTV_lADOB9Ao_c4BlwurzgL64bo`.

**The 1,308 rows are queued issues, not active workers.** The controller's successful complete readback is evidence of semantic class and view integrity only. It is neither a licence to increase concurrent work nor a theorem or editorial certification.

## Capacity policy (implementation contract; not activated by documentation)

Allocate capacity independently by *semantic* class and programme, bounded by the existing controller and worker pool. `check_admission` in `ci/gcl_queue_class_contract.py` fails closed when either class's admission budget or its complete AVAILABLE count is missing; a full Project snapshot is required. The pilot protected CONFIG.json now proposes **8 active Mathematics reservations** and an independent **8-slot Editorial planning budget**, subject to protected admission. The Mathematics guard counts all **trusted, unexpired reservation histories** and serializes claim/release/reaper operations before admitting another Solve /claim; it never uses the 1,271 Mathematics queue items as occupied slots. Editorial has **no enforceable active-worker count** until actual authenticated direct-issue start/return evidence is tracked; its budget must not be represented as live capacity enforcement. This check is a pure decision guard, **not connected to a Project writer**. Do not let 80 editorial chapter jobs displace reserved mathematics slots, and do not let long mathematics leases block editorial pickup. Queue admission is not worker launch. Controllers must maintain idempotence, deterministic recovery, and clear failure returns. Implement actual *available-item admission* enforcement at the Project-write boundary. Direct-editorial workers do not have MATHSOLVE reservation leases; therefore runtime concurrency cannot be derived from `AVAILABLE` counts. Track real direct-editorial start/return ownership before asserting active worker concurrency limits. Existing Solve leases are never reclassified or preempted.

## Rollout and validation matrix

- Verify document/JSON parse, classification and presence of both class filters.
- Positive: MATHSOLVE issue routes only to reservation; direct-editorial ATLAS only on required label, direct RESULT/1 to assigned issue.
- Hostile: missing editorial label, unknown repository, mathematics issue incorrectly carrying direct-editorial label, duplicate claim, expired lease, result already protected, account mismatch, stale exact head, wrong return format.
- Inspect exact Project #2 Queue Class field `PVTSSF_lADOB9Ao_c4BlwurzhlJkjI`: prior operator readback reported 1,294 entries, 1,258 Editorial and 36 Mathematics; this was by pickup mode and is **not** a successful semantic-class audit. Read all pages; correct Erdős catalogue source-audit entries to Mathematics without changing their direct pickup mode. Verify Project #2 board filtered views EDITORIAL and MATHEMATICS or equivalent saved queries, and zero missing/duplicate jobs in the global AVAILABLE view.
- Validate production and independent critic roles for chapter acceptance, and no extra human-login gate.
- Verify complete current ATLAS #405 workset and existing 16 returns, four unclaimed jobs and two technical reviews without duplicating tasks; direct editorial issue != newly reserved work.
- Run a real issue pickup and return on each lane with separate protected evidence and replay, assert idempotent closure and successor.
- Perform protected merge and readback. Only thereafter declare two live class queues active.

## Activation evidence still required

The protected semantic-class guard and tests provide deterministic local evidence only. To close [GCL-QUEUE-CLASS-CUTOVER #1049](https://github.com/grandchallenge/MATHSOLVE/issues/1049), an authenticated, Projects-write-capable operator/controller must: (1) collect all Project items and option IDs under pagination; (2) correct semantic classifications, including the Erdős source-audit tranche; (3) create/read back both Project saved views without losing global AVAILABLE; (4) set *governed* class-specific admission budgets and bind the pure guard into the **actual** Project admission controller; (5) inspect live availability and active work separately, execute genuine positive and hostile pickups and RESULT/1 returns, preserve leases; (6) commit exact SHA, Project IDs, counts, test receipts and rollback in the cutover issue. Missing any part leaves this cutover incomplete, not silently activated.

## Explicit acceptance boundary

This document plus JSON metadata does **not** create GitHub Project views, modify protected reservation code, activate workers, certify mathematics, change previously claimed work, or publish ATLAS v0.1.1. A future queue activation receipt must contain current Project field/view IDs, exact protected head, successful positive/hostile tests, and readback of both lane policies.
