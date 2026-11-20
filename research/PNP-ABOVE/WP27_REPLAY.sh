#!/usr/bin/env bash
# Original MIPRE exact full UNCACHED WP08-WP27 theorem/source replay.
set -euo pipefail
if (( $# != 3 )); then
  echo 'USAGE: WP27_REPLAY.sh PINNED_UPSTREAM EXACT_GCL_CANDIDATE REPLAY_DIR' >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=$3
mkdir -p "$work/PNPAbove"
work=$(cd "$work" && pwd -P)
src="$gcl/research/PNP-ABOVE"
test "$(git -C "$upstream" rev-parse HEAD)" = 5926bdff5db621f44682a101007ef2fe3ae8d970 || {
  echo WP27_UPSTREAM_PIN_DRIFT >&2; exit 65;
}
parent=$(python3 - "$src/WP27_SOURCE_LOCK.json" <<'PY'
import json,sys
print(json.load(open(sys.argv[1]))['source_protected_parent'])
PY
)
test "$(git -C "$gcl" cat-file -t "$parent")" = commit || {
  echo WP27_PROTECTED_PARENT_UNKNOWN >&2; exit 65;
}
git -C "$gcl" merge-base --is-ancestor "$parent" HEAD || {
  echo WP27_EXACT_PARENT_ANCESTRY_DRIFT >&2; exit 65;
}
test "$(printenv PNP_REPLAY_CACHE_SKIP 2>/dev/null || echo 0)" = 0 || {
  echo WP27_CACHED_PROTECTED_ADMISSION_FORBIDDEN >&2; exit 65;
}
export PNP_REPLAY_ADMISSION=1
bash "$src/WP26_REPLAY.sh" "$upstream" "$gcl" "$work" || {
  echo WP27_UNCACHED_PREDECESSOR_SOURCE_REPLAY_FAILED >&2
  exit 1
}
cp "$src/WP27_SOURCE_LOCK.json" "$work/WP27_SOURCE_LOCK.json"
python3 "$src/WP27_SOURCE_GUARD.py" \
  "$src/WP27_SOURCE_LOCK.json" "$src" "$work/PNPAbove"
printf 'WP27_PARENT=%s\nWP27_CANDIDATE=%s\n' \
  "$parent" "$(git -C "$gcl" rev-parse HEAD)" >> "$work/lock.txt"
cd "$upstream"
lake build MIPRE.Foundations.CL.DetypingProgParse \
  MIPRE.Foundations.Halting.PolyBounded MIPRE.Foundations.Cost.Growth \
  > "$work/WP27_original_raw_parser_and_cost_imports.log" 2>&1 || {
  echo WP27_ORIGINAL_SOURCE_IMPORT_BUILD_FAILED >&2
  tail -120 "$work/WP27_original_raw_parser_and_cost_imports.log" >&2
  exit 1
}
export LEAN_PATH="$work:$(lake env printenv LEAN_PATH)"
for mod in WP27RawNormalizer WP27TotalCost WP27RobustVerifier; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work" \
    -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean" \
    > "$work/$mod.log" 2>&1 || {
      echo "WP27_ORIGINAL_LEAN_KERNEL_COMPILE_FAILED_$mod" >&2
      tail -125 "$work/$mod.log" >&2
      exit 1
    }
done
python3 "$src/WP27_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP27_TOTAL_RAW_DATA_COST_NATIVE_ISBOUNDED_AND_SAT_COMPRESSION_PROMISES_PROVED__UNIFORM_LAMBDA_AND_CLASSICAL_HARDNESS_OPEN\n' | tee "$work/status.txt"
