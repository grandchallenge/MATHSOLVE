Find compact exact finite witnesses that improve a lower bound for the real Grothendieck constant.

# Grothendieck constant witnesses

The real Grothendieck constant is the supremum of a vector relaxation over the
corresponding signed bilinear optimization. Its exact value is open. This hill
does not ask for that value. It asks for a finite sign matrix together with
rational unit vectors that give a large exact lower-bound witness.

For a submitted sign matrix `A`, the evaluator computes exactly

```
sign(A) = max_{x_i, y_j in {-1, 1}} sum_ij A_ij x_i y_j
```

and verifies the submitted rational unit vectors `u_i`, `v_j`. Their objective

```
vector(A; u, v) = sum_ij A_ij <u_i, v_j>
```

gives the certified finite lower bound `vector / sign <= K_G`. A high score is
a useful concrete witness, not a proof of the exact Grothendieck constant.

## Submission format

Submit one directory containing exactly one regular UTF-8 JSON file:

```text
solution.json
```

It must contain exactly these fields:

```json
{
  "matrix": [[1, 1], [1, -1]],
  "left_vectors": [[[1, 1], [0, 1]], [[0, 1], [1, 1]]],
  "right_vectors": [[[3, 5], [4, 5]], [[3, 5], [-4, 5]]]
}
```

- `matrix` is an `m` by `n` rectangular list with `2 <= m,n <= 8`; every
  entry is the integer `-1` or `1`.
- `left_vectors` has `m` rows and `right_vectors` has `n` rows. Each vector
  has one common dimension `d`, where `2 <= d <= 16`.
- A coordinate is a canonical rational pair `[numerator, denominator]` with a
  positive denominator, coprime integers, and absolute values at most `10^6`.
- Every submitted vector must have squared Euclidean norm exactly one. The
  evaluator uses `fractions.Fraction`; floating-point values are invalid.
- The JSON file may not exceed 262,144 bytes. Submitted code is never run.

The example is a rational witness for the `2 x 2` CHSH sign matrix. It has
`sign(A)=2` and vector objective `14/5`, yielding the lower bound `7/5`.

## Metrics

| metric | direction | meaning |
| --- | --- | --- |
| `gap_ppm` | max | `floor(1,000,000 * vector(A;u,v) / sign(A))`, a certified lower bound scaled by one million. |
| `matrix_area` | min | `m * n`, preferring smaller witnesses when lower bounds tie. |
| `certificate_bits` | min | Sum of numerator and denominator bit lengths in the rational vectors, preferring compact certificates. |

Reports rank lexicographically. The evaluator computes the sign optimum by
exhaustive enumeration of one sign side and computes every rational dot product
exactly. It ignores any claimed score in the submission because no such field
is allowed.

## Held-out evaluator checks

The candidate witness itself is an exact, deterministic mathematical object, so
there is no training corpus or hidden target matrix. `private/validation.json`
and `private/test.json` instead contain disjoint rational witness fixtures used
to guard the evaluator's exact arithmetic. Normal evaluation checks the
validation fixture; `--final` checks the test fixture. These held-out fixtures
are never exposed to the climbing agent and cannot improve the score directly.

## What counts as progress

A score above the baseline is a fully inspectable finite lower-bound witness
for the real Grothendieck constant. Researchers can reuse the matrix, rational
vectors, sign optimum, and Gram structure in analytic or computational work.
