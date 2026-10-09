# GCL Worker Queue — systemic pickup and projection remediation

**Date:** 2026-10-08  
**Scope:** Project #2 worker discovery, pickup routing, Issue Field projection, and board-status reconciliation.  
**Boundary:** operational queue mechanics only. No mathematical, editorial-acceptance, certification, merge, publication, or release authority is created here.

## Why this remediation exists

The queue had accumulated several independent-looking failures that shared one cause: worker pickup semantics and Project metadata were not represented by one enforceable contract.

The visible symptom was that a direct-review job could be correctly listed as AVAILABLE while the canonical worker bootstrap still told every worker to post `/claim` and wait for the MATHSOLVE reservation controller. Additional audit then found missing Project metadata on newer MATHSOLVE jobs, an obsolete `gh project item-edit` invocation, Windows text-decoding failure, and a first-error-only reconciler that concealed the full defect set.

This remediation converts those cases from conventions into checked invariants.

## Frozen repository pickup modes

The supported repository map is explicit and duplicated only through validated machine bindings:

| Repository | Pickup mode | Required worker action |
| --- | --- | --- |
| `grandchallenge/MATHSOLVE` | `reservation_controlled` | `/claim` → controller reservation → immutable task |
| `grandchallenge/ADAPTIVE-INTELLIGENCE-ATLAS` | `direct_editorial` | execute bound issue directly; no `/claim` |
| `grandchallenge/COMPUTATIONAL-DIFFICULTY-ATLAS` | `direct_editorial` | execute bound issue directly; no `/claim` |

Direct-editorial Project items must carry exactly `gcl-pickup:direct-editorial`. Reservation-controlled MATHSOLVE items must not carry a `gcl-pickup:*` label. A direct-editorial item may not enter `GCL State=RESERVED`.

Unknown repositories or unknown pickup labels are queue-integrity failures. The code must fail closed rather than infer a route.

## Single worker-facing decision

A zero-context worker now performs exactly one routing decision after opening an AVAILABLE issue:

1. determine repository/pickup mode;
2. reservation-controlled → use `/claim`;
3. direct-editorial → do not use `/claim`; follow the bounded issue and return its requested `RESULT/1`.

The public Project README, `WORKERS.md`, the full queue handoff, and machine bootstrap describe the same routing contract.

## Immutable metadata projection

For reservation-controlled MATHSOLVE jobs, the controller no longer projects only lifecycle state. Every controller transition also reprojects immutable job metadata from protected queue/dispatch sources:

- campaign;
- role;
- collaboration mode;
- phase;
- cohort;
- timebox when present.

The mapping to organization Issue Field vocabulary is centralized in `.gcl/worker_queue/CONFIG.json`.

The live status auditor independently recomputes expected MATHSOLVE metadata from the protected registry and dispatch and rejects mismatches.

## Project Status mutation

Project `Status` remains presentation only:

| GCL State | Project Status |
| --- | --- |
| AVAILABLE | Todo |
| RESERVED | In Progress |
| BLOCKED | In Progress |
| RETURNED | Done |
| CLOSED | Done |

The exact Project ID, Status field ID, and option IDs are versioned in `.gcl/worker_queue/PROJECT.json`. Reconciliation uses the current `gh project item-edit --id --project-id --field-id --single-select-option-id` interface. Human-readable field names are not used as mutation authority.

## Fail-closed live audit

`ci/gcl_worker_queue_project_status.py` validates the entire current Project population before any write. It checks:

- recognized repository and exact issue URL;
- required `gcl-job` label;
- authoritative GCL State and corresponding lifecycle label;
- campaign, role, collaboration, and phase fields;
- repository pickup-mode contract;
- direct-editorial label boundary;
- role-label ↔ role-field concordance;
- collaboration-label ↔ collaboration-field concordance;
- no RESERVED state for direct-editorial work;
- protected metadata concordance for MATHSOLVE jobs;
- Project Status vocabulary;
- complete Project listing and unique item IDs.

All integrity defects are accumulated and reported together. No mutation occurs if any defect exists.

Subprocess interaction with `gh` is forced to UTF-8 so the audit behaves consistently on Windows and Unix-like runners.

## CI contract

The normal Solve checks run:

- worker bootstrap validation;
- Project binding validation;
- queue policy validation;
- JSON syntax validation;
- queue projection unit tests;
- Project-status / pickup-routing unit tests.

The queue-specific offline suite covers both pickup modes, malformed labels, role/collaboration label-field disagreement, missing fields, direct-job reservation rejection, immutable metadata projection, mapping failure, lifecycle transitions, and result/release/reconcile paths.

## Live reconciliation performed

During this remediation, the full 61-item Project population exposed nine MATHSOLVE items whose lifecycle state existed but whose core Project metadata had not been populated:

- #985;
- #1003–#1010.

Their campaign/role/collaboration/phase/cohort fields were reconstructed from protected registry/dispatch state and written back. No mathematical or adjudicative state was inferred.

After repair and the added label-field concordance checks, the full live audit reported:

- 61 Project items;
- 33 reservation-controlled MATHSOLVE items;
- 28 direct-editorial Atlas items;
- 52 RETURNED;
- 7 RESERVED;
- 1 BLOCKED;
- 1 AVAILABLE;
- zero queue-integrity defects;
- zero Project Status updates remaining on final readback.

The remaining three board-only Status mismatches were then reconciled. Exact readback completed with:

`SUCCESS pickup contract + exact-item board projection + readback`

At that readback, the sole AVAILABLE item was the Computational Difficulty Atlas direct-review assignment.

## Recovery / operator commands

Read-only full audit:

```sh
python ci/gcl_worker_queue_project_status.py --report /tmp/gcl-project2-audit.json
```

Apply board Status reconciliation only after a clean full audit:

```sh
python ci/gcl_worker_queue_project_status.py --apply --report /tmp/gcl-project2-reconciled.json
```

Offline contract replay:

```sh
python ci/validate_gcl_worker_bootstrap.py
python ci/validate_gcl_worker_queue_project.py
python ci/validate_gcl_worker_queue.py
python -m unittest   tests.test_gcl_worker_queue_projection   tests.test_gcl_worker_queue_project_status -v
```

## Remaining infrastructure boundary

The operator environment has organization Project-write permission. Repository `GITHUB_TOKEN` credentials do not establish that cross-repository Project-write authority, and no dedicated governed Project-write secret is currently configured.

Therefore this remediation does **not** pretend that cross-repository Project Status reconciliation is unattended. What is now automatic is prevention/reprojection within the MATHSOLVE controller plus CI validation of the durable contract. The cross-repository live auditor is deterministic, idempotent, and fail-closed and can be scheduled only when an appropriately governed organization Project credential exists.

Until then, missing credentials are an infrastructure boundary, not a reason to weaken validation or infer state.

## Non-regression rule

A future queue change is incomplete unless it preserves all of these invariants. Adding another repository or pickup mode requires one bounded change to the repository-mode map, machine bootstrap, Project binding, worker documentation, validators, and tests. It must not be implemented as a one-off issue-body exception.
