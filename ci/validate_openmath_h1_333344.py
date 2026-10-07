#!/usr/bin/env python3
"""Finite replay for the conditional q=6 profile-333344 obstruction.

The checker deliberately works in a relaxation of real line geometry.  It
reuses the protected q=6 local-word/planarity machinery, then minimizes the
core-incidence excess after allowing every favorable collinearity compatible
with D2 elementary chains.  Only the unique equality family is handed to the
paper-level multiplicity argument.
"""
from __future__ import annotations

import collections
import functools
import hashlib
import itertools
import json
from pathlib import Path

import validate_openmath_h1_333335 as base

N = 18
PROFILE = (3, 3, 3, 3, 4, 4)
VERTICES = tuple(range(6))
EDGES = tuple(itertools.combinations(VERTICES, 2))
EXPECTED_RELAXED = {6: 327, 7: 765, 8: 2464, 9: 1510, 10: 1077}
EXPECTED_PLANAR = {6: 327, 7: 765, 8: 2464, 9: 1500, 10: 1017}
EXPECTED_TRIANGLE = {7: 36, 8: 90}
EXPECTED_EXCESS_HIST = {
    (7, 18, 13, 0, 0, 4): 12,
    (7, 19, 15, 1, 1, 4): 36,
    (7, 19, 16, 1, 0, 4): 36,
    (8, 18, 14, 1, 0, 4): 6,
    (8, 19, 16, 2, 1, 4): 6,
    (8, 19, 17, 2, 0, 4): 54,
    (8, 20, 16, 3, 4, 4): 6,
    (8, 20, 17, 3, 3, 4): 6,
    (8, 20, 18, 3, 2, 4): 54,
    (8, 20, 19, 3, 1, 4): 54,
    (8, 20, 20, 3, 0, 3): 12,
    (8, 20, 20, 3, 0, 4): 78,
}


def configure_base():
    # The imported routines are exact generic six-core routines except for the
    # declared profile constant read by global_states/triangle_compatible.
    base.PROFILE = PROFILE


def graph(mask: int):
    return base.graph(mask)


def edge_set(mask: int):
    return base.edge_set(mask)


def global_states(mask: int):
    return base.global_states(mask)


def planar(mask: int):
    return base.planar_six_vertex(mask)


def triangle_compatible(mask: int, targets):
    return base.triangle_compatible(mask, targets)


def bipartite_missing_certificate(mask: int):
    """Unique K3,3-minus-1-or-2-edge bipartition for the residual graphs."""
    edges = edge_set(mask)
    universe = set(VERTICES)
    certs = set()
    for left_tuple in itertools.combinations(VERTICES, 3):
        left = set(left_tuple)
        right = universe - left
        if any(tuple(sorted(e)) in edges for e in itertools.combinations(left, 2)):
            continue
        if any(tuple(sorted(e)) in edges for e in itertools.combinations(right, 2)):
            continue
        cross = {tuple(sorted((a, b))) for a in left for b in right}
        missing = tuple(sorted(cross - edges))
        if len(missing) not in (1, 2):
            continue
        a, b = tuple(sorted(left)), tuple(sorted(right))
        certs.add((min(a, b), max(a, b), missing))
    assert len(certs) == 1
    return next(iter(certs))


def local_total_assignments(mask: int, target: tuple[int, int]):
    neighbors = graph(mask)
    options = [base.local_pairs(r, len(neighbors[v])) for v, r in enumerate(PROFILE)]
    return tuple(
        assignment
        for assignment in itertools.product(*options)
        if (
            sum(d1 for d1, _ in assignment),
            sum(blocked for _, blocked in assignment),
        ) == target
    )


@functools.lru_cache(None)
def local_signatures(r: int, neighbors: tuple[int, ...], d1: int, blocked: int):
    """Forced neighbor pairs and antipodal D2 neighbor pairs for a local word.

    If a D1 ray is flanked by two D2 rays, the ordinary-endpoint transverse-line
    lemma forces the two corresponding D2-neighbor cores to share an arrangement
    line.  Antipodal D2 pairs are recorded because two D2 elementary edges can
    lie on one full arrangement line only in opposite ray directions.
    """
    degree = len(neighbors)
    out = set()
    for a, b, word in base.local_word_records(r, degree):
        if (a, b) != (d1, blocked):
            continue
        positions = [i for i, label in enumerate(word) if label == 2]
        n = len(word)
        for perm in itertools.permutations(neighbors):
            label = dict(zip(positions, perm))
            forced = set()
            antipodal = set()
            for i, x in enumerate(word):
                if x == 1 and word[(i - 1) % n] == 2 and word[(i + 1) % n] == 2:
                    forced.add(tuple(sorted((label[(i - 1) % n], label[(i + 1) % n]))))
            for p, v in label.items():
                q = (p + r) % (2 * r)
                if q in label:
                    antipodal.add(tuple(sorted((v, label[q]))))
            out.add((tuple(sorted(forced)), tuple(sorted(antipodal))))
    return tuple(sorted(out, key=lambda x: (len(x[0]), len(x[1]), x)))


def valid_line_block(vertices, d2_edges, antipodal_by_vertex):
    """Necessary conditions for several cores to lie on one arrangement line."""
    S = frozenset(vertices)
    on_line = {e for e in d2_edges if set(e) <= S}
    degree = collections.Counter(v for e in on_line for v in e)
    if any(x > 2 for x in degree.values()):
        return False
    # A set of elementary D2 segments on one line is a disjoint union of paths,
    # never a cycle.  Degree-two continuation must use antipodal rays locally.
    touched = {v for e in on_line for v in e}
    if on_line and len(on_line) >= len(touched):
        return False
    for v, x in degree.items():
        if x == 2:
            ns = tuple(sorted(w for e in on_line if v in e for w in e if w != v))
            if ns not in antipodal_by_vertex[v]:
                return False
    return True


def minimum_incidence_excess(mask: int, forced_pairs, antipodal_by_vertex):
    """Relaxed minimum E=(I-h)-D2 compatible with required core collinearities.

    A geometric line block S contributes |S|-1 core-incidence savings and gets
    credit for every D2 elementary edge it carries.  Its excess is therefore
    |S|-1-e_D2(S).  The exact cover allows extra favorable collinearities, so
    the returned minimum is a lower bound for any real arrangement.
    """
    d2_edges = frozenset(edge_set(mask))
    required = d2_edges | frozenset(forced_pairs)
    blocks = []
    for size in range(2, 7):
        for S in itertools.combinations(VERTICES, size):
            pairs = frozenset(itertools.combinations(S, 2))
            covered = pairs & required
            if not covered or not valid_line_block(S, d2_edges, antipodal_by_vertex):
                continue
            d2_on_line = pairs & d2_edges
            cost = size - 1 - len(d2_on_line)
            blocks.append((frozenset(S), pairs, covered, cost, d2_on_line))

    by_edge = collections.defaultdict(list)
    for index, block in enumerate(blocks):
        for e in block[2]:
            by_edge[e].append(index)

    best_cost = 99
    best_solution = None

    def dfs(remaining, chosen, used_pairs, cost):
        nonlocal best_cost, best_solution
        if cost > best_cost:
            return
        if not remaining:
            if cost < best_cost:
                best_cost, best_solution = cost, tuple(chosen)
            return
        edge = min(remaining, key=lambda x: len(by_edge[x]))
        for index in by_edge[edge]:
            S, pairs, covered, block_cost, _ = blocks[index]
            if pairs & used_pairs:
                continue
            # Distinct geometric lines cannot share two core points.
            if any(len(S & blocks[j][0]) >= 2 for j in chosen):
                continue
            dfs(remaining - covered, chosen + (index,), used_pairs | pairs, cost + block_cost)

    dfs(set(required), tuple(), frozenset(), 0)
    assert best_solution is not None
    certificate = [
        {
            "vertices": sorted(blocks[i][0]),
            "cost": blocks[i][3],
            "d2_edges": [list(e) for e in sorted(blocks[i][4])],
            "required_covered": [list(e) for e in sorted(blocks[i][2])],
        }
        for i in best_solution
    ]
    return best_cost, certificate


def minimum_line_cover_patterns(mask: int, forced_pairs, antipodal_by_vertex, target_cost: int):
    """Enumerate canonical minimum-cost line-cover patterns at a fixed cost."""
    d2_edges = frozenset(edge_set(mask))
    required = d2_edges | frozenset(forced_pairs)
    blocks = []
    for size in range(2, 7):
        for S in itertools.combinations(VERTICES, size):
            pairs = frozenset(itertools.combinations(S, 2))
            covered = pairs & required
            if not covered or not valid_line_block(S, d2_edges, antipodal_by_vertex):
                continue
            d2_on_line = pairs & d2_edges
            cost = size - 1 - len(d2_on_line)
            blocks.append((frozenset(S), pairs, covered, cost, d2_on_line))

    by_edge = collections.defaultdict(list)
    for index, block in enumerate(blocks):
        for e in block[2]:
            by_edge[e].append(index)

    patterns = set()
    def dfs(remaining, chosen, used_pairs, cost):
        if cost > target_cost:
            return
        if not remaining:
            if cost == target_cost:
                pattern = tuple(sorted(
                    (tuple(sorted(blocks[i][0])), blocks[i][3], tuple(sorted(blocks[i][4])))
                    for i in chosen
                ))
                patterns.add(pattern)
            return
        edge = min(remaining, key=lambda x: len(by_edge[x]))
        for index in by_edge[edge]:
            S, pairs, covered, block_cost, _ = blocks[index]
            if pairs & used_pairs:
                continue
            if any(len(S & blocks[j][0]) >= 2 for j in chosen):
                continue
            dfs(remaining - covered, chosen + (index,), used_pairs | pairs, cost + block_cost)

    dfs(set(required), tuple(), frozenset(), 0)
    return tuple(sorted(patterns))


def replay():
    configure_base()
    relaxed = collections.Counter()
    planar_counts = collections.Counter()
    triangle_counts = collections.Counter()
    residual = []

    for mask in range(1 << len(EDGES)):
        targets = global_states(mask)
        if not targets:
            continue
        d2 = mask.bit_count()
        relaxed[d2] += 1
        if not planar(mask):
            continue
        planar_counts[d2] += 1
        if not triangle_compatible(mask, targets):
            continue
        triangle_counts[d2] += 1
        residual.append((mask, targets))

    assert dict(sorted(relaxed.items())) == EXPECTED_RELAXED
    assert dict(sorted(planar_counts.items())) == EXPECTED_PLANAR
    assert dict(sorted(triangle_counts.items())) == EXPECTED_TRIANGLE
    assert len(residual) == 126

    graph_roles = collections.Counter()
    excess_hist = collections.Counter()
    equality = []

    for mask, targets in residual:
        left, right, missing = bipartite_missing_certificate(mask)
        assert mask.bit_count() == 9 - len(missing)
        if len(missing) == 1:
            graph_roles[(8, tuple(sorted(tuple(sorted(PROFILE[v] for v in e)) for e in missing)))] += 1
        else:
            shared = set(missing[0]) & set(missing[1])
            assert len(shared) == 1
            graph_roles[(7, tuple(sorted(tuple(sorted(PROFILE[v] for v in e)) for e in missing)), PROFILE[next(iter(shared))])] += 1

        neighbors = graph(mask)
        d2 = mask.bit_count()
        clean_lower = N - (sum(PROFILE) - d2)
        for d1, blocked, unused in targets:
            capacity = 2 * unused + d1 - blocked
            slack = capacity - clean_lower
            best = None
            for assignment in local_total_assignments(mask, (d1, blocked)):
                local = [
                    local_signatures(PROFILE[v], tuple(sorted(neighbors[v])), *assignment[v])
                    for v in VERTICES
                ]
                for choice in itertools.product(*local):
                    forced = frozenset(p for f, _ in choice for p in f)
                    antipodal = [frozenset(a) for _, a in choice]
                    excess, cover = minimum_incidence_excess(mask, forced, antipodal)
                    candidate = (excess, tuple(sorted(forced)), assignment, cover, choice)
                    if best is None or candidate[:2] < best[:2]:
                        best = candidate
            assert best is not None
            excess_hist[(d2, d1, blocked, unused, slack, best[0])] += 1
            if best[0] <= slack:
                equality.append({
                    "mask": mask,
                    "D2": d2,
                    "D1": d1,
                    "B": blocked,
                    "U": unused,
                    "slack": slack,
                    "minimum_incidence_excess": best[0],
                    "forced_pairs": [list(e) for e in best[1]],
                    "assignment": [list(x) for x in best[2]],
                    "line_cover": best[3],
                    "bipartition": [list(left), list(right)],
                    "missing_edges": [list(e) for e in missing],
                })

    assert dict(excess_hist) == EXPECTED_EXCESS_HIST
    assert graph_roles == {
        (8, ((3, 3),)): 36,
        (8, ((3, 4),)): 48,
        (8, ((4, 4),)): 6,
        (7, ((3, 4), (3, 4)), 3): 12,
        (7, ((3, 4), (4, 4)), 4): 24,
    }

    # Exactly six labeled equality escapes survive the relaxed incidence bound.
    assert len(equality) == 6
    for row in equality:
        assert (row["D2"], row["D1"], row["B"], row["U"], row["slack"]) == (8, 20, 16, 3, 4)
        assert row["minimum_incidence_excess"] == 4
        missing = row["missing_edges"]
        assert len(missing) == 1 and sorted(PROFILE[v] for v in missing[0]) == [4, 4]
        # Four triple cores are degree three and the two quadruple cores degree two.
        degrees = tuple(map(len, graph(row["mask"])))
        assert sorted((PROFILE[v], degrees[v]) for v in VERTICES) == [
            (3, 3), (3, 3), (3, 3), (3, 3), (4, 2), (4, 2)
        ]
        assert row["assignment"] == [[3, 3], [3, 3], [3, 3], [3, 3], [4, 2], [4, 2]]
        left, right = map(tuple, row["bipartition"])
        forced_expected = set(itertools.combinations(left, 2)) | set(itertools.combinations(right, 2))
        assert set(map(tuple, row["forced_pairs"])) == forced_expected
        positive_cost_blocks = [x for x in row["line_cover"] if x["cost"]]
        assert sorted((x["vertices"], x["cost"], x["d2_edges"]) for x in positive_cost_blocks) == sorted([
            (list(left), 2, []), (list(right), 2, [])
        ])
        zero_blocks = [x for x in row["line_cover"] if x["cost"] == 0]
        assert len(zero_blocks) == 8 and all(len(x["vertices"]) == 2 and len(x["d2_edges"]) == 1 for x in zero_blocks)

        # Audit the optimizer witness: in the equality family every local word
        # has no antipodal D2 continuation and the union of forced neighbor-pair
        # lines is invariant. Enumerating every cost-four cover leaves exactly
        # the two bipartition triples plus the eight individual D2 supports.
        neighbors = graph(row["mask"])
        local = [
            local_signatures(PROFILE[v], tuple(sorted(neighbors[v])), *row["assignment"][v])
            for v in VERTICES
        ]
        assert all(not antipodal for options in local for _, antipodal in options)
        forced_sets = {
            frozenset(pair for forced, _ in choice for pair in forced)
            for choice in itertools.product(*local)
        }
        assert forced_sets == {frozenset(forced_expected)}
        patterns = minimum_line_cover_patterns(
            row["mask"], next(iter(forced_sets)), [frozenset() for _ in VERTICES], 4
        )
        assert len(patterns) == 1
        positive = sorted((list(S), cost, [list(e) for e in d2s]) for S, cost, d2s in patterns[0] if cost)
        assert positive == sorted([(list(left), 2, []), (list(right), 2, [])])

    return {
        "schema_version": "1.0.0",
        "record_id": "OM26-H1-333344-OBSTRUCTION-001",
        "state": "CONDITIONAL_PAPER_PROOF__FINITE_REPLAY_PASS__TRUSTED_MATHEMATICAL_ADAPTER_PENDING",
        "profile": "333344",
        "checker_sha256": hashlib.sha256(Path(__file__).read_bytes().replace(b"\r\n", b"\n")).hexdigest(),
        "labeled_graphs_visited": 1 << len(EDGES),
        "relaxed_graph_candidates_by_D2": dict(sorted(relaxed.items())),
        "planar_graph_candidates_by_D2": dict(sorted(planar_counts.items())),
        "triangle_compatible_graph_candidates_by_D2": dict(sorted(triangle_counts.items())),
        "post_triangle_residual_labelings": len(residual),
        "post_triangle_graph_role_counts": {str(k): v for k, v in sorted(graph_roles.items(), key=lambda kv: str(kv[0]))},
        "incidence_excess_histogram": {str(k): v for k, v in sorted(excess_hist.items())},
        "relaxed_equality_escape_labelings": len(equality),
        "equality_escape": equality,
        "paper_obstruction": (
            "The unique minimum-excess equality pattern forces one three-core line on each K3,3 bipartition. "
            "Every triple core has D2-degree three to the opposite bipartition. Since the three opposite cores "
            "are collinear on a distinct line, their three D2 support lines through the triple core are pairwise "
            "distinct. Together with its own bipartition line this would give four arrangement lines through a "
            "multiplicity-three point, contradiction."
        ),
        "realizable_candidates_remaining_in_profile": 0,
        "remaining_q6_profiles": ["333333", "333334"],
        "dependencies": [
            "six-core no-long-run fan premise",
            "six-core clean-line charging premise",
            "elementary D2 edge planarity",
            "elementary D2 triangle adjacency lemma",
            "ordinary-endpoint transverse-line lemma",
        ],
        "claim_boundary": (
            "Conditional elimination of q=6 profile 333344. The finite replay verifies the graph/local-word "
            "reduction, relaxed incidence lower bound, and unique equality normal form; the accompanying note "
            "supplies the final real-geometric multiplicity contradiction. No q=6 closure, q>=7 conclusion, "
            "hill-global <=94 claim, MATHCERT promotion, novelty claim, or competition submission."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(replay(), indent=2, sort_keys=True))
