# BSD-R2-A1 WP60K — selected mod-4 BSS finite Hypothesis 3.2 obstruction

## Status

This package continues `BSD-001` / #215 after protected WP60J.

Protected entering MATHSOLVE head:

`d5159aabcfb03129ca1ef669f506870974988605`.

Operation: #229.

## Result

For every curve in the selected `BSD-R2-A1` class:

1. protected WP60J gives
   `Gal(Q(E[4])/Q)=GL_2(Z/4)`;
2. exact finite computation proves
   `|H^1(GL_2(Z/4),(Z/4)^2)|=2`;
3. for the formal literal-`p=2` BSS II coefficient specialization
   `R=Z/4`, `A=E[4]`, `M=4`, the restriction quotient
   `Gal(K(A)_4/Q) -> Gal(Q(E[4])/Q)`
   has kernel acting trivially on `A`, so inflation injects this nonzero cohomology into
   `H^1(K(A)_4/Q,A)`;
4. hence BSS II Hypothesis 3.2(iii) fails already at coefficient level `E[4]`;
5. Weil self-duality gives the same failure for `A^*(1)`.

Record:

`BSS_LITERAL_P2_SELECTED_FINITE_HYP32III_FAILS_AT_E4`

and

`R5_BSS_STANDARD_FINITE_HYPOTHESIS_ROUTE_BLOCKED_ALREADY_AT_MOD4`.

## Relation to WP60J and WP60I

There is no contradiction.

- WP60J proves the residual coefficient module `E[2]` satisfies BSS II Hypotheses 3.2 and 3.3.
- WP60K proves the next coefficient module `E[4]` fails Hypothesis 3.2(iii).
- WP60I proves the related BSS III infinite `(H3)` condition fails on the full `2`-power division tower.

Thus the first failure of the standard finite BSS cohomological hypothesis is already visible at mod `4`.

## Exact replay

Run:

```bash
python work_packages/BSD_R2_A1_WP60K_BSS_MOD4_HYP32_OBSTRUCTION/02_GL2Z4_Z4_H1_CERTIFICATE.py
```

The certificate exhausts all `96` elements of `GL_2(Z/4)`, all consistent generator assignments for `1`-cocycles, all `16` coboundaries, and verifies the cocycle identity on every ordered pair for every accepted cocycle.

## Route consequence

The standard BSS finite-level/inverse-limit control chain cannot be recovered by simply extending the WP60J residual verification level-by-level: the required finite cohomology vanishing is false at `E[4]`.

A BSS-derived literal-`2` reopening must therefore weaken, replace, or bypass finite Hypothesis 3.2(iii), in addition to resolving any required core-vertex/connectivity issue.

This is not an impossibility theorem for all literal-`2` Kolyvagin, Euler-system, determinant, or Fitting methods.

`BSD-R2-A1` remains unproved. MATHCERT is not invoked.
