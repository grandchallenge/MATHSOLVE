#!/usr/bin/env bash
# Original MIPRE WP08–WP20 source-locked 44-module replay. Fail closed.
# Usage: bash WP20_REPLAY.sh PINNED_UPSTREAM_GIT CANDIDATE_GIT REPLAY_DIR
set -euo pipefail
if (( $# != 3 )); then
  echo "USAGE: $0 PINNED_UPSTREAM_GIT CANDIDATE_GIT REPLAY_DIR" >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
upstream_sha=5926bdff5db621f44682a101007ef2fe3ae8d970
wp19_sha=0780909e5a31c8fb7ff882a25b1ccad5bf31dd51
test "$(git -C "$upstream" rev-parse HEAD)" = "$upstream_sha" ||
  { echo WP20_UPSTREAM_ORIGINAL_SOURCE_DRIFT >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor "$wp19_sha" HEAD ||
  { echo WP20_WP19_ADMITTED_PARENT_DRIFT >&2; exit 65; }
# Recompile all 27 predecessor source-native modules under their own locks,
# verifying original WP08–WP19 SHA256 and Git blob and standard axioms.
bash "$src/WP19_REPLAY.sh" "$upstream" "$gcl" "$work" ||
  { echo WP20_PREDECESSOR_NATIVE_REPLAY_FAILED >&2; exit 1; }
cp "$src/WP20_SOURCE_LOCK.json" "$work/WP20_SOURCE_LOCK.json"
python3 "$src/WP20_SOURCE_GUARD.py" "$src/WP20_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
sha256sum "$work"/PNPAbove/WP20*.lean >> "$work/lock.txt"
printf "WP20_ADMITTED_PARENT=%s\nWP20_CANDIDATE=%s\n" "$wp19_sha"   "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
base_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work:$base_path"
for mod in WP20Cycle WP20Law WP20Parity WP20Quantum WP20Decomp     WP20Expectation WP20Aggregation WP20QuantumGlobal WP20BellGap     WP20SourceProg WP20SourceSemantics WP20CLSem WP20SourceQueries     WP20BitEquiv WP20Native WP20Bounded WP20ClassicalExact; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work"     -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean"     >"$work/$mod.log" 2>&1 ||
    { echo "WP20_SOURCE_COMPILE_FAILED $mod" >&2; tail -n 100 "$work/$mod.log" >&2; exit 1; }
done
python3 "$src/WP20_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP20_EXACT_NATIVE_CYCLIC_SAMPLER_SOURCE_GAME_POSITIVE_BELL_GAP_PASS\n' |
  tee "$work/status.txt"
