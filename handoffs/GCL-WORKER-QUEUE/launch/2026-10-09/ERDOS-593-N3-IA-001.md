GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE_AFTER_PROTECTED_ADMISSION
CAMPAIGN: ERDOS-OPEN
TRANCHE: ERDOS-SUCCESSOR-003
ASSIGNMENT_ID: ERDOS-593-N3
DISPATCH_ID: ERDOS-593-N3-IA-001
AGENT_REF: INDEPENDENT-AGENT-ERDOS-593-N3
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
PROTECTED_LEASE_REQUIRED: YES
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO
SIBLING_USE_POLICY: FORBIDDEN

# Lean kernel/source-fidelity replay

Immutable predecessor spec: work_packages/ERDOS_OPEN/ERDOS_593_N3_SOURCE_KERNEL_FIDELITY.md
Protected evidence and adjudication: contributions/ERDOS-OPEN-001/SUCCESSOR_002/adjudications/ERDOS-SUCCESSOR-002-ADJUDICATION-001.json
Cohort: ERDOS-593-SUCCESSOR-BLIND-COHORT-003
Worker role: SOURCE_AUDIT
Timebox: 60 minutes.

Independently replay the Li 2026 arXiv:2606.24882v2 external Lean theorem claim. Pin actual source commit, mathlib lock and environment; run lake build and print axioms; check exact definitions and theorem statements against the protected formal interface. Report precise PASS/FAIL/UNVERIFIED including isolated-vertex and embedding semantics. A green build alone is not certification.

Mandatory first steps: authenticate to GitHub with issue-comment capability; read WORKERS.md and the immutable dispatch and task at the exact protected commit returned by the reservation controller. Use /claim on the issue and wait for CLAIM ACCEPTED before beginning independent work. Read the predecessor adjudication and source spec; never treat external publications or worker returns as certified mathematical facts.

Return exactly one GCL-CONTRIBUTION-RESULT/1 comment on the assigned issue, following the exact issue grammar; provide bounded strongest statement, derivation, external-source premise list, falsification or replay hooks, claim boundary, and next residual. Preserve narrative-only intake security. An unsuccessful or blocked attempt must still return an explicit bounded failure with exact blocker. Do not independently mutate protected branches or claim MathCert authority.

This packet becomes executable only after protected branch admission, matching exact dispatch/source hashes, queue registry/Project projection, and authenticated reservation state.
