"""PNP-ABOVE WP01: explicit-table classical-game to SAT reduction.

Not an implementation of MIP*=RE compression. No quantum-strategy claims.
Uses only Python standard library. Run: python3 WP01_EXPLICIT_GAME_SAT_TRANSFER.py
"""
from dataclasses import dataclass
from itertools import combinations, product


@dataclass(frozen=True)
class Game:
    alice_questions: tuple
    bob_questions: tuple
    alice_answers: tuple
    bob_answers: tuple
    support: tuple  # positive-probability (x,y) pairs only
    accepts: object  # bool predicate(x,y,a,b)


def encode(game):
    """Exactly-one answer per question and no forbidden answer pair.

    Output clauses (signed integer literals), variable id -> (player,q,answer).
    Complexity polynomial in the EXPLICIT question/answer/acceptance table.
    """
    names = []
    for player, questions, answers in (
        ("A", game.alice_questions, game.alice_answers),
        ("B", game.bob_questions, game.bob_answers),
    ):
        for q in questions:
            for a in answers:
                names.append((player, q, a))
    assert len(set(names)) == len(names)
    ids = {name: i + 1 for i, name in enumerate(names)}
    clauses = []
    for player, questions, answers in (
        ("A", game.alice_questions, game.alice_answers),
        ("B", game.bob_questions, game.bob_answers),
    ):
        for q in questions:
            vs = [ids[(player, q, a)] for a in answers]
            clauses.append(tuple(vs))  # at least one
            clauses.extend((-u, -v) for u, v in combinations(vs, 2))
    for x, y in game.support:
        for a in game.alice_answers:
            for b in game.bob_answers:
                if not game.accepts(x, y, a, b):
                    clauses.append((-ids[("A", x, a)], -ids[("B", y, b)]))
    return tuple(clauses), tuple(names)


def simplify(clauses, assignments):
    out = []
    for c in clauses:
        if any((abs(lit) in assignments and assignments[abs(lit)] == (lit > 0)) for lit in c):
            continue
        residual = tuple(lit for lit in c if abs(lit) not in assignments)
        if not residual:
            return None
        out.append(residual)
    return out


def solve(clauses, nvars, fixed=()):
    """Independent baseline DPLL SAT oracle, not polynomial time in general."""
    assignments = {}
    for lit in fixed:
        v, val = abs(lit), lit > 0
        if v in assignments and assignments[v] != val:
            return None
        assignments[v] = val

    def visit(assignment):
        while True:
            remaining = simplify(clauses, assignment)
            if remaining is None:
                return None
            if not remaining:
                return assignment
            units = [c[0] for c in remaining if len(c) == 1]
            if not units:
                break
            next_assignment = dict(assignment)
            for lit in units:
                v, val = abs(lit), lit > 0
                if v in next_assignment and next_assignment[v] != val:
                    return None
                next_assignment[v] = val
            assignment = next_assignment
        # Pick the shortest clause; this is a practical heuristic only.
        lit = min(remaining, key=len)[0]
        for val in (lit > 0, lit < 0):
            a2 = dict(assignment)
            a2[abs(lit)] = val
            out = visit(a2)
            if out is not None:
                return out
        return None

    partial = visit(assignments)
    if partial is None:
        return None
    return {v: partial.get(v, False) for v in range(1, nvars + 1)}


def self_reduce(clauses, nvars, sat_oracle):
    """At most nvars+1 SAT-decision calls; each query fixes a prefix."""
    calls = 1
    if not sat_oracle(clauses, nvars, ()):  # unsatisfiable
        return None, calls
    prefix = []
    for v in range(1, nvars + 1):
        calls += 1
        if sat_oracle(clauses, nvars, tuple(prefix + [-v])):
            prefix.append(-v)
        else:
            prefix.append(v)
    return {v: v in prefix for v in range(1, nvars + 1)}, calls


def decode_strategy(game, names, assignment):
    strategy = {}
    for i, name in enumerate(names, start=1):
        if assignment.get(i, False):
            player, question, answer = name
            assert (player, question) not in strategy
            strategy[(player, question)] = answer
    assert len(strategy) == len(game.alice_questions) + len(game.bob_questions)
    assert all(game.accepts(x, y, strategy[("A", x)], strategy[("B", y)]) for x, y in game.support)
    return strategy


def magic_square():
    qs = (0, 1, 2)
    even = tuple(t for t in product((0, 1), repeat=3) if sum(t) % 2 == 0)
    odd = tuple(t for t in product((0, 1), repeat=3) if sum(t) % 2 == 1)
    # Answer alphabet is tagged (parity-class, triple); enforce parity in predicate.
    answers = tuple((tag, t) for tag, subset in ((0, even), (1, odd)) for t in subset)
    def accepts(r, c, a, b):
        return (a[0] == 0 and b[0] == int(c == 2) and a[1][c] == b[1][r])
    return Game(qs, qs, answers, answers, tuple(product(qs, qs)), accepts)


def diagonal_identity(n=9):
    qs = tuple(product((0, 1), repeat=n))
    return Game(qs, qs, ((),), ((),), tuple((q, q) for q in qs), lambda x, y, a, b: x == y and a == b == ())


def compatible_example():
    return Game((0, 1), (0, 1), (0, 1), (0, 1), tuple(product((0, 1), repeat=2)), lambda x, y, a, b: a == x and b == y)


def run_tests():
    g = compatible_example()
    cnf, names = encode(g)
    model, calls = self_reduce(cnf, len(names), lambda f, n, prefix: solve(f, n, prefix) is not None)
    assert model is not None and calls <= len(names) + 1
    strategy = decode_strategy(g, names, model)
    assert strategy[("A", 0)] == 0 and strategy[("B", 1)] == 1

    m = magic_square()
    mcnf, mn = encode(m)
    assert len(mn) == 48 and len(mcnf) == 678  # 6 eight-way exact-one groups + 504 forbidden tuples
    assert solve(mcnf, len(mn)) is None
    assert self_reduce(mcnf, len(mn), lambda f, n, prefix: solve(f, n, prefix) is not None) == (None, 1)
    # Exact classical 8/9 witness from zero rows, first two zero columns, last column (1,0,0).
    alice = {r: (0, (0, 0, 0)) for r in range(3)}
    bob = {0: (0, (0, 0, 0)), 1: (0, (0, 0, 0)), 2: (1, (1, 0, 0))}
    assert sum(m.accepts(r, c, alice[r], bob[c]) for r, c in m.support) == 8

    d = diagonal_identity(9)
    dcnf, dn = encode(d)
    assert len(dn) == 1024 and len(dcnf) == 1024
    dmodel = solve(dcnf, len(dn))
    assert dmodel is not None
    decode_strategy(d, dn, dmodel)
    return {
        "compatible": {"variables": len(names), "clauses": len(cnf), "sat_calls": calls, "perfect": True},
        "magic_square": {"variables": len(mn), "clauses": len(mcnf), "perfect_classical": False, "optimum_win_fraction": "8/9"},
        "nine_level_identity": {"support": len(d.support), "variables": len(dn), "clauses": len(dcnf), "perfect_classical": True},
        "full_quantum_compressor_executed": False,
    }


if __name__ == "__main__":
    import json
    print(json.dumps(run_tests(), indent=2, sort_keys=True))
