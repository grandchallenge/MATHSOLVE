# BSD-001 frontier after WP29

## Candidate identity

Work package:

`BSD-R2-A1-WP29-P2-TOROIDAL-FORMAL-NORM-COORDINATE`.

Protected baseline used to author this package:

`grandchallenge/MATHSOLVE@3bae7e80d148adb297fc3746e4f1eb0466148354`.

Protected source authority:

`grandchallenge/MATHFORGE@2021db4f98da3d0df7cea2a37c9d9f6d4e9a4576`.

Programme owner:

`grandchallenge/MATHSOLVE#164`.

## Exact result

WP29 represents the protected WP28 formal universal-norm class by a Hall/Lubin-Rosen toroidal Galois coordinate

`theta_form(P) in Gamma_2/(1-u)Gamma_2`

and proves

`ord(theta_form(P))=ord(z_form(P))`.

Put

`m_2=ord_2(3-a_2)`.

Since protected WP28 gives `#F_2^norm=3-a_2` and the protected WP29 source gives

`F_2^norm ~= Gamma_2/(1-u)Gamma_2`,

WP29 proves internally

`ord_2(1-u)=m_2`.

After choosing any topological generator of `Gamma_2`, write the toroidal class as a scalar modulo `(1-u)` and define its canonical truncated valuation

`tau_form(P)=min(m_2,ord_2(t_form(P)))`.

This invariant is independent of scalar lift, topological generator, and source-compatible toroidal coordinate.

The exact remaining formal order is

`s_form(P)=m_2-tau_form(P)`.

Therefore

`rho_2(P)
 = r_red(P)+m_2-tau_form(P)`

and

`rho_E
 = max(
     r_red(P)+m_2-tau_form(P),
     rho_bad(P)
   )`.

The protected control-defect length becomes

`len_Z2(C_E^vee)
 = 2m_2
   + sum_{ell|N} ord_2(c_ell)
   - max(
       r_red(P)+m_2-tau_form(P),
       rho_bad(P)
     )`.

## Finite residual uncertainty

The selected good-ordinary branch has only two cases.

If `a_2=+1`, then `m_2=1` and

`tau_form(P) in {0,1}`.

If `a_2=-1`, then `m_2=2` and

`tau_form(P) in {0,1,2}`.

Thus the remaining D1b place-2 uncertainty is finite and has at most three states.

## Active D1b boundary

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`.

A successor must evaluate `tau_form(P)` uniformly in the selected branch or prove an exact protected comparison that determines it.

## Candidate successor directions

The following directions are admissible reconnaissance targets but are not established facts:

1. source an exact comparison between the toroidal twist/module coordinate and the protected ordinary unit-root normalization;
2. source or derive an element-level formal-logarithm description of the Hall/Lubin-Rosen coordinate at `p=2`;
3. compare the resulting finite congruence depth with the protected WP20 Bockstein/regulator object while preserving exact normalization;
4. if none of these closes the element depth, record a bounded barrier rather than replacing the missing comparison by a unit ambiguity.

## Other protected boundaries unchanged

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`.
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.
- `BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.
- No MATHCERT certification is authorized.

## Claim firewall

Do not promote equality of valuations to equality of local factors. In particular, WP29 does not identify `u` with `alpha` or `alpha^(-1)`, does not make the toroidal scalar canonical, and does not identify `tau_form(P)` with a regulator, height, formal logarithm, or Bockstein valuation.
