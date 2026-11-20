#!/usr/bin/env bash
# Mandatory UN-CACHED original MIPRE source replay WP08–WP25.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP25_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP25_ORIGINAL_UPSTREAM_DRIFT >&2
  exit 65
}
git -C "$gcl" merge-base --is-ancestor af675f4862d2f2822d6fe669ab043be438dff4ed HEAD || {
  echo WP25_PROTECTED_WP24_PARENT_DRIFT >&2
  exit 65
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP25_CACHED_ADMISSION_FORBIDDEN >&2
  exit 65
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP24_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP25_FULL_PREDECESSOR_UNCACHED_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP25_SOURCE_LOCK.json" "$work/WP25_SOURCE_LOCK.json"
python3 "$src/WP25_SOURCE_GUARD.py" \
  "$src/WP25_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP25_PARENT=%s\nWP25_CANDIDATE=%s\n' \
  af675f4862d2f2822d6fe669ab043be438dff4ed \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
lake build MIPRE.Foundations.SAT.ArrayProg MIPRE.Foundations.SAT.FmlProg \
  > "$work/OriginalSATSourceEvaluator_import_build.log" 2>&1 || {
    echo WP25_PINNED_SOURCE_EVALUATOR_IMPORT_BUILD_FAILED >&2
    tail -100 "$work/OriginalSATSourceEvaluator_import_build.log" >&2
    exit 1
  }
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP25SourceEvaluator
LEAN_NUM_THREADS=1 lake env lean -R "$work" \
  -o "$work/PNPAbove/WP25SourceEvaluator.olean" \
  "$work/PNPAbove/WP25SourceEvaluator.lean" \
  > "$work/WP25SourceEvaluator.log" 2>&1 || {
    echo WP25_ORIGINAL_LEAN_KERNEL_SOURCE_FAILED >&2
    tail -120 "$work/WP25SourceEvaluator.log" >&2
    exit 1
  }
python3 "$src/WP25_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP25_ORIGINAL_COST_PROG_POLYTIME_SAT_ANSWER_CHECKER_PROVED__VERIFIER7_AND_HARDNESS_OPEN\n' | tee "$work/status.txt"
