# FIGURATE WP09-022 — three more exact Pell seeds in the local-positive frontier

**Result:** exact global positive-integer Type B seeds for $(k,c)=(308,2),(340,2),(356,2)$ and an infinite family for each via protected WP09-013 Theorem A. This is internal producer mathematics; independent MATHCERT certification and external literature-priority review remain separate.

All three use $a=1$, $b=k-2$, $r=2$. Thus $ab+2=k=P_k(2)$ and $ab=k-2\equiv2\pmod{16}$ is nonsquare. For each order,

$$
X^2-(k-2)S^2=-(k-3)\Delta,\qquad
\Delta=8(k-2)\cdot2+(k-4)^2.
$$

The index lattice is $X\equiv S\equiv-(k-4)\pmod{2(k-2)}$.

## Exact seed data

| $k$ | Base point $(X_0,S_0)$ | Unit $U+V\sqrt{k-2}$ | Steps | Third entry $d$ | Indices $(r,s,t)$ |
|---:|---:|---:|---:|---:|---|
| 308 | (7521856,429996) | $35+2\sqrt{306}$ | 1 | 369944066839 | $(2,49173,860168)$ |
| 340 | (18592,1068) | $114243+6214\sqrt{338}$ | 8 | 22055110173676298711853052417255546283873851842341288791785952330313175104651322552060223 | $(2,11423817684781477108531933830301694263727175,210024332750642484748486106183948953202007676)$ |
| 356 | (30800,1676) | $258065+13716\sqrt{354}$ | 32 | 400749170861244294657713664277790654885026802109356000545437704103819727217408006938307289707716852386075417895044484644972147329057081727230022277377747386716231343146949861171138906096651353752252092374331177905029455032677534403983871399033119357528777809592397662723973078140250811576316509887623046621428256348426978817656495932258870392977774352222156809812844119 | $(2,1504699175711065838545810739621546414075173402601182922297946649529406030599934525304843746212948910534739063336262843490746949935379315752643229820190642759031366538474817891572918891,28310746046730887754276264183444936494431225824953708096748139660266943479349467842325013732113325958668456801885031571068528490872704349886026004149581313743303522144747989411694575404)$ |

For every row, direct substitution using the standard polygonal polynomial checks $P_k(2)=k$, $P_k(s)=d+2$, and $P_k(t)=(k-2)d+2$. The third entries have 12, 89 and 369 digits.

## Infinite amplification

The least identity exponents of the displayed units modulo the amplification lattice modulus $M=2aR=4(k-2)$ are:

| $k$ | Modulus | Unit order | Next family third-entry digits |
|---:|---:|---:|---:|
| 308 | 1224 | 612 | 2270 |
| 340 | 1352 | 52 | 646 |
| 356 | 1416 | 118 | 1717 |

Exact modular recurrence checks every smaller positive exponent. Applying the identity power preserves the index and divisibility lattice, and direct integer evaluation verifies the next member. Since the first-pair products 306, 338 and 354 are nonsquare, WP09-013 proves infinitely many distinct exact positive triples for each parameter pair.

## Local/global scope

The protected WP09-012 all-place classifier returns local compatibility for all three pairs: discriminants 97312, 118304 and 129568. These exact seeds establish global existence for these three cases. They do not prove that every locally compatible pair has an integer seed.

## Reproduction

- Constructor: [research/figurate_wp09_local_positive_seed_batch_022.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_local_positive_seed_batch_022.py)
- Independent tests: [tests/test_figurate_wp09_local_positive_seed_batch_022.py](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_local_positive_seed_batch_022.py)
- Amplification theorem: [WP09-013 dossier](https://github.com/grandchallenge/MATHSOLVE/blob/main/work_packages/FIGURATE_WP09_GENERAL_FIRST_PAIR_PELL_013.md)

Run:

    python3 -m unittest -v tests.test_figurate_wp09_local_positive_seed_batch_022
    python3 -m research.figurate_wp09_local_positive_seed_batch_022 --order 308
    python3 -m research.figurate_wp09_local_positive_seed_batch_022 --order 340
    python3 -m research.figurate_wp09_local_positive_seed_batch_022 --order 356

No independent MATHCERT certification or external originality claim is made.
