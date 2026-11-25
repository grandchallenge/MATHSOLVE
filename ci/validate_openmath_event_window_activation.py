#!/usr/bin/env python3
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def validate(root=ROOT):
    errors=[]
    activation=json.loads((root/'handoffs/OPENMATH-2026/event-window/ACTIVATION.json').read_text())
    registry=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
    contract=json.loads((root/'.gcl/campaigns/OPENMATH-2026/LIFECYCLE_CONTRACT.json').read_text())
    receipt=json.loads((root/'work_packages/OPENMATH_2026/EVENT_WINDOW_TERMINAL_RECEIPT.json').read_text())
    if activation.get('state')!='TERMINALIZED_RESEARCH_RESET': errors.append('event window not terminalized')
    term=activation.get('terminalization',{})
    if term.get('official_submissions')!=0 or term.get('official_acceptances')!=0: errors.append('terminal competition result drift')
    if contract.get('successor_policy',{}).get('mode')!='FRONTIER_GATE_REQUIRED': errors.append('frontier gate not required')
    if contract.get('successor_policy',{}).get('automatic_replay_successor') is not False: errors.append('automatic replay successor still enabled')
    scripts=list(registry.get('launch_contract',{}).get('current_scripts',{}).values())+list(registry.get('launch_contract',{}).get('support_scripts',{}).values())
    if len(scripts)!=9: errors.append('nine historical launch slots required')
    if any(x.get('executable') is not False for x in scripts): errors.append('terminal event window exposes executable task')
    summary=registry.get('mathematics_release_policy',{}).get('summary',{})
    if summary.get('leased_not_launched_agents')!=0 or summary.get('launched_agents')!=0: errors.append('terminal event window retains active leases')
    if receipt.get('official_submissions')!=0 or receipt.get('official_acceptances')!=0: errors.append('terminal receipt result drift')
    if receipt.get('promoted_campaign')!='GCL-ERDOS3': errors.append('H7 promotion missing')
    return errors

if __name__=='__main__':
    e=validate()
    for x in e: print('FAIL:',x)
    if not e: print('PASS: OPENMATH event window terminal; research corpus preserved; automatic replay successors disabled')
    raise SystemExit(bool(e))
