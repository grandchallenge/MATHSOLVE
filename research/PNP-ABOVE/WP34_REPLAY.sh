#!/usr/bin/env bash
# Exact original upstream WP08–WP34 uncached source replay and axiom audit.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP34_REPLAY.sh PINNED_UPSTREAM GCL_HEAD REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
test ! -e "$work/PNPAbove" || { echo WP34_FRESH_REPLAY_DIR_REQUIRED >&2; exit 65; }
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || { echo WP34_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor 935a2e59d13bfb39487b166e187e38e794b913f9 HEAD || { echo WP34_PROTECTED_PARENT_DRIFT >&2; exit 65; }
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || { echo WP34_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65; }
export PNP_REPLAY_ADMISSION=1
bash "$src/WP33_REPLAY.sh" "$upstream" "$gcl" "$work" || { echo WP34_PREDECESSOR_FULL_UNCACHED_REPLAY_FAILED >&2; exit 1; }
cp "$src/WP34_SOURCE_LOCK.json" "$work/WP34_SOURCE_LOCK.json"
python3 "$src/WP34_SOURCE_GUARD.py" "$src/WP34_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP34_PARENT=935a2e59d13bfb39487b166e187e38e794b913f9\nWP34_CANDIDATE=%s\n' "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP34Scope
LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/WP34Scope.olean" "$work/PNPAbove/WP34Scope.lean" > "$work/WP34Scope.log" 2>&1 || { echo WP34_ORIGINAL_KERNEL_SOURCE_FAILED >&2; tail -110 "$work/WP34Scope.log" >&2; exit 1; }
python3 "$src/WP34_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP34_CANONICAL_SCOPE_AND_NATIVE_BUDGET_CLOSED__VALID_PROMISE_POLYTIME_EQUIVALENT_TO_FORMULA_SAT__LOWER_BOUND_OPEN\n' | tee "$work/status.txt"
