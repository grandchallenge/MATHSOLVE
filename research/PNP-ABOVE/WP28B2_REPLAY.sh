#!/usr/bin/env bash
# Original pinned source replay, FULL UNCACHED predecessor chain WP08–WP28B2.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP28B2_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP28B2_PINNED_ORIGINAL_UPSTREAM_DRIFT >&2; exit 65
}
git -C "$gcl" merge-base --is-ancestor d41eb5f2af9856080fa10a7a093d1ea5d0672e08 HEAD || {
  echo WP28B2_PROTECTED_ADMISSION_PARENT_DRIFT >&2; exit 65
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP28B2_ADMISSION_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP28B_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP28B2_FULL_UNCACHED_PREDECESSOR_REPLAY_FAILED >&2; exit 1
}
cp "$src/WP28B2_SOURCE_LOCK.json" "$work/WP28B2_SOURCE_LOCK.json"
python3 "$src/WP28B2_SOURCE_GUARD.py" \
  "$src/WP28B2_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP28B2_PARENT=%s\nWP28B2_CANDIDATE=%s\n' \
  d41eb5f2af9856080fa10a7a093d1ea5d0672e08 \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
LAKE_NUM_THREADS=1 lake build \
  MIPRE.Foundations.Halting.WrapperCost \
  MIPRE.Foundations.CL.DetypingProgParse MIPRE.Foundations.SAT.Rename \
  MIPRE.Foundations.OracularDecider \
  > "$work/WP28B2_original_dependencies.log" 2>&1 || {
    echo WP28B2_ORIGINAL_IMPORT_BUILD_FAILED >&2
    tail -120 "$work/WP28B2_original_dependencies.log" >&2
    exit 1
  }
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for module in WP28B2NodeReader WP28B2Evaluator WP28B2Raw WP28B2Value; do
  echo "CHECKING_ORIGINAL_SOURCE_$module"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$module.olean" "$work/PNPAbove/$module.lean" \
    > "$work/$module.log" 2>&1 || {
      echo "WP28B2_ORIGINAL_LEAN_KERNEL_FAILED_$module" >&2
      tail -150 "$work/$module.log" >&2
      exit 1
    }
done
python3 "$src/WP28B2_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP28B2_FIXED_CODE_UNIFORM_LAMBDA_SOURCE_NATIVE_VERIFIER7_SAT_01_PROMISE_PROVED__CLASSICAL_POLYLENGTH_AND_2POWK_COMPRESSION_OPEN\n' | tee "$work/status.txt"
