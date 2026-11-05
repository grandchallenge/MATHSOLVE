# FIGURATE WP09-005 — a uniform odd-prime-square obstruction

**Status:** internally proved research candidate; neither source-priority established nor independently MATHCERT-certified. Parent [WP09](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). This is a distinct prime-uniform structural theorem, not an attempted reroute of the explicitly held WP09-004 repository operation.

## Uniform theorem

Let k be an integer at least 3; define P_k(t)=t+(k-2)t(t-1)/2. A Type B triple comprises three distinct positive integers a,b,d, an integer offset c and positive integer indices r,s,t such that ab+c=P_k(r), ad+c=P_k(s), bd+c=P_k(t).

Let p be **any odd prime** not dividing k-2, and let A=(k-2)/2 in the field F_p. Suppose A is a **quadratic nonresidue** modulo p. If

- 8(k-2)c+(k-4)^2 is divisible by p, but
- 8(k-2)c+(k-4)^2 is **not** divisible by p^2,

then **no Type B triple exists**, at any entry size. Indeed, no three residues, even allowing repeated entry classes, satisfy the three polygonal pair-output conditions modulo p^2. Negative offsets are included.

This is a sufficient obstruction. It does **not** assert a complete classification of all p^2-compatible cases for arbitrary p, and local compatibility is not the existence of an exact-integer triple.

## Algebraic proof without finite enumeration

Work in R=Z/p^2 Z. Since p is odd and p does not divide k-2, the elements 2 and k-2 are units. Complete the polygonal square:

- A=(k-2)/2;
- h=(k-4)/(2(k-2));
- B=-(k-4)^2/(8(k-2));
- P_k(t)=A(t-h)^2+B, as an identity in R.

Write v=c-B. The offset assumption is precisely v=p*u in R, with u a unit modulo p. Each hypothetical pair product xy must therefore satisfy

    xy+v = A*z^2 (mod p^2)

for a suitable shifted polygonal index z.

A square modulo p^2 which is divisible by p is zero modulo p^2. Hence no A*z^2 can have exact p-adic valuation one.

There are three exhaustive divisibility patterns for a,b,d.

1. **No entry divisible by p.** Reducing the three equations modulo p shows that ab, ad and bd are all nonzero quadratic nonresidues: each equals the nonresidue A multiplied by a nonzero square. Their product is (abd)^2, a quadratic residue, whereas the product of three nonresidues is a nonresidue. Contradiction.
2. **At least two entries divisible by p.** Their pair product is zero modulo p^2; adding v=p*u gives valuation exactly one and cannot equal A*z^2. Contradiction.
3. **Exactly one entry divisible by p**, say a, with b,d units. Both ab+v and ad+v are divisible by p, so their squares-on-the-right must vanish modulo p^2. If a were zero modulo p^2 this would force v=0, impossible. Thus a=p*alpha with alpha a unit modulo p. Divide the two zero congruences by p: alpha*b+u=0 and alpha*d+u=0 (mod p). Hence b=d (mod p). But bd=b^2 (mod p) is a nonzero square while bd=A*z^2 (mod p) requires a nonresidue. Contradiction.

All patterns contradict the pair equations. Therefore no Type B triple exists. QED.

The decisive phenomenon is valuation one at p: the obstruction is invisible in the reduction to p but becomes decisive at p^2. The argument uses no bound on any entry.

## Infinitely many excluded parameter classes; exact density

For a fixed odd prime p, exactly p(p-1)^2/2 of the p^4 periodic order/offset classes (k,c) modulo p^2 satisfy the theorem. Their fraction is (p-1)^2/(2p^3).

Proof: the nonzero coefficient A ranges over F_p as k varies, and (p-1)/2 values are nonsquares. Each such k mod p has p lifts modulo p^2. For each k, there is a unique B mod p^2; exactly p-1 offsets equal B mod p but differ from B mod p^2.

| Prime p | Classes excluded by theorem | Previous result |
| --- | ---: | --- |
| 3 | 6 of 81 | WP09 modulo-nine global obstruction |
| 5 | 40 of 625 | WP09 modulo-25 classification |
| 7 | 126 of 2401 | WP09-004 modulo-49 candidate |
| 11 | 550 of 14641 | New prime covered by uniform theorem |
| 13 | 936 of 28561 | New prime covered by uniform theorem |

For p=3,5,7, complete independent finite scans confirm the theorem also accounts for **all** locally excluded cells modulo p^2; this finite coincidence is not generalized into an unproved universal completeness claim.

The earlier coprime CRT theorem remains valid: separate prime-power compatible triples can be glued locally, so independent moduli do not introduce mysterious new CRT exclusions. Congruence compatibility still does not imply exact positive-index integer solutions. The existing exact triangular-output Pell family (1,3,15), (1,3,210), (1,3,2926), etc. is a positive-integer control, not a novelty claim.

## Replay, independent adversarial checks, and source boundaries

Producer: research/figurate_wp09_uniform_prime_square.py

Independent arithmetic: tests/test_figurate_wp09_uniform_prime_square.py

Run from repository root:

    python3 -m unittest -v tests.test_figurate_wp09_uniform_prime_square
    python3 -m research.figurate_wp09_uniform_prime_square --prime 7 --audit

The independent test directly evaluates the quadratic polygonal polynomial and scans residue triples, including repeated classes. It exercises the full p=3,5,7 classifications, additional p=11,13 cases, negative offsets, periodicity, exact positive triangular controls, and invalid moduli. The abstract proof does not depend on the computation.

**Novelty boundary:** Legendre symbols, quadratic completion, congruence valuation and CRT are classical. This parameter-uniform Type B implication is new to the GCL proof ledger but has NOT been established as previously unknown in the literature. The WP05 2025 primary-source full-text gap and independent source-semantic scrutiny remain open. Protected producer admission and downstream public explanation do not confer independent mathematical certification. No claim about Type A/C is made.
