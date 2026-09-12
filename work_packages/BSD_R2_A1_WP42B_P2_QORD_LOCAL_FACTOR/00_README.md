# BSD-R2-A1 WP42B — exact split-`2` ordinary local factor

## State

`PROVED_BOUNDED_LOCAL_NORMALIZATION`

Protected predecessors:

- MATHSOLVE WP41: `3463858d6281bcc2030d11f7f9af76c9f9097ff9`;
- MATHFORGE WP42B source admission: `a014559b89897bcfa2078147224e598ab6aaedca`.

## Result

For the selected `p=2` place, protected campaign facts give:

- `2` splits in the auxiliary imaginary quadratic field `K`;
- the Hecke character is trivial;
- `E` has good ordinary reduction at `2`, hence the local automorphic representation and its ordinary refinement are unramified.

Disegni Appendix A.3 then gives, for its canonical ordinary vectors and canonical local measure,

`Q^ord_{2,dt_2^can}=1`.

Therefore

`ord_2(Q^ord_{2,dt_2^can})=0`.

This closes the source-normalized split-`2` local toric factor inside the WP41 global ordinary factor `Q^ord`.

## Measure firewall

The statement is tied to Disegni's canonical local measure, for which `vol^circ=1`. If the chosen adelic decomposition rescales the `2`-local measure, the compensating scalar must be carried elsewhere in the global measure ledger.

Thus WP42B does not assert that every presentation of the global `Q^ord` has a literal p-local scalar one.

## Refined D2c remainder

The unresolved valuation terms are now:

1. reconciliation between the canonical local measures and the chosen global adelic measure;
2. split semistable bad primes `ell|N`;
3. auxiliary finite places in Disegni's `Sigma` and `Sigma'`;
4. remaining local L-factor/vector-normalization terms;
5. the archimedean/global normalization in the ordinary product.

No one of these is declared a unit.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.