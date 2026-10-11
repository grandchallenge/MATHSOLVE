#!/usr/bin/env bash
# Publish only the audited source tree as a reviewable MATHSOLVE candidate PR.
# Does not merge, deploy GitHub Actions, alter Project fields, or publish credentials.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  echo 'BLOCKED: run source publisher as a Bash child process' >&2
  return 0
fi
set -euo pipefail
ROOT="${HOME}/gcl-commander"
[[ -f "$ROOT/gcl_commander/repositories.py" && -f "$ROOT/deploy/supervise-openai-tunnel-wsl.sh" && -f "$ROOT/deploy/gcl-chad-detached-start.sh" && -f "$ROOT/deploy/start-at-logon.ps1" ]] || {
  echo 'BLOCKED: v0.2.1 verified source missing' >&2; exit 2;
}
[[ "$(gh api user --jq .login)" == fyremael ]] || { echo 'BLOCKED: unexpected authenticated GitHub actor' >&2; exit 2; }
command -v git >/dev/null || { echo 'BLOCKED: git missing' >&2; exit 2; }
TS="$(date -u +%Y%m%dT%H%M%SZ)"
BRANCH="feat/gcl-commander-v021-${TS}"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
# Lock to exact current protected main and reject concurrent remote changes.
gh repo clone grandchallenge/MATHSOLVE "$TMP/repo" -- --quiet --depth 1 --branch main --single-branch
cd "$TMP/repo"
BASE="$(git rev-parse HEAD)"
[[ "$BASE" =~ ^[0-9a-f]{40}$ ]] || { echo 'BLOCKED: expected exact protected SHA' >&2; exit 2; }
CURRENT="$(gh api repos/grandchallenge/MATHSOLVE/commits/main --jq .sha)"
[[ "$CURRENT" == "$BASE" ]] || { echo 'BLOCKED: protected main advanced during clone' >&2; exit 2; }
git checkout -q -b "$BRANCH"
TARGET="$TMP/repo/tools/gcl-commander"
if [[ -e "$TARGET" ]]; then echo 'BLOCKED: destination already exists' >&2; exit 2; fi
mkdir -p "$TARGET/gcl_commander" "$TARGET/tests" "$TARGET/deploy"
cp "$ROOT/pyproject.toml" "$ROOT/README.md" "$TARGET/"
cp "$ROOT"/gcl_commander/*.py "$TARGET/gcl_commander/"
cp "$ROOT"/tests/test_*.py "$TARGET/tests/"
cp "$ROOT"/deploy/*.sh "$ROOT"/deploy/*.ps1 "$ROOT"/deploy/*.service "$TARGET/deploy/"
# Confirm the full source tree contains no key values or runtime credentials.
if grep -RInE 'sk-proj-[a-zA-Z0-9_-]{25,}|sk-admin-[a-zA-Z0-9_-]{25,}' "$TARGET"; then
  echo 'BLOCKED: apparent credential material in source PR' >&2; exit 2;
fi
PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="$TARGET" "$ROOT/.venv/bin/python" -m pytest -q "$TARGET/tests"
# If the branch is retried after a previous push, do not overwrite.
git add -- tools/gcl-commander
if git diff --cached --quiet; then echo 'BLOCKED: no source changes to publish' >&2; exit 2; fi
LOGIN="$(gh api user --jq .login)"; ID="$(gh api user --jq .id)"
git -c user.name="$LOGIN" -c user.email="${ID}+${LOGIN}@users.noreply.github.com" commit -q -m 'feat(gcl-commander): guarded WSL autostart and exact-head repository read tools'
git push -q origin "HEAD:refs/heads/$BRANCH"
gh pr create --repo grandchallenge/MATHSOLVE --base main --head "$BRANCH" --draft \
  --title 'GCL Commander v0.2.1: proven Linux-detached CHAD startup and governed repository readback' \
  --body "Candidate source admission. Exact protected base: $BASE. Local tests passed. Preserves the CHAD-proven synchronous Windows-to-WSL Linux-detached startup, adds a read-only authenticated Project view readback and bounded repository head/file/PR inspection. No general shell tool, no protected merge, no Project writes, no repository writes from MCP. Separate capacity and worker lifecycle acceptance remains on #1049. Review security boundaries and fresh head CI before admission."
echo 'DRAFT SOURCE PR CREATED; protected main unchanged.'
