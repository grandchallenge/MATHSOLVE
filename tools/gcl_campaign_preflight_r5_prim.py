#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def fail(msg):
    raise SystemExit('GCL BSD-R5-PRIM preflight: FAIL: '+msg)

def load(rel):
    p=ROOT/rel
    if not p.exists(): fail('missing '+rel)
    return json.loads(p.read_text())

def blob(rel):
    data=(ROOT/rel).read_bytes()
    return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()

def main():
    if len(sys.argv)!=3 or sys.argv[1:]!=['BSD-001','BSD-R5-PRIM']:
        fail('expected BSD-001 BSD-R5-PRIM')
    state=load('.gcl/campaigns/BSD-001/CAMPAIGN_STATE.json')
    op=load('.gcl/operations/BSD-R5-PRIM/OPERATION.json')
    fr=load('.gcl/admission/BSD-R5-PRIM/FREEZE.json')
    if state['current_operation']!='BSD-R5-PRIM' or op['operation']!='BSD-R5-PRIM':
        fail('operation mismatch')
    if state['current_frontier']['id']!=op['objective']['retire_frontier']:
        fail('frontier mismatch')
    if not state['protected_inputs']['math_base'].endswith(op['protected_base']):
        fail('base mismatch')
    if not state['protected_inputs']['provider'].endswith(op['provider_anchor']):
        fail('provider mismatch')
    if not state['authority']['constitution'].endswith(op['constitutional_anchor']):
        fail('constitution mismatch')
    if state['execution_standard']['staffing_directive']!=op['staffing_directive']:
        fail('staffing directive mismatch')
    if state['candidate_disposition']['type']!=op['candidate_disposition']:
        fail('candidate disposition mismatch')
    if state['candidate_disposition']['next_frontier_if_protected']!=op['successor_policy']['next_frontier_if_blocked']:
        fail('successor mismatch')
    if state['cold_start']['completion_receipt_surface']!=op['completion_receipt']['surface']:
        fail('completion receipt surface mismatch')
    if fr['protected_base']!=op['protected_base']:
        fail('freeze base mismatch')
    ledger=(ROOT/op['validation']['claim_ledger']).read_text()
    theorem=(ROOT/op['validation']['theorem']).read_text()
    frontier=(ROOT/op['validation']['frontier_record']).read_text()
    combined='\n'.join((ledger,theorem,frontier))
    for t in op['validation']['required_tokens']:
        if t not in combined: fail('missing token '+t)
    for t in op['validation']['forbidden_tokens']:
        if t in ledger: fail('forbidden token '+t)
    for k,v in op['claim_firewall'].items():
        if v is False and f'{k}: false' not in ledger:
            fail('firewall '+k)
    routing=load(op['validation']['routing_registry'])
    if op['validation']['workflow'] not in {x.get('path') for x in routing['workflows']}:
        fail('workflow not routed')
    if not (ROOT/op['validation']['workflow']).exists():
        fail('workflow missing')
    frozen=fr['artifacts']; governed=op['governed_artifacts']
    if set(frozen)!=set(governed): fail('freeze set mismatch')
    for rel in governed:
        if not (ROOT/rel).exists(): fail('missing '+rel)
        if blob(rel)!=frozen[rel]: fail('freeze mismatch '+rel)
    print(json.dumps({
        'status':'PASS',
        'campaign':'BSD-001',
        'operation':'BSD-R5-PRIM',
        'candidate_disposition':'BLOCKED',
        'next_frontier':'MISSING_P2_KATO_KOLYVAGIN_PRIMITIVITY_INDEX_EQUALITY',
        'frozen_artifacts':len(governed),
        'r5_prim':False,
        'bsd_r2_a1':False,
        'mathcert_certified':False
    },sort_keys=True))

if __name__=='__main__':
    main()
