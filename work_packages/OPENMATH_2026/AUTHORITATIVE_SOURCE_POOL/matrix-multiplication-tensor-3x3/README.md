Find exact low-rank decompositions of the tensor for general 3 by 3 matrix multiplication over the rationals.

## Task

Construct a bilinear algorithm for multiplying two arbitrary `3 x 3` matrices. The longstanding open problem is whether this tensor has rank at most 22. Rank 23 is known; the supplied baseline is Laderman's rank-23 decomposition.

Your submission gives three factor matrices `U`, `V`, and `W`. With row-major input coordinates `A[0], ..., A[8]` and `B[0], ..., B[8]`, each term `t` computes

```
L_t(A) = sum_i U[t][i] A[i]
R_t(B) = sum_j V[t][j] B[j]
M_t = L_t(A) R_t(B)
```

and the output is reconstructed as `sum_t W[t][k] M_t`. The `W` coordinate for output entry `C[row][column]` is `3 * column + row` (column-major).

The evaluator expands every candidate exactly and checks all 729 Brent identities. It never executes submission code. A rank-22 certificate would be a major result; a new exact rank-23 decomposition with lower support is meaningful progress for this hill.

## Submission format

A submission is a directory containing exactly one regular file:

```text
solution.json
```

It is an object with exactly three fields:

```json
{
  "u": [[0, 1, 0, 0, 0, 0, 0, 0, 0]],
  "v": [[1, 0, 0, 0, 0, 0, 0, 0, 0]],
  "w": [[1, 0, 0, 0, 0, 0, 0, 0, 0]]
}
```

`u`, `v`, and `w` must each be a list of the same number of rows, between 1 and 40. Every row has exactly 9 exact rational coefficients. Write an integer as a JSON integer, or a non-integral rational as `[numerator, denominator]` with a positive denominator. Numerators and denominators have absolute value at most one million.

The example above is only one schoolbook term and is not a complete algorithm. A valid submission must satisfy the complete matrix-multiplication tensor identity.

## Metric

| metric | direction | meaning |
|---|---|---|
| `rank` | min | Number of bilinear products, namely the number of rows of `u`, `v`, and `w`. |
| `support` | min | Total number of nonzero coefficients in `u`, `v`, and `w`; a compactness tie-breaker, not a claimed addition count. |

Scores rank lexicographically, then compare support among equal-rank schemes. The evaluator computes both values from the submitted factor matrices.

## Exact and held-out checks

The 729 symbolic identities are decisive, so no random sample can substitute for correctness. Private validation and final files contain disjoint concrete matrix-product replays as an additional regression guard; they do not weaken or replace the full symbolic check. Run the held-out mode with:

```text
hills eval <submission> -H matrix-multiplication-tensor-3x3 --final
```

## Fixed conventions

- `A` and `B` use row-major coordinate order.
- `W` uses the stated column-major coordinate order for `C`.
- Scalar products preserve the order `L_t(A) R_t(B)`, so ternary certificates also apply to noncommutative rings.
- Coefficient encoding, full tensor target, and both metric definitions are fixed in this hill version.
