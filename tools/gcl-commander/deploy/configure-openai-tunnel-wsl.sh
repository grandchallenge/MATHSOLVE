#!/usr/bin/env bash
# Interactive, bounded local configuration of Secure MCP Tunnel for GCL Commander.
# Uses tunnel-client's official profile generator; keeps the runtime key out of command history.
# Does not run arbitrary shell commands from the MCP server and keeps Project writes disabled.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  printf 'Do not source this configurator. Use bash as a child process.\n' >&2
  return 0
fi
set -euo pipefail

cmd="$HOME/gcl-commander/.venv/bin/gcl-commander"
tunnel="$HOME/.local/bin/tunnel-client"
[[ -x "$cmd" && -x "$tunnel" ]] || { echo 'BLOCKED: install Commander and verified tunnel-client first' >&2; exit 2; }

# Read from the controlling terminal even when invoked through a safe here-doc wrapper.
# No credentials flow through stdin scripts, command arguments, or shell history.
if ! exec 3</dev/tty; then
  echo 'BLOCKED: interactive CHAD terminal required' >&2
  exit 2
fi
id="${1:-}"
if [[ -z "$id" ]]; then
  IFS= read -r -p 'Platform tunnel ID (tunnel_...): ' id <&3
fi
[[ "$id" =~ ^tunnel_[0-9a-f]{32}$ ]] || { echo 'BLOCKED: invalid tunnel ID; obtain it from Platform Tunnels' >&2; exit 2; }

config="$HOME/.config/gcl-commander"
secrets="$config/tunnel.env"
profile='gcl-commander'
profile_path="$HOME/.config/tunnel-client/profiles/${profile}.yaml"
mkdir -p "$config"
chmod 0700 "$config"
if [[ -e "$secrets" || -e "$profile_path" ]]; then
  echo 'BLOCKED: tunnel configuration already exists; inspect/reconcile instead of overwriting.' >&2
  exit 2
fi

# Key never passed as a CLI argument, printed, or recorded in shell history.
IFS= read -r -s -p 'Platform tunnel runtime API key (input hidden): ' key <&3
printf '\n'
[[ "$key" =~ ^[a-zA-Z0-9_-]{12,}$ ]] || { unset key; echo 'BLOCKED: invalid key format' >&2; exit 2; }
umask 077
# systemd EnvironmentFile escapes are avoided by strict alphanumeric/hyphen/underscore key policy.
printf 'CONTROL_PLANE_API_KEY=%s\nGCL_COMMANDER_PROJECT_WRITE=disabled\nGCL_COMMANDER_TRANSPORT=stdio\nGCL_COMMANDER_GITHUB_ACTOR=fyremael\n' "$key" > "$secrets"
unset key
chmod 0600 "$secrets"

# Verify host credentials before configuring the tunnel. Loading secrets in local subshell only.
if ! GCL_COMMANDER_GITHUB_ACTOR=fyremael "$cmd" doctor; then
  rm -f "$secrets"
  echo 'BLOCKED: Commander authenticated identity check failed; secrets file removed' >&2
  exit 2
fi
# The stdio child inherits a restrictive environment; no exposed localhost MCP listener.
if ! "$tunnel" init --sample sample_mcp_stdio_local --profile "$profile" \
  --tunnel-id "$id" --mcp-command "$cmd serve" \
  --health-listen-addr '127.0.0.1:8080'; then
  rm -f "$secrets"
  echo 'BLOCKED: tunnel profile creation failed; secrets file removed' >&2
  exit 2
fi
# Exact config location may differ with user overrides; profile discovery must succeed before activation.
echo "PASS: local Secure MCP Tunnel profile $profile configured."
echo "Private runtime environment: $secrets (0600)"
echo "NEXT: use the official tunnel-client doctor; then enable the user service if systemd is available."
echo "Do not paste runtime keys or the tunnel profile into a public issue."
