# FIGURATE WP09-011 — diagonal-anchor incompleteness at the binary prime

**Programme:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). This tranche distinguishes a sufficient **square-shift global-existence constructor** from necessary conditions for Type B solvability, and separates *local* residue compatibility from actual positive-integer triples. All claims are internally derived research candidates, not external literature priority or independent MATHCERT certification.

## The uniform binary non-diagonal theorem

For any polygonal order k divisible by four, and any offset c≡2 (mod 4):

1. There exist **no integers** u,a (of any sign, including zero) with c=P_k(u)−a². In fact no such relation exists modulo four.
2. There is **no diagonal Type B local witness modulo four**: three entries sharing a residue x cannot have x²+c congruent to a k-gonal number.
3. Nevertheless, there is a **simultaneous non-diagonal Type B witness modulo four**, with entry residues (1,2,3) and positive polygonal-index residues (4,1,4).

**Proof.** The exact polynomial identity

    P_k(u)−u²=(k−4)u(u−1)/2

shows that when 4 divides k, the difference is divisible by four for **every integer u**. Thus P_k(u)≡u² (mod 4), so all k-gonal residues are 0 or 1 modulo four, and the set of differences P_k(u)−a² modulo four is precisely {0,1,3}. In particular residue 2 is absent. For c≡2 (mod4), every x²+c lies in {2,3}, so diagonal compatibility is impossible.

Now choose entry residues a=1,b=2,d=3 and take polygonal-index residues r=4,s=1,t=4. Their shifted pair products are

    ab+c≡0, ad+c≡1, bd+c≡0 (mod 4),

and P_k(4)≡0, P_k(1)≡1. Hence all three congruences hold simultaneously. QED.

This is a universal failure of the **diagonal-witness equivalence at the binary prime** for orders divisible by four. It does not contradict the protected WP09-006 theorem: that theorem proves the equivalence for odd prime powers only.

## Genuine exact integer solutions beyond the square-shift family

Non-diagonal congruence compatibility is not automatically exact integer existence. We therefore supply independently checkable **exact** Type B triples whose offsets cannot be represented as P_k(u)−a²:

| k | c | entries (a,b,d) | polygonal indices (r,s,t) | pair outputs |
| --- | ---: | --- | --- | --- |
| 4 | 2 | (1,7,14) | (3,4,10) | 9,16,100 |
| 20 | 2 | (1,18,13375) | (2,39,164) | 20,13377,240752 |
| 36 | 2 | (1,343,6478) | (5,20,362) | 345,6480,2221956 |

For k=36, P_36(t)=17t²−16t. The identities are exact:

    1*343+2=345=P_36(5),
    1*6478+2=6480=P_36(20),
    343*6478+2=2221956=P_36(362).

For k=20 and 36, the second entries 18 and 343 are nonsquares. Therefore the already protected **WP09-008 Pell amplification theorem** applies, providing infinitely many distinct exact Type B triples with each same fixed first pair and offset 2. The new 36-gonal seed is an additional explicit exact integer family not required by WP09-010.

The square order k=4 supplies a much broader exact result: for **every** integer c≡2 modulo four (indeed for all signed c), and every sufficiently large t,

    (a,b,d)=(1,t²−c,(t+1)²−c)

is an exact Type B triple with polygonal indices

    (r,s,t_3)=(t,t+1,t(t+1)−c),

since the three shifted products are the squares t², (t+1)², and [t(t+1)−c]². The infinite offset family c≡2 (mod4) is **disjoint** from the WP09-010 square-shift hypothesis, yet every one of its parameter pairs at k=4 is globally realizable.

## Interpretation and precise boundary

The square-shift representation c=P_k(u)−a² is the existence of an exact **diagonal algebraic anchor**, not a necessary condition for an exact Type B triple. Failure of that representation, even for a uniform congruence reason, does **not** establish a Type B obstruction.

At odd prime powers, the prior WP09-006 theorem proves that whenever any Type B triple is locally possible, a diagonal residue witness is locally possible. At the binary prime, this fails: non-diagonal entry residue patterns genuinely enlarge the local solution set.

The distinction is substantive for the programme's local-to-global analysis. A valid global nonexistence claim needs to rule out **all three-entry patterns**, not just the convenient diagonal seed used by WP09-009/010. Conversely, any exact triple supplies a compatible residue tuple modulo every prime power automatically.

This result does NOT prove global existence for every k divisible by four and c≡2 (mod4). In particular we do not extrapolate the seeds at k=4,20,36 to all such k. Nor do we assert that the general local-to-global problem is resolved.

## Executable and checking obligations

- [Classifier and exact seed calculator](../research/figurate_wp09_nondiagonal_anchor_gap.py) validates the mod-four theorem and each exact positive-integer tuple. It integrates the protected WP09-008 Pell amplification when k is 20 or 36.
- [Independent integer arithmetic tests](../tests/test_figurate_wp09_nondiagonal_anchor_gap.py) check 40 polygonal orders and multiple positive/negative offsets c≡2 (mod4), direct modular and polynomial evaluations, exact Euler tuples for multiple offsets, and multiple exact Pell iterates at k=20,36.

Run on repository exact candidate head:

    python3 -m unittest -v tests.test_figurate_wp09_nondiagonal_anchor_gap
    python3 -m research.figurate_wp09_nondiagonal_anchor_gap --order 36 --offset 2

**Next mathematical frontier:** investigate the genuinely unresolved orders (e.g. k divisible four but not yet carrying an exact seed at c≡2 mod4). Distinguish a failed repeated-entry anchor, a genuine prime-power obstruction to all triples, and an actual global nonexistence theorem. Any external-originality claim awaits source-critical literature comparison. Routine protected producer integration must not be mislabeled MATHCERT certification.
