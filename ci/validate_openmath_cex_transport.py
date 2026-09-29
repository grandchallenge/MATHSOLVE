#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / '.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json'
ENTRYPOINT = ROOT / 'handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md'
CONTRACT = ROOT / 'handoffs/OPENMATH-2026/CEX_TRANSPORT_CONTRACT.md'
BOARD = ROOT / 'handoffs/OPENMATH-2026/CEX_JOB_BOARD.md'

def validate() -> list[str]:
    errors: list[str] = []
    registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
    entry = ENTRYPOINT.read_text(encoding='utf-8')
    contract = CONTRACT.read_text(encoding='utf-8')
    board = BOARD.read_text(encoding='utf-8')

    policy = registry.get('return_policy', {})
    if policy.get('capability_assumption_forbidden') is not True:
        errors.append('registry does not forbid assumed external capabilities')
    for key in ('task_hydration_rule','primary_return','fallback_return','no_return_path_rule','relay_durability_rule','transport_contract'):
        if not policy.get(key): errors.append(f'missing return_policy.{key}')

    for marker in ('TASK_HYDRATION = AVAILABLE','GITHUB_WRITE_AVAILABLE','LAUNCHER_RELAY_AVAILABLE','GCL-RETURN-RELAY/1','LAUNCH_TRANSPORT_BLOCKED','BEGIN_RESULT','END_RESULT'):
        if marker not in contract: errors.append(f'transport contract missing {marker}')
        if marker not in entry and marker not in ('BEGIN_RESULT','END_RESULT'): errors.append(f'entrypoint missing {marker}')

    if 'MUST NOT assume that a zero-context worker has GitHub access' not in board:
        errors.append('job board launcher contract still permits GitHub capability assumption')
    if 'launcher-supplied exact work-package content' not in board:
        errors.append('job board lacks self-contained hydration requirement')
    if 'GCL-RETURN-RELAY/1' not in board:
        errors.append('job board lacks relay return path')

    return errors

def main() -> int:
    errors = validate()
    if errors:
        for error in errors: print('FAIL:', error)
        return 1
    print('PASS: OPENMATH CEX transport is capability-explicit and has a durable relay path')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
