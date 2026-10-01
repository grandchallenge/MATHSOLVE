#!/usr/bin/env python3
from __future__ import annotations
import hashlib,json,re,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def validate(root=ROOT):
 errors=[]
 activation=json.loads((root/'handoffs/OPENMATH-2026/event-window/ACTIVATION.json').read_text())
 registry=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
 items={x['assignment_id']:x for x in registry['assignments']}
 rows=activation['assignments']
 for key in ('assignment_id','dispatch_id','agent_ref','issue_number'):
  if len({r[key] for r in rows})!=9: errors.append(f'nine distinct {key} required')
 if len(rows)!=9: errors.append('nine task roster mismatch')
 if activation['state']!='PINNED_READY_AFTER_PROTECTED_MERGE':errors.append('activation not pinned')
 for r in rows:
  a=items.get(r['assignment_id'],{})
  d=json.loads((root/r['dispatch_path']).read_text()); op=json.loads((root/r['operation_path']).read_text())
  for key in ('assignment_id','dispatch_id','agent_ref'):
   av=a.get('assignment_id') if key=='assignment_id' else a.get('lease',{}).get(key)
   if av!=r[key] or d.get(key)!=r[key] or op.get(key)!=r[key]:errors.append(f'{r["packet"]}: identity drift {key}')
  if d['github_issue_url']!=r['issue_url'] or op['github_issue_url']!=r['issue_url']: errors.append(f'{r["packet"]}: return issue drift')
  for rel,key in ((r['bootstrap_path'],'bootstrap_blob_sha1'),(r['launch_path'],'task_blob_sha1')):
   b=(root/rel).read_bytes();sha=hashlib.sha1(f'blob {len(b)}\0'.encode()+b).hexdigest()
   if sha!=r[key]:errors.append(f'{r["packet"]}: content hash drift')
  if hashlib.sha256((root/r['launch_path']).read_bytes()).hexdigest()!=r['task_sha256']: errors.append(f'{r["packet"]}: task SHA-256 drift')
  expected=f'https://github.com/grandchallenge/MATHSOLVE/blob/{activation["content_commit"]}/{r["launch_path"]}'
  if r['task_url']!=expected or not re.fullmatch('[0-9a-f]{40}',r.get('content_commit','')): errors.append(f'{r["packet"]}: immutable pin drift')
  if a['lease']['execution_authorized'] and a['lease']['state']!='LEASED':errors.append(f'{r["packet"]}: closed lease executable')
  if not d.get('protected_lease_required'):errors.append(f'{r["packet"]}: missing protected lease gate')
 for r in activation['retired']:
  a=items[r['assignment_id']]
  if a['state']!='SUPERSEDED' or a['lease']['execution_authorized'] or not a['lifecycle']['closed']:errors.append('retired assignment executable')
  d=json.loads((root/a['dispatch_record']).read_text())
  if d['dispatch_status']!='RETIRED_SUPERSEDED':errors.append('retired dispatch accepts returns')
 if registry.get('event_window_priority')!=['OM26-H1','OM26-H7','OM26-H4','OM26-H3','OM26-H6','OM26-H5','OM26-H2']:errors.append('priority drift')
 return errors
if __name__=='__main__':
 e=validate()
 for x in e:print('FAIL:',x)
 if not e:print('PASS: nine distinct immutable mathematical tasks, return bindings, and retired leases')
 raise SystemExit(bool(e))
