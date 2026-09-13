# BSD-001 frontier after WP53A

## Protected predecessors

- MATHSOLVE WP52A protected head: `3aae8375de252a782eaf82e0bb393814e033f857`.
- MATHFORGE WP53 protected head: `c1aaf027df8e03fd79783cfc8ed14c9d58632a50`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.

## WP53A result

For every selected odd bad semistable prime `ell|N`, the protected auxiliary field is split at `ell`, the toric character is trivial, and the local representation is a conductor-one unramified twist of Steinberg.

In the exact Cai–Shu–Tian local measure admitted by MATHFORGE WP53,

`Q_{ell,dt_ell^CST}=1+ell^(-1)`

and therefore

`ord_2 Q_{ell,dt_ell^CST}=ord_2(ell+1)`.

Hence

`Q_bad^CST
 = product_{ell|N, ell odd}(1+ell^(-1))`

and

`ord_2 Q_bad^CST
 = sum_{ell|N, ell odd} ord_2(ell+1)`.

For Disegni's actual local component

`dt_ell=s_ell dt_ell^CST`,

one has exactly

`Q_{ell,dt_ell}=s_ell(1+ell^(-1))`.

Thus with `s_bad=product s_ell`,

`Q_bad=s_bad Q_bad^CST`.

No unit claim is made about `s_bad`.

## D2c disposition

The former local boundary

`MISSING_P2_DISEGNI_SPLIT_BAD_PRIME_NEWVECTOR_QORD_FACTORS`

is resolved:

`RESOLVED_WP53A_SPLIT_BAD_PRIME_NEWVECTOR_FACTOR`.

The surviving D2c boundary is

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`.

## Live campaign boundaries

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`.
- D2c: `MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`.
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`.
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## Immediate successor WP54A — global `Q^ord` measure/vector ledger

Fix one source-compatible decomposition of Disegni's volume-one adelic torus measure and compute the complete remaining factor in Lemma 4.3.3 / (4.3.4):

1. local scaling factors comparing the chosen `dt_v` with the already-computed canonical local measures;
2. every nonbad finite place retained in `Sigma` or `Sigma'`;
3. the away-from-`S p infinity` vector ratio;
4. the archimedean factor and any scalar used to impose global quotient volume one;
5. the exact resulting `2`-adic valuation.

The desired output is one exact factorization

`Q^ord = Q_2^ord * Q_bad^CST * Q_rem`

with protected `Q_2^ord=1`, explicit `Q_bad^CST`, and a fully evaluated or explicitly bounded `Q_rem`.

Do not move a measure scalar between places and then declare it absent.

## Parallel successor WP54B — narrow D1c screen

Continue only the literal-`p=2`, height-one-`(2)` analytic determinant search. Do not reopen odd-prime or inverted-`2` results already rejected by protected source audits.

## Firewall

Do not promote:

- `s_ell` or `s_bad` to a `2`-adic unit without proof;
- `Q_bad^CST` to the complete `Q^ord`;
- coincidence of local prime labels to cancellation with WP34 Tamagawa/Euler terms;
- height existence to nondegeneracy;
- any analytic determinant result not literal at `(2)`;
- BSD or MATHCERT certification.
