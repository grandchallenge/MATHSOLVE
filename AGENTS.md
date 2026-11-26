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

## Binding CHAD-local Lean placement

Apply the Human Steward's 2026-11-24 placement instruction in [MATH-PROGRAMME AGENTS.md](https://github.com/grandchallenge/MATH-PROGRAMME/blob/97d0f0d4b5aee119e4002778ecb870b66955aea9/AGENTS.md), reaffirmed 2026-11-25, to all new CHAD-local Lean development, scratch checks, replay preparation and bounded Lake builds. Before each local build use `~/.local/bin/gcl-lean-work status`, stage an exact source revision with `gcl-lean-work stage REPO EXACT_COMMIT PROJECT_SUBDIR NAME` (or `new NAME TOOLCHAIN` for scratch), seed only exact locked dependencies, and invoke `gcl-lean-work run NAME lean|lake ...`. Verify the resolved source, build, package, compiler, cache and temporary paths use the dedicated native ext4 NVMe-backed `/mnt/gcl-lean-work` or `/mnt/gcl-lean-ssd` volumes; do not merely move the compiler. Preserve exact toolchain/dependency pins, workspace isolation and capacity reserve. Existing HDD worktrees may remain for Git custody, not local compilation. On placement, mount or capacity failure, recover the SSD environment or use an authorized alternate runner; no silent HDD fallback and no bypass via absolute compiler paths. Record placement in local execution receipts. Do not remove other workers' active workspaces. This requirement does not alter protected review, evidence or certification gates.

## Required CI resource isolation

Classify the exact material transition before allocating expensive CI runners.
Native PNP-ABOVE research under `research/PNP-ABOVE/` uses its own locked
upstream replay; it is not a dependency of the local RH/NS, Erdős 602, PNP
library bridge, Union-Closed, or Ten Proofs replay jobs. Do not dispatch those
jobs for an isolated native PNP-ABOVE transition. Shared Lean environment and
compiler-checker changes retain conservative coverage; full Solve CI replay is
available by explicit manual dispatch. The root import index is not by itself
a reason to run every campaign: classify its actual import delta. Retain the
required global ledger, routing, policy and security checks. Never interpret a
skipped replay as mathematical evidence or substitute this CI route for native
source-locked validation. New replay steps must have explicit material routing
and a negative-control test proving an unrelated change does not launch them.
