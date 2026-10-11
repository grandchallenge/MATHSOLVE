#!/usr/bin/env bash
# GCL Commander — uv-managed Python installer for CHAD/WSL.
# Safe to rerun. Never replaces the system Python or overwrites an unknown directory.
# Do not let accidental `source`/`.` change or terminate the caller's shell.
# Installation and upgrades must run in an isolated Bash child process.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  printf '%s\n' 'GCL Commander: source is not supported; run this script with bash in a child process.' >&2
  return 0
fi
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

command -v gh >/dev/null 2>&1 || {
  echo 'STOP: gh is missing from WSL PATH. Install/authenticate GitHub CLI first.' >&2
  exit 2
}

export PATH="$HOME/.local/bin:$PATH"
if ! command -v uv >/dev/null 2>&1; then
  command -v curl >/dev/null 2>&1 || {
    echo 'STOP: curl is required for the official uv installer.' >&2
    exit 2
  }
  echo 'Installing uv with its official standalone installer...'
  curl -LsSf https://astral.sh/uv/install.sh | sh
fi
command -v uv >/dev/null 2>&1 || {
  echo 'STOP: uv install did not produce an executable in ~/.local/bin or PATH.' >&2
  exit 2
}
uv --version

# uv manages this interpreter without changing Ubuntu/WSL's Python 3.10.
uv python install 3.12

if [[ -e .venv || -L .venv ]]; then
  [[ -d .venv && -f .venv/pyvenv.cfg && ! -L .venv ]] || {
    echo 'STOP: .venv exists but is not a regular virtual environment; inspect manually.' >&2
    exit 2
  }
  if [[ ! -x .venv/bin/python ]] || ! .venv/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12)' 2>/dev/null; then
    backup=".venv-before-uv-$(date -u +%Y%m%dT%H%M%SZ)-$$"
    echo "Preserving old/incompatible .venv at $ROOT/$backup"
    mv -- .venv "$backup"
  fi
fi

if [[ ! -d .venv ]]; then
  uv venv --managed-python --python 3.12 .venv
fi
.venv/bin/python -c 'import sys; assert sys.version_info[:2] == (3, 12), sys.version; print("GCL Commander Python:", sys.version.split()[0])'

# Install dependencies into the validated interpreter; never use system pip.
uv pip install --python .venv/bin/python -e '.[test]'
.venv/bin/python -m pytest -q
GCL_COMMANDER_GITHUB_ACTOR=fyremael .venv/bin/gcl-commander doctor
printf '\nINSTALL PRECHECK PASS — service not automatically started.\n'
printf 'Next: GCL_COMMANDER_GITHUB_ACTOR=fyremael .venv/bin/gcl-commander audit\n'
printf 'A local user service may be configured after audit and network review.\n'
