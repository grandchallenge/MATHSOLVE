# RH-R039-QW-PARITY-GAP-EVIDENCE-001

Campaign: RH-001

Protected theorem predecessor:
- MATHSOLVE@4c16cade154a0538f9dde8c12d0b3c2f3f0778fd
- RH-R037-QW-SECTOR-GALERKIN-001

Protected source substrate:
- MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b

Protected claimed-proof audit:
- MATHFORGE@a11c6dedede09af6f3c67c5eec337941b73d4d3a

## Purpose

RH-R037 proves, for each fixed lambda,

    epsilon_{+,N} -> epsilon_+
    epsilon_{-,N} -> epsilon_-
    g_N := epsilon_{-,N} - epsilon_{+,N} -> g.

R039 asks only what the exact finite CCM matrices do numerically under
high-precision, cross-checked assembly.

It is an evidence tranche, not a proof tranche.

## Exact finite matrix

The runner implements the protected CCM formula

    QW_lambda = W_{0,2} - W_R - sum_p W_p

in the Fourier basis V_n, |n| <= N.

It then uses the exact inversion symmetry to form the even and odd blocks:

    E_mn = QW(V_m,V_n) + QW(V_m,V_-n)       (m,n > 0)

    O_mn = QW(V_m,V_n) - QW(V_m,V_-n)       (m,n > 0),

with the standard sqrt(2) normalization for the zero/even cross terms.

The archimedean integral is evaluated directly from the source master
formula by high-precision Gauss-Legendre quadrature.

## Cross-check grid

Retained evidence uses all six combinations

- dps in {50, 80};
- Gauss-Legendre degree in {96, 128, 160};

for both lambda^2 = 13 and lambda^2 = 14.

The reference configuration is 80 digits / degree 160.

The retained JSON includes:

- matrix symmetry residual;
- parity residual;
- epsilon_plus;
- epsilon_minus;
- finite gap g_N;
- maximum absolute spread over the cross-check grid.

The largest observed gap spread in the retained table is below 3.4e-50.

## Results

For lambda^2 = 13:

| N | g_N |
|---:|---:|
| 2 | 7.7058803379975316e-7 |
| 4 | 3.9294491208560441e-12 |
| 6 | 2.4519689077337548e-16 |
| 8 | 3.9071708276489838e-20 |
| 10 | 1.6420932405408130e-23 |
| 12 | 1.4567150714360194e-26 |

For lambda^2 = 14:

| N | g_N |
|---:|---:|
| 2 | 1.2733630950991919e-7 |
| 4 | 1.8690303100327589e-12 |
| 6 | 6.6581597991943487e-17 |
| 8 | 6.7251119441058066e-21 |
| 10 | 3.1984757602581183e-24 |
| 12 | 1.8448275535200157e-27 |

Every retained finite gap is positive and far larger than the observed
cross-check spread.

## Interpretation

The result is not a positive-tail certificate.

The finite gaps decrease extremely rapidly with N.  RH-R037 proves only
that they converge to the full gap.  A positive sequence may converge to
zero.

Therefore the evidence supports only:

    FINITE_PARITY_ORDER_POSITIVE_THROUGH_N12

at lambda^2 in {13,14} under the retained finite truncations.

It does not support:

    inf_N g_N > 0

or

    g(lambda) > 0.

The rapid collapse is itself a useful route diagnostic.  Any attempted
proof of a strict full parity gap must explain why the finite sequence
does not converge to zero.

## Independent normalization check

Before retaining the evidence, the implementation was checked against an
independent centered-cosine formulation:

- the point term agrees exactly after the diagonal (-1)^n basis change;
- the prime term agrees exactly after the same basis change;
- the independent Fourier archimedean integral agrees with -W_R to its
  numerical quadrature accuracy.

This resolved an earlier high-N prototype discrepancy as numerical
integration loss rather than a source-normalization mismatch.

The retained tranche is deliberately capped at N <= 12, where the two
precision levels and three quadrature degrees agree to the reported
spread.

## Reproduction

Install the pinned dependency:

    python -m pip install -r work_packages/RH_R039_QW_PARITY_GAP_EVIDENCE/requirements.txt

Run:

    python scripts/rh_r039_qw_parity_gap.py \
      --json-out rh_r039_evidence.json \
      --csv-out rh_r039_evidence.csv

Default parameters reproduce the retained lambda^2, N, precision, and
quadrature grid.

## Evidence files

- evidence.json
- evidence.csv
- ../../scripts/rh_r039_qw_parity_gap.py

## Claim boundary

R039 does not prove:

- a positive full parity gap;
- a nonzero Galerkin tail limit;
- even-sector simplicity;
- the CCM simple-even theorem;
- determinant convergence to Xi;
- RH;
- novelty or priority.

## Next target

The next useful mathematical target is not another unbounded finite-N
scan.

It is a tail-rate statement capable of distinguishing

    g_N -> g > 0

from

    g_N -> 0.

A source/theory audit should therefore look for quantitative Galerkin
error estimates for the parity-restricted Weil form, or structural
estimates on the even/odd Rayleigh minima strong enough to bound
|g_N-g|.

If such estimates are unavailable, the next computational tranche should
move to rigorously enclosed higher-N blocks with an explicit error model,
not ordinary floating-point eigensolvers.

## Terminal state

RH-R039_EXECUTED__FINITE_GAPS_POSITIVE_THROUGH_N12__NO_TAIL_CERTIFICATE
