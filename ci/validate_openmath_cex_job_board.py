#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = '.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json'
BOARD = 'handoffs/OPENMATH-2026/CEX_JOB_BOARD.md'
RECEIPT = 'work_packages/OPENMATH_2026/H2_H7_AUTHORITATIVE_LIST_RECEIPT.json'
CAMPAIGN = '.gcl/campaigns/OPENMATH-2026-SOURCE-ACQ/CAMPAIGN_STATE.json'
OPERATION = '.gcl/operations/OM26-H2-H7-SOURCE-ACQ/OPERATION.json'
PREP = 'work_packages/OPENMATH_2026/CEX_H2_H7_PREPARATION.json'
ROUTING = '.ghos-routing/workflows.json'
WORKFLOW = '.github/workflows/openmath-cex-job-board.yml'


def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))


def validate() -> list[str]:
    errors: list[str] = []
    registry = load(REGISTRY)
    receipt = load(RECEIPT)
    campaign = load(CAMPAIGN)
    operation = load(OPERATION)
    prep = load(PREP)
    routing = load(ROUTING)

    if registry.get('record_type') != 'GCL_CEX_ASSIGNMENT_REGISTRY':
        errors.append('assignment registry record_type mismatch')
    if registry.get('campaign') != 'OPENMATH-2026':
        errors.append('assignment registry campaign mismatch')
    if registry.get('operation') != 'OM26-H2-H7-SOURCE-ACQ':
        errors.append('assignment registry operation mismatch')

    if registry.get('lease_policy', {}).get('external_self_claim_allowed') is not False:
        errors.append('external self-claim must remain disabled')
    if registry.get('mathematics_release_policy', {}).get('current_math_jobs') != 0:
        errors.append('H2-H7 mathematical jobs must remain zero before source lock and slot bind')
    if registry.get('slot_binding_policy', {}).get('current_mapping') != 'UNRESOLVED':
        errors.append('slot mapping must remain unresolved')

    expected_pool = receipt.get('unresolved_source_pool', [])
    if len(expected_pool) != 6:
        errors.append('authoritative unresolved source pool must contain six hills')
    if 'alejandrozu/kobon-triangles' in expected_pool:
        errors.append('H1 must not appear in unresolved source pool')

    assignments = registry.get('assignments', [])
    ids = [item.get('assignment_id') for item in assignments]
    if len(ids) != len(set(ids)):
        errors.append('assignment IDs are not unique')
    observed_pool = [item.get('external_hill_id') for item in assignments]
    if observed_pool != expected_pool:
        errors.append(f'assignment hill IDs do not exactly match authoritative source pool: {observed_pool}')

    source_pool = registry.get('source_pool', {})
    if source_pool.get('receipt') != RECEIPT:
        errors.append('registry does not bind authoritative list receipt')
    if source_pool.get('normalized_sha256') != receipt.get('source', {}).get('normalized_sha256'):
        errors.append('registry source-pool digest mismatch')

    prep_pool = prep.get('authoritative_unresolved_source_pool', {})
    if prep_pool.get('receipt') != RECEIPT:
        errors.append('preparation ledger does not bind authoritative list receipt')
    if prep_pool.get('hill_ids') != expected_pool:
        errors.append('preparation ledger source pool mismatch')

    for item in assignments:
        aid = item.get('assignment_id')
        hill = item.get('external_hill_id')
        if item.get('class') != 'SOURCE_ACQUISITION':
            errors.append(f'{aid}: class must be SOURCE_ACQUISITION')
        if item.get('state') != 'AVAILABLE_FOR_LEASE':
            errors.append(f'{aid}: initial state must be AVAILABLE_FOR_LEASE')
        if item.get('slot_binding') is not None:
            errors.append(f'{aid}: slot_binding must remain null before protected binding')
        lease = item.get('lease', {})
        if lease.get('state') != 'UNCLAIMED':
            errors.append(f'{aid}: initial lease must be UNCLAIMED')
        for key in ('dispatch_id', 'agent_ref', 'dispatch_issue_number', 'protected_lease_commit'):
            if lease.get(key) is not None:
                errors.append(f'{aid}: {key} must be null while unclaimed')
        perms = item.get('permissions', {})
        for key in ('hill_specific_mathematics', 'competition_submission', 'certification', 'canonical_claim_mutation'):
            if perms.get(key) is not False:
                errors.append(f'{aid}: permission {key} must remain false')
        if item.get('prerequisites', {}).get('source_lock') is not None:
            errors.append(f'{aid}: source lock must remain null before acquisition')

        wp = ROOT / str(item.get('work_package', ''))
        if not wp.is_file():
            errors.append(f'{aid}: work package missing')
            continue
        text = wp.read_text(encoding='utf-8')
        required = [
            f'**Assignment ID:** `{aid}`',
            f'**Organizer hill ID:** `{hill}`',
            '## Execution gate',
            'NO_ACTIVE_LEASE',
            'Do not self-claim this assignment.',
            '## Successor gate',
        ]
        for marker in required:
            if marker not in text:
                errors.append(f'{aid}: work package missing marker {marker}')

    board = (ROOT / BOARD).read_text(encoding='utf-8')
    for item in assignments:
        row = f'| `{item["assignment_id"]}` | `{item["external_hill_id"]}` | `{item["state"]}` | `{item["work_package"]}` |'
        if board.count(row) != 1:
            errors.append(f'{item["assignment_id"]}: human board row missing or duplicated')
    if 'External agents do **not** choose or claim work by browsing the repository.' not in board:
        errors.append('human board self-claim prohibition missing')
    if 'No H2-H7 mathematical hill-climbing package is executable yet.' not in board:
        errors.append('human board source-lock firewall missing')

    if campaign.get('protected_inputs', {}).get('authoritative_list_receipt') != f'grandchallenge/MATHSOLVE:{RECEIPT}':
        errors.append('campaign state does not bind authoritative list receipt')
    if operation.get('external_assignment_policy', {}).get('registry') != REGISTRY:
        errors.append('operation does not bind assignment registry')
    if operation.get('external_assignment_policy', {}).get('external_self_claim_allowed') is not False:
        errors.append('operation external self-claim boundary mismatch')
    if operation.get('scope', {}).get('may_author_hill_mathematics') is not False:
        errors.append('operation hill mathematics firewall changed')

    entries = [x for x in routing.get('workflows', []) if x.get('path') == WORKFLOW]
    if len(entries) != 1:
        errors.append('job-board workflow must be registered exactly once')
    else:
        entry = entries[0]
        if entry.get('observed_features') != ['OPAQUE_EXECUTION']:
            errors.append('job-board workflow routing features mismatch')
        if entry.get('topology') != 'PERSISTENT_CONTROLLER_REQUIRED':
            errors.append('job-board workflow topology mismatch')
        if entry.get('controller_id') != 'GITHUB_ACTIONS':
            errors.append('job-board workflow controller mismatch')

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    print('PASS: OPENMATH CEX assignment pickup is coherent, source-pool exact, and fail-closed')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
