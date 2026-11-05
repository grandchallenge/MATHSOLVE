# FIGURATE WP08 — exact global Type B triple obstructions modulo 32

**Work package:** [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125), parent [FIGURATE #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093). **Tranche 004, 4 November 2026.**

**Claim level:** internally testable elementary modular theorem and finite proof certificate. No originality or independent specialist certification claim. This is not a global existence/nonexistence classification outside the explicitly excluded classes.

## Main proposition

Let $k\ge3$, $c\in\mathbb Z$, and $P_k(t)=t+(k-2)\binom t2$ for integer $t\ge1$. A **Type B triple** is a set of three distinct positive integers $a,b,d$ such that each of $ab+c$, $ad+c$, and $bd+c$ is a $k$-gonal number.

**Theorem (modulo-32 exclusion).** No such triple exists if **any** of these conditions holds:

1. $k\equiv0\pmod8$ and $c\equiv2,3,$ or $6\pmod8$ (previously admitted).
2. $k\equiv12\pmod{16}$ and $c\equiv2\pmod4$ (previously admitted).
3. **New at modulus 32:** $k\equiv0\pmod{16}$ and $c\equiv5\pmod{16}$.
4. **New at modulus 32:** $k\equiv8\pmod{16}$ and $c\equiv9\pmod{16}$.

All conclusions are **global**: there is no numerical bound and no assumed entry such as 1. The qualifier *new at modulus 32* means stronger than the programme's modulo-16 test, **not** new to the mathematical literature.

### Complete necessary-condition table

This table records **all** order/offset cells excluded by the complete modulo-32 Type B triple **local** test; the sixteen distinct order/offset classes are lifted from the following table rows.

| Polygonal order $k\bmod32$ | Offset residues $c\bmod32$ excluded |
| --- | --- |
| 0 or 16 | 2, 3, **5**, 6, 10, 11, 14, 18, 19, **21**, 22, 26, 27, 30 |
| 8 or 24 | 2, 3, 6, **9**, 10, 11, 14, 18, 19, 22, **25**, 26, 27, 30 |
| 12 or 28 | 2, 6, 10, 14, 18, 22, 26, 30 |
| Every other $k\bmod32$ | None |

Bold residues are absent from the earlier modulo-16 exclusions. For cells **not** excluded here, a local residue solution exists, but this does **not** imply any triple of distinct positive integers exists.

### Direct 2-adic proof of the two new families

The two newly excluded families can be proved without relying on a large enumerator. For either
$k\equiv0\pmod{16}$, $c\equiv5\pmod{16}$ or
$k\equiv8\pmod{16}$, $c\equiv9\pmod{16}$,
the allowed pair products $xy=P_k(t)-c$ have, **modulo 16**, exactly the following shape:

- every **odd** allowed product is $3\pmod4$;
- every **even** allowed product is $8$ or $12\pmod{16}$, and therefore has 2-adic valuation exactly 3 or 2 respectively.

A further inspection modulo 32 gives an essential strengthening: **among allowed even pair-product residues, there is exactly one class of valuation 3 modulo 32**. This follows directly from the complete $P_k(t)$ images:

| $k\bmod32$ | $P_k(t)\bmod32$ | $c\bmod32$ | Unique allowed product with valuation 3, modulo 32 |
| --- | --- | --- | --- |
| 0 | 0,1,8,16,17,24,29 | 5 / 21 | 24 / 8 |
| 16 | 0,1,8,13,16,17,24 | 5 / 21 | 8 / 24 |
| 8 or 24 | 0,1,5,8,16,21,24 | 9 / 25 | 24 / 8 |

In particular, **two allowed products of valuation 3 cannot differ by 16 modulo 32**. (Valuation 3 here means divisible by 8 but not 16.)

Suppose three positive integers $a,b,d$ satisfy all three pair conditions. Consider their parity:

**All three odd.** Each of $ab$, $ad$, $bd$ is $3\pmod4$. Multiplication gives
$(abd)^2\equiv3^3\equiv3\pmod4$, impossible for a square.

**Exactly one even**, say $a$. Then the odd pair $bd\equiv3\pmod4$ makes $b,d$ opposite odd classes modulo 4. Their products with $a$ must both have valuation 2 or 3.
If $v_2(a)=2$, write $a=4x$ with $x$ odd. Because $b-d\equiv2\pmod4$, the products $ab,ad$ differ by $8\pmod{16}$, impossible among allowed $8,12\pmod{16}$.
If $v_2(a)=3$, their difference is $16\pmod{32}$, impossible because there is only one allowed valuation-3 residue modulo 32.
Other valuations of $a$ are ruled out by the allowed product valuations.

**Exactly two even**, with the remaining entry odd. Both even entries must individually have valuation 2 or 3 from their products with the odd entry. Their mutual product then has valuation at least 4, whereas every allowed even pair product has valuation 2 or 3. Contradiction.

**All three even.** The three pair-product valuations must each be 2 or 3. Hence their individual valuations are either $(1,1,1)$ or a permutation of $(2,1,1)$; all other patterns force a pair-product valuation at least 4.
For $(1,1,1)$, write $a=2x,b=2y,d=2z$ with $x,y,z$ odd. All products have valuation 2 and thus equal $12\pmod{16}$, so $xy,xz,yz\equiv3\pmod4$, and multiplying gives $(xyz)^2\equiv3\pmod4$, impossible.
For $(2,1,1)$, write $a=4x,b=2y,d=2z$ with $x,y,z$ odd. Then $bd\equiv12\pmod{16}$ forces $yz\equiv3\pmod4$, so $y-z\equiv2\pmod4$. The products $ab=8xy$ and $ad=8xz$, both of valuation 3, differ by $16\pmod{32}$, contradicting the unique allowed valuation-3 residue.

Every parity pattern fails. This establishes both new infinite families directly, independently of the program's exhaustive enumeration. The finite code remains valuable as an **independent completeness certificate** for the entire modulo-32 table and for the absence of other local exclusions.

### Finite exact proof certificate

For a positive integer modulus $m$, define the complete image

$$
R_{k,m}=\{P_k(t)\bmod m:1\le t\le2m\}.
$$

This image is complete because $P_k(t+2m)\equiv P_k(t)\pmod m$. Moreover, the identity

$$
P_k(t)=t+(k-2)\binom t2
$$

shows that $R_{k,m}$ depends only on $k\pmod m$.

For each order residue $k\bmod32$ and offset residue $c\bmod32$, test **all**

$$
\binom{32+3-1}{3}=\binom{34}{3}=5984
$$

nondecreasing triples of entry remainders $0\le a\le b\le d<32$. A residue triple survives exactly when

$$
(ab+c)\bmod32,\quad (ad+c)\bmod32,\quad (bd+c)\bmod32\in R_{k,32}.
$$

**Distinct integer entries may have the same remainder.** Consequently repeated residue classes are included. If no residue triple survives, every hypothetical integer triple would project into a nonexistent residue witness and is impossible.

The complete enumeration over the $32\times32=1024$ order/offset residue cells produces exactly the exclusion table above. The producer [`figurate_wp08_mod32.py`](../research/figurate_wp08_mod32.py) returns not only the excluded cells but the **lexicographically first local residue witness in every nonexcluded cell**. A canonical JSON commitment to the entire witness table is SHA-256:

```text
4d67102c4c16572b93679b2d3875269351e4c67687bb418c48a88aa5447fa3f5
```

This is a finite integer-arithmetic proof certificate. The exact theorem also admits a future paper proof by decomposing residue parities; such a shorter analytic reduction for the *two new* classes has **not** yet been formally admitted. Do not characterize a machine-enumerated finite verification as a new conceptual classification theorem without that distinction.

## Independent validation and nonvacuity

The [independent test suite](../tests/test_figurate_wp08_mod32.py) calculates the polygonal images using the explicit quadratic polynomial and constructs a separate Boolean pair-compatibility matrix. It independently reconstructs every one of the 1024 cells and each lexicographically first local witness; additionally checks periodicity in order and offset, the inclusion of all prior modulus-16 obstructions, direct bounded counterexample searches in the two *new* classes, and compatible **actual** pairs.

Actual compatible pairs exist infinitely often for every order and offset: take $\{1,P_k(t)-c\}$ with sufficiently large index $t$. Thus the modular impossibility is genuinely about **triples**, not about failure to produce pairs.

Examples of parameters newly excluded by modulus 32 are $(k,c)=(16,5)$ and $(8,9)$. The lower modulus-16 check admits local residue triples in both cases, whereas modulus 32 rules out every possible third-entry residue arrangement for all integer entries.

### Runbook

```sh
python3 -m research.figurate_wp08_mod32
python3 -m research.figurate_wp08_mod32 --k 16 --offset 5
python3 -m research.figurate_wp08_mod32 --k 8 --offset 9
python3 -m unittest discover -s tests -p test_figurate_wp08_mod32.py -v
```

The programme also has the protected [modulo-8](FIGURATE_WP08_GLOBAL_TRIPLE_OBSTRUCTION_002.md) and [modulo-16](FIGURATE_WP08_MOD16_GLOBAL_OBSTRUCTIONS_003.md) results. Each is a separate reproducing step; the stronger present theorem subsumes their previously excluded order/offset classes.

## Literature and admission boundary

A targeted prior-art search located R. Radha, G. Janaki and M. Madhumika, *Diophantine Triples Involving Octagonal Numbers* and *Non-Extendability of Special Diophantine Triples Involving Octagonal Numbers* (2023), listed at [*Explorations in Diophantine Equations*, pp. 50–67](https://stm.bookpi.org/EDE/issue/view/1251). Their complete texts and exact tuple semantics require source-level review before claiming priority. Octagonal **pyramidal** numbers and **square-output** tuple constraints are not interchangeable with the ordinary polygonal Type B output condition.

**GCL status:** finite residue exhaustion and independent software tests constitute verifiable internal arithmetic evidence. Protected repository checks establish code and documentary admission, **not** outside mathematical novelty, an independent specialist proof review, or public certification. The WP08 research issue remains open for stronger 2-adic structural proof, comparison to prior art, and adjudicated mathematical certification work.
