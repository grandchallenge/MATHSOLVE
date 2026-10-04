#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def blob(path):
    data=path.read_bytes()
    return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def validate(root=ROOT):
    errors=[]
    campaign=json.loads((root/'work_packages/GCL_ERDOS3/CAMPAIGN.json').read_text())
    frontier=json.loads((root/'work_packages/GCL_ERDOS3/FRONTIER.json').read_text())
    gate=json.loads((root/'.gcl/campaigns/GCL-ERDOS3/FRONTIER_GATE.json').read_text())
    prov=json.loads((root/'work_packages/GCL_ERDOS3/BOOTSTRAP_PROVENANCE.json').read_text())
    f01=json.loads((root/'work_packages/GCL_ERDOS3/results/E3-F01_RESULT.json').read_text())
    tranche=json.loads((root/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-01.json').read_text())
    tranche03=json.loads((root/'work_packages/GCL_ERDOS3/E3-TRANCHE-03.json').read_text())
    tranche04=json.loads((root/'work_packages/GCL_ERDOS3/E3-TRANCHE-04.json').read_text())
    capture=json.loads((root/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_CAPTURE.json').read_text())
    adjud03=json.loads((root/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_ADJUDICATION.json').read_text())
    lease_policy=json.loads((root/'work_packages/GCL_ERDOS3/LEASE_POLICY.json').read_text())

    if campaign.get('campaign_id')!='GCL-ERDOS3' or campaign.get('status')!='ACTIVE__E3_V03_DISPATCHED':
        errors.append('campaign identity/status drift')
    if gate.get('next_residual_role')!='EVIDENCE_ONLY_NOT_SCHEDULING_AUTHORITY':
        errors.append('Next residual regained scheduling authority')
    if gate.get('default_independent_replay_budget')!=1:
        errors.append('verification budget drift')
    if gate.get('constraints',{}).get('closed_or_exhausted_node_forbids_equivalent_replay_successor') is not True:
        errors.append('replay recursion guard disabled')

    if lease_policy.get('policy_id')!='GCL-IA-LEASE-25M-24M-001':
        errors.append('lease policy identity drift')
    if lease_policy.get('initial_lease_minutes')!=25 or lease_policy.get('agent_max_execution_minutes')!=24:
        errors.append('lease duration/agent cap drift')
    if lease_policy.get('lease_clock',{}).get('start')!='canonical_activation_marker_comment_created_at':
        errors.append('lease clock no longer starts from canonical activation marker')
    if lease_policy.get('lease_clock',{}).get('activation_marker')!='GCL-LEASE-ACTIVATION/1':
        errors.append('lease activation marker drift')

    rows={x.get('id'):x for x in frontier.get('nodes',[])}
    required={
        'E3-ROOT','E3-C-D3','E3-C-D4','E3-F-D5','E3-B-SCALE-LOCAL',
        'E3-B-AP-THRESHOLD','E3-V-B01','E3-B-AP'
    }
    if not required <= set(rows):
        errors.append('frontier node set incomplete')
    if rows.get('E3-F-D5',{}).get('status')!='CLOSED':
        errors.append('E3-F-D5 not closed after exact pinned replay')
    if rows.get('E3-B-SCALE-LOCAL',{}).get('status')!='PROVED':
        errors.append('E3-B-SCALE-LOCAL not proved')
    if rows.get('E3-B-AP-THRESHOLD',{}).get('status')!='PROVED':
        errors.append('E3-B-AP-THRESHOLD not proved')
    if rows.get('E3-V-B01',{}).get('status')!='CLOSED':
        errors.append('B01 independent verification node not closed')
    if rows.get('E3-V-B01',{}).get('disposition')!='VERIFIED':
        errors.append('B01 independent verification disposition drift')
    if rows.get('E3-B-AP',{}).get('status')!='PROVED':
        errors.append('exact extremal-series equivalence not proved')
    if rows.get('E3-Q4-SERIES',{}).get('status')!='OPEN':
        errors.append('k=4 extremal-series frontier not open')
    if rows.get('E3-V-B02',{}).get('status')!='CLOSED':
        errors.append('B02 verification node not closed after E3-V02')
    if rows.get('E3-V-B02',{}).get('disposition')!='VERIFIED':
        errors.append('B02 verification disposition drift')
    if rows.get('E3-Q4-DENSITY-LOSS',{}).get('status')!='OPEN':
        errors.append('density-loss frontier not open')
    if frontier.get('active_frontier')!=['E3-Q4-DENSITY-LOSS']:
        errors.append('active frontier drift')
    if rows.get('E3-B-GLUING-RADIUS-EQUIV',{}).get('status')!='PROVED_PENDING_INDEPENDENT_VERIFY':
        errors.append('gluing-radius bridge verification state drift')
    if rows.get('E3-Q4-GLUING-RADIUS',{}).get('status')!='FORMULATED_PENDING_VERIFY':
        errors.append('gluing-radius successor candidate state drift')
    if rows.get('E3-B-FOUR-FIBRE-DEFICIT',{}).get('status')!='OPEN_NATIVE_SUBTARGET':
        errors.append('four-fibre native subtarget state drift')
    if rows.get('E3-B-QUADRATIC-MOTIF-AMPLIFICATION',{}).get('status')!='REDUCED_NATIVE_RESIDUAL':
        errors.append('quadratic-motif reduced residual state drift')
    if rows.get('E3-B-ALL-FIBRE-U3-FORCING',{}).get('status')!='PROVED_NATIVE':
        errors.append('all-fibre U3 native lemma state drift')
    if rows.get('E3-B-ADJACENT-WITNESS-DICHOTOMY',{}).get('status')!='PROVED_NATIVE':
        errors.append('adjacent witness dichotomy native lemma state drift')
    if rows.get('E3-B-JOINT-WITNESS-INCOMPATIBILITY',{}).get('status')!='OPEN_NATIVE_RESIDUAL':
        errors.append('joint-witness native residual state drift')
    if rows.get('E3-B-JOINT-WITNESS-INCOMPATIBILITY',{}).get('parent')!='E3-B-FOUR-FIBRE-DEFICIT':
        errors.append('joint-witness native residual parent drift')
    if rows.get('E3-B-QUADRATIC-MOTIF-AMPLIFICATION',{}).get('successor')!='E3-B-JOINT-WITNESS-INCOMPATIBILITY':
        errors.append('quadratic-motif successor drift')
    if rows.get('E3-B-QUADRATIC-MOTIF-AMPLIFICATION',{}).get('parent')!='E3-B-FOUR-FIBRE-DEFICIT':
        errors.append('quadratic-motif residual parent drift')
    density=rows.get('E3-Q4-DENSITY-LOSS',{})
    if density.get('prepared_tranche')!='E3-TRANCHE-04':
        errors.append('density-loss tranche-04 registration drift')
    if density.get('active_attacks')!=['E3-B-JOINT-WITNESS-INCOMPATIBILITY']:
        errors.append('density-loss active native residual drift')
    if rows.get('E3-V-B03',{}).get('status')!='LAUNCHED':
        errors.append('E3-V-B03 epoch-4 marker-clock lease not launched')
    v03_frontier=rows.get('E3-V-B03',{}).get('dispatch',{})
    if v03_frontier.get('issue_number')!=866 or v03_frontier.get('dispatch_id')!='GCL-ERDOS3-E3-V03-IA-004':
        errors.append('E3-V03 epoch-4 frontier binding drift')
    if v03_frontier.get('lease_epoch')!=4 or v03_frontier.get('replay_budget_ordinal')!=1:
        errors.append('E3-V03 epoch-4 frontier lease/replay drift')
    if v03_frontier.get('lease_clock_source')!='GITHUB_ACTIVATION_COMMENT':
        errors.append('E3-V03 epoch-4 frontier clock source drift')
    if v03_frontier.get('lease_duration_minutes')!=25 or v03_frontier.get('agent_max_execution_minutes')!=24:
        errors.append('E3-V03 epoch-4 frontier duration/cap drift')
    if rows.get('E3-V-B03',{}).get('replay_budget')!=1 or rows.get('E3-V-B03',{}).get('replay_budget_consumed')!=0:
        errors.append('E3-V03 frontier replay budget consumed by silence')

    if f01.get('disposition')!='FORMALIZED':
        errors.append('F01 disposition drift')
    if f01.get('artifact',{}).get('git_blob_sha1')!='530ee6d6651e90f683dd3e3d3abd2246f8aae6de':
        errors.append('F01 exact D5 blob drift')
    if f01.get('proof_replay',{}).get('workflow_run_id')!=36990793026:
        errors.append('F01 workflow receipt drift')
    if f01.get('proof_replay',{}).get('job_id')!=110786278497:
        errors.append('F01 job receipt drift')
    if f01.get('proof_replay',{}).get('conclusion')!='success':
        errors.append('F01 replay no longer successful')

    if tranche.get('results',{}).get('E3-B01',{}).get('frontier_action')!='INDEPENDENT_VERIFY':
        errors.append('B01 historical frontier action drift')
    if campaign.get('work_package_results',{}).get('E3-V01')!='VERIFIED__CLOSED':
        errors.append('E3-V01 closure missing')
    if campaign.get('current_frontier')!=['E3-Q4-DENSITY-LOSS']:
        errors.append('campaign frontier drift after tranche-02 synthesis')
    if campaign.get('prepared_tranche')!='E3-TRANCHE-04':
        errors.append('tranche-04 preparation missing')
    if campaign.get('prepared_work_packages')!=['E3-L01','E3-Q02','E3-T01','E3-A04']:
        errors.append('tranche-04 prepared work-package set drift')
    expected_native_results={
        'E3-L01':'NATIVE_FINITE_LIFTED_CERTIFICATE',
        'E3-Q02':'PROVED_NATIVE_LABELLED_FORCING',
        'E3-T01':'NATIVE_SMALLER_MISSING_LEMMA__PHASE_ALIGNMENT_REQUIRED',
        'E3-A04':'NATIVE_ADVERSARIAL_CLASS_RULED_OUT',
    }
    for key,value in expected_native_results.items():
        if campaign.get('work_package_results',{}).get(key)!=value:
            errors.append(f'{key} native campaign result drift')
    if campaign.get('tranche_04_manifest')!='work_packages/GCL_ERDOS3/E3-TRANCHE-04.json':
        errors.append('tranche-04 campaign manifest binding drift')
    if campaign.get('tranche_04_synthesis')!='work_packages/GCL_ERDOS3/results/E3-TRANCHE-04_SYNTHESIS.md':
        errors.append('tranche-04 campaign synthesis binding drift')
    if campaign.get('native_residual')!='E3-B-JOINT-WITNESS-INCOMPATIBILITY':
        errors.append('Q03 native residual drift')
    if campaign.get('work_package_results',{}).get('E3-Q03')!='PROVED_NATIVE_ALL_FIBRE_U3_FORCING':
        errors.append('E3-Q03 native campaign result drift')
    if campaign.get('work_package_results',{}).get('E3-Q04')!='PROVED_NATIVE_JOINT_WITNESS_DICHOTOMY':
        errors.append('E3-Q04 native campaign result drift')
    ext=campaign.get('tranche_04_extension',{})
    if ext.get('result')!='E3-Q03' or ext.get('path')!='work_packages/GCL_ERDOS3/results/E3-Q03_NATIVE_RESULT.md':
        errors.append('E3-Q03 campaign extension binding drift')
    ext2=campaign.get('tranche_04_extension_2',{})
    if ext2.get('result')!='E3-Q04' or ext2.get('path')!='work_packages/GCL_ERDOS3/results/E3-Q04_NATIVE_RESULT.md':
        errors.append('E3-Q04 campaign extension binding drift')
    if campaign.get('dispatch_state')!='VERIFY_DISPATCHED__AWAITING_RETURN':
        errors.append('E3-V03 dispatch state drift')
    if campaign.get('synthesis_allowed') is not False:
        errors.append('synthesis gate remained open after adjudication')
    if tranche03.get('status')!='ADJUDICATED__VERIFY_G01_PENDING' or tranche03.get('synthesis_allowed') is not False:
        errors.append('tranche-03 adjudication/verification gate drift')
    if tranche04.get('status')!='NATIVE_SYNTHESIS_READY__NO_FRONTIER_PROMOTION':
        errors.append('tranche-04 native synthesis status drift')
    if tranche04.get('target_node')!='E3-B-FOUR-FIBRE-DEFICIT':
        errors.append('tranche-04 target node drift')
    if tranche04.get('native_synthesis',{}).get('next_named_residual')!='E3-B-QUADRATIC-MOTIF-AMPLIFICATION':
        errors.append('tranche-04 synthesis residual drift')
    if tranche04.get('verification_separation',{}).get('gate')!='E3-V03':
        errors.append('tranche-04 verification separation drift')
    native_files={
        'E3-L01':'work_packages/GCL_ERDOS3/results/E3-L01_NATIVE_RESULT.md',
        'E3-Q02':'work_packages/GCL_ERDOS3/results/E3-Q02_NATIVE_RESULT.md',
        'E3-T01':'work_packages/GCL_ERDOS3/results/E3-T01_NATIVE_RESULT.md',
        'E3-A04':'work_packages/GCL_ERDOS3/results/E3-A04_NATIVE_RESULT.md',
    }
    for key,path in native_files.items():
        row=tranche04.get('native_results',{}).get(key,{})
        if row.get('path')!=path:
            errors.append(f'{key} tranche-04 native result path drift')
        fp=root/path
        if not fp.is_file() or blob(fp)!=row.get('blob_sha1'):
            errors.append(f'{key} tranche-04 native result blob drift')
    synrow=tranche04.get('native_synthesis',{})
    synpath=root/'work_packages/GCL_ERDOS3/results/E3-TRANCHE-04_SYNTHESIS.md'
    if synrow.get('path')!='work_packages/GCL_ERDOS3/results/E3-TRANCHE-04_SYNTHESIS.md' or not synpath.is_file() or blob(synpath)!=synrow.get('blob_sha1'):
        errors.append('tranche-04 synthesis blob drift')
    expected_dispatches={'E3-R01','E3-D01','E3-G01','E3-C01','E3-A03','E3-S04'}
    if set(campaign.get('active_dispatches',{}))!={'E3-V03'}:
        errors.append('epoch-4 E3-V03 is not sole active dispatch')
    active4=campaign.get('active_dispatches',{}).get('E3-V03',{})
    if active4.get('dispatch_id')!='GCL-ERDOS3-E3-V03-IA-004' or active4.get('issue_number')!=866:
        errors.append('E3-V03 epoch-4 campaign identity drift')
    if active4.get('lease_epoch')!=4 or active4.get('lease_attempt_ordinal')!=4 or active4.get('replay_budget_ordinal')!=1:
        errors.append('E3-V03 epoch-4 campaign lease/replay ordinal drift')
    if active4.get('lease_clock_source')!='GITHUB_ACTIVATION_COMMENT':
        errors.append('E3-V03 epoch-4 campaign clock source drift')
    if active4.get('lease_duration_minutes')!=25 or active4.get('agent_max_execution_minutes')!=24:
        errors.append('E3-V03 epoch-4 campaign duration/cap drift')
    expired3=campaign.get('completed_dispatches',{}).get('E3-V03-LEASE-003',{})
    if expired3.get('dispatch_id')!='GCL-ERDOS3-E3-V03-IA-003' or expired3.get('issue_number')!=820:
        errors.append('expired E3-V03 epoch-3 campaign identity drift')
    if expired3.get('valid_result_count')!=0 or expired3.get('replay_budget_consumed') is not False:
        errors.append('silent E3-V03 epoch-3 expiry consumed replay or invented evidence')
    if expired3.get('lease_activation_comment_id')!=5979703216:
        errors.append('expired E3-V03 epoch-3 activation marker receipt drift')
    expired2=campaign.get('completed_dispatches',{}).get('E3-V03-LEASE-002',{})
    if expired2.get('issue_number')!=814 or expired2.get('dispatch_id')!='GCL-ERDOS3-E3-V03-IA-002':
        errors.append('expired E3-V03 epoch-2 campaign identity drift')
    if expired2.get('valid_result_count')!=0 or expired2.get('replay_budget_consumed') is not False:
        errors.append('silent E3-V03 epoch-2 expiry consumed replay or invented evidence')
    if expired2.get('clock_model')!='LEGACY_STATIC_TIMESTAMP_SUPERSEDED':
        errors.append('E3-V03 epoch-2 migration boundary drift')
    expired=campaign.get('completed_dispatches',{}).get('E3-V03-LEASE-001',{})
    if expired.get('issue_number')!=798 or expired.get('dispatch_id')!='GCL-ERDOS3-E3-V03-IA-001':
        errors.append('expired E3-V03 campaign lease identity drift')
    if expired.get('valid_result_count')!=0 or expired.get('replay_budget_consumed') is not False:
        errors.append('silent E3-V03 expiry consumed replay or invented evidence')
    if not expected_dispatches <= set(campaign.get('completed_dispatches',{})):
        errors.append('tranche-03 completed dispatch set incomplete')
    if campaign.get('completed_dispatches',{}).get('E3-D01',{}).get('issue_number')!=789:
        errors.append('E3-D01 canonical intake issue drift')
    if adjud03.get('selected_successor_candidate',{}).get('id')!='E3-Q4-GLUING-RADIUS':
        errors.append('tranche-03 successor selection drift')
    if adjud03.get('selected_successor_candidate',{}).get('verification_gate')!='E3-V03':
        errors.append('tranche-03 verification gate missing')
    if adjud03.get('selected_successor_candidate',{}).get('active_frontier_effect_before_verification')!='NONE':
        errors.append('candidate advanced before independent verification')

    expected_receipts={
        'E3-R01':(788,5974689856,'PROVED_REPRESENTATION_REDUCTION','1945c71f250725619a536a08c7cbc878c8f426fd'),
        'E3-D01':(789,5974710520,'FINITE_CARRY_REPRESENTATION_PROVED','fa48b4dca2e575d639cd6ca3cae7d9064063c3cb'),
        'E3-G01':(791,5974734856,'SMALLER_GLUE_LEMMA','41037a11d9f36248fbcf49c946eb50e44ce3b03f'),
        'E3-C01':(792,5974760875,'FINITE_PATTERN_DISCOVERED','212cea2c27eeba50c243d7e4e769bd78afeb117b'),
        'E3-A03':(793,5974733560,'NO_COUNTEREXAMPLE_IN_DECLARED_FAMILY','5c54ddfede81e56bf8327b6dc8c1f7570ec21711'),
        'E3-S04':(794,5974746941,'SOURCE_INTERFACE_REQUIRES_BRIDGE','30f24cff18d14ac197695e272868786b0e77cd0c'),
    }
    if set(capture.get('receipts',{}))!=set(expected_receipts):
        errors.append('capture receipt set drift')
    if capture.get('synthesis_allowed') is not True:
        errors.append('capture manifest does not authorize synthesis')
    if capture.get('duplicate_transport',{}).get('issue_number')!=790 or capture.get('duplicate_transport',{}).get('canonical_issue_number')!=789:
        errors.append('duplicate transport quarantine drift')
    if capture.get('canonical_return_policy',{}).get('duplicate_issue_790_valid_return_surface') is not False:
        errors.append('duplicate issue 790 became a valid return surface')
    for assignment,(issue,comment,disposition,result_blob) in expected_receipts.items():
        receipt=capture.get('receipts',{}).get(assignment,{})
        dispatch=campaign.get('completed_dispatches',{}).get(assignment,{})
        dispatch_file=root/f'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-{assignment}-IA-001.json'
        result_path=root/f'work_packages/GCL_ERDOS3/results/{assignment}_RESULT.md'
        if not dispatch_file.is_file() or not result_path.is_file():
            errors.append(f'{assignment} capture artifacts missing')
            continue
        dj=json.loads(dispatch_file.read_text())
        if receipt.get('issue_number')!=issue or dispatch.get('issue_number')!=issue or dj.get('issue_number')!=issue:
            errors.append(f'{assignment} canonical issue binding drift')
        if receipt.get('comment_id')!=comment or dispatch.get('result_comment_id')!=comment or dj.get('result_comment_id')!=comment:
            errors.append(f'{assignment} result comment binding drift')
        if receipt.get('dispatch_id')!=f'GCL-ERDOS3-{assignment}-IA-001' or dj.get('dispatch_id')!=f'GCL-ERDOS3-{assignment}-IA-001':
            errors.append(f'{assignment} dispatch identity drift')
        if receipt.get('declared_disposition')!=disposition or dj.get('declared_disposition')!=disposition:
            errors.append(f'{assignment} disposition drift')
        if receipt.get('result_blob_sha1')!=result_blob or dj.get('result_blob_sha1')!=result_blob or blob(result_path)!=result_blob:
            errors.append(f'{assignment} captured result blob drift')
        text=result_path.read_text()
        expected_prefix='\n'.join([
            'GCL-CONTRIBUTION-RESULT/1',
            f'dispatch_id: GCL-ERDOS3-{assignment}-IA-001',
            f'assignment: {assignment}',
            f'agent_ref: INDEPENDENT-AGENT-{assignment}-001',
            f'disposition: {disposition}',
            'context_class: ZERO_CONTEXT',
        ])
        if not text.startswith(expected_prefix):
            errors.append(f'{assignment} RESULT/1 preamble drift')
        expected_state='ADJUDICATED__INDEPENDENT_VERIFY_REQUIRED' if assignment=='E3-G01' else 'ADJUDICATED__CLOSED_NO_FRONTIER_PROMOTION'
        if dj.get('state')!=expected_state:
            errors.append(f'{assignment} dispatch adjudication state drift')
        if dispatch.get('state')!='CLOSED_COMPLETED':
            errors.append(f'{assignment} campaign completion state drift')
        if dj.get('task_commit')!='266b0857f3e13524ea9e69e2ef3bf4cd422503b5':
            errors.append(f'{assignment} immutable task commit drift')
    v03_file=root/'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-001.json'
    if v03_file.is_file():
        v03d=json.loads(v03_file.read_text())
        if v03d.get('issue_number')!=798 or v03d.get('task_commit')!='eb94ed1df6c3743fc8a186dcc423ce372fb512c8' or v03d.get('task_blob_sha1')!='44d366be27cec0679c695c03074bceeab9b7cf01':
            errors.append('E3-V03 durable dispatch receipt drift')
        if v03d.get('state')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 expired dispatch lifecycle drift')
        if v03d.get('replay_budget_ordinal')!=1 or v03d.get('replay_budget_consumed') is not False:
            errors.append('E3-V03 expiry consumed replay budget')
        if v03d.get('dispatch_status')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 expired dispatch status drift')
        if v03d.get('lease_policy_id')!='GCL-IA-LEASE-25M-24M-001':
            errors.append('E3-V03 lease policy drift')
        if v03d.get('lease_epoch')!=1 or v03d.get('lease_attempt_ordinal')!=1:
            errors.append('E3-V03 expired lease epoch drift')
        if v03d.get('lease_started_at')!='2026-10-04T00:15:38Z' or v03d.get('lease_expires_at')!='2026-10-04T00:40:38Z':
            errors.append('E3-V03 expired lease clock drift')
        if v03d.get('lease_duration_minutes')!=25 or v03d.get('agent_max_execution_minutes')!=24:
            errors.append('E3-V03 lease duration/cap drift')
        if v03d.get('valid_result_count_at_expiry')!=0 or v03d.get('stale_return_fenced') is not True:
            errors.append('E3-V03 silent-expiry fence drift')
        if v03d.get('github_issue_number')!=798:
            errors.append('E3-V03 automated intake issue drift')
        if v03d.get('github_issue_title')!='[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-001 — gluing-radius equivalence replay':
            errors.append('E3-V03 automated intake title drift')
        if v03d.get('bootstrap_path')!='work_packages/GCL_ERDOS3/launch/E3-V03-IA-001.md':
            errors.append('E3-V03 bootstrap path drift')
        if v03d.get('bootstrap_blob_sha1')!='4909526f36f38bde2957dbaa323a3a33a1a873e6':
            errors.append('E3-V03 bootstrap blob binding drift')
        bootstrap=root/'work_packages/GCL_ERDOS3/launch/E3-V03-IA-001.md'
        if not bootstrap.is_file() or blob(bootstrap)!='4909526f36f38bde2957dbaa323a3a33a1a873e6':
            errors.append('E3-V03 protected bootstrap bytes drift')
        if set(v03d.get('allowed_dispositions',[]))!={'VERIFIED','REFUTED','EXACT_BLOCKER'}:
            errors.append('E3-V03 allowed disposition set drift')
        if v03d.get('required_sections')!=[
            'Strongest exact statement','Derivation / evidence','Adversarial checks',
            'First defect','Frontier effect','Next residual','Sources'
        ]:
            errors.append('E3-V03 RESULT/1 section contract drift')
        if v03d.get('first_valid_result_lock') is not True:
            errors.append('E3-V03 first-valid-result lock disabled')
        if v03d.get('automated_intake_canonical_effect') is not False:
            errors.append('E3-V03 automated intake gained canonical effect')
        if v03d.get('intake_workflow')!='.github/workflows/gcl-erdos3-independent-contribution-intake.yml':
            errors.append('E3-V03 intake workflow binding drift')
    else:
        errors.append('missing E3-V03 durable dispatch receipt')
    v03_file2=root/'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-002.json'
    if v03_file2.is_file():
        v03d2=json.loads(v03_file2.read_text())
        if v03d2.get('issue_number')!=814 or v03d2.get('task_commit')!='eb94ed1df6c3743fc8a186dcc423ce372fb512c8' or v03d2.get('task_blob_sha1')!='44d366be27cec0679c695c03074bceeab9b7cf01':
            errors.append('E3-V03 epoch-2 durable dispatch receipt drift')
        if v03d2.get('state')!='LEASE_EXPIRED__NO_RETURN' or v03d2.get('dispatch_status')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 epoch-2 expired lifecycle drift')
        if v03d2.get('lease_policy_id')!='GCL-IA-LEASE-25M-24M-001':
            errors.append('E3-V03 epoch-2 lease policy drift')
        if v03d2.get('lease_epoch')!=2 or v03d2.get('lease_attempt_ordinal')!=2 or v03d2.get('replay_budget_ordinal')!=1:
            errors.append('E3-V03 epoch-2 lease/replay ordinal drift')
        if v03d2.get('lease_clock_source')!='LEGACY_STATIC_TIMESTAMP_SUPERSEDED':
            errors.append('E3-V03 epoch-2 clock migration drift')
        if v03d2.get('valid_result_count_at_expiry')!=0 or v03d2.get('replay_budget_consumed') is not False or v03d2.get('stale_return_fenced') is not True:
            errors.append('E3-V03 epoch-2 silent-expiry fence drift')
        if v03d2.get('lease_duration_minutes')!=25 or v03d2.get('agent_max_execution_minutes')!=24 or v03d2.get('return_grace_minutes')!=1:
            errors.append('E3-V03 epoch-2 duration/cap drift')
        if v03d2.get('predecessor_dispatch_id')!='GCL-ERDOS3-E3-V03-IA-001' or v03d2.get('predecessor_state')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 epoch-2 predecessor fence drift')
        if v03d2.get('github_issue_title')!='[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-002 — gluing-radius equivalence replay':
            errors.append('E3-V03 epoch-2 expected active title drift')
        if v03d2.get('bootstrap_path')!='work_packages/GCL_ERDOS3/launch/E3-V03-IA-002.md' or v03d2.get('bootstrap_blob_sha1')!='4cd3c1aa7ef0ad4768b9be0f85d231bac5bda861':
            errors.append('E3-V03 epoch-2 bootstrap binding drift')
        bootstrap2=root/'work_packages/GCL_ERDOS3/launch/E3-V03-IA-002.md'
        if not bootstrap2.is_file() or blob(bootstrap2)!='4cd3c1aa7ef0ad4768b9be0f85d231bac5bda861':
            errors.append('E3-V03 epoch-2 protected bootstrap bytes drift')
        if v03d2.get('first_valid_result_lock') is not True or v03d2.get('automated_intake_canonical_effect') is not False:
            errors.append('E3-V03 epoch-2 intake integrity drift')
    else:
        errors.append('missing E3-V03 epoch-2 durable dispatch receipt')
    v03_file3=root/'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-003.json'
    if v03_file3.is_file():
        v03d3=json.loads(v03_file3.read_text())
        if v03d3.get('issue_number')!=820 or v03d3.get('task_commit')!='eb94ed1df6c3743fc8a186dcc423ce372fb512c8' or v03d3.get('task_blob_sha1')!='44d366be27cec0679c695c03074bceeab9b7cf01':
            errors.append('E3-V03 epoch-3 durable dispatch receipt drift')
        if v03d3.get('state')!='LEASE_EXPIRED__NO_RETURN' or v03d3.get('dispatch_status')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 epoch-3 expired lifecycle drift')
        if v03d3.get('lease_policy_id')!='GCL-IA-LEASE-25M-24M-001':
            errors.append('E3-V03 epoch-3 lease policy drift')
        if v03d3.get('lease_clock_source')!='GITHUB_ACTIVATION_COMMENT' or v03d3.get('lease_activation_marker')!='GCL-LEASE-ACTIVATION/1':
            errors.append('E3-V03 epoch-3 marker-clock drift')
        if v03d3.get('lease_epoch')!=3 or v03d3.get('lease_attempt_ordinal')!=3 or v03d3.get('replay_budget_ordinal')!=1:
            errors.append('E3-V03 epoch-3 lease/replay ordinal drift')
        if v03d3.get('lease_duration_minutes')!=25 or v03d3.get('agent_max_execution_minutes')!=24 or v03d3.get('return_grace_minutes')!=1:
            errors.append('E3-V03 epoch-3 duration/cap drift')
        if v03d3.get('lease_activation_comment_id')!=5979703216:
            errors.append('E3-V03 epoch-3 activation comment drift')
        if v03d3.get('lease_started_at_observed')!='2026-10-04T12:00:55Z' or v03d3.get('lease_expires_at_observed')!='2026-10-04T12:25:55Z':
            errors.append('E3-V03 epoch-3 observed lease clock drift')
        if v03d3.get('valid_result_count_at_expiry')!=0 or v03d3.get('replay_budget_consumed') is not False or v03d3.get('stale_return_fenced') is not True:
            errors.append('E3-V03 epoch-3 silent-expiry fence drift')
        if v03d3.get('predecessor_dispatch_id')!='GCL-ERDOS3-E3-V03-IA-002' or v03d3.get('predecessor_state')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 epoch-3 predecessor fence drift')
        if v03d3.get('github_issue_title')!='[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-003 — gluing-radius equivalence replay':
            errors.append('E3-V03 epoch-3 active title binding drift')
        if v03d3.get('github_issue_staging_title')!='[GCL-STAGING] GCL-ERDOS3 E3-V03-IA-003 — gluing-radius equivalence replay':
            errors.append('E3-V03 epoch-3 staging title binding drift')
        if v03d3.get('bootstrap_path')!='work_packages/GCL_ERDOS3/launch/E3-V03-IA-003.md' or v03d3.get('bootstrap_blob_sha1')!='b2c99c557fc3e0206f03affe469a87fbb8a8ec46':
            errors.append('E3-V03 epoch-3 bootstrap binding drift')
        bootstrap3=root/'work_packages/GCL_ERDOS3/launch/E3-V03-IA-003.md'
        if not bootstrap3.is_file() or blob(bootstrap3)!='b2c99c557fc3e0206f03affe469a87fbb8a8ec46':
            errors.append('E3-V03 epoch-3 protected bootstrap bytes drift')
        if v03d3.get('activation_controller')!='.github/workflows/gcl-erdos3-lease-activator.yml' or v03d3.get('reaper_controller')!='.github/workflows/gcl-erdos3-lease-reaper.yml':
            errors.append('E3-V03 epoch-3 controller binding drift')
        if v03d3.get('first_valid_result_lock') is not True or v03d3.get('automated_intake_canonical_effect') is not False:
            errors.append('E3-V03 epoch-3 intake integrity drift')
    else:
        errors.append('missing E3-V03 epoch-3 durable dispatch receipt')
    v03_file4=root/'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-004.json'
    if v03_file4.is_file():
        v03d4=json.loads(v03_file4.read_text())
        if v03d4.get('issue_number')!=866 or v03d4.get('task_commit')!='eb94ed1df6c3743fc8a186dcc423ce372fb512c8' or v03d4.get('task_blob_sha1')!='44d366be27cec0679c695c03074bceeab9b7cf01':
            errors.append('E3-V03 epoch-4 durable dispatch receipt drift')
        if v03d4.get('state')!='DISPATCHED__AWAITING_RETURN' or v03d4.get('dispatch_status')!='READY_FOR_GITHUB_COMMENT':
            errors.append('E3-V03 epoch-4 lifecycle drift')
        if v03d4.get('lease_policy_id')!='GCL-IA-LEASE-25M-24M-001':
            errors.append('E3-V03 epoch-4 lease policy drift')
        if v03d4.get('lease_clock_source')!='GITHUB_ACTIVATION_COMMENT' or v03d4.get('lease_activation_marker')!='GCL-LEASE-ACTIVATION/1':
            errors.append('E3-V03 epoch-4 marker-clock drift')
        if v03d4.get('lease_epoch')!=4 or v03d4.get('lease_attempt_ordinal')!=4 or v03d4.get('replay_budget_ordinal')!=1:
            errors.append('E3-V03 epoch-4 lease/replay ordinal drift')
        if v03d4.get('lease_duration_minutes')!=25 or v03d4.get('agent_max_execution_minutes')!=24 or v03d4.get('return_grace_minutes')!=1:
            errors.append('E3-V03 epoch-4 duration/cap drift')
        if v03d4.get('predecessor_dispatch_id')!='GCL-ERDOS3-E3-V03-IA-003' or v03d4.get('predecessor_state')!='LEASE_EXPIRED__NO_RETURN':
            errors.append('E3-V03 epoch-4 predecessor fence drift')
        if v03d4.get('github_issue_title')!='[GCL-CONTRIB] GCL-ERDOS3 E3-V03-IA-004 — gluing-radius equivalence replay':
            errors.append('E3-V03 epoch-4 active title binding drift')
        if v03d4.get('github_issue_staging_title')!='[GCL-STAGING] GCL-ERDOS3 E3-V03-IA-004 — gluing-radius equivalence replay':
            errors.append('E3-V03 epoch-4 staging title binding drift')
        if v03d4.get('bootstrap_path')!='work_packages/GCL_ERDOS3/launch/E3-V03-IA-004.md' or v03d4.get('bootstrap_blob_sha1')!='d66729bf05cf3ba176cb0ee17a6dd8d9af1b179e':
            errors.append('E3-V03 epoch-4 bootstrap binding drift')
        bootstrap4=root/'work_packages/GCL_ERDOS3/launch/E3-V03-IA-004.md'
        if not bootstrap4.is_file() or blob(bootstrap4)!='d66729bf05cf3ba176cb0ee17a6dd8d9af1b179e':
            errors.append('E3-V03 epoch-4 protected bootstrap bytes drift')
        if v03d4.get('activation_controller')!='.github/workflows/gcl-erdos3-lease-activator.yml' or v03d4.get('reaper_controller')!='.github/workflows/gcl-erdos3-lease-reaper.yml':
            errors.append('E3-V03 epoch-4 controller binding drift')
        if v03d4.get('first_valid_result_lock') is not True or v03d4.get('automated_intake_canonical_effect') is not False:
            errors.append('E3-V03 epoch-4 intake integrity drift')
    else:
        errors.append('missing E3-V03 epoch-4 durable dispatch receipt')
    if tranche.get('results',{}).get('E3-F01',{}).get('frontier_action')!='CLOSED_NO_SUCCESSOR':
        errors.append('F01 replay recursion guard drift')

    for row in prov.get('artifacts',[]):
        p=root/row['path']
        if not p.is_file() or blob(p)!=row['git_blob_sha1']:
            errors.append(f"provenance drift: {row['path']}")

    required_files=[
        'work_packages/GCL_ERDOS3/results/E3-B01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-A01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-S01_RESULT.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-V01.md',
        'work_packages/GCL_ERDOS3/results/E3-V01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-V01_ADJUDICATION.json',
        'work_packages/GCL_ERDOS3/results/E3-B02_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-S02_RESULT.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-V02.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-Q01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-X01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-A02.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-S03.md',
        'work_packages/GCL_ERDOS3/E3-TRANCHE-02.json',
        'work_packages/GCL_ERDOS3/E3-TRANCHE-03.json',
        'work_packages/GCL_ERDOS3/E3-TRANCHE-03_REPRESENTATION.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-R01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-D01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-G01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-C01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-A03.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-S04.md',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-R01-IA-001.json',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-D01-IA-001.json',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-G01-IA-001.json',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-C01-IA-001.json',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-A03-IA-001.json',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-S04-IA-001.json',
        'work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_CAPTURE.json',
        'work_packages/GCL_ERDOS3/results/E3-R01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-D01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-G01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-C01_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-A03_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-S04_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_SYNTHESIS.md',
        'work_packages/GCL_ERDOS3/results/E3-TRANCHE-03_ADJUDICATION.json',
        'work_packages/GCL_ERDOS3/E3-TRANCHE-04.json',
        'work_packages/GCL_ERDOS3/E3-TRANCHE-04_FOUR_FIBRE_DEFICIT.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-L01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-Q02.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-T01.md',
        'work_packages/GCL_ERDOS3/work_packages/E3-A04.md',
        'work_packages/GCL_ERDOS3/results/E3-L01_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-Q02_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-T01_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-A04_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-TRANCHE-04_SYNTHESIS.md',
        'work_packages/GCL_ERDOS3/results/E3-Q03_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/results/E3-Q04_NATIVE_RESULT.md',
        'work_packages/GCL_ERDOS3/tools/e3_l01_family_certificate.py',
        'work_packages/GCL_ERDOS3/LEASE_POLICY.json',
        'work_packages/GCL_ERDOS3/work_packages/E3-V03.md',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-001.json',
        'work_packages/GCL_ERDOS3/launch/E3-V03-IA-001.md',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-002.json',
        'work_packages/GCL_ERDOS3/launch/E3-V03-IA-002.md',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-003.json',
        'work_packages/GCL_ERDOS3/launch/E3-V03-IA-003.md',
        'work_packages/GCL_ERDOS3/dispatches/GCL-ERDOS3-E3-V03-IA-004.json',
        'work_packages/GCL_ERDOS3/launch/E3-V03-IA-004.md',
        'ci/gcl_erdos3_github_contribution_intake.py',
        'tests/test_gcl_erdos3_github_contribution_intake.py',
        '.github/workflows/gcl-erdos3-independent-contribution-intake.yml',
        'ci/gcl_erdos3_lease_activation.py',
        'tests/test_gcl_erdos3_lease_activation.py',
        '.github/workflows/gcl-erdos3-lease-activator.yml',
        'ci/gcl_erdos3_lease_reaper.py',
        'tests/test_gcl_erdos3_lease_reaper.py',
        '.github/workflows/gcl-erdos3-lease-reaper.yml',
    ]
    for path in required_files:
        if not (root/path).is_file():
            errors.append(f'missing {path}')

    for wp in campaign.get('initial_work_packages',[]):
        if not (root/f'work_packages/GCL_ERDOS3/work_packages/{wp}.md').is_file():
            errors.append(f'missing {wp}')
    intake_workflow=root/'.github/workflows/gcl-erdos3-independent-contribution-intake.yml'
    if intake_workflow.is_file():
        wf=intake_workflow.read_text()
        for needle in (
            'issue_comment:',
            'pull-requests: write',
            'ci/gcl_erdos3_github_contribution_intake.py',
            '--issue-comments',
            'gh pr create',
            'canonical claim effect: NONE',
            'frontier effect: NONE',
        ):
            if needle not in wf:
                errors.append(f'GCL-ERDOS3 intake workflow missing integrity control: {needle}')
    activation_script=root/'ci/gcl_erdos3_lease_activation.py'
    if activation_script.is_file():
        at=activation_script.read_text()
        for needle in (
            'ACTIVATION_MARKER = "GCL-LEASE-ACTIVATION/1"',
            'lease_duration_minutes: 25',
            'agent_max_execution_minutes: 24',
            'multiple matching activation markers exist',
        ):
            if needle not in at:
                errors.append(f'GCL-ERDOS3 activation planner missing integrity control: {needle}')
    activator_workflow=root/'.github/workflows/gcl-erdos3-lease-activator.yml'
    if activator_workflow.is_file():
        aw=activator_workflow.read_text()
        for needle in (
            'push:',
            'branches: [main]',
            'issues: write',
            'ci/gcl_erdos3_lease_activation.py',
            'Post immutable lease activation marker',
        ):
            if needle not in aw:
                errors.append(f'GCL-ERDOS3 lease activator missing integrity control: {needle}')
        if 'contents: write' in aw or 'gh pr merge' in aw or 'gh pr create' in aw:
            errors.append('GCL-ERDOS3 lease activator gained repository mutation authority')
    reaper_workflow=root/'.github/workflows/gcl-erdos3-lease-reaper.yml'
    if reaper_workflow.is_file():
        rw=reaper_workflow.read_text()
        for needle in (
            'schedule:',
            'cron: "*/5 * * * *"',
            'workflow_dispatch:',
            'ci/gcl_erdos3_lease_reaper.py',
            'gh pr create',
            'mathematical replay budget consumed: NO',
            'canonical claim effect: NONE',
            'frontier promotion effect: NONE',
        ):
            if needle not in rw:
                errors.append(f'GCL-ERDOS3 lease reaper missing integrity control: {needle}')
        if 'gh pr merge' in rw or 'canonical_claim_effect: true' in rw.lower():
            errors.append('GCL-ERDOS3 lease reaper gained unauthorized promotion/merge authority')
    ci_workflow=root/'.github/workflows/ci.yml'
    if ci_workflow.is_file():
        ci_text=ci_workflow.read_text()
        for needle in (
            'python ci/validate_gcl_erdos3_frontier.py',
            'python -m unittest tests/test_gcl_erdos3_github_contribution_intake.py tests/test_gcl_erdos3_lease_activation.py tests/test_gcl_erdos3_lease_reaper.py -v',
        ):
            if needle not in ci_text:
                errors.append(f'GCL-ERDOS3 required CI missing: {needle}')

    q03=root/'work_packages/GCL_ERDOS3/results/E3-Q03_NATIVE_RESULT.md'
    if not q03.is_file() or blob(q03)!='a102df8ac5488cadd0af367351f4544e646ad031':
        errors.append('E3-Q03 native result blob drift')
    q04=root/'work_packages/GCL_ERDOS3/results/E3-Q04_NATIVE_RESULT.md'
    if not q04.is_file() or blob(q04)!='912aefd88752f888167838eafca9f6c77cc5080f':
        errors.append('E3-Q04 native result blob drift')

    return errors

if __name__=='__main__':
    e=validate()
    for x in e: print('FAIL:',x)
    if not e: print('PASS: GCL-ERDOS3 Q04 preserves aligned Fourier-or-fourfold witnesses and sharpens joint witness incompatibility; active parent frontier and V03 gate remain unchanged')
    raise SystemExit(bool(e))
