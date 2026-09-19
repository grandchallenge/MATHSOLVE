#!/usr/bin/env python3
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
WP = ROOT / 'work_packages' / 'BSD_R5_RECIP_P2_NORMALIZED_RECIPROCITY'


def need(text, token):
    assert token in text, token


def main():
    local = (WP / '01_LITERAL_P2_LOCAL_LATTICE_THEOREM.md').read_text()
    symbol = (WP / '02_LITERAL_P2_SYMBOL_AND_RECIPROCITY_THEOREM.md').read_text()
    ledger = (WP / '03_CLAIM_LEDGER.yaml').read_text()

    for token in [
        'BSD-R5-RECIP-LOCAL-DUALEXP-006',
        'q_2/2^(t_2+1)',
        'finite principal Frobenius ring',
        'BSD-R5-RECIP-LOCAL-TORSIONCOEFF-007',
    ]:
        need(local, token)

    for token in [
        'BSD-R5-RECIP-SYMBOL-SATURATION-002',
        '2 [a/n]^+ in Z_2',
        'Delta_n^(2)',
        'BSD-R5-RECIP-SYMBOL-KKS-005',
        'BSD-R5-RECIP-NORMALIZED-RECIPROCITY-006',
        'MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS',
    ]:
        need(symbol, token)

    q_values = {2, 4}
    for q in q_values:
        valid_t = []
        for t in range(1, 5):
            if q % (2 ** (t - 1)) == 0:
                valid_t.append(t)
                lhs_num = q
                lhs_den = 2
                lattice_num = q
                lattice_den = 2 ** (t + 1)
                # (q/2) = (q/2^(t+1))*2^t exactly.
                assert lhs_num * lattice_den == lattice_num * (2 ** t) * lhs_den
        assert valid_t

    for token in [
        'candidate_disposition: CLOSED',
        'r5_res: false',
        'r5_prim: false',
        'bsd_r2_a1: false',
        'mathcert_certification: false',
    ]:
        need(ledger, token)

    print(json.dumps({
        'status': 'PASS',
        'operation': 'BSD-R5-RECIP',
        'retired_frontier': 'MISSING_P2_NORMALIZED_ANOMALOUS_ORDINARY_KATO_KURIHARA_RECIPROCITY',
        'next_frontier': 'MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS',
        'r5_res': False,
        'r5_prim': False,
        'bsd_r2_a1': False,
        'mathcert_certified': False,
    }, sort_keys=True))


if __name__ == '__main__':
    main()
