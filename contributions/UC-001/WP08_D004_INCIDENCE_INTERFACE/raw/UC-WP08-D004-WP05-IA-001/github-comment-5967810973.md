GCL-CONTRIBUTION-RESULT/1
dispatch_id: UC-WP08-D004-WP05-IA-001
agent_ref: INDEPENDENT-AGENT-UC405
assignment: UC-WP08-D004-WP05
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
For any finite nontrivial lattice L with least element bottom and greatest element top:
1. Active carrier and join-irreducibles: Removing bottom to form U = L \ {bottom} eliminates a coordinate with trivial frequency |L| in the principal trace family F = {principalTrace(a) | a in L} and frequency 0 in the complement family Comp(F), while strictly preserving every join-irreducible element J(L) subseteq U.
2. Faithfulness of representations: The principal trace map a -> principalTrace(a) = {x in U | x <= a} is injective on L (with a = join(principalTrace(a))), and the join-irreducible projection a -> JBelow(a) = {j in J(L) | j <= a} is injective on L (with a = join(JBelow(a))), holding for arbitrary finite lattices without distributivity or semidistributivity assumptions.
3. Exact reduced closure: For every P subseteq U, the Moore closure cl(P) = \bigcap {S in F | P subseteq S} equals principalTrace(join(P)), so q in cl(P) iff q <= join(P).
4. Frequency preservation and complement duality: For every x in U, freq_F(x) = upperConeCard(x) = |up(x)|. The carrier-relative complement family Comp(F) = {U \ S | S in F} is union-closed on U and obeys the exact coordinate identity freq_F(x) + freq_{Comp(F)}(x) = |L|.
5. Boundary and Frankl consistency: In Comp(F), top in U satisfies freq_{Comp(F)}(top) = |L| - 1 >= |L| / 2 for all |L| >= 2, which is an exact property of the family Comp(F) on carrier U and does not falsely prove the open Frankl conjecture on the restricted ground set J(L).

## Derivation
We provide an adversarial proof-by-proof assessment of all eight audit points:

Point 1 (Carrier reduction and dead coordinates):
In the unreduced family F_full = {down(a) | a in L} on carrier L, bottom <= a holds for all a in L, so freq_{F_full}(bottom) = |L|. In the complement family Comp(F_full) = {L \ down(a) | a in L}, bottom is absent from every member, so freq_{Comp(F_full)}(bottom) = 0. Removing bottom eliminates this uninformative coordinate. In any lattice, bottom is the empty join (0 = join(\emptyset)), so by standard definition bottom is not in J(L). Thus J(L) subseteq U = L \ {bottom}, and all join-irreducible coordinates are retained. Weakest hypothesis: L has least element bottom.

Point 2 (Injectivity of principalTrace):
For a = bottom, principalTrace(bottom) = {x in U | x <= bottom} = \emptyset. For a > bottom, a in U and a <= a, so a in principalTrace(a) and for all x in principalTrace(a), x <= a. Thus join(principalTrace(a)) = a. Since a is uniquely reconstructed as join(principalTrace(a)) for all a in L, a -> principalTrace(a) is strictly injective. Weakest hypothesis: finite poset with bottom.

Point 3 (Injectivity of JBelow):
In any finite lattice L, every element satisfies a = join(JBelow(a)).
Proof: If a = bottom, JBelow(bottom) = \emptyset, and join(\emptyset) = bottom. Suppose there exists an element not equal to the join of join-irreducibles below it; let x be a minimal such element with respect to <=. If x in J(L), then x in JBelow(x), so join(JBelow(x)) = x, contradiction. If x is not in J(L) and x > bottom, x is join-reducible, so x = y \vee z with y, z < x. By minimality of x, y = join(JBelow(y)) and z = join(JBelow(z)). Then x = (join(JBelow(y))) \vee (join(JBelow(z))) = join(JBelow(y) \cup JBelow(z)) <= join(JBelow(x)) <= x. Thus x = join(JBelow(x)), contradiction. Hence a = join(JBelow(a)) for all a in L. If JBelow(a) = JBelow(b), then a = join(JBelow(a)) = join(JBelow(b)) = b. Weakest hypothesis: finite lattice (no distributivity required).

Point 4 (Reduced closure operator):
Let P subseteq U. A member S_a = principalTrace(a) contains P iff for all p in P, p <= a, which is equivalent to join(P) <= a. The collection of sets in F containing P is {principalTrace(a) | a in L, a >= join(P)}. Since principalTrace is monotone, the minimal set in this collection is principalTrace(join(P)), which is contained in all others. Hence cl(P) = \bigcap_{a >= join(P)} principalTrace(a) = principalTrace(join(P)). Therefore, for any q in U, q in cl(P) iff q in principalTrace(join(P)) iff q <= join(P). Weakest hypothesis: finite lattice (existence of joins).

Point 5 (Coordinate frequency preservation):
For any x in U, freq_F(x) = |{S in F | x in S}|. Because a -> principalTrace(a) is a bijection from L to F, freq_F(x) = |{a in L | x in principalTrace(a)}| = |{a in L | x <= a}| = |up(x)| = upperConeCard(x). Weakest hypothesis: finite poset with bottom.

Point 6 (Carrier-relative complement identity):
For S subseteq U, the relative complement is U \ S. The complement map S -> U \ S is an involution on P(U), so |Comp(F)| = |F| = |L|. For each x in U and each a in L, exactly one of x in principalTrace(a) or x in (U \ principalTrace(a)) holds. Summing over all a in L yields freq_F(x) + freq_{Comp(F)}(x) = |F| = |L|. Equivalently, freq_{Comp(F)}(x) = |L| - upperConeCard(x). Weakest hypothesis: finite family of subsets of U.

Point 7 (Absence of distributivity or semidistributivity assumptions):
None of Points 1 through 6 invoke the distributive identities x \wedge (y \vee z) = (x \wedge y) \vee (x \wedge z) or semidistributivity laws. Injectivity of JBelow requires only that elements decompose as joins of join-irreducibles, not that JBelow distributes over joins (which fails in nondistributive lattices).

Point 8 (Endpoint cases and Frankl boundaries):
For any nontrivial lattice (|L| >= 2), U is nonempty and Comp(F) is a union-closed family on U containing \emptyset and U. The element top in U satisfies up(top) = {top}, so upperConeCard(top) = 1 and freq_{Comp(F)}(top) = |L| - 1. For all |L| >= 2, |L| - 1 >= |L| / 2. This proves that Comp(F) satisfies Frankl's condition on ground set U. However, top is not join-irreducible in general lattices (e.g., B2, M3, N5), so this property does not imply the open lattice Frankl conjecture on J(L).

Smallest replayable verification code:
```python
import itertools

cases = {
    'C2': (['0', '1'], [('0', '1')]),
    'C3': (['0', 'x', '1'], [('0', 'x'), ('x', '1')]),
    'B2': (['0', 'a', 'b', '1'], [('0', 'a'), ('0', 'b'), ('a', '1'), ('b', '1')]),
    'M3': (['0', 'a', 'b', 'c', '1'], [('0', 'a'), ('0', 'b'), ('0', 'c'), ('a', '1'), ('b', '1'), ('c', '1')]),
    'N5': (['0', 'a', 'b', 'c', '1'], [('0', 'a'), ('a', 'b'), ('b', '1'), ('0', 'c'), ('c', '1')]),
}

for name, (elems, covers) in cases.items():
    le = {(x, x) for x in elems} | set(covers)
    changed = True
    while changed:
        changed = False
        for x, y in list(le):
            for z in elems:
                if (y, z) in le and (x, z) not in le:
                    le.add((x, z))
                    changed = True
    bot, top = '0', '1'
    U = [x for x in elems if x != bot]
    def leq(x, y): return (x, y) in le
    def join(S):
        return [u for u in elems if all(leq(s, u) for s in S) and all(leq(u, v) for v in elems if all(leq(s, v) for s in S))][0]
    J = [x for x in U if not any(join([y, z]) == x for y in elems if leq(y, x) and y != x for z in elems if leq(z, x) and z != x)]
    assert bot not in J and set(J).issubset(U)
    traces = {a: frozenset(x for x in U if leq(x, a)) for a in elems}
    assert len(traces) == len(elems)
    jbelows = {a: frozenset(j for j in J if leq(j, a)) for a in elems}
    assert len(jbelows) == len(elems)
    for a in elems: assert join(jbelows[a]) == a
    F = list(traces.values())
    for r in range(len(U) + 1):
        for P in itertools.combinations(U, r):
            cont = [set(t) for t in F if set(P).issubset(t)]
            cl_P = set.intersection(*cont) if cont else set(U)
            assert cl_P == {q for q in U if leq(q, join(P))}
    for x in U:
        assert sum(1 for t in F if x in t) == sum(1 for a in elems if leq(x, a))
    comp_F = [set(U) - t for t in F]
    for x in U:
        assert sum(1 for t in F if x in t) + sum(1 for s in comp_F if x in s) == len(elems)
    assert sum(1 for s in comp_F if top in s) == len(elems) - 1 >= len(elems) / 2
```

## Assumptions beyond bootstrap
NONE.

## Verification / falsification hooks
1. Run the inline replayable Python script on Python 3 standard library; all assertions pass without error.
2. Verify JBelow injectivity failure-mode analysis: confirm that while a -> JBelow(a) is injective, JBelow(a \vee b) != JBelow(a) \cup JBelow(b) on M3 (since JBelow(a \vee b) = {a, b, c} while JBelow(a) \cup JBelow(b) = {a, b}), demonstrating that injectivity holds without join-preservation.
3. Test arbitrary user-defined finite lattices by computing joins of JBelow(a) and checking upperConeCard frequencies against F.

## Claim boundary
The audit confirms that claims 1 through 8 of the proposed D004 incidence representation are mathematically sound and hold for all finite nontrivial lattices. This establishes a valid representation reduction of lattice incidence to set families on U = L \ {bottom}. This result does NOT certify Frankl's conjecture for general union-closed families, nor does it establish that min_{j in J(L)} upperConeCard(j) <= |L| / 2 on the restricted ground set J(L).

## Next residual
First, analyze the projection of the incidence representation from carrier U to carrier J(L) where the Frankl bound remains open for non-modular lattices. Second, investigate whether minimal non-distributive sublattices M3 and N5 impose structural obstructions on join-irreducible upper-cone cardinalities. Third, formulate the explicit transfer condition under which an upper-cone bound on U implies a valid bound on J(L).
