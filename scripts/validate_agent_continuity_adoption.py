#!/usr/bin/env python3
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
ADOPTION = ROOT / ".gcl/agent-continuity.json"
AGENTS = ROOT / "AGENTS.md"
errors = []

for p in (ADOPTION, AGENTS):
    if not p.exists():
        errors.append(f"missing required file: {p.relative_to(ROOT)}")

data = {}
if ADOPTION.exists():
    try:
        data = json.loads(ADOPTION.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"invalid adoption JSON: {exc}")

if data.get("policy_id") != "GCL-AGENT-CONTINUITY-001":
    errors.append("unexpected policy_id")
if data.get("version") != "1.0.0":
    errors.append("unexpected policy version")
if data.get("required") is not True:
    errors.append("continuity policy is not required")

controls = data.get("controls", {})
for key in (
    "exact_head_preflight",
    "narrow_durable_tranches",
    "checkpoint_before_branch_expansion",
    "post_mutation_readback",
    "timeout_recovery_from_repository",
    "alternate_agent_rebind",
    "named_terminal_boundary",
):
    if controls.get(key) is not True:
        errors.append(f"required control disabled: {key}")

if AGENTS.exists():
    text = AGENTS.read_text(encoding="utf-8")
    if "GCL-AGENT-CONTINUITY-001@1.0.0" not in text:
        errors.append("AGENTS.md does not bind continuity policy")

if errors:
    for err in errors:
        print(f"ERROR: {err}", file=sys.stderr)
    raise SystemExit(1)

print("MATHSOLVE continuity adoption: PASS")
