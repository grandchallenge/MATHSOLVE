"""PNP-ABOVE WP00 nine-level normal-form finite sampler emulator.

Implements query semantics of arXiv:2001.04383v4 Definition 4.14.
Not a bit-exact Turing-machine encoding or an execution of Compress.
"""
from itertools import product

LEVELS = 9
FIELD = 2
DIMENSION = 9
DEFAULT = "BAD_QUERY"

def bits(v):
    return isinstance(v, tuple) and len(v) == 9 and all(type(x) is int and x in (0, 1) for x in v)

def samp(n, query, player=None, level=None, z=None, u=None, y=None):
    if type(n) is not int or n < 1:
        return DEFAULT
    if query == "DIMENSION":
        return 9
    if query == "FIELD":
        return 2
    if player not in ("A", "B") or type(level) is not int or not 1 <= level <= 9:
        return DEFAULT
    if query == "MARGINAL":
        if not bits(z):
            return DEFAULT
        return z[:level] + (0,)*(9-level)
    if query == "FACTOR":
        if not bits(u) or any(u[k] for k in range(level-1, 9)):
            return DEFAULT
        return tuple(int(k == level-1) for k in range(9))
    if query == "LINEAR":
        if not bits(u) or not bits(y) or any(u[k] for k in range(level-1, 9)):
            return DEFAULT
        return tuple(y[k] if k == level-1 else 0 for k in range(9))
    return DEFAULT

def dec(n, x, y, a, b):
    return int(type(n) is int and n >= 1 and bits(x) and bits(y) and a == b == "")

def run_tests():
    assert samp(2, "DIMENSION") == 9
    assert samp(2, "FIELD") == 2
    all_vectors = list(product((0, 1), repeat=9))
    assert len(all_vectors) == 512
    for player in ("A", "B"):
        for z in all_vectors:
            previous = (0,)*9
            for j in range(1, 10):
                marginal = samp(2, "MARGINAL", player, j, z=z)
                factor = samp(2, "FACTOR", player, j, u=previous)
                linear = samp(2, "LINEAR", player, j, u=previous, y=z)
                assert factor == tuple(int(k == j-1) for k in range(9))
                assert marginal == tuple(z[k] if k < j else 0 for k in range(9))
                assert tuple(previous[k] ^ linear[k] for k in range(9)) == marginal
                previous = marginal
            assert previous == z
    pairs = [(z,z) for z in all_vectors]
    assert len(set(pairs)) == 512
    assert all(dec(2,x,y,"","") == 1 for x,y in pairs)
    assert dec(2,(0,)*9,(0,)*9,"1","") == 0
    assert samp(2,"FACTOR","A",4,u=(0,)*8) == DEFAULT
    assert samp(2,"MARGINAL","B",10,z=(0,)*9) == DEFAULT
    return {"dimension":9, "levels":9, "field":2, "pairs":512, "mass_each":"1/512",
            "classical_perfect_strategy":"both answers empty", "test_result":"PASS"}

if __name__ == "__main__":
    print(run_tests())
