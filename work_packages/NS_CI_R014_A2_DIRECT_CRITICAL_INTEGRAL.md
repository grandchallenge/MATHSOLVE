# NS-CI-R014-A2-L5 — Direct critical-integral decomposition

## Status

- Campaign: `NS-CI-001`
- Parent: `MATHSOLVE#24`
- Tracker: `MATHSOLVE#59`
- State: `INITIALIZED_INDEPENDENT_CROSS_CHECK`
- A2 status: unproved
- Numerical lane: closed

## 1. Question

Can one prove directly that

```math
\int_0^T\|u(t)\|_6^4dt<\infty
```

from `Lambda in L2_t` and the Leray energy class, without first proving the low-mode coefficient `f` belongs to `L1_t`?

This lane must remain genuinely independent of L4. A decomposition that merely renames `f` is not a second proof route.

## 2. Scaling table

Under

```math
u_\rho(x,t)=\rho u(\rho x,\rho^2t),
```

with viscosity fixed:

| Quantity | Scaling factor |
|---|---:|
| `dt` | `rho^-2` |
| `Lambda`, `lambda_q` | `rho` |
| `||u||_2` | `rho^-1/2` |
| `||u||_6` | `rho^1/2` |
| `||u||_6^4` | `rho^2` |
| `||grad u||_2` | `rho^1/2` |
| `||grad u||_2^2` | `rho` |
| `Lambda^2 dt` | invariant |
| `||u||_6^4 dt` | invariant |

The target integral and the `Lambda L2` hypothesis are both critical. A valid majorant must preserve this balance.

## 3. Imported analytic tools

The audit may use, with constants independent of `Q`:

```math
\|v\|_6\lesssim\|\nabla v\|_2,
```

for suitable whole-space functions,

```math
\|u_q\|_r
\lesssim
\lambda_q^{3(1/p-1/r)}\|u_q\|_p,
```

for annular blocks and `p<=r`, and a justified Littlewood–Paley square-function estimate.

The exact version used at each step must be named. Triangle estimates and square-function estimates are not interchangeable without loss.

## 4. Moving-cutoff split

At almost every time set

```math
u=u_{\le Q}+u_{>Q},
\qquad
\Lambda=\lambda_Q.
```

The elementary inequality

```math
\|u\|_6^4
\lesssim
\|u_{\le Q}\|_6^4
+
\|u_{>Q}\|_6^4
```

is harmless, but each term must acquire its own `L1_t` majorant.

## 5. Low-frequency baseline

Sobolev and the spectral cutoff give

```math
\|u_{\le Q}\|_6^4
\lesssim
\|\nabla u_{\le Q}\|_2^4.
```

One factor may be bounded by

```math
\|\nabla u_{\le Q}\|_2^2
\lesssim
\Lambda^2\|u_{\le Q}\|_2^2
\le
\Lambda^2\|u_0\|_2^2.
```

Therefore

```math
\|u_{\le Q}\|_6^4
\lesssim
\|u_0\|_2^2
\Lambda^2
\|\nabla u_{\le Q}\|_2^2.
```

This estimate is scaling correct. It does **not** close in time: both

```math
\Lambda^2
\quad\text{and}\quad
\|\nabla u\|_2^2
```

are known only in `L1_t`, and the product of unrelated `L1_t` functions need not be integrable.

This is the direct lane's baseline obstruction. A successful low-frequency estimate must exploit correlation, shell weights, or a different interpolation—not simply repeat this product.

A cruder Bernstein estimate gives

```math
\|u_{\le Q}\|_6^4
\lesssim
\Lambda^4\|u_0\|_2^4,
```

which requires `Lambda in L4_t` and is strictly worse.

## 6. Shellwise low-frequency reformulation

Using a square function, one may seek estimates based on

```math
\|u_{\le Q}\|_6^2
\lesssim
\left\|
\sum_{p\le Q}|u_p|^2
\right\|_3.
```

The proof must then determine whether the fourth power can be reorganized into a weighted bilinear shell sum whose time integral is controlled by `Lambda L2` and shell dissipation.

Required ledger entries:

- diagonal `p=r` terms;
- off-diagonal `p<r` terms;
- frequency ratio weights;
- row and column sums;
- dependence on `Q`;
- whether the result is genuinely different from L4.

## 7. Strict high-mode information

For shells strictly above the dissipation wavenumber, the definition supplies schematically

```math
\|u_p(t)\|_\infty
<
c_0\nu\lambda_p,
\qquad p>Q(t),
```

with the exact source normalization to be reconstructed.

Interpolation gives

```math
\|u_p\|_6
\le
\|u_p\|_2^{1/3}\|u_p\|_\infty^{2/3},
```

hence

```math
\|u_p\|_6^2
\lesssim
\nu^{4/3}\lambda_p^{4/3}\|u_p\|_2^{2/3}.
```

In terms of shell enstrophy

```math
A_p=\lambda_p^2\|u_p\|_2^2,
```

this becomes

```math
\|u_p\|_6^2
\lesssim
\nu^{4/3}\lambda_p^{2/3}A_p^{1/3}.
```

The positive power `lambda_p^(2/3)` shows that the strict high-mode threshold does not by itself make the `L6` shell sum converge. Additional use of dissipation, orthogonality, or nonlinear structure is required.

This calculation also prevents an invalid inference: an upper bound on `||u_p||_infinity` does not imply an upper bound on `||u_p||_2` through Bernstein.

## 8. High-frequency proof obligations

The high-frequency lane must test, in order:

1. square-function summation rather than triangle summation;
2. weighted Hölder across shell index;
3. use of the time-integrated dissipation `nu int A_p dt`;
4. separation of the finite near-threshold cluster from the strict tail;
5. possible absorption of the strict tail into viscosity;
6. uniformity as the maximal frequency tends to infinity.

A finite shell truncation is not evidence of convergence.

## 9. Time-integrability ledger

Every candidate pointwise bound must be reduced to factors from this table:

| Factor | Known control |
|---|---|
| `Lambda^2` | `L1_t` by hypothesis |
| `||u||_2` | `Linfinity_t` by energy |
| `||grad u||_2^2` | `L1_t` by energy |
| `||u||_4^2` | `L^(4/3)_t` consequence of energy interpolation |
| `D_p=nu||grad u_p||_2^2` | summable in `L1_t l1_p` |
| low-mode coefficient `f` | target of another route; not imported |

The ledger must state the exact Hölder exponents. Phrases such as “integrable by energy” are insufficient when a product is present.

## 10. Proof-obligation DAG

```text
L5-0 scaling and source normalization
    |
    v
L5-1 justified LP representation of ||u||_6
    |
    v
moving split at Q(t)
    |
    +-----------------------+
    |                       |
    v                       v
low shell bilinear form   strict high-tail series
    |                       |
    +-----------+-----------+
                |
                v
      time-integrability ledger
                |
                v
      uniform L1 majorant or route termination
```

## 11. Mandatory adversarial checks

### Check A — unrelated `L1` product

Use scalar functions `a,b in L1` with `ab notin L1` to reject any unsupported product closure.

### Check B — threshold direction

The strict high-mode bound may not be used at `p=Q` or below.

### Check C — Bernstein direction

`||u_p||_infinity <= C lambda_p^(3/2)||u_p||_2` does not allow an upper bound on `||u_p||_2` from an upper bound on the supremum.

### Check D — shell-sum endpoint

Compute every geometric series and endpoint exponent explicitly. A ratio equal to one produces a logarithmic divergence.

### Check E — hidden low-mode criterion

Any coefficient equivalent to `sup_{p<=Q} lambda_p||u_p||_infinity` must be cross-referenced to L4 and may not be called an independent closure.

## 12. Pedagogical lemma template

Each lemma must include:

1. exact statement and cutoff convention;
2. scaling check;
3. named analytic tools;
4. line-by-line exponent arithmetic;
5. shell-sum convergence calculation;
6. time-integrability table;
7. counterfixture;
8. disposition.

## 13. Acceptance criterion

L5 closes only if it proves

```math
\|u(t)\|_6^4
\le
G(t)
```

for almost every time, where

```math
G\in L^1(0,T)
```

with norm controlled by `int Lambda^2`, Leray data, viscosity, and `T`, uniformly across frequency truncations.

A conditional estimate involving a new shell norm must be promoted as a narrower theorem candidate, not as A2.

## 14. First executable task

Derive the exact Littlewood–Paley low/high formula and produce a complete exponent table for the diagonal and off-diagonal low-frequency terms and the strict high tail.

## Claim boundary

This document initializes the direct lane and records baseline deductions. It does not prove the critical integral is finite.