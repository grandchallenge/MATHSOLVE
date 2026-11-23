#!/usr/bin/env bash
# Exact original upstream WP08–WP30 uncached source replay and axiom audit.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP30_REPLAY.sh PINNED_UPSTREAM GCL_HEAD REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || { echo WP30_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor 621f2866eda64f4b00d6b01145351610d0a315da HEAD || { echo WP30_PROTECTED_PARENT_DRIFT >&2; exit 65; }
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || { echo WP30_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65; }
export PNP_REPLAY_ADMISSION=1
bash "$src/WP29_REPLAY.sh" "$upstream" "$gcl" "$work" || { echo WP30_PREDECESSOR_FULL_UNCACHED_REPLAY_FAILED >&2; exit 1; }
cp "$src/WP30_SOURCE_LOCK.json" "$work/WP30_SOURCE_LOCK.json"
python3 "$src/WP30_SOURCE_GUARD.py" "$src/WP30_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP30_PARENT=621f2866eda64f4b00d6b01145351610d0a315da\nWP30_CANDIDATE=%s\n' "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP30Classical
LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/WP30Classical.olean" "$work/PNPAbove/WP30Classical.lean" > "$work/WP30Classical.log" 2>&1 || { echo WP30_ORIGINAL_KERNEL_SOURCE_FAILED >&2; tail -110 "$work/WP30Classical.log" >&2; exit 1; }
python3 "$src/WP30_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP30_COMPRESSED_CLASSICAL_SAT_TRANSFER_CONDITIONAL__NUMERIC_INDEX_AND_CLASSICAL_LOWER_BOUND_OPEN\n' | tee "$work/status.txt"
