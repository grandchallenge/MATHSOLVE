import copy,json,shutil,tempfile,unittest
from pathlib import Path
from ci.openmath_cex_github_contribution_intake import emit_intake, IntakeError
from ci.openmath_lifecycle_candidate import apply_candidate,finalize_pin
from ci.validate_openmath_event_window_activation import ROOT,validate

class EventWindowActivationTests(unittest.TestCase):
 def test_protected_activation_concordance(self):
  self.assertEqual(validate(),[])

 def test_all_nine_returns_advance_without_support_overwriting_primary(self):
  # Synthetic local events only. No GitHub comment, agent launch or mathematical claim.
  with tempfile.TemporaryDirectory() as td:
   root=Path(td)/'repo'
   shutil.copytree(ROOT,root,ignore=shutil.ignore_patterns('.git','__pycache__'))
   registry=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
   scripts=list(registry['launch_contract']['current_scripts'].values())+list(registry['launch_contract']['support_scripts'].values())
   queue_path=root/'work_packages/OPENMATH_2026/COMPETITION_PACKETS/SECTION8_EVIDENCE_REVIEW_QUEUE.json'
   initial_queue=json.loads(queue_path.read_text())
   initial_queue_count=len(initial_queue['items'])
   for i,s in enumerate(scripts):
    registry=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
    a=next(x for x in registry['assignments'] if x['assignment_id']==s['assignment_id'])
    d=json.loads((root/a['dispatch_record']).read_text())
    raw=f'''GCL-CONTRIBUTION-RESULT/1
dispatch_id: {d['dispatch_id']}
agent_ref: {d['agent_ref']}
assignment: {d['assignment_id']}
disposition: EXACT_BLOCKER
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
Synthetic local infrastructure fixture, no mathematical result.

## Derivation
No agent work occurred; exercise return processing only.

## Assumptions beyond bootstrap
None; this event is local and is never posted.

## Verification / falsification hooks
Run the governed local regression test.

## Claim boundary
No mathematical claim, launch, independent review or official score.

## Next residual
Independently replay real evidence after a genuine return.
'''
    envelope=f"GCL-RETURN-RELAY/1\nDISPATCH_ID: {d['dispatch_id']}\nAGENT_REF: {d['agent_ref']}\nINTENDED_RETURN: {d['github_issue_url']}\n\nBEGIN_RESULT\n{raw}\nEND_RESULT\n"
    event={'issue':{'number':d['github_issue_number'],'title':d['github_issue_title'],'body':(root/d['bootstrap_path']).read_text()},'comment':{'id':900000+i,'body':envelope,'user':{'login':'local-fixture'},'created_at':'2026-10-01T22:00:00Z'}}
    bad=copy.deepcopy(event);bad['issue']['number']+=1000
    with self.assertRaises(IntakeError):emit_intake(bad,root,Path(td)/f'bad{i}')
    before=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())['mathematics_release_policy']['per_hill']['OM26-H1']['assignment']
    intake=Path(td)/f'intake{i}';emit_intake(event,root,intake)
    manifest=apply_candidate(root,intake,999100+i,f'https://github.com/grandchallenge/MATHSOLVE/issues/{999100+i}')
    pin=finalize_pin(root,d['dispatch_id'],'a'*40)
    after=json.loads((root/'.gcl/campaigns/OPENMATH-2026/CEX_ASSIGNMENTS.json').read_text())
    self.assertEqual(manifest['pipeline'],['RETURNED','CAPTURED','REPLAYED','ADJUDICATED','ADVANCED'])
    self.assertIn('a'*40,pin['task_url'])
    if a.get('lane_role')=='SUPPORT':
     self.assertEqual(after['mathematics_release_policy']['per_hill']['OM26-H1']['assignment'],before)
     self.assertEqual(after['launch_contract']['support_scripts'][a['support_slot']]['assignment_id'],pin['successor'])
    # Same first comment can be re-observed idempotently after closure; a replacement cannot.
    emit_intake(event,root,Path(td)/f'repeat{i}')
    replacement=copy.deepcopy(event);replacement['comment']['id']+=10000
    with self.assertRaises(IntakeError):emit_intake(replacement,root,Path(td)/f'replacement{i}')
    adj=json.loads((root/manifest['programme_projection_path']).read_text())
    self.assertEqual(adj['claim_effect'],'NONE')
   queue=json.loads(queue_path.read_text())
   self.assertEqual(len(queue['items']),initial_queue_count+len(scripts))
   self.assertEqual(len({x['dispatch_id'] for x in queue['items']}),len(queue['items']))
   self.assertTrue(all(x['claim_effect']=='NONE' for x in queue['items']))

if __name__=='__main__':unittest.main()
