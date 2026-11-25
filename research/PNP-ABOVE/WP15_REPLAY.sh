#!/usr/bin/env bash
# PNP-ABOVE WP15 bounded, fail-closed source-native Lean replay.
# Usage: bash WP15_REPLAY.sh PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT [WORK_DIR]
set -euo pipefail

if (( $# < 2 || $# > 3 )); then
  echo "USAGE: $0 PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT [WORK_DIR]" >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=${3:-"$PWD/wp15-replay"}
mkdir -p "$work"/PNPAbove
work=$(cd "$work" && pwd -P)

upstream_commit=5926bdff5db621f44682a101007ef2fe3ae8d970
gcl_commit=cb65e0f5386bbc42ffde5f9ea6943b8d9955e529
b08=45b9fa687fad92bf1b1d4be2809473e0c4f9957d
b09=3b64353814fd70a77810e51f2d04cbcfb4271def
b10=860ad60fca4e99fcd836eec748fa419efd0701b2

test "$(git -C "$upstream" rev-parse HEAD)" = "$upstream_commit" ||
  { echo "SOURCE_LOCK_MISMATCH upstream" >&2; exit 65; }
test "$(git -C "$gcl" merge-base "$gcl_commit" HEAD)" = "$gcl_commit" ||
  { echo "SOURCE_LOCK_MISMATCH gcl" >&2; exit 65; }

src=$gcl/research/PNP-ABOVE
for tag in 08 09 10 11 12 13 14 15; do
  case "$tag" in
    08) name=WP08_NineBitDecider.lean; expected=$b08;;
    09) name=WP09_InterpreterSoundness.lean; expected=$b09;;
    10) name=WP10_SourceAcceptanceBridge.lean; expected=$b10;;
    11) name=WP11_EvalFuelCompleteness.lean; expected=088a731db4a7a1a21097a593958706df6b8a488b;;
    12) name=WP12_TypedParserAndRawCounterexample.lean; expected=c509e7e96383c7cb8199d7a9095b915a6d4db759;;
    13) name=WP13_NineLevelSamplerVerifier.lean; expected=711e3e7938ea8c6682778252062adfc920ff4dbd;;
    14) name=WP14_ConditionalNineStageSampler.lean; expected=939f801c874e1e9acc6223a24eb055888466d51b;;
    15) name=WP15_PerfectClassicalNoGap.lean; expected=$(git -C "$gcl" rev-parse "HEAD:research/PNP-ABOVE/WP15_PerfectClassicalNoGap.lean");;
  esac
  source_path=$src/$name
  test -f "$source_path" ||
    { echo "SOURCE_MISSING $name" >&2; exit 66; }
  actual=$(git -C "$gcl" hash-object -- "$source_path")
  test "$actual" = "$expected" ||
    { echo "SOURCE_BLOB_MISMATCH $name: $actual" >&2; exit 65; }
  cp -- "$source_path" "$work/PNPAbove/WP$tag.lean"
done

test -z "$(git -C "$gcl" status --porcelain -- research/PNP-ABOVE/WP15_PerfectClassicalNoGap.lean)" || { echo UNCOMMITTED_WP15_SOURCE >&2; exit 65; }
printf 'UPSTREAM_SHA=%s\nGCL_BASE_SHA=%s\nGCL_CANDIDATE_HEAD=%s\nWP08_GIT_BLOB=%s\nWP09_GIT_BLOB=%s\n' \
  "$upstream_commit" "$gcl_commit" "$(git -C "$gcl" rev-parse HEAD)" "$b08" "$b09" > "$work/lock.txt"
sha256sum "$work"/PNPAbove/*.lean >> "$work/lock.txt"

# No hidden network download or cold rebuild: a pre-existing exact upstream
# source-native Verifier import is necessary. Missing dependencies are a separate
# compute-route obligation, not a theorem failure.
test -f "$upstream/.lake/build/lib/lean/MIPRE/Foundations/Verifier.olean" ||
  { echo "SOURCE_IMPORTS_UNBUILT: upstream Verifier .olean missing" >&2; exit 78; }
cd "$upstream"
base_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work:$base_path"
for tag in 08 09 10 11 12 13 14 15; do
  echo "CHECKING_SOURCE_NATIVE_WP$tag"
  lake env lean -R "$work" -o "$work/PNPAbove/WP$tag.olean" "$work/PNPAbove/WP$tag.lean" \
    > "$work/WP$tag.log" 2>&1 ||
    { echo "LEAN_FAIL_WP$tag" >&2; cat "$work/WP$tag.log" >&2; exit 1; }
done
# WP15 theorem axiom audit: machine-created by the pinned source, parsed below.
python3 "$src/WP15_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP15_SOURCE_NATIVE_PERFECT_CLASSICAL_NO_GAP_PASS\n' | tee "$work/status.txt"
