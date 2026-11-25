import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parent
r=json.loads((root/'PROVENANCE_RECEIPT.json').read_text(encoding='utf-8'))
for f in r['files']:
    p=(root/f['path']).resolve()
    assert p.is_relative_to(root.resolve())
    assert hashlib.sha256(p.read_bytes()).hexdigest()==f['sha256'],f['path']
assert not r['mathematical_certification'] and not r['full_search_replayed'] and not r['recovery_request_sent']
a=json.loads((root/'470-lineage-provenance-audit.json').read_text(encoding='utf-8'))
assert a['source_commit']==r['source_commit'] and a['archived_records']==527827
assert a['distinct_payloads_by_marker']['c']==41776
assert not a['interval_coverage_proved'] and not a['historical_checksum_replayed']
c=json.loads((root/'470-legacy-pruning-certificate.json').read_text(encoding='utf-8'))
assert c['semiperfect'] and not c['odd_weird_counterexample'] and not c['certification']
print('PASS: provenance packet hashes and explicit source, interval and certification gaps')
