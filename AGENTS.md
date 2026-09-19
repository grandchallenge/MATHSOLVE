# Agent instructions

MATHSOLVE coordinates bounded mathematical work packages. It does not certify
claims. Under `GCL-AGENT-STAFFING-001` version `1.0.0`, one Codex system may
implement, staff distinct non-reserved logical audit passes, merge through
satisfied protected controls, and read back the result. Authoring-system
Adversary and Referee passes are declared `non_authoring_read_only`. Automation
may not write directly to protected branches, manufacture reserved authority,
or infer certification from CI or integration.

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
