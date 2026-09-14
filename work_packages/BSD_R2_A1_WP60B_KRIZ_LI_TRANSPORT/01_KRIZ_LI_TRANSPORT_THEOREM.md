# WP60B theorem — exact Kriz–Li literal-`2` transport and ordinary local obstruction

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. In particular:

- `E` has good ordinary reduction at `2`;
- its Frobenius trace satisfies `a_2 in {+1,-1}`, so
  `#E(F_2)=3-a_2 in {2,4}`;
- protected WP12 gives a surjective residual representation
  `G_Q -> GL_2(F_2)`;
- protected WP38 identifies the free rank-one Mordell–Weil lattices over `Q` and each WP09 quadratic field `K`;
- protected WP56A fixes a primitive generator
  `P in E(Q)/E(Q)_tors`
  and writes
  `P_K(f)=m_K(f)P+T`,
  with `m_K(f) != 0` and `T in E(K)_tors`;
- protected WP58A fixes the source-compatible modular parametrization
  `f:X_0(N)->E`
  and the WP00 minimal Néron differential `omega_E` with
  `f^*omega_E = eps_f C_f phi(q)dq/q`,
  where `eps_f in {+1,-1}` and `C_f in Z_2^x`.

Protected MATHFORGE WP60B at

`grandchallenge/MATHFORGE@a8f72ed64755777870a300053e11659fb1dfff1b`

admits the exact Kriz–Li Assumption `(F)`. For the same parametrization `f`, let `omega_f^KL` satisfy

`f^*omega_f^KL=phi(q)dq/q`.

The source condition is

`2 splits in K`

and

`((3-a_2)/2) log_{omega_f^KL}(P_KL(f)) != 0 mod 2`.

The selected WP09 lane already requires `2` to split in `K`.

## 2. Differential and Heegner-point transport

### Lemma `BSD-A1-WP60B-DIFF-001`

For the fixed parametrization `f`,

`omega_f^KL=eps_f C_f^(-1) omega_E`.

Hence

`log_{omega_f^KL}(Q)
 = eps_f C_f^(-1) log_{omega_E}(Q)`

for every point in the common `2`-adic logarithm domain.

### Proof

Protected WP58A gives

`f^*omega_E=eps_f C_f phi(q)dq/q`,

while the admitted Kriz–Li normalization gives

`f^*omega_f^KL=phi(q)dq/q`.

Pullback by a nonconstant modular parametrization is injective on invariant differentials. The logarithm is linear in the differential. QED.

The Kriz–Li point attached to the same conductor-one parametrization is the same classical conductor-one trace point as protected `P_K(f)`, up to the source-allowed sign and torsion ambiguity. Since the `2`-adic logarithm has torsion-free additive target, it kills torsion. Therefore

`log_{omega_E}(P_KL(f))
 = +/- m_K(f) log_{omega_E}(P)`.

Define

`q_2:=#E(F_2)=3-a_2`

and

`kappa_2(E,P)
 := (q_2/2)log_{omega_E}(P)`.

Then the normalized Kriz–Li quantity satisfies the exact factorization

### Theorem `BSD-A1-WP60B-KL-TRANSPORT-001`

`KL_2(E,K,f)
 := (q_2/2)log_{omega_f^KL}(P_KL(f))
 = u_f m_K(f) kappa_2(E,P)`

with

`u_f=+/- C_f^(-1) in Z_2^x`.

QED.

## 3. Good ordinary reduction forces the shallow formal coefficient to be odd

Choose a minimal integral generalized Weierstrass equation at `2`

`y^2 + A_1 xy + A_3 y
 = x^3 + A_2 x^2 + A_4 x + A_6`.

Here `A_i` denote Weierstrass coefficients and must not be confused with the Frobenius trace `a_2`.

### Lemma `BSD-A1-WP60B-ORDINARY-A1-001`

`A_1` is odd.

### Proof

Assume instead that `A_1` is even. Reduce the equation modulo `2`, so the `xy` term vanishes.

For each `x in F_2`, the left side as a function of `y in F_2` is

`y^2 + bar A_3 y`.

If `bar A_3=0`, then `y^2=y`; for each right-hand side there is exactly one `y`. Thus there are exactly two affine `F_2`-points and the point at infinity, so `#E(F_2)=3`, which is odd.

If `bar A_3=1`, then `y^2+y=0` for both values of `y`; for each `x` the number of solutions is either `0` or `2`. Hence the total number of affine points is even, and adding the point at infinity again makes `#E(F_2)` odd.

Therefore `A_1` even implies `#E(F_2)` odd. But

`a_2=3-#E(F_2)`,

so the Frobenius trace would be even. This contradicts good ordinary reduction at `2`, for which `a_2` is not divisible by `2`. Hence `A_1` is odd. QED.

## 4. The ordinary formal logarithm gains an extra factor of `2`

Let `t=-x/y` be the standard formal parameter at the identity. The formal group attached to the generalized Weierstrass equation has

`F_E(X,Y)=X+Y-A_1XY+O((X,Y)^3)`.

Hence its invariant differential has expansion

`omega_E=g(t)dt`,

where

`g(t)=1+g_1 t+g_2 t^2+... in Z_2[[t]]`

and

`g_1 congruent A_1 mod 2`.

By Lemma `ORDINARY-A1-001`, `g_1` is odd.

The formal logarithm is

`log_{omega_E}(t)
 = t + (g_1/2)t^2
   + sum_{n>=3} g_{n-1} t^n/n`.

### Lemma `BSD-A1-WP60B-ORDINARY-LOG-001`

For every point `Q in E_1(Q_2)`,

`log_{omega_E}(Q) in 4Z_2`.

### Proof

For `Q in E_1(Q_2)`, its formal parameter lies in `2Z_2`. Write

`t(Q)=2s`, `s in Z_2`.

Divide the displayed formal logarithm by `2`:

`(1/2)log_{omega_E}(Q)
 = s + g_1 s^2
   + sum_{n>=3} g_{n-1} 2^(n-1) s^n/n`.

For `n>=3`,

`n-1-ord_2(n) >= 1`,

so every term in the final sum lies in `2Z_2`.

Modulo `2`, therefore,

`(1/2)log_{omega_E}(Q)
 congruent s+g_1 s^2
 congruent s+s^2
 congruent 0`.

Thus `(1/2)log_{omega_E}(Q) in 2Z_2`, equivalently

`log_{omega_E}(Q) in 4Z_2`.

QED.

This is a divisibility statement only. It does not assert that the logarithm is an isomorphism on the shallow subgroup `E_1(Q_2)`.

## 5. The Kriz–Li fixed local factor is always even on the selected lane

The reduction of the primitive rational generator `P` lies in the finite group `E(F_2)` of order `q_2`. Hence

`Q:=[q_2]P`

lies in `E_1(Q_2)`.

The logarithm is a group homomorphism, so

`log_{omega_E}(Q)=q_2 log_{omega_E}(P)`.

Therefore

`kappa_2(E,P)
 = (q_2/2)log_{omega_E}(P)
 = (1/2)log_{omega_E}(Q)`.

Apply Lemma `ORDINARY-LOG-001`.

### Theorem `BSD-A1-WP60B-KAPPA-EVEN-001`

For every curve in the protected selected class and every primitive generator `P`,

`kappa_2(E,P) in 2Z_2`.

In particular

`kappa_2(E,P) notin Z_2^x`.

This conclusion is independent of the auxiliary field `K` and of the sign of `P`.

## 6. Kriz–Li Assumption `(F)` is incompatible with the selected good-ordinary lane

Combine Theorem `KL-TRANSPORT-001` with Theorem `KAPPA-EVEN-001`.

### Theorem `BSD-A1-WP60B-F-OBSTRUCTION-001`

For every selected curve `E`, every WP09-compatible imaginary quadratic field `K`, and the protected source-compatible parametrization `f`,

`KL_2(E,K,f) in 2Z_2`.

Therefore the Kriz–Li nonvanishing condition

`KL_2(E,K,f) != 0 mod 2`

cannot hold.

Equivalently, Kriz–Li Assumption `(F)` is incompatible with the protected selected hypothesis of good ordinary reduction at `2`.

### Proof

In

`KL_2(E,K,f)=u_f m_K(f) kappa_2(E,P)`,

`u_f` is a `2`-adic unit, `m_K(f)` is an integer, and `kappa_2(E,P)` lies in `2Z_2`. Hence the product lies in `2Z_2`. QED.

Disposition:

`KRIZ_LI_F_LOCALLY_OBSTRUCTED_ON_SELECTED_GOOD_ORDINARY_LANE`.

This is a theorem about the current selected hypotheses, not a claim that Kriz–Li `(F)` is impossible for other reduction types. Indeed the source contains examples outside this ordinary local configuration.

## 7. Compatibility with the source indivisibility statement

Protected MATHFORGE records that, under Kriz–Li's stated local hypotheses, `(F)` implies that the Heegner point is indivisible by `2`.

Independently, protected WP12 gives image

`GL_2(F_2) ~= S_3`

on `E[2]`. The stabilizer of a nonzero `2`-torsion point has index three, so no such point can be defined over a quadratic field. Hence

### Lemma `BSD-A1-WP60B-K2TORS-001`

`E(K)[2]=0`

for every quadratic `K/Q` on the selected lane.

Thus `E(K)_tors` has odd order and multiplication by `2` is an automorphism on the torsion subgroup.

### Corollary `BSD-A1-WP60B-INDEX-PARITY-001`

`P_K(f)` is indivisible by `2` in `E(K)` if and only if `m_K(f)` is odd.

The source implication `(F) =>` Heegner `2`-indivisibility remains correct; Theorem `F-OBSTRUCTION-001` says only that its antecedent cannot occur in the selected good-ordinary branch.

## 8. Consequence for the WP59 reopening contract

Protected WP59 reopening form `R3` proposed a theorem forcing the Kriz–Li mod-`2` logarithmic condition for a WP09-compatible field.

WP60B proves that this reopening form is incompatible with the selected local hypotheses. No variation of the auxiliary field can change the obstruction, because it is already present in the fixed local scalar at `2`.

Record the exact disposition

`R3_RETIRED_FOR_SELECTED_GOOD_ORDINARY_LANE_BY_WP60B_LOCAL_OBSTRUCTION`.

This retires only WP59 reopening form `R3`. It does not resolve `R1`, `R2`, `R4`, or `R5`, and it does not resolve D2d.

The genuine Heegner-index parity problem remains

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`.

## 9. Implication for WP60C

The originally planned WP60C test of whether `kappa_2(E,P)` might be uniformly a unit is no longer a research question: WP60B proves it is uniformly nonunit on the selected branch.

A small exact real-data replay may be used as a regression check, but it cannot change the theorem state and is not required to decide `KL-LOCAL`.

WP60C should therefore be redirected, if used, toward discriminating the remaining genuine theorem lanes rather than sampling an already-settled local condition.

## 10. Remaining live boundaries

- `MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`;
- `MISSING_P2_KATO_ZETA_FITTING_DIVISIBILITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`;
- `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- `MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`;
- downstream `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## 11. Claim firewall

WP60B does not prove:

- `m_K(f)` is odd for any WP09 field;
- an exact value of `ord_2(m_K(f))` or `ord_2(lambda_D)`;
- WP59 `R1`, `R2`, `R4`, or `R5`;
- D2d;
- the WP60A height-one-`(2)` Fitting divisibility or determinant primitivity;
- fixed-`2` height nondegeneracy;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

The local impossibility statement is restricted to Kriz–Li `(F)` under the protected selected good-ordinary-at-`2` hypotheses. It is not a literature-exhaustiveness or general impossibility claim.
