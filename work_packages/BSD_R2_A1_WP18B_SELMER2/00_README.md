# BSD-R2-A1-WP18B — exact 2-Selmer measurement and full 2-primary collapse on the A/B controls

## Purpose

WP18B performs an independent finite Selmer computation on the protected WP18A controls and then applies only protected WP16A/WP05 inputs plus elementary finite-group algebra.

It does **not** use analytic Sha, the BSD leading-term formula, numerical stabilization, or an odd-prime theorem.

`BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED` remains unchanged.

## Protected inputs

- MATHSOLVE WP18A protected baseline: `6d44e401e584498992c78f053992bde1dcba2452`.
- MATHFORGE computation-interface admission: `35837626ec887737f26f0acc5d9de48c5fd4db83`.
- Protected WP05: rank one, finite Sha, odd rational torsion for the selected class.
- Protected WP16A: for every `n>=1`,

  `#Sel_{2^n}(E/Q) = 2^n #Sha(E/Q)[2^n]`

  and

  `s_n(E) = ord_2 #Sha(E/Q)[2^n]`.

- Protected WP16B: `T_E = Sha(E/Q)[2^infinity]^vee` and

  `Fitt^0_{Z_2}(T_E) = 2^{lim_n s_n(E)} Z_2`.

## Exact computational subject

Curves:

- regime A: `53a1 = [1,-1,1,0,0]`;
- regime B: `203b1 = [1,1,1,0,-2]`.

Exact computation head:

`c4a4fcc7339991becf7210f8978afb64e440ccdd`.

GitHub Actions run:

`34321076589`.

Job:

`102367621468`.

Runtime:

- SageMath `10.8`, release date `2025-12-18`;
- image `sagemath/sagemath@sha256:e2e4747b0e1ea8753a9cb5a399314a8b2c25fcefaf69ba85b22ee075829d09ea`;
- image ID `sha256:aeef59a8c17212357aeb83bd7f1cfac43bb1c789ae3fa2d887227c763bdfcac3`;
- Ubuntu runner `24.04.5`.

The admitted interface requires agreement between Sage/PARI and the mwrank/eclib route. The runner also invokes eclib directly.

## Raw 2-Selmer result

For `53a1`:

- `selmer_rank(algorithm="pari") = 1`;
- `selmer_rank(algorithm="mwrank") = 1`;
- direct eclib `selmer_rank() = 1`;
- therefore `#Sel_2(E/Q)=2`.

For `203b1`:

- `selmer_rank(algorithm="pari") = 1`;
- `selmer_rank(algorithm="mwrank") = 1`;
- direct eclib `selmer_rank() = 1`;
- therefore `#Sel_2(E/Q)=2`.

The three reported interfaces agree for both curves.

## Theorem — vanishing of the full 2-primary Sha on both controls

For each control curve,

`Sha(E/Q)[2^infinity] = 0`.

### Proof

Protected rank one and odd rational torsion give

`#(E(Q)/2E(Q)) = 2`.

The Kummer exact sequence at level `2` is

`0 -> E(Q)/2E(Q) -> Sel_2(E/Q) -> Sha(E/Q)[2] -> 0`.

The independent computation gives `#Sel_2(E/Q)=2`. Hence multiplicativity of cardinality gives

`#Sha(E/Q)[2] = 1`,

so

`Sha(E/Q)[2]=0`.

Protected WP05 gives finiteness of `Sha(E/Q)`. Let

`A := Sha(E/Q)[2^infinity]`.

If `A` were nonzero, choose an element of order `2^r` with `r>=1`; multiplying it by `2^{r-1}` would produce a nonzero element of order `2`, contradicting `A[2]=Sha(E/Q)[2]=0`.

Therefore `A=0`. QED.

## Corollary — the complete finite Selmer tower is determined

For each of `53a1` and `203b1`, and for every `n>=1`,

`Sha(E/Q)[2^n] = 0`,

`#Sel_{2^n}(E/Q) = 2^n`,

and

`s_n(E) = 0`.

Thus the stabilization index is exactly `n=1`, not merely observed numerically.

### Proof

The theorem gives `Sha(E/Q)[2^infinity]=0`, hence every finite `2^n`-torsion subgroup is zero. Protected WP16A then gives the stated Selmer orders and `s_n=0`. QED.

## Integral consequence

Protected WP16B now gives, for both control curves,

`T_E = 0`,

`len_Z2 T_E = 0`,

and

`Fitt^0_{Z_2}(T_E) = Z_2`.

Therefore the selected BSD equality for either control specializes to the still-unproved analytic statement

`delta_2(E) = 0`.

WP18B proves the arithmetic side of that specialized equality. It does not prove the analytic side.

## Regime comparison

The result holds for both protected WP13 regimes in this cohort:

- `53a1`: regime A, no even bad-prime Tamagawa factor, residual conductor `53`;
- `203b1`: regime B, `ord_2(c_7)=1`, residual conductor `29`.

Thus the regime-B Tamagawa/conductor-drop phenomenon does not force nontrivial `2`-primary Sha on the selected control. This is a two-curve diagnostic fact, not a uniform theorem.

## Next diagnostic tranche

The exact arithmetic side is now completely known for both controls. The next atlas question is the independently normalized analytic side:

`delta_2(E) = ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`.

A successor computation may test whether `delta_2(E)=0` under the fixed WP00 normalization, but it must use an independently audited analytic computation/normalization interface. Approximate legacy `rational factor` or analytic-Sha fields are not sufficient evidence for exact `ord_2`.

The uniform theorem/source frontier remains

`BSD-R2-A1-S3-K-INTEGRAL-FITTING-CONTROL`

with provider debt

`P2_GOOD_ORDINARY_IRREDUCIBLE_S3_EXACT_MU_OR_PRIMITIVE_FITTING_CONTROL`.

## Claim firewall

- `BSD-R2-A1` remains unproved.
- No analytic Sha value is used.
- No BSD leading-term identity is assumed.
- No numerical equality is promoted to proof.
- The full `2^n` tower conclusion follows from the exact level-2 computation plus protected finiteness, not from unperformed higher descents.
- The result is specific to the two WP18A controls and is not a uniform selected-class theorem.
- MATHCERT certification authority is not invoked.
