# HC-R021-P4 — Numerical RM/Schottky transversality witness from the 17T7 genus-four Jacobian

**Campaign:** `HC-001`  
**Restricted target:** `HC-R021-A8-CM4-C2`  
**Parent development revision:** `7ac00fc389ea287971a7810ff9e5191a0105d3bb`  
**State:** `COMPUTATIONAL_EVIDENCE_ONLY__RM_SCHOTTKY_TRANSVERSALITY_NUMERICALLY_WITNESSED__EXACT_CERTIFICATION_OPEN`  
**Date:** 2026-09-16

## 1. Purpose

Supply an explicit, reproducible witness for the transverse branch of `HC-R021-L043` without promoting a numerical period calculation into an exact theorem.

`L043` reduces the ordinary-direction incidence question to

```text
T_RM subset T_Jac
    iff
canonical quadric Q_C lies in E_1 tensor E_2.
```

Equivalently, a nonzero derivative of the genus-four Schottky modular form along the relevant RM locus at the Jacobian point proves transversality analytically. The calculation below finds such a nonzero derivative to high numerical separation.

The calculation is evidence only because the Hilbert-modular period reconstruction used to locate the Jacobian point is numerical. The later arithmetic identification of the resulting genus-four Jacobian does not, by itself, certify that this floating-point tangent vector is the exact tangent vector of that algebraic model.

## 2. External datum

Use the genus-four 17T7 construction of van Bommel--Costa--Elkies--Keller--Schiavone--Voight, arXiv:2411.07857v4, together with the public code repositories:

```text
SamSchiavone/17T7
edgarcosta/EichlerShimuraHMF
```

The quartic totally real field in the reconstruction is

```text
K = Q(nu),
nu^4 - nu^3 - 3 nu^2 + nu + 1 = 0,
```

with discriminant `725`.

The field contains the quadratic subfield `Q(sqrt(5))`; one exact representative is

```text
sqrt(5) = -2 nu^3 + 2 nu^2 + 4 nu - 1,
```

up to the choice of sign of `sqrt(5)`. Direct reduction modulo the defining polynomial gives square `5`.

Thus every quartic-RM tangent direction is in particular a tangent direction for the induced quadratic `Q(sqrt(5))` RM structure relevant to `L043`.

## 3. Public Hilbert-modular period datum

`EichlerShimuraHMF/Examples/17T7.m` records the approximate moduli point

```text
z = (
  2.782906766939281866286997098793... i,
  0.754158171567683194535850592900... i,
  1.427741289884804796261342526038... i,
  5.044828437439746283467218454714... i
).
```

The same file searches the `2`-isogenous neighbours and orders them by absolute value of the genus-four Schottky modular form.

The code in `src/Utils.m` gives the Hecke-neighbour formula. Since the prime above `2` is inert in this degree-four field, the candidates are the sixteen points

```text
(z + sigma(r))/2,
r in O_K / 2 O_K,
```

plus

```text
2 z.
```

The source then chooses the neighbour with smallest Schottky value.

## 4. Independent reconstruction of the Siegel period matrix

Let

```text
d = -2 nu^3 + 4 nu^2 + 3 nu + 2
```

be the totally positive generator used for the codifferent datum. In the power basis

```text
1, nu, nu^2, nu^3,
```

the trace-pairing matrix for the polarization is

```text
P = [
  [1,0,1,1],
  [0,1,1,3],
  [1,1,3,5],
  [1,3,5,12]
],
```

with

```text
det(P)=1
```

and

```text
P^(-1) = [
  [ 2, 1,-1, 0],
  [ 1, 6, 1,-2],
  [-1, 1, 2,-1],
  [ 0,-2,-1, 1]
].
```

Writing `V` for the real-embedding Vandermonde matrix in the embedding order matching the recorded `z`, the small Hilbert period matrix is reconstructed by the public `PeriodMatrices.m` formula as

```text
tau(z) = P V^(-1) diag(z) V.
```

The resulting matrix is symmetric with positive-definite imaginary part, as required.

## 5. Schottky evaluation

`src/Schottky.m` defines the genus-four Schottky modular form directly in theta constants:

```text
S(tau)
 = pi_1^2 + pi_2^2 + pi_3^2
   - 2(pi_1 pi_2 + pi_2 pi_3 + pi_1 pi_3),
```

where each `pi_i` is the product of the eight theta constants specified in that source file.

Evaluating this formula on all seventeen `2`-isogenous candidates independently reproduces the source ordering. The unique Schottky-near-zero candidate is

```text
z_* = 2 z.
```

In ordinary double precision with a truncated theta sum, the reconstructed value is approximately

```text
|S(tau(z_*))| ~= 4.1e-34,
```

whereas the next candidate is approximately

```text
2.6e-7.
```

The public high-precision source calculation obtains a much smaller value; the `1e-34` floor here is numerical cancellation from the deliberately lightweight independent reproduction.

## 6. Directional derivative along the quartic-RM locus

Differentiate the same Schottky expression by perturbing one Hilbert-modular coordinate at a time while retaining the same polarization and period-matrix construction.

Central finite differences with step sizes

```text
h = 1e-4, 1e-5, 1e-6
```

are stable. In the four coordinate directions one obtains, to the precision justified by this calculation,

```text
dS/dz_1 ~=  1.56e-32 i,
dS/dz_2 ~=  8.51e-33 i,
dS/dz_3 ~= -9.92e-33 i,
dS/dz_4 ~= -3.41e-33 i.
```

Perturbations in the conjugate real/imaginary coordinate directions show the expected holomorphic phase relation. In particular the derivative is not numerically compatible with zero.

Because the quartic-RM tangent space is contained in the tangent space for its quadratic subfield `Q(sqrt(5))`, a certified version of any one of these nonzero derivatives would imply

```text
T_RM(Q(sqrt(5))) is not contained in T_Jac,
```

and hence the transverse branch of `L043`:

```text
dim(T_RM cap T_Jac)=5.
```

## 7. Why this is not yet HC-R021-L044 as an exact theorem

Two exactness gaps remain.

1. The moduli point `z` used to reconstruct `tau` is obtained from the numerical Hilbert-modular period pipeline. The 2026 version of the 17T7 paper rigorously identifies the relevant algebraic Jacobian and its RM endomorphism ring, but that arithmetic result does not automatically certify this floating-point period coordinate to an interval that excludes zero for the derivative.

2. The public paper does not expose, in a compact exact form, the induced `4 x 4` action of the quadratic RM generator on `H^0(K_C)` in the published canonical coordinates. Such a matrix would give a direct exact test by decomposing the canonical quadric into

```text
Q_11 + Q_12 + Q_22
```

relative to the two `Q(sqrt(5))` eigenspaces.

Therefore the present package deliberately records

```text
numerical_transversality_witness = true
exact_RM_quadric_test = open
RM_QUADRIC_A1 = open
```

and does not upgrade the lower bound on the secant obstruction rank using transversality as an exact statement.

## 8. Exact next steps

There are two independent certification routes.

### Route A — exact differential action

Recover the algebraic correspondence used in the certified endomorphism computation, induce its action on canonical differentials, and compute the two rank-two eigenspaces. For the published canonical quadric `Q_C`, test

```text
Q_C|Sym^2(E_1) != 0
or
Q_C|Sym^2(E_2) != 0.
```

Any nonzero pure block proves transversality exactly.

### Route B — interval Schottky derivative

Recompute the Hilbert period and theta constants with rigorous complex ball arithmetic, including an explicit tail bound for the theta series, then enclose one directional derivative in a ball excluding zero.

Either route would close `RM-QUADRIC-A1` for this explicit RM Jacobian.

## 9. Disposition

```text
HC-R021-L043 = retained
17T7_quadratic_subfield_Qsqrt5 = exact
17T7_Schottky_neighbour_identification = numerically_reproduced
quartic_RM_Schottky_derivative_nonzero = strong_numerical_evidence
quadratic_RM_transversality = not_yet_certified
second_factor_rank20_exists = open
HC-R021-P4 = open
restricted_target_proved = false
full_hodge_conjecture_proved = false
```

This is a Solve-package computational evidence record, not a MATHCERT disposition.
