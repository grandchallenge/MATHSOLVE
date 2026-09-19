# BSD-001 R5-WIT frontier — finite normalized witness and direct residual bypass

## Operation

- Operation: `BSD-R5-WIT`.
- Issue: `grandchallenge/MATHSOLVE#282`.
- Protected entering MATHSOLVE base: `8e692aaca7b0932c412a03eb33985ba5994b1d5f`.
- Protected provider: `grandchallenge/MATHFORGE@3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.
- Parent tracker: `grandchallenge/MATHSOLVE#215`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## Entering frontier

`MISSING_P2_NORMALIZED_FINITE_KURIHARA_NONVANISHING_WITNESS`.

Protected R5-RECIP already proves the normalized literal-`2` finite identity

`xi_n(exp^*(loc^s_2(kappa_n^Kato))) = u_n Delta_n^(2)`

with

`Delta_n^(2)=2^t_2 delta_tilde_n`.

Protected R5-PRIM separately proves that a single legitimate nonzero finite cyclotomic residual Kato/Kolyvagin image suffices for the height-one `(2)` residual nonvanishing reduction.

## Exact local stratification proved by R5-WIT

The operation proves:

- `t_2(53a1)=1`;
- `t_2(203b1)=1`;
- `t_2(79a1)=2`;
- `t_2(61a1)=1`;
- `t_2(83a1)=1`;
- `t_2(201b1)=2`;
- `t_2(89a1)=3`.

Consequently the normalized Kurihara coordinate is structurally unavailable modulo two on `79a1`, `201b1`, and `89a1`: protected R5-RECIP forces `Delta_n^(2)=0 mod 2` at every admitted derivative level whenever `t_2>=2`.

This is not a residual Kato-class vanishing theorem.

## Exact finite reconnaissance on the t_2=1 lane

The admitted PARI/GP 2.15.4 interface was replayed exactly.

For `53a1` and `203b1`, every single-prime normalized witness through `ell<=2000` is zero modulo two; the explicitly tested three-prime indices are also zero.

For the effective deterministic cohort through `ell<=500`, the exact aggregate result is

`DISCOVERY_HITS []`.

In particular the `t_2=1` candidates `53a1`, `61a1`, `83a1`, and `203b1` yielded no bounded single-prime hit.

These are finite negative results only. They do not prove global nonexistence of a normalized witness on a `t_2=1` curve.

## Direct finite residual bypass

Protected WP60T gives, for every admitted rank-one Euler system `c` and every coefficient level `m`,

`kappa_m(c)_1 = c_Q mod 2^m`.

For the integral Kato Euler system at `m=1`,

`kappa_1^Kato{}_1 = c_Q^Kato mod 2`.

Therefore

`c_Q^Kato mod 2 != 0`

is itself a legitimate finite residual witness and, by protected R5-PRIM finite detection, bypasses the normalized Kurihara/local-dual-exponential coordinate completely.

This bypass remains meaningful on the `t_2>=2` sublane.

## Protected source audit

MATHFORGE protects the bounded direct-detector source audit at

`grandchallenge/MATHFORGE@3a097cf5f1ad5e12eeba83a08dccfbf7bc49b5f4`.

It retains:

- integral literal-`2` Kato Euler-system classes;
- literal-`2` cyclotomic Kato explicit reciprocity;
- the distinction between characteristic-zero nonvanishing and integral mod-`2` indivisibility.

The specifically screened rank-one Beilinson-Kato/Heegner comparison results impose odd-prime hypotheses or otherwise do not provide an integral unit comparison at literal `2`. No protected theorem or exact legitimate computation currently proves

`c_Q^Kato mod 2 != 0`

on the selected rank-one anomalous ordinary lane.

## Candidate disposition

`BLOCKED`.

Exact current substantive evidentiary/theorem boundary:

`MISSING_P2_BASE_KATO_CLASS_MOD2_NONVANISHING_ON_SELECTED_RANK_ONE_LANE`.

This names the current direct bypass. It is not a claim that every other finite residual detector has been excluded.

Reopen R5-WIT on any exact protected evidence that either:

1. proves `c_Q^Kato mod 2 != 0` on a selected instance;
2. supplies another legitimate finite Kato/Kolyvagin component nonzero modulo two;
3. supplies a nonzero normalized Kurihara witness on a certified `t_2=1` instance.

## Claim firewall

Do not infer or promote:

- `R5_RES_ESTABLISHED`;
- `R5_PRIM_ESTABLISHED`;
- D2d;
- `BSD-R2-A1`;
- novelty or priority;
- public certification;
- MATHCERT certification.
