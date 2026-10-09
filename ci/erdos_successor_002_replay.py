#!/usr/bin/env python3
"""Native, deterministic replay for protected Erdős successor-002 returns.

Only elementary finite mathematical facts and documentary evidence integrity
are replayed.  External set-theory, literature, Lean build and 80-core-year
search claims are explicitly NOT certified here.
"""
from __future__ import annotations

import hashlib
import itertools
import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
BASE = Path("contributions/ERDOS-OPEN-001/SUCCESSOR_002")
INPUTS = {
    "ERDOS-593-R2-IA-001": 6075616641,
    "ERDOS-593-S2-IA-001": 6071504892,
    "ERDOS-470-S2-IA-001": 6071306717,
}
REPLAY = ROOT / BASE / "replays/ERDOS-SUCCESSOR-002-REPLAY-001.json"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def audit_evidence(root: Path = ROOT) -> dict[str, Any]:
    rows: list[dict[str, Any]] = []
    for dispatch, comment_id in INPUTS.items():
        raw_path = root / BASE / "raw" / dispatch / f"github-comment-{comment_id}.md"
        receipt_path = root / BASE / "receipts" / dispatch / f"github-comment-{comment_id}.json"
        raw = raw_path.read_bytes()
        receipt_bytes = receipt_path.read_bytes()
        receipt = json.loads(receipt_bytes)
        digest = sha256(raw)
        required = {
            "dispatch_id": dispatch,
            "github_comment_id": comment_id,
            "raw_artifact_path": raw_path.relative_to(root).as_posix(),
            "raw_sha256": digest,
            "schema_result": "valid",
            "handling_state": "received_unadjudicated",
            "canonical_claim_effect": False,
            "mathematical_correctness_adjudicated": False,
            "worker_reservation_enforced": True,
            "certification_effect": False,
        }
        failures = [
            key for key, expected in required.items()
            if receipt.get(key) != expected
        ]
        if failures:
            raise ValueError(f"{dispatch}: receipt disagreement: {failures}")
        if not raw.startswith(b"GCL-CONTRIBUTION-RESULT/1\n"):
            raise ValueError(f"{dispatch}: raw payload marker differs")
        if f"dispatch_id: {dispatch}\n".encode() not in raw:
            raise ValueError(f"{dispatch}: raw dispatch preamble differs")
        rows.append({
            "dispatch_id": dispatch,
            "github_comment_id": comment_id,
            "raw_sha256": digest,
            "integrity": "EXACT_RAW_AND_RECEIPT_CONCORDANT",
            "mathematical_acceptance": False,
        })
    return {"records": rows, "all_protected_inputs_concordant": True}


def triangle_of_pairs(n: int) -> tuple[set[frozenset[frozenset[int]]], int]:
    triples = list(itertools.combinations(range(n), 3))
    edges = {
        frozenset(frozenset(pair) for pair in itertools.combinations(t, 2))
        for t in triples
    }
    assert len(edges) == len(triples)
    max_overlap = max(
        (len(a & b) for a, b in itertools.combinations(edges, 2)),
        default=0,
    )
    return edges, max_overlap


def has_monochromatic_triangle(n: int, coloring_bits: int) -> bool:
    pairs = list(itertools.combinations(range(n), 2))
    pair_index = {p: i for i, p in enumerate(pairs)}
    return any(
        len({
            (coloring_bits >> pair_index[tuple(sorted(pair))]) & 1
            for pair in itertools.combinations(t, 2)
        }) == 1
        for t in itertools.combinations(range(n), 3)
    )


def first_difference_replay() -> dict[str, Any]:
    # Color a pair of distinct binary strings by its first differing bit.
    # No three pairwise distances can have the same first-difference index:
    # at that coordinate three binary symbols cannot be pairwise different.
    samples: dict[str, dict[str, int]] = {}
    for depth in (2, 3, 4, 5):
        vertices = tuple(range(1 << depth))
        def first_difference(a: int, b: int) -> int:
            differing = a ^ b
            return next(i for i in range(depth) if differing & (1 << i))
        mono = sum(
            len({first_difference(a, b), first_difference(a, c),
                 first_difference(b, c)}) == 1
            for a, b, c in itertools.combinations(vertices, 3)
        )
        if mono:
            raise AssertionError("first-difference construction contains monochromatic triangle")
        samples[str(depth)] = {
            "vertices": 1 << depth,
            "monochromatic_triangles": mono,
        }
    return {
        "finite_binary_sequence_tests": samples,
        "infinite_first_difference_omega_coloring": "PROVED_BY_BINARY_COORDINATE_ARGUMENT",
        "two_color_version": "IMPOSSIBLE_FOR_AT_LEAST_SIX_VERTICES",
    }


def finite_ramsey_replay() -> dict[str, Any]:
    # Independently exhaust all 2^(6 choose 2)=32768 edge-colorings of K6.
    k6_colorings = 1 << 15
    no_triangle_k6 = sum(
        not has_monochromatic_triangle(6, bits)
        for bits in range(k6_colorings)
    )
    # K5 has the known red 5-cycle / blue complementary 5-cycle witness.
    pairs = list(itertools.combinations(range(5), 2))
    cycle = {frozenset(e) for e in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0)]}
    witness_bits = sum(
        (1 << i) for i, pair in enumerate(pairs)
        if frozenset(pair) in cycle
    )
    k5_no_mono_triangle = not has_monochromatic_triangle(5, witness_bits)
    if no_triangle_k6 or not k5_no_mono_triangle:
        raise AssertionError("independent R(3,3) replay failed")
    return {
        "K6_two_colorings_exhausted": k6_colorings,
        "K6_triangle_free_two_colorings": no_triangle_k6,
        "K5_cycle_complement_witness_no_monochromatic_triangle": k5_no_mono_triangle,
        "R_3_3_equals_6_confirmed_finite": True,
        "worker_R2_claim_of_two_coloring_large_complete_pair_graph_avoiding_all_monochromatic_triangles": "REFUTED",
    }


def structural_replay() -> dict[str, Any]:
    tested = {}
    for n in (3, 4, 5, 6, 7):
        edges, overlap = triangle_of_pairs(n)
        if overlap > 1:
            raise AssertionError(f"triangle-of-pairs nonlinear at n={n}")
        tested[str(n)] = {
            "hyperedges": len(edges),
            "maximum_distinct_hyperedge_overlap": overlap,
        }
    # K_5^(3) has two different edges sharing {0,1}.
    k5 = list(itertools.combinations(range(5), 3))
    max_k5_overlap = max(len(set(a) & set(b)) for a, b in itertools.combinations(k5, 2))
    if max_k5_overlap != 2:
        raise AssertionError("K5^(3) overlap replay failed")
    # This direct combinatorial proof generalizes the finite tests:
    # for any A != B in [lambda]^3, if two pairs belonged to [A]^2
    # and [B]^2 they would recover all three elements, forcing A=B.
    # Injectivity preserves intersections of hyperedges, so a pair of
    # overlapping hyperedges in F cannot embed in a linear host.
    return {
        "triangle_of_pairs_finite_samples": tested,
        "K5_3_maximum_distinct_hyperedge_overlap": max_k5_overlap,
        "general_pair_intersection_lemma": "PROVED_BY_ELEMENTARY_SET_ARGUMENT",
        "nonlinear_F_nonembedding_into_linear_H": "PROVED_BY_INJECTIVITY_INTERSECTION_ARGUMENT",
        "uncountable_chromaticity": "CONDITIONAL_ON_EXTERNAL_ERDOS_RADO_PARTITION_THEOREM_NOT_REPLAYED",
    }


def build_report(root: Path = ROOT) -> dict[str, Any]:
    return {
        "schema_version": "1.0.0",
        "record_type": "GCL_ERDOS_SUCCESSOR_002_NATIVE_REPLAY",
        "tranche": "ERDOS-OPEN-SUCCESSOR-002",
        "evidence": audit_evidence(root),
        "erdos_593": {
            "structural": structural_replay(),
            "ramsey_falsification": finite_ramsey_replay(),
            "countable_coloring_boundary": first_difference_replay(),
            "li_lean_artifact": {
                "repository": "ericlisg/erdos-593-1177-lean",
                "reported_head_at_source_inspection": "5dcb6e4906df03f2e4294b21be73b55db7736f5a",
                "file": "RequestProject/PublicationCertificate.lean",
                "status": "PRIMARY_REPOSITORY_EXISTS_NOT_REBUILT_NOT_ADJUDICATED",
            },
        },
        "erdos_470": {
            "source_repository": "fwjmath/ows-data",
            "source_commit_from_worker": "88d22faf46400f0050287c3c32c9a807ca3b1340",
            "source_commit_existence": "OBSERVED_GITHUB_COMMIT_OBJECT",
            "data_1e21_prefix_cover": "NOT_REPLAYED",
            "workunit_checksums": "NOT_REPLAYED",
            "full_search_or_exclusion_theorem": "NOT_ADJUDICATED",
            "six_distinct_prime_factor_theorem_body": "NOT_SOURCE_LOCKED",
        },
        "authority_effects": {
            "native_finite_checks": True,
            "proof_assistant_verification": False,
            "external_source_theorems_independently_verified": False,
            "complete_classification_certified": False,
            "odd_weird_exclusion_certified": False,
            "erdos_problem_closed": False,
            "mathcert_certification": False,
            "publication": False,
        },
    }


def main() -> int:
    expected = json.loads(REPLAY.read_text(encoding="utf-8"))
    actual = build_report()
    if actual != expected:
        print("FAIL: protected successor replay differs from deterministic reconstruction")
        return 1
    print("PASS: ERDOS successor-002 evidence digests, finite replay, and authority boundaries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
