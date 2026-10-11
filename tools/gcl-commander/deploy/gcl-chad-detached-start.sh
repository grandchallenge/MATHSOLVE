#!/usr/bin/env bash
# GCL Commander CHAD: detach the existing supervised tunnel within WSL.
# Intended to be called synchronously via wsl.exe. No credentials are printed.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  echo 'BLOCKED: execute as a child; do not source this script' >&2
  return 0
fi
set -euo pipefail
umask 077
SUP="$HOME/gcl-commander/deploy/supervise-openai-tunnel-wsl.sh"
STATE="$HOME/.local/state/gcl-commander"
LOG="$STATE/tunnel-supervisor.log"
READY_URL='http://127.0.0.1:8080/readyz'

if [[ "$(id -un)" != 'jim' || ! -f "$SUP" || -L "$SUP" ]]; then
  echo 'BLOCKED: exact CHAD supervisor or Linux identity mismatch'
  exit 2
fi
for utility in nohup setsid flock curl stat; do
  if ! command -v "$utility" >/dev/null 2>&1; then
    printf 'BLOCKED: required utility missing: %s\n' "$utility"
    exit 2
  fi
done
if ! bash -n "$SUP"; then
  echo 'BLOCKED: existing supervisor fails Bash syntax'
  exit 2
fi

ready() { curl --silent --fail --max-time 2 "$READY_URL" >/dev/null 2>&1; }
if ready; then
  echo 'ALREADY_READY: existing GCL tunnel; no duplicate launched'
  exit 0
fi

if [[ -f "$STATE/tunnel-supervisor.lock" ]]; then
  if ! flock -n "$STATE/tunnel-supervisor.lock" -c true >/dev/null 2>&1; then
    echo 'BLOCKED: supervisor lock held while tunnel not ready; no duplicate launch'
    exit 3
  fi
fi

# setsid -f double-detaches from the WSL invocation process group. Redirect
# all file descriptors; the existing supervisor writes its own private log.
# nohup avoids SIGHUP from loss of the Windows launch console.
nohup setsid -f /bin/bash "$SUP" </dev/null >/dev/null 2>&1 &
wait "$!" || {
  echo 'BLOCKED: Linux detach command exited unsuccessfully'
  exit 3
}
for attempt in 1 2 3 4 5 6 7 8 9 10 11 12; do
  if ready; then
    printf 'LINUX_DETACH_READY: 200 (attempt %s)\n' "$attempt"
    echo 'WINDOWS_LAUNCH_RETURN_PENDING: verify readiness from a new Windows WSL call'
    exit 0
  fi
  sleep 1
done
if [[ -f "$LOG" ]]; then
  echo 'BLOCKED: detached supervisor did not reach readiness; private log retained on CHAD'
else
  echo 'BLOCKED: detached supervisor did not reach readiness before log creation'
fi
exit 3
