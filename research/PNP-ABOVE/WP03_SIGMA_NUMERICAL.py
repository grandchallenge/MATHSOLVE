#!/usr/bin/env python3
"""PNP-ABOVE WP03: source-faithful numerical sigma recurrence.

Implements only the VALUE of MIPRE.Pipeline.sigmaFun at upstream
vidick/MIPRE-formalization commit 5926bdff5db621f44682a101007ef2fe3ae8d970,
file MIPRE/Foundations/Pipeline/Compress.lean, definitions sigmaFun_zero/succ.
No Lean formal proof object, DecisionCompiler.compute, or full compressor is run.
"""
from __future__ import annotations
import json
from hashlib import sha256


UPSTREAM_COMMIT = "5926bdff5db621f44682a101007ef2fe3ae8d970"
UPSTREAM_SOURCE = "MIPRE/Foundations/Pipeline/Compress.lean"
UPSTREAM_BLOB = "37023b8d945c57b342bb8b5cf75339beb58b67d8"


def nat_size(n: int) -> int:
    """Value of natural-number binary bit size for nonnegative n."""
    if type(n) is not int or n < 0:
        raise ValueError("natural number required")
    return n.bit_length()


def sigma_recurrence(c: int, n: int) -> int:
    """sigma(0,n)=2n+1; sigma(c+1,n)=2^(2*size(sigma(c,n)))."""
    if type(c) is not int or type(n) is not int or min(c, n) < 0:
        raise ValueError("c and n must be natural numbers")
    value = 2 * n + 1
    for _ in range(c):
        value = 1 << (2 * nat_size(value))
    return value


def sigma_closed(c: int, n: int) -> int:
    """Elementary closed form derived from the source recurrence; c>=1."""
    if type(c) is not int or type(n) is not int or min(c, n) < 0:
        raise ValueError("c and n must be natural numbers")
    if c == 0:
        return 2 * n + 1
    b0 = nat_size(2 * n + 1)
    return 1 << ((1 << c) * (b0 + 1) - 2)


def exact_checks() -> dict:
    """No stochastic tests and no third-party packages."""
    expected = [7, 64, 16384, 1 << 30, 1 << 62, 1 << 126]
    assert [sigma_recurrence(c, 3) for c in range(6)] == expected
    recurrence_cases = 0
    bound_cases = 0
    for c in range(8):
        for n in range(40):
            r = sigma_recurrence(c, n)
            assert r == sigma_closed(c, n)
            recurrence_cases += 1
            if c < 6 and n <= 20:
                # Independently sampled instances of upstream le_sigmaFun;
                # universal proof remains in upstream Lean, not in this script.
                assert c * (n + 1) ** c <= r
                bound_cases += 1
            if n < 39:
                assert r <= sigma_recurrence(c, n + 1)
    for invalid in (-1, 1.5, True):
        try:
            sigma_recurrence(invalid, 3)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input accepted")

    return {
        "upstream_commit": UPSTREAM_COMMIT,
        "upstream_source": UPSTREAM_SOURCE,
        "upstream_blob_sha1": UPSTREAM_BLOB,
        "independent_recursion_closed_form_cases": recurrence_cases,
        "sampled_source_polynomial_bound_cases": bound_cases,
        "n3_values": [str(v) for v in expected],
        "numerical_source_recurrence": "PASS",
        "full_upstream_lean_build": "NOT_RUN",
        "DecisionCompiler.compute": "NOT_RUN",
        "introspection_answer_reduction_repetition": "NOT_RUN",
    }


if __name__ == "__main__":
    print(json.dumps(exact_checks(), indent=2, sort_keys=True))
