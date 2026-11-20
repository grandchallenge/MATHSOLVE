#!/usr/bin/env bash
# Original MIPRE WP08–WP26 full UNCACHED source and Lean kernel axiom replay.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP26_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP26_ORIGINAL_PINNED_UPSTREAM_DRIFT >&2
  exit 65
}
git -C "$gcl" merge-base --is-ancestor df62dc3de0a585ff490f4e56abf5d1c76cb6f12e HEAD || {
  echo WP26_PROTECTED_PREDECESSOR_DRIFT >&2
  exit 65
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP26_CACHE_BYPASS_FORBIDDEN >&2
  exit 65
}
export PNP_REPLAY_ADMISSION=1
# Mandatory full source recompilation of 74 original predecessor modules.
bash "$src/WP25_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP26_FULL_PREDECESSOR_UNCACHED_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP26_SOURCE_LOCK.json" "$work/WP26_SOURCE_LOCK.json"
python3 "$src/WP26_SOURCE_GUARD.py" \
  "$src/WP26_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP26_PARENT=%s\nWP26_CANDIDATE=%s\n' \
  df62dc3de0a585ff490f4e56abf5d1c76cb6f12e \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
# Original pinned source imports are independently built, not replaced
# by local dev cache objects.
lake build MIPRE.Foundations.Halting.WrapperCost \
  MIPRE.Foundations.Halting.Classes MIPRE.Foundations.SAT.Rename \
  > "$work/OriginalVerifierWrapperAndRename_import_build.log" 2>&1 || {
    echo WP26_ORIGINAL_VERIFIER_WRAPPER_IMPORT_BUILD_FAILED >&2
    tail -120 "$work/OriginalVerifierWrapperAndRename_import_build.log" >&2
    exit 1
  }
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP26NativeVerifier WP26UniformCompiler; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
      echo "WP26_ORIGINAL_LEAN_SOURCE_KERNEL_COMPILE_FAILED_$mod" >&2
      tail -130 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP26_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP26_UNIFORM_ORIGINAL_VERIFIER7_SOURCE_SAT_PCC_AND_COMPRESSION_PROMISES_PROVED__RAW_ISBOUNDED_OPEN\n' | tee "$work/status.txt"
