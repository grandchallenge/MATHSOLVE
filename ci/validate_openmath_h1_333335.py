#!/usr/bin/env python3
"""Finite replay for the conditional q=6 profile-333335 obstruction."""
from __future__ import annotations

import hashlib
import itertools
import json
from collections import Counter
from functools import lru_cache
from pathlib import Path

N = 18
PROFILE = (3, 3, 3, 3, 3, 5)
EDGES = tuple(itertools.combinations(range(6), 2))
EXPECTED_RELAXED = {7: 60, 8: 540, 9: 250, 10: 525}
EXPECTED_PLANAR = {7: 60, 8: 540, 9: 240, 10: 465}
EXPECTED_TRIANGLE_COMPATIBLE = {8: 30}


def graph(mask: int) -> list[set[int]]:
    neighbors = [set() for _ in range(6)]
    for index, (a, b) in enumerate(EDGES):
        if mask & (1 << index):
            neighbors[a].add(b)
            neighbors[b].add(a)
    return neighbors


def edge_set(mask: int) -> set[tuple[int, int]]:
    return {edge for index, edge in enumerate(EDGES) if mask & (1 << index)}


@lru_cache(None)
def local_word_records(r: int, degree: int):
    """Exact sector-consistent local words (0 other, 1 D1, 2 D2)."""
    n = 2 * r
    full = (1 << n) - 1

    def rotate(mask: int) -> int:
        return ((mask << 1) & full) | (mask >> (n - 1))

    out = set()
    for sectors in range(1 << n):
        shared = sectors & rotate(sectors)
        positions = [i for i in range(n) if (shared >> i) & 1]
        for chosen in itertools.combinations(positions, degree):
            two = sum(1 << i for i in chosen)
            one = shared ^ two
            run = one
            shifted = one
            for _ in range(r - 2):
                shifted = rotate(shifted)
                run &= shifted
            if run:
                continue
            adjacent = rotate(two) | (two >> 1) | ((two & 1) << (n - 1))
            d1 = one.bit_count()
            blocked = (one & adjacent).bit_count()
            word = tuple(
                2 if (two >> i) & 1 else 1 if (one >> i) & 1 else 0
                for i in range(n)
            )
            out.add((d1, blocked, word))
    return tuple(sorted(out))


@lru_cache(None)
def local_pairs(r: int, degree: int):
    return tuple(sorted({(d1, blocked) for d1, blocked, _ in local_word_records(r, degree)}))


@lru_cache(None)
def combined_states(pairs):
    totals = {(0, 0)}
    for r, degree in pairs:
        totals = {
            (a + c, b + d)
            for a, b in totals
            for c, d in local_pairs(r, degree)
        }
    return tuple(sorted(totals))


def global_states(mask: int):
    neighbors = graph(mask)
    degree = tuple(map(len, neighbors))
    d2 = mask.bit_count()
    I = sum(PROFILE)
    S = sum(r * (r - 2) for r in PROFILE)
    valid = []
    for d1, blocked in combined_states(tuple(sorted(zip(PROFILE, degree)))):
        unused = 3 - S + d1 + d2
        if unused >= 0 and N - I + d2 <= 2 * unused + d1 - blocked:
            valid.append((d1, blocked, unused))
    return tuple(valid)


def planar_six_vertex(mask: int) -> bool:
    """Exact here because every candidate has six vertices and at most ten edges.

    By Kuratowski, a nonplanar graph contains a subdivision of K5 or K3,3.
    A proper K5 subdivision has at least 11 edges; a proper K3,3 subdivision
    has at least seven vertices. Thus in this bounded universe it suffices to
    detect an unsubdivided K5 or K3,3 subgraph.
    """
    edges = edge_set(mask)
    for vertices in itertools.combinations(range(6), 5):
        if all(tuple(sorted(edge)) in edges for edge in itertools.combinations(vertices, 2)):
            return False
    universe = set(range(6))
    for left_tuple in itertools.combinations(range(6), 3):
        left = set(left_tuple)
        right = universe - left
        if all(tuple(sorted((a, b))) in edges for a in left for b in right):
            return False
    return True


def required_triangle_mask(mask: int, vertex: int) -> tuple[int, int]:
    """Encode pairs of incident D2 edges belonging to D2 graph triangles."""
    neighbors = sorted(graph(mask)[vertex])
    edges = edge_set(mask)
    required = 0
    for index, (i, j) in enumerate(itertools.combinations(range(len(neighbors)), 2)):
        if tuple(sorted((neighbors[i], neighbors[j]))) in edges:
            required |= 1 << index
    return len(neighbors), required


@lru_cache(None)
def local_triangle_compatible(r: int, degree: int, d1: int, blocked: int, required: int) -> bool:
    """Can incident D2 edges be placed on rays so every D2 triangle uses adjacent rays?"""
    for a, b, word in local_word_records(r, degree):
        if (a, b) != (d1, blocked):
            continue
        d2_positions = [i for i, label in enumerate(word) if label == 2]
        n = len(word)
        for assignment in itertools.permutations(d2_positions):
            ok = True
            for index, (i, j) in enumerate(itertools.combinations(range(degree), 2)):
                if required & (1 << index):
                    if (assignment[i] - assignment[j]) % n not in (1, n - 1):
                        ok = False
                        break
            if ok:
                return True
    return False


def triangle_compatible(mask: int, targets) -> bool:
    neighbors = graph(mask)
    target_pairs = {(d1, blocked) for d1, blocked, _ in targets}
    max_d1 = max(d1 for d1, _ in target_pairs)
    max_blocked = max(blocked for _, blocked in target_pairs)
    options = []
    for vertex, r in enumerate(PROFILE):
        degree, required = required_triangle_mask(mask, vertex)
        local = [
            (d1, blocked)
            for d1, blocked in local_pairs(r, degree)
            if local_triangle_compatible(r, degree, d1, blocked, required)
        ]
        if not local:
            return False
        options.append(local)
    totals = {(0, 0)}
    for local in options:
        totals = {
            (a + c, b + d)
            for a, b in totals
            for c, d in local
            if a + c <= max_d1 and b + d <= max_blocked
        }
    return bool(totals & target_pairs)


def local_total_assignments(mask: int, target: tuple[int, int]):
    neighbors = graph(mask)
    options = [local_pairs(r, len(neighbors[v])) for v, r in enumerate(PROFILE)]
    out = []
    for assignment in itertools.product(*options):
        if (
            sum(d1 for d1, _ in assignment),
            sum(blocked for _, blocked in assignment),
        ) == target:
            out.append(assignment)
    return tuple(out)


def k33_minus_edge_certificate(mask: int):
    edges = edge_set(mask)
    if len(edges) != 8:
        return None
    universe = set(range(6))
    certificates = []
    for left_tuple in itertools.combinations(range(6), 3):
        left = set(left_tuple)
        if 0 not in left:
            continue
        right = universe - left
        if any(tuple(sorted(edge)) in edges for edge in itertools.combinations(left, 2)):
            continue
        if any(tuple(sorted(edge)) in edges for edge in itertools.combinations(right, 2)):
            continue
        cross = [tuple(sorted((a, b))) for a in left for b in right]
        missing = [edge for edge in cross if edge not in edges]
        if len(missing) == 1:
            certificates.append((tuple(sorted(left)), tuple(sorted(right)), missing[0]))
    assert len(certificates) == 1
    return certificates[0]


def no_antipodal_d2(r: int, degree: int, d1: int, blocked: int) -> bool:
    for a, b, word in local_word_records(r, degree):
        if (a, b) != (d1, blocked):
            continue
        positions = {i for i, label in enumerate(word) if label == 2}
        if any((i + r) % (2 * r) in positions for i in positions):
            return False
    return True


def alternating_saturated_triple() -> bool:
    records = [
        word for d1, blocked, word in local_word_records(3, 3)
        if (d1, blocked) == (3, 3)
    ]
    assert len(records) == 2
    return all(
        all(
            word[(i - 1) % 6] == 2 and word[(i + 1) % 6] == 2
            for i, label in enumerate(word) if label == 1
        )
        for word in records
    )


def replay():
    relaxed = Counter()
    planar = Counter()
    triangle_ok = Counter()
    residual = []

    for mask in range(1 << len(EDGES)):
        targets = global_states(mask)
        if not targets:
            continue
        d2 = mask.bit_count()
        relaxed[d2] += 1
        if not planar_six_vertex(mask):
            continue
        planar[d2] += 1
        if not triangle_compatible(mask, targets):
            continue
        triangle_ok[d2] += 1
        residual.append((mask, targets))

    assert dict(sorted(relaxed.items())) == EXPECTED_RELAXED
    assert dict(sorted(planar.items())) == EXPECTED_PLANAR
    assert dict(sorted(triangle_ok.items())) == EXPECTED_TRIANGLE_COMPATIBLE
    assert len(residual) == 30
    assert alternating_saturated_triple()

    certificates = []
    for mask, targets in residual:
        assert targets == ((20, 16, 1),)
        neighbors = graph(mask)
        degree = tuple(map(len, neighbors))
        partition = k33_minus_edge_certificate(mask)
        assert partition is not None
        left, right, missing_edge = partition
        assert 5 in missing_edge
        assert degree[5] == 2
        triple_degree_two = next(v for v in range(5) if degree[v] == 2)
        assert set(missing_edge) == {5, triple_degree_two}
        assert sorted(degree[:5]) == [2, 3, 3, 3, 3]

        assignments = local_total_assignments(mask, (20, 16))
        assert len(assignments) == 1
        assignment = assignments[0]
        for vertex in range(5):
            expected = (2, 2) if degree[vertex] == 2 else (3, 3)
            assert assignment[vertex] == expected
        assert assignment[5] == (6, 2)

        for vertex, r in enumerate(PROFILE):
            d1, blocked = assignment[vertex]
            assert no_antipodal_d2(r, degree[vertex], d1, blocked)

        witness_vertex = next(v for v in range(5) if degree[v] == 3)
        witness_neighbors = sorted(neighbors[witness_vertex])
        assert len(witness_neighbors) == 3
        edges = edge_set(mask)
        assert all(
            tuple(sorted(pair)) not in edges
            for pair in itertools.combinations(witness_neighbors, 2)
        )

        certificates.append({
            'mask': mask,
            'missing_edge': list(missing_edge),
            'saturated_triple_witness': witness_vertex,
        })

    I = sum(PROFILE)
    d2 = 8
    d1, blocked, unused = (20, 16, 1)
    min_clean = N - (I - d2)
    charge_capacity = 2 * unused + d1 - blocked
    assert min_clean == charge_capacity == 6

    local_word_counts = {
        'triple_degree3_D1_3_B_3': sum(
            1 for a, b, _ in local_word_records(3, 3) if (a, b) == (3, 3)
        ),
        'triple_degree2_D1_2_B_2': sum(
            1 for a, b, _ in local_word_records(3, 2) if (a, b) == (2, 2)
        ),
        'quintuple_degree2_D1_6_B_2': sum(
            1 for a, b, _ in local_word_records(5, 2) if (a, b) == (6, 2)
        ),
    }
    assert local_word_counts == {
        'triple_degree3_D1_3_B_3': 2,
        'triple_degree2_D1_2_B_2': 18,
        'quintuple_degree2_D1_6_B_2': 10,
    }

    return {
        'record_id': 'OM26-H1-333335-OBSTRUCTION-001',
        'state': 'CONDITIONAL_PAPER_PROOF__FINITE_REPLAY_PASS__TRUSTED_MATHEMATICAL_ADAPTER_PENDING',
        'profile': '333335',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'labeled_graphs_visited': 1 << len(EDGES),
        'relaxed_graph_candidates_by_D2': dict(sorted(relaxed.items())),
        'planar_graph_candidates_by_D2': dict(sorted(planar.items())),
        'triangle_compatible_graph_candidates_by_D2': dict(sorted(triangle_ok.items())),
        'final_residual_isomorphism_type': 'K3,3-minus-one-edge',
        'final_residual_labelings': len(certificates),
        'final_residual_global_totals': {'D1': d1, 'B': blocked, 'U': unused, 'D2': d2},
        'clean_line_lower_bound': min_clean,
        'charge_capacity': charge_capacity,
        'forced_core_line_equality': {'I': I, 'h': I - d2, 'clean_lines': N - (I - d2)},
        'local_word_counts': local_word_counts,
        'all_final_local_states_have_no_antipodal_D2_pair': True,
        'all_degree3_triple_words_alternate_D1_D2': True,
        'certificates': certificates,
        'realizable_candidates_remaining_in_profile': 0,
        'remaining_q6_profiles': ['333333', '333334', '333344'],
        'dependencies': [
            'six-core no-long-run fan premise',
            'six-core clean-line charging premise',
            'elementary D2 edge planarity',
            'elementary D2 triangle adjacency lemma',
            'ordinary-endpoint transverse-line lemma',
        ],
        'claim_boundary': (
            'Conditional elimination of q=6 profile 333335. Finite replay verifies the exact graph/local-word '
            'reduction and equality antecedents; the accompanying manuscript supplies the geometric incidence '
            'argument. No q=6 closure, q>=7 conclusion, hill-global <=94 claim, MATHCERT promotion, external-agent '
            'lease consumption, or competition submission.'
        ),
    }


if __name__ == '__main__':
    print(json.dumps(replay(), indent=2, sort_keys=True))
