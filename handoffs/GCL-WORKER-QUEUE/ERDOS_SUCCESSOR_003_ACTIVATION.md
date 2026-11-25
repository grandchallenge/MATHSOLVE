# ERDOS successor-003 — dispatch activation transaction

RECOVERY_RULE: Read protected MATHSOLVE main, then this plan. Never reconstruct activation state from conversation history.
SOURCE_AUTHORITY: contributions/ERDOS-OPEN-001/SUCCESSOR_002/adjudications/ERDOS-SUCCESSOR-002-ADJUDICATION-001.json
TRANSACTION: ERDOS-SUCCESSOR-003-DISPATCH-001

## Frozen task sources

- ERDOS-593-N3-IA-001: handoffs/GCL-WORKER-QUEUE/launch/2026-10-09/ERDOS-593-N3-IA-001.md
- ERDOS-593-N4-IA-001: handoffs/GCL-WORKER-QUEUE/launch/2026-10-09/ERDOS-593-N4-IA-001.md
- ERDOS-470-N3-IA-001: handoffs/GCL-WORKER-QUEUE/launch/2026-10-09/ERDOS-470-N3-IA-001.md

## Ordered, idempotent transaction

1. Admit the three immutable launch packets through protected PR, recording the **actual** protected main SHA as TASK_COMMIT. Do not use a candidate branch SHA as immutable source.
2. Create or reuse exactly one stable GitHub issue per dispatch; initially apply gcl-job and role/staged labels without gcl-state:available. Read back issue number, exact title, immutable body and authenticated issue metadata.
3. Write protected GCL_EXTERNAL_DISPATCH records under contributions/ERDOS-OPEN-001/SUCCESSOR_003/dispatches, with claim/return boundary and task_path/task_commit/task_url bound to step 1.
4. Append each new dispatch to .gcl/worker_queue/JOBS.json and add matching intake entries in .gcl/worker_queue/INTAKE_BINDINGS.json. Bind each issue body digest and pinned task SHA-256, with explicit dispositions/external-sources policy. Validate that legacy jobs and source authority remain unchanged.
5. Run queue, intake, Project, bootstrap and cross-platform validators on the material candidate closure. Exercise standing delegated execution authority and admit through the repository's actual protected checks and merge rules. **No generic independent non-author approval, Referee ceremony, or Human Steward disposition is required for this routine dispatch/queue registration.** Apply specialist review only if the change materially expands mathematical or certification authority, changes source semantics, weakens security/protection, or promotes an external claim. Never bypass an actual applicable protected gate.
6. After protected readback, project each issue into GCL Worker Queue Project #2 and the appropriate GCL Issue Fields. Only when exact protected registry+dispatch hashes and issue fields match, atomically advertise gcl-state:available.
7. Re-read the Project, issues, and active registry; demonstrate one consistent AVAILABLE state per unclaimed job. No worker reservation, RESULT/1, mathematical certification, or progress beyond queue publication may be fabricated.

## Dependency and stop conditions

If remote credentials or Project write permission are absent, retain the issues in STAGED state and write the exact blocker to durable control record. A pending or unapproved PR is not sufficient to mark a job AVAILABLE. Creation of a task packet alone is not external launch authorization. Old worker returns are never reclassified as successor-003 returns. The new worker jobs remain genuinely independent and require authenticated claims.

This transaction is completed only after protected registry admission and a successful live three-job queue/issue/project readback.

## Standing streamlined review disposition

This is bounded campaign-execution and queue administration under `MP-STREAMLINED-EXECUTION-001` (MATH-PROGRAMME `docs/governance/STREAMLINED_EXECUTION_AMENDMENT.md`, §§1, 5–7). Approval count, account multiplicity, independent GitHub logins, and a second human review are not completion conditions. Protected checks, immutable launch bytes, Issue Field consistency, reserved execution lease, worker authentication, intake provenance, and claim boundaries remain mandatory. Logical adversarial review of race/security/authority-inflation cases is appropriate within the agent's verification work and cannot be represented as external mathematical independence. If a specialist review is materially required, identify the specific changed material object and governing instrument rather than invoking a generic review habit. Historical PRs and reviews are left intact.
