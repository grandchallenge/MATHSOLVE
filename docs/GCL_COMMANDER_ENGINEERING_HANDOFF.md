# GCL Commander — CHAD-owned MCP operator (engineering handoff)

Status: **prototype implemented and tested locally; CHAD doctor/authentication confirmed, read-only 1,308-item semantic audit confirmed clean; secure-tunnel registration and live Projects reconciliation remain pending.** Do not claim this branch contains the executable distribution.

A complete separately packaged implementation artifact is attached to the creating ChatGPT conversation as `GCL-Commander-v0.1.4.zip` (SHA-256 `cfe3c4f7b53821d4155fd8597fe9219bad118447fa21b83f4a6968acdc6b34e4`); it needs source admission to an appropriate GCL-owned code repository before operational promotion. The artifact is not a durable GitHub source archive merely because this record exists.

The prototype contains Python package `gcl_commander` with:
- MCP SDK v2 server using loopback-only Streamable HTTP or stdio;
- bounded `system_status`, `project_queue_audit`, and `project_queue_reconcile` tools;
- read-only complete GraphQL Project #2 pagination with totalCount, item identity, label completeness and Project ID guards;
- queue semantic classifier matching protected `ci/gcl_queue_class_contract.py` at prototype creation: Erdős catalogue/critics Mathematics despite direct-editorial pickup, typography issue ED07/ED09 Editorial;
- state-preserving Project field corrections gated by exact inventory count and local `GCL_COMMANDER_PROJECT_WRITE=enabled`;
- complete post-write readback and receipt artifacts, no generic terminal capability.
- twenty-nine local pytest unit tests, all passing, including two uv-installer regression checks. The WSL installer provisions uv-managed Python 3.12, preserves an incompatible Python 3.10 virtual environment as a backup, and never modifies Ubuntu's system Python; an optional loopback-only systemd user service is included.

## First live audit finding and bounded fix

CHAD authenticated `fyremael` successfully under uv/Python 3.12, but its first full read-only Project audit stopped with `INVALID_MATHSOLVE_PICKUP_OR_SOURCE_ROLE`. Live GitHub evidence confirms legitimate reserved MATHSOLVE Erdős dispatches (#843, #1033, etc.) carry the `gcl-role:source-audit` **role**. This label does not imply direct-editorial pickup. Protected classifier remediation and two regression tests are in [PR #1071](https://github.com/grandchallenge/MATHSOLVE/pull/1071). Commander v0.1.4 incorporates the matching local fix and preserves bans on direct pickup labels on MATHSOLVE. It adds issue identity on subsequent classification errors. No live Project mutation was undertaken. Re-audit after deployment and retain full exact receipts.

## Shell-survival repair in v0.1.3

Both packaged installer and upgrader refuse accidental sourcing without changing parent shell options. Copy/paste invocations now use `if bash -s <<'GCL_SAFE_UPGRADE'` to isolate `set -euo pipefail` and child error codes. Simulated WSL bash with parent `errexit` enabled survives failed child upgrades; regression tests for shell syntax, sourcing, failed upgrade and documented paste wrapper pass. **Never paste an unguarded top-level `set -euo pipefail` into CHAD's interactive shell.** New archive SHA-256 above; prior archive hashes must not be reused. Full 22-test local replay passes.

## Private outbound Secure MCP Tunnel candidate — v0.1.4

OpenAI's official [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels) and [openai/tunnel-client](https://github.com/openai/tunnel-client) provide an outbound-only connection; no inbound CHAD port needs exposure. v0.1.4 adds (1) an official release checksum-verifying WSL tunnel-client installer, (2) an interactive hidden-input tunnel-id/runtime-key profile configurator, (3) loopback-only health and stdio MCP launch, (4) a systemd **user** service with `GCL_COMMANDER_PROJECT_WRITE=disabled`, and (5) local bash syntactic, shell-survival and fail-closed tests. All **29/29** local tests pass. Archive: `GCL-Commander-v0.1.4.zip`; SHA-256 `cfe3c4f7b53821d4155fd8597fe9219bad118447fa21b83f4a6968acdc6b34e4`.

**Do not declare a live tunnel.** CHAD must install v0.1.4, the Platform owner must provision a tunnel ID and runtime key with Tunnels Read+Use, the tunnel-client must pass `doctor --profile gcl-commander --explain` and health/ready readback, and the operator must explicitly register/install the plugin in ChatGPT. The account's full write-tool eligibility is independent of CHAD readiness and must be established before promising direct Project mutation. No secure-tunnel credentials have been pasted into GitHub. Executable source remains only in the downloadable archive pending protected source admission.

## Exact deployment boundary

The host CHAD remains unavailable for remote shell access to this ChatGPT session. The user has confirmed local CHAD installation through authenticated `doctor`; v0.1.3 upgrade and complete read-only audit were confirmed by the CHAD operator, no tunnel is provisioned, and no ChatGPT custom MCP tool connection is registered. Independent capacity control, saved Project views and live pickup/return evidence remain outstanding under [GCL-QUEUE-CLASS-CUTOVER #1049](https://github.com/grandchallenge/MATHSOLVE/issues/1049).

## Mandatory promotion steps

1. Import and inspect the archive's actual source and tests into GCL-owned source control. Verify SHA-256 and run tests under CHAD.
2. Resolve any drift between the prototype classifier and **current exact protected** queue-class source before live write; maintain classification independently of pickup mode.
3. Execute authenticated full Project read-only audit, reconcile only after preflight and explicit local authorization, complete second full readback.
4. Deploy unprivileged MCP service loopback-only and secure authenticated tunnel; verify client permission compatibility for write tools (plan/organization dependent).
5. Run hostile network/auth/command tests and actual two-lane Project cutover tests. Never expose an unrestricted shell or CHAD's raw MCP port.
6. Record exact source SHAs, CI, receipt hashes, tunnel and app authority, Project item counts and protected queue readback in #1049.

Release requires evidence, not just the existence of this handoff.
