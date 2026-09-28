#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = '.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json'
BOARD = 'handoffs/OPENMATH-2026/CEX_JOB_BOARD.md'
ENTRYPOINT = 'handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md'
RECEIPT = 'work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json'
SOURCE_CAMPAIGN = '.gcl/campaigns/OPENMATH-2026-SOURCE-ACQ/CAMPAIGN_STATE.json'
SOURCE_OPERATION = '.gcl/operations/OM26-H2-H7-SOURCE-ACQ/OPERATION.json'
H1_OPERATION = '.gcl/operations/OM26-H1-H1-12-IA-001/OPERATION.json'
H1_DISPATCH = 'contributions/OPENMATH-2026/OM26-H1/H1-12/dispatches/OM26-H1-H1-12-IA-001.json'
PREP = 'work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json'
ROUTING = '.ghos-routing/workflows.json'
JOB_BOARD_WORKFLOW = '.github/workflows/openmath-cex-job-board.yml'
INTAKE_WORKFLOW = '.github/workflows/openmath-cex-independent-contribution-intake.yml'

BASE_URL = 'https://github.com/grandchallenge/MATHSOLVE'
ENTRYPOINT_URL = BASE_URL + '/blob/main/' + ENTRYPOINT
REGISTRY_URL = 'https://raw.githubusercontent.com/grandchallenge/MATHSOLVE/main/' + REGISTRY
BOARD_URL = BASE_URL + '/blob/main/' + BOARD
H1_DISPATCH_ID = 'OM26-H1-H1-12-IA-001'
H1_AGENT_REF = 'INDEPENDENT-AGENT-001'
H1_ISSUE_URL = BASE_URL + '/issues/498'
H1_WORK_PACKAGE = 'handoffs/OPENMATH-2026/jobs/OM26-H1-H1-12-IA-001.md'


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def absolute_https(value: object) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urlparse(value)
    return parsed.scheme == 'https' and bool(parsed.netloc) and bool(parsed.path)


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    receipt = load(RECEIPT)
    source_campaign = load(SOURCE_CAMPAIGN)
    source_operation = load(SOURCE_OPERATION)
    h1_operation = load(H1_OPERATION)
    h1_dispatch = load(H1_DISPATCH)
    prep = load(PREP)
    routing = load(ROUTING)

    if registry.get('record_type') != 'GCL_CEX_ASSIGNMENT_REGISTRY':
        errors.append('assignment registry record_type mismatch')
    if registry.get('campaign') != 'OPENMATH-2026':
        errors.append('assignment registry campaign mismatch')
    if registry.get('scope') != 'OPENMATH_CAMPAIGN_WIDE_CEX_ASSIGNMENTS':
        errors.append('assignment registry is not campaign-wide')
    for op in ('OM26-H2-H7-SOURCE-ACQ', 'OM26-H1-H1-12-IA-001'):
        if op not in registry.get('operations', []):
            errors.append(f'missing registry operation {op}')

    discovery = registry.get('discovery', {})
    expected_discovery = {
        'entrypoint_url': ENTRYPOINT_URL,
        'machine_registry_url': REGISTRY_URL,
        'human_board_url': BOARD_URL,
        'operator_issue_url': BASE_URL + '/issues/495',
    }
    for key, expected in expected_discovery.items():
        if discovery.get(key) != expected:
            errors.append(f'discovery {key} mismatch')
        if not absolute_https(discovery.get(key)):
            errors.append(f'discovery {key} is not an absolute HTTPS URL')

    launch = registry.get('launch_contract', {})
    if launch.get('required_fields') != ['ENTRYPOINT_URL', 'DISPATCH_ID', 'AGENT_REF']:
        errors.append('launch contract required_fields mismatch')
    if launch.get('entrypoint_url') != ENTRYPOINT_URL:
        errors.append('launch contract entrypoint URL mismatch')
    if launch.get('repository_discovery_required') is not False:
        errors.append('zero-context launch must not require repository discovery')
    if registry.get('lease_policy', {}).get('external_self_claim_allowed') is not False:
        errors.append('external self-claim must remain disabled')

    expected_pool = receipt.get('unresolved_source_pool', [])
    if len(expected_pool) != 6:
        errors.append('authoritative unresolved source pool must contain six hills')
    source_assignments = [x for x in registry.get('assignments', []) if x.get('class') == 'SOURCE_ACQUISITION']
    if [x.get('external_hill_id') for x in source_assignments] != expected_pool:
        errors.append('source-acquisition assignments do not exactly match authoritative unresolved pool')
    if any(x.get('state') != 'AVAILABLE_FOR_LEASE' for x in source_assignments):
        errors.append('source-acquisition assignments must remain AVAILABLE_FOR_LEASE')
    if any(x.get('lease', {}).get('state') != 'UNCLAIMED' for x in source_assignments):
        errors.append('source-acquisition assignments must remain UNCLAIMED')
    if registry.get('mathematics_release_policy', {}).get('current_math_jobs') != 0:
        errors.append('H2-H7 mathematical jobs must remain zero')
    if registry.get('slot_binding_policy', {}).get('current_mapping') != 'UNRESOLVED':
        errors.append('H2-H7 slot mapping must remain unresolved')
    if source_campaign.get('protected_inputs', {}).get('authoritative_list_receipt') != f'grandchallenge/MATHSOLVE:{RECEIPT}':
        errors.append('source campaign authoritative receipt mismatch')
    if source_operation.get('scope', {}).get('may_author_hill_mathematics') is not False:
        errors.append('H2-H7 source operation mathematics firewall changed')
    if prep.get('authoritative_unresolved_source_pool', {}).get('hill_ids') != expected_pool:
        errors.append('preparation ledger source pool mismatch')

    math_assignments = [x for x in registry.get('assignments', []) if x.get('class') == 'MATHEMATICAL_RESEARCH']
    if len(math_assignments) != 1:
        errors.append('expected exactly one inaugural mathematical assignment')
    else:
        item = math_assignments[0]
        lease = item.get('lease', {})
        if item.get('assignment_id') != 'OM26-H1-H1-12':
            errors.append('H1 assignment_id mismatch')
        if item.get('hill') != 'OM26-H1' or item.get('obligation') != 'H1-12':
            errors.append('H1 assignment target mismatch')
        if item.get('external_hill_id') != 'alejandrozu/kobon-triangles':
            errors.append('H1 external hill identity mismatch')
        if item.get('state') != 'LEASED' or lease.get('state') != 'LEASED':
            errors.append('inaugural H1 assignment is not LEASED')
        if lease.get('dispatch_id') != H1_DISPATCH_ID:
            errors.append('inaugural H1 dispatch_id mismatch')
        if lease.get('agent_ref') != H1_AGENT_REF:
            errors.append('inaugural H1 agent_ref mismatch')
        if lease.get('dispatch_issue_number') != 498:
            errors.append('inaugural H1 issue number mismatch')
        if lease.get('dispatch_url') != H1_ISSUE_URL or lease.get('return_url') != H1_ISSUE_URL:
            errors.append('inaugural H1 dispatch/return URL mismatch')
        if not isinstance(lease.get('protected_lease_commit'), str) or len(lease.get('protected_lease_commit', '')) != 40:
            errors.append('inaugural H1 lease lacks introducing commit identity')
        if item.get('work_package') != H1_WORK_PACKAGE:
            errors.append('inaugural H1 work-package path mismatch')
        if item.get('work_package_url') != BASE_URL + '/blob/main/' + H1_WORK_PACKAGE:
            errors.append('inaugural H1 work-package URL mismatch')
        if item.get('operation_contract') != H1_OPERATION:
            errors.append('inaugural H1 operation contract mismatch')
        if item.get('dispatch_record') != H1_DISPATCH:
            errors.append('inaugural H1 dispatch record mismatch')
        if item.get('return_protocol') != 'GCL-CONTRIBUTION-RESULT/1':
            errors.append('inaugural H1 return protocol mismatch')
        perms = item.get('permissions', {})
        if perms.get('hill_specific_mathematics') is not True:
            errors.append('inaugural H1 mathematical permission missing')
        for key in ('competition_submission', 'certification', 'canonical_claim_mutation'):
            if perms.get(key) is not False:
                errors.append(f'inaugural H1 prohibited permission enabled: {key}')
        prereq = item.get('prerequisites', {})
        if prereq.get('protected_source_lock_required') is not True or prereq.get('solve_release') is not True:
            errors.append('inaugural H1 source/release prerequisites mismatch')
        sl = prereq.get('source_lock', {})
        if sl.get('repository') != 'grandchallenge/MATHFORGE' or sl.get('blob_sha1') != '7a90cd6eeb54e8e4c5b63c5977e40a1ab5bcaa2c':
            errors.append('inaugural H1 source-lock identity mismatch')

    if h1_operation.get('operation') != H1_DISPATCH_ID:
        errors.append('H1 operation ID mismatch')
    if h1_operation.get('assignment_id') != 'OM26-H1-H1-12':
        errors.append('H1 operation assignment mismatch')
    if h1_operation.get('agent_ref') != H1_AGENT_REF:
        errors.append('H1 operation agent mismatch')
    if h1_operation.get('return', {}).get('issue_url') != H1_ISSUE_URL:
        errors.append('H1 operation return surface mismatch')

    if h1_dispatch.get('dispatch_id') != H1_DISPATCH_ID:
        errors.append('H1 dispatch record ID mismatch')
    if h1_dispatch.get('agent_ref') != H1_AGENT_REF:
        errors.append('H1 dispatch record agent mismatch')
    if h1_dispatch.get('github_issue_number') != 498 or h1_dispatch.get('github_issue_url') != H1_ISSUE_URL:
        errors.append('H1 dispatch issue binding mismatch')
    if h1_dispatch.get('bootstrap_path') != H1_WORK_PACKAGE:
        errors.append('H1 dispatch bootstrap path mismatch')
    wp = ROOT / H1_WORK_PACKAGE
    if not wp.is_file():
        errors.append('H1 inaugural work package missing')
    else:
        text = wp.read_text(encoding='utf-8')
        for marker in (
            'GCL-CONTRIBUTION-DISPATCH/1',
            'dispatch_id: OM26-H1-H1-12-IA-001',
            'agent_ref: INDEPENDENT-AGENT-001',
            'GCL-CONTRIBUTION-RESULT/1',
            '## Strongest exact statement',
            '## Next residual',
        ):
            if marker not in text:
                errors.append(f'H1 work package missing marker {marker}')

    entrypoint = (ROOT / ENTRYPOINT).read_text(encoding='utf-8')
    for marker in (ENTRYPOINT_URL, REGISTRY_URL, 'DISPATCH_ID:', 'AGENT_REF:', 'work_package_url'):
        if marker not in entrypoint:
            errors.append(f'external-agent entrypoint missing marker {marker}')

    board = (ROOT / BOARD).read_text(encoding='utf-8')
    if H1_DISPATCH_ID not in board or H1_AGENT_REF not in board or 'LEASED' not in board:
        errors.append('human board does not expose inaugural H1 lease')
    if 'No H2-H7 mathematical hill-climbing package is executable yet.' not in board:
        errors.append('human board lost H2-H7 mathematics firewall')

    by_path = {x.get('path'): x for x in routing.get('workflows', [])}
    job_board = by_path.get(JOB_BOARD_WORKFLOW)
    if not job_board or job_board.get('controller_id') != 'GITHUB_ACTIONS':
        errors.append('job-board workflow routing registration missing')
    intake = by_path.get(INTAKE_WORKFLOW)
    if not intake:
        errors.append('OPENMATH independent contribution intake workflow routing registration missing')
    else:
        if intake.get('observed_features') != ['OPAQUE_EXECUTION', 'SECRET_CREDENTIAL', 'WRITE_CAPABLE']:
            errors.append('OPENMATH intake workflow routing features mismatch')
        if intake.get('topology') != 'PERSISTENT_CONTROLLER_REQUIRED' or intake.get('controller_id') != 'GITHUB_ACTIONS':
            errors.append('OPENMATH intake workflow routing topology mismatch')

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    print('PASS: OPENMATH CEX has one protected inaugural H1 mathematical lease with automated RESULT/1 return')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
