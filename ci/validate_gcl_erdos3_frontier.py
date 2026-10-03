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
    if campaign.get('campaign_id')!='GCL-ERDOS3' or campaign.get('status')!='ACTIVE__RESEARCH_RESET':
        errors.append('campaign identity/status drift')
    if gate.get('next_residual_role')!='EVIDENCE_ONLY_NOT_SCHEDULING_AUTHORITY':
        errors.append('Next residual regained scheduling authority')
    if gate.get('default_independent_replay_budget')!=1:
        errors.append('verification budget drift')
    if gate.get('constraints',{}).get('closed_or_exhausted_node_forbids_equivalent_replay_successor') is not True:
        errors.append('replay recursion guard disabled')
    ids={x.get('id') for x in frontier.get('nodes',[])}
    required={'E3-ROOT','E3-C-D3','E3-C-D4','E3-F-D5','E3-B-SCALE-LOCAL','E3-B-AP'}
    if not required <= ids:
        errors.append('frontier node set incomplete')
    if frontier.get('active_frontier')!=['E3-F-D5','E3-B-SCALE-LOCAL']:
        errors.append('active frontier drift')
    for row in prov.get('artifacts',[]):
        p=root/row['path']
        if not p.is_file() or blob(p)!=row['git_blob_sha1']:
            errors.append(f"provenance drift: {row['path']}")
    for wp in campaign.get('initial_work_packages',[]):
        if not (root/f'work_packages/GCL_ERDOS3/work_packages/{wp}.md').is_file():
            errors.append(f'missing {wp}')
    return errors

if __name__=='__main__':
    e=validate()
    for x in e: print('FAIL:',x)
    if not e: print('PASS: GCL-ERDOS3 frontier reset is coherent')
    raise SystemExit(bool(e))
