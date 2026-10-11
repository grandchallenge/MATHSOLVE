#!/usr/bin/env bash
# Install the OFFICIAL OpenAI tunnel-client release on WSL with archive SHA-256 verification.
# Run as `bash ...`, never source it. No sudo, no tokens, no Project writes.
if [[ "${BASH_SOURCE[0]}" != "$0" ]]; then
  printf 'Do not source this installer. Use bash as a child process.\n' >&2
  return 0
fi
set -euo pipefail

command -v gh >/dev/null || { echo 'BLOCKED: gh CLI missing' >&2; exit 2; }
command -v unzip >/dev/null || { echo 'BLOCKED: unzip missing' >&2; exit 2; }
command -v sha256sum >/dev/null || { echo 'BLOCKED: sha256sum missing' >&2; exit 2; }
arch="$(uname -m)"
case "$arch" in
  x86_64) platform=linux-amd64 ;;
  aarch64) platform=linux-arm64 ;;
  *) printf 'BLOCKED: unsupported platform: %s\n' "$arch" >&2; exit 2 ;;
esac
if [[ "$(uname -s)" != Linux ]]; then
  echo 'BLOCKED: run this installer inside CHAD WSL Linux' >&2; exit 2
fi

# Discover the latest release through GitHub's authenticated metadata; do not hardcode a stale release.
release="$(gh api repos/openai/tunnel-client/releases/latest --jq '.tag_name')"
[[ "$release" =~ ^v[0-9]+\.[0-9]+\.[0-9]+$ ]] || { echo 'BLOCKED: invalid release tag' >&2; exit 2; }
archive="tunnel-client-${release}-${platform}.zip"
# Compare with official asset names before downloading to catch release-layout drift.
assets="$(gh api repos/openai/tunnel-client/releases/latest --jq '.assets[].name')"
grep -Fxq "$archive" <<< "$assets" || {
  echo "BLOCKED: official release does not contain $archive" >&2; exit 2;
}
grep -Fxq 'SHA256SUMS.txt' <<< "$assets" || {
  echo 'BLOCKED: official checksum manifest is missing' >&2; exit 2;
}

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
( cd "$tmp" && gh release download "$release" --repo openai/tunnel-client --pattern "$archive" --pattern SHA256SUMS.txt )
checksum="$(awk -v name="$archive" '$2==name || $2=="*"name {print $1}' "$tmp/SHA256SUMS.txt")"
[[ "$checksum" =~ ^[0-9a-fA-F]{64}$ ]] || { echo 'BLOCKED: release checksum not unique/valid' >&2; exit 2; }
printf '%s  %s\n' "$checksum" "$tmp/$archive" | sha256sum -c -

# Extract ONLY the single tunnel-client executable, never arbitrary archive paths.
mapfile -t entries < <(unzip -Z1 "$tmp/$archive")
executable=''
for entry in "${entries[@]}"; do
  case "$entry" in
    tunnel-client|*/tunnel-client)
      [[ -z "$executable" ]] || { echo 'BLOCKED: ambiguous executable' >&2; exit 2; }
      executable="$entry"
      ;;
  esac
done
[[ -n "$executable" ]] || { echo 'BLOCKED: tunnel-client executable missing' >&2; exit 2; }
mkdir -p "$HOME/.local/bin" "$HOME/.local/share/gcl-commander/tunnel-releases"
binary="$HOME/.local/share/gcl-commander/tunnel-releases/tunnel-client-${release}-${platform}"
unzip -p "$tmp/$archive" "$executable" > "$tmp/tunnel-client"
chmod 0755 "$tmp/tunnel-client"
"$tmp/tunnel-client" --version
# Never silently replace an existing binary unless it is precisely identical.
if [[ -e "$binary" ]] && ! cmp -s "$binary" "$tmp/tunnel-client"; then
  echo "BLOCKED: immutable release binary collision at $binary" >&2; exit 2;
fi
if [[ ! -e "$binary" ]]; then
  install -m 0755 "$tmp/tunnel-client" "$binary"
fi
link="$HOME/.local/bin/tunnel-client"
if [[ -e "$link" || -L "$link" ]]; then
  if [[ -L "$link" && "$(readlink "$link")" == "$binary" ]]; then
    : # idempotent reinstall of this exact verified release
  else
    backup="$link.backup-$(date -u +%Y%m%dT%H%M%SZ)-$$"
    mv -- "$link" "$backup"
    echo "Preserved previous tunnel-client executable at $backup"
  fi
fi
ln -sfn "$binary" "$link"
# Durable non-secret provenance manifest.
printf '%s\n' "release=$release" "archive_sha256=$checksum" "platform=$platform" > "$HOME/.local/share/gcl-commander/tunnel-releases/ACTIVE.txt"
echo "PASS: verified official OpenAI tunnel-client $release installed: $binary"
echo 'NEXT: provision a Platform tunnel_id and a runtime API key; never paste keys into ChatGPT.'
