#!/usr/bin/env python3
from __future__ import annotations
import json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
HEX40=re.compile(r'^[0-9a-f]{40}$')

def fail(msg): raise SystemExit('GCL completion receipt v2: FAIL: '+msg)
def req(ok,msg):
    if not ok: fail(msg)
def load(p): return json.loads((ROOT/p).read_text())

def main():
    if len(sys.argv)!=2: fail('usage: gcl_completion_receipt_validate_v2.py OPERATION')
    opid=sys.argv[1]
    op=load(f'.gcl/operations/{opid}/OPERATION.json')
    state=load(f'.gcl/campaigns/{op["campaign"]}/CAMPAIGN_STATE.json')
    r=load(op['completion_receipt']['surface'])
    req(r.get('record_type')=='GCL_COMPLETION_RECEIPT','record_type')
    req(r.get('campaign')==op['campaign'] and r.get('operation')==opid,'identity')
    cand=r.get('candidate_head',''); merge=r.get('merge_sha',''); read=r.get('protected_readback_sha','')
    req(bool(HEX40.match(cand)),'candidate head')
    req(bool(HEX40.match(merge)) and merge==read,'merge/readback')
    adv=r['adversary_record']; ref=r['referee_record']
    req(adv.get('role')=='Adversary' and ref.get('role')=='Referee','review roles')
    req(adv.get('mode')==ref.get('mode')=='non_authoring_read_only','review mode')
    req(adv.get('reviewed_candidate_head')==ref.get('reviewed_candidate_head')==cand,'review subject')
    req(adv.get('logical_pass_id')!=ref.get('logical_pass_id'),'logical pass separation')
    req(adv.get('record_ref')!=ref.get('record_ref'),'review record separation')
    req(adv.get('finding')==ref.get('finding')=='approved','review findings')
    req(not adv.get('unresolved_obligations') and not ref.get('unresolved_obligations'),'unresolved review obligation')
    checks=r.get('required_checks',[]); req(bool(checks),'checks missing')
    for c in checks:
        req(c.get('result')=='success','non-success check')
        phase=c.get('phase'); req(phase in {'candidate','protected_readback'},'check phase')
        req(c.get('head')==(cand if phase=='candidate' else merge),'stale check head')
        req('run' in c or 'check_run' in c,'check identity')

    d=r['disposition']
    dtype=d.get('type')
    req(dtype==op['candidate_disposition'],'disposition type')
    objective=op.get('objective',{})
    successor=op.get('successor_policy',{})

    if dtype=='CLOSED':
        expected_frontier=objective.get('retire_frontier',objective.get('frontier'))
        expected_next=successor.get('next_frontier_if_closed')
        if expected_next is None:
            expected_next=state.get('candidate_disposition',{}).get('next_frontier_if_protected')
        req(bool(expected_frontier),'closed frontier contract')
        req(bool(expected_next),'closed successor contract')
        req(d.get('frontier')==expected_frontier,'frontier')
        req(d.get('next_frontier')==expected_next,'next frontier')
    elif dtype=='BLOCKED':
        expected_frontier=objective.get('frontier',objective.get('retire_frontier'))
        blocked=op.get('blocked_on') or state.get('candidate_disposition',{}).get('blocked_on')
        req(bool(expected_frontier),'blocked frontier contract')
        req(bool(blocked),'blocked theorem contract')
        req(d.get('frontier')==expected_frontier,'frontier')
        req(d.get('blocked_on')==blocked,'blocked theorem')
        req(d.get('next_frontier')==blocked,'next frontier')
        state_disp=state.get('candidate_disposition',{})
        if state.get('current_operation')==opid:
            req(state_disp.get('type')=='BLOCKED','campaign blocked disposition')
            req(state_disp.get('blocked_on')==blocked,'campaign blocked theorem')
    elif dtype=='FALSIFIED':
        expected_frontier=objective.get('frontier',objective.get('retire_frontier'))
        expected_next=successor.get('next_frontier_if_falsified')
        req(bool(expected_frontier),'falsified frontier contract')
        req(d.get('frontier')==expected_frontier,'frontier')
        if expected_next is not None:
            req(d.get('next_frontier')==expected_next,'next frontier')
    else:
        fail('unsupported disposition type')

    expected={k for k,v in op['claim_firewall'].items() if v is False}
    req(expected.issubset(set(r.get('preserved_false',[]))),'preserved false firewall')
    for review in (adv,ref):
        req(not any(bool(v) for v in review.get('authority_claims',{}).values()),'review manufactured authority')
    print(json.dumps({'status':'PASS','operation':opid,'candidate_head':cand,'protected_readback':merge,'disposition':dtype,'next_frontier':d.get('next_frontier'),'mathcert_certified':False},sort_keys=True))
if __name__=='__main__': main()
