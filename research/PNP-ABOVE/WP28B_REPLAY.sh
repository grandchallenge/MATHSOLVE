#!/usr/bin/env bash
# Original pinned MIPRE source, full UN-CACHED replay through WP28B1.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP28B_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP28B_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65
}
git -C "$gcl" merge-base --is-ancestor 3ef8c09ecb21392ecf86e23665bc1fdd0733ae73 HEAD || {
  echo WP28B_PROTECTED_PARENT_DRIFT >&2; exit 65
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP28B_PROTECTED_SOURCE_REPLAY_CACHE_FORBIDDEN >&2; exit 65
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP28_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP28B_FULL_PREDECESSOR_UNCACHED_REPLAY_FAILED >&2; exit 1
}
cp "$src/WP28B_SOURCE_LOCK.json" "$work/WP28B_SOURCE_LOCK.json"
python3 "$src/WP28B_SOURCE_GUARD.py" \
  "$src/WP28B_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP28B_PARENT=%s\nWP28B_CANDIDATE=%s\n' \
  3ef8c09ecb21392ecf86e23665bc1fdd0733ae73 \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
LAKE_NUM_THREADS=1 lake build \
  MIPRE.Foundations.Halting.Serial MIPRE.Foundations.OracularDecider \
  > "$work/WP28B_original_import_build.log" 2>&1 || {
    echo WP28B_ORIGINAL_SERIAL_AND_DECODER_IMPORT_BUILD_FAILED >&2
    tail -110 "$work/WP28B_original_import_build.log" >&2
    exit 1
  }
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP28BIndex
LEAN_NUM_THREADS=1 lake env lean -R "$work" \
  -o "$work/PNPAbove/WP28BIndex.olean" "$work/PNPAbove/WP28BIndex.lean" \
  > "$work/WP28BIndex.log" 2>&1 || {
    echo WP28B_ORIGINAL_LEAN_KERNEL_SOURCE_FAILED >&2
    tail -130 "$work/WP28BIndex.log" >&2
    exit 1
  }
python3 "$src/WP28B_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP28B_UNIFORM_BINARY_SAT_INDEX_SOURCE_ENCODER_AND_EXACT_DECODER_PROVED__FIXED_SOURCE_SAT_DECIDER_OPEN\n' | tee "$work/status.txt"
