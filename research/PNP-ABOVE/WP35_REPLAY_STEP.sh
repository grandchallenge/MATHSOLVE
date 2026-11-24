#!/usr/bin/env bash
# Append WP35 to the same fresh uncached WP34 replay, with exact predecessor-source continuity.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP35_REPLAY_STEP.sh PINNED_UPSTREAM GCL_HEAD COMPLETED_FRESH_WP34_REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$(cd "$3" && pwd -P)
src="$gcl/research/PNP-ABOVE"
base=be2056e4404c9293b3cf406bd0139d0afb0af874
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970
git -C "$gcl" merge-base --is-ancestor "$base" HEAD
prior=$(sed -n 's/^WP34_CANDIDATE=//p' "$work/lock.txt")
test -n "$prior"
git -C "$gcl" merge-base --is-ancestor "$prior" HEAD
git -C "$gcl" diff --exit-code "$base" HEAD -- research/PNP-ABOVE ':!research/PNP-ABOVE/WP35*'
git -C "$gcl" diff --exit-code "$prior" HEAD -- research/PNP-ABOVE ':!research/PNP-ABOVE/WP35*'
test "$(cat "$work/status.txt")" = WP34_CANONICAL_SCOPE_AND_NATIVE_BUDGET_CLOSED__VALID_PROMISE_POLYTIME_EQUIVALENT_TO_FORMULA_SAT__LOWER_BOUND_OPEN
test -f "$work/WP34_AxiomAudit.log"
test "$(find "$work/PNPAbove" -name '*.olean' | wc -l)" -eq 94
test ! -e "$work/PNPAbove/WP35Dense.olean"
test ! -e "$work/PNPAbove/WP35Dense.lean"
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0
export PNP_REPLAY_ADMISSION=1
cp "$work/status.txt" "$work/WP34_FRESH_STATUS.txt"
sha256sum "$work/WP34_FRESH_STATUS.txt" "$work/WP34_AxiomAudit.log" >> "$work/lock.txt"
cp "$src/WP35_SOURCE_LOCK.json" "$work/WP35_SOURCE_LOCK.json"
python3 "$src/WP35_SOURCE_GUARD.py" "$src/WP35_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP35_PREDECESSOR_CANDIDATE=%s\nWP35_CANDIDATE=%s\nWP35_FRESH_PREDECESSOR_REPLAY=%s\n' "$base" "$(git -C "$gcl" rev-parse HEAD)" "$prior" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP35Dense
LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/WP35Dense.olean" "$work/PNPAbove/WP35Dense.lean" > "$work/WP35Dense.log" 2>&1 || { tail -100 "$work/WP35Dense.log" >&2; exit 1; }
python3 "$src/WP35_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP35_DENSE_SUPPORT_AND_SHORT_WITNESS_CLOSED__NATIVE_CLASSICAL_TRANSFER_CLOSED__LOWER_BOUND_OPEN\n' | tee "$work/status.txt"
