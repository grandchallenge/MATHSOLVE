#!/usr/bin/env python3
"""Independent exact scorer for the OPENMATH-2026 Kobon-triangles hill."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path

MAX_BYTES = 65_536
MAX_COEFF = 10**30


class InputError(ValueError):
    """The submitted data violates the locked hill input contract."""


def _pairs_no_dupes(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise InputError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def _reject_float(text: str):
    raise InputError(f"floating-point JSON number is invalid: {text}")


def _reject_constant(text: str):
    raise InputError(f"non-finite JSON constant is invalid: {text}")


def load_solution(path: Path, expected_n: int | None = None):
    if path.is_symlink():
        raise InputError("solution file must not be a symlink")
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        raise InputError(f"solution file exceeds {MAX_BYTES} bytes")
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise InputError("solution file is not UTF-8") from exc
    try:
        obj = json.loads(
            text,
            object_pairs_hook=_pairs_no_dupes,
            parse_float=_reject_float,
            parse_constant=_reject_constant,
        )
    except (json.JSONDecodeError, InputError) as exc:
        raise InputError(str(exc)) from exc

    if type(obj) is not dict or set(obj) != {"lines"}:
        raise InputError("top-level object must contain exactly the field 'lines'")
    raw_lines = obj["lines"]
    if type(raw_lines) is not list:
        raise InputError("'lines' must be a list")
    if expected_n is not None and len(raw_lines) != expected_n:
        raise InputError(f"expected exactly {expected_n} lines, got {len(raw_lines)}")
    if not (3 <= len(raw_lines) <= 100):
        raise InputError("line count must lie in 3..100")

    lines: list[tuple[int, int, int]] = []
    seen = set()
    for i, triple in enumerate(raw_lines):
        if type(triple) is not list or len(triple) != 3:
            raise InputError(f"line {i} must be a three-element JSON array")
        if any(type(value) is not int for value in triple):
            raise InputError(
                f"line {i} coefficients must be JSON integers (booleans are invalid)"
            )
        a, b, c = triple
        if max(abs(a), abs(b), abs(c)) > MAX_COEFF:
            raise InputError(f"line {i} coefficient exceeds 10^30")
        if a == 0 and b == 0:
            raise InputError(f"line {i} has a=b=0")

        divisor = math.gcd(math.gcd(abs(a), abs(b)), abs(c))
        if divisor:
            a, b, c = a // divisor, b // divisor, c // divisor
        for coefficient in (a, b, c):
            if coefficient:
                if coefficient < 0:
                    a, b, c = -a, -b, -c
                break
        normalized = (a, b, c)
        if normalized in seen:
            raise InputError(f"line {i} is proportional to an earlier line")
        seen.add(normalized)
        lines.append(normalized)

    return lines, hashlib.sha256(data).hexdigest()


def intersection(
    first: tuple[int, int, int], second: tuple[int, int, int]
) -> tuple[Fraction, Fraction] | None:
    a, b, c = first
    d, e, f = second
    determinant = a * e - d * b
    if determinant == 0:
        return None
    return (
        Fraction(b * f - e * c, determinant),
        Fraction(c * d - a * f, determinant),
    )


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"{value.numerator}/{value.denominator}"


def score(lines: list[tuple[int, int, int]]):
    line_points: list[set[tuple[Fraction, Fraction]]] = [
        set() for _ in lines
    ]
    all_points: set[tuple[Fraction, Fraction]] = set()

    for i, j in combinations(range(len(lines)), 2):
        point = intersection(lines[i], lines[j])
        if point is not None:
            line_points[i].add(point)
            line_points[j].add(point)
            all_points.add(point)

    points = sorted(all_points)
    point_id = {point: index for index, point in enumerate(points)}
    adjacency: dict[int, set[int]] = defaultdict(set)
    edge_line: dict[tuple[int, int], int] = {}

    # On a line a*x+b*y+c=0, (b,-a) is a direction vector.  Consecutive
    # intersection vertices in its exact dot-product order are arrangement edges.
    for line_index, (a, b, _c) in enumerate(lines):
        ids = sorted(
            (point_id[point] for point in line_points[line_index]),
            key=lambda vertex: (
                b * points[vertex][0] - a * points[vertex][1]
            ),
        )
        for u, v in zip(ids, ids[1:]):
            edge = (u, v) if u < v else (v, u)
            old = edge_line.get(edge)
            if old is not None and old != line_index:
                raise AssertionError(
                    "distinct normalized lines cannot share a nonzero segment"
                )
            edge_line[edge] = line_index
            adjacency[u].add(v)
            adjacency[v].add(u)

    faces = []
    for u in sorted(adjacency):
        for v in sorted(vertex for vertex in adjacency[u] if vertex > u):
            common = adjacency[u].intersection(adjacency[v])
            for w in sorted(vertex for vertex in common if vertex > v):
                pu, pv, pw = points[u], points[v], points[w]
                area2 = (
                    (pv[0] - pu[0]) * (pw[1] - pu[1])
                    - (pv[1] - pu[1]) * (pw[0] - pu[0])
                )
                if area2 == 0:
                    continue

                supports = tuple(
                    sorted(
                        (
                            edge_line[tuple(sorted((u, v)))],
                            edge_line[tuple(sorted((v, w)))],
                            edge_line[tuple(sorted((w, u)))],
                        )
                    )
                )
                if len(set(supports)) != 3:
                    raise AssertionError(
                        "a nondegenerate triangular cycle must have three supporting lines"
                    )
                faces.append(
                    {
                        "supporting_lines": list(supports),
                        "vertices": [
                            [fraction_text(point[0]), fraction_text(point[1])]
                            for point in (pu, pv, pw)
                        ],
                    }
                )

    faces.sort(key=lambda face: (face["supporting_lines"], face["vertices"]))
    return {
        "triangles": len(faces),
        "faces": faces,
        "arrangement_vertices": len(points),
        "bounded_arrangement_edges": len(edge_line),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Independent exact Kobon triangular-face scorer"
    )
    parser.add_argument("solution", type=Path)
    parser.add_argument("--n", type=int, default=None)
    parser.add_argument("--expect", type=int, default=None)
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    try:
        lines, digest = load_solution(args.solution, args.n)
        result = score(lines)
    except InputError as exc:
        print(json.dumps({"passed": False, "reason": str(exc)}, sort_keys=True))
        raise SystemExit(2) from exc

    result = {
        "passed": True,
        "solution_sha256": digest,
        "n": len(lines),
        **result,
    }
    rendered = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output is not None:
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")

    if args.expect is not None and result["triangles"] != args.expect:
        raise SystemExit(
            f"expected {args.expect} triangles, got {result['triangles']}"
        )


if __name__ == "__main__":
    main()
