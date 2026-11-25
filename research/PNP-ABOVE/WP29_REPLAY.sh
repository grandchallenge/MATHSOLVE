#!/usr/bin/env bash
# Original source exact-head full UN-CACHED WP08–WP29 admission replay.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP29_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP29_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor 9bdf8c4893f8eebfe551b092e1322db7a334541a HEAD || {
  echo WP29_PROTECTED_PARENT_DRIFT >&2; exit 65;
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP29_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65;
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP28C_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP29_PREDECESSOR_FULL_UNCACHED_SOURCE_REPLAY_FAILED >&2; exit 1;
}
cp "$src/WP29_SOURCE_LOCK.json" "$work/WP29_SOURCE_LOCK.json"
python3 "$src/WP29_SOURCE_GUARD.py" \
  "$src/WP29_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP29_PARENT=%s\nWP29_CANDIDATE=%s\n' \
  9bdf8c4893f8eebfe551b092e1322db7a334541a \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
LAKE_NUM_THREADS=1 lake build MIPRE.Foundations.SAT.FmlProg \
  > "$work/WP29_original_import_build.log" 2>&1 || {
    echo WP29_PINNED_FMLPROG_BUILD_FAILED >&2
    tail -110 "$work/WP29_original_import_build.log" >&2
    exit 1
  }
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP29CNF
LEAN_NUM_THREADS=1 lake env lean -R "$work" \
  -o "$work/PNPAbove/WP29CNF.olean" "$work/PNPAbove/WP29CNF.lean" \
  > "$work/WP29CNF.log" 2>&1 || {
    echo WP29_ORIGINAL_KERNEL_SOURCE_FAILED >&2
    tail -130 "$work/WP29CNF.log" >&2
    exit 1
  }
python3 "$src/WP29_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP29_EXECUTABLE_POLYNOMIAL_EXPLICIT_3CNF_TO_INDEX_SOURCE_COMPILER_PROVED__FULL_GAME_LENGTH_AND_CLASSICAL_HARDNESS_OPEN\n' | tee "$work/status.txt"
