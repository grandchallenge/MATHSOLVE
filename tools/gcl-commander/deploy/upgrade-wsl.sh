#!/usr/bin/env bash
# GCL Commander v0.2.1 WSL source upgrade: local tests before writes, rollback on failure.
# Never source this script into your interactive WSL session.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  echo 'GCL Commander: source is not supported; run upgrade using bash' >&2
  return 0
fi
set -euo pipefail
ROOT="${GCL_COMMANDER_HOME:-$HOME/gcl-commander}"
ZIP="${1:-/mnt/d/Downloads/GCL-Commander-v0.2.1.zip}"
[[ -f "$ZIP" && -x "$ROOT/.venv/bin/python" && -f "$ROOT/pyproject.toml" ]] || {
  echo 'BLOCKED: archive or prior uv installation unavailable' >&2; exit 2;
}
ROOT="$(realpath "$ROOT")"
[[ "$ROOT" == "$HOME/gcl-commander" ]] || { echo 'BLOCKED: installation root unexpectedly changed' >&2; exit 2; }
export PATH="$HOME/.local/bin:$PATH"
command -v uv >/dev/null || { echo 'BLOCKED: uv not found' >&2; exit 2; }
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
unzip -q "$ZIP" -d "$TMP"
SRC="$TMP/gcl-commander"
FILES=(
  gcl_commander/core.py gcl_commander/server.py gcl_commander/cli.py
  gcl_commander/__init__.py gcl_commander/repositories.py gcl_commander/queue_views.py
  pyproject.toml README.md
  tests/test_core.py tests/test_shell_safety.py tests/test_uv_installer.py
  tests/test_tunnel_install.py tests/test_repositories.py tests/test_persistence.py tests/test_queue_views.py
  tests/test_chad_detached_startup.py tests/test_cli_readonly.py
  deploy/install-wsl.sh deploy/upgrade-wsl.sh deploy/gcl-commander.service
  deploy/install-openai-tunnel-client-wsl.sh deploy/configure-openai-tunnel-wsl.sh
  deploy/activate-openai-tunnel-wsl.sh deploy/gcl-commander-tunnel.service
  deploy/supervise-openai-tunnel-wsl.sh deploy/install-chad-autostart.ps1
  deploy/publish-source-pr-wsl.sh
  deploy/gcl-chad-detached-start.sh deploy/start-at-logon.ps1
  deploy/install-chad-detached-autostart.ps1
)
for file in "${FILES[@]}"; do
  [[ -f "$SRC/$file" ]] || { echo "BLOCKED: archive missing $file" >&2; exit 2; }
done
"$ROOT/.venv/bin/python" -c 'import sys; assert sys.version_info >= (3,11)'
(cd "$SRC" && PYTHONPATH="$SRC" "$ROOT/.venv/bin/python" -m pytest -q)
TS="$(date -u +%Y%m%dT%H%M%SZ)-$$"
BACKUP="$ROOT/.upgrade-backups/$TS"
mkdir -p "$BACKUP"
for file in "${FILES[@]}"; do
  mkdir -p "$BACKUP/$(dirname "$file")" "$ROOT/$(dirname "$file")"
  [[ ! -f "$ROOT/$file" ]] || cp -p "$ROOT/$file" "$BACKUP/$file"
done
success=0
rollback() {
  if [[ "$success" != 1 ]]; then
    echo 'Upgrade failed: restoring previous source' >&2
    for file in "${FILES[@]}"; do
      if [[ -f "$BACKUP/$file" ]]; then
        cp -p "$BACKUP/$file" "$ROOT/$file"
      else
        rm -f "$ROOT/$file"
      fi
    done
    (cd "$ROOT" && uv pip install --python .venv/bin/python -e '.[test]' >/dev/null) || true
  fi
}
trap 'rollback; rm -rf "$TMP"' EXIT
for file in "${FILES[@]}"; do
  cp -p "$SRC/$file" "$ROOT/$file"
done
(cd "$ROOT" && uv pip install --python .venv/bin/python -e '.[test]' && .venv/bin/python -m pytest -q)
GCL_COMMANDER_GITHUB_ACTOR=fyremael "$ROOT/.venv/bin/gcl-commander" doctor
success=1
printf 'UPGRADE PASS: v0.2.1 tested, old files backed up at %s\n' "$BACKUP"
printf 'NEXT: review protected repository source PR; existing CHAD HKCU startup remains unchanged.\n'
