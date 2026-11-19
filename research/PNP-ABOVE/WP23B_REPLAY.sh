#!/usr/bin/env bash
# Full original imported MIPRE WP08–WP23B source replay and kernel audit.
# Development cache is NEVER used by this script.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP23B_REPLAY.sh PINNED_UPSTREAM_GIT GCL_CANDIDATE_GIT REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP23B_PINNED_ORIGINAL_SOURCE_DRIFT >&2
  exit 65
}
git -C "$gcl" merge-base --is-ancestor c6a3bb4c389baa093a4acbd644284b343e42d08c HEAD || {
  echo WP23B_PROTECTED_PARENT_DRIFT >&2
  exit 65
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP23B_FULL_REPLAY_CACHE_SHORTCUT_FORBIDDEN >&2
  exit 65
}
# Full predecessor source compilation, original axiom reports and source
# locks, no cached proof objects. This is the required protected gate.
bash "$src/WP23A_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP23B_PREDECESSOR_SOURCE_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP23B_SOURCE_LOCK.json" "$work/WP23B_SOURCE_LOCK.json"
python3 "$src/WP23B_SOURCE_GUARD.py" "$src/WP23B_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP23B_PARENT=%s\nWP23B_CANDIDATE=%s\n' \
  c6a3bb4c389baa093a4acbd644284b343e42d08c \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
lake build MIPRE.TM.CookLevin.Assemble > "$work/CookLevin_build.log" 2>&1 || {
  echo WP23B_ORIGINAL_CONSTRUCTED_COOK_LEVIN_BUILD_FAILED >&2
  tail -120 "$work/CookLevin_build.log" >&2
  exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP23BNativeCost WP23BMask WP23BSuccinctBridge WP23BCharacterization WP23BConcrete; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
      echo "WP23B_SOURCE_COMPILE_FAILED_$mod" >&2
      tail -120 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP23B_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP23B_EXACT_SOURCE_NATIVE_SUCCINCT_SAT_MASK__SAT_HARDNESS_TRANSFER_OPEN\n' | tee "$work/status.txt"
