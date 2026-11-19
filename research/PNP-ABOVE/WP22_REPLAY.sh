#!/usr/bin/env bash
# Original pinned MIPRE WP08-WP22 source, native semantics and axiom replay.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP22_REPLAY.sh PINNED_UPSTREAM_GIT CANDIDATE_GIT REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP22_UPSTREAM_SOURCE_DRIFT >&2
  exit 65
}
git -C "$gcl" merge-base --is-ancestor 46d7bbc9167bb52d457e55d1b8741f7695e16576 HEAD || {
  echo WP22_PROTECTED_PARENT_DRIFT >&2
  exit 65
}
bash "$src/WP21_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP22_PREDECESSOR_EXACT_SOURCE_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP22_SOURCE_LOCK.json" "$work/WP22_SOURCE_LOCK.json"
python3 "$src/WP22_SOURCE_GUARD.py" "$src/WP22_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP22_PARENT=%s\nWP22_CANDIDATE=%s\n' \
  46d7bbc9167bb52d457e55d1b8741f7695e16576 \
  "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
# Upstream GameTransport is a proven source module, but was not required
# by WP21; ensure the pinned import is built before checking WP22.
cd "$upstream"
lake build MIPRE.Foundations.GameTransport > "$work/GameTransport_build.log" 2>&1 || {
  echo WP22_PINNED_GAMETRANSPORT_BUILD_FAILED >&2
  tail -100 "$work/GameTransport_build.log" >&2
  exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP22BitRead WP22Truth WP22Evaluator WP22Parser WP22Native \
           WP22SourceBridge WP22Classical WP22Quantum WP22Gap; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
      echo "WP22_SOURCE_COMPILE_FAILED_$mod" >&2
      tail -100 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP22_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP22_SOURCE_NATIVE_SYNCHRONOUS_EXECUTABLE_STRICT_BELL_GAP_PROVED\n' | tee "$work/status.txt"
