#!/usr/bin/env bash
# Original pinned source FULL UN-CACHED replay WP08–WP28C, exact head.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP28C_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
 echo WP28C_PINNED_UPSTREAM_DRIFT >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602 HEAD || {
 echo WP28C_PROTECTED_WP28B2_PARENT_DRIFT >&2; exit 65;
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
 echo WP28C_CACHE_ADMISSION_FORBIDDEN >&2; exit 65;
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP28B2_REPLAY.sh" "$upstream" "$gcl" "$work" || {
 echo WP28C_PREDECESSOR_FULL_UNCACHED_REPLAY_FAILED >&2; exit 1;
}
cp "$src/WP28C_SOURCE_LOCK.json" "$work/WP28C_SOURCE_LOCK.json"
python3 "$src/WP28C_SOURCE_GUARD.py" "$src/WP28C_SOURCE_LOCK.json" \
 "$src" "$work/PNPAbove"
printf 'WP28C_PARENT=%s\nWP28C_CANDIDATE=%s\n' \
 b0e9acce5cffa8aeff5e7a6fd9e7f20970ea9602 \
 "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
LAKE_NUM_THREADS=1 lake build MIPRE.Foundations.SAT.Rename \
 > "$work/WP28C_original_imports.log" 2>&1 || {
 echo WP28C_ORIGINAL_RENAME_BUILD_FAILED >&2
 tail -110 "$work/WP28C_original_imports.log" >&2
 exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP28CPower WP28CVerifier WP28CCompression; do
 echo "CHECKING_ORIGINAL_SOURCE_$mod"
 LEAN_NUM_THREADS=1 lake env lean -R "$work" \
  -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
  > "$work/$mod.log" 2>&1 || {
    echo "WP28C_ORIGINAL_KERNEL_COMPILE_FAILED_$mod" >&2
    tail -130 "$work/$mod.log" >&2
    exit 1
  }
done
python3 "$src/WP28C_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP28C_NATIVE_2POWK_COMPRESSOR_SOURCE_PROMISES_PROVED__SAT_POLYLENGTH_FULL_GAME_OPEN\n' | tee "$work/status.txt"
