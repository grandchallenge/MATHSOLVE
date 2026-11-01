"""PNP-ABOVE WP01: executable source-encoding and classical-introspection preflight.

Implements the tuple bit encoding of Ji et al. v4 Section 3.1 and computes
exact finite randomness/support barriers. It is *not* the paper's MIP*=RE
Compress constructor (no quantum introspection, PCP answer reduction, or
entangled parallel repetition is implemented).
"""
from fractions import Fraction
from itertools import product


def encode_tuple(xs):
    """Source Section 3.1: 0 -> 00, 1 -> 01, 10 separates fields."""
    for x in xs:
        if not isinstance(x, str) or any(c not in "01" for c in x):
            raise ValueError("tuple components must be binary strings")
    return "10".join("".join("0" + b for b in x) for x in xs) + "10"


def decode_tuple(bits, arity):
    if not isinstance(bits, str) or any(c not in "01" for c in bits) or arity < 1:
        raise ValueError("invalid bit string or arity")
    fields = []
    current = []
    if len(bits) % 2:
        raise ValueError("odd bit length")
    for j in range(0, len(bits), 2):
        tok = bits[j:j + 2]
        if tok == "10":
            fields.append("".join(current))
            current = []
        elif tok in ("00", "01"):
            current.append(tok[1])
        else:
            raise ValueError("invalid two-bit token")
    if current or len(fields) != arity:
        raise ValueError("wrong arity or unterminated field")
    return tuple(fields)


def uniform_from_seed(m, r):
    """Sharp witness: use r fresh bits and pad to m bits when 0<=r<=m."""
    if not (0 <= r <= m):
        raise ValueError("must have 0 <= r <= m")
    dist = {}
    for seed in product((0, 1), repeat=r):
        output = seed + (0,) * (m - r)
        dist[output] = dist.get(output, Fraction(0)) + Fraction(1, 2**r)
    return dist


def tv_to_uniform(m, dist):
    """Total variation to the uniform distribution on 2^m words."""
    target = Fraction(1, 2**m)
    return sum((abs(dist.get(x, Fraction(0)) - target) for x in product((0, 1), repeat=m)), Fraction()) / 2


def barrier(m, r):
    """Any r-bit classical sampler of m uniform bits has TV>=1-2^(r-m)."""
    if not (0 <= r <= m):
        raise ValueError("0 <= r <= m required")
    return Fraction(1) - Fraction(2**r, 2**m)


def tests():
    # The example explicitly given in the v4 paper for encoding (00,1)
    assert encode_tuple(("00", "1")) == "0000100110"
    assert decode_tuple("0000100110", 2) == ("00", "1")
    assert len(encode_tuple(("001", "", "101"))) == 2 * (3 + 0 + 3 + 3)
    for arity in (1, 2, 3):
        for words in product(("", "0", "1", "00", "01", "10", "11"), repeat=arity):
            code = encode_tuple(words)
            assert decode_tuple(code, arity) == words
            assert len(code) == 2 * (sum(map(len, words)) + arity)
    for malformed in ("", "00", "01", "1011", "0010", "110"):
        try:
            decode_tuple(malformed, 2)
        except ValueError:
            pass
        else:
            raise AssertionError("malformed encoding accepted: " + malformed)
    cases = 0
    for m in range(1, 10):
        for r in range(m + 1):
            d = uniform_from_seed(m, r)
            assert len(d) == 2**r
            assert sum(d.values()) == 1
            assert tv_to_uniform(m, d) == barrier(m, r)
            cases += 1
    assert barrier(9, 8) == Fraction(1, 2)
    assert barrier(9, 7) == Fraction(3, 4)
    assert barrier(9, 0) == Fraction(511, 512)
    assert barrier(9, 9) == 0
    return {"tuple_encoder":"PASS", "uniformity_cases":cases,
            "m9_r8_tv":"1/2", "m9_r7_tv":"3/4", "m9_r0_tv":"511/512",
            "m9_exact_random_bits_needed":9,
            "source_tm_transition_table_compiled":False,
            "full_mipstar_compress_implemented":False}


if __name__ == '__main__':
    import json
    print(json.dumps(tests(), indent=2, sort_keys=True))
