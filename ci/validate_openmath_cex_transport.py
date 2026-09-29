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
    if policy.get('agent_github_auth_required') is not False:
        errors.append('registry still requires agent GitHub authentication')
    if policy.get('self_contained_launch_required') is not True:
        errors.append('registry does not require self-contained launch hydration')
    if policy.get('durable_intake_owner') != 'AUTHENTICATED_GCL_INFRASTRUCTURE':
        errors.append('durable intake is not owned by authenticated GCL infrastructure')
    if policy.get('direct_agent_github_return') != 'OPTIONAL_IF_EXPLICITLY_AVAILABLE':
        errors.append('direct agent GitHub posting is not optional')
    if policy.get('missing_github_capability_effect') != 'NO_BLOCK':
        errors.append('missing GitHub capability still blocks execution')

    lease = registry.get('lease_policy', {})
    if 'launcher/controller verifies exactly one protected LEASED assignment' not in lease.get('start_rule', ''):
        errors.append('lease start rule still delegates protected-lease discovery to the external agent')
    launch = registry.get('launch_contract', {})
    if launch.get('launcher_verification_required') is not True:
        errors.append('launch contract does not require launcher-side lease verification')
    if launch.get('agent_repository_discovery_required') is not False:
        errors.append('launch contract still requires agent repository discovery')
    for field in ('ASSIGNMENT_ID','INTENDED_RETURN','PROTECTED_LEASE_IDENTITY','SELF_CONTAINED_WORK_PACKAGE','RESULT_GRAMMAR','CLAIM_BOUNDARY'):
        if field not in launch.get('required_fields', []):
            errors.append(f'launch contract missing required field {field}')

    required = ('GCL-RETURN-RELAY/1','BEGIN_RESULT','END_RESULT','Direct posting is optional','not required to have GitHub access')
    for marker in required:
        if marker not in contract and marker not in entry:
            errors.append(f'missing transport invariant: {marker}')

    if 'not required to authenticate to GitHub' not in board:
        errors.append('job board still implies GitHub-authenticated external agents')
    if 'Authenticated GCL infrastructure' not in board:
        errors.append('job board does not assign durable intake to GCL infrastructure')

    return errors

def main() -> int:
    errors = validate()
    if errors:
        for error in errors: print('FAIL:', error)
        return 1
    print('PASS: OPENMATH CEX separates zero-context execution from authenticated durable intake')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
