GCL-CONTRIBUTION-RESULT/1
dispatch_id: UC-WP08-D004-WP03-IA-001
agent_ref: INDEPENDENT-AGENT-UC403
assignment: UC-WP08-D004-WP03
disposition: FORMAL_LEMMA_PROVED
context_class: ZERO_CONTEXT
external_sources: PROTECTED_PACKET_ONLY
timebox_observed: YES

## Strongest exact statement
1. Target Closure Characterization (Proved):
Let L be a finite nontrivial lattice with least element bottom and greatest element top. Let J be the set of join-irreducible elements of L. For a in L, let JBelow(a) = {j in J | j <= a}. Let CJ = {JBelow(a) | a in L}.
For any P subset J, the closure cl(P) = intersection { S in CJ | P subseteq S } satisfies:
cl(P) = JBelow(join(P)),
where join(P) is the finite supremum in L with join(empty) = bottom.
Consequently, for every finite P subset J and q in J:
q in cl(P) iff q <= join(P).

2. Exact Implication Criterion (Proved):
An implication P -> q (with P subset J and q in J) is valid in every member of CJ (i.e., for all S in CJ, P subseteq S implies q in S) if and only if:
q <= join(P).

3. Unary Specialization:
For p, q in J:
{p} -> q is valid in every member of CJ iff q <= p.
Hence unary implications between join-irreducibles coincide exactly with the partial order of L restricted to J.

4. Characterization of Genuinely Non-Unary Valid Implications:
A valid implication P -> q is genuinely non-unary (meaning q <= join(P) and q is not below any individual p in P) if and only if:
join_{p in P} (q meet p) <= q_* < q <= join(P),
where q_* = join { x in L | x < q } is the unique lower cover of q in L.
In particular, genuinely non-unary valid implications exist in L if and only if L is non-distributive.

5. Irredundancy of Premise-Minimal Implications:
An implication P -> q is premise-minimal if q <= join(P) and for all proper subsets P' strictly subset P, q not <= join(P').
Premise-minimality strictly entails that:
(i) P is an antichain in (J, <=),
(ii) P is join-irredundant (for every p in P, p not <= join(P \ {p})), and
(iii) q not in P whenever |P| >= 2.
Therefore, premise-minimal non-unary implications require NO additional irredundancy condition beyond premise-minimality itself.

## Derivation
1. Foundation: Finite Lattice Representation by Join-Irreducibles:
In a finite lattice L, an element j in L is join-irreducible (j in J) if j != bottom and for all x, y in L, j = x join y implies j = x or j = y. Equivalently, j covers a unique lower element j_* = join { x in L | x < j } < j.
Every element a in L is the join of the join-irreducibles below it: a = join(JBelow(a)).
Proof: If a = bottom, JBelow(bottom) is empty, and join(empty) = bottom. If there were elements with a != join(JBelow(a)), choose a minimal such element a. If a in J, then a in JBelow(a), so join(JBelow(a)) = a, contradiction. If a not in J and a != bottom, a is reducible, so a = x join y with x, y < a. By minimality, x = join(JBelow(x)) and y = join(JBelow(y)), so a = join(JBelow(x) union JBelow(y)) <= join(JBelow(a)) <= a, giving a = join(JBelow(a)), a contradiction.
Furthermore, the map a |-> JBelow(a) is an order-isomorphism from (L, <=) to (CJ, subseteq):
a <= b iff JBelow(a) subseteq JBelow(b), and JBelow(a meet b) = JBelow(a) intersection JBelow(b).
Thus CJ is a closure system (closed under arbitrary intersections).

2. Proof of Target cl(P) = JBelow(join(P)):
Let P subset J. By definition:
cl(P) = intersection { S in CJ | P subseteq S }.
Since every S in CJ is of the form S = JBelow(a) for some a in L:
P subseteq JBelow(a) iff for all p in P, p <= a iff join(P) <= a.
Therefore:
cl(P) = intersection { JBelow(a) | a in L, join(P) <= a }
      = JBelow( meet { a in L | join(P) <= a } ).
The family { a in L | join(P) <= a } has a unique least element, which is join(P).
Hence:
cl(P) = JBelow(join(P)).
It follows immediately that for any q in J:
q in cl(P) iff q in JBelow(join(P)) iff q <= join(P).

3. Exact Implication Criterion:
By standard semantics of closure systems, an implication P -> q is valid in CJ iff every S in CJ that contains P also contains q:
(for all S in CJ, P subseteq S implies q in S)
iff q in intersection { S in CJ | P subseteq S } = cl(P)
iff q <= join(P).

4. Unary Premises:
For P = {p} with p in J, join({p}) = p.
Thus {p} -> q is valid in CJ iff q <= p.

5. Genuinely Non-Unary Implications:
A valid implication P -> q is genuinely non-unary iff q <= join(P) and for all p in P, q not <= p.
Since q in J has a unique lower cover q_*, the condition q not <= p is equivalent to q meet p < q, which is equivalent to q meet p <= q_*.
Taking the join over all p in P gives join_{p in P} (q meet p) <= q_*.
Hence the exact separation condition is:
join_{p in P} (q meet p) <= q_* < q <= join(P).
If L were distributive, q meet join(P) = join_{p in P} (q meet p). But q <= join(P) implies q meet join(P) = q, which would force q <= q_*, a contradiction. Thus genuinely non-unary implications can only exist in non-distributive lattices.

6. Irredundancy in Premise-Minimal Implications:
Suppose P -> q is premise-minimal with |P| >= 2, meaning q <= join(P) and for every proper subset P' strictly subset P, q not <= join(P').
- If there exists p in P such that p <= join(P \ {p}), then join(P \ {p}) = join(P) >= q. Then P' = P \ {p} is a proper subset of P with q <= join(P'), violating premise-minimality. Thus P is join-irredundant.
- If p1 < p2 for distinct p1, p2 in P, then p1 <= join(P \ {p1}), which contradicts join-irredundancy. Thus P is an antichain.
- If q in P, then {q} strictly subset P satisfies q <= join({q}) = q, violating premise-minimality since |P| >= 2.
Thus premise-minimality alone is necessary and sufficient to eliminate all redundancies; no additional irredundancy condition is required.

7. Inline Minimal Replayable Code:
```python
def verify_wp03():
    # Lattice M3: 0 < a, b, c < 1 (non-distributive diamond)
    elems = ['0', 'a', 'b', 'c', '1']
    leq = {('0',x) for x in elems} | {(x,'1') for x in elems} | {(x,x) for x in elems}
    J = ['a', 'b', 'c']
    join = lambda S: '1' if len(S) >= 2 or '1' in S else (list(S)[0] if S else '0')
    CJ = [set(), {'a'}, {'b'}, {'c'}, {'a', 'b', 'c'}]
    
    # 1. Target check: cl(P) == JBelow(join(P))
    for P in [set(), {'a'}, {'a','b'}, {'a','b','c'}]:
        cl_P = set(J)
        for S in CJ:
            if P.issubset(S): cl_P &= S
        expected = {j for j in J if (j, join(P)) in leq}
        assert cl_P == expected
        
    # 2. Implication check: P -> q valid iff q <= join(P)
    for P in [{'a','b'}, {'a'}]:
        for q in J:
            valid = all(not P.issubset(S) or q in S for S in CJ)
            assert valid == ((q, join(P)) in leq)
            
    # 3. Genuinely non-unary implication: {a, b} -> c
    assert (('c', join({'a', 'b'})) in leq) and ('c', 'a') not in leq and ('c', 'b') not in leq
    print("Verification passed.")

verify_wp03()
```

## Assumptions beyond bootstrap
NONE.

## Verification / falsification hooks
1. For any finite lattice L and subset P of J(L), compute cl(P) by intersection of all S in CJ containing P, and verify that cl(P) equals {j in J(L) | j <= join(P)}.
2. In the modular non-distributive lattice M3, test that {a, b} -> c is valid, premise-minimal, and join-irredundant, satisfying join_{p in {a,b}} (c meet p) = 0 <= c_* = 0 < c <= join({a, b}) = 1.
3. In any finite distributive lattice, verify that no valid implication P -> q can satisfy q not <= p for all p in P, proving no genuinely non-unary implications exist.

## Claim boundary
The derived results hold universally for all finite nontrivial lattices. They characterize the exact semantic validity of implications on the reduced join-irreducible closure system CJ over carrier J. They make no claim regarding frequency distributions on Comp(CJ), element rarity, or Frankl's conjecture. No formal certification or institutional authority is asserted.

## Next residual
1. Determine the canonical Guigues-Duquenne implication base of CJ directly from lattice-theoretic pseudo-intents.
2. Analyze how non-unary implications constrain member frequencies in Comp(CJ) compared to the distributive unary setting.
3. Investigate whether non-unary implication density provides an obstruction or an advantage for frequency balance in non-distributive lattices.
