#!/usr/bin/env bash
# CHAD WSL (no systemd): serial, bounded tunnel-client restart supervisor.
# Run with bash as a child process; never source into interactive shell.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  echo 'BLOCKED: run supervisor using bash, not source' >&2
  return 0
fi
set -euo pipefail
umask 077
ROOT="${HOME}/gcl-commander"
ENV_FILE="$HOME/.config/gcl-commander/tunnel.env"
CLIENT="$HOME/.local/bin/tunnel-client"
STATE="$HOME/.local/state/gcl-commander"
[[ -x "$CLIENT" && -x "$ROOT/.venv/bin/gcl-commander" ]] || {
  echo 'BLOCKED: GCL Commander and verified tunnel-client must be installed' >&2; exit 2;
}
[[ -f "$ENV_FILE" && ! -L "$ENV_FILE" && "$(stat -c %a "$ENV_FILE")" = 600 ]] || {
  echo 'BLOCKED: protected tunnel.env missing or permissions unsafe' >&2; exit 2;
}
[[ "$(stat -c %a "$(dirname "$ENV_FILE")")" = 700 ]] || {
  echo 'BLOCKED: tunnel credential directory is not private' >&2; exit 2;
}
[[ "$(wc -l < "$ENV_FILE")" = 4 ]] || { echo 'BLOCKED: unexpected secret config format' >&2; exit 2; }
KEY="$(sed -n 's/^CONTROL_PLANE_API_KEY=//p' "$ENV_FILE")"
[[ "$KEY" =~ ^sk-[A-Za-z0-9_-]{16,}$ ]] || { echo 'BLOCKED: runtime credential invalid format' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_PROJECT_WRITE=disabled' "$ENV_FILE" || { echo 'BLOCKED: project mutation not permitted' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_TRANSPORT=stdio' "$ENV_FILE" || { echo 'BLOCKED: stdio required' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_GITHUB_ACTOR=fyremael' "$ENV_FILE" || { echo 'BLOCKED: actor mismatch' >&2; exit 2; }
export CONTROL_PLANE_API_KEY="$KEY"
export GCL_COMMANDER_TRANSPORT=stdio
export GCL_COMMANDER_PROJECT_WRITE=disabled
export GCL_COMMANDER_REPO_WRITE=disabled
export GCL_COMMANDER_GITHUB_ACTOR=fyremael
unset KEY
mkdir -p "$STATE"
chmod 700 "$STATE"
exec 9>"$STATE/tunnel-supervisor.lock"
flock -n 9 || { echo 'BLOCKED: GCL Commander tunnel supervisor is already running' >&2; exit 3; }
LOG="$STATE/tunnel-supervisor.log"
if [[ -f "$LOG" && "$(stat -c %s "$LOG")" -gt 5242880 ]]; then
  mv "$LOG" "$LOG.old"
fi
: >>"$LOG"
chmod 600 "$LOG"
CHILD=''
stopping=0
stop() {
  stopping=1
  if [[ -n "$CHILD" ]]; then
    kill "$CHILD" 2>/dev/null || true
    wait "$CHILD" 2>/dev/null || true
  fi
}
trap stop TERM INT

# Do not compete with an existing foreground tunnel or service.
if curl --silent --fail --max-time 2 http://127.0.0.1:8080/readyz >/dev/null; then
  echo 'BLOCKED: existing healthy tunnel already listening; stop foreground tunnel before scheduled startup' >&2
  exit 4
fi

failures=0
while [[ "$stopping" == 0 ]]; do
  printf '[%s] starting tunnel-client (supervised; write tools disabled)\n' "$(date -u +%FT%TZ)" >> "$LOG"
  "$CLIENT" run --profile gcl-commander >>"$LOG" 2>&1 &
  CHILD=$!
  # The tunnel-client owns reconnection; supervisor restarts only if the process exits.
  status=0
  wait "$CHILD" || status=$?
  CHILD=''
  [[ "$stopping" == 0 ]] || break
  failures=$((failures+1))
  printf '[%s] tunnel-client exited (%s), retry=%s\n' "$(date -u +%FT%TZ)" "$status" "$failures" >> "$LOG"
  # Bounded backoff 10,20,40,60 seconds; never spin on invalid credentials.
  delay=$((10 * (2 ** (failures < 3 ? failures-1 : 2))))
  if ((delay > 60)); then delay=60; fi
  sleep "$delay" || true
done
