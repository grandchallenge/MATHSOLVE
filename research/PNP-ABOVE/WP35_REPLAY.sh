#!/usr/bin/env bash
# Fresh, uncached original-source replay, including the complete predecessor chain.
set -euo pipefail
if (( $# != 3 )); then echo 'USAGE: WP35_REPLAY.sh PINNED_UPSTREAM GCL_HEAD REPLAY_DIR' >&2; exit 64; fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
src="$gcl/research/PNP-ABOVE"
test ! -e "$work/PNPAbove" || { echo WP35_FRESH_REPLAY_DIR_REQUIRED >&2; exit 65; }
bash "$src/WP34_REPLAY.sh" "$upstream" "$gcl" "$work"
bash "$src/WP35_REPLAY_STEP.sh" "$upstream" "$gcl" "$work"
