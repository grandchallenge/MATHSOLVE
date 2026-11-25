#!/usr/bin/env bash
# Replay exact original MIPRE WP08-WP21 sources and audit standard kernel axioms.
set -euo pipefail
if (( $# != 3 )); then
  echo "USAGE: WP21_REPLAY.sh PINNED_UPSTREAM_GIT CANDIDATE_GIT REPLAY_DIR" >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP21_UPSTREAM_SOURCE_DRIFT >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor ab30e727a6bf6762432d4b95546908f8c4d3711a HEAD || {
  echo WP21_ADMITTED_PARENT_DRIFT >&2; exit 65;
}
bash "$src/WP20_REPLAY.sh" "$upstream" "$gcl" "$work"
cp "$src/WP21_SOURCE_LOCK.json" "$work/WP21_SOURCE_LOCK.json"
python3 "$src/WP21_SOURCE_GUARD.py" "$src/WP21_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP21_ADMITTED_PARENT=%s\nWP21_CANDIDATE=%s\n'     ab30e727a6bf6762432d4b95546908f8c4d3711a     "$(git -C "$gcl" rev-parse HEAD)" >>"$work/lock.txt"
cd "$upstream"
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP21Masked WP21Prog WP21Safety WP21Total WP21Length            WP21Verifier WP21Checks WP21Runtime WP21Time WP21Bounded; do
  echo CHECKING_ORIGINAL_SOURCE_"$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" -o "$work/PNPAbove/$mod.olean"     "$work/PNPAbove/$mod.lean" >"$work/$mod.log" 2>&1 || {
      echo WP21_SOURCE_COMPILE_FAILED_"$mod" >&2
      tail -100 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP21_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP21_NATIVE_BOUNDED_ANSWER_SENSITIVE_VERIFIER_SOURCE_PASS\n' | tee "$work/status.txt"
