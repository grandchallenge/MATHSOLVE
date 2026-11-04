# FIGURATE WP08 — complete modulus-16 global Type B triple obstructions (tranche 003)

**Programme:** [FIGURATE-PILOT-001](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3093); [WP08 #3125](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3125). **Claim class:** elementary modular theorem with a finite exhaustive proof certificate. **Not asserted novel to mathematics; not specialist certified.**

## Theorem and strictly qualified classification

Let $k\geq3$ and $c$ be integers, and consider the Type B condition that the three pairwise shifted products of distinct positive integers belong to the polygonal sequence $P_k(t)$ at positive indices.

**Proposition.** There is no Type B triple whenever either of the following holds:

- $k\equiv0\pmod8$ and $c\equiv2,3,$ or $6\pmod8$;
- $k\equiv12\pmod{16}$ and $c\equiv2\pmod4$.

This result holds **without any bound on the tuple entries or a prescribed member**. Compatible Type B pairs still exist infinitely often for every fixed polygonal order and offset.

**Exact completeness statement:** these are precisely the order-and-offset classes for which the full *necessary* Type B triple residue condition modulo $16$ has no solution, as the following table shows.

| $k\bmod16$ | Excluded $c\bmod16$ |
| --- | --- |
| $0,8$ | $2,3,6,10,11,14$ |
| $12$ | $2,6,10,14$ |
| All other classes | None |

For a listed row, the obstruction is a rigorous global nonexistence conclusion. For an unlisted row, the existence of a compatible residue triple **does not prove a compatible integer triple exists**; stronger moduli, simultaneous equations or global arguments can still exclude it.

### Proof certificate

The standard polygonal identity

$$
P_k(t)=t+(k-2)\binom{t}{2}
$$

shows that modulo $m$, the complete image depends only on $k\bmod m$. The index shift $t\mapsto t+2m$ preserves $P_k(t)\bmod m$, so the first $2m$ positive indices give every polygonal residue.

For modulus $16$, exhaust the sixteen order residues using representatives $k=16,17,\ldots,31$. At each of the sixteen offset residues, enumerate **every multiset** of three candidate entry residues (including repetitions) and test the three shifted pair products against the calculated polygonal residue image. The following pseudocode is an entire exact finite proof; no search over increasing integer entry bounds or heuristic primality statements is required:

```python
for k in range(16, 32):
    image = {P(k,t) % 16 for t in range(1, 33)}
    for c in range(16):
        possible = False
        for a in range(16):
            for b in range(a, 16):
                for d in range(b, 16):
                    if ((a*b+c) % 16 in image and
                        (a*d+c) % 16 in image and
                        (b*d+c) % 16 in image):
                        possible = True
        record(k % 16, c, not possible)
```

The resulting excluded cells are exactly those in the table. Inclusion of repeated residues is mandatory: three distinct positive integers can have identical residues. The implementation is [a versioned exact modular classifier](../research/figurate_wp08_mod16_classification.py) and its output is independently verified in [the test suite](../tests/test_figurate_wp08_mod16_classification.py) using a distinct direct polynomial and separate enumeration.

### Direct explanatory parity argument for the new offset-3 family

The newly excluded subfamily with $k\equiv0\pmod8$ and $c\equiv3\pmod8$ also admits a transparent argument from the allowed pair-product residues.

For $k\equiv8\pmod{16}$, the target polygonal residues are $\{0,1,5,8\}$; for $k\equiv0\pmod{16}$, they are $\{0,1,8,13\}$. Subtracting $c\equiv3$ or $11\pmod{16}$ gives allowed **odd** pair products $\{5,13\}$ in either case, and exactly two allowed **even** pair products differing by $4\pmod{16}$ (up to sign).

Two even entries are impossible, since an even-even product is divisible by $4$ but each permitted even pair product is $2\pmod4$. If all entries are odd, each pair product is $5\pmod8$, so multiplying the three relations gives an odd square equal to $5\pmod8$, impossible since an odd square is $1\pmod8$.

There must therefore be exactly one even entry $a$ and two odd entries $b,d$. Both $ab$ and $ad$ are $2\pmod4$, so $a\equiv2\pmod4$. Because $bd$ must be $5\pmod8$, the two odd residues satisfy $d\equiv b+4\pmod8$; hence $ad-ab\equiv4a\equiv8\pmod{16}$. But two allowable even pair-product residues differ by only $0$ or $\pm4\pmod{16}$, never by $8$. This contradiction proves the offset-3 subfamily without relying on the enumeration.

The additional $k\equiv12\pmod{16}$ family is established by the exhaustive exact residue certificate above; no simpler closed-form proof has yet been admitted for that subfamily.

### Relation to the previously admitted theorem

The earlier [modulus-8 global obstruction](FIGURATE_WP08_GLOBAL_TRIPLE_OBSTRUCTION_002.md) excluded triples when $k\equiv0\pmod8$ and $c\equiv2$ or $6\pmod8$. The present theorem strictly enlarges that set of excluded parameter classes, while preserving the precise family taxonomy and the distinction between local compatibility and actual integer existence.

### Reproduction and novelty boundaries

```sh
python3 -m research.figurate_wp08_mod16_classification
python3 -m research.figurate_wp08_mod16_classification --k 8 --offset 3
python3 -m unittest discover -s tests -p test_figurate_wp08_mod16_classification.py -v
```

The independent suite checks all 256 order/offset residue classes, order lifting, positive and negative offset representatives, pairs that really exist, and bounded attempts to contradict the excluded triples. The finite residue computation establishes an arithmetic necessity statement; the bounded searches are ancillary.

**Source and certification restriction:** Polygonal nonextension problems have extensive prior art, and the prior source catalogue remains incomplete for this exact octagonal-output condition. This is a substantive **new-to-GCL** strengthening, not a claim of external discovery. An independent specialist proof check, literature-semantic comparison and formal certification remain separate open obligations; protected repository admission is not a substitute for them.
