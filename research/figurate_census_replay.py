"""Replay the FIGURATE L60 snapshot using exact integer arithmetic.

Usage:
  python3 -m research.figurate_census_replay
The snapshot is a bounded census, not an infinite-family theorem.
"""
from __future__ import annotations
import csv
from pathlib import Path
from research.figurate_census import census, verify_tuple

HERE = Path(__file__).resolve().parent
SNAPSHOT = HERE / "figurate_census_2026_11_03_L60.csv"


def replay(path: Path = SNAPSHOT) -> dict[str, int]:
    expected = {(kind, k, offset, size) for kind in ("A", "B", "C")
                for k in range(3, 13) for offset in (-1, 0, 1)
                for size in (2, 3, 4)}
    seen = set()
    totals = {"A": 0, "B": 0, "C": 0}
    with path.open(newline="", encoding="utf-8") as stream:
        rows = csv.DictReader(stream)
        assert rows.fieldnames == ["kind", "k", "offset", "size",
                                   "entry_limit", "count", "first_values"]
        for row in rows:
            kind = row["kind"]
            k, offset, size, limit, count = (int(row[key]) for key in (
                "k", "offset", "size", "entry_limit", "count"))
            key = (kind, k, offset, size)
            assert key in expected and key not in seen and limit == 60
            seen.add(key)
            obtained = census(kind, k, offset, limit, size)
            assert len(obtained) == count, (key, len(obtained), count)
            first = tuple(map(int, row["first_values"].split(";"))) if row["first_values"] else None
            assert (tuple(obtained[0]["values"]) if obtained else None) == first, key
            if first is not None:
                assert len(first) == size
                assert verify_tuple(first, kind, k, offset) is not None
            totals[kind] += count
    assert seen == expected, expected - seen
    return totals


if __name__ == "__main__":
    print("FIGURATE L60 replay PASS:", replay())
