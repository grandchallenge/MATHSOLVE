"""FIGURATE WP06: deterministic bounded matrix with independent baseline replay.

No global theorem is asserted by a finite enumeration.
Run: python3 -m research.figurate_wp06_panel --output research/figurate_wp06_L240_panel.csv
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import platform
import time
from pathlib import Path
from research.figurate_census import census
from research.figurate_residue_sieve import census_summary

FIELDS = ("kind", "k", "offset", "size", "entry_limit", "count",
          "first_values", "candidate_pairs", "residue_rejected",
          "exact_pair_checks", "edges")


def panel_rows(limit: int = 240) -> list[dict]:
    """All 30 B configurations plus A/C controls for a fixed entry bound."""
    parameters = (
        [(kind, k, offset, size)
         for kind in ("B",) for k in range(3, 9)
         for offset in (-1, 0, 1) for size in (3, 4)]
        + [(kind, k, offset, 3)
           for kind in ("A", "C") for k in (3, 4, 5)
           for offset in (-1, 0, 1)]
    )
    rows = []
    for kind, k, offset, size in parameters:
        d = census_summary(kind, k, offset, limit, size)
        rows.append({
            "kind": kind, "k": k, "offset": offset, "size": size,
            "entry_limit": limit, "count": d["count"],
            "first_values": ";".join(map(str, d["first_values"] or ())),
            "candidate_pairs": d["candidate_pairs"],
            "residue_rejected": d["residue_rejected"],
            "exact_pair_checks": d["exact_pair_checks"],
            "edges": d["edges"],
        })
    return rows


def encode(rows: list[dict]) -> bytes:
    s = io.StringIO(newline="")
    writer = csv.DictWriter(s, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return s.getvalue().encode("utf-8")


def validate(rows: list[dict]) -> None:
    """Independently reconstruct all 54 cell counts via baseline exact census."""
    if len(rows) != 54:
        raise AssertionError("expected 54 settings")
    for row in rows:
        key = (row["kind"], row["k"], row["offset"],
               row["entry_limit"], row["size"])
        baseline = census(*key)
        expected_first = ";".join(map(str, baseline[0]["values"])) if baseline else ""
        assert len(baseline) == row["count"], (key, "count")
        assert expected_first == row["first_values"], (key, "first")
        assert row["candidate_pairs"] == row["residue_rejected"] + row["exact_pair_checks"]
        assert row["residue_rejected"] >= 0
        assert row["edges"] >= 0


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--output", default="research/figurate_wp06_L240_panel.csv")
    p.add_argument("--limit", type=int, default=240)
    args = p.parse_args()
    if args.limit < 1:
        p.error("--limit must be positive")
    start = time.perf_counter()
    rows = panel_rows(args.limit)
    sieve_seconds = time.perf_counter() - start
    start = time.perf_counter()
    validate(rows)
    baseline_seconds = time.perf_counter() - start
    data = encode(rows)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)
    print(json.dumps({
        "scheme": "FIGURATE-WP06-PANEL/1", "rows": len(rows),
        "limit": args.limit, "sha256": hashlib.sha256(data).hexdigest(),
        "sieve_seconds": round(sieve_seconds, 6),
        "baseline_verify_seconds": round(baseline_seconds, 6),
        "python": platform.python_version(), "platform": platform.platform(),
        "total_candidate_pairs": sum(r["candidate_pairs"] for r in rows),
        "total_residue_rejected": sum(r["residue_rejected"] for r in rows),
        "total_exact_calls": sum(r["exact_pair_checks"] for r in rows),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
