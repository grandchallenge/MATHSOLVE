"""Check custody, actual replay output and non-certifying review boundaries."""
import hashlib,json,re
from pathlib import Path
ROOT=Path(__file__).resolve().parent
receipt=json.loads((ROOT/'REPLAY_RECEIPT.json').read_text(encoding='utf-8'))
assert receipt['source']['commit']=='5dcb6e4906df03f2e4294b21be73b55db7736f5a'
assert receipt['source']['mathlib']=='8f9d9cff6bd728b17a24e163c9402775d9e6a365'
assert receipt['source']['lean']=='4.28.0'
seen=set()
for row in receipt['files']:
    p=(ROOT/row['path']).resolve()
    assert p.is_relative_to(ROOT.resolve()) and row['path'] not in seen
    seen.add(row['path'])
    assert hashlib.sha256(p.read_bytes()).hexdigest()==row['sha256'],row['path']
assert {'CLAIM_LEDGER.json','PROOF_OBLIGATIONS.json','593_REVIEW_HANDOFF.md','SourceTargetBridge.lean'}<=seen
assert 'Build completed successfully (8091 jobs).' in (ROOT/'593-build-resumed.log').read_text(encoding='utf-8')
standard={'propext','Classical.choice','Quot.sound'}
for file,count in [('593-axioms.log',17),('593-fidelity-lean.log',2),('593-finite-axioms-428-v2.log',6),('593-source-target-bridge.log',4)]:
    text=(ROOT/file).read_text(encoding='utf-8')
    rows=re.findall(r"'([^']+)' depends on axioms: \[([^\]]*)\]",text)
    assert len(rows)==count and 'error:' not in text and 'sorryAx' not in text,file
    for name,axioms in rows:
        assert set(s.strip() for s in axioms.split(',') if s.strip())<=standard,name
assert (ROOT/'593-source-target-bridge.log').read_text(encoding='utf-8').rstrip().endswith('BRIDGE_PASS')
snapshot=(ROOT/'ProtectedSnapshot-original.lean.txt').read_bytes()
assert hashlib.sha1(b'blob '+str(len(snapshot)).encode()+b'\0'+snapshot).hexdigest()=='8a247f7a4ac1b466513c04a40dcf26b90332faeb'
text=snapshot.decode('utf-8')
body=text[text.index('open Cardinal Set'):].rstrip()
assert body.endswith('\nend')
body=body[:-len('\nend')]
expected=text[:text.index('module\n')]+'import RequestProject.PublicationCertificate\n\nnamespace ProtectedSnapshot\n\n'+body+'\n\nend ProtectedSnapshot\n'
assert (ROOT/'ProtectedInterface.lean').read_text(encoding='utf-8')==expected
assert receipt['route']['registered_erdos_route'] is None
routes=json.loads((ROOT/'mathcert-routes-snapshot.json').read_text(encoding='utf-8'))['routes']
assert not any(r['campaign_id'].startswith('ERDOS') or any('593' in c for c in r['target_claim_ids']) for r in routes)
assert receipt['route']['submission_status']=='NOT_SUBMITTED_ROUTE_ADMISSION_REQUIRED'
assert receipt['authority_effects']['mathematical_certification'] is False
assert receipt['authority_effects']['independent_semantic_review'] is False
assert all(c['claim_promotion'] is False for c in json.loads((ROOT/'CLAIM_LEDGER.json').read_text(encoding='utf-8'))['claims'])
print('PASS: exact replay evidence, protected definition copy, standard axioms, pending route/review boundaries')
