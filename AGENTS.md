# Agent instructions

**Engineering architecture and reliability:** Adopt [GCL-ENGINEERING-001 v1.0.0](https://github.com/grandchallenge/gcl-standards/blob/2a3cfed9419ba9b74eeaaee70b9db8c3f47f3c9b/standards/GCL-ENGINEERING-001.md), pinned at protected `gcl-standards` commit `2a3cfed9419ba9b74eeaaee70b9db8c3f47f3c9b`. Engineering agents own architecture, necessity, integration, tests, deploy/readback and retirement; reuse GitHub and existing components before inventing infrastructure. Do not duplicate workflow authority or mistake CI/merge for live completion. Preserve this repository's superior, reserved, and domain-specific policies. Cross-repository adoption requires explicit readback, never assumption.

If you are an external or zero-context agent and do not already hold a bounded
assignment, read [`WORKERS.md`](WORKERS.md) before doing anything else.
That file is the stable discovery/bootstrap entrypoint for the public GCL Worker
Queue. If you already hold a specific immutable launch artifact, follow that
artifact instead.

MATHSOLVE coordinates bounded mathematical work packages. It does not certify
claims. Under `GCL-AGENT-STAFFING-001` version `1.0.0`, one Codex system may
implement, staff distinct non-reserved logical audit passes, merge through
satisfied protected controls, and read back the result. Authoring-system
Adversary and Referee passes are declared `non_authoring_read_only`. Automation
may not write directly to protected branches, manufacture reserved authority,
or infer certification from CI or integration.

## Routine protected execution: no review ceremony

Apply MATH-PROGRAMME's binding `MP-STREAMLINED-EXECUTION-001` to bounded,
already-authorized MATHSOLVE queue registration, source-lock staging, dispatch,
intake engineering, CI remediation, maintenance and documentary updates.
The sequence is material-evidence classification, affected checks, delegated
disposition, protected PR merge, and readback. **Do not require an independent
non-author GitHub approval, a distinct user account, a Human Steward signoff,
or a generic Referee/Clerk pass for routine operational work.** A team review
request does not by itself create a mandatory approval gate.

Specialist independent scrutiny remains in force for actual mathematical proof
or certification promotion, source-semantic adjudication, constitutional
authority expansion, security-sensitive protection weakening, or external claim
promotion where the governing claim/control demands it. Independent worker
results and independent mathematical verification are not substitutes for
routine PR signoff, and routine PR signoff is not a proof of mathematical truth.
Follow the actual protected GitHub ruleset and record authoritative readback;
never use standing delegation to bypass a real protected check or issue-field
source lock.

MATHSOLVE adopts `GCL-AGENT-CONTINUITY-001@1.0.0` from
`grandchallenge/INTELLECT/governance/agent_execution/GCL-AGENT-CONTINUITY-001.md`.
For multi-step or interruption-prone work, agents must bind the live exact head,
work in narrow durable tranches, checkpoint proof-quality results before opening
another expensive branch, read back after mutation, and recover from timeout,
connector failure, truncated output, or context loss from repository state.
Those failures are not substantive stopping conditions. A successor agent must
rebind live state and continue from the last durable checkpoint without asking
the Human Steward to restate already-established authority or facts. Before
stopping, name the exact governance, authentication, safety, materially changed
state, scope, or substantive evidentiary boundary that prevents the next
authorized recovery action.

## Completed operation handoffs

- **GCL-RWP-003:** [operator completion and recovery record](handoffs/GCL-RWP-003/COMPLETION.md).
  The bounded continuity pilot and research assignment are closed. Consult that
  record and its pinned issue/commit evidence before interpreting historical
  `received_unadjudicated` intake metadata. This entry grants no mathematical
  certification, new worker reservation, or reopening authority.
