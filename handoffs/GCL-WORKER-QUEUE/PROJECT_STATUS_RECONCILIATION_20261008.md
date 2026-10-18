# GCL Worker Queue — Project #2 lifecycle projection and recovery

**Policy owner:** MATH-PROGRAMME / GCL-WORKER-QUEUE-001. **Implementation:** MATHSOLVE.  
**Project:** https://github.com/orgs/grandchallenge/projects/2  
**Recovery tranche:** GCL-PROJECT-2-RECONCILE-20261008.  
**Scope:** Presentation and integrity of the public worker-pickup queue only. This is not protected dispatch admission, mathematical adjudication, certification, release permission, agent staffing approval, or closure of the editorial programme.

## Authority and semantic separation

The organization's **Issue Field** `GCL State` controls worker discovery: `AVAILABLE`, `RESERVED`, `RETURNED`, `BLOCKED`, `CLOSED`. Its corresponding issue label is checked, not inferred as authority. Protected Solve dispatch/lease remains execution authority for MATHSOLVE; Atlas uses its distinct direct-editorial return projector and role-separated review doctrine. Project `Status` is **only** a worker-assignment board column, with the following mapping:

| `GCL State` Issue Field | Project `Status` | Meaning |
| --- | --- | --- |
| `AVAILABLE` | `Todo` | Worker may discover it subject to the dispatch-specific rules |
| `RESERVED` | `In Progress` | Pickup is reserved; it does not create an execution lease |
| `BLOCKED` | `In Progress` | Operational attention/return adjudication needed; NOT available for pickup |
| `RETURNED` | `Done` | Worker assignment has been handed back; mathematics/editorial acceptance **not** asserted |
| `CLOSED` | `Done` | Operational assignment is closed; protected issue/result authority remains separate |

The `AVAILABLE` Project view already filters `is:open "GCL State":AVAILABLE`; `RETURNED` already filters `"GCL State":RETURNED`. Do not create duplicate views. Historical issue bodies may retain the frozen phrase `AVAILABLE_UNCLAIMED`; *do not* use that phrase instead of live fields to determine eligibility. Return comments must remain visible for retrospective audit.

Project `Done` does **not** mean a proof was accepted, an Atlas chapter signed off, a mathematical result certified, or returned work adjudicated. Returned items remain in the existing `RETURNED` view. Adjudication and successor planning belong to their protected campaigns and may create new bounded assignments if evidence warrants them.

## Observed defects and bounded repairs (2026-10-08)

Full inventory originally 61 issues spanning MATHSOLVE, Adaptive Intelligence Atlas and Computational Difficulty Atlas. All 61 Project items had generic `Status=Todo`, while project/issue labels showed the majority had returned. Source-state inspection discovered:

- Atlas #335 / `ATLAS-EDITORIAL-P08`: a valid issue-bound `RESULT/1` (comment `6059431186`) and returned label, but the organization Issue Field remained `AVAILABLE`. Field reclassified `RETURNED`, read back.
- Atlas #336 / `ATLAS-EDITORIAL-P09`: valid issue-bound `RESULT/1` (comment `6059816123`) and returned label, but the organization Issue Field remained `AVAILABLE`. Field reclassified `RETURNED`, read back.
- Computational Difficulty Atlas #2: bounded agent job visibly available with no organization Issue Fields. Initialized `GCL State=AVAILABLE`, campaign `COMPUTATIONAL-DIFFICULTY-ATLAS`, `GCL Role=VERIFY`, `GCL Collaboration=COOPERATIVE`, `GCL Phase=SHARED`, read back.
- MATHSOLVE #1003: its `GCL State=BLOCKED` Issue Field was already authoritative despite no `gcl-state` label, and reflects a protected worker reservation/returned-comment intake boundary. **Do not** assign `AVAILABLE` or `RETURNED` from a label guess.

After source repair: **48 RETURNED / 12 AVAILABLE / 1 BLOCKED**, 0 missing fields, 0 label/field mismatches. `AVAILABLE` should contain only the 12 currently discoverable issues across the three programmes.

A one-time board `Status` synchronization successfully applied the first **40 of 49** required projection changes but then encountered GitHub's GraphQL rate-limit/secondary-throttle response. This partial result is **not** a complete readback; do not claim the board clean until the remaining changes replay and the end-to-end status check passes. No issue fields, result evidence, protected dispatch, release or certification were changed by the incomplete board-only batch.

## Reproduction and recovery

Use an authenticated operator environment with read/write access to the organization Project:

```sh
python ci/gcl_worker_queue_project_status.py --report /tmp/gcl-project2-preflight.json
python -m unittest discover -s tests -p test_gcl_worker_queue_project_status.py -v
python ci/gcl_worker_queue_project_status.py --apply --report /tmp/gcl-project2-reconciled.json
```

Dry-run is default. `--apply` loads **the current actual population** (not a stale 61-item list), validates one authoritative `GCL State` Issue Field and corresponding label per item, then changes only the Project `Status` when different. Every changed item checks its live Issue Field again immediately before writing. Final readback refuses to claim success if any item is inconsistent. Unknown states, new repos, absent/duplicate fields, unexpected URLs or inconsistent labels stop the operation without inferring or authorizing a state transition. Subsequent replays are idempotent.

The operator's GitHub CLI token has organization Projects permissions. The default repository `GITHUB_TOKEN` does **not** establish organization Projects-write capability. On 2026-10-08 neither MATHSOLVE nor Atlas exposes a dedicated Project-write secret. Do not create a purported unattended Actions mutator requiring an unconfigured token or bypass protection. If a governed Project-write credential becomes available, this reconciler can be scheduled or invoked by the existing queue controller subject to exact-rights and separate admission checks; until then it is a supported idempotent authenticated operation.

## Atlas editorial intake triage

At this checkpoint, Atlas's Project entries include six available: [#321](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/321), [#322](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/322), and the four genuinely unclaimed chapter reviews [#338](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/338), [#339](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/339), [#343](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/343), [#344](https://github.com/grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS/issues/344). #321 and #322 now have a current controlling issue-body header superseding stale PR #320 hashes, historical numbering status and separate-login doctrine; retain the old issue bodies as provenance. **Do not populate 20 duplicate review jobs.** Returned source/math review assignments from the previous tranche have an outstanding adjudication/synthesis obligation, not another copy-paste worker-claim obligation. Atlas PRs #370 and #371 are source corrections to assess on current exact head; they are not necessarily queue pickup items. Full 80-chapter editorial signoff remains a separately governed process.

## Separate pending work

The existing `RETURNED` view should be the intake/adjudication lane for 48 returned assignments. Their `Done` worker-board status must not destroy issues, hide source evidence, or imply final claim authority. Evaluate partial vs completed returns and promote work only through actual campaign review. If a returned job has open corrections, retain its original return as evidence and open a *new bounded successor* only if no already active task covers the gap.

Future work should test automated drift detection and secure Projects-write provisioning before it is represented as fully unattended. The reconciler and its offline tests are intentionally a bounded operational change and must go through normal protected MATHSOLVE admission.
