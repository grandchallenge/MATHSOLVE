# FIGURATE WP09-031 — complete oriented ray groups for the odd square-conductor family

**Parent:** [FIGURATE WP09 #3145](https://github.com/grandchallenge/MATH-PROGRAMME/issues/3145). **Predecessors:** protected WP09-027, -029 and -030. **Precisely bounded claim:** for every positive odd conductor `f`, the complete **oriented ray-class group**, including its extension structure and invariant factors, is determined by a finite explicit quotient. This closes WP09-030's order-only gap for `A=f²=8m+1`, `O_f=Z[f√2]`. A resource guard raises an exception rather than returning a partial classification. This is not an all-parameter solution, Type A/C assertion, independent MATHCERT certification, or originality determination.

## Theorem A — a complete finite ray-group presentation

Put `K=Q(√2)`, `O_K=Z[√2]`, `O_f=Z+f O_K`, `A=f²`, and `I=f² O_f`. The narrow maximal-order class group is trivial: `O_K` is norm-Euclidean, and the negative-norm unit `1+√2` permits selection of totally positive generators. All totally positive maximal-order units are powers of `u=3+2√2`.

There is a canonical group isomorphism
```text
Cl⁺_I(O_f)  ≅
   (O_K/f³O_K)× /
   ( image〈3+2√2〉 · {1+f²j (mod f³O_K): j∈Z/fZ} ).
```
All products are taken in the actual quadratic integer ring; the residue ring is `(Z/f³)[T]/(T²−2)`. Its units are exactly pairs `(x,y)` with `gcd(x²−2y²,f)=1`, and multiplication is
`(x,y)(v,w)=(xv+2yw,xw+yv)` modulo `f³`.

**Proof (ideal extension, ray congruence and kernel).**

1. Since `I=f²O_f=f²Z+f³O_K`, the maximal-order ideal `f³O_K` is contained in `I`. The quotient `I/f³O_K` consists exactly of the scalar classes `f²j`, `j mod f`. Its ray-unit image is the subgroup `H={1+f²j}` of size `f`; its multiplication is additive in `j`, because `f⁴` is divisible by `f³`.
2. Invertible `O_f`-ideals prime to `f` correspond bijectively to `O_K`-ideals prime to `f` by extension/contraction, including fractional ideals whose `f`-localizations are the unit ideal. Since the narrow `O_K` class group vanishes, each extension admits a totally positive generator `β` coprime to `f`. Replacing `β` by a totally positive maximal-order unit changes its residue only by a power of `u`.
3. Conversely, each maximal-order residue unit is represented by a totally positive integral `β` coprime to `f`: choose a lift and add a sufficiently large positive integer multiple of `f³` to make both real embeddings positive. Contraction of `(β)` is therefore a prime-to-`f` invertible `O_f`-ideal, proving surjectivity of the residue description.
4. Two such ideals give the same oriented ray class precisely when their generator quotient, after multiplication by a totally positive maximal-order unit, is congruent to `1` modulo `I` at the `f`-localization. Reducing modulo `f³O_K`, this is exactly membership in `H`. Conversely a residue in `H` means congruence `1` modulo `f²O_f`, which is the specified ray-principal relation; the sign requirement is already satisfied. Hence the exact kernel is `〈u〉H), proving the quotient. No replacement of `I` by `f²O_K` is permitted.

This quotient determines the *full multiplication law*, not just cardinality. It is not the same as the narrow Picard quotient of WP09-030.

## Theorem B — explicit local cyclic presentation and exact invariant factors

Factor `f=∏p^e` over odd primes. The Chinese remainder theorem decomposes the numerator and `H` into local factors with moduli `p^(3e)` and scalar rays `1+p^(2e)Z`. There is only **one global diagonal relation** for the totally positive unit `u`.

Because `2` is unramified at every odd prime, the torsion part of the local residue-unit group is `C_(p²−1)` for inert primes `p≡3,5 mod8`, and `C_(p−1)×C_(p−1)` for split primes `p≡1,7 mod8`. The principal units have generators `1+p` and `1+p√2`, each of order `p^(3e−1)`; this follows by successive `p`-adic coefficient lifting (valid for odd `p`). Modding out the scalar subgroup `1+p^(2e)Z` reduces the **scalar** principal factor to `C_(p^(2e−1))`, leaving the other principal factor `C_(p^(3e−1))`. Accordingly:

```text
B_(p,e) = (O_K/p^(3e) O_K)× / (1+p^(2e)Z)
inert: C_(p²−1) × C_(p^(2e−1)) × C_(p^(3e−1))
split: C_(p−1)² × C_(p^(2e−1)) × C_(p^(3e−1)).
```

The implementation computes the precise coordinates of `u` in these groups: finite-field primitive generators and Teichmüller lifts isolate torsion coordinates; coefficientwise principal-unit digits are recovered successively and reconstructed exactly. In the CRT product `B=∏B_(p,e)=⊕C_(n_i)`, writing the image of `u` as `a=(a_i)`, the full oriented ray group is `G=B/〈a〉`.

For each prime `q` and `j≥1`, let `v_q(0)=∞`. The exact torsion counts are
```text
log_q |G[q^j]| =
    Σ_i min(v_q(n_i),j)
    − max_i max(0, min(v_q(n_i),j) − v_q(a_i)).
```
Indeed `G[q^j]` is the inverse image of `〈a〉` under multiplication by `q^j`, modulo `〈a〉`. Its cardinality is `|B[q^j]|/ord(a mod q^j B)`. Differences of successive displayed exponents give the ranks of `q^j`-torsion, and their further differences determine all elementary divisors. Padded multiplication across primes gives exact invariant factors. Product of factors is separately required to equal `|B|/ord(a)`. Thus the algorithm computes the full extension and invariant factors without guessing the splitting of the WP09-029 short exact sequence.

## Exact results (new structure, not merely order)

| Odd conductor f | Full oriented ray group | Order | Prior WP09-030 order |
|---:|:---|---:|---:|
| 1 | trivial | 1 | 1 |
| 3 | C6 | 6 | 6 |
| 5 | C20 | 20 | 20 |
| 7 | C2 × C42 | 84 | 84 |
| 9 | C54 | 54 | 54 |
| 11 | C110 | 110 | 110 |
| 13 | C13 × C156 | 2,028 | 2,028 |
| 15 | C6 × C120 | 720 | 720 |
| 17 | C2 × C272 | 544 | 544 |
| 19 | C342 | 342 | 342 |
| 21 | C6 × C6 × C42 | 1,512 | 1,512 |

Further CRT and prime-power examples: `f=25:C500`, `27:C486`, `33:C6×C1320`, `35:C2×C6×C420`, `45:C6×C1080`, `49:C2×C2058`, `63:C6×C6×C378`. These are exact finite arithmetic predictions subject to test replay, **not** global positive-index Type B existence claims.

## Evidence and strict scope

- [Exact source](https://github.com/grandchallenge/MATHSOLVE/blob/main/research/figurate_wp09_full_ray_square_conductor_031.py) implements the ring, split/inert finite-field coordinates, Hensel and principal-unit lifting, one global relation, torsion-derived invariant factors and explicit computational guards.
- [Independent tests](https://github.com/grandchallenge/MATHSOLVE/blob/main/tests/test_figurate_wp09_full_ray_square_conductor_031.py) independently enumerate *all* quadratic ring units and ray-congruence subgroups for `f=3,5,7`, count the `q^j`-torsion directly, reconcile all eleven WP09-030 order results through the earlier Picard and ray-kernel code, test composite/prime-power CRT, coefficient lifting and negative resource guards.
- Replay: `python3 -m unittest -q tests.test_figurate_wp09_full_ray_square_conductor_031`. CI/exact-head execution and protected merge must be independently observed, not inferred from committed source.

**Boundaries:** The theorem is uniform only in the odd square-conductor subfamily `A=f²`. It does not calculate narrow Picard groups for general `A=f²a_0` with `a_0≠1`, or classify all `m` with a norm ideal in the *target* oriented ray. The group may be known without any prescribed norm-ideal fibre meeting its target. No independent MATHCERT certification, external priority, or universal Type B local-to-global theorem is claimed. FIGURATE WP09 stays open for those separate problems.
