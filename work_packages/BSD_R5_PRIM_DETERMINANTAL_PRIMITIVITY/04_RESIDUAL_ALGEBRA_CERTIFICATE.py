#!/usr/bin/env python3
"""Deterministic structural checks for the BSD-R5-PRIM residual criterion.

This checks finite algebra used by the written proof. It does not prove the
missing arithmetic nonvanishing theorem and creates no certification authority.
"""
from __future__ import annotations

from math import comb


def req(ok: bool, msg: str) -> None:
    if not ok:
        raise SystemExit("BSD R5-PRIM residual certificate: FAIL: " + msg)


def main() -> None:
    # In characteristic two, (1+T)^(2^n)-1 = T^(2^n).
    binomial_levels = []
    for n in range(0, 11):
        d = 2**n
        middle = [comb(d, k) % 2 for k in range(1, d)]
        req(all(x == 0 for x in middle), f"binomial parity n={n}")
        binomial_levels.append(d)

    # A nonzero residual power series T^r is detected in a sufficiently deep
    # quotient F2[[T]]/(T^(2^n)), although it need not be a finite-ring unit.
    detection = []
    for r in range(0, 65):
        n = 0
        while 2**n <= r:
            n += 1
        req(r < 2**n, f"finite detection r={r}")
        detection.append((r, n))

    # Finite-level basis status is strictly stronger than the height-one-(2)
    # criterion: T is nonzero/nonunit in F2[T]/(T^2), but T is inverted in
    # Lambda_(2), so it becomes a unit there.
    finite_ring_elements = {0, 1, 2, 3}  # a+bT encoded as a+2b, T^2=0
    units = {1, 3}                       # constant coefficient 1
    T = 2
    req(T in finite_ring_elements and T not in units and T != 0,
        "T finite-layer nonzero/nonunit witness")

    print({
        "status": "PASS",
        "operation": "BSD-R5-PRIM",
        "checked_binomial_levels": binomial_levels,
        "finite_detection_samples": len(detection),
        "height_one_residue_field": "F2((T))",
        "finite_layer_basis_required": False,
        "residual_nonvanishing_required": True,
        "candidate_disposition": "BLOCKED",
        "blocked_on": "MISSING_P2_RESIDUAL_CYCLOTOMIC_KATO_KOLYVAGIN_NONVANISHING",
        "r5_lift": True,
        "r5_prim": False,
        "bsd_r2_a1": False,
        "mathcert_certification": False,
    })


if __name__ == "__main__":
    main()
