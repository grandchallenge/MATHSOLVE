#!/usr/bin/env python3
"""Finite certificates for the conditional saturated-prism obstruction."""
import hashlib
import itertools
import json
from pathlib import Path
from ci.validate_openmath_h1_q6_replay import graph, cubic_certificate, local_states

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / 'work_packages/OPENMATH_2026/OM26_H1_KOBON_TRIANGLES'

def saturated_words(r):
    words = []
    for two in itertools.combinations(range(2*r), 3):
        word = [2 if i in two else 1 for i in range(2*r)]
        if any(all(word[(i+j) % (2*r)] == 1 for j in range(r-1))
               for i in range(2*r)):
            continue
        gaps = [(two[(i+1) % 3]-two[i]-1) % (2*r) for i in range(3)]
        assert min(gaps) >= 1
        words.append({'word':word, 'D1_gaps':gaps})
    return words

def replay():
    predecessor_path = PACKAGE / 'H1_Q6_INTERNAL_REPLAY_RECEIPT.json'
    predecessor = json.loads(predecessor_path.read_text())
    assert predecessor['profile_333444']['local_totals'] == {'D1':24,'B':24,'U':3}
    words = {str(r):saturated_words(r) for r in (3,4)}
    assert [len(words[str(r)]) for r in (3,4)] == [2,8]
    for r in (3,4):
        maximum = 2*r-3
        assert max(d1 for d1,_ in local_states(r,3)) == maximum
        assert [(a,b) for a,b in local_states(r,3) if a == maximum] == [(maximum,maximum)]
    certificates = []
    for candidate in predecessor['profile_333444']['certificates']:
        neighbors = graph(candidate['mask'])
        assert json.loads(json.dumps(cubic_certificate(neighbors))) == {k:v for k,v in candidate.items() if k != 'mask'}
        if candidate['class'] != 'TRIANGULAR_PRISM':
            continue
        triangle = candidate['triangles'][0]
        assert all(b in neighbors[a] for a,b in itertools.combinations(triangle,2))
        certificates.append({'mask':candidate['mask'], 'forbidden_D2_triangle':triangle})
    assert len(certificates) == len({c['mask'] for c in certificates}) == 60
    return {
        'record_id':'OM26-H1-SATURATED-PRISM-OBSTRUCTION-001',
        'state':'CONDITIONAL_PAPER_PROOF__INDEPENDENT_GEOMETRIC_REVIEW_PENDING',
        'predecessor_receipt_sha256':hashlib.sha256(predecessor_path.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'profile':'333444', 'clean_lines':6, 'unused_segments':3,
        'local_totals':{'D1':24,'B':24,'D2':9},
        'saturated_local_words':words,
        'prism_certificates':certificates,
        'prism_candidates_excluded':60,
        'realizable_candidates_remaining_in_profile':0,
        'remaining_q6_profiles':['333333','333334','333335','333344'],
        'dependencies':['six-core no-long-run fan premise',
                        'six-core clean-line charging premise',
                        'elementary D2 edges and planar core graph'],
        'claim_boundary':'Conditional elimination of profile 333444. The finite checker verifies words and graph certificates, not the real-geometric theorem or its premises. No independent Cert disposition, external lease consumption, global score bound, or q>=7 conclusion.'
    }

if __name__ == '__main__':
    print(json.dumps(replay(), indent=2, sort_keys=True))
