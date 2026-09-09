from sage.all import EllipticCurve
from sage.libs.eclib.interface import mwrank_EllipticCurve
import json

COHORT = [
    ("53a1", [1, -1, 1, 0, 0]),
    ("203b1", [1, 1, 1, 0, -2]),
]

for label, ainvs in COHORT:
    E = EllipticCurve(ainvs)
    pari_rank = int(E.selmer_rank(algorithm="pari"))
    mwrank_rank = int(E.selmer_rank(algorithm="mwrank"))
    direct_eclib_rank = int(mwrank_EllipticCurve(ainvs).selmer_rank())

    if not (pari_rank == mwrank_rank == direct_eclib_rank):
        raise RuntimeError(
            f"2-Selmer implementation disagreement for {label}: "
            f"pari={pari_rank}, mwrank={mwrank_rank}, eclib={direct_eclib_rank}"
        )

    result = {
        "label": label,
        "ainvs": ainvs,
        "discriminant": int(E.discriminant()),
        "torsion_order": int(E.torsion_order()),
        "selmer_rank_pari": pari_rank,
        "selmer_rank_mwrank": mwrank_rank,
        "selmer_rank_eclib_direct": direct_eclib_rank,
        "selmer_2_order": 2 ** pari_rank,
        "s_1": pari_rank - 1,
    }
    print("WP18B_RESULT=" + json.dumps(result, sort_keys=True))
