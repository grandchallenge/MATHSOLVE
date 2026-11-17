#!/usr/bin/env bash
# PNP-ABOVE WP10 bounded, fail-closed source-native Lean replay.
# Usage: bash WP10_REPLAY.sh PINNED_MIPRE_CHECKOUT EXACT_GCL_CHECKOUT [WORK_DIR]
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
gcl_commit=a0af41fad9ad58d3e333092586119b4c660da382
b08=45b9fa687fad92bf1b1d4be2809473e0c4f9957d
b09=3b64353814fd70a77810e51f2d04cbcfb4271def

test "$(git -C "$upstream" rev-parse HEAD)" = "$upstream_commit" ||
  { echo "SOURCE_LOCK_MISMATCH upstream" >&2; exit 65; }
test "$(git -C "$gcl" rev-parse HEAD)" = "$gcl_commit" ||
  { echo "SOURCE_LOCK_MISMATCH gcl" >&2; exit 65; }

src=$gcl/research/PNP-ABOVE
for tag in 08 09; do
  case "$tag" in
    08) name=WP08_NineBitDecider.lean; expected=$b08;;
    09) name=WP09_InterpreterSoundness.lean; expected=$b09;;
  esac
  source_path=$src/$name
  test -f "$source_path" ||
    { echo "SOURCE_MISSING $name" >&2; exit 66; }
  actual=$(git -C "$gcl" hash-object -- "$source_path")
  test "$actual" = "$expected" ||
    { echo "SOURCE_BLOB_MISMATCH $name: $actual" >&2; exit 65; }
  cp -- "$source_path" "$work/PNPAbove/WP$tag.lean"
done

wp10=$src/WP10_SourceAcceptanceBridge.lean
test -f "$wp10" ||
  { echo "WP10_MISSING $wp10" >&2; exit 66; }
cp -- "$wp10" "$work/PNPAbove/WP10.lean"
printf 'UPSTREAM_SHA=%s\nGCL_SHA=%s\nWP08_GIT_BLOB=%s\nWP09_GIT_BLOB=%s\n' \
  "$upstream_commit" "$gcl_commit" "$b08" "$b09" > "$work/lock.txt"
sha256sum "$work"/PNPAbove/*.lean >> "$work/lock.txt"

# No hidden network download or cold rebuild: a pre-existing exact upstream
# source-native Verifier import is necessary. Missing dependencies are a separate
# compute-route obligation, not a theorem failure.
test -f "$upstream/.lake/build/lib/lean/MIPRE/Foundations/Verifier.olean" ||
  { echo "SOURCE_IMPORTS_UNBUILT: upstream Verifier .olean missing" >&2; exit 78; }
cd "$upstream"
base_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work:$base_path"
for tag in 08 09 10; do
  echo "CHECKING_SOURCE_NATIVE_WP$tag"
  lake env lean -o "$work/PNPAbove/WP$tag.olean" "$work/PNPAbove/WP$tag.lean" \
    > "$work/WP$tag.log" 2>&1 ||
    { echo "LEAN_FAIL_WP$tag" >&2; cat "$work/WP$tag.log" >&2; exit 1; }
done
printf 'WP10_IMPORTED_REPLAY_PASS\n' | tee "$work/status.txt"
