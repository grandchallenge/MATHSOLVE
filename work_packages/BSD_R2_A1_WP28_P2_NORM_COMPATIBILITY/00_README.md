# BSD-R2-A1-WP28 — concrete good-ordinary norm coordinates at `2`

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP27-P2-CONTROL-FILTRATION`.
- Protected MATHSOLVE baseline: `8628ad1d612b45e5254dcf5fa7165b986c371000`.
- Protected MATHFORGE source authority: `e5c49ee60ba300cff8026ddf65059c3049ab1226`.
- Admitted source audit: `sources/BSD-001/TAN_GOOD_ORDINARY_NORM_FILTRATION_WP28_SOURCE_AUDIT.md`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: exact place-`2` reduction/formal universal-norm representation theorem.

## Protected input

Protected WP25 gives the canonical local universal-norm quotient

`U_2 = E(Q_2)/N_2^infinity ~= K_2^vee`.

Protected WP27 gives an abstract two-step filtration of `U_2` and proves that the order depth of the saturated generator is the sum of its two extension-coordinate depths. WP27 intentionally does not identify either coordinate with literal reduction or with a formal universal-norm class.

MATHFORGE now protects Tan's stronger literal-`p=2`, totally ramified, good-ordinary source interface. It supplies an independent exact universal-norm sequence induced by the reduction/formal-group sequence and proves that the formal universal-norm quotient injects into the full quotient.

## WP28 result

Let

`L=Q_{infty,2}`

be the completion of the cyclotomic `Z_2`-extension at `2`, and let `L_n/Q_2` be its finite layers.

Define

`N_2^form := intersection_n N_{L_n/Q_2} Ehat(m_{L_n})`

inside the formal subgroup `Ehat(2 Z_2)`, and put

`F_2^norm := Ehat(2 Z_2)/N_2^form`.

Tan's protected source gives the exact sequence

`0 -> F_2^norm
   -> U_2
   -> E_tilde(F_2)
   -> 0`.

The last map is induced by literal reduction of local points.

The reduction quotient is exactly `E_tilde(F_2)` because the local cyclotomic tower is totally ramified, so the residue field stays `F_2`, and the finite-layer norm acts on the finite reduction group as multiplication by `2^n`. Protected WP07 gives

`#E_tilde(F_2)=3-a_2 in {2,4}`,

so the intersection of those norm images is zero.

Since protected WP23/WP25 give

`#U_2=(3-a_2)^2`,

exactness also gives

`#F_2^norm=3-a_2`.

For a saturated global rank-one generator `P`, let

`red_2(P) in E_tilde(F_2)`

be its literal reduction and define

`r_red(P):=ord_2(ord(red_2(P)))`.

Put

`x_2(P):=[P]_2 in U_2`.

Then

`2^{r_red(P)} x_2(P)`

lies in the image of `F_2^norm`. Let

`z_form(P) in F_2^norm`

be its unique preimage under the injective formal-norm map, and define

`s_form(P):=ord_2(ord(z_form(P)))`.

WP28 proves

`rho_2(P)=r_red(P)+s_form(P)`.

Hence, with protected WP26's explicit odd-prime quantity

`rho_bad(P)=max_{ell|N} ord_2(ord(comp_ell(P)))`,

one has

`rho_E=max(r_red(P)+s_form(P),rho_bad(P))`.

## Refined boundary

The former abstract position boundary

`MISSING_P2_SATURATED_GENERATOR_POSITION_IN_GOOD_ORDINARY_CONTROL_EXTENSION`

is replaced by

`MISSING_P2_FORMAL_UNIVERSAL_NORM_ORDER_OF_REDUCTION_KILLED_GENERATOR`.

The finite reduction coordinate is now literal arithmetic data. The only unresolved local structural datum in D1b is the order of the reduction-killed generator class in the formal universal-norm quotient.

Tan also gives an abstract ambient identification of the formal norm quotient in terms of a Frobenius twist scalar `u`, but WP28 does not identify `u` with the protected unit root `alpha` or `alpha^(-1)` and does not derive an element-level logarithmic formula.

## Claim firewall

WP28 does not prove:

- a value of `s_form(P)` or `rho_2(P)`;
- that the exact sequence splits;
- a canonical identification of the new concrete coordinates with WP27's named abstract coordinates `r_2(P),s_2(P)`;
- an element-level formal logarithm formula for `z_form(P)`;
- an identification of Tan's twist scalar with `alpha` or `alpha^(-1)`;
- equality with a regulator, height, Bockstein, Euler factor, or analytic term;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
