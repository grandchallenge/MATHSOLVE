# FIGURATE WP09-016 — complete bounded frontier census for 84-gonal and 100-gonal offsets

**Research status:** exact finite mathematical producer result, not a global nonexistence theorem, universal local-to-global result, external novelty claim, or independent MATHCERT certification. Parent [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145).

## Scope and conclusion

For the two pairs $(k,c)=(84,2)$ and $(100,2)$, **no three distinct positive integer entries $(a,b,d)$ all at most 300,000** satisfy the exact Type B system

$$
ab+c=P_k(r),\qquad ad+c=P_k(s),\qquad bd+c=P_k(t)
$$

for positive polygonal indices $r,s,t$. The exact programme enumerates all possible unordered entry triples within the bound, not just an anchored subset with small $a$, small $r$, or small $s$.

The 84-gonal run has 46,852 positive polygonal indices examined before the pair-product threshold, 17,471 distinct graph edges, and **zero triangles**. The 100-gonal run has 42,857 indices, 25,454 edges, and **zero triangles**. These are finite, replayable computational certificates with a proof of exhaustive coverage; they do not exclude larger exact triples.

## The exhaustive graph reduction

Fix $(k,c)$ and entry bound $B$. Form a graph on vertices $1,\ldots,B$. Join distinct vertices $a<b$ precisely when there is a positive integer index $n$ with $ab+c=P_k(n)$. Since $ab\le B^2$, it is sufficient and necessary to enumerate each positive $n$ up to the first with $P_k(n)-c>B^2$. For each $n$, factor the positive integer $P_k(n)-c$ and enumerate **every** divisor $a$ with $a<b=(P_k(n)-c)/a\le B$. The recorded edge is exact. Every three-entry Type B solution with all entries $\le B$ is a triangle, and conversely every graph triangle provides exact indices for all three pair products. Thus the zero-triangle result is a proof of bounded absence.

Factorization is performed by integer trial division against all primes at most $B$; after peeling every tested prime factor, any remaining factor is prime (a composite remainder would have a prime divisor no greater than $\sqrt{P_k(n)-c}\le B$). This proves all divisors are enumerated without approximation or sampling.

The [implementation](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_frontier_census_016.py) records bounds, edges, indices, and exact triples. [Independent regressions](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_frontier_census_016.py) separately evaluate $P_k(n)=n+(k-2)n(n-1)/2$, use a direct triple oracle at smaller bounds, compare divisor sets by brute force and test both full-bound zero-triangle results. Full mathematical assertions are internal research evidence, not certification.

## A structural residue lemma (unbounded)

For **any** order $k\equiv0\pmod4$ and offset $c\equiv2\pmod4$, every exact Type B triple, if one exists, has entries in the **three different** residue classes $1,2,3\pmod4$ in some order.

**Proof.** The polygonal polynomial obeys $P_k(n)\equiv n^2\pmod4$, so every pair product must lie in $\{2,3\}\pmod4$. No entry can be $0\pmod4$. Three entries all odd fail because at least two have the same odd residue and then their product is $1\pmod4$. Two even entries have product $0\pmod4$, also impossible. Thus exactly one entry is even, and it must be $2\pmod4$. The two odd entries must multiply to $3\pmod4$, so one is $1$ and the other $3\pmod4$. QED.

This strengthens the explicit non-diagonal modulo-four witness from WP09-011 into a **necessary residue classification for actual exact triples**. It is not a new global obstruction for either target: the residue pattern is compatible locally.

## Local compatibility and unresolved global existence

Both cases pass the **complete local WP09-012 sieve**. They satisfy $k\equiv4\pmod{16}$. The discriminants are

$$
\Delta_{84,2}=7712=2^5\cdot241,\qquad
\Delta_{100,2}=10784=2^5\cdot337.
$$

At the lone odd prime of odd discriminant valuation, the relevant coefficients $A=(k-2)/2$ are quadratic residues: $A=41$ modulo 241 for order 84 and $A=49=7^2$ modulo 337 for order 100. Therefore every finite modulus admits Type B congruence witnesses, but this **does not prove any positive integer triple exists**.

The previous protected WP09-013 scan covered $1\le a\le10$, $r\le69$, $s\le1099$ without these seeds. The new result covers **all entry triples** up to 300,000 without anchored restrictions. The search scope and negative conclusion must not be silently extended beyond this entry bound.

## Execution and next steps

Run:

```bash
python3 -m unittest -v tests.test_figurate_wp09_frontier_census_016
python3 -m research.figurate_wp09_frontier_census_016 --order 84 --entry-bound 300000
python3 -m research.figurate_wp09_frontier_census_016 --order 100 --entry-bound 300000
```

The remaining genuinely mathematical frontier is either an explicit exact seed for either case (which the protected fixed-pair Pell theorem may amplify when $ab$ is nonsquare), or a rigorous global exclusion that goes beyond a finite search. Independent mathematical certification, priority/source review and public programme explanation are separate admissions.
