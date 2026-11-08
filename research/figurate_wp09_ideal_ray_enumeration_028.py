"""FIGURATE WP09-028: finite targeted oriented ray-class decision via ideal HNF.

O = Z[sqrt(D)], D=2A, A=8m+1. All integral O-ideals of index n
have unique HNF basis (ch,0),(cj,c), c*c*h=n, 0<=j<h,
j*j == D (mod h). Since gcd(n,A)=1, such ideals are invertible.

For N<0, a norm-N generator with positive chosen embedding is equivalent
to an oriented principal ideal of the correct norm signature. The prior
complete norm-representative theorem and two-gcd ray test classify each
enumerated ideal as ray target or not. This does NOT compute a general
ray class group, nor decide every parameter m with a resource guard.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from research.figurate_wp09_odd_ray_lattice_025 import normalized_parameters
from research.figurate_wp09_uniform_pell_lattice_023 import (
    fundamental_unit, norm_representatives,
)
from research.figurate_wp09_linear_ray_026 import (
    linear_ray_hit, verified_hit_modulo,
)
from research.figurate_wp09_ray_class_conductor_027 import order_data


@dataclass(frozen=True, order=True)
class IdealHNF:
    c: int
    h: int
    j: int

    @property
    def norm(self) -> int:
        return self.c * self.c * self.h

    def contains(self, x: int, y: int) -> bool:
        # x+y sqrt(D) belongs to <ch, cj+c sqrt(D)>.
        return y % self.c == 0 and (
            x - self.j * (y // self.c)
        ) % (self.c * self.h) == 0


def is_stable_ideal(ideal: IdealHNF, D: int) -> bool:
    """Closure under sqrt(D) on the two HNF lattice generators."""
    c, h, j = ideal.c, ideal.h, ideal.j
    return (
        c >= 1 and h >= 1 and 0 <= j < h
        and (j * j - D) % h == 0
    )


def enumerate_norm_ideals(D: int, n: int, *,
                          max_root_checks: int | None = 500000) -> list[IdealHNF]:
    """Complete HNF enumeration; a guard raises, never returns partial NO."""
    if D <= 1 or n < 1:
        raise ValueError("D>1, n>=1 required")
    if max_root_checks is not None and max_root_checks < 0:
        raise ValueError("nonnegative guard required")
    entries = []
    count = 0
    for c in range(1, isqrt(n) + 1):
        if n % (c * c):
            continue
        h = n // (c * c)
        if max_root_checks is not None and count + h > max_root_checks:
            raise ValueError("complete ideal root enumeration exceeds guard")
        count += h
        for j in range(h):
            if (j * j - D) % h == 0:
                ideal = IdealHNF(c, h, j)
                if ideal.norm != n or not is_stable_ideal(ideal, D):
                    raise ArithmeticError("invalid ideal HNF candidate")
                entries.append(ideal)
    return entries


def principal_ideal_from_generator(
        D: int, x: int, y: int,
        ideals: list[IdealHNF]) -> IdealHNF:
    """Find exact ideal (x+y sqrt(D)); rejects ambiguous/incomplete lists."""
    n = abs(x * x - D * y * y)
    match = [i for i in ideals if i.norm == n and i.contains(x, y)]
    if len(match) != 1:
        raise ArithmeticError("norm-generator ideal not uniquely represented")
    return match[0]


def classify_norm_ideal_ray(m: int, *,
                            max_ideal_checks: int | None = 500000,
                            max_representative_bound: int | None = 250000
                            ) -> dict:
    """All norm-|N| ideals classified for oriented negative-norm ray target.

    'not_oriented_principal' excludes norm-N generators of desired
    sign, but makes NO claim about ordinary principality (a positive-norm
    generator might still exist). 'oriented_principal_wrong_ray' says no
    norm-N generator in the target ray. This is NOT a full class group.
    """
    p = normalized_parameters(16 * m + 4)
    data = order_data(m)
    A, D, N = p["A"], p["Q"], p["N"]
    n = abs(N)
    if gcd(n, A) != 1 or D != data["D"]:
        raise ArithmeticError("conductor avoidance contract failed")
    ideals = enumerate_norm_ideals(
        D, n, max_root_checks=max_ideal_checks
    )
    unit = fundamental_unit(D)
    reps, cap = norm_representatives(
        p, unit, max_representative_bound
    )
    # Every positive norm-N generator normalizes under the norm-one
    # unit to one of these complete positive representatives.
    principal = {i: [] for i in ideals}
    for rep in reps:
        x, y = rep
        if x <= 0 or y <= 0 or x*x - D*y*y != N:
            raise ArithmeticError("invalid complete norm representative")
        ideal = principal_ideal_from_generator(D, x, y, ideals)
        hit = linear_ray_hit(p, unit, rep)
        if hit is not None and not verified_hit_modulo(
                p, unit, rep, hit["step"]):
            raise ArithmeticError("false oriented ray exponent")
        principal[ideal].append({"representative": rep, "ray_hit": hit})
    classifications = []
    for ideal in ideals:
        gen = principal[ideal]
        ray = next((x for x in gen if x["ray_hit"] is not None), None)
        status = ("ray_match" if ray else
                  "oriented_principal_wrong_ray" if gen else
                  "not_oriented_principal")
        classifications.append({
            "hnf": (ideal.c, ideal.h, ideal.j),
            "status": status,
            "generator_count_in_region": len(gen),
            "witness": ray
        })
    return {
        "m": m, "A": A, "D": D, "N": N,
        "order_conductor": data["f"],
        "candidate_ideal_count": len(ideals),
        "norm_representative_count": len(reps),
        "complete_representative_bound": cap,
        "ray_match_count": sum(
            item["status"] == "ray_match" for item in classifications
        ),
        "exists": any(item["status"] == "ray_match"
                      for item in classifications),
        "ideal_classes": classifications,
        "full_ray_class_group_computed": False,
        "global_parameter_classification_proved": False,
        "resource_guard_was_triggered": False
    }
