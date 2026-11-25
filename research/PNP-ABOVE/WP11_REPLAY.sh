#!/usr/bin/env bash
# PNP-ABOVE WP11 bounded, fail-closed source-native Lean replay.
# Usage: bash WP11_REPLAY.sh PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT [WORK_DIR]
set -euo pipefail

if (( $# < 2 || $# > 3 )); then
  echo "USAGE: $0 PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT [WORK_DIR]" >&2
  exit 64
fi
upstream=$(cd "$1" && pwd -P)
gcl=$(cd "$2" && pwd -P)
work=${3:-"$PWD/wp10-replay"}
mkdir -p "$work"/PNPAbove
work=$(cd "$work" && pwd -P)

upstream_commit=5926bdff5db621f44682a101007ef2fe3ae8d970
gcl_commit=b447809368083cdab92395dd1f64654388b2aa64
b08=45b9fa687fad92bf1b1d4be2809473e0c4f9957d
b09=3b64353814fd70a77810e51f2d04cbcfb4271def
b10=860ad60fca4e99fcd836eec748fa419efd0701b2

test "$(git -C "$upstream" rev-parse HEAD)" = "$upstream_commit" ||
  { echo "SOURCE_LOCK_MISMATCH upstream" >&2; exit 65; }
test "$(git -C "$gcl" merge-base "$gcl_commit" HEAD)" = "$gcl_commit" ||
  { echo "SOURCE_LOCK_MISMATCH gcl" >&2; exit 65; }

src=$gcl/research/PNP-ABOVE
for tag in 08 09 10 11; do
  case "$tag" in
    08) name=WP08_NineBitDecider.lean; expected=$b08;;
    09) name=WP09_InterpreterSoundness.lean; expected=$b09;;
    10) name=WP10_SourceAcceptanceBridge.lean; expected=$b10;;
    11) name=WP11_EvalFuelCompleteness.lean; expected=$(git -C "$gcl" rev-parse "HEAD:research/PNP-ABOVE/WP11_EvalFuelCompleteness.lean");;
  esac
  source_path=$src/$name
  test -f "$source_path" ||
    { echo "SOURCE_MISSING $name" >&2; exit 66; }
  actual=$(git -C "$gcl" hash-object -- "$source_path")
  test "$actual" = "$expected" ||
    { echo "SOURCE_BLOB_MISMATCH $name: $actual" >&2; exit 65; }
  cp -- "$source_path" "$work/PNPAbove/WP$tag.lean"
done

test -z "$(git -C "$gcl" status --porcelain -- research/PNP-ABOVE/WP11_EvalFuelCompleteness.lean)" || { echo UNCOMMITTED_WP11_SOURCE >&2; exit 65; }
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
for tag in 08 09 10 11; do
  echo "CHECKING_SOURCE_NATIVE_WP$tag"
  lake env lean -R "$work" -o "$work/PNPAbove/WP$tag.olean" "$work/PNPAbove/WP$tag.lean" \
    > "$work/WP$tag.log" 2>&1 ||
    { echo "LEAN_FAIL_WP$tag" >&2; cat "$work/WP$tag.log" >&2; exit 1; }
done
# WP11 theorem axiom audit: machine-created by the pinned source, parsed below.
python3 "$src/WP11_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP11_IMPORTED_COST_COMPLETENESS_PASS\n' | tee "$work/status.txt"
