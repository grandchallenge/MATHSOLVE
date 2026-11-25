# FIGURATE WP08 — complete classification of orders uniformly admitting 2-adic Type B triples

**Programme:** [FIGURATE #3093](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093); [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125). **Tranche 009, 5 November 2026.**

**Claim scope:** an exact, internally tested theorem about **a single fixed triple satisfying every binary congruence simultaneously**. It does not assert a Type B Diophantine triple with exact positive-index polygonal outputs, establish originality relative to the literature, or grant independent mathematical certification.

## Main theorem: necessary and sufficient classification of polygonal orders

For a polygonal order $k\ge3$, say **uniformly 2-adically Type B admissible** if, **for every integer offset** $c$, there exist **three fixed, distinct, positive integers** $a,b,d$ such that, for every exponent $n\ge1$, each of $ab+c$, $ad+c$ and $bd+c$ is congruent to a $k$-gonal number at some positive index (which may depend on $n$ and the pair).

**Theorem.** The following are equivalent:

1. $k$ is uniformly 2-adically Type B admissible.
2. $4\nmid k$ **or** $k\equiv4\pmod{16}$.

If the condition fails, the single offset **$c=2$** already has no locally compatible Type B triple at modulus $16$ (for $k\equiv12\pmod{16}$) or modulus $8$ (for $8\mid k$).

**Interpretation:** This completes the *all-offset* 2-adic admissibility question for polygonal orders. It does **not** classify individual offsets when $k\equiv0,8,12\pmod{16}$: some are permitted and some are obstructed.

### Proof of sufficiency, case I: $4\nmid k$

The previously admitted [constructive binary-surjectivity theorem](FIGURATE_WP08_2ADIC_SURJECTIVITY_MOD64_006.md) shows that every 2-adic remainder is polygonal for such an order, at **every exponent**. Consequently the same ordinary integer triple $(a,b,d)=(1,2,3)$ works locally for every $c$ and $n$: its pair outputs $2+c$, $3+c$, $6+c$ are automatically represented modulo every $2^n$.

### Proof of sufficiency, case II: $k\equiv4\pmod{16}$

Set $A=k/2-1$, $q=k/4-1$ and $D=Ac+q^2$. Then

$$
A\equiv1\pmod8,
\qquad A\in\mathbb Z_2^\times,
\qquad A=s^2\text{ for a unit }s\in\mathbb Z_2.
$$

The last assertion is the classical exact criterion for an odd 2-adic unit to be a square. Write

$$
C=\frac{D}{A}\in\mathbb Z_2.
$$

Choose $t\in\{2,3\}$ so $t^2+t-C\ne0$ in $\mathbb Z_2$: take $t=2$ unless $C=6$, in which case take $t=3$. Define the **formal 2-adic entries**

$$
a_0=1,\qquad b_0=t^2-C,\qquad d_0=(t+1)^2-C.
$$

Direct algebra (the regular pair-to-triple construction) gives three exact identities in $\mathbb Z_2$:

$$
b_0+C=t^2,\quad d_0+C=(t+1)^2,\quad
b_0d_0+C=(b_0+t)^2.
\tag{1}
$$

Since $A=s^2$, multiplying (1) by $A$ gives

$$
A(a_0b_0+c)+q^2=(st)^2,
\quad A(a_0d_0+c)+q^2=(s(t+1))^2,
\quad A(b_0d_0+c)+q^2=(s(b_0+t))^2.
\tag{2}
$$

The three roots in (2) are **nonzero** by choice of $t$.

**Integer approximation lemma.** If $u=r^2$ for a nonzero $r\in\mathbb Z_2$, then any $v\in\mathbb Z_2$ satisfying

$$
v\equiv u\pmod{2^N},\qquad N\ge2v_2(r)+3
$$

is also a square in $\mathbb Z_2$. Indeed $v$ has the same even valuation as $u$, and after removing that power of two its odd unit remains $1\pmod8$.

Choose

$$
N\ge\max\{4,\ 2v_2(t)+3,\ 2v_2(t+1)+3,\ 2v_2(t^2+t-C)+3\}.
$$

Compute the ordinary modular residue $C_N=D A^{-1}\pmod{2^N}$ and put $M=2^N$. Select positive integers

$$
a=1,\quad
b=M+((t^2-C_N)\bmod M),\quad
d=2M+(((t+1)^2-C_N)\bmod M).
\tag{3}
$$

Then $1<b<d$, so the entries are distinct and positive. They are congruent to $(a_0,b_0,d_0)$ modulo $M$. Therefore all three transformed pair expressions in (2), with $b,d$ replaced by the integers from (3), are congruent to the corresponding **nonzero squares** modulo $M$. By the approximation lemma, each is a square in $\mathbb Z_2$.

Finally, the exact [polygonal square normal form](FIGURATE_WP08_2ADIC_SQUARE_NORMAL_FORM_007.md) states that for every $n\ge1$,

$$
z\text{ is polygonal modulo }2^n
\iff Az+q^2\text{ is square modulo }2^n.
$$

Hence (3) is **one fixed positive integer Type B triple satisfying all binary local tests simultaneously**, for *any* offset $c$. No entries change when $n$ increases. This proves sufficiency.

**Worked complementary-offset example.** For $k=20,c=2$, $A=9,q=4,D=34$. Here $D$ is **not** a 2-adic square (valuation $1$), so the preceding one-sixth density theorem gives no witness. The new construction takes $t=2$, $N=7$, and produces

$$
(a,b,d)=(1,242,375).
$$

All three outputs $244,377,90752$ pass every power-of-two 20-gonal congruence test, but are **not asserted to equal** 20-gonal integers. This is strictly beyond the predecessor's offset-immunity criterion.

### Proof of necessity, direct residue contradictions at $c=2$

If $k$ fails the displayed order criterion then either $8\mid k$ or $k\equiv12\pmod{16}$.

**If $8\mid k$**, then $P_k(t)\bmod8\in\{0,1,5\}$. At offset $c=2$, each pair product must be $2$ or $3\pmod4$. A hypothetical triple cannot contain two even entries (their product is $0\pmod4$), or three odd entries (the product of the three pair products is the square $(abd)^2\equiv3\pmod4$). With exactly one even entry $a$ and two odd entries $b,d$, the products $ab,ad$ must be $2\pmod4$, while $bd\equiv3\pmod4$ makes $b,d$ opposite odd classes. Then $ab$ and $ad$ differ by four modulo eight, but both $ab+2$ and $ad+2$ would have to equal the **sole even polygonal residue zero modulo eight**. Contradiction. This is the direct [tranche-002 proof](FIGURATE_WP08_GLOBAL_TRIPLE_OBSTRUCTION_002.md).

**If $k\equiv12\pmod{16}$**, then $P_k(t)\bmod16\in\{0,1,9,12\}$; with $c=2$ all permitted pair products must lie in

$$
S=\{7,10,14,15\}\pmod{16}.
$$

Every member of $S$ is $2$ or $3\pmod4$. The preceding parity argument again rules out two even entries and all three odd entries. Thus exactly one entry, say $a$, is even and satisfies $a\equiv2\pmod4$, while $b,d$ are odd. Their product $bd$ must lie in the odd part $\{7,15\}$ of $S$, so $bd\equiv7\pmod8$. Every odd $b$ is its own inverse modulo eight; hence $d\equiv-b\pmod8$ and $b+d\equiv0\pmod8$. Consequently

$$
ab+ad=a(b+d)\equiv0\pmod{16}.
$$

But each even product $ab,ad$ must lie in $\{10,14\}\pmod{16}$, and the negative of either $10$ or $14$ is $6$ or $2$, neither allowed. Contradiction.

Thus $c=2$ is 2-adically impossible for **every** order outside the two sufficient classes, establishing necessity and proving the theorem.

## Executable and independent verification

The [constructive source](../research/figurate_wp08_uniform_admissibility.py) gives the **fixed positive integer triple** and the precision $N$ used in the proof; it uses modular inversion, not numerical optimization or speculative heuristics. The [independent test suite](../tests/test_figurate_wp08_uniform_admissibility.py) verifies:

- the complete order classification for $3\le k<194$ against prior exact local obstructions;
- more than 1,900 **complementary offsets** not covered by the earlier one-sixth theorem, each passing exponents $1$–$8$, $16$, $32$, $64$, $128$;
- independent direct quadratic-polynomial residue membership through exponent eight, for several polygonal orders;
- the three exact 2-adic formal square identities and nonzero-root precision thresholds, including negative offsets;
- the $k\equiv12\pmod{16}$ necessity argument's permitted residue set and parity implication;
- the alternative $t=3$ seed branch, very large positive/negative offsets and high precision $2^{256}$;
- the distinction between a locally valid triple and an *actual integer Type B tuple* (e.g., $(1,130,263)$ for squares at offset $2$ passes every binary test but is not an exact Type B triple).

```sh
python3 -m research.figurate_wp08_uniform_admissibility --k 20 --offset 2 --exponent 128
python3 -m research.figurate_wp08_uniform_admissibility --k 12 --offset 2 --exponent 16
python3 -m unittest discover -s tests -p test_figurate_wp08_uniform_admissibility.py -v
```

## Novelty and next research boundary

The algebra (1) is an instance of the classical **Euler regular extension** of a pair to a Diophantine triple. Historical context appears in A. Dujella's [lecture notes on Diophantine tuples](https://web.math.pmf.unizg.hr/~fran/Istanbul2025/Diophantine-m-tuples.pdf) and [Cipu et al., *Journal of Number Theory* 210 (2020), pp. 433–475](https://repozitorij.grad.unizg.hr/en/articles/grad%3A2686/show-file/0). The present theorem is a **local 2-adic polygonal-output application** with a fixed integer approximation and a full order-class converse. Neither the Euler construction nor square-unit arithmetic is claimed original.

Routine GCL proof/code admission demonstrates internal reproducibility, **not** independent expert certification or literature priority. The theorem does not establish exact positive-integer Type B triples for all offsets; a simultaneous *global* polygonal-index and Pell-equation analysis remains necessary. The next substantive programme question is whether the remaining order classes $k\equiv0,8,12\pmod{16}$ admit a more refined parameter-uniform classification of their individual offsets, avoiding unbounded residue-table growth.
