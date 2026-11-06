# FIGURATE WP09-019 — exact 100-gonal Type B seed from a constrained Pell orbit

**Result:** an exact global positive-integer Type B solution for $(k,c)=(100,2)$ and an infinite family from the protected WP09-013 fixed-first-pair Pell theorem. This is internal producer mathematics; independent MATHCERT certification and external literature-priority review remain separate.

## 1. Exact seed

The entries are

$$
(a,b,d)=(1,98,394141484570467638798107106734400805257750080265189167281283878325018383881627360745786897584655),
$$

and the indices are

$$
(r,s,t)=(2,89686697824951931533091760698417159299075689513,887853010999532105318395994347406981537890234904).
$$

Direct substitution gives

$$
P_{100}(r)=100=98+2,
$$

$$
P_{100}(s)=394141484570467638798107106734400805257750080265189167281283878325018383881627360745786897584657=d+2,
$$

$$
P_{100}(t)=38625865487905828602214496459971278915259507865988538393565820075851801620399481353087115963296192=98d+2.
$$

The 96-digit third entry is beyond the complete WP09-016 census bound of 300,000. That earlier finite exclusion remains correct and does not imply global nonexistence.

## 2. Constrained Pell construction

The small first pair is $a=1,b=98$ at $r=2$, since

$$
ab+2=98+2=100=P_{100}(2).
$$

Put $R=2(k-2)=196$, $L=k-4=96$, and

$$
\Delta=8(k-2)c+L^2=8\cdot98\cdot2+96^2=10784.
$$

The fixed-first-pair norm equation is

$$
X^2-98S^2=(1)(1-98)\cdot10784=-1046048,
$$

where $S=196s-96$ and $X=196t-96$. An exact starting point is

$$
4019472^2-98\cdot406028^2=-1046048.
$$

The integer unit $99+10\sqrt{98}$ has norm

$$
99^2-98\cdot10^2=1.
$$

After 19 applications to the starting point,

$$
(X,S)=(174019190155908292642405614892091768381426486041088,\;
17578592773690578580485985096889763222618835144452).
$$

Both coordinates have the required residue:

$$
X\equiv100\pmod{196},\qquad S\equiv100\pmod{196}.
$$

Thus $s=(S+96)/196$ and $t=(X+96)/196$ are positive integers. Setting $d=P_{100}(s)-2$ gives the exact 96-digit entry above, and direct substitution verifies $P_{100}(t)=98d+2$.

## 3. Infinite family

The protected WP09-013 Theorem A applies to every exact positive Type B seed whose first-pair product $ab$ is nonsquare. Here $ab=98$ is nonsquare, so infinitely many exact positive triples follow with the same first pair $a=1,b=98$ and the same order and offset.

The amplification lattice modulus is

$$
M=2aR=392.
$$

The least positive exponent for which

$$
(99+10\sqrt{98})^e\equiv1\pmod{392}
$$

in the quadratic integer coordinates is $e=196$, verified by exact modular recurrence over all smaller positive exponents and the exponent 196. Applying this power preserves the seed's index and divisibility classes. The next exact family member has a 996-digit third entry and is strictly larger than the seed. WP09-013 supplies the infinite-family proof.

## 4. Combined WP09-016/WP09-018/WP09-019 disposition

Both globally unresolved parameter pairs from the preceding frontier are now solved:

- $(84,2)$: WP09-018, exact seed with 39-digit third entry and an infinite family.
- $(100,2)$: WP09-019, exact seed with 96-digit third entry and an infinite family.

WP09-016 correctly excluded all seeds with all three entries at most 300,000 for each pair. The exact constructions above show why that bound could not settle the global question. Both pairs are everywhere locally compatible under WP09-012, and both now have actual global integer solutions. Neither is a local-to-global counterexample.

## 5. Reproduction and audit

- Exact constructor: [research/figurate_wp09_exact_seed_019.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_exact_seed_019.py)
- Independent direct-polynomial tests: [tests/test_figurate_wp09_exact_seed_019.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_exact_seed_019.py)
- Amplification theorem: [WP09-013 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_GENERAL_FIRST_PAIR_PELL_013.md)
- Earlier bounded exclusions: [WP09-016 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_FRONTIER_CENSUS_016.md)

Run:

    python3 -m unittest -v tests.test_figurate_wp09_exact_seed_019
    python3 -m research.figurate_wp09_exact_seed_019
    python3 -m research.figurate_wp09_exact_seed_019 --next-family-member

The independent tests use the standard polygonal formula, separately replay the Pell orbit, check every exact pair equation and lattice residue, verify the modular unit order 196, and validate the next exact family member. No independent MATHCERT certification or external originality claim is asserted.
