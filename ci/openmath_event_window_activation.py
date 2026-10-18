#!/usr/bin/env python3
"""Register the bounded event-window packets through existing CEX contracts.

No network or protected-branch writes. Issue creation and protected merge are
owned by the authenticated caller. Content is committed before pin() runs.
"""
from __future__ import annotations
import argparse, copy, hashlib, json, re
from pathlib import Path
from ci.openmath_lifecycle_candidate import REGISTRY, LANES, BOARD, INDEX, board_text, index_text, refresh_summary, dump, blob_sha1

ROOT=Path(__file__).resolve().parents[1]
PACKETS=Path('handoffs/OPENMATH-2026/event-window')
ACTIVATION=PACKETS/'ACTIVATION.json'
SPECS=[
 ('H1-PREMISES','OM26-H1-WP03','PRIMARY'),
 ('H1-Q6','OM26-H1-WP30','SUPPORT'),
 ('H1-ADVERSARY','OM26-H1-WP60','SUPPORT'),
 ('H7-DIVERGENCE','OM26-H7-WP04','PRIMARY'),
 ('H4-EXTEND','OM26-H4-WP03','PRIMARY'),
 ('H3-DELTA','OM26-H3-WP04','PRIMARY'),
 ('H6-OFFENSIVE','OM26-H6-WP04','PRIMARY'),
 ('H5-ELIGIBILITY','OM26-H5-WP03','PRIMARY'),
 ('H2-GATE','OM26-H2-WP05','PRIMARY'),
]
DISPOSITIONS=['PROVED_REDUCTION','EXACT_CERTIFICATE','FORMAL_LEMMA_PROVED','COUNTEREXAMPLE','NO_MATERIAL_DELTA','EXACT_BLOCKER']

def identity(assignment):
 m=re.fullmatch(r'OM26-H([1-7])-WP([0-9]{2})',assignment)
 if not m: raise ValueError('invalid assignment')
 h,w=map(int,m.groups())
 return f'OM26-H{h}',f'{assignment}-IA-001',f'INDEPENDENT-AGENT-{h*100+w:03d}'

def bootstrap(root,packet,assignment,role):
 hill,dispatch,agent=identity(assignment)
 template=(root/PACKETS/f'{packet}.md').read_text()
 template=re.sub(r'## Activation and durable return\n.*?(?=## Pinned inputs)', '', template, flags=re.S)
 template=re.sub(r'## Required protected return\n.*?(?=## Section 8 update obligation)', '',template,flags=re.S)
 header=f'''GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: {dispatch}
agent_ref: {agent}
campaign: OPENMATH-2026
hill: {hill}
assignment: {assignment}
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1

'''
 contract=f'''\n## Execution and independence

This is the {role.lower()} assignment for packet {packet}. The primary seven-hill topology remains unchanged; supporting H1 assignments have distinct leases and return locks. Execute this bounded packet only. Authenticated GitHub commenting capability in your environment is required before substantive work. No GCL-specific credential, membership or repository-write permission is needed. If transport is unavailable, report RETURN_TRANSPORT_UNAVAILABLE and stop. No human evidence shuttling is required.

For H1-ADVERSARY, use a reasoning session that has not authored the proofs under review. A shared model or account does not establish independent authorship; declare actual provenance. Do not claim independent certification.

## Complete result grammar

Post one narrative-only RESULT/1 inside the launch envelope. No URLs, attachments or Markdown links in the INNER result. Include complete source code/proof/certificate inline, within GitHub's comment limit; if too large, return the smallest independently replayable bounded contribution rather than truncate evidence. Use only the listed dispositions. NO_MATERIAL_DELTA recommends HOLD and does not invent a positive contribution. Next residual has at most three sentences. Event-window UTC times, exact hashes and prior-work comparison belong inside the six required sections; do not add level-two headings.

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: {dispatch}
agent_ref: {agent}
assignment: {assignment}
disposition: <{'|'.join(DISPOSITIONS)}>
context_class: ZERO_CONTEXT
external_sources: <PROTECTED_PACKET_ONLY|ADDITIONAL_PUBLIC_SOURCES>
timebox_observed: <YES|NO>

## Strongest exact statement
<Exact statement, domain, disposition and event-window UTC timestamps.>

## Derivation
<Complete argument or certificate and code; prior-work/novelty comparison.>

## Assumptions beyond bootstrap
<Every assumption, source and independence limitation.>

## Verification / falsification hooks
<Exact commands, outputs, source hashes, and independent replay/formal-check evidence.>

## Claim boundary
<What this establishes; unresolved hypotheses; no certification or official score.>

## Next residual
<At most three sentences; include HOLD recommendation if warranted.>
```

Structural intake preserves evidence only. Mathematical replay, novelty review and Section 8 claim updates remain distinct and must precede promotion. The controller records a Section 8 evidence-review item immediately; it never converts a declared disposition into a theorem.
'''
 return header+template+contract

def prepare_issues(root):
 return [{'packet':p,'assignment_id':a,'lane_role':role,'title':f'[GCL-CONTRIB] OPENMATH-2026 {identity(a)[1]} — {p}', 'body':bootstrap(root,p,a,role)} for p,a,role in SPECS]

def apply(root,issues):
 registry=json.loads((root/REGISTRY).read_text()); lanes=json.loads((root/LANES).read_text())
 byid={x['assignment_id']:x for x in registry['assignments']}
 issue_by={x['packet']:x for x in issues}
 if set(issue_by)!={p for p,_,_ in SPECS}: raise ValueError('issue roster mismatch')
 if any(a in byid for _,a,_ in SPECS): raise ValueError('already registered; recover pinned state instead')
 registry['launch_contract'].setdefault('support_scripts',{})
 records=[]; retired=[]
 old_per=copy.deepcopy(registry['mathematics_release_policy']['per_hill'])
 for packet,assignment,role in SPECS:
  hill,dispatch,agent=identity(assignment); issue=issue_by[packet]
  number=issue['number']; url=f'https://github.com/grandchallenge/MATHSOLVE/issues/{number}'
  if issue['body']!=bootstrap(root,packet,assignment,role): raise ValueError('issue/bootstrap byte drift')
  predecessor=byid[old_per[hill]['assignment']]
  if role=='PRIMARY':
   if predecessor['state']!='LEASED_NOT_LAUNCHED' or predecessor['lifecycle']['launched']: raise ValueError('old lease already executed; reconcile before retirement')
   predecessor.update(state='SUPERSEDED',superseded_by=assignment,supersession_reason='Event-window mathematical target replaces completed replay-only task')
   predecessor['lease'].update(state='SUPERSEDED',execution_authorized=False)
   predecessor['lifecycle'].update(closed=True,pipeline_state='SUPERSEDED')
   old_dispatch=root/predecessor['dispatch_record']
   d=json.loads(old_dispatch.read_text()); d['dispatch_status']='RETIRED_SUPERSEDED'; dump(old_dispatch,d)
   retired.append({'assignment_id':predecessor['assignment_id'],'return_issue':predecessor['lease']['return_url'],'superseded_by':assignment,'launched':False})
  bootstrap_path=f'handoffs/OPENMATH-2026/jobs/{dispatch}.md'; launch_path=f'handoffs/OPENMATH-2026/launch/{assignment}.md'
  op_path=f'.gcl/operations/{dispatch}/OPERATION.json'; dispatch_path=f'contributions/OPENMATH-2026/{hill}/{assignment.rsplit("-",1)[1]}/dispatches/{dispatch}.json'
  body=issue['body']; (root/bootstrap_path).write_text(body)
  launch=f'''GCL-ZERO-CONTEXT-LAUNCH/2
CAMPAIGN: OPENMATH-2026
HILL: {hill}
ASSIGNMENT_ID: {assignment}
DISPATCH_ID: {dispatch}
AGENT_REF: {agent}
PROTECTED_LEASE_IDENTITY: {assignment} :: {dispatch} :: {agent}
INTENDED_RETURN: {url}
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
COMPETITION_SUBMISSION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

{body}

## Embedded protected source snapshots

All required source identities and commit-pinned inputs are listed in the bounded task above. Read only those explicit sources; do not discover a different assignment. This artifact supplies the complete identity, mathematical scope, acceptance criteria, result grammar and return route. A source fetch failure is an execution blocker, not mathematical evidence.

## Exact return envelope

Before substantive work, confirm available authenticated GitHub comment transport in your environment. Post this complete envelope as one comment to INTENDED_RETURN. An explicitly authorized environment relay may post on your behalf and must return the durable comment URL. No private-chat-only result or manual Human Steward forwarding satisfies this contract.

```text
GCL-RETURN-RELAY/1
DISPATCH_ID: {dispatch}
AGENT_REF: {agent}
INTENDED_RETURN: {url}

BEGIN_RESULT
<complete inner GCL-CONTRIBUTION-RESULT/1 verbatim>
END_RESULT
```

Authenticated GCL infrastructure owns durable GitHub intake.
'''
  (root/launch_path).write_text(launch)
  prereq=copy.deepcopy(predecessor['prerequisites'])
  # Preserve accepted ancestry; retirement is not an invented accepted result.
  prereq['supersedes_assignment']=predecessor['assignment_id']; prereq['solve_release']=True
  item=copy.deepcopy(predecessor)
  for key in ('superseded_by','supersession_reason'): item.pop(key,None)
  item.update(assignment_id=assignment,obligation=assignment.rsplit('-',1)[1],state='LEASED_NOT_LAUNCHED',priority=f'P{["H1","H7","H4","H3","H6","H5","H2"].index(hill[5:])}',lane_role=role,support_slot=packet if role=='SUPPORT' else None,packet_id=packet,work_package=bootstrap_path,work_package_url='PENDING_CONTENT_COMMIT',operation_contract=op_path,source_work_package=bootstrap_path,dispatch_record=dispatch_path,prerequisites=prereq,completion=DISPOSITIONS,successor_gate='Protected event-window release; no mathematics promoted')
  item['lease']={'state':'LEASED','dispatch_id':dispatch,'agent_ref':agent,'dispatch_issue_number':number,'protected_lease_commit':'PENDING_CONTENT_COMMIT','dispatch_url':url,'return_url':url,'readback_verified':False,'execution_authorized':True,'activation_condition':'PROTECTED_MERGE_OF_EVENT_WINDOW_ACTIVATION'}
  item['lifecycle']={'prepared':True,'leased':True,'launched':False,'launch_receipt':None,'returned':False,'captured':False,'replayed':False,'adjudication':'NOT_STARTED','pipeline_state':'READY','certification':'NOT_ELIGIBLE','closed':False}
  registry['assignments'].append(item)
  script={'path':launch_path,'executable':True,'assignment_id':assignment,'dispatch_id':dispatch,'agent_ref':agent,'intended_return':url,'task_commit':'PENDING_CONTENT_COMMIT','task_blob_sha1':blob_sha1(launch),'task_url':'PENDING_CONTENT_COMMIT','lane_role':role}
  if role=='PRIMARY':
   policy=registry['mathematics_release_policy']['per_hill'][hill]
   policy.update(assignment=assignment,agent_state='LEASED_NOT_LAUNCHED',closed=False,superseded_assignment=predecessor['assignment_id'])
   registry['launch_contract']['current_scripts'][hill]=script
   lane=next(x for x in lanes['hills'] if x['hill_slot']==hill)
   lane['active_lease']={'assignment_id':assignment,'dispatch_id':dispatch,'agent_ref':agent,'issue_url':url,'protected_merge':'PENDING_CONTENT_COMMIT','readback_verified':False,'lifecycle_state':'LEASED_NOT_LAUNCHED','launch_evidence':None,'return_evidence':None}
   lane['status']='EVENT_WINDOW_MATHEMATICAL_TASK_READY'; lane['next_action']=f'Execute {packet} from the registered immutable task; retain priority order.'
  else:
   registry['launch_contract']['support_scripts'][packet]=script
   next(x for x in lanes['hills'] if x['hill_slot']==hill).setdefault('supporting_leases',{})[packet]={'assignment_id':assignment,'dispatch_id':dispatch,'agent_ref':agent,'issue_url':url,'protected_merge':'PENDING_CONTENT_COMMIT','readback_verified':False,'lifecycle_state':'LEASED_NOT_LAUNCHED','launch_evidence':None,'return_evidence':None}
  operation={'schema_version':'1.0.0','record_type':'GCL_OPERATION_CONTRACT','operation':dispatch,'campaign':'OPENMATH-2026','hill':hill,'assignment_id':assignment,'dispatch_id':dispatch,'agent_ref':agent,'objective':packet,'acceptable_dispositions':DISPOSITIONS,'return_protocol':'GCL-CONTRIBUTION-RESULT/1','github_issue_number':number,'github_issue_url':url,'canonical_mutation_authorized':False,'lane_role':role}
  d={'schema_version':'1.0.0','record_type':'GCL_EXTERNAL_DISPATCH','dispatch_id':dispatch,'campaign':'OPENMATH-2026','hill':hill,'assignment_id':assignment,'agent_ref':agent,'concurrency_mode':'independent_blind','bootstrap_path':bootstrap_path,'bootstrap_blob_sha1':blob_sha1(body),'source_handoff_commit_sha':'PENDING_CONTENT_COMMIT','return_protocol':'GCL-CONTRIBUTION-RESULT/1','github_issue_number':number,'github_issue_url':url,'github_issue_title':issue['title'],'canonical_mutation_authorized':False,'dispatch_status':'READY_FOR_GITHUB_COMMENT','operation_contract':op_path,'protected_lease_required':True}
  dump(root/op_path,operation); dump(root/dispatch_path,d)
  records.append({'packet':packet,'assignment_id':assignment,'dispatch_id':dispatch,'agent_ref':agent,'lane_role':role,'support_slot':item['support_slot'],'issue_number':number,'issue_url':url,'bootstrap_path':bootstrap_path,'launch_path':launch_path,'operation_path':op_path,'dispatch_path':dispatch_path,'bootstrap_blob_sha1':blob_sha1(body),'task_blob_sha1':blob_sha1(launch),'task_sha256':hashlib.sha256(launch.encode()).hexdigest()})
 registry['event_window_priority']=['OM26-H1','OM26-H7','OM26-H4','OM26-H3','OM26-H6','OM26-H5','OM26-H2']
 registry['claim_boundary']='Seven peer hill lanes, with separately leased supporting H1 tasks. Task readiness is not launch, mathematical acceptance, novelty, certification or competition submission.'
 refresh_summary(registry)
 dump(root/REGISTRY,registry); dump(root/LANES,lanes)
 dump(root/ACTIVATION,{'record_type':'OPENMATH_EVENT_WINDOW_ACTIVATION','state':'CONTENT_CREATED_PENDING_IMMUTABLE_PIN','source_head':'36b7c79bebd42fde17ea9f0f809406fb55e093f9','prepared_packet_commit':'23f49a75550ce130d83ecd09ae3120c82d3ca05d','retired':retired,'assignments':records,'claim_effect':'NONE','worker_launches':0})
 (root/BOARD).write_text(board_text(registry)); (root/INDEX).write_text(index_text(registry))
 return records

def pin(root,commit):
 if not re.fullmatch('[0-9a-f]{40}',commit): raise ValueError('exact content commit required')
 registry=json.loads((root/REGISTRY).read_text()); lanes=json.loads((root/LANES).read_text()); activation=json.loads((root/ACTIVATION).read_text())
 for row in activation['assignments']:
  item=next(x for x in registry['assignments'] if x['assignment_id']==row['assignment_id'])
  script=(registry['launch_contract']['current_scripts'][item['hill']] if row['lane_role']=='PRIMARY' else registry['launch_contract']['support_scripts'][row['support_slot']])
  script.update(task_commit=commit,task_url=f'https://github.com/grandchallenge/MATHSOLVE/blob/{commit}/{row["launch_path"]}')
  item['lease']['protected_lease_commit']=commit; item['work_package_url']=f'https://github.com/grandchallenge/MATHSOLVE/blob/{commit}/{row["bootstrap_path"]}'
  d=json.loads((root/row['dispatch_path']).read_text()); d['source_handoff_commit_sha']=commit; dump(root/row['dispatch_path'],d)
  row['task_url']=script['task_url']; row['content_commit']=commit
  lane=next(x for x in lanes['hills'] if x['hill_slot']==item['hill'])
  if row['lane_role']=='PRIMARY': lane['active_lease']['protected_merge']=commit
  else: lane['supporting_leases'][row['support_slot']]['protected_merge']=commit
 activation.update(state='PINNED_READY_AFTER_PROTECTED_MERGE',content_commit=commit)
 dump(root/REGISTRY,registry); dump(root/LANES,lanes); dump(root/ACTIVATION,activation)
 (root/BOARD).write_text(board_text(registry)); (root/INDEX).write_text(index_text(registry))
 lines=['# Event-window agent tasks','', 'Priority: H1 → H7 → H4 → H3 → H6 → H5 → H2. Organizer-route blockage is external.','', 'The following distinct assignments are executable after the protected activation merge. No worker has been launched. Ordinary authenticated GitHub commenting in the participant environment is required; no GCL-specific permission or human forwarding is needed.','', '| Packet | Immutable task | Return |','|---|---|---|']
 for r in activation['assignments']: lines.append(f'| {r["packet"]} | [Read task]({r["task_url"]}) | [#{r["issue_number"]}]({r["issue_url"]}) |')
 lines.extend(['','H1-PREMISES is the primary H1 task; H1-Q6 and H1-ADVERSARY are separately leased supporting tasks. Supporting returns retain their own successor chains and never replace the primary lane. H7 is the parallel formal lane. Lower-priority readiness does not instruct all hills to consume compute.','', 'The original packet manifest is historical preparation evidence. ACTIVATION.json and the protected CEX registry allocate current execution. Existing replay-only leases were retired without inventing returns or changing accepted history.','', 'Intake records every valid return in the Section 8 evidence-review queue. Mathematical claims are updated only after exact replay/formal checking and novelty review.'])
 (root/PACKETS/'README.md').write_text('\n'.join(lines)+'\n')

if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('action',choices=['issues','apply','pin']);p.add_argument('--issues');p.add_argument('--commit');a=p.parse_args()
 if a.action=='issues': print(json.dumps(prepare_issues(ROOT)))
 elif a.action=='apply': apply(ROOT,json.loads(Path(a.issues).read_text()))
 else: pin(ROOT,a.commit)
