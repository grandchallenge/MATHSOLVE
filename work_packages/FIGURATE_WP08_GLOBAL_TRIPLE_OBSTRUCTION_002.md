# FIGURATE WP08 — global Type B triple obstruction modulo eight (tranche 002)

**Campaign:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093); [WP08](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125). **Research status:** exact elementary proof and exhaustive finite local classification; mathematical originality and specialist certification **not established**.

## Theorem: no Type B triples for an infinite family of orders and offsets

Let $k\geq3$ be a polygonal order and $c$ any integer. A Type B triple consists of three **distinct positive integers** $a,b,d$ such that

$$
ab+c=P_k(r),\quad ad+c=P_k(s),\quad bd+c=P_k(t)
$$

for some positive integer indices $r,s,t$.

**Theorem (modular obstruction).** If $k\equiv0\pmod8$ and $c\equiv2$ or $6\pmod8$, there is **no Type B triple whatsoever**. The assertion is unbounded in the values of $a,b,d$; it does **not** require an entry equal to 1.

### Direct parity proof

Since

$$
P_k(t)=t+(k-2)\binom{t}{2},
$$

for $k\equiv0\pmod8$ the complete polygonal residue image modulo 8 is

$$
R_{k,8}=\{0,1,5\}.
$$

As $c\equiv2\pmod4$, any valid pair product is therefore $2$ or $3$ modulo 4. Three cases exhaust the possibilities:

1. If two entries are even, their product is $0\pmod4$, a contradiction.
2. If all three entries are odd, every pair product must be $3\pmod4$. Multiplying the three pair-product relations gives $(abd)^2\equiv3^3\equiv3\pmod4$, impossible for a square.
3. Thus exactly one entry, say $a$, is even. Each product $ab$ and $ad$ must be $2\pmod4$, while the other two entries $b,d$ are odd and their product is $3\pmod4$. Consequently $a\equiv2\pmod4$ and $b,d$ occupy opposite odd residue classes modulo 4. Hence $ab$ and $ad$ differ by $4\pmod8$.

   On the other hand, the **only even residue** in $R_{k,8}$ is 0. Both $ab+c$ and $ad+c$ are even polygonal numbers and therefore must be $0\pmod8$, which forces $ab\equiv ad\equiv-c\pmod8$. This contradicts their difference by 4 modulo 8.

All cases are impossible. This completes an elementary proof valid for **all** $k$ and $c$ in the stated congruence classes, without a bounded computer search.

### Completeness of the local classification at modulus 8

The above theorem is precisely the **only** triple-nonexistence case detectable by the complete modulus-8 necessary condition across all order and offset residue classes:

| Polygonal order $k\bmod8$ | Offset residues $c\bmod8$ for which **no local triple** exists |
| --- | --- |
| 0 | 2, 6 |
| 1, 2, 3, 4, 5, 6, 7 | none |

To establish *local* completeness, enumerate all unordered residue **multisets** $0\leq a\leq b\leq d<8$, including repeated classes. For each of the eight order classes $k\bmod8$, calculate the complete image $R_{k,8}$ from indices $1$ through $16$; for each offset class $c\bmod8$, test the three residues $ab+c$, $ad+c$, $bd+c$. The exact, independently reproduced enumeration returns the table above. This is a finite exhaustive certificate (120 residue multisets per order/offset cell), not a claim that all other parameter classes possess actual integer triples.

**Why order lifting works.** Since $P_k(t)=t+(k-2)\binom t2$, the polynomial image modulo $m$ depends only on $k\bmod m$; $P_k(t+2m)\equiv P_k(t)\pmod m$. Therefore the 8 order representatives used in the table cover infinitely many actual polygonal orders. Repeated residue classes are permitted: distinct positive entries may coincide modulo 8.

### Nonvacuity and scope

Compatible Type B **pairs** still exist for *every* polygonal order and integer offset. Indeed, for every sufficiently large $t$, take $a=1$ and $b=P_k(t)-c>1$; then $ab+c=P_k(t)$. Hence the triple obstruction is strictly stronger than, and is not obtained by simply ruling out, all pairs.

The theorem also implies the anchored nonextension result already admitted in [WP08 tranche 001](FIGURATE_WP08_MOD8_CLASSIFICATION_001.md), but not conversely: earlier work proved no triple **containing 1** at the same congruence parameters. The present proof removes that restriction.

## Executable, adversarial and reproducibility evidence

- [Modulus-8 triple classifier](../research/figurate_wp08_global_mod8.py): enumerate all residue triples (with replacement) for any order, offset and modulus; report exact excluded classes.
- [Independent verification suite](../tests/test_figurate_wp08_global_mod8.py): use an independently expressed polynomial, independent residue loops, all $3\leq k\leq130$ and $-18\leq c\leq18$ at modulus 8, additional moduli 3, 4, 5, 7, 8, 9, 12 and 16, exact compatible positive pair constructions, and direct finite triple counterexample searches.
- Prior [WP07 obstruction dossier](FIGURATE_WP07_OBSTRUCTIONS_001.md) documents earlier restricted octagonal pair examples.
- Source provenance and external novelty limitations are recorded in the [GCL source register](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/campaigns/FIGURATE_SOURCES.md).

```sh
python3 -m research.figurate_wp08_global_mod8
python3 -m research.figurate_wp08_global_mod8 --k 8 --offset 2 --modulus 8
python3 -m unittest discover -s tests -p 'test_figurate_wp08_global_mod8.py' -v
```

**Novelty boundary.** The statement is a substantive strengthening **within GCL** of the previous anchored-pair theorem, but it is an elementary congruence obstruction. No exhaustive external literature search or independent specialist mathematical review has established originality. Do not advertise it as a new theorem in the mathematical literature, and do not conflate repository CI with mathematical certification. The open WP08 goal remains a genuinely new, externally defensible classification or rigorous algorithm, subject to prior-art and specialist gates.
