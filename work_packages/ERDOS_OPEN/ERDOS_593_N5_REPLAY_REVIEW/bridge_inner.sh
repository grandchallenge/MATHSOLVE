#!/usr/bin/env bash
set -euo pipefail
echo INTERFACE_START
lean -o .lake/build/lib/lean/ProtectedInterface.olean ProtectedInterface.lean
echo FINITE_WITNESS_START
lean -o .lake/build/lib/lean/StatementFidelityAudit.olean StatementFidelityAudit.lean
echo BRIDGE_START
timeout 1800s lean SourceTargetBridge.lean
echo BRIDGE_PASS
