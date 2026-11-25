# FIGURATE WP09-013 — exact 52-gonal Type B seed and infinite Pell orbit

**Scope:** bounded mathematical producer result for [WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145), not independent MATHCERT certification, external novelty or universal local-to-global existence.

## Theorem: a new exact parameter pair beyond the diagonal anchor

For order $k=52$ and offset $c=2$, the three distinct positive integers

$$
(a,b,d)=(2,25,703)
$$

form an exact Type B tuple, with positive 52-gonal indices $(r,s,t)=(2,8,27)$. Indeed the polygonal polynomial is

$$
P_{52}(n)=25n^2-24n,
$$

and the **exact** equalities are

$$
2\cdot25+2=52=P_{52}(2),
$$

$$
2\cdot703+2=1408=P_{52}(8),
$$

$$
25\cdot703+2=17577=P_{52}(27).
$$

This example is outside the sufficient square-shift family of WP09-010: since $52$ is divisible by four, $P_{52}(u)\equiv u^2\pmod4$, and the difference $P_{52}(u)-a^2$ can never be $2\pmod4$. It supplements the previously admitted examples at orders 20 and 36. It makes no claim of external novelty.

The parameters also pass the complete all-place local sieve of WP09-012: $52\equiv4\pmod{16}$ and $\Delta=8(52-2)2+(52-4)^2=3104=2^5\cdot97$. The only odd prime with an odd discriminant valuation is 97, where $A=(52-2)/2=25=5^2$ is a quadratic residue. Here global existence is established by the explicit exact seed, not inferred merely from local tests.

## Theorem: infinitely many exact solutions with fixed first pair

There are infinitely many positive integer Type B triples at $(k,c)=(52,2)$ whose first two entries stay $(a,b)=(2,25)$.

**Proof.** Put $R=2(k-2)=100$, $L=k-4=48$ and $D=8(k-2)c+L^2=3104$. Fix $a=2,b=25,r=2$. For the remaining indices $s,t$ introduce

$$
S=Rs-L,\qquad X=a(Rt-L).
$$

The exact polygonal equations become the Pell-type norm equation

$$
X^2-50S^2=2(2-25)D=-142784.
$$

The seed $s=8,t=27$ gives $(X,S)=(5304,752)$ and satisfies this identity. Multiplication by the positive norm-one unit $99+14\sqrt{50}$ sends

$$
(X,S)\longmapsto(99X+700S,14X+99S),
$$

preserving the norm because $99^2-50\cdot14^2=1$.

For the integer-integrality gate use the **200th power** of this unit. Direct modular multiplication gives $(99+14\sqrt{50})^{200}\equiv1\pmod{400}$ in $\mathbb Z[\sqrt{50}]$. Thus successive 200-step iterates preserve $X$ and $S$ modulo 400. In particular, $(X/2+48)/100$ and $(S+48)/100$ remain positive integer indices $t,s$, and $s$ stays even. Since $P_{52}(s)=25s^2-24s$, even $s$ makes $d=(P_{52}(s)-2)/2$ an integer. The norm equation then gives the third exact pair equality, while the first pair stays $2\cdot25+2=P_{52}(2)$. All coordinates grow strictly under positive-unit multiplication, so $d>25$ and the solutions are pairwise distinct and infinite. QED.

This uses classical Pell arithmetic and makes no priority claim; the preceding WP09-008/010 research establishes closely related amplification methods.

## Additional complete bounded census

The independent bounded arithmetic graph enumerator factors every positive $P_{52}(n)-2\le B^2$ and joins distinct vertices $a,b\le B$ exactly when $ab+2=P_{52}(n)$ for some positive integer $n$. A Type B tuple with all entries $\le B$ is precisely a triangle in this graph. At $B=2000$, the census yields **exactly one** unordered triangle, $(2,25,703)$. This is a finite-bound statement, NOT an assertion of global uniqueness. The exact Pell orbit proves global nonuniqueness outside this finite bound.

## Reproducibility

- [Exact seed, Pell transport and complete bounded graph enumeration](../research/figurate_wp09_k52_exact_pell_seed.py)
- [Separately coded polynomial arithmetic and adversarial regression tests](../tests/test_figurate_wp09_k52_exact_pell_seed.py)

Execute:

```bash
python3 -m unittest -v tests.test_figurate_wp09_k52_exact_pell_seed
python3 -m research.figurate_wp09_k52_exact_pell_seed --step 0
```

The research lane remains separate from public MkDocs editorial admission and independent MATHCERT certification. The larger WP09 and FIGURATE programmes remain open.
