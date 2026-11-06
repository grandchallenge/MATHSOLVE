# FIGURATE WP09-012 — complete everywhere-local stratification for k divisible by four and c=2 modulo four

**Status:** internal integration theorem, NOT independent MATHCERT certification or external novelty claim. The binary nonexistence theorems are ALREADY protected in WP08-002, WP08-003 and WP08-009. The odd-prime-power converse is ALREADY protected in WP09-006. This work integrates them and supplies a finite, exact all-place algorithm.

## Objective and correction of WP09-011 interpretation

Earlier WP09-011 correctly observed that for any k divisible by four and c=2 mod4, a diagonal entry-residue witness fails modulo4 even though the non-diagonal triple (1,2,3) succeeds at that single modulus. **But this is not an unresolved order family.** WP08 already proved that for k divisible by eight the offset is impossible modulo eight, and for k=12 mod16 it is impossible modulo sixteen. In particular k=8,12,16,24 and c=2 already have GLOBAL nonexistence proofs in the protected research corpus. This must be reconciled before any stronger claims about non-diagonal witnesses or new mathematical novelty are made.

## Theorem: complete local decision for this parameter family

Let k≥4 be divisible by four and let c≡2 (mod4). Define

    Δ=8(k-2)c+(k-4)².

Then simultaneous Type B compatibility at **every** prime power (equivalently, at every positive integer modulus) holds if and only if:

1. k≡4 (mod16);
2. for every odd prime p with p∤(k-2), if the integer valuation v_p(Δ) is odd, then (k-2)/2 is a quadratic **residue** modulo p.

In the second condition no test is required if Δ=0, or if p∣(k-2), or if v_p(Δ) is even. In particular, the test is finite and effective: factor the odd part of |Δ|, inspect only primes with odd valuation, and test the Legendre symbol.

If the criterion fails, there is a **finite explicit modulus that excludes all Type B triples**, independent of entry bounds:

- k divisible by eight: modulus 8, from protected WP08-002;
- k≡12 (mod16): modulus 16, from protected WP08-003;
- k≡4 (mod16) with an odd-prime violation at p and odd e=v_p(Δ): modulus p^(e+1), from protected WP09-006.

If the criterion holds, for every M≥1 there exist simultaneous local residues of all three entries and all three polygonal output indices satisfying all three pair equations mod M. The residues may depend on M. **This is NOT a theorem that exact positive-integer Type B triples exist.**

### Proof

The exact binary classification in WP08-009 states that if k≡4 (mod16), for every integer c there exists one fixed distinct positive integer triple whose three pair products plus c are 2-adic polygonal outputs at every exponent. Conversely, WP08-002 and WP08-003 exclude all residues at the displayed small moduli for the other k divisible by four when c≡2 (mod4). Thus binary local compatibility for this parameter family is equivalent to k≡4 (mod16).

By the complete odd-prime-power classification in WP09-006, a local obstruction at p^n occurs if and only if p∤(k-2), A=(k-2)/2 is a quadratic nonresidue mod p, and the **truncated** p-valuation of Δ is odd and less than n. Such an n exists if and only if the ordinary valuation e=v_p(Δ) is odd and A is a nonresidue. Its first excluding exponent is e+1. If Δ=0 no odd prime obstructs. Thus condition 2 is necessary and sufficient for compatibility at all odd-prime powers.

When both conditions hold, for any M factor M into its pairwise coprime prime-power factors. Apply the protected WP08 binary witness at the 2-factor and the WP09-006 constructive diagonal witness at every odd factor; use the Chinese remainder theorem on each of six variables (three entry and three index residues). This gives a simultaneous Type B congruence witness modulo M. Conversely any excluded prime-power factor forbids one modulo M divisible by it. QED.

## Exact classification examples

| k | c | status | certificate |
| --- | ---: | --- | --- |
| 8 | 2 | impossible, including global exact triples | binary modulus 8 |
| 12 | 2 | impossible, including global exact triples | binary modulus 16 |
| 16 | 2 | impossible, including global exact triples | binary modulus 8 |
| 24 | 2 | impossible, including global exact triples | binary modulus 8 |
| 20 | 2 | everywhere locally compatible and exact triples known | WP09-007 global Pell seed |
| 36 | 2 | everywhere locally compatible and exact triples known | WP09-011 candidate seed; protected admission of that separate candidate remains held |
| 36 | 18 | impossible, including global exact triples | Δ=5920=2⁵·5·37; nonresidue A=17 at p=5,37 |
| 68 | 2 | impossible, including global exact triples | odd-prime witnesses p=7 and 23 |

An important distinction: k=36,c=2 has an exact integer Type B example (1,343,6478), indices (5,20,362), but that exact 36-gonal example is currently part of the WP09-011 **unmerged** research candidate, not yet a protected theorem admission. Its elementary equalities are independently checkable; no protected admission is inferred from them. The k=20,c=2 exact example has already been protected-merged in WP09-007.

## Computational evidence

The source research/figurate_wp09_everywhere_local_sieve.py implements this theorem. It returns an actual finite excluding modulus when one exists, or an explicitly qualified every-modulus compatibility status when none exists; it does not fabricate an exact global tuple.

The independent test suite tests/test_figurate_wp09_everywhere_local_sieve.py checks:
- complete three-entry residue oracles at moduli 4,8,16 across many k and signed c;
- exact factorization and Legendre classification;
- independent full three-entry p² checks at odd primes for representative parameter classes;
- positive local examples and explicit impossible k8,12,16,24;
- invalid-domain checks.

The exact-head CHAD replay recorded 5/5 tests passed. This is a synthesis of existing theorems within the protected GCL repository, not new independent specialist certification.

## Mathematical frontier

For k≡4 (mod16) and c≡2 (mod4) passing every odd-prime criterion, all finite local congruence tests admit Type B triples. Some have exact positive-integer solutions, e.g. k20,c2. **The actual local-to-global existence question remains open** for the remaining parameter pairs. A fruitful next direction is systematic exact seed search for all-place-positive cases at k36,52,68,..., with explicit branch-and-bound or Pell-norm descent and separate statements about the limits of finite negative searches.

The explicitly held protected merge operation for WP09-011 is separate. Do not retry or route around that safety denial through this independent integration work package.
