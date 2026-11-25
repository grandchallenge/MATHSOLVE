#!/usr/bin/env bash
# Exact uncached original MIPRE source replay through WP24.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP24_REPLAY.sh PINNED_UPSTREAM_GIT EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP24_PINNED_UPSTREAM_DRIFT >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor 442cef7f7b5c18afffa132ae5eba01087ba7cdea HEAD || {
  echo WP24_PROTECTED_PREDECESSOR_DRIFT >&2; exit 65;
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP24_CACHE_SHORTCUT_FORBIDDEN >&2; exit 65;
}
# This is the full required 70-module original source rebuild, not a cache lookup.
export PNP_REPLAY_ADMISSION=1
bash "$src/WP23B_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP24_PREDECESSOR_FULL_SOURCE_REPLAY_FAILED >&2; exit 1;
}
cp "$src/WP24_SOURCE_LOCK.json" "$work/WP24_SOURCE_LOCK.json"
python3 "$src/WP24_SOURCE_GUARD.py" "$src/WP24_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP24_PARENT=%s\nWP24_CANDIDATE=%s\n' \
  442cef7f7b5c18afffa132ae5eba01087ba7cdea \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
lake build MIPRE.Foundations.SAT.Flatten > "$work/OriginalSATFlatten_build.log" 2>&1 || {
  echo WP24_PINNED_SAT_COMPILER_BUILD_FAILED >&2
  tail -100 "$work/OriginalSATFlatten_build.log" >&2
  exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP24SATGame WP24CNF WP24Examples; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
      echo "WP24_KERNEL_SOURCE_COMPILE_FAILED_$mod" >&2
      tail -110 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP24_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP24_SAT_SOURCE_GAME_PCC_AND_QUANTUM_PROMISE_PROVED__VERIFIER7_SOURCE_COMPILER_OPEN\n' | tee "$work/status.txt"
