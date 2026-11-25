# FIGURATE WP09-014 — exact 52-gonal Type B family at offset six

**Programme:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Authority:** bounded producer research. No external originality, general local-to-global theorem or independent MATHCERT certification is claimed.

## New positive-integer seed

For polygonal order $k=52$ and offset $c=6$, there is an exact Type B triple with positive distinct entries $(a,b,d)=(2,2279,4757)$ and positive indices $(r,s,t)=(14,20,659)$. With $P_{52}(n)=25n^2-24n$:

$$
2\cdot2279+6=4564=P_{52}(14),
$$

$$
2\cdot4757+6=9520=P_{52}(20),
$$

$$
2279\cdot4757+6=10841209=P_{52}(659).
$$

This is a new *parameter pair in GCL's protected result record*, not a published-literature novelty assertion. It falls outside the sufficient square-shift family of WP09-010: since $52\equiv0\pmod4$, the difference $P_{52}(u)-a^2$ never equals $6\equiv2\pmod4$.

It is consistent with the full local sieve WP09-012: $52\equiv4\pmod{16}$, and $\Delta=8(50)(6)+48^2=4704=2^5\cdot3\cdot7^2$. The only odd prime of odd discriminant valuation is $p=3$, where $A=(52-2)/2=25$ is a quadratic residue modulo 3. Local compatibility does not imply global existence; the exact seed supplies the additional global evidence.

## Infinite exact Pell family

The already protected general fixed-first-pair Pell theorem from WP09-013 applies because $ab=4558$ is nonsquare. The seed determines $R=100$, $L=48$, $\Delta=4704$ and

$$
S=100s-48,\qquad X=2(100t-48),
$$

satisfying the exact norm identity

$$
X^2-4558S^2=2(2-2279)4704.
$$

A suitable positive norm-one Pell unit power preserves the required residue lattice and generates infinitely many exact positive integer Type B triples keeping entries $(2,2279)$ fixed. This is an application of the protected general theorem, not an independently certified strengthening.

## Complete finite bound and limitations

The separate producer enumerator factors each positive $P_{52}(n)-6\le10000^2$, includes every admissible factor pair with both entries at most 10,000, and searches the complete arithmetic graph for three-vertex cliques. Every Type B triple within the entry bound corresponds to one such clique, and every clique verifies the exact integer equations. The resulting bounded census has **one unordered triple**, $(2,2279,4757)$, when all entries are at most 10,000. This statement is finite; the Pell theorem implies other solutions at larger entries. No infinite exclusion or global uniqueness is inferred.

## Exact arithmetic and documentary obligations

- [Bounded graph enumerator and inverse polygonal arithmetic](../research/figurate_wp09_k52_c6_exact_seed.py)
- [Independent polynomial, exhaustive small-bound, and Pell regression tests](../tests/test_figurate_wp09_k52_c6_exact_seed.py)
- Re-run: `python3 -m unittest -v tests.test_figurate_wp09_k52_c6_exact_seed`
- Re-run: `python3 -m research.figurate_wp09_k52_c6_exact_seed --entry-bound 10000`

WP09 continues to seek an exact seed or a **rigorous nonexistence theorem** for everywhere-local pairs such as $(68,6)$, $(84,2)$ and $(100,2)$. A failed finite search does not establish global nonexistence. Public MkDocs review and independent certification are separate transitions.
