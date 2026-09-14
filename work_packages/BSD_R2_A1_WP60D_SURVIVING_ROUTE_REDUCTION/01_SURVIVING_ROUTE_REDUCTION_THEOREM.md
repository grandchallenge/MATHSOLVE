# WP60D theorem — surviving-route reduction after the WP60B obstruction

## 1. Protected setup

Let `E/Q` lie in the protected selected `BSD-R2-A1` class. Retain protected WP57A, WP58A, WP59, WP60A-A1, and WP60B.

For any protected WP09-compatible imaginary quadratic field `K/Q` with fundamental discriminant `D=D_K<0`, protected WP57A/WP58A give

`L'(E,1)/(Omega_E Reg_E)
 = 2 m_K(f)^2 /(C_f^2 c_infinity(E^D) lambda_D)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`

and protected WP58A gives

`ord_2(C_f)=0`.

Protected WP59 defines

`R_2(E,K,f)
 := 2ord_2(m_K(f))-ord_2(lambda_D)`.

The purpose of WP60D is to determine whether the surviving WP59 form `R4`, a direct exact theorem for `R_2`, is genuinely auxiliary-field-dependent or an exact repackaging of a fixed base-curve invariant.

## 2. Real connected components are invariant under quadratic twist

Recall that for an elliptic curve over `R`,

`c_infinity(E):=#pi_0(E(R)) in {1,2}`.

### Lemma `BSD-A1-WP60D-CINF-TWIST-001`

For every nonzero real twist parameter `d`,

`c_infinity(E^d)=c_infinity(E)`.

In particular, for every protected negative fundamental discriminant `D`,

`c_infinity(E^D)=c_infinity(E)`.

### Proof

Over `R` put `E` in a short Weierstrass form

`y^2=x^3+Ax+B`.

A quadratic twist by `d in R^x` can be written

`E^d: y^2=x^3+d^2Ax+d^3B`.

Its discriminant is

`Delta(E^d)=d^6 Delta(E)`.

Since `d^6>0`, the discriminants of `E` and `E^d` have the same sign.

For a nonsingular real cubic, positive discriminant means three distinct real roots and hence two connected components of the real elliptic curve; negative discriminant means one real root and hence one connected component. Therefore the number of connected components is unchanged by twisting.

The statement is independent of the chosen real Weierstrass model because an admissible real change of variables multiplies the discriminant by a positive twelfth power. QED.

### Corollary `BSD-A1-WP60D-CINF-VAL-001`

`ord_2(c_infinity(E^D))=ord_2(c_infinity(E))`

for every WP09 field.

Thus the topological term appearing in WP57A is fixed by the base curve and carries no auxiliary-field variation.

## 3. Exact auxiliary-field invariance of the WP59 combined residual

Take `ord_2` in the protected WP57A identity and use protected WP58A:

`ord_2(L'(E,1)/(Omega_E Reg_E))
 = 1
   +2ord_2(m_K(f))
   -ord_2(c_infinity(E^D))
   -ord_2(lambda_D)`.

Rearrange and apply Corollary `CINF-VAL-001`.

### Theorem `BSD-A1-WP60D-R2-INVARIANT-001`

For every protected WP09-compatible auxiliary field `K`,

`R_2(E,K,f)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -1
   +ord_2(c_infinity(E))`.

Consequently `R_2(E,K,f)` is independent of `K`, despite the separate quantities `m_K(f)` and `lambda_D` being auxiliary-field-dependent.

In particular, for any two protected WP09-compatible fields `K_1,K_2`,

`2ord_2(m_{K_1}(f))-ord_2(lambda_{D_1})
 =2ord_2(m_{K_2}(f))-ord_2(lambda_{D_2})`.

QED.

## 4. Exact relation to the target defect

By definition

`delta_2(E)
 = ord_2(L'(E,1)/(Omega_E Reg_E))
   -sum_{ell|N}ord_2(c_ell)`.

Substitute this into Theorem `R2-INVARIANT-001`.

### Corollary `BSD-A1-WP60D-R2-DELTA-001`

Exactly,

`R_2(E,K,f)
 = delta_2(E)
   +sum_{ell|N}ord_2(c_ell)
   -1
   +ord_2(c_infinity(E))`.

Hence the selected BSD equality

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`

is equivalent to

`R_2(E,K,f)
 = v_2(Fitt^1_{Z_2}(X_E))
   +sum_{ell|N}ord_2(c_ell)
   -1
   +ord_2(c_infinity(E))`.

This equivalence is exact for every protected WP09-compatible field.

## 5. Disposition of WP59 reopening form R4

WP59 form `R4` asks for a direct exact theorem determining

`R_2(E,K,f)`.

Theorem `R2-INVARIANT-001` proves that `R4` is not an independent auxiliary-field mechanism. Its value is exactly the fixed base analytic leading-term valuation shifted by the explicit real-topology term.

Record the route classification

`R4_EQUIVALENT_TO_FIXED_BASE_ANALYTIC_LEADING_TERM_VALUATION`.

This is not a retirement of `R4`: a genuinely new theorem computing that fixed valuation could still close the residual. It means that varying `K`, or seeking cancellation between `m_K(f)` and `lambda_D` solely through auxiliary-field choice, cannot create new information about `R_2` beyond the base analytic quotient itself.

## 6. Consequences for the surviving route map

After protected WP60B retires `R3`, and WP60D classifies `R4`, the surviving paths have the following roles.

### R1 — Heegner-index control

`MISSING_LITERAL_P2_HEEGNER_INDEX_PARITY`

or stronger exact valuation control remains genuine field-dependent arithmetic information. By itself it does not determine `R_2` unless paired with exact twist-value information.

### R2 — twist-L-ratio control

Exact `ord_2(lambda_D)` under all WP09 constraints remains a genuine field-dependent arithmetic input. By itself it does not determine `R_2` unless paired with Heegner-index information.

### R4 — combined residual

Not field-dependent after all. It is exactly the fixed base leading-term valuation above.

### R5 — height-one-`(2)` reciprocity/Fitting control

WP60A-A1 has already reduced this route to the missing one-sided Kato/Fitting divisibility and determinant primitivity at `(2)`.

### D2a — fixed-`2` height nondegeneracy

Remains a separate literal-`2` theorem boundary. A new nondegeneracy theorem could still unlock a p-adic Gross–Zagier route, but no such theorem is proved here.

## 7. Research consequence

A search for an `R4` theorem should no longer be framed as a search for a special auxiliary field or a miraculous cancellation between the two WP59 residual terms. The exact combined quantity cannot vary with `K`.

The genuinely new arithmetic information must therefore enter through one of:

1. separate control of `m_K(f)` and `lambda_D` strong enough to evaluate their fixed combination;
2. a direct theorem for the base analytic leading-term valuation;
3. height-one-`(2)` determinant/Fitting reciprocity;
4. a fixed-`2` height theorem that, together with the already-protected p-adic Gross–Zagier normalization, yields one of the preceding exact quantities.

## 8. Claim firewall

WP60D does not prove:

- any value of `ord_2(m_K(f))`;
- any value of `ord_2(lambda_D)`;
- the fixed value of `R_2(E,K,f)`;
- the selected BSD equality;
- WP59 `R1`, `R2`, `R4`, or `R5` closure;
- D2a;
- the WP60A height-one-`(2)` divisibility/primitivity boundaries;
- D2d;
- D2e;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.

The theorem proves only the exact auxiliary-field invariance and route equivalence stated above.
