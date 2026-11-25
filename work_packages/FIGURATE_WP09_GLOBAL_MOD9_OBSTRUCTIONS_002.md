# FIGURATE WP09 — global Type B triple obstruction at the odd prime power 9

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093) · [active WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Tranche 002, 5 November 2026.**

**Claim boundary:** global nonexistence of **every** Type B triple in stated infinite order/offset families. This is stronger than the earlier fixed-triple exclusion, but is an elementary congruence argument and is **not claimed novel to mathematical literature or independently certified**.

## Theorem

Let $k\ge3$ be a polygonal order divisible by three, and let $c\equiv4$ or $7\pmod9$. There exist **no three distinct positive integers** $a,b,d$ for which all three shifted products

$$
ab+c,\qquad ad+c,\qquad bd+c
$$

equal $P_k(t)$ at positive integer indices. No upper bound, prescribed entry or finite search assumption is involved.

**Sharp local qualification:** The complete modulus-nine necessary local condition excludes **exactly** these pairs of order/offset residue classes:

| $k\bmod9$ | Excluded $c\bmod9$ |
| --- | --- |
| $0,3,6$ | $4,7$ |
| All other classes | none |

A nonexcluded cell has merely a local residue witness; it does not guarantee an exact integer Type B triple. Modulus **three alone excludes no Type B parameter classes at all**. The new obstruction appears only when one retains the next ternary digit.

### Proof

Since $P_k(t)=t+(k-2)\binom t2$, its complete image modulo nine depends only on $k\bmod9$. For each $k\equiv0,3,6\pmod9$, direct calculation through the nine index classes gives

$$
R_{k,9}=\{0,1,3,6\}.
$$

Suppose a Type B triple exists. For $c\equiv4\pmod9$ the three pair products must lie in

$$
S_4=R_{k,9}-4=\{2,5,6,8\}\pmod9.
$$

For $c\equiv7\pmod9$ they must lie in

$$
S_7=R_{k,9}-7=\{2,3,5,8\}\pmod9.
$$

In **either** case, the only allowed pair-product remainders modulo three are 0 or 2; residue 1 is forbidden. Furthermore, modulo nine the **only** allowed product divisible by three is 6 in the first case, or 3 in the second case. In particular, residue zero modulo nine is always forbidden.

There are three cases.

1. **Two or three entries are divisible by three.** Their mutual product is divisible by nine, hence zero modulo nine, which is forbidden.
2. **No entry is divisible by three.** All pair products are units modulo three; each must therefore equal 2 modulo three. Multiplying the three products gives $(abd)^2\equiv2^3\equiv2\pmod3$, impossible because the only nonzero square modulo three is 1.
3. **Exactly one entry, say $a$, is divisible by three.** Since $ab$ and $ad$ must be the **single** permitted multiple-of-three product residue modulo nine, their difference is zero modulo nine:

   $$
   a(b-d)\equiv0\pmod9.
   $$

   The entry $a$ cannot be divisible by nine (else both products would be zero modulo nine). Hence $v_3(a)=1$ and $b\equiv d\pmod3$. Both $b,d$ are units modulo three, so $bd\equiv1\pmod3$, which is forbidden.

All cases contradict the pairwise requirements. Thus no Type B triple exists for the stated parameter classes. QED.

### Infinite pairs are still genuinely compatible

For every fixed order $k$ and integer offset $c$, sufficiently large positive indices $t$ give a distinct positive compatible Type B pair

$$
\{1,\,P_k(t)-c\},
$$

because the pair product plus offset equals $P_k(t)$ exactly. Thus the theorem does **not** merely exclude all pairs: it proves that such pairs can **never be extended to a triple**, for the specified parameter classes.

## Executable certificate and independent replay

[Exact modulus-nine classifier](../research/figurate_wp09_mod9_global.py) computes full polygonal images and the lexicographically first locally compatible triple of entry residue classes, allowing repeated classes; absence proves global nonexistence. [Independent regression tests](../tests/test_figurate_wp09_mod9_global.py) reconstruct the full nine-by-nine order/offset table with a distinct direct polynomial calculation, test more than 150 polygonal orders and signed offset representatives, check the proof's allowed product sets, verify the failure of modulus three to detect the obstruction, and confirm actual positive compatible pairs and negative exact-triple controls.

\`\`\`sh
python3 -m research.figurate_wp09_mod9_global --k 3 --offset 4
python3 -m research.figurate_wp09_mod9_global --k 6 --offset 7
python3 -m research.figurate_wp09_mod9_global
python3 -m unittest discover -s tests -p 'test_figurate_wp09_mod9_global.py' -v
\`\`\`

**Scientific distinction:** The earlier [WP09 tranche 001](FIGURATE_WP09_ODD_PRIME_SEPARATION_001.md) excluded a **single particular triple** for a family of offsets, by applying modulus five. This tranche proves **all-triples nonexistence** for new infinite families, using modulus nine. It does not imply Type A or Type C impossibility outside their own separately proven conditions. The proof is internally checkable elementary arithmetic; originality, independent specialist review and public mathematical certification remain open.

**Next distinct obligation:** pursue simultaneous odd-prime-power and binary local conditions in cases that survive each separately, or construct exact integer Type B triple families with correctly certified polygonal indices. Do not conflate a locally consistent residue triple with exact Diophantine existence.
