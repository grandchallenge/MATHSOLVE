# BSD-001 frontier after WP43A

## Protected predecessors

- MATHSOLVE WP42B: `15f264595f2929270cea84009e943ed1535f021b`.
- MATHFORGE WP43A source admission: `d7114e8c61ff0fb414e95a162800a7199f1dec0a`.

## WP43A closure

The strict-Greenberg side of the cyclotomic compatibility problem is closed.

For the protected literal-`p=2`, totally imaginary field `K`, Nekovář's first-order cyclotomic augmentation triangle induces compatible Greenberg local conditions and an exact triangle of strict Selmer complexes. Its specialization connecting morphism is the first cyclotomic Bockstein used in WP37.

Therefore the former broad boundary

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`

is replaced by the strictly narrower boundary

`MISSING_P2_KUMMER_IWASAWA_LOCAL_CONDITION_COMPLEX_AND_SPECIALIZATION_OVER_K`.

The missing object is the integral classical-Kummer cyclotomic Selmer condition/comparison over `K`, not the strict-side Bockstein naturality.

## Live boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

### D1c

`MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.

### D2a

`MISSING_P2_K_HEIGHT_NONDEGENERACY`.

### D2b

WP40 proves

`j_K+d_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

To relate `d_K` to the WP37 height/Bockstein formalism, a successor must construct an integral cyclotomic classical-Kummer object `C_Kum,infty` over `K`, a comparison morphism from the protected strict Iwasawa complex, and exact derived augmentation recovering WP39/WP40's finite quotient. A rationalized or finite-error comparison is insufficient.

### D2c

WP42B proves the canonical selected split-`2` ordinary local toric factor is one:

`Q^ord_{2,dt_2^can}=1`.

The next local boundary is

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`.

Global/local measure reconciliation, split semistable bad primes, auxiliary finite places, remaining local L/vector terms, and global normalization remain open.

### D2d

`MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.

### D2e

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successors

### WP44A — classical-Kummer Iwasawa local condition over `K`

Search narrowly for a literal integral construction that provides the local Kummer condition throughout the cyclotomic tower and packages it in a Selmer complex over the Iwasawa algebra. The required properties are:

1. integral `p=2` validity;
2. compatibility with corestriction/base change through the tower;
3. a strict-Greenberg-to-Kummer comparison morphism;
4. a perfect or controlled derived object over the Iwasawa algebra;
5. derived augmentation equal to the WP39/WP40 finite quotient, not merely isogenous to it.

If no source supplies this exact object, the constructive route is to define the mapping-fibre local condition from finite-level Kummer complexes and prove derived base-change directly.

### WP44B — semistable split bad-prime `Q^ord` factors

Continue the exact local Rankin–Selberg/newvector calculation for each odd `ell|N`, preserving split/nonsplit multiplicative type, Steinberg twist, local Haar measure, local L-factor, denominator pairing, and Tamagawa-sensitive terms.

## Claim firewall

Do not promote:

- strict-Greenberg Bockstein naturality to existence of the missing Kummer Iwasawa object;
- any rationalized/up-to-finite-error Kummer comparison to the exact `2`-primary defect;
- canonical `Q^ord_2=1` to global `Q^ord=1`;
- interpolation of semistable local zeta integrals to their explicit values;
- height existence to nondegeneracy;
- BSD or MATHCERT certification.
