# FIGURATE WP08 — a 2-adic surjectivity theorem and complete modulus-64 local exclusions

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093) · [WP08](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125).

**Tranche 006 — 4 November 2026.** Two logically distinct outputs: (A) a constructive theorem valid for **every power of two**, and (B) an exact complete modulo-64 local-obstruction certificate. Internally checked mathematical propositions; novelty in the literature and independent specialist proof/certification remain **unverified**.

## 1. Structural theorem: binary surjectivity exactly when four does not divide the polygonal order

For each integer order $k\ge3$ and positive index $t$, set

$$
P_k(t)=\frac{(k-2)t^2-(k-4)t}{2}
      =t+(k-2)\binom t2.
$$

**Theorem 1.** The following are equivalent:

1. $4\nmid k$.
2. For **every** integer exponent $n\ge1$, the reductions $P_k(t)\pmod{2^n}$, $t\ge1$, attain **every** residue modulo $2^n$.
3. The same surjectivity holds at exponent $n=2$ (modulo $4$).

For $4\mid k$, the *complete* image modulo $4$ is only $\{0,1\}$. For $4\nmid k$, an explicit binary-lifting algorithm produces a positive index $t$ for every requested residue and exponent.

### Proof: lift one binary digit at a time

For any positive integer index increment $H$, direct subtraction gives

$$
P_k(t+H)-P_k(t)
 =\frac H2\bigl((k-2)(2t+H)-(k-4)\bigr).
\tag{1}
$$

**Case 1: $k$ odd.** Initially $P_k(1)=1$ is odd, while $P_k(3)=3k-3$ is even, so either target parity is attainable. Suppose $t$ already represents the target modulo $2^n$. Put $H=2^{n+1}$ into (1). The bracket is odd (an even term minus the odd integer $k-4$). Hence

$$
P_k(t+2^{n+1})-P_k(t)\equiv2^n\pmod{2^{n+1}}.
$$

We can therefore **choose** $t$ or $t+2^{n+1}$ to obtain either possible next binary digit, without disturbing the lower $n$ digits. Induction constructs the target modulo every $2^n$.

**Case 2: $k\equiv2\pmod4$.** The base values $P_k(1)=1$ and $P_k(2)=k$ represent both parities. Put $H=2^n$ in (1). Since $k-2\equiv0\pmod4$ and $k-4\equiv2\pmod4$, its bracket is $2\pmod4$ for $n\ge1$. Thus

$$
P_k(t+2^n)-P_k(t)\equiv2^n\pmod{2^{n+1}}.
$$

Exactly the same binary-digit induction applies, with a shorter increment.

**Case 3: $k\equiv0\pmod4$.** Write $k=4h$. Then $P_k(t)=(2h-1)t^2-(2h-2)t$. For even $t$, this is $0\pmod4$; for odd $t$, it is $1\pmod4$. Thus residues 2 and 3 never occur modulo 4, and surjectivity at exponent 2 fails.

This proves the equivalence, including a constructive algorithm and an explicit impossibility witness. The proof is independent of exhaustive enumeration.

### Corollary: classification of orders amenable to *purely 2-adic* Type B triple obstructions

For $4\nmid k$, **every** Type B order/offset pair $(k,c)$ has a *locally compatible triple of entry residues modulo every power of two*: choose entry residues $(0,0,0)$, so each shifted pair product is $c$; Theorem 1 supplies a polygonal index with value $c\pmod{2^n}$.

Although the residues repeat, they can represent **distinct positive integers**, for example $2^n,2\cdot2^n,3\cdot2^n$. Thus they must be retained in every sound local search.

**Crucial scope:** local compatibility for each modulus does **not** show that a Type B triple of distinct positive integers exists, nor even that one fixed triple works at all moduli. Rather, it shows that *no single congruence obstruction obtained solely from a power-of-two modulus* can prove global nonexistence when $4\nmid k$. Odd moduli and global Diophantine analysis remain possible.

The theorem explains, rather than merely observes, why all previous 2-power local-exclusion tables have listed orders divisible by 4 only.

## 2. Exact modulo-64 extension: four genuinely new congruence families

In addition to the prior complete modulo-32 Type B triple obstructions, the necessary local conditions modulo 64 exclude these **additional** parameter classes:

| Order restriction | Offset restriction newly excluded modulo 64 |
| --- | --- |
| $k\equiv0\pmod{32}$ | $c\equiv9\pmod{32}$ |
| $k\equiv16\pmod{32}$ | $c\equiv25\pmod{32}$ |
| $k\equiv8\pmod{16}$ | $c\equiv13\pmod{32}$ |
| $k\equiv12\pmod{16}$ | $c\equiv4\pmod{16}$ |

**Corollary 2.** In any of these four infinite families, **no Type B triple of distinct positive integers exists**, with no restriction on the size or particular value of its entries. For example, $(k,c)=(64,9),(80,25),(72,13),(76,4)$ are new modulo-64 exclusions that survived the earlier modulo-32 local test.

This is a sound implication of an exhaustive **finite arithmetic certificate**, not a claim that these four families have a separate general parity proof or have never been noticed in mathematical literature.

The complete modulo-64 exclusion set is the union of the lifted [previous modulo-32 table](FIGURATE_WP08_MOD32_GLOBAL_OBSTRUCTIONS_004.md) with the four rows above. No other order/offset cell is excluded *by this specific modulus-64 test*. A nonexcluded cell may still be globally impossible.

### Finite proof certificate with independent reconstruction

Fix modulus $m=64$. Define the complete polygonal image

$$
R_{k,m}=\{P_k(t)\bmod m:1\le t\le2m\}.
$$

The identity $P_k(t)=t+(k-2)\binom t2$ shows this image depends only on $k\bmod m$, and $P_k(t+2m)\equiv P_k(t)\pmod m$, so the $2m$ indices are exhaustive. For every one of the $64^2=4096$ order-and-offset residue cells, evaluate the three conditions

$$
ab+c\in R_{k,m},\qquad ad+c\in R_{k,m},\qquad bd+c\in R_{k,m}
\pmod m
$$

for all $\binom{64+2}{3}=45{,}760$ ordered-nondecreasing *residue triples* $(a,b,d)$, allowing repeated classes. Exclude a cell **only if** every residue triple fails. In every nonexcluded cell, save its lexicographically first witness.

The [primary implementation](../research/figurate_wp08_2adic.py) uses exact adjacency **bitsets** and intersections, whereas the [independent test suite](../tests/test_figurate_wp08_2adic.py) computes polygonal residues with the original quadratic formula and repeats the whole $64\times64$ classification with **set-valued compatibility graphs**. The independent suite compares every local first witness, not just the excluded-cell list.

The canonical JSON SHA-256 of all 4096 local first witnesses, including explicit nulls for excluded cells, is:

```text
1218764ff77c735d1fda1d27545c6fd6415b31d18ff377999eb082a808285264
```

The same tests verify every binary-lifting construction for orders $3\le k<80$ with $4\nmid k$ through exponent 10, the exact failure modulo 4 whenever $4\mid k$, the strict improvement beyond the modulo-32 table, and the continued existence of ordinary compatible Type B **pairs** for the excluded settings.

The bitset implementation computes each local compatibility graph in $O(m^2)$ arithmetic steps and tests each graph edge by a word-vector intersection (up to $m$ bits), instead of explicitly evaluating all $O(m^3)$ residue triples. This is a deterministic algorithmic representation, **not** a measured runtime improvement or a claimed complexity lower bound.

### Reproduction

```sh
python3 -m research.figurate_wp08_2adic --k 3 --exponent 9 --residue 317
python3 -m research.figurate_wp08_2adic --k 6 --exponent 9 --residue 317
python3 -m research.figurate_wp08_2adic
python3 -m unittest discover -s tests -p test_figurate_wp08_2adic.py -v
```

## 3. Next mathematical and evidence gates

Theorem 1 is a **structural all-exponents statement**, while Corollary 2 is a **complete finite local-classification statement**. These should not be conflated. In particular, the newly excluded modulo-64 classes may admit shorter direct 2-adic proofs, but none is asserted here. A meaningful successor would characterize the $4\mid k$ obstruction hierarchy by 2-adic valuation or prove stabilization/nonstabilization as exponents grow, rather than expand tables indefinitely.

**Novelty:** A targeted 2023 source comparison remains open for R. Radha, G. Janaki and M. Madhumika's *Diophantine Triples Involving Octagonal Numbers* and *Non-Extendability of Special Diophantine Triples Involving Octagonal Numbers*, listed in [*Explorations in Diophantine Equations*, pp. 50–67](https://stm.bookpi.org/EDE/issue/view/1251). The full source semantics have not been reconciled; titles alone do not establish equivalence with polygonal-output Type B. The general surjectivity theorem may have classical antecedents. **No external originality, independent specialist mathematical certification, or publication priority is claimed.**

The results here may be admitted internally with reproducible code and precise boundaries through protected governance. Public pedagogy should explain the binary-lifting insight, not just add a longer congruence table.
