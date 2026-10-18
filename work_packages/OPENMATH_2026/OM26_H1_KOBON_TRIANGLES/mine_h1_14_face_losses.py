#!/usr/bin/env python3
"""Mine exact H1-14 determinant-flip face losses for reusable motifs.

This is seed-local route analysis, not an upper-bound proof.  It works in the
abstract orientation cell used by H1-14 and records exactly which triangular
supports change under each required blocker-exit determinant flip.
"""
from __future__ import annotations

import argparse
import collections
import json
from itertools import combinations
from pathlib import Path

import wolfram_94_semialgebraic as bridge

ROOT = Path(__file__).resolve().parent
SEED = ROOT / "candidates/RH_BADER_RECONSTRUCTION_093/solution.json"
ATLAS = ROOT / "H1_14_NEAR_MISS_ATLAS.json"


def face_set(lines, flips=()):
    pair_signs = bridge._pair_signs(lines)
    triple_signs = bridge._triple_signs(lines)
    for key in {tuple(sorted(x)) for x in flips}:
        if triple_signs[key] == 0:
            raise ValueError(f"cannot flip zero determinant wall {key}")
        triple_signs[key] *= -1

    faces = set()
    n = len(lines)
    for i, j, k in combinations(range(n), 3):
        wij = bridge._d2_sign(pair_signs, i, j)
        wjk = bridge._d2_sign(pair_signs, j, k)
        wki = bridge._d2_sign(pair_signs, k, i)
        if 0 in (wij, wjk, wki):
            continue
        if bridge._d3_sign(triple_signs, i, j, k) == 0:
            continue
        crossed = False
        for m in range(n):
            if m in (i, j, k):
                continue
            vals = (
                bridge._d3_sign(triple_signs, m, i, j) * wij,
                bridge._d3_sign(triple_signs, m, j, k) * wjk,
                bridge._d3_sign(triple_signs, m, k, i) * wki,
            )
            if 1 in vals and -1 in vals:
                crossed = True
                break
        if not crossed:
            faces.add((i, j, k))
    return faces


def incidence_signature(face, flip):
    return len(set(face) & set(flip))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()

    lines = [tuple(x) for x in json.loads(SEED.read_text())["lines"]]
    atlas = json.loads(ATLAS.read_text())
    base = face_set(lines)
    if len(base) != 93:
        raise SystemExit(f"seed face drift: {len(base)}")

    unique = {}
    for case in atlas["two_blocker_cases"]:
        target = tuple(case["target_triple"])
        for route in case["blockers"]:
            key = tuple(route["required_flip_key"])
            unique.setdefault(key, {"targets": [], "moving_line": route["moving_line"]})
            unique[key]["targets"].append(target)

    single_records = []
    lost_hist = collections.Counter()
    gained_hist = collections.Counter()
    lost_incidence_hist = collections.Counter()
    gained_incidence_hist = collections.Counter()
    all_three_toll = True
    all_lost_touch_flip_twice = True

    for key, meta in sorted(unique.items()):
        after = face_set(lines, [key])
        lost = sorted(base - after)
        gained = sorted(after - base)
        lost_hist[len(lost)] += 1
        gained_hist[len(gained)] += 1
        linc = collections.Counter(incidence_signature(f, key) for f in lost)
        ginc = collections.Counter(incidence_signature(f, key) for f in gained)
        lost_incidence_hist.update(linc)
        gained_incidence_hist.update(ginc)
        all_three_toll &= len(lost) == 3 and len(gained) == 0
        all_lost_touch_flip_twice &= all(incidence_signature(f, key) >= 2 for f in lost)
        single_records.append({
            "flip": list(key),
            "moving_line": meta["moving_line"],
            "target_count": len(meta["targets"]),
            "targets": [list(t) for t in sorted(meta["targets"])],
            "score": len(after),
            "lost": [list(f) for f in lost],
            "gained": [list(f) for f in gained],
            "lost_flip_intersection_histogram": {str(k): v for k, v in sorted(linc.items())},
            "gained_flip_intersection_histogram": {str(k): v for k, v in sorted(ginc.items())},
        })

    dual_records = []
    dual_lost_hist = collections.Counter()
    dual_gained_hist = collections.Counter()
    overlap_hist = collections.Counter()
    target_gain_count = 0
    for case in atlas["two_blocker_cases"]:
        target = tuple(case["target_triple"])
        keys = [tuple(b["required_flip_key"]) for b in case["blockers"]]
        a1 = face_set(lines, [keys[0]])
        a2 = face_set(lines, [keys[1]])
        both = face_set(lines, keys)
        lost1, lost2 = base - a1, base - a2
        lost = base - both
        gained = both - base
        overlap = lost1 & lost2
        dual_lost_hist[len(lost)] += 1
        dual_gained_hist[len(gained)] += 1
        overlap_hist[len(overlap)] += 1
        if target in gained:
            target_gain_count += 1
        dual_records.append({
            "target": list(target),
            "flips": [list(k) for k in keys],
            "score": len(both),
            "lost_count": len(lost),
            "gained_count": len(gained),
            "single_loss_overlap_count": len(overlap),
            "target_gained": target in gained,
            "lost": [list(f) for f in sorted(lost)],
            "gained": [list(f) for f in sorted(gained)],
            "single_loss_overlap": [list(f) for f in sorted(overlap)],
        })

    result = {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-16-FACE-LOSS-MINING",
        "seed_score": len(base),
        "unique_required_flip_count": len(unique),
        "single_flip": {
            "lost_count_histogram": {str(k): v for k, v in sorted(lost_hist.items())},
            "gained_count_histogram": {str(k): v for k, v in sorted(gained_hist.items())},
            "lost_flip_intersection_histogram": {str(k): v for k, v in sorted(lost_incidence_hist.items())},
            "gained_flip_intersection_histogram": {str(k): v for k, v in sorted(gained_incidence_hist.items())},
            "all_three_face_toll_no_gain": all_three_toll,
            "all_lost_faces_share_at_least_two_flip_lines": all_lost_touch_flip_twice,
            "records": single_records,
        },
        "dual_flip": {
            "cases": len(dual_records),
            "lost_count_histogram": {str(k): v for k, v in sorted(dual_lost_hist.items())},
            "gained_count_histogram": {str(k): v for k, v in sorted(dual_gained_hist.items())},
            "single_loss_overlap_histogram": {str(k): v for k, v in sorted(overlap_hist.items())},
            "target_gained_count": target_gain_count,
            "records": dual_records,
        },
        "claim_boundary": "Exact seed-local orientation-cell mining only; motifs are conjecture generators until separately proved under H1-12 hypotheses.",
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
