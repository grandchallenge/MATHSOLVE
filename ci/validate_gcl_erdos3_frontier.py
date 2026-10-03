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

    if campaign.get('campaign_id')!='GCL-ERDOS3' or campaign.get('status')!='ACTIVE__TRANCHE_E3_01':
        errors.append('campaign identity/status drift')
    if gate.get('next_residual_role')!='EVIDENCE_ONLY_NOT_SCHEDULING_AUTHORITY':
        errors.append('Next residual regained scheduling authority')
    if gate.get('default_independent_replay_budget')!=1:
        errors.append('verification budget drift')
    if gate.get('constraints',{}).get('closed_or_exhausted_node_forbids_equivalent_replay_successor') is not True:
        errors.append('replay recursion guard disabled')

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
    if rows.get('E3-V-B01',{}).get('status')!='OPEN':
        errors.append('B01 independent verification node not open')
    if rows.get('E3-B-AP',{}).get('status')!='OPEN':
        errors.append('parent AP bridge incorrectly closed')
    if frontier.get('active_frontier')!=['E3-V-B01','E3-B-AP']:
        errors.append('active frontier drift')

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
        errors.append('B01 frontier action drift')
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
    ]
    for path in required_files:
        if not (root/path).is_file():
            errors.append(f'missing {path}')

    for wp in campaign.get('initial_work_packages',[]):
        if not (root/f'work_packages/GCL_ERDOS3/work_packages/{wp}.md').is_file():
            errors.append(f'missing {wp}')
    return errors

if __name__=='__main__':
    e=validate()
    for x in e: print('FAIL:',x)
    if not e: print('PASS: GCL-ERDOS3 E3 tranche is coherent; F01 closed and B01 advanced to one independent verification plus k>=4 frontier')
    raise SystemExit(bool(e))
