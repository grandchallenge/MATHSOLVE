#!/usr/bin/env bash
# Native original MIPRE WP08-WP19 all-dependency source replay, fail-closed.
# bash WP19_REPLAY.sh PINNED_UPSTREAM_GIT GCL_CANDIDATE_GIT WORK_DIR
set -euo pipefail
if (( $# != 3 )); then
  echo "USAGE: $0 PINNED_UPSTREAM GCL_CANDIDATE WORK_DIR" >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
expected_upstream=5926bdff5db621f44682a101007ef2fe3ae8d970
protected_parent=21f3e9edb946ae2ab4f4a312663f1e5559214a6b
source_wp18=760d30d74672309ae58f015b0f511c062f431e08
test "$(git -C "$upstream" rev-parse HEAD)" = "$expected_upstream" ||
  { echo "WP19_ORIGINAL_UPSTREAM_LOCK_DRIFT" >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor "$protected_parent" HEAD ||
  { echo "WP19_PROTECTED_PARENT_DRIFT" >&2; exit 65; }
git -C "$gcl" merge-base --is-ancestor "$source_wp18" HEAD ||
  { echo "WP19_WP18_SOURCE_ANCESTRY_DRIFT" >&2; exit 65; }

# First reconstruct WP08 through WP18 using their *own* original fully
# source-locked 19-module replay, including every original WP08-WP17
# protected blob, all nine WP18 blobs, original Lean and its axiom audit.
bash "$src/WP18_REPLAY.sh" "$upstream" "$gcl" "$work" ||
  { echo "WP19_PREDECESSOR_NATIVE_REPLAY_FAILED" >&2; exit 1; }
python3 "$src/WP19_SOURCE_GUARD.py" "$src/WP19_SOURCE_LOCK.json"   "$src" "$work/PNPAbove"
sha256sum "$work"/PNPAbove/WP19*.lean >> "$work/lock.txt"
printf "WP19_PROTECTED_PARENT=%s\nWP19_SOURCE_WP18=%s\nWP19_CANDIDATE=%s\n"   "$protected_parent" "$source_wp18" "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
base_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work:$base_path"
for mod in WP19Support WP19Law WP19Choice WP19Scalar     WP19Envelope WP19Global WP19Strategies WP19Native; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work"     -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean"     >"$work/$mod.log" 2>&1 ||
    { echo "WP19_SOURCE_COMPILE_FAILED $mod" >&2; tail -n 100 "$work/$mod.log" >&2; exit 1; }
done
python3 "$src/WP19_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP19_UNIVERSAL_STAR_SUPPORT_SOURCE_NATIVE_NO_GAP_PASS\n' |
  tee "$work/status.txt"
