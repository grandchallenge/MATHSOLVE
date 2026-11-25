# FIGURATE WP09-009 — global seed existence at polygonal-minus-one offsets

**Programme:** FIGURATE Type B, [WP09 tracker #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Claim scope:** actual distinct positive integer entries and actual positive integer polygonal indices. Internal mathematical proof and reproducible exact arithmetic. Neither published-literature originality nor independent MATHCERT certification is asserted.

## Universal exact seed-existence theorem

Let k≥3 be any polygonal order and u≥1 any integer. Define

    P_k(t)=((k−2)t²−(k−4)t)/2,
    c=P_k(u)−1.

**Theorem.** At this exact offset c, there are infinitely many actual Type B triples of distinct positive integers (a,b,d), with all three shifted pair products equal to k-gonal numbers at positive integer indices.

Stronger fixed-pair statement: for every (k,u) except (4,1), there are infinitely many distinct nonsquare integers b>1 of the form b=P_k(r)−c, and **for each such fixed b** infinitely many exact Type B triples (1,b,d) exist. For the exceptional pair (k,u)=(4,1), c=0 and infinitely many exact square-output triples exist directly.

This is an explicit **global existence** theorem, not a finite-modulus compatibility test and not a universal assertion about all offsets.

## Proof I: degenerate exact index seed and Pell promotion

Fix k,u and c=P_k(u)−1. Let r≥1 be any index such that

    b=P_k(r)−c>1

is not a square. The formal triple (1,b,1) has exact pair-output identities

    1*b+c=P_k(r),
    1*1+c=P_k(u),
    b*1+c=P_k(r).

It is deliberately **not** a Type B triple, since the first and third entries coincide. Nevertheless, the two latter polygonal identities give a genuine point on the generalized Pell conic, enabling promotion to distinct entries.

Set

    R=2(k−2), L=k−4,
    S=R*u−L, T=R*r−L,
    D=8(k−2)c+L².

The completed polygonal square yields

    T²−b S²=−(b−1)D.                      (1)

Both S and T are positive. Because b>1 is nonsquare, take a positive integral norm-one Pell unit U+V√b>1, so U²−bV²=1. Its multiplication matrix has determinant 1 and is therefore invertible modulo R. Some positive power e≤R² is the identity modulo R. Hence for every m≥1,

    T_m+S_m√b=(T+S√b)(U+V√b)^(e*m)

preserves (1), stays integral and strictly increases both positive coordinates. It also satisfies

    S_m≡T_m≡−L (mod R).

Thus

    s_m=(S_m+L)/R,
    t_m=(T_m+L)/R,
    d_m=P_k(s_m)−c

are integers, with s_m,t_m positive, and the original exact identity (1) implies

    b*d_m+c=P_k(t_m).

Also 1*b+c=P_k(r) and 1*d_m+c=P_k(s_m) identically. The growth of S_m ensures d_m>max(1,b) after a finite number of steps; in fact the provided positive starting point and nontrivial norm-one unit make the first step valid in the tested examples. Taking all sufficiently large steps gives infinitely many distinct positive actual Type B triples (1,b,d_m). QED for any nonsquare b.

The executable constructor verifies all three exact integer equations before returning an output; step zero is rejected because it is the repeated-entry formal seed.

## Proof II: infinitely many nonsquare fixed second entries

Write

    F(r)=P_k(r)−P_k(u)+1
        = A*r²+B*r+C,
    A=(k−2)/2, B=−(k−4)/2,
    C=1−P_k(u).

We claim F(r)>1 is nonsquare for infinitely many positive integers r unless (k,u)=(4,1).

Suppose instead that F(r) is a square for all sufficiently large integers r. Let y_r=√F(r) be its nonnegative **integer** square root for these large r. The asymptotic expansion gives

    y_(r+1)−y_r → √A.

The left side is an integer sequence with a real limit. It must therefore eventually equal a single integer m=√A>0. Thus y_r=m*r+v for all sufficiently large r, where m and v are integers. Since two quadratic polynomials agreeing at infinitely many integers are identical,

    A=m², B=2*m*v, C=v².

The first identity gives k−2=2m², so k=2m²+2. The second becomes

    1−m²=2*m*v.

In particular m divides 1−m², hence m divides 1. Thus m=1 and k=4. Then B=0 forces v=0, and C=0 implies P_4(u)=1, hence u=1. This is the only possible exception. Therefore outside (4,1), F(r) is nonsquare at infinitely many r, proving the stronger fixed-pair assertion.

## Proof III: exceptional square-order case

For (k,u)=(4,1), c=P_4(1)−1=0. Choose distinct integers r,s≥2. The triple

    (a,b,d)=(1,r²,s²)

is positive with distinct entries and has exact square pair outputs

    r²=P_4(r), s²=P_4(s), (rs)²=P_4(rs).

Letting s increase gives infinitely many triples. QED.

## Exact sample constructions

| order k | index u | offset c | exact entries (a,b,d) | exact pair indices (r,s,t) |
| --- | ---: | ---: | --- | --- |
| 3 | 1 | 0 | (1,3,210) | (2,20,35) |
| 4 | 1 | 0 | (1,4,9) | (2,3,6) |
| 7 | 2 | 6 | (1,12,28051219) | (3,3350,11604) |

For the 7-gonal example, P_7(t)=(5t²−3t)/2. Exact verification:

    1*12+6=P_7(3)=18,
    1*28051219+6=P_7(3350)=28051225,
    12*28051219+6=P_7(11604)=336614634.

The congruence normal form and Pell growth are used to *find* the solutions; the three displayed equalities are in the ordinary integers.

## Implementation and test evidence

- Producer: [research/figurate_wp09_seed_existence.py](../research/figurate_wp09_seed_existence.py), with a separate square-exception constructor and explicit refusal to mislabel the repeated-entry point as a Type B triple.
- Independent regressions: [tests/test_figurate_wp09_seed_existence.py](../tests/test_figurate_wp09_seed_existence.py). Uses an independently typed quadratic formula to recompute exact pair outputs; checks 26 consecutive orders and six offsets each, multiple growing Pell steps, 12 distinct nonsquare b choices across selected orders, input errors, and exceptional c=0 squares.

Run from repository root:

    python3 -m unittest -v tests.test_figurate_wp09_seed_existence
    python3 -m research.figurate_wp09_seed_existence --order 7 --index 2

**Remaining mathematical boundary.** The result covers the explicit infinite family of offsets c=P_k(u)−1 for every order k. It neither proves that all everywhere-locally-compatible offsets have exact positive integer Type B triples nor exhibits a locally compatible but globally impossible offset. The next serious question is whether a similarly general seed construction exists for offsets not one less than a polygonal number, or whether generalized Pell equations with index congruence conditions furnish a rigorously certified local-to-global counterexample. The universal eventual-square lemma and Pell-unit lifting are elementary/classical tools; literature priority remains unverified.
