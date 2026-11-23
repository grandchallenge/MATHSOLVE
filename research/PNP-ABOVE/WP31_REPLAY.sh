#!/usr/bin/env bash
# Exact original upstream WP08–WP31 uncached source replay and axiom audit.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP31_REPLAY.sh PINNED_UPSTREAM GCL_HEAD REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || { echo WP31_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor 290d2fd2bb5861aaa9155a1549aee4f72946862f HEAD || { echo WP31_PROTECTED_PARENT_DRIFT >&2; exit 65; }
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || { echo WP31_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65; }
export PNP_REPLAY_ADMISSION=1
bash "$src/WP30_REPLAY.sh" "$upstream" "$gcl" "$work" || { echo WP31_PREDECESSOR_FULL_UNCACHED_REPLAY_FAILED >&2; exit 1; }
cp "$src/WP31_SOURCE_LOCK.json" "$work/WP31_SOURCE_LOCK.json"
python3 "$src/WP31_SOURCE_GUARD.py" "$src/WP31_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP31_PARENT=290d2fd2bb5861aaa9155a1549aee4f72946862f\nWP31_CANDIDATE=%s\n' "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP31Counting
LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/WP31Counting.olean" "$work/PNPAbove/WP31Counting.lean" > "$work/WP31Counting.log" 2>&1 || { echo WP31_ORIGINAL_KERNEL_SOURCE_FAILED >&2; tail -110 "$work/WP31Counting.log" >&2; exit 1; }
python3 "$src/WP31_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP31_LOSSLESS_INDEX_COUNTING_EXPONENTIAL_BARRIER_PROVED__SEMANTIC_SAT_LABEL_COMPUTABILITY_AND_CLASSICAL_LOWER_BOUND_OPEN\n' | tee "$work/status.txt"
