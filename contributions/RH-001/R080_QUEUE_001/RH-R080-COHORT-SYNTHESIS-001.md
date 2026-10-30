# RH-R080 blind cohort — bounded protected synthesis

Record: RH-R080-COHORT-SYNTHESIS-001  
Status: MATHEMATICAL_ADJUDICATION_CANDIDATE; NO_CERTIFICATION  
Exact predecessor: MATHSOLVE/main `c6e04ae07aca6fedaf7565674c1b3ceab7f54f3c`  
Cohort: `RH-R080-BLIND-COHORT-001`

## Evidence and custody

| Assignment | Return issue and locked comment | Protected intake | Bounded disposition |
| --- | --- | --- | --- |
| WP-A, positivity mechanism | #1003, comment 6059225450 | PR #1026, merge `b3d3c0173402ed9d386b2efa8a18f66942dd71b1` | Free-parameter finite sign-changing countermodel credible; cannot infer actual CCM arithmetic realization or universal exclusion of positivity mechanisms |
| WP-B, positivity falsification | #1004, comment 6076596820 | PR #1027, merge `4305d7370abcb065c9d9edc29c6258a9a461fd69` | Conditional N=1 positivity criterion accepted; numerical scan and asymptotic impossibility unverified |
| WP-C, signed normality | #1005, comment 6071609203 | PR #1028, merge `1733d4e8f35e97ff6439f2e3866700bd5207e7ef` | Kernel/variation/Montel estimates accepted conditionally; claimed boundary-anchor noncollapse is false |

All three captures are evidence, not theorem-level certification. Their receipts explicitly say `received_unadjudicated`. The synthesis threshold in `handoffs/RH-001/r080/README.md` is satisfied by WP-A/B and WP-C. This document does not assert that a separate controller has already declared the blind cohort closed.

## Verifier — valid mathematical intersection

For a real even function $f\in L^1([-a,a])$ with $a>0$ and nonzero normalization

$$
A(f)=\int_0^a f(x)\cosh(x/2)\,dx,
$$

define the finite signed measure and kernel by

$$
d\mu_f(x)=\frac{f(x)\cosh(x/2)}{A(f)}\,dx,
\qquad K_z(x)=\frac{\cos(zx)}{\cosh(x/2)},
$$

and, for $\delta\geq 0$, the signed-projective variation

$$
\kappa_\delta(f)=
\frac{\int_0^a |f(x)|\cosh(\delta x)\,dx}{|A(f)|}.
$$

Direct integration and $|\cos(zx)|\leq\cosh(|\operatorname{Im}z|x)$ give

$$
F_f(z)=\frac12\int_0^a K_z(x)\,d\mu_f(x),
\qquad
\sup_{|\operatorname{Im}z|\leq\delta}|F_f(z)|
\leq\frac12\kappa_\delta(f).
$$

For each fixed $0\leq\delta<1/2$, a uniform bound on $\kappa_\delta$ along an actual admissible family is sufficient for local boundedness and hence Montel normality on $U=\{z:|\operatorname{Im}z|<1/2\}$. Actual-family bounds are not supplied by the cohort. The integral representation presumes the same normalization of $F_f$ as in the protected RH work packages.

The $N=1$ WP-B identity, conditional on $w_1<0$ and normalization $w_0-\sqrt{2}\,w_1=1$, gives

$$
\min_{x\in[0,a]}\xi(x)=\frac{2w_0-1}{\sqrt{2a}}.
$$

Thus strict positivity is equivalent to $w_0>1/2$, with a zero at equality. The reported CCM numerical values require independent source-pinned replay.

## Adversary — rejected promotions

1. WP-A supplies a free-parameter structured matrix exhibiting a simple even ground eigenfunction with a sign change. It does not produce a parameter-locked actual CCM instance. Nonpositivity of Fourier projection alone does not imply every compressed positive operator fails positivity. Reflection symmetry alone does not preclude total positivity.
2. WP-B's small positive minima at finitely many points do not prove that no uniform lower bound exists along a cofinal family. The published examples also do not reproduce all claimed $N=3,4$ scan records or certify numerical error.
3. WP-C attempts to infer nonzero interior limits from $F_j(i/2)=1/2$. This is invalid because $i/2\notin U$. Protected `work_packages/RH_R077_PROJECTIVE_MEASURE_REPAIR.md` already supplies the exact counterexample

$$
E_n(z)=\frac{\cos(nz)}{2\cosh(n/2)}\longrightarrow 0
$$

on compact subsets of $U$, while retaining $E_n(i/2)=1/2$. The frozen WP-C task itself explicitly warned against boundary-anchor anti-collapse.

The acceptance of conditional normality cannot be upgraded to an RH theorem, actual-family C4/C5 discharge, certified CCM ground-state positivity or publication.

## Remaining smallest actual-family obligations

- Establish uniform signed-projective $\kappa_\delta$ control along a provably admissible cofinal CCM sequence (C4).
- Establish a nonzero *interior* subsequential observable and projective shape identification, as required by protected RH-R077 Theorem 7.1 (C5).
- Independently reconstruct any numerical positivity/negativity claim from the locked source matrix and certified error bounds. A free-parameter model does not substitute for this.

## Governance

This is a synthesis evidence candidate only, derived from authenticated preserved raw returns and protected mathematical predecessors. Keep each immutable worker comment/receipt unchanged. Do not close #1003–#1005, change dispatch lease or Project statuses, or declare a cohort terminal state solely from this document. A protected lifecycle reconciler must verify actual exact-head registry/lease mutations and record the corresponding terminal readback. Specialist mathematical certification is not issued here.
