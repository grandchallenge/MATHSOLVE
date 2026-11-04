# FIGURATE WP08 — parameter-uniform anchored-pair obstruction at modulus 8

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093). **Research issue:** [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125).

**Admission class:** mathematical *candidate* and reproducible exact verification. The mathematics below is elementary, but independent specialist review and exhaustive originality analysis remain **OPEN**. No public novelty or certification claim is made.

## The exact local classification

Let $P_k(t)$ be the polygonal sequence of order $k\geq3$, and let $c$ be an arbitrary integer. Consider **Type B** tuples with distinct positive entries and pair products shifted by $c$ equal to values of $P_k$.

Fix the first entry at $a=1$. Suppose the pair $\{1,b\}$ is **actually compatible**, so

$$
b+c=P_k(t)
$$

for some positive integer $t$. At a modulus $m$, define the complete polygonal residue image $R_{k,m}$ and the set of necessary third-entry residues

$$
E_{k,c,m}(b)=\{d\bmod m:(d+c)\bmod m\in R_{k,m},\ (bd+c)\bmod m\in R_{k,m}\}.
$$

An empty set $E_{k,c,m}(b)$ proves that the pair **cannot extend to a Type B triple over the positive integers**. Conversely, a nonempty set is only local consistency and does not establish extension.

**Proposition (complete modulus-8 classification for compatible pairs anchored at 1).** For every integer $k\geq3$, every offset $c$, and every actually compatible positive pair $\{1,b\}$, the local necessary set $E_{k,c,8}(b)$ is empty **if and only if** $k\equiv0\pmod8$ and one of the following two rows applies:

| Offset $c$ modulo 8 | Excluded residue classes $b$ modulo 8 |
| --- | --- |
| 2 | 3, 6, 7 |
| 6 | 2, 3, 7 |

**Global corollary for triples containing 1.** If $k\equiv0\pmod8$ and $c\equiv2$ or $6\pmod8$, **no Type B triple of distinct positive integers can contain the entry 1**, regardless of the other two entries. Indeed, every pair $\{1,b\}$ that could occur in such a triple must be an exactly compatible anchored pair, and the table shows that every such pair has an empty local extension set. This conclusion is unbounded in the entries, but is restricted to triples containing 1. It does **not** exclude Type B triples without 1.

For all other polygonal orders modulo 8 and offsets modulo 8, **no compatible anchored pair is excluded by this particular modulus-8 test**. This is not a statement that other obstructions or global nonextension are impossible.

### Proof: order lifting and exhaustive finite residue certificates

The fundamental identity, for every positive integer $t$, is

$$
P_k(t)=t+(k-2)\binom{t}{2}.
$$

It follows immediately that if $k\equiv\ell\pmod m$, then $P_k(t)\equiv P_\ell(t)\pmod m$ for **every** integer index $t$. Thus the complete local obstruction predicate depends on the order only modulo $m$, not on its magnitude. Moreover, $P_k(t+2m)\equiv P_k(t)\pmod m$, so indices $1$ through $2m$ give the **entire** residue image.

At modulus 8, evaluate the eight order classes (using representatives $k=8,\ldots,15$). For each of the eight offset classes, enumerate **only** residue classes $b$ such that $(b+c)\bmod8\in R_{k,8}$, then test all eight possible $d\bmod8$. This is a finite exhaustive proof certificate. The independent baseline test repeats the calculation with the polynomial formula, rather than using the certificate implementation's precomputed residue-image function. Both enumerations produce exactly the table above.

For the sole obstructed order class $k\equiv0\pmod8$, the residue image is $R_{k,8}=\{0,1,5\}$. The table can also be checked by hand: for $c\equiv2\pmod8$, the compatibility classes $b$ are $\{3,6,7\}$ and their extension sets are empty; for $c\equiv6\pmod8$, the compatibility classes $b$ are $\{2,3,7\}$ and their extension sets are empty. All other compatible anchored-pair classes across the eight order classes admit at least one **local** third-entry residue.

### Infinite nonvacuity

For every fixed order $k\equiv0\pmod8$ and **every** integer offset $c\equiv2$ or $6\pmod8$, the excluded classes contain infinitely many *genuine* compatible pairs, not just abstract residues. Choose an index $t_0\in\{1,2,3\}$ according to the target residue, and take $t=t_0+16n$ with $n$ sufficiently large. Then

$$
b=P_k(t)-c>1, \qquad b+c=P_k(t),
$$

and $b$ has the selected excluded residue, since $P_k(1)\equiv1$, $P_k(2)=k\equiv0$, and $P_k(3)=3k-3\equiv5$ modulo 8. Different large $n$ give distinct positive $b$ and the corresponding pair $\{1,b\}$ has exact polygonal index witness $t$. The complete local classification proves that **none** of these infinitely many compatible pairs can extend to a Type B triple.

This strengthens WP07's first octagonal example by transferring it uniformly to all polygonal orders divisible by 8, adding the entire offset-6 congruence class, and classifying **all** anchored compatible residue cases modulo 8. It does not establish a nontrivial global classification of extensions for arbitrary pairs.

### Modulus-16 lift

The same order-periodicity identity lifts WP07's other independent obstruction: for every $k\equiv8\pmod{16}$ and $c\equiv3\pmod{16}$, any compatible Type B pair with entries congruent to 1 and 5 modulo 16 has no extension. Infinitely many compatible examples arise as $\{1,P_k(t)-c\}$ with $t\equiv2\pmod{32}$ sufficiently large.

## Executable evidence

- [Order/offset classifier](../research/figurate_wp08_mod8_classification.py) computes **all** compatible anchor residue classes. Residue 0 and 1 are not misinterpreted as invalid positive tuple entries; local residues and genuine entries are distinct objects.
- [Independent unit tests](../tests/test_figurate_wp08_mod8_classification.py) check the complete modulus-8 table for $3\leq k<100$ and independently reconstruct all modulus-3,4,5,8,9,12,16 tables for two full order periods. Tests also verify infinite-family representatives with exact pair witnesses and rule out third entries by direct search.
- [WP07 source](../work_packages/FIGURATE_WP07_OBSTRUCTIONS_001.md) establishes the predecessor octagonal cases and the full local residue-period argument.

```sh
python3 -m research.figurate_wp08_mod8_classification
python3 -m unittest discover -s tests -p 'test_figurate_wp08_mod8_classification.py' -v
```

## Originality and scientific decision

This is an independently checkable **new-to-the-GCL-programme** uniform modular classification. It is **not** asserted novel to number theory; congruence arguments and local obstruction tables are classical techniques. The [GCL source catalogue](https://github.com/grandchallenge/MATH-PROGRAMME/blob/main/docs/campaigns/FIGURATE_SOURCES.md) covers important triangular special cases, and [Dujella's active bibliography](https://dujella.github.io/ref.html) provides wider Diophantine-tuple context. The dedicated polygonal-order modular classification literature and independent specialist proof review have not been exhaustively checked.

**WP08 gate:** a valid, parameter-uniform elementary classification and exact implementation now exist, but promotion to a research result beyond this elementary local theorem requires either (1) a substantively stronger global or multi-modulus classification with independent originality review, or (2) a rigorously evaluated algorithmic improvement. Routine protected merge admits documentary/computational artifacts only. The parent programme remains active; no mathematical certification is requested or claimed.
