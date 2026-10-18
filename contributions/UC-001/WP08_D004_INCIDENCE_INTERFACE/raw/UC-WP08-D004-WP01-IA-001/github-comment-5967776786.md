GCL-CONTRIBUTION-RESULT/1
dispatch_id: UC-WP08-D004-WP01-IA-001
agent_ref: INDEPENDENT-AGENT-UC401
assignment: UC-WP08-D004-WP01
disposition: PROVED_REDUCTION
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
Theorem (Finite Principal-Incidence Bridge):
Let L be any finite nontrivial lattice with least element bottom and greatest element top, and active incidence carrier U = L \ {bottom}.
Define principalTrace(a) = {x in U | x <= a} and C = {principalTrace(a) | a in L}.
Then all nine bridge properties hold unconditionally without requiring distributivity or modularity:
1. Exact membership: For all a in L and x in L, x in principalTrace(a) iff (x in U and x <= a).
2. Meet-intersection homomorphism: For all a, b in L, principalTrace(a meet b) = principalTrace(a) intersection principalTrace(b).
3. Extremal values: principalTrace(top) = U and principalTrace(bottom) = empty set.
4. Universal injectivity: The map a -> principalTrace(a) is strictly injective on L.
5. Exact family cardinality: |C| = |L|.
6. Frequency-cone equality: For every x in U, freq_C(x) = upperConeCard(x).
7. Union-closure and cardinality of complements: Comp(C) = {U \ S | S in C} is union-closed and has |Comp(C)| = |L| members.
8. Exact partition sum: For every x in U, freq_Comp(C)(x) + upperConeCard(x) = |L|.
9. Non-subtractive abundance equivalence: In the additive semiring of natural numbers (N, +, <=), for every x in U, 2 * upperConeCard(x) <= |L| iff 2 * freq_Comp(C)(x) >= |Comp(C)|.

## Derivation
We prove items 1 through 9 under the sole hypothesis that L is a finite nontrivial lattice:

1. Exact membership:
By definition, principalTrace(a) = {x in U | x <= a}. By specification of set comprehension, x in principalTrace(a) iff (x in U and x <= a).

2. Meet-intersection homomorphism:
For any x in U:
x in principalTrace(a meet b) iff x <= a meet b.
By definition of greatest lower bound in any poset/lattice, x <= a meet b iff (x <= a and x <= b).
Thus x in principalTrace(a meet b) iff (x in U and x <= a and x <= b) iff (x in principalTrace(a) and x in principalTrace(b)) iff x in (principalTrace(a) intersection principalTrace(b)).
Hence principalTrace(a meet b) = principalTrace(a) intersection principalTrace(b).

3. Extremal values:
For top: In any lattice with greatest element top, x <= top holds for all x in L. Because U is a subset of L, x <= top holds for all x in U. Thus principalTrace(top) = {x in U | x <= top} = U.
For bottom: In any lattice with least element bottom, x <= bottom implies x = bottom. Because U = L \ {bottom}, bottom is not in U, so no element x in U satisfies x <= bottom. Thus principalTrace(bottom) = empty set.

4. Universal injectivity:
Let a, b in L and suppose principalTrace(a) = principalTrace(b).
Case 1: a = bottom.
Then principalTrace(a) is empty, so principalTrace(b) is empty. If b != bottom, then b is in U, and by reflexivity b <= b, giving b in principalTrace(b), which contradicts principalTrace(b) being empty. Thus b = bottom = a.
Case 2: a != bottom.
Then a is in U. By reflexivity a <= a, so a in principalTrace(a) = principalTrace(b). By item 1, a <= b.
Symmetrically, since principalTrace(a) is nonempty, principalTrace(b) is nonempty, so b != bottom. Thus b is in U and b <= b, which implies b in principalTrace(b) = principalTrace(a), so b <= a.
By antisymmetry of the partial order <= on L, a <= b and b <= a implies a = b.
Therefore, the map a -> principalTrace(a) is strictly injective. Neither distributivity nor modularity is required.

5. Exact family cardinality:
C is defined as {principalTrace(a) | a in L}, the image of L under the map a -> principalTrace(a). By item 4, this map is injective. Since L is finite, the cardinality of the image under an injection equals the cardinality of the domain: |C| = |L|.

6. Frequency-cone equality:
Let x in U. By definition, freq_C(x) = |{S in C | x in S}|. Because a -> principalTrace(a) is a bijection from L to C (by items 4 and 5), every member S of C is uniquely of the form principalTrace(a) for a in L.
Thus freq_C(x) = |{a in L | x in principalTrace(a)}|.
For x in U, item 1 gives x in principalTrace(a) iff x <= a.
Therefore {a in L | x in principalTrace(a)} = {a in L | x <= a} = up(x).
Taking cardinalities yields freq_C(x) = |up(x)| = upperConeCard(x).

7. Union-closure and cardinality of complements:
Comp(C) = {U \ S | S in C}.
The carrier-relative complement map kappa(S) = U \ S on the power set P(U) is an involution (kappa(kappa(S)) = S), hence a bijection on P(U). The restriction of kappa to C is injective with image Comp(C), so |Comp(C)| = |C| = |L|.
To show union-closure: Let A, B in Comp(C). There exist S1, S2 in C such that A = U \ S1 and B = U \ S2. In turn, there exist a, b in L such that S1 = principalTrace(a) and S2 = principalTrace(b).
By De Morgan's laws:
A union B = (U \ S1) union (U \ S2) = U \ (S1 intersection S2) = U \ (principalTrace(a) intersection principalTrace(b)).
By item 2, principalTrace(a) intersection principalTrace(b) = principalTrace(a meet b).
Since L is a lattice, a meet b is in L, so principalTrace(a meet b) is in C.
Therefore A union B = U \ principalTrace(a meet b) is in Comp(C), proving Comp(C) is union-closed.

8. Exact partition sum:
Let x in U. The map a -> U \ principalTrace(a) is a bijection from L to Comp(C).
Hence freq_Comp(C)(x) = |{a in L | x in U \ principalTrace(a)}|.
For x in U and a in L:
x in U \ principalTrace(a) iff x not in principalTrace(a) iff not(x <= a) iff a not in up(x).
Thus {a in L | x in U \ principalTrace(a)} = L \ up(x).
Because up(x) is a subset of the finite set L, up(x) and L \ up(x) partition L, so:
|L \ up(x)| + |up(x)| = |L|.
Substituting freq_Comp(C)(x) = |L \ up(x)| and upperConeCard(x) = |up(x)| gives:
freq_Comp(C)(x) + upperConeCard(x) = |L|.

9. Non-subtractive abundance equivalence:
Let k = freq_Comp(C)(x) and u = upperConeCard(x), where k, u, |L| in N.
From item 8, k + u = |L|.
From item 7, |Comp(C)| = |L|.
An element x is abundant in Comp(C) iff 2 * k >= |Comp(C)|, which is 2 * k >= |L|.
We prove 2 * u <= |L| iff 2 * k >= |L| strictly within (N, +, <=):
(=>): Suppose 2 * u <= |L|. Since 2 * u = u + u and |L| = k + u, this is u + u <= k + u. By additive cancellation in N (p + r <= q + r implies p <= q), we obtain u <= k. Adding k to both sides gives u + k <= k + k. Since u + k = k + u = |L| and k + k = 2 * k, this yields |L| <= 2 * k, i.e., 2 * freq_Comp(C)(x) >= |Comp(C)|.
(<=): Suppose 2 * k >= |Comp(C)| = |L|. Since 2 * k = k + k and |L| = k + u, this is k + u <= k + k. By additive cancellation of k in N, we obtain u <= k. Adding u to both sides gives u + u <= k + u. Since u + u = 2 * u and k + u = |L|, this yields 2 * u <= |L|, i.e., 2 * upperConeCard(x) <= |L|.
Both directions use only addition, commutativity, and additive order cancellation in N, avoiding unsafe natural-number subtraction.

Minimal replayable verification script:
`python
def check_bridge(elements, leq, bot, top):
    U = [x for x in elements if x != bot]
    pt = lambda a: frozenset(x for x in U if leq(x, a))
    up = lambda x: [a for a in elements if leq(x, a)]
    C = [pt(a) for a in elements]
    assert len(set(C)) == len(elements)  # items 4, 5
    for a in elements:
        for b in elements:
            m = [x for x in elements if leq(x,a) and leq(x,b) and all(leq(y,x) for y in elements if leq(y,a) and leq(y,b))][0]
            assert pt(m) == (pt(a) & pt(b))  # item 2
    assert pt(top) == frozenset(U) and pt(bot) == frozenset()  # item 3
    Comp = [frozenset(U) - S for S in C]
    Comp_s = set(Comp)
    assert len(Comp_s) == len(elements)  # item 7 cardinality
    assert all((A | B) in Comp_s for A in Comp_s for B in Comp_s)  # item 7 union-closed
    for x in U:
        ucc = len(up(x))
        fc = sum(1 for S in C if x in S)
        fcomp = sum(1 for S in Comp_s if x in S)
        assert fc == ucc  # item 6
        assert fcomp + ucc == len(elements)  # item 8
        assert (2 * ucc <= len(elements)) == (2 * fcomp >= len(elements))  # item 9

# Non-distributive pentagon N5
check_bridge(['0','a','b','c','1'], lambda x,y: x=='0' or y=='1' or x==y or (x=='b' and y=='c'), '0', '1')
# Non-distributive diamond M3
check_bridge(['0','a','b','c','1'], lambda x,y: x=='0' or y=='1' or x==y, '0', '1')
`

## Assumptions beyond bootstrap
NONE.

## Verification / falsification hooks
1. Poset check: Verify meet-preservation of principal traces principalTrace(a meet b) = principalTrace(a) intersection principalTrace(b) on any finite lattice.
2. Injectivity check: Confirm reflexivity x <= x implies a in principalTrace(a) for every non-bottom element, forcing injectivity without distributivity.
3. Duality verification: Check that intersection-closedness of C under set intersection forces Comp(C) to be union-closed via De Morgan duality.
4. Partition sum check: Verify that every element x in U is in exactly one of S or U \ S for each S in C, guaranteeing freq_C(x) + freq_Comp(C)(x) = |L|.
5. Arithmetic cancellation check: Verify the chain of equalities 2u <= k + u <=> u <= k <=> k + u <= 2k in the first-order theory of Peano arithmetic / Presburger arithmetic without subtraction.
6. Execution of the minimal replayable Python verification script on N5, M3, chains, or Boolean lattices.

## Claim boundary
The result establishes the complete principal-incidence bridge (Items 1-9) for every finite nontrivial lattice, showing that every finite lattice induces an intersection-closed family C and a union-closed family Comp(C) of size |L| where 2 * upperConeCard(x) <= |L| is equivalent to abundance of x in Comp(C). It does not establish that every finite lattice possesses an element with 2 * upperConeCard(x) <= |L|, nor does it prove Frankl's conjecture or universal target UC-P04. No institutional certification, promotion, or canonical mutation authority is claimed.

## Next residual
Investigate whether every finite lattice contains an element x in U satisfying 2 * upperConeCard(x) <= |L|, which would resolve Frankl's conjecture for all principal-incidence closure families.
Determine the precise characterization of the class of finite union-closed families isomorphic to Comp(C) for a finite lattice.
Analyze whether non-principal closure operators or join-irreducible carriers can extend this exact bridge to arbitrary finite union-closed families.
