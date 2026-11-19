#!/usr/bin/env bash
# Development-only cached predecessors. NEVER a protected-admission replay.
# Usage: bash PNP_WARM_REPLAY.sh PINNED_UPSTREAM GCL_CANDIDATE DEV_WORK NEW_LEAN_SOURCE
set -euo pipefail
if (( $# != 4 )); then
  echo 'USAGE: PNP_WARM_REPLAY.sh PINNED_UPSTREAM GCL_CANDIDATE DEV_WORK NEW_LEAN_SOURCE' >&2
  exit 64
fi
if [[ "$(printenv PNP_REPLAY_ADMISSION 2>/dev/null || true)" == 1 ]]; then
  echo ADMISSION_MUST_USE_FULL_WP23A_REPLAY >&2
  exit 65
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
source=$4
src="$gcl/research/PNP-ABOVE"
test -f "$source" && test ! -L "$source" || { echo SOURCE_FILE_REQUIRED >&2; exit 65; }
case "$source" in
  *.lean) ;;
  *) echo LEAN_SOURCE_REQUIRED >&2; exit 65 ;;
esac
cache_root=$(printenv PNP_REPLAY_CACHE_ROOT 2>/dev/null || echo "$HOME/.cache/gcl/pnp-source-replay")
python3 "$src/PNP_REPLAY_CACHE.py" restore --upstream "$upstream" --gcl "$gcl" \
  --cache-root "$cache_root" --work "$work"
work=$(cd "$work" && pwd -P)
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo PNP_DEV_SOURCE_KERNEL_ELABORATION_START
LEAN_NUM_THREADS=1 lake env lean -R "$work" "$source"
echo PNP_DEV_SOURCE_KERNEL_ELABORATION_PASS__NOT_FULL_REPLAY
