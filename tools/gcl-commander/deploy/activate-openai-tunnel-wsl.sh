#!/usr/bin/env bash
# Runs tunnel-client doctor, optionally enables user systemd tunnel without exposing MCP HTTP.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  printf 'Do not source this script. Use bash as a child process.\n' >&2
  return 0
fi
set -euo pipefail
root="${GCL_COMMANDER_HOME:-$HOME/gcl-commander}"
secret="$HOME/.config/gcl-commander/tunnel.env"
client="$HOME/.local/bin/tunnel-client"
[[ -x "$client" && -f "$secret" ]] || { echo 'BLOCKED: tunnel-client or runtime secret missing' >&2; exit 2; }
[[ "$(stat -c '%a' "$secret")" == 600 ]] || { echo 'BLOCKED: secrets file must be mode 0600' >&2; exit 2; }
[[ "$(stat -c '%a' "$(dirname "$secret")")" == 700 ]] || { echo 'BLOCKED: secrets directory must be mode 0700' >&2; exit 2; }
# Parse the fixed EnvironmentFile contract as data, NEVER source executable shell content.
[[ "$(wc -l < "$secret")" -eq 4 ]] || { echo 'BLOCKED: unexpected runtime environment content' >&2; exit 2; }
key="$(sed -n 's/^CONTROL_PLANE_API_KEY=//p' "$secret")"
[[ "$key" =~ ^[a-zA-Z0-9_-]{12,}$ ]] || { echo 'BLOCKED: malformed tunnel runtime credential' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_PROJECT_WRITE=disabled' "$secret" || { echo 'BLOCKED: Project writes must stay disabled' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_TRANSPORT=stdio' "$secret" || { echo 'BLOCKED: stdio transport required' >&2; exit 2; }
grep -Fxq 'GCL_COMMANDER_GITHUB_ACTOR=fyremael' "$secret" || { echo 'BLOCKED: expected GitHub actor missing' >&2; exit 2; }
export CONTROL_PLANE_API_KEY="$key"
unset key
"$root/.venv/bin/gcl-commander" doctor
"$client" doctor --profile gcl-commander --explain
if [[ "$(ps -p 1 -o comm= | tr -d ' ')" != systemd ]]; then
  echo 'PASS: tunnel doctor; systemd not running in WSL. Service NOT started.'
  echo 'For foreground testing run: ~/.local/bin/tunnel-client run --profile gcl-commander'
  exit 0
fi
unit="$HOME/.config/systemd/user/gcl-commander-tunnel.service"
mkdir -p "$(dirname "$unit")"
if [[ -e "$unit" ]] && ! cmp -s "$root/deploy/gcl-commander-tunnel.service" "$unit"; then
  cp -p "$unit" "$unit.backup-$(date -u +%Y%m%dT%H%M%SZ)"
fi
install -m 0644 "$root/deploy/gcl-commander-tunnel.service" "$unit"
systemctl --user daemon-reload
systemctl --user enable --now gcl-commander-tunnel.service
systemctl --user --no-pager --full status gcl-commander-tunnel.service
printf 'Tunnel service activated. Verify healthy/ready through the client health interface; service process alone is insufficient.\n'
