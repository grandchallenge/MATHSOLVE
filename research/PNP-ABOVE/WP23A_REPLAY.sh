#!/usr/bin/env bash
# Original exact MIPRE WP08-WP23A source and axiom replay.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP23A_REPLAY.sh PINNED_UPSTREAM_GIT CANDIDATE_GIT REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP23A_ORIGINAL_SOURCE_DRIFT >&2
  exit 65
}
git -C "$gcl" merge-base --is-ancestor 38e37a53596762757798c75729aaedfef3af1d1f HEAD || {
  echo WP23A_PROTECTED_PARENT_DRIFT >&2
  exit 65
}
bash "$src/WP22_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP23A_INHERITED_SOURCE_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP23A_SOURCE_LOCK.json" "$work/WP23A_SOURCE_LOCK.json"
python3 "$src/WP23A_SOURCE_GUARD.py" "$src/WP23A_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP23A_PARENT=%s\nWP23A_CANDIDATE=%s\n' \
  38e37a53596762757798c75729aaedfef3af1d1f \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP23NativeConst WP23Probe; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
    echo "WP23A_SOURCE_COMPILE_FAILED_$mod" >&2
    tail -100 "$work/$mod.log" >&2
    exit 1
  }
done
python3 "$src/WP23A_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP23A_FIXED_GAME_INVARIANCE_AND_NO_COMPRESSION_SOUNDNESS_PREMISE_PROVED\n' | tee "$work/status.txt"
