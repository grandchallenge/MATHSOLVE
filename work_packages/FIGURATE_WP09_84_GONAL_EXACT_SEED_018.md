# FIGURATE WP09-018 — exact 84-gonal Type B seed from a constrained Pell orbit

**Result:** an exact global positive-integer Type B solution for $(k,c)=(84,2)$, followed by an explicit application of the protected WP09-013 infinite-amplification theorem. This is internal producer mathematics; independent MATHCERT certification and external literature-priority review remain separate.

## 1. Exact seed

For $P_k(n)=((k-2)n^2-(k-4)n)/2$, the following entries and indices satisfy all three Type B equations:

$$
(a,b,d)=
(2,41,172124700980346120000589924527450935999),
$$

$$
(r,s,t)=
(2,2897641606046209200,13119630367519738931).
$$

The exact pair outputs are

$$
P_{84}(r)=84=2\cdot41+2,
$$

$$
P_{84}(s)=344249401960692240001179849054901872000=2d+2,
$$

$$
P_{84}(t)=7057112740194190920024186905625488375961=41d+2.
$$

All entries and indices are positive integers; the three entries are pairwise distinct. These equalities are checked using arbitrary-precision integer arithmetic and the original polygonal polynomial, not floating point or approximate square roots.

The third entry has 39 decimal digits, so this exact seed is fully consistent with the WP09-016 exhaustive exclusion of triples whose entries are all at most 300,000. The earlier finite census did not approach the first solution.

## 2. Derivation from a fixed-first-pair norm equation

The first pair is deliberately small:

$$
ab+2=2\cdot41+2=84=P_{84}(2).
$$

Put $R=2(k-2)=164$, $L=k-4=80$, and

$$
\Delta=8(k-2)c+L^2=8\cdot82\cdot2+80^2=7712.
$$

For a fixed first pair $(a,b)$, any extension to a Type B seed gives the generalized Pell equation

$$
X^2-abS^2=a(a-b)\Delta,
$$

with $S=Rs-L$ and $X=a(Rt-L)$. Here $ab=82$ and the right-hand side is

$$
2(2-41)\cdot7712=-601536.
$$

An exact starting point is

$$
3585208^2-82\cdot395920^2=-601536.
$$

The integer unit $163+18\sqrt{82}$ has norm

$$
163^2-82\cdot18^2=1.
$$

Multiplication by this unit preserves the norm equation. Applying it six times to the starting point gives

$$
(X,S)=(4303238760546474369208,\;
475213223391578308720).
$$

The lattice conditions are exact:

$$
S\equiv84\pmod{164},\qquad
X\equiv168\pmod{328}.
$$

Therefore

$$
s=(S+80)/164=2897641606046209200,
$$

$$
t=(X/2+80)/164=13119630367519738931
$$

are positive integers. Set $d=(P_{84}(s)-2)/2$. Direct integer evaluation gives the 39-digit value in Section 1 and verifies $P_{84}(t)=41d+2$. This constructs the exact seed.

## 3. Infinite family

The protected WP09-013 Theorem A states that any exact positive Type B seed with nonsquare first-pair product $ab$ generates infinitely many distinct exact positive Type B triples with the same $a,b,k,c$.

Here $ab=82$ is nonsquare, so the theorem applies. For a direct congruence-preserving readback, its lattice modulus is

$$
M=2aR=2\cdot2\cdot164=656.
$$

The least positive exponent for which

$$
(163+18\sqrt{82})^e\equiv1\pmod{656}
$$

in the quadratic integer coordinates is $e=328$. This is established by exact modular recurrence: no exponent $1,\ldots,327$ is the identity and exponent 328 is. Applying the 328th unit power to the seed coordinates preserves their residue classes modulo 656, hence preserves the integral polygonal indices and the divisibility needed to recover the third entry. The next exact family member has a 1,687-digit third entry, strictly larger than the seed. The WP09-013 theorem supplies infinitely many distinct members, not merely this second example.

## 4. Why this matters

The pair $(84,2)$ passed the complete WP09-012 all-place local compatibility sieve. WP09-016 then excluded all exact triples with entries at most 300,000 for this pair. WP09-018 now proves global integer existence by finding a seed with a 39-digit third entry. This is a concrete demonstration that a large exact bounded exclusion can coexist with a genuine global solution far beyond the search region.

It is not a local-to-global counterexample: local compatibility and global existence both hold here. The remaining cases, including $(100,2)$, must be studied separately. No global nonexistence claim is made for $(100,2)$.

## 5. Reproduction and audit

- Exact constructor: [research/figurate_wp09_exact_seed_018.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_exact_seed_018.py)
- Independent direct-polynomial tests: [tests/test_figurate_wp09_exact_seed_018.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_exact_seed_018.py)
- Prior amplification theorem: [WP09-013 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_GENERAL_FIRST_PAIR_PELL_013.md)
- Prior bounded exclusion: [WP09-016 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_FRONTIER_CENSUS_016.md)

Run:

    python3 -m unittest -v tests.test_figurate_wp09_exact_seed_018
    python3 -m research.figurate_wp09_exact_seed_018
    python3 -m research.figurate_wp09_exact_seed_018 --next-family-member

The tests independently recompute the seed with the standard polygonal formula, verify the norm and unit identities, check every index congruence and all three pair equations, prove the modular order 328 by exhaustive finite recurrence, and verify the next exact family member. No independent MATHCERT certification or external originality claim is asserted.
