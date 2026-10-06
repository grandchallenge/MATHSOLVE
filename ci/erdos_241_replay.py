#!/usr/bin/env python3
from __future__ import annotations

import argparse
import itertools
import json
from pathlib import Path
from typing import Iterable


EXPECTED_MINIMAL_SPANS = {1: 1, 2: 2, 3: 5, 4: 12, 5: 24, 6: 46}
EXPECTED_EXTREMIZERS = {
    1: [(1,)],
    2: [(1, 2)],
    3: [(1, 2, 5), (1, 4, 5)],
    4: [(1, 2, 8, 12), (1, 2, 9, 12), (1, 4, 11, 12), (1, 5, 11, 12)],
    5: [(1, 2, 16, 19, 24), (1, 2, 16, 21, 24), (1, 4, 9, 23, 24), (1, 6, 9, 23, 24)],
    6: [(1, 3, 12, 27, 43, 46), (1, 4, 20, 35, 44, 46)],
}


def is_b3(values: Iterable[int]) -> bool:
    a = sorted(values)
    sums: set[int] = set()
    for i, x in enumerate(a):
        for j in range(i, len(a)):
            y = a[j]
            for k in range(j, len(a)):
                z = a[k]
                s = x + y + z
                if s in sums:
                    return False
                sums.add(s)
    return True


def normalized_b3_sets(k: int, n: int) -> list[tuple[int, ...]]:
    if k < 1 or n < 1:
        return []
    if k == 1:
        return [(1,)]
    cur = [1]
    sums = {3}
    out: list[tuple[int, ...]] = []

    def search(next_c: int) -> None:
        if len(cur) == k:
            out.append(tuple(cur))
            return
        need = k - len(cur)
        for x in range(next_c, n + 1):
            if n - x + 1 < need:
                break
            generated = [3 * x]
            generated.extend(2 * x + a for a in cur)
            generated.extend(
                x + a + b
                for i, a in enumerate(cur)
                for b in cur[i:]
            )
            if len(set(generated)) != len(generated):
                continue
            if any(s in sums for s in generated):
                continue
            new = set(generated)
            cur.append(x)
            sums.update(new)
            search(x + 1)
            cur.pop()
            sums.difference_update(new)

    search(2)
    return out


def first_normalized_b3_set(k: int, n: int) -> tuple[int, ...] | None:
    if k == 1:
        return (1,)
    cur = [1]
    sums = {3}

    def search(next_c: int) -> tuple[int, ...] | None:
        if len(cur) == k:
            return tuple(cur)
        need = k - len(cur)
        for x in range(next_c, n + 1):
            if n - x + 1 < need:
                break
            generated = [3 * x]
            generated.extend(2 * x + a for a in cur)
            generated.extend(
                x + a + b
                for i, a in enumerate(cur)
                for b in cur[i:]
            )
            if len(set(generated)) != len(generated):
                continue
            if any(s in sums for s in generated):
                continue
            new = set(generated)
            cur.append(x)
            sums.update(new)
            found = search(x + 1)
            if found is not None:
                return found
            cur.pop()
            sums.difference_update(new)
        return None

    return search(2)


def minimal_span(k: int) -> tuple[int, tuple[int, ...]]:
    for n in range(1, 80):
        found = first_normalized_b3_set(k, n)
        if found is not None:
            return n, found
    raise RuntimeError(f"minimal span not found for k={k}")


def extremizers_at_minimal_span(k: int, n: int) -> list[tuple[int, ...]]:
    return [x for x in normalized_b3_sets(k, n) if x[-1] == n]


def positive_difference_pairs(a: tuple[int, ...]) -> list[tuple[int, int, int]]:
    return [(x - y, x, y) for x in a for y in a if x > y]


def structural_violation(a: tuple[int, ...]) -> dict | None:
    pairs = positive_difference_pairs(a)
    values = {d for d, _, _ in pairs}
    for d in values:
        if 2 * d in values:
            return {"kind": "DOUBLE_DIFFERENCE", "set": a, "d": d}
    for d1, x1, y1 in pairs:
        for d2, x2, y2 in pairs:
            if {x1, y1}.isdisjoint({x2, y2}) and d1 + d2 in values:
                return {
                    "kind": "DISJOINT_DIFFERENCE_SUM",
                    "set": a,
                    "d1": d1,
                    "d2": d2,
                }
    return None


def finite_structural_falsification_sweep(limit: int = 15) -> dict:
    checked = 0
    for n in range(1, limit + 1):
        for k in range(1, min(6, n) + 1):
            for a in itertools.combinations(range(1, n + 1), k):
                if not is_b3(a):
                    continue
                checked += 1
                violation = structural_violation(a)
                if violation is not None:
                    return {
                        "limit": limit,
                        "checked_b3_sets": checked,
                        "violation": violation,
                    }
    return {"limit": limit, "checked_b3_sets": checked, "violation": None}


def build_report() -> dict:
    spans: dict[str, int] = {}
    witnesses: dict[str, list[int]] = {}
    extremizers: dict[str, list[list[int]]] = {}
    for k in range(1, 7):
        n, witness = minimal_span(k)
        spans[str(k)] = n
        witnesses[str(k)] = list(witness)
        extremizers[str(k)] = [list(x) for x in extremizers_at_minimal_span(k, n)]

    no_seven_through_64 = first_normalized_b3_set(7, 64) is None
    exact_f_intervals = [
        {"start": 1, "end": 1, "value": 1},
        {"start": 2, "end": 4, "value": 2},
        {"start": 5, "end": 11, "value": 3},
        {"start": 12, "end": 23, "value": 4},
        {"start": 24, "end": 45, "value": 5},
        {"start": 46, "end": 64, "value": 6},
    ]

    small = {
        "f_1": 1,
        "f_2": 2,
        "f_3": 2,
        "f_4": 2,
        "f_5_at_least": 3,
        "witness_f5": [1, 2, 5],
        "a1_extension_counterexample_base": [1, 3],
        "a1_extension_candidates_rejected": [2, 4, 5],
        "adjacent_block_union_collision": "1+1+4=2+2+2",
    }

    expected_spans = {str(k): v for k, v in EXPECTED_MINIMAL_SPANS.items()}
    expected_extremizers = {
        str(k): [list(x) for x in values]
        for k, values in EXPECTED_EXTREMIZERS.items()
    }

    return {
        "schema_version": "1.0.0",
        "record_type": "ERDOS_241_INDEPENDENT_REPLAY",
        "replay_id": "ERDOS-241-RA-REPLAY-001",
        "problem_id": 241,
        "definition": "strong B3: all cardinality-3 multisets supported on A have distinct sums unless the multisets are equal",
        "minimal_spans": spans,
        "first_witnesses": witnesses,
        "minimal_span_extremizers": extremizers,
        "no_seven_element_b3_set_through_64": no_seven_through_64,
        "exact_f_intervals_through_64": exact_f_intervals,
        "expected_minimal_spans_match": spans == expected_spans,
        "expected_extremizers_match": extremizers == expected_extremizers,
        "a1_small_n_replay": small,
        "a1_small_n_checks": {
            "set_1_2_5_is_b3": is_b3((1, 2, 5)),
            "set_1_3_2_is_not_b3": not is_b3((1, 2, 3)),
            "set_1_3_4_is_not_b3": not is_b3((1, 3, 4)),
            "set_1_3_5_is_not_b3": not is_b3((1, 3, 5)),
            "set_1_2_3_4_is_not_b3": not is_b3((1, 2, 3, 4)),
        },
        "structural_lemma_falsification_sweep": finite_structural_falsification_sweep(15),
        "external_sources_used": False,
        "claim_boundary": "Computational replay certifies only the enumerated finite claims and provides a falsification sweep for the structural lemmas. General structural lemmas are adjudicated separately by direct proof.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    report = build_report()
    text = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.report:
        args.report.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    ok = (
        report["expected_minimal_spans_match"]
        and report["expected_extremizers_match"]
        and all(report["a1_small_n_checks"].values())
        and report["structural_lemma_falsification_sweep"]["violation"] is None
    )
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
