# GCL Commander — CHAD-owned MCP operator (engineering handoff)

Status: **CHAD tunnel and authenticated read-only MCP integration LIVE**; current verified Project #2 inventory **1,311** (1,271 Mathematics, 40 Editorial), zero class corrections, all write flags disabled. The recovered Linux-detached supervisor survives termination of its Windows launcher, and an HKCU Run logon entry is registered. Fresh Windows sign-in/reboot acceptance and executable-source PR admission are **not yet complete**. This documentary branch does **not** contain the executable distribution.

A complete separately packaged implementation artifact is attached to the creating ChatGPT conversation as `GCL-Commander-v0.1.4.zip` (SHA-256 `9a600fe946e0f876ed9635bef490bf2d8dc10a5533f0402d2ee3225db2a09d50`); it needs source admission to an appropriate GCL-owned code repository before operational promotion. The artifact is not a durable GitHub source archive merely because this record exists.

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

OpenAI's official [Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels) and [openai/tunnel-client](https://github.com/openai/tunnel-client) provide an outbound-only connection; no inbound CHAD port needs exposure. v0.1.4 adds (1) an official release checksum-verifying WSL tunnel-client installer, (2) an interactive hidden-input tunnel-id/runtime-key profile configurator, (3) loopback-only health and stdio MCP launch, (4) a systemd **user** service with `GCL_COMMANDER_PROJECT_WRITE=disabled`, and (5) local bash syntactic, shell-survival and fail-closed tests. All **29/29** local tests pass. Archive: `GCL-Commander-v0.1.4.zip`; SHA-256 `9a600fe946e0f876ed9635bef490bf2d8dc10a5533f0402d2ee3225db2a09d50`.

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


## v0.2.0 follow-on: CHAD logon persistence and read-only repository tools

Candidate release `GCL-Commander-v0.2.0.zip` created and locally validated (SHA-256 `5c95d6ca4ffad2e31e409027cba53b6efc66ccda93f8d310faf968f6e8e5573a`, **53/53 tests PASS**). CHAD's earlier v0.1.4 tunnel is **genuinely ChatGPT-connected**: live `system_status` and two complete read-only `project_queue_audit` invocations returned `fyremael`, 1308 jobs, 37 Editorial, 1271 Mathematics and zero class corrections. This is NOT evidence of persistence across Windows restart.

v0.2.0 adds a WSL tunnel supervisor with `flock` singleton, bounded restart backoff, secret mode checks, no inbound MCP listener, explicit Project/repository write-disable; plus a Windows **non-elevated current-user logon Scheduled Task** installer (for CHAD's no-systemd WSL). It adds typed MCP tools `project_queue_views_readback`, `governed_repository_head`, `governed_repository_file`, and `governed_repository_pr`. These are read-only with an explicit repository allowlist, exact main SHA and file size/path guards, and no generic command executor. Repository document proposals remain unactivated even if an environment flag is set.

A shell-safe `deploy/upgrade-wsl.sh` backs up existing source, tests before overlay, replays after overlay, and rolls back on failure; a `deploy/publish-source-pr-wsl.sh` creates a DRAFT candidate source PR containing explicit source files under `tools/gcl-commander/`. The existing GitHub handoff PR #1070 contains only this documentary record: **the candidate code will not become durable source authority until CHAD executes its publisher and GCL protects/admits that separate PR.** No local machine secrets belong in GitHub. Windows logon persistence is not live until CHAD installs/starts the task and proves new health/readiness after foreground shutdown or reboot.

**Queue acceptance evidence:** protected Council Clerk #2563 already verified three saved view identities: EDITORIAL `PVTV_lADOB9Ao_c4BlwurzgMAfZU`, MATHEMATICS `PVTV_lADOB9Ao_c4BlwurzgMAfZY`, global AVAILABLE `PVTV_lADOB9Ao_c4BlwurzgL64bo`. Protected Solve worker workflow already serializes claims and enforces eight active Mathematics reservations based on trusted lease history; Editorial eight slots are still planning only until authenticated direct-issue start/return custody exists. MATHSOLVE #999 is now labeled RETURNED with capture comments, but its original `github-actions[bot]` claim/RESULT/1 is not evidence for a genuinely distinct-worker acceptance, nor of downstream protected adjudication and successor closure. Do not certify the full two-lane worker lifecycle on these facts alone.


## v0.2.1 source-concordance and CLI acceptance candidate

GCL Commander v0.2.1 is a 31-file, 45,940-byte candidate archive, SHA-256 `a6d4f43504e5e434a177223274ed32dcc74a59fdaf960cf251cdc8bdb8be4ed9`; the verified local suite is **61/61 passing**. This source candidate includes the exact hash-pinned WSL Linux-detach launcher actually validated on CHAD, current-user Windows logon wrapper and installer, and a fail-closed legacy Task Scheduler entry point. It adds repeatable, read-only CLI parity for backend MCP `views`, `repo-head`, `repo-file` and `repo-pr`, so view and exact-head checks can be exercised on CHAD independently of ChatGPT's cached tool catalog. The original 53-test v0.2.0 source is insufficient to reproduce the working detached Windows startup.

Protected source admission is still pending: neither this documentary branch nor the downloadable archive is a GitHub source PR. To produce the reviewable source branch, CHAD should checksum-verify the v0.2.1 archive, execute its child-process `deploy/upgrade-wsl.sh` (backs up and replays tests), execute read-only `gcl-commander views` and `repo-head grandchallenge/MATHSOLVE`, then run `bash ~/gcl-commander/deploy/publish-source-pr-wsl.sh`. The publisher pins current main, creates a new **DRAFT** feature PR and runs tests, without granting merge/certification or enabling writes. CI/review/merge must bind exact head. A fresh Windows logon and ChatGPT tool re-discovery are additional acceptance steps. Retain the eight-slot Mathematics reservation-policy and unproven Editorial active-worker cap as separate queue work; neither is changed by the Commander upgrade.
