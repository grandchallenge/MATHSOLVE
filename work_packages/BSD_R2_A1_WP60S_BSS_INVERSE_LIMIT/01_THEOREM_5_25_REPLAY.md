# WP60S theorem — selected literal-2 replay of BSS II Theorem 5.25

## 1. Protected setup

Let

`T := T_2(E)`, `R := Z_2`, `A_m := T/2^m T`, `R_m := Z/2^m`.

Fix a selected `BSD-R2-A1` curve and the exact canonical BSS Selmer structure.

Protected WP60R proves for every `m>=1` the selected finite-level conclusions of BSS II Theorem 5.2. In particular there are finite Stark- and Kolyvagin-system modules

`SS_m := SS^r(A_m,Fcan)`,

`KS_m := KS^r(A_m,Fcan)`

and a regulator isomorphism

`Reg_m : SS_m -> KS_m`.

Each is free of rank one over `R_m`. The finite Kolyvagin ideals satisfy the protected Theorem-5.2 Fitting inclusions/equalities.

Protected MATHFORGE WP60S at

`grandchallenge/MATHFORGE@770f95d1f8e7cfdd3facbd9242bf3c21c0e8b074`

admits the exact source-dependency replacements needed for the inverse-limit passage while preserving failure of full BSS Hypothesis 4.7(iii).

## 2. Compatible auxiliary-prime systems

The source useful-prime sets may be chosen with

`P_(m+1) subset P_m`.

On the selected lane this follows from reduction of the exact Frobenius conjugacy condition modulo `2^(m+1)` to the corresponding condition modulo `2^m`. It is independent of the false auxiliary-field cohomology vanishing.

Hence the square-free auxiliary-ideal sets satisfy

`N_(m+1) subset N_m`.

Protected provider WP60S also gives core-vertex persistence: a core vertex at level `m+1` remains core after coefficient reduction to level `m`.

Record

`BSD-A1-WP60S-NESTED-AUXILIARY-001`.

## 3. Stark transition system

Protected provider WP60S replays the source construction of Lemma 4.10 using the selected WP60M/WP60R coefficient-reduction interface rather than full Hypothesis 4.7(iii).

Thus for every `m>=1` there is a canonical surjective reduction

`s_(m+1,m) : SS_(m+1) -> SS_m`

compatible with the coefficient reduction `R_(m+1)->R_m`.

The source construction is functorial in successive quotient maps. Therefore

`s_(m+2,m) = s_(m+1,m) o s_(m+2,m+1)`.

The finite Stark ideals reduce compatibly under these maps.

Define

`SS_infty := lim_m SS_m`.

By the protected provider inverse-limit Stark theorem, `SS_infty` is free of rank one over `Z_2`.

Record

`BSD-A1-WP60S-STARK-LIMIT-002`.

## 4. Kolyvagin transition system

Define

`k_(m+1,m)
 := Reg_m o s_(m+1,m) o Reg_(m+1)^(-1)
 : KS_(m+1) -> KS_m`.

### Lemma `BSD-A1-WP60S-KS-TRANSITION-003`

The maps `k_(m+1,m)` are the unique reductions that make the regulator squares commute, and they form an inverse system.

### Proof

Because `Reg_m` and `Reg_(m+1)` are isomorphisms, there is exactly one map from `KS_(m+1)` to `KS_m` satisfying

`k_(m+1,m) o Reg_(m+1)
 = Reg_m o s_(m+1,m)`.

The displayed conjugation is that unique map.

For three consecutive levels, functoriality of the Stark reductions gives

`s_(m+2,m)=s_(m+1,m)o s_(m+2,m+1)`.

Conjugating by the regulator isomorphisms gives

`k_(m+2,m)=k_(m+1,m)o k_(m+2,m+1)`.

Thus the `KS_m` form an inverse system. QED.

Define

`KS_infty := lim_m KS_m`.

The componentwise finite regulator maps induce

`Reg_infty : SS_infty -> KS_infty`.

### Theorem `BSD-A1-WP60S-INTEGRAL-REGULATOR-004`

`Reg_infty` is an isomorphism. Consequently `KS_infty` is free of rank one over `Z_2`.

### Proof

A family `(epsilon_m)_m` is compatible under the Stark transitions if and only if `(Reg_m(epsilon_m))_m` is compatible under the Kolyvagin transitions, by the defining commuting squares. The inverse family is obtained componentwise using `Reg_m^(-1)`. Hence `Reg_infty` is an isomorphism.

Protected provider WP60S gives `SS_infty ~= Z_2`. Therefore `KS_infty ~= Z_2`. QED.

Record

`BSS_LITERAL_P2_SELECTED_INTEGRAL_REGULATOR_ISOMORPHISM`.

## 5. Compatible Kolyvagin ideals

Let

`kappa=(kappa^(m))_m in KS_infty`.

For every `i>=0`, finite WP60R defines the ideal

`I_i(kappa^(m)) subset R_m`

and finite Theorem 5.2 gives

`I_i(kappa^(m))
 subset Fitt^i_(R_m)(X_m)`,

where `X_m` is the corresponding finite-level dual Selmer module, with equality for a basis Kolyvagin system in the source's principal-ring cases.

Protected provider WP60S supplies the source Corollary-3.8 coefficient compatibility and the compatibility of these ideals under reduction:

`I_i(kappa^(m+1)) R_m = I_i(kappa^(m))`.

Hence define the integral ideal

`I_i(kappa) := lim_m I_i(kappa^(m)) subset Z_2`.

Record

`BSD-A1-WP60S-KOLYVAGIN-IDEALS-005`.

## 6. Integral Fitting passage

Let `X` denote the selected integral dual Selmer module occurring in the BSS Theorem-5.25 interface. Cartesian coefficient reduction identifies its finite quotients with the `X_m` used above.

Protected provider WP60S admits the inverse-limit Fitting identity

`Fitt^i_(Z_2)(X)
 = lim_m Fitt^i_(R_m)(X_m)`.

The source proof uses the finite Fitting identities, coefficient compatibility, and completeness of the noetherian coefficient ring; all are available here because `Z_2` is complete, noetherian, local, Gorenstein, and principal.

Taking inverse limits in the finite WP60R inclusions gives

`I_i(kappa)
 subset Fitt^i_(Z_2)(X)`

for every `i>=0`.

If `kappa` is a basis of the free rank-one module `KS_infty`, then every reduction `kappa^(m)` is a basis of `KS_m`. Finite WP60R therefore gives equality at every level. Passing to the inverse limit gives

`I_i(kappa)
 = Fitt^i_(Z_2)(X)`

for every `i>=0`.

In particular the `i=0` statement reproduces the source Theorem-5.25 zeroth-Fitting assertion, and principality of `Z_2` supplies the higher-Fitting equality clause.

Record

`BSD-A1-WP60S-INTEGRAL-FITTING-006`.

## 7. Selected literal-2 Theorem 5.25

### Theorem `BSD-A1-WP60S-BSS-525-007`

For the exact selected canonical literal-`2` lane, the conclusions of BSS II Theorem 5.25 hold after replacing the source's use of full Hypothesis 4.7(iii) by the protected WP60M/WP60R selected coefficient-reduction interfaces and protected MATHFORGE WP60S cross-level interfaces:

1. the integral regulator
   `Reg_infty : SS_infty -> KS_infty`
   is an isomorphism;
2. `KS_infty` is free of rank one over `Z_2`;
3. for every `kappa in KS_infty`, the Kolyvagin ideals lie in the corresponding integral Fitting ideals;
4. if `kappa` is a basis, these containments are equalities for all higher Fitting ideals.

Record

`BSS_LITERAL_P2_SELECTED_THEOREM_5_25_REPLAYED`.

### Proof

Claims (1) and (2) are Theorem `INTEGRAL-REGULATOR-004`. Claims (3) and (4) are §6. These are exactly the three source conclusions, whose published proof reduces them to the corresponding finite Theorem-5.2 conclusions once the inverse systems and coefficient compatibilities are available. QED.

## 8. What is not repaired

The proof does not assert

`H^1(Q(T)_(2^infinity)/Q,E[2])=0`

or its dual analogue. Full BSS Hypothesis 4.7(iii) and the protected infinite H3 condition remain unavailable. The theorem works because the source use of that standing hypothesis in the inverse-limit construction is replaced on the selected lane by the narrower WP60M/WP60R modified-Selmer coefficient-reduction result.

Formal higher-level BSS Hypothesis 3.2(iii) likewise remains false.

## 9. Next boundary

The next source/application chain is BSS II Theorem 6.12 and Corollary 6.15. Protected source evidence does not yet authorize their literal-`2` application: the published derivative/application framework has separate standing hypotheses, and the standard infinite H3 route remains false.

Record

`MISSING_LITERAL_P2_BSS_THEOREM_6_12_COROLLARY_6_15_APPLICATION_REPLAY_WITHOUT_INFINITE_H3`.

## 10. Claim firewall

WP60S does not establish:

- full BSS Hypothesis 4.7 or clause (iii);
- the protected infinite H3 condition;
- formal higher-level Hypothesis 3.2(iii);
- BSS Theorem 6.12 or Corollary 6.15 at literal `2`;
- height-one `(2)` Kato/Fitting divisibility;
- determinant primitivity at `(2)`;
- R5-LIFT, R5-PRIM, D2d, or `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
