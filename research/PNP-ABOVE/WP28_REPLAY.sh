#!/usr/bin/env bash
# Exact original-source UNCACHED Lean replay WP08–WP28A.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP28_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP28_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor 6182a58097b759119767dc78255e0c38d9f21e03 HEAD || {
  echo WP28_PROTECTED_PARENT_DRIFT >&2; exit 65;
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP28_CACHE_REUSE_FOR_ADMISSION_FORBIDDEN >&2; exit 65;
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP27_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP28_FULL_UNCACHED_ORIGINAL_PREDECESSOR_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP28_SOURCE_LOCK.json" "$work/WP28_SOURCE_LOCK.json"
python3 "$src/WP28_SOURCE_GUARD.py" "$src/WP28_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP28_PARENT=%s\nWP28_CANDIDATE=%s\n' \
  6182a58097b759119767dc78255e0c38d9f21e03 \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
lake build MIPRE.Foundations.SAT.FmlProg > "$work/WP28_original_sat_source_import.log" 2>&1 || {
  echo WP28_PINNED_ORIGINAL_SAT_SOURCE_IMPORT_FAILED >&2
  tail -100 "$work/WP28_original_sat_source_import.log" >&2
  exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
echo CHECKING_ORIGINAL_SOURCE_WP28UniformExponentObstruction
LEAN_NUM_THREADS=1 lake env lean -R "$work" \
  -o "$work/PNPAbove/WP28UniformExponentObstruction.olean" \
  "$work/PNPAbove/WP28UniformExponentObstruction.lean" \
  > "$work/WP28UniformExponentObstruction.log" 2>&1 || {
    echo WP28_ORIGINAL_LEAN_KERNEL_SOURCE_FAILED >&2
    tail -120 "$work/WP28UniformExponentObstruction.log" >&2
    exit 1
  }
python3 "$src/WP28_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP28_HARDCODED_NATIVE_VERIFIER7_HAS_NO_UNIFORM_ISBOUNDED_LAMBDA__ALTERNATIVE_VARIABLE_INPUT_COMPILER_OPEN\n' | tee "$work/status.txt"
