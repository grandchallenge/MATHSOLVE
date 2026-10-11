# GCL Commander — CHAD-owned MCP operator (engineering handoff)

Status: **prototype implemented and tested locally; CHAD installation, secure-tunnel registration, and live Projects reconciliation remain pending.** Do not claim this branch contains the executable distribution.

A complete separately packaged implementation artifact is attached to the creating ChatGPT conversation as `GCL-Commander-v0.1.0.zip` (SHA-256 `7834b08e798c3cb8dba6cfacada8afc94ed5f5c4b10cd9b9e7471eaa352a3553`); it needs source admission to an appropriate GCL-owned code repository before operational promotion. The artifact is not a durable GitHub source archive merely because this record exists.

The prototype contains Python package `gcl_commander` with:
- MCP SDK v2 server using loopback-only Streamable HTTP or stdio;
- bounded `system_status`, `project_queue_audit`, and `project_queue_reconcile` tools;
- read-only complete GraphQL Project #2 pagination with totalCount, item identity, label completeness and Project ID guards;
- queue semantic classifier matching protected `ci/gcl_queue_class_contract.py` at prototype creation: Erdős catalogue/critics Mathematics despite direct-editorial pickup, typography issue ED07/ED09 Editorial;
- state-preserving Project field corrections gated by exact inventory count and local `GCL_COMMANDER_PROJECT_WRITE=enabled`;
- complete post-write readback and receipt artifacts, no generic terminal capability.
- eleven local pytest unit tests, all passing; a CHAD WSL installer and optional loopback-only systemd user service are included.

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
