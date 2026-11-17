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
test "$(git -C "$gcl" merge-base "$gcl_commit" HEAD)" = "$gcl_commit" ||
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
for tag in 08 09 10; do
  echo "CHECKING_SOURCE_NATIVE_WP$tag"
  lake env lean -R "$work" -o "$work/PNPAbove/WP$tag.olean" "$work/PNPAbove/WP$tag.lean" \
    > "$work/WP$tag.log" 2>&1 ||
    { echo "LEAN_FAIL_WP$tag" >&2; cat "$work/WP$tag.log" >&2; exit 1; }
done
# Audit every public WP10 theorem for extra proof axioms. The simple
# decidable examples use kernel `decide`, NOT `native_decide`.
cat > "$work/AxiomAudit.lean" <<'EOF'
import PNPAbove.WP10
#print axioms PNPAbove.WP10.accepts_of_fuel
#print axioms PNPAbove.WP10.rejects_of_fuel
#print axioms PNPAbove.WP10.accepts_nine_bit_example
#print axioms PNPAbove.WP10.rejects_zero_index
EOF
lake env lean -R "$work" "$work/AxiomAudit.lean" > "$work/AxiomAudit.log" 2>&1 ||
  { echo "WP10_AXIOM_AUDIT_ELABORATION_FAIL" >&2; cat "$work/AxiomAudit.log" >&2; exit 1; }
python3 - "$work/AxiomAudit.log" <<'PYAX'
from pathlib import Path
import re
import sys
s = Path(sys.argv[1]).read_text()
expected = ("accepts_of_fuel", "rejects_of_fuel", "accepts_nine_bit_example", "rejects_zero_index")
allowed = {"propext", "Classical.choice", "Quot.sound"}
for theorem in expected:
    matches = re.findall(r"'PNPAbove\.WP10\." + theorem + r"' depends on axioms: \[([^\]]*)\]", s, re.S)
    if len(matches) != 1:
        raise SystemExit("AXIOM_AUDIT_NOT_FOUND " + theorem)
    found = {a.strip() for a in matches[0].split(",") if a.strip()}
    if not found <= allowed:
        raise SystemExit("UNEXPECTED_AXIOMS " + theorem + " " + repr(found - allowed))
print("WP10_STANDARD_AXIOMS_ONLY_PASS")
PYAX
printf 'WP10_IMPORTED_REPLAY_PASS\n' | tee "$work/status.txt"
