#!/usr/bin/env python3
"""Bounded compound order-type search for OM26-H1 score 94.

This script is a proposal generator only.  It imports the pinned external
projective-mutation implementation supplied by the caller, explores compound
macros that may traverse deep score valleys, and invokes the external exact-
checked LP reconstruction only for a combinatorial endpoint of score >=94.

Search failure is not an upper bound or infeasibility certificate.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import time
from pathlib import Path


def load_external(root: Path):
    construction = root / "experiments/2026-09-21/construction-search"
    sys.path.insert(0, str(construction))
    from beam_mutation import ProjectiveChamber, apply_flip, read_lines, realize_target
    from chamber_mutation import arrangement, save_result
    return ProjectiveChamber, apply_flip, read_lines, realize_target, arrangement, save_result


def run(args):
    ext = args.external.resolve()
    ProjectiveChamber, apply_flip, read_lines, realize_target, arrangement, save_result = load_external(ext)
    source = args.source.resolve()
    lines = read_lines(source)
    ch = ProjectiveChamber(lines)
    initial = ch.score
    initial_projective = ch.pscore
    rng = random.Random(args.seed)
    start = time.time()
    best = initial
    combinatorial_best = initial
    projective_best = initial_projective
    nodes = edges = realization_attempts = 0
    endpoints_ge_94 = 0
    tested_targets = set()
    best_endpoint = None
    realized = []
    anchor_summaries = []

    for anchor in range(ch.n):
        if time.time() - start >= args.seconds:
            break
        rows = [((), 0, ch.score, ch.pscore, 0)]
        seen = {(0, 0)}
        anchor_nodes = anchor_edges = 0
        anchor_best = initial

        for level in range(1, args.depth + 1):
            choices = []
            for flips, mask, score, pscore, bridges in rows:
                for q in flips:
                    apply_flip(ch, q)
                assert (ch.score, ch.pscore) == (score, pscore)
                nodes += 1
                anchor_nodes += 1

                for q, empty in enumerate(ch.pempty):
                    if not empty or ((mask >> q) & 1):
                        continue
                    is_anchor = anchor in ch.triples[q]
                    if not is_anchor and bridges >= args.bridge_budget:
                        continue
                    new_bridges = bridges + (0 if is_anchor else 1)
                    newmask = mask | (1 << q)
                    state_key = (newmask, new_bridges)
                    if state_key in seen:
                        continue
                    seen.add(state_key)

                    apply_flip(ch, q)
                    sc, psc = ch.score, ch.pscore
                    apply_flip(ch, q)
                    edges += 1
                    anchor_edges += 1
                    child = flips + (q,)
                    combinatorial_best = max(combinatorial_best, sc)
                    projective_best = max(projective_best, psc)
                    anchor_best = max(anchor_best, sc)

                    if sc >= 94:
                        endpoints_ge_94 += 1
                        target_key = tuple(sorted(child))
                        if target_key not in tested_targets:
                            tested_targets.add(target_key)
                            for r in child:
                                apply_flip(ch, r)
                            try:
                                assert ch.score == sc
                                for mode in ("offset", "normal"):
                                    realization_attempts += 1
                                    candidate, reason = realize_target(ch, mode)
                                    if candidate is None:
                                        continue
                                    exact_score = len(arrangement(candidate)["triangles"])
                                    if exact_score != sc:
                                        raise AssertionError((exact_score, sc))
                                    record = {
                                        "anchor": anchor,
                                        "level": level,
                                        "score": sc,
                                        "projective_score": psc,
                                        "bridges": new_bridges,
                                        "mode": mode,
                                        "margin": reason,
                                        "flips": [list(ch.triples[x]) for x in child],
                                    }
                                    realized.append(record)
                                    if exact_score > best:
                                        best = exact_score
                                        best_endpoint = record
                                        if args.candidate:
                                            save_result(
                                                args.candidate,
                                                candidate,
                                                exact_score,
                                                str(source),
                                                "H1-15 compound anchor-line order-type macro",
                                                record,
                                            )
                                    break
                            finally:
                                for r in reversed(child):
                                    apply_flip(ch, r)

                    # No score-drop cutoff: the point of H1-15 is to cross
                    # valleys H1-13's drop=4 beam pruned. Score still dominates
                    # endpoint ranking; projective score and deterministic noise
                    # retain topologically diverse recovery paths.
                    rank = sc + args.projective_weight * psc + args.noise * rng.expovariate(1)
                    choices.append((rank, child, newmask, sc, psc, new_bridges))
                    if time.time() - start >= args.seconds:
                        break

                for q in reversed(flips):
                    apply_flip(ch, q)
                if time.time() - start >= args.seconds:
                    break

            if not choices or time.time() - start >= args.seconds:
                break
            choices.sort(key=lambda x: x[0], reverse=True)
            rows = [x[1:] for x in choices[: args.width]]

        assert ch.score == initial and ch.pscore == initial_projective
        anchor_summaries.append({
            "anchor": anchor,
            "nodes": anchor_nodes,
            "edges": anchor_edges,
            "best_score": anchor_best,
        })

    report = {
        "schema_version": "1.0.0",
        "record_id": "MS-OPENMATH-2026-OM26-H1-H1-15-COMPOUND-ORDER-TYPE-SEARCH",
        "source": str(source.relative_to(ext)).replace("\\", "/"),
        "source_sha256": hashlib.sha256(source.read_text().replace("\r\n", "\n").encode()).hexdigest(),
        "search_script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "external_commit_required": args.external_commit,
        "n": ch.n,
        "initial_score": initial,
        "initial_projective_score": initial_projective,
        "realized_best": best,
        "combinatorial_best": combinatorial_best,
        "projective_best": projective_best,
        "nodes": nodes,
        "edges": edges,
        "endpoints_ge_94": endpoints_ge_94,
        "realization_attempts": realization_attempts,
        "realized_candidates": realized,
        "best_endpoint": best_endpoint,
        "anchors_completed": len(anchor_summaries),
        "completed_all_anchors": len(anchor_summaries) == ch.n,
        "anchor_summaries": anchor_summaries,
        "width": args.width,
        "depth": args.depth,
        "bridge_budget": args.bridge_budget,
        "seed": args.seed,
        "projective_weight": args.projective_weight,
        "noise": args.noise,
        "seconds": time.time() - start,
        "configured_seconds": args.seconds,
        "found_94_or_better": best >= 94,
        "limitations": [
            "bounded beam search, not exhaustive over all oriented matroids",
            "at most the declared number of off-anchor bridge mutations per macro",
            "combinatorial endpoints are not straight-line candidates unless exact reconstruction succeeds",
            "failed search is not an upper bound or infeasibility certificate",
        ],
        "claim_boundary": (
            "Proposal-generation route evidence only. No global upper bound, optimality, novelty, "
            "competition acceptance, or MATHCERT certification follows from this search."
        ),
    }
    args.report.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({k: v for k, v in report.items() if k not in ("anchor_summaries", "realized_candidates")}, indent=2, sort_keys=True))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--external", type=Path, required=True)
    p.add_argument("--external-commit", default="22d1165f6c455fe45e461baef4410f6d5c78a014")
    p.add_argument("--source", type=Path, required=True)
    p.add_argument("--report", type=Path, required=True)
    p.add_argument("--candidate", type=Path)
    p.add_argument("--seconds", type=float, default=300)
    p.add_argument("--width", type=int, default=256)
    p.add_argument("--depth", type=int, default=10)
    p.add_argument("--bridge-budget", type=int, default=1)
    p.add_argument("--seed", type=int, default=2026100701)
    p.add_argument("--projective-weight", type=float, default=0.08)
    p.add_argument("--noise", type=float, default=0.35)
    args = p.parse_args()
    head = __import__("subprocess").check_output(
        ["git", "-C", str(args.external), "rev-parse", "HEAD"], text=True
    ).strip()
    if head != args.external_commit:
        raise SystemExit(f"external source drift: {head} != {args.external_commit}")
    run(args)


if __name__ == "__main__":
    main()
