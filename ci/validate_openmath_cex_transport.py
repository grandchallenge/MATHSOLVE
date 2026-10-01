#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / '.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json'
ENTRYPOINT = ROOT / 'handoffs/OPENMATH-2026/CEX_AGENT_ENTRYPOINT.md'
CONTRACT = ROOT / 'handoffs/OPENMATH-2026/CEX_TRANSPORT_CONTRACT.md'
BOARD = ROOT / 'handoffs/OPENMATH-2026/CEX_JOB_BOARD.md'
LAUNCH_DIR = ROOT / 'handoffs/OPENMATH-2026/launch'
PINNED_URL = re.compile(
    r'^https://github\.com/grandchallenge/MATHSOLVE/blob/([0-9a-f]{40})/(.+)$'
)


def git_blob_sha1(data: bytes) -> str:
    header = f'blob {len(data)}\0'.encode('ascii')
    return hashlib.sha1(header + data).hexdigest()


def validate_iteration_policy(policy: dict) -> list[str]:
    errors = []
    expected = {
        'mode': 'ANONYMOUS_PARTICIPATION_GITHUB_AUTHENTICATED_RETURN',
        'zero_credentialed_intake': 'POSTPONED',
        'participant_environment_github_auth_required': True,
        'gcl_organization_membership_required': False,
        'gcl_repository_write_access_required': False,
        'gcl_specific_credentials_required': False,
        'real_world_identity_required': False,
        'github_posting_actor_public': True,
        'default_submission': 'COMPLETE_RELAY_ENVELOPE_COMMENT_ON_EXACT_INTENDED_RETURN',
        'new_hosted_relay_required': False,
        'third_party_submission_service_required': False,
    }
    current = policy.get('current_iteration', {})
    if not isinstance(current, dict):
        return ['current iteration policy must be an object']
    for key, value in expected.items():
        actual = current.get(key)
        if type(actual) is not type(value) or actual != value:
            errors.append(f'current iteration policy mismatch: {key}')
    if policy.get('missing_github_capability_effect') != 'RETURN_TRANSPORT_UNAVAILABLE_BEFORE_SUBSTANTIVE_WORK':
        errors.append('missing authenticated posting capability must block work')
    unsolicited = policy.get('unsolicited_return', {})
    if not isinstance(unsolicited, dict) or unsolicited.get('authentication_owner') != 'AUTHENTICATED_PARTICIPANT_ENVIRONMENT':
        errors.append('unsolicited return authentication owner mismatch')
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    registry = json.loads(REGISTRY.read_text(encoding='utf-8'))
    entry = ENTRYPOINT.read_text(encoding='utf-8')
    contract = CONTRACT.read_text(encoding='utf-8')
    board = BOARD.read_text(encoding='utf-8')

    policy = registry.get('return_policy', {})
    errors.extend(validate_iteration_policy(policy))
    for label, text in (('entrypoint', entry), ('contract', contract)):
        if 'You do not need GitHub authentication' in text:
            errors.append(f'{label}: stale credential-free kickoff')
        if 'The default return path is the launching conversation' in text:
            errors.append(f'{label}: stale chat-only default return')
        if 'Zero-credentialed agent intake is POSTPONED' not in text:
            errors.append(f'{label}: missing zero-credential deferral')
    if policy.get('agent_github_auth_required') is not False:
        errors.append('registry requires agent GitHub authentication')
    if policy.get('self_contained_launch_required') is not False:
        errors.append('legacy pasted self-contained launch mode remains required')
    if policy.get('self_contained_task_artifact_required') is not True:
        errors.append('linked task artifact is not required to be self-contained')
    if policy.get('manual_envelope_transfer_required') is not False:
        errors.append('manual envelope transfer remains part of transport')
    if policy.get('primary_launch_mode') != 'LINK_IN_RELAY_OUT':
        errors.append('primary launch mode is not LINK_IN_RELAY_OUT')
    if policy.get('task_read_auth_required') is not False:
        errors.append('public task read incorrectly requires authentication')
    if policy.get('task_fetch_fallback') != 'LAUNCHER_HYDRATES_EXACT_IMMUTABLE_TASK_ARTIFACT':
        errors.append('launcher-side task hydration fallback is not protected')
    if policy.get('durable_intake_owner') != 'AUTHENTICATED_GCL_INFRASTRUCTURE':
        errors.append('durable intake is not owned by authenticated GCL infrastructure')
    if policy.get('direct_agent_github_return') != 'OPTIONAL_IF_EXPLICITLY_AVAILABLE':
        errors.append('direct agent GitHub posting is not optional')

    lease = registry.get('lease_policy', {})
    start_rule = lease.get('start_rule', '')
    if 'resolves that assignment to its registered immutable task_url' not in start_rule:
        errors.append('lease start rule does not resolve one immutable task URL')
    if 'No human is required to reconstruct or paste a task envelope' not in lease.get('no_lease_rule', ''):
        errors.append('no-lease rule does not exclude human task reconstruction')

    launch = registry.get('launch_contract', {})
    if launch.get('mode') != 'LINK_IN_RELAY_OUT':
        errors.append('launch contract mode mismatch')
    if launch.get('required_fields') != ['TASK_URL', 'TASK_COMMIT', 'TASK_BLOB_SHA1']:
        errors.append('launch contract required fields are not exact immutable-link identity')
    if launch.get('default_return') != 'GCL-RETURN-RELAY/1 comment on exact INTENDED_RETURN':
        errors.append('launch default must be authenticated issue return')
    if 'You do not need GitHub authentication' in launch.get('canonical_agent_prompt', ''):
        errors.append('launch prompt contains stale credential-free instruction')
    if launch.get('launcher_verification_required') is not True:
        errors.append('launcher-side lease verification is not required')
    if launch.get('agent_repository_discovery_required') is not False:
        errors.append('agent repository discovery remains required')
    if launch.get('agent_github_auth_required') is not False:
        errors.append('launch contract requires GitHub authentication')
    if launch.get('manual_copy_paste_required') is not False:
        errors.append('manual task copy/paste remains required')
    if launch.get('public_task_url_is_primary') is not True:
        errors.append('public immutable task URL is not primary')
    if launch.get('fallback_hydration_owner') != 'AUTHENTICATED_GCL_LAUNCHER':
        errors.append('fallback hydration is not launcher-owned')
    if 'human operator SHALL NOT be required' not in launch.get('fallback_rule', ''):
        errors.append('fallback rule does not protect human from manual transport')
    if 'SELF_CONTAINED_WORK_PACKAGE' in launch.get('required_fields', []):
        errors.append('legacy pasted work-package field leaked into launch contract')

    for marker in (
        'LINK_IN_RELAY_OUT',
        'immutable public task URL',
        'GCL-RETURN-RELAY/1',
        'Authenticated GCL infrastructure',
    ):
        if marker not in entry and marker not in contract:
            errors.append(f'missing transport invariant: {marker}')

    if 'Nothing else from the work package needs to be copied' not in entry:
        errors.append('entrypoint does not state one-link launch clearly')
    if 'SHALL NOT require a human operator to locate or paste the work package' not in contract:
        errors.append('transport contract does not prohibit manual human shuttling')
    if 'launcher/controller SHALL fetch that exact pinned task artifact' not in contract:
        errors.append('transport contract lacks automatic launcher hydration fallback')
    if 'Canonical mode is `LINK_IN_RELAY_OUT`' not in board:
        errors.append('job board does not expose canonical link-in mode')

    scripts = launch.get('current_scripts', {})
    expected_hills = [f'OM26-H{i}' for i in range(1, 8)]
    if list(scripts) != expected_hills:
        errors.append('current launch-script roster is not exactly OM26-H1 through OM26-H7')

    h1 = scripts.get('OM26-H1', {})
    if h1.get('executable') is not True and h1.get('reason') != 'NO_ACTIVE_SUCCESSOR_LEASE':
        errors.append('H1 launch guard does not reflect no active successor lease')

    for hill in expected_hills:
        row = scripts.get(hill, {})
        rel = row.get('path', '')
        path = ROOT / rel
        if not path.is_file():
            errors.append(f'{hill}: registered launch task missing')
            continue

        task_url = row.get('task_url', '')
        task_commit = row.get('task_commit', '')
        task_blob = row.get('task_blob_sha1', '')
        match = PINNED_URL.match(task_url)
        if not match:
            errors.append(f'{hill}: task URL is not immutable commit-pinned GitHub URL')
        else:
            url_commit, url_path = match.groups()
            if url_commit != task_commit:
                errors.append(f'{hill}: task URL commit differs from task_commit')
            if url_path != rel:
                errors.append(f'{hill}: task URL path differs from registered path')
        if not re.fullmatch(r'[0-9a-f]{40}', task_commit):
            errors.append(f'{hill}: invalid task_commit')
        actual_blob = git_blob_sha1(path.read_bytes())
        if task_blob != actual_blob:
            errors.append(f'{hill}: registered task blob does not match exact task bytes')

        text = path.read_text(encoding='utf-8')
        if 'GCL-ZERO-CONTEXT-LAUNCH/2' not in text:
            errors.append(f'{hill}: task artifact missing GCL-ZERO-CONTEXT-LAUNCH/2')
        if 'H2-H7' in text:
            errors.append(f'{hill}: deprecated aggregate topology leaked into launch task')
        if row.get('executable') is not True:
            if 'NOT_EXECUTABLE_NO_ACTIVE_LEASE' not in text or 'INVALID_LAUNCH' not in text:
                errors.append('H1 task guard is not explicit')
            continue
        for marker in (
            'GCL-RETURN-RELAY/1',
            'BEGIN_RESULT',
            'END_RESULT',
            'Authenticated GCL infrastructure owns durable GitHub intake',
            '## Embedded protected source snapshots',
        ):
            if marker not in text:
                errors.append(f'{hill}: linked task missing invariant {marker}')
        for field in ('assignment_id', 'dispatch_id', 'agent_ref', 'intended_return'):
            value = row.get(field)
            if not value or value not in text:
                errors.append(f'{hill}: registered {field} does not match task content')
        if 'Return exactly one GitHub issue comment' in text:
            errors.append(f'{hill}: legacy direct-GitHub return instruction leaked into current task')
        if 'Execute only under a protected' in text or 'Execute only when' in text:
            errors.append(f'{hill}: agent-side lease rediscovery leaked into current task')

    index = LAUNCH_DIR / 'README.md'
    if not index.is_file():
        errors.append('current launch-link index missing')
    else:
        index_text = index.read_text(encoding='utf-8')
        if 'LINK_IN_RELAY_OUT' not in index_text:
            errors.append('launch index does not declare link-in relay-out mode')
        if 'No human work-package copy/paste is part of the protocol' not in index_text:
            errors.append('launch index does not exclude manual copy/paste')
        for i in range(1, 8):
            row = scripts.get(f'OM26-H{i}', {})
            if row.get('task_url') not in index_text:
                errors.append(f'launch index missing immutable H{i} task URL')

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print('FAIL:', error)
        return 1
    print('PASS: OPENMATH CEX uses immutable LINK_IN_RELAY_OUT transport with launcher-owned fallback and durable GCL intake')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
