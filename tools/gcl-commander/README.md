# GCL Commander — CHAD-owned execution service v0.2.0

**Proposed release v0.2.0.** The v0.1.4 tunnel has been verified from ChatGPT using actual `system_status` and full 1,308-item `project_queue_audit` calls. This release extends it with guarded repository readback, exact Project view-filter readback, and **Windows Task Scheduler logon startup** for WSL systems without systemd. These new capabilities are not live until CHAD upgrades and restarts the tunnel. Project and repository writes remain disabled by default. No API key, local credential or machine path is admitted to GitHub by this package.

## v0.2.0: single CHAD upgrade and autostart registration

Download `GCL-Commander-v0.2.0.zip` to Windows `D:\Downloads`. Verify the archive's published SHA-256 in the ChatGPT response. In the existing WSL terminal paste the complete guarded `if bash -s <<'GCL_V020' ... GCL_V020` block supplied with the release. That block runs the archive's `deploy/upgrade-wsl.sh` in a Bash child process (preserves the interactive shell), replays the full tests, performs a read-only queue audit, registers a **current-Windows-user-only logon Scheduled Task**, and opens a **draft source-control PR** for review. It does **not** start a second tunnel while the currently working foreground tunnel is running. It does not merge any protected branch.

Once installation/registration succeeds, **stop the existing foreground `tunnel-client run` using Ctrl+C**, then in PowerShell:

```powershell
Start-ScheduledTask -TaskName 'GCL Commander CHAD Tunnel'
Get-ScheduledTask -TaskName 'GCL Commander CHAD Tunnel' | Get-ScheduledTaskInfo
```

Wait 10–30 seconds; from WSL, `curl -fsS http://127.0.0.1:8080/readyz` should succeed. ChatGPT should then be able to call `system_status`, `project_queue_views_readback`, `governed_repository_head`, and `governed_repository_pr` again. In this mode the tunnel auto-restarts on process failure and relaunches at Windows **interactive user logon**. It does not guarantee availability before a user logs into Windows, while CHAD is powered off, or when the user's WSL distribution is unavailable; those require a separately authorized headless Windows service design.

**The WSL supervisor is bounded:** it acquires a flock singleton, refuses to compete with an already-ready tunnel, requires a mode-0600 private runtime key and specific unchanged policy, prohibits both Project/repository writes, logs only to chmod-0600 local state, and retries abnormal tunnel-client exits with backoff. Task Scheduler uses only a non-elevated interactive principal; the installer refuses replacement of a different task.

## Live two-lane queue acceptance

The protected MATHSOLVE queue document records **the EDITORIAL and MATHEMATICS saved views as already verified**, together with global AVAILABLE. The protected live Mathematics /claim controller also already has an eight-active-reservation guard from complete trusted ledger comments and serialized claim/release/reap. These need readback, not reinvention. The Editorial eight-slot policy remains a *planning budget*, **not enforced worker concurrency**: enforceable active ownership requires verified authenticated direct-issue starts and result/return histories without creating a fake Solve reservation. The returned Mathematics canary MATHSOLVE #999 has historical queue and result comments but its path must not be treated as final production acceptance without capture, protected merge, replay, adjudication and successor readback.

The v0.2.0 repository tools are **read-only**: exact protected `main` SHA, SHA-pinned small nonsecret file contents, and PR identity/review evidence; unknown repos, sensitive paths, stale heads, oversized files and incomplete reviews fail closed. A proposed document writer exists in source only as a guaranteed refusal, not as an advertised operational MCP tool. Neither queue reclassification, merge, issue mutations, worker-result injection nor arbitrary shell execution is available through these new tools.

---


A constrained Model Context Protocol (MCP) operator service for Grand Challenge Labs. **v0.1.3 was installed and its read-only CHAD audit passed; v0.1.4 secure-tunnel deployment has not yet been run or connected to ChatGPT.** The first bounded tool is a full Project #2 semantic queue reconciliation with project-wide pagination, preflight, exact-total guard, and full post-write readback.

## Safety model

- No general shell execution, no arbitrary file browsing, no unrestricted GitHub mutations.
- Runs `gh api` using the CHAD user's existing authenticated GitHub credential; no credential material is returned through MCP tools or receipts.
- Semantic queue class and pickup mode are independent. Erdős source-audit work may be Mathematics while using direct-editorial pickup. Typography source defects remain Editorial.
- Dry-run audit first, then exact-total assertion and explicit local opt-in for Project field updates. Does not change worker claims, leases, labels, issues, protected merge, or returns.
- Receipt files are chmod 0600 under `~/.local/state/gcl-commander/receipts/`.
- Default transport is local stdio. HTTP is loopback-only (`127.0.0.1:8765/mcp`), and requires MCP SDK v2. **Never expose this port publicly.** Only an authenticated secure MCP tunnel should bridge it to ChatGPT.
- ChatGPT write-tool availability varies by plan. If unavailable, use the local CLI and/or other authorized GCL runner instead.

## WSL installation on CHAD (uv-managed Python 3.12)

CHAD's Ubuntu Python 3.10 cannot install this package (requires Python >=3.11). The installer uses [uv](https://docs.astral.sh/uv/) to provision Python 3.12 without modifying Ubuntu's system Python. The installer is safe to rerun: if the previous failed pip install left an incompatible `.venv`, it is **preserved** under `.venv-before-uv-<timestamp>` before creating a fresh environment.

Download the v0.1.4 package to Windows `D:\Downloads`, inspect its published SHA-256, then in WSL use these commands to upgrade an existing source directory **without losing local state**:

The recommended CHAD invocation is in the **CHAD-safe copy/paste upgrade** section below. Never paste `set -euo pipefail` directly into the interactive WSL shell; any error could close it.

If you do not want to download the new bundle, the equivalent manual recovery from an already extracted v0.1.0 source is: install uv, run `uv python install 3.12`, preserve the failed `.venv`, create `uv venv --managed-python --python 3.12 .venv`, then install with `uv pip install --python .venv/bin/python -e '.[test]'` and run tests. No system Python changes are required.

The installation script itself (which may also be run independently after updating an existing checkout) performs `uv python install 3.12`, `uv venv --managed-python --python 3.12 .venv`, and `uv pip install --python .venv/bin/python -e '.[test]'`. `gh auth status` must already work inside WSL. No sudo is needed for uv or the Python virtual environment. The service is **not** automatically started.

Do **not** run the earlier pickup-based classification scripts. This reconciler follows the protected semantic classifier as of Oct 11, 2026; changes to that classifier need a fresh synchronisation and replay before Project mutation.

After inspecting the audit's complete `total` and `sample_changes`, choose the current exact total from that readback (not an older reported count):

```bash
export GCL_COMMANDER_PROJECT_WRITE=enabled
gcl-commander reconcile --expected-total <CURRENT_AUDIT_TOTAL> --apply
```

The API snapshot must have exactly `totalCount` rows before any writes. The Project still needs saved-view creation/readback, governed admission budgets, live worker returns, and receipt registration in MATHSOLVE #1049. This service does **not** pretend those tasks are complete.

### Optional local MCP service

```bash
export GCL_COMMANDER_TRANSPORT=http
export GCL_COMMANDER_PORT=8765
gcl-commander serve
```

Expose only through an authenticated Secure MCP Tunnel supported by ChatGPT; configure tunnel authorization and host/origin validation in accordance with the current MCP SDK and tunnel vendor instructions. Do not install or trust a tunnel that anonymously exposes `/mcp`. Prefer an OS-managed service with an unprivileged user and credentials stored only in CHAD's `gh` key store. No sudo available to MCP tools.

## First milestone acceptance

1. `pytest` passes on CHAD.
2. Correct authenticated `fyremael` actor.
3. Full Project #2 enumeration and exact item count.
4. All eligible GCL issues semantically classified, including Erdős exceptions.
5. Authenticated Project-write reconciliation and second complete readback.
6. Evidence attached to #1049; separate Project views and capacity controls treated as subsequent gates.

### Optional systemd user service on CHAD

The bundle includes `deploy/gcl-commander.service` and `deploy/install-wsl.sh`. The installer creates a uv-managed Python 3.12 environment, runs tests, and checks the authenticated actor; it does not enable any system service. Before enabling the user service, review WSL systemd support and filesystem hardening settings. The default user service has `GCL_COMMANDER_PROJECT_WRITE=disabled`. Explicit local opt-in is needed to enable write operations after evidence review.

## v0.1.3 — live-source-role routing correction and shell safety

A Project audit on CHAD exposed a fail-closed classifier defect: legitimate
MATHSOLVE Erdős dispatches carrying `gcl-role:source-audit` were rejected.
Those issues remain Mathematics and use the existing `reservation_controlled`
pickup mode. A source-audit **role** does not grant editorial-style pickup.
Unknown `gcl-pickup:*` labels on MATHSOLVE still fail closed. This release also
includes the offending issue number in any future classification error.
This prototype repair must be reconciled against the independently protected
GCL classifier before queue mutation. Run `audit` again read-only.

The v0.1.3 installer and upgrader reject accidental `source` without terminating
the caller or setting `errexit`. Each legitimate installation runs as an isolated
Bash process. The CHAD-safe wrapper catches child failures even if the parent
Bash session already has `set -e` enabled.

For an already-installed uv environment, apply the complete source package
(rather than only the deploy script), preserving `.venv` and local state.
Back up the source directory first and overlay the extracted v0.1.4 source.


## CHAD-safe copy/paste upgrade

After downloading `GCL-Commander-v0.1.4.zip` to `D:\\Downloads`, paste this
**whole block** into CHAD's WSL shell. Only the child Bash uses `set -euo
pipefail`; neither the installer's exit codes nor the audit's `BLOCKED` outcome
can terminate the interactive shell. This remains safe even if `errexit` was
previously enabled in that shell.

```bash
if bash -s <<'GCL_SAFE_UPGRADE'
set -euo pipefail
ZIP=/mnt/d/Downloads/GCL-Commander-v0.1.4.zip
EXPECTED_SHA256=REPLACE_WITH_PUBLISHED_ARCHIVE_SHA256
[[ -f "$ZIP" ]] || { echo "BLOCKED: Download $ZIP first" >&2; exit 2; }
printf '%s  %s\n' "$EXPECTED_SHA256" "$ZIP" | sha256sum -c -
TMP=$(mktemp)
trap 'rm -f "$TMP"' EXIT
unzip -p "$ZIP" gcl-commander/deploy/upgrade-wsl.sh > "$TMP"
bash "$TMP" "$ZIP"
GCL_COMMANDER_GITHUB_ACTOR=fyremael "$HOME/gcl-commander/.venv/bin/gcl-commander" audit
GCL_SAFE_UPGRADE
then
  printf '%s\n' 'GCL Commander upgrade and read-only audit: PASS'
else
  printf '%s\n' 'GCL Commander upgrade/audit returned an error; WSL shell remains open.' >&2
fi
```

Replace the SHA-256 placeholder with the exact hash published with the v0.1.4
release before running. No `reconcile --apply` should be attempted until the
independent protected classifier fix and complete audit have passed.


## v0.1.4 — private Secure MCP Tunnel deployment on CHAD

This release adds an **outbound-only**, OpenAI-hosted Secure MCP Tunnel path. Its `tunnel-client` spawns GCL Commander's local **stdio MCP transport**. There is no public listener and no requirement to expose `127.0.0.1:8765` through a public tunnel. The original `gcl-commander.service` HTTP example is NOT the recommended ChatGPT integration.

**Prerequisites held outside this package:** an OpenAI Platform Tunnel ID associated with the appropriate ChatGPT workspace and a separate runtime API key authorized for Tunnels Read + Use. They cannot be invented by this installer. Tunnel creation requires Tunnels Read + Manage. See https://platform.openai.com/settings/organization/tunnels and https://platform.openai.com/settings/organization/api-keys . These are different from the existing `fyremael` GitHub credential. Never paste either key into this chat or a GitHub issue.

After upgrading to v0.1.4 on CHAD and confirming the existing read-only `gcl-commander audit` remains correct, run the following **commands in isolated child Bash processes**. Never `source` the installers or paste `set -euo pipefail` into your interactive shell.

```bash
if bash "$HOME/gcl-commander/deploy/install-openai-tunnel-client-wsl.sh"; then
  echo 'Official OpenAI tunnel-client checksum verified'
else
  echo 'Tunnel-client install blocked; interactive shell preserved'
fi

if bash "$HOME/gcl-commander/deploy/configure-openai-tunnel-wsl.sh"; then
  echo 'Private tunnel profile created'
else
  echo 'Profile setup blocked; interactive shell preserved'
fi

if bash "$HOME/gcl-commander/deploy/activate-openai-tunnel-wsl.sh"; then
  echo 'Activation attempted; inspect the actual health/ready evidence'
else
  echo 'Tunnel activation blocked; interactive shell preserved'
fi
```

The configurator prompts for the Platform Tunnel ID and runtime API key. The runtime key input is hidden and stored only in `~/.config/gcl-commander/tunnel.env` with `0600` permissions. The service loads that file; it never uses a token in its executable command line, logs, or GitHub repository. The installed tunnel binary is downloaded directly from the official `openai/tunnel-client` GitHub release and checked against the matching official `SHA256SUMS.txt`. The script refuses architecture and asset-name drift.

The optional systemd *user* service has `GCL_COMMANDER_PROJECT_WRITE=disabled`, spawns `gcl-commander serve` over stdio, and does not expose a public port. On WSL hosts without systemd, the script stops without enabling an unsupported service. Even with systemd available, WSL itself must be running for the service to remain available; Windows boot persistence is a separate operational concern. After activation, inspect `tunnel-client doctor --profile gcl-commander --explain` and `/healthz` and `/readyz` or the client `/ui` before calling the runtime ready.

### Explicit ChatGPT connection step

Navigate to ChatGPT Plugins → Add custom MCP server, choose **Tunnel**, and select the *same* Platform tunnel ID. Perform the required account/workspace permission flow and install the resulting plugin. This step needs your explicit action and must not be represented as done by installing the CHAD service. Full write-enabled custom MCP support is plan/workspace-dependent; the first connected tool test should be `system_status` or `project_queue_audit` (read-only). Project mutation remains locally disabled.

### Runbook boundaries

- Never substitute the GitHub token for the Platform runtime key.
- Never mark #1049 closed on a local audit alone; saved views, live admission/writer, and worker pickup/RESULT/1 replay require separate proof.
- Never promote MCP tool write access merely by changing an app permission; local policy must enable and audit the specific authorized mutation first.
- The CHAD-local receipt locations are not protected GitHub evidence until imported and bound to an exact revision.
- Only invoke a tunnel daemon once per tunnel ID. Do not spawn multiple copies under background `nohup` and systemd simultaneously.


## v0.2.1 — CHAD-proven detached startup recovery

The original CHAD Windows Task Scheduler approach could not persist its WSL process
(result `0xFFFFFFFF`). Direct synchronous Windows PowerShell to WSL Bash did
work, and became ready in approximately one second. The successful recovery is
now included as source rather than being stranded in a downloaded ZIP:

- `deploy/gcl-chad-detached-start.sh` launches the protected supervisor using
  `nohup setsid -f`, preserving the singleton `flock` and read-only execution;
- `deploy/start-at-logon.ps1` is the short current-user HKCU logon shim;
- `deploy/install-chad-detached-autostart.ps1` verifies exact user, old task,
  expected Linux launcher hash, two post-parent readiness samples, live client
  PID and supervisor lock before registering the new HKCU Run entry;
- `deploy/install-chad-autostart.ps1` now blocks the obsolete Scheduler installer.

These files reflect the successful CHAD current-session recovery. They do not
establish automatic reconnection after a *new Windows sign-in*, which needs a
fresh, operator-observed acceptance checkpoint. They also do not make a GitHub
queue lifecycle or formal certification claim. Never store API keys, WSL
`tunnel.env`, or raw private supervisor logs in a source PR.

The ChatGPT MCP server deliberately exposes only typed, read-only repository
inspection and Project audit functions unless a later protected governance
change authorizes write scope. Refresh the ChatGPT custom-plugin tool manifest
when the backend's new capabilities are not visible in an existing session.


### Read-only operator acceptance commands

After installing the candidate and checking `doctor`, the following commands
exercise the same exact-head and protected-view functions as the MCP backend,
without waiting for ChatGPT to refresh a cached tool manifest:

```bash
GCL_COMMANDER_GITHUB_ACTOR=fyremael ~/gcl-commander/.venv/bin/gcl-commander views
GCL_COMMANDER_GITHUB_ACTOR=fyremael ~/gcl-commander/.venv/bin/gcl-commander repo-head grandchallenge/MATHSOLVE
```

Neither command changes GitHub or the local tunnel state. Source PR publication
remains a separate explicit draft action through
`bash ~/gcl-commander/deploy/publish-source-pr-wsl.sh` and is not protected
admission until review, checks and exact-head readback are complete.
