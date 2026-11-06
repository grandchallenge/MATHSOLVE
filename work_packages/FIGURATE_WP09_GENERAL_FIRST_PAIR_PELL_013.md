# FIGURATE WP09-013 — arbitrary first-pair Pell amplification and exact frontier seeds

**Programme:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Claim:** actual exact positive-integer Type B triples, not merely finite-modulus congruence compatibility. Internal research proof; literature priority, formalization, independent specialist certification and universal local-to-global are NOT asserted.

## Theorem A — exact amplification for any nonsquare pair product

For any polygonal order k≥3 and integer offset c, suppose **an actual exact Type B seed** consists of three distinct positive integers (a,b,d) and positive integer indices (r,s,t), with

    ab+c=P_k(r), ad+c=P_k(s), bd+c=P_k(t),

where P_k(n)=((k−2)n²−(k−4)n)/2. If the **product ab** is nonsquare, then there are **infinitely many distinct exact positive Type B triples (a,b,d_j)** with the same first two entries a,b and the same k,c.

This strictly generalizes WP09-008's fixed-pair theorem, which imposed a=1 and nonsquare b. A second entry can be square as long as the product ab is nonsquare.

### Proof

Set

    R=2(k−2), L=k−4, D=8(k−2)c+L²,
    Q=ab, S=R s−L, T=R t−L, X=a T.

Use the exact quadratic identity

    (R n−L)²=8(k−2)P_k(n)+L².

Eliminating d from ad+c=P_k(s) and bd+c=P_k(t) gives

    P_k(t)=(b/a)P_k(s)+(1−b/a)c.

Multiplying the completed-square identity by a² proves the **integral generalized Pell norm equation**

    X²−Q S²=a(a−b)D.                 (1)

All coordinates X,S of the seed are strictly positive, and Q=ab is nonsquare by hypothesis.

Let U+V√Q>1 be a positive integral norm-one Pell unit, U²−Q V²=1, whose existence follows from the classical Pell theorem. Let M=2aR. Its integral multiplication map on the pair (X,S),

    (X,S) ↦ (U X+Q V S, V X+U S),

has determinant 1, so it is invertible modulo M. Consequently there is an exponent e≥1 (at most M²) such that the unit's e-th power acts as the identity modulo M. Apply its e*j-th power for j≥0 to the original positive (X,S). Every resulting (X_j,S_j) is integral, has unchanged norm (1), and satisfies

    X_j≡X (mod M), S_j≡S (mod M).

The first congruence ensures a divides X_j; define T_j=X_j/a. Since M=2aR, it also ensures T_j≡T (mod R), hence the index

    t_j=(T_j+L)/R

is an integer. The second congruence gives

    s_j=(S_j+L)/R ≡s (mod 2a).

Since P_k(n) is an integer-valued quadratic polynomial and s_j−s is divisible by 2a,

    P_k(s_j)−P_k(s) ≡0 (mod a).

The seed had a | P_k(s)−c, so

    d_j=(P_k(s_j)−c)/a

is an integer. Substituting (X_j,S_j) into (1) proves the third exact identity

    b d_j+c=P_k(t_j),

while ab+c=P_k(r) and a d_j+c=P_k(s_j) hold identically.

All S_j and X_j are strictly increasing because the Pell unit and initial coordinates are positive. Thus s_j→∞ and d_j→∞. For sufficiently large j, d_j is positive and differs from both a and b. Discard at most finitely many early collisions: the remaining infinitely many (a,b,d_j) are valid exact positive-integer Type B triples. QED.

**Scope:** existence of the original exact seed is required. The theorem gives no seed from purely local congruence data, and the square-product Q case is not treated by Pell amplification.

## Theorem B — independently checked exact seeds in the local-positive frontier

The protected WP09-012 sieve classifies all-place Type B compatibility for k divisible by four and c≡2 mod4. A bounded exact seed search gives the following **actual integral solutions**, independently verified using the original polygonal polynomial:

| k | c | entries (a,b,d) | indices (r,s,t) | exact pair outputs |
| --- | --- | --- | --- | --- |
| 52 | 2 | (2,25,703) | (2,8,27) | (52,1408,17577) |
| 116 | 2 | (1,2399,5602386) | (7,314,15356) | (2401,5602388,13440124016) |
| 36 | 6 | (1,30,715) | (2,7,36) | (36,721,21456) |

In particular, at order 52, the second entry **b=25 is square**, but the product ab=50 is nonsquare; this seed was not covered by the old WP09-008 restriction a=1. The new Theorem A therefore gives infinitely many actual exact 52-gonal Type B triples with fixed first pair (2,25), offset 2. For 116-gonal numbers, Q=2399 is nonsquare and the same theorem gives infinitely many exact triples. The 36-gonal offset-6 example also amplifies.

**Independent fixed-pair arithmetical readback:**
- k52,c2: P_52(2)=52=2·25+2, P_52(8)=1408=2·703+2, P_52(27)=17577=25·703+2.
- k116,c2: P_116(7)=2401, P_116(314)=5602388, P_116(15356)=13440124016=2399·5602386+2.
- k36,c6: P_36(2)=36, P_36(7)=721, P_36(36)=21456=30·715+6.

Each seed lies in an everywhere-locally-compatible parameter class by the protected WP09-012 sieve. The exact integral seed itself is much stronger than any collection of modular witnesses.

## Bounded negative searches — no unwarranted nonexistence claims

The exact search scans first entries a from a finite supplied list, first output indices r up to max_r, and second output indices s up to max_s, uses divisibility of P_k(r)−c and P_k(s)−c by a, and checks the third output using the exact integer square test

    [2(k−2)t−(k−4)]²=8(k−2)(bd+c)+(k−4)².

It records the precise integer bounds and number of candidate pairs tested. A negative result states only that **no seed occurred within those specified finite bounds**. In particular, the bounded scans for (k,c)=(68,6),(84,2),(100,2),(132,2) were initially negative; that supplies no global nonexistence proof, and no local-to-global counterexample.

An especially instructive comparison is k=52,c=2: searching only a=1 over r≤90,s≤2499 found no seed, but allowing a=2 produced the exact seed (2,25,703) already at r=2,s=8. Therefore **a=1 search failure cannot justify a general global obstruction**.

## Computational evidence and limitations

- Constructive fixed-pair amplifier and bounded exact seed search: research/figurate_wp09_fixed_pair_seed_frontier.py.
- Independent regression with a separately expressed polygonal polynomial, separate brute loop ordering, exact norm checks, locally admissible status checks, finite negative-search bounds and invalid-input guards: tests/test_figurate_wp09_fixed_pair_seed_frontier.py.
- Arithmetic independent of the producer was also evaluated with exact arbitrary-precision integers for the three new seeds, and for Pell steps 0,1,2 in each family. The residue-preserving Pell powers for k52 have modulus 400 and order 200, so the next tuple has hundreds of digits: large exact output size is not numerical uncertainty.

**Research boundary:** Theorem A is conditional on a genuine exact seed. Theorem B supplies several additional such seeds and explicit infinite families. Nothing in this tranche proves that every everywhere-locally-admissible pair has an exact integer triple, or gives any rigorously established everywhere-local/global failure. Literature novelty, external certification, and relation to the separate operation-safety-held WP09-011 merge are independent.
