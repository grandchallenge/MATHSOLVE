# GCL Commander — CHAD-owned MCP operator (engineering handoff)

Status: **prototype implemented and tested locally; CHAD installation, secure-tunnel registration, and live Projects reconciliation remain pending.** Do not claim this branch contains the executable distribution.

A complete separately packaged implementation artifact is attached to the creating ChatGPT conversation as `GCL-Commander-v0.1.1.zip` (SHA-256 `811b28e216485122bea9f4328e89381a7c9f2831ac269aa365470919aa36ae81`); it needs source admission to an appropriate GCL-owned code repository before operational promotion. The artifact is not a durable GitHub source archive merely because this record exists.

The prototype contains Python package `gcl_commander` with:
- MCP SDK v2 server using loopback-only Streamable HTTP or stdio;
- bounded `system_status`, `project_queue_audit`, and `project_queue_reconcile` tools;
- read-only complete GraphQL Project #2 pagination with totalCount, item identity, label completeness and Project ID guards;
- queue semantic classifier matching protected `ci/gcl_queue_class_contract.py` at prototype creation: Erdős catalogue/critics Mathematics despite direct-editorial pickup, typography issue ED07/ED09 Editorial;
- state-preserving Project field corrections gated by exact inventory count and local `GCL_COMMANDER_PROJECT_WRITE=enabled`;
- complete post-write readback and receipt artifacts, no generic terminal capability.
- thirteen local pytest unit tests, all passing, including two uv-installer regression checks. The WSL installer provisions uv-managed Python 3.12, preserves an incompatible Python 3.10 virtual environment as a backup, and never modifies Ubuntu's system Python; an optional loopback-only systemd user service is included.

## Exact deployment boundary

The host CHAD remains unavailable to the current ChatGPT session. The service is **not installed**, no tunnel is provisioned, and no ChatGPT custom MCP tool connection is registered. Independent capacity control, saved Project views and live pickup/return evidence remain outstanding under [GCL-QUEUE-CLASS-CUTOVER #1049](https://github.com/grandchallenge/MATHSOLVE/issues/1049).

## Mandatory promotion steps

1. Import and inspect the archive's actual source and tests into GCL-owned source control. Verify SHA-256 and run tests under CHAD.
2. Resolve any drift between the prototype classifier and **current exact protected** queue-class source before live write; maintain classification independently of pickup mode.
3. Execute authenticated full Project read-only audit, reconcile only after preflight and explicit local authorization, complete second full readback.
4. Deploy unprivileged MCP service loopback-only and secure authenticated tunnel; verify client permission compatibility for write tools (plan/organization dependent).
5. Run hostile network/auth/command tests and actual two-lane Project cutover tests. Never expose an unrestricted shell or CHAD's raw MCP port.
6. Record exact source SHAs, CI, receipt hashes, tunnel and app authority, Project item counts and protected queue readback in #1049.

Release requires evidence, not just the existence of this handoff.
