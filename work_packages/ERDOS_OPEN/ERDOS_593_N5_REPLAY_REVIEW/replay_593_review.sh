#!/usr/bin/env bash
set -euo pipefail
packet_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
task_root="${1:?Supply an absolute scratch directory with sufficient host disk space}"
[[ "$task_root" = /* ]] || { echo 'Scratch directory must be absolute'; exit 2; }
lean --version | grep -F 'version 4.28.0'
lean --version | grep -F '7e01a1bf5c70fc6167d49c345d3bf80596e9a79b'
if grep -qi microsoft /proc/sys/kernel/osrelease; then
  : "${TASK_HOST_FREE_BYTES:?For WSL, provide measured free bytes on the Windows volume containing the VHDX}"
  [[ "$TASK_HOST_FREE_BYTES" =~ ^[0-9]+$ && "$TASK_HOST_FREE_BYTES" -ge 40000000000 ]] || exit 2
fi
mkdir -p "$task_root"
cd "$task_root"
if [[ ! -d source/.git ]]; then
  mkdir -p source
  git -C source init -q
  git -C source remote add origin https://github.com/ericlisg/erdos-593-1177-lean.git
  git -C source fetch --depth=1 origin 5dcb6e4906df03f2e4294b21be73b55db7736f5a
  git -C source checkout --detach FETCH_HEAD
fi
cd source
[[ "$(git rev-parse HEAD)" = 5dcb6e4906df03f2e4294b21be73b55db7736f5a ]]
git diff --quiet -- RequestProject lake-manifest.json lean-toolchain lakefile.toml
if [[ ! -d .lake/packages/mathlib/.git ]]; then
  mkdir -p .lake/packages/mathlib
  git -C .lake/packages/mathlib init -q
  git -C .lake/packages/mathlib remote add origin https://github.com/leanprover-community/mathlib4.git
  git -C .lake/packages/mathlib fetch --depth=1 origin 8f9d9cff6bd728b17a24e163c9402775d9e6a365
  git -C .lake/packages/mathlib checkout --detach FETCH_HEAD
fi
lake exe cache get
[[ "$(git -C .lake/packages/mathlib rev-parse HEAD)" = 8f9d9cff6bd728b17a24e163c9402775d9e6a365 ]]
timeout 1800s lake build > "$task_root/build.log" 2>&1
lake env lean RequestProject/AxiomAudit.lean > "$task_root/axioms.log" 2>&1
cp "$packet_dir/ProtectedInterface.lean" "$packet_dir/StatementFidelityAudit.lean" "$packet_dir/SourceTargetBridge.lean" .
lake env bash "$packet_dir/bridge_inner.sh" > "$task_root/bridge.log" 2>&1
echo "Review outputs: $task_root/build.log $task_root/axioms.log $task_root/bridge.log"
