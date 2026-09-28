#!/usr/bin/env python3
"""Replay the saturated-hub separator reduction for profile 3333."""
from __future__ import annotations

import json

try:
    from ci.validate_openmath_h1_12_3333_normal_form import EXPECTED_ORBITS
except ModuleNotFoundError:
    from validate_openmath_h1_12_3333_normal_form import EXPECTED_ORBITS


def has_saturated_triple_hub(row: dict) -> bool:
    return any(
        degree == 3 and d1 == 3
        for degree, d1 in zip(row["degrees"], row["d1"])
    )


def reduced_orbits() -> list[dict]:
    out = []
    for source in EXPECTED_ORBITS:
        row = dict(source)

        if has_saturated_triple_hub(row):
            if row["D2"] != 3:
                continue

            row["clean"] = 12
            if row["clean"] > row["capacity"]:
                continue

        out.append(row)
    return out


def main() -> None:
    source = EXPECTED_ORBITS
    saturated = [row for row in source if has_saturated_triple_hub(row)]
    if len(saturated) != 5:
        raise SystemExit(f"unexpected saturated-hub orbit count: {len(saturated)}")

    rows = reduced_orbits()
    if len(rows) != 8:
        raise SystemExit(f"unexpected residual orbit count: {len(rows)}")

    labeled = sum(row["labeled"] for row in rows)
    if labeled != 48:
        raise SystemExit(f"unexpected residual labeled count: {labeled}")

    histogram = {
        d2: sum(row["labeled"] for row in rows if row["D2"] == d2)
        for d2 in sorted({row["D2"] for row in rows})
    }
    if histogram != {1: 6, 2: 15, 3: 24, 4: 3}:
        raise SystemExit(f"unexpected D2 histogram: {histogram}")

    if any(row["D2"] >= 5 for row in rows):
        raise SystemExit("D2>=5 survived saturated-hub separator reduction")

    d2_four = [row for row in rows if row["D2"] == 4]
    if len(d2_four) != 1 or d2_four[0]["saturated"] != 0:
        raise SystemExit(f"unexpected D2=4 residual: {d2_four}")

    saturated_residual = [
        row for row in rows if has_saturated_triple_hub(row)
    ]
    if len(saturated_residual) != 1:
        raise SystemExit(
            f"unexpected saturated residual count: {len(saturated_residual)}"
        )
    if (
        saturated_residual[0]["D2"] != 3
        or saturated_residual[0]["clean"] != 12
        or saturated_residual[0]["capacity"] != 12
    ):
        raise SystemExit(
            "saturated residual did not tighten to D2=3, clean=capacity=12"
        )

    equality = [row for row in rows if row["clean"] == row["capacity"]]
    if len(equality) != 4:
        raise SystemExit(f"unexpected equality-form count: {len(equality)}")

    receipt = {
        "input_normal_forms": len(source),
        "input_labeled_states": sum(row["labeled"] for row in source),
        "saturated_hub_input_forms": len(saturated),
        "retained_normal_forms": len(rows),
        "retained_labeled_states": labeled,
        "D2_histogram": histogram,
        "equality_normal_forms": len(equality),
        "saturated_residual": saturated_residual,
        "result": "SATURATED_HUB_FORCES_D2_3_AND_SIX_CORE_PAIR_LINES",
        "claim_boundary": (
            "Finite consequence of the independently reconstructed separator "
            "lemma after invoking the named source-scoped triple-point local "
            "fan premise; lower-form exclusion also invokes the protected "
            "clean-line charging map. No hill-global upper bound or "
            "certification effect."
        ),
    }
    print(json.dumps(receipt, sort_keys=True))


if __name__ == "__main__":
    main()
