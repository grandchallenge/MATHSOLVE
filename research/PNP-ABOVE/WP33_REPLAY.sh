#!/usr/bin/env bash
# Exact original upstream WP08–WP33 uncached source replay and axiom audit.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP33_REPLAY.sh PINNED_UPSTREAM GCL_HEAD REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || { echo WP33_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor 46ec251d240066ea2abef652a35c42a8069953f4 HEAD || { echo WP33_PROTECTED_PARENT_DRIFT >&2; exit 65; }
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || { echo WP33_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65; }
export PNP_REPLAY_ADMISSION=1
bash "$src/WP32_REPLAY.sh" "$upstream" "$gcl" "$work" || { echo WP33_PREDECESSOR_FULL_UNCACHED_REPLAY_FAILED >&2; exit 1; }
cp "$src/WP33_SOURCE_LOCK.json" "$work/WP33_SOURCE_LOCK.json"
python3 "$src/WP33_SOURCE_GUARD.py" "$src/WP33_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP33_PARENT=46ec251d240066ea2abef652a35c42a8069953f4\nWP33_CANDIDATE=%s\n' "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP33Budget
LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/WP33Budget.olean" "$work/PNPAbove/WP33Budget.lean" > "$work/WP33Budget.log" 2>&1 || { echo WP33_ORIGINAL_KERNEL_SOURCE_FAILED >&2; tail -110 "$work/WP33Budget.log" >&2; exit 1; }
python3 "$src/WP33_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP33_UNIFORM_VARIABLE_BUDGET_FALSE_FOR_NATIVE_NONEMPTY_SAT_INPUTS__NORMALIZATION_AND_CLASSICAL_LOWER_BOUND_OPEN\n' | tee "$work/status.txt"
