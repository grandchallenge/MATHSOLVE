#!/usr/bin/env bash
# Original MIPRE all-pred predecessor and WP18 exact-source replay.
# bash WP18_REPLAY.sh PINNED_UPSTREAM GCL_CANDIDATE WORK_DIR
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
upstream_commit=5926bdff5db621f44682a101007ef2fe3ae8d970
gcl_source=7c999a2f31f6580e8f8e7459818dd04a9bd9d8e2
test "$(git -C "$upstream" rev-parse HEAD)" = "$upstream_commit" ||
  { echo "ORIGINAL_SOURCE_LOCK_DRIFT" >&2; exit 65; }
test "$(git -C "$gcl" merge-base "$gcl_source" HEAD)" = "$gcl_source" ||
  { echo "GCL_SOURCE_PARENT_MISMATCH" >&2; exit 65; }
src=$gcl/research/PNP-ABOVE
check_old() {
  tag=$1
  name=$2
  expected=$3
  actual=$(git -C "$gcl" hash-object -- "$src/$name")
  test "$actual" = "$expected" ||
    { echo "ORIGINAL_WP$tag _BLOB_DRIFT got=$actual expected=$expected" >&2; exit 65; }
  cp -- "$src/$name" "$work/PNPAbove/WP$tag.lean"
}
check_old 08 WP08_NineBitDecider.lean 45b9fa687fad92bf1b1d4be2809473e0c4f9957d
check_old 09 WP09_InterpreterSoundness.lean 3b64353814fd70a77810e51f2d04cbcfb4271def
check_old 10 WP10_SourceAcceptanceBridge.lean 860ad60fca4e99fcd836eec748fa419efd0701b2
check_old 11 WP11_EvalFuelCompleteness.lean 088a731db4a7a1a21097a593958706df6b8a488b
check_old 12 WP12_TypedParserAndRawCounterexample.lean c509e7e96383c7cb8199d7a9095b915a6d4db759
check_old 13 WP13_NineLevelSamplerVerifier.lean 711e3e7938ea8c6682778252062adfc920ff4dbd
check_old 14 WP14_ConditionalNineStageSampler.lean 939f801c874e1e9acc6223a24eb055888466d51b
check_old 15 WP15_PerfectClassicalNoGap.lean 3e7d4905f6483acbbbafd173c735da17671dcc67
check_old 16 WP16_DiagonalSupportObstruction.lean c576f71397ce86013e07fad08e480bcff294ef3e
check_old 17 WP17_UnconditionalDiagonalNoGap.lean 86ece0db534e18327ad380a542e7636bc0d746fa
python3 "$src/WP18_SOURCE_GUARD.py" "$src/WP18_SOURCE_LOCK.json" "$src" "$work/PNPAbove"

test -f "$upstream/.lake/build/lib/lean/MIPRE/Foundations/Verifier.olean" ||
  { echo "ORIGINAL_MIPRE_SOURCE_IMPORTS_UNBUILT" >&2; exit 78; }
cd "$upstream"
base_path=$(lake env printenv LEAN_PATH)
export LEAN_PATH="$work:$base_path"
printf "UPSTREAM=%s\nPROTECTED_GCL_SOURCE_PARENT=%s\nCANDIDATE=%s\n"   "$upstream_commit" "$gcl_source" "$(git -C "$gcl" rev-parse HEAD)" > "$work/lock.txt"
sha256sum "$work"/PNPAbove/*.lean >> "$work/lock.txt"
for mod in WP08 WP09 WP10 WP11 WP12 WP13 WP14 WP15 WP16 WP17   WP18 WP18Sampler WP18Query WP18Final WP18Runs WP18Native WP18Bound WP18Value WP18NoGap; do
  echo "CHECKING_ORIGINAL_SOURCE_$mod"
  LEAN_NUM_THREADS=1 lake env lean -R "$work"     -o "$work/PNPAbove/$mod.olean" "$work/PNPAbove/$mod.lean"     > "$work/$mod.log" 2>&1 ||
    { echo "ORIGINAL_SOURCE_COMPILE_FAILED $mod" >&2; tail -n 90 "$work/$mod.log" >&2; exit 1; }
done
python3 "$src/WP18_AXIOM_AUDIT.py" "$work" "$upstream"
printf 'WP18_NATIVE_NONDIAGONAL_SAMPLER_BOUNDED_VERIFIER_NO_GAP_PASS\n' |
  tee "$work/status.txt"
