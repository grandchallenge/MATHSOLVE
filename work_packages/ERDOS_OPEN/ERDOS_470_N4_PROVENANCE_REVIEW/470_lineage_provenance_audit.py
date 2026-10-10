"""Read-only archive reconciliation; filename groups are not certified lineages."""
from collections import Counter, defaultdict
import argparse, hashlib, json, subprocess, tarfile
from pathlib import Path

E = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--source', type=Path, default=E / 'ows-data')
parser.add_argument('--output', type=Path, default=E / '470-lineage-provenance-audit.json')
args = parser.parse_args()
S = args.source
PIN = '88d22faf46400f0050287c3c32c9a807ca3b1340'
assert subprocess.check_output(['git', '-C', str(S), 'rev-parse', 'HEAD']).decode().strip() == PIN
manifest = json.loads((E / 'ows-archive-manifest.json').read_text(encoding='utf-8'))
markers = Counter()
names = defaultdict(set)
payload_markers = defaultdict(set)
groups = defaultdict(Counter)
group_completed = defaultdict(set)
name_collisions = set()
by_name = {}
for archive in manifest:
    path = S / archive['path']
    raw_archive = path.read_bytes()
    assert hashlib.sha256(raw_archive).hexdigest() == archive['sha256']
    assert hashlib.sha1(b'blob ' + str(len(raw_archive)).encode() + b'\0' + raw_archive).hexdigest() == archive['git_blob_sha1']
    with tarfile.open(path, mode='r|gz') as tf:
        for member in tf:
            if not member.isfile():
                continue
            raw = tf.extractfile(member).read()
            marker = raw.decode('ascii').splitlines()[-1]
            digest = hashlib.sha256(raw).hexdigest()
            name = Path(member.name).name
            tokens = name.split('_')
            assert len(tokens) == 4 and tokens[0] == 'ows' and all(t.isdigit() for t in tokens[1:]), name
            # This observed naming group is a hypothesis, not a recovered generator rule.
            group = tokens[2]
            markers[marker] += 1
            names[marker].add(name)
            payload_markers[marker].add(digest)
            groups[group][marker] += 1
            if marker == 'c':
                group_completed[group].add(digest)
            if name in by_name and by_name[name] != digest:
                name_collisions.add(name)
            by_name[name] = digest
out = {
    'record_type': 'GCL_ERDOS_470_ARCHIVE_PROVENANCE_RECONCILIATION_CANDIDATE',
    'source_commit': PIN,
    'archive_manifest_sha256': hashlib.sha256(json.dumps(manifest, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
    'archive_count': len(manifest), 'archived_records': sum(markers.values()),
    'marker_counts': dict(markers), 'distinct_names_by_marker': {k: len(v) for k, v in names.items()},
    'distinct_payloads_by_marker': {k: len(v) for k, v in payload_markers.items()},
    'same_name_different_payload_count': len(name_collisions),
    'observed_filename_groups': len(groups),
    'observed_groups_without_c': len(set(groups) - set(group_completed)),
    'observed_groups_with_multiple_distinct_c': sum(len(v) > 1 for v in group_completed.values()),
    'published_table_1': {'first_batch_lineages': 41776, 'first_batch_workunits': 527191,
        'source': 'https://doi.org/10.1007/s10723-017-9411-5', 'page': 655},
    'archived_minus_published_workunits': sum(markers.values()) - 527191,
    'filename_group_semantics': 'Third token is documented as running number in the batch; persistence across recycled workunits and interval identity remain unverified',
    'filename_documentation': 'https://www.rechenkraft.net/wiki/index.php?title=Yoyo%40home_en',
    'interval_coverage_proved': False, 'historical_checksum_replayed': False,
    'paired_validator_results_recovered': False, 'odd_weird_exclusion_certified': False,
}
args.output.write_text(json.dumps(out, indent=2) + '\n', encoding='utf-8')
print(json.dumps(out, indent=2))
