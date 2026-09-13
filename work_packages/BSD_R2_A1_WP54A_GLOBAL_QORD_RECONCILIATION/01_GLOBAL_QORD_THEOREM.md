# WP54A theorem — exact global Disegni ordinary factor

## 1. Protected setup

Retain protected WP09, WP41B, WP42B, WP53A, and protected MATHFORGE WP54.

Let `K/Q` be the protected WP09 imaginary quadratic field. Write

- `D_K` for its fundamental discriminant;
- `h_K := #Cl(K)`;
- `u_K := [O_K^x:{+1,-1}]`.

The protected packet gives:

- `(D_K,2N)=1`;
- `2` splits in `K`;
- every `ell|N` splits in `K`;
- `chi=1`;
- the selected curve has good ordinary reduction at `2`;
- the selected curve is semistable, so every `ell|N` is an odd multiplicative prime.

Protected MATHFORGE WP54 additionally gives:

1. the finite ramification set of Disegni's locally distinguished quaternion datum is empty, `Sigma=emptyset`;
2. the CST quotient measure may be used at every finite place;
3. at every good auxiliary finite place `ell not|2N`, the source-normalized factor equals the compact quotient volume `m_ell`, with `m_ell=1` away from `D_K` and `m_ell=|D_ell|^(1/2)` at `ell|D_K`;
4. at `2`, with the CST local measure, `Q^ord_2=2`;
5. at infinity, `Q^ord_infinity=vol(H'_infinity)/2` in the selected trivial-weight source-compatible vector lane;
6. at every odd bad `ell|N`, protected WP53A remains `Q_ell=1+ell^(-1)`.

We now compute the single archimedean formal volume required by Disegni's global volume-one condition.

## 2. Elementary idelic quotient-volume lemma

Let

`H' = Res_{K/Q} G_m / G_m`.

Then

`H'(Q)\H'(A)
 ~= K^x\A_K^x/A_Q^x`.

At each finite place let `dt_ell^CST` be the protected CST quotient measure and put

`m_ell
 := vol(O_{K,ell}^x/Z_ell^x,dt_ell^CST)`.

Let `dt_infinity` be an arbitrary formal Haar measure on

`H'(R)=C^x/R^x`,

and write

`V_infinity := vol(H'(R),dt_infinity)`.

### Lemma `BSD-A1-WP54A-IDELIC-VOLUME-001`

For the product measure

`dt = dt_infinity * product_{ell<infinity} dt_ell^CST`,

one has exactly

`vol(H'(Q)\H'(A),dt)
 = (h_K/u_K) * V_infinity * product_ell m_ell`.

### Proof

Consider the finite ideles. Sending a finite idele of `K` to its associated fractional ideal induces the standard ideal-class quotient. Modding out by `K^x` changes an ideal only by a principal ideal. Modding out additionally by `A_{Q,f}^x` does not further change the ideal class: for any rational finite idele, its valuation vector is represented by a rational number `q in Q^x`, and after division by `q` the finite idele lies in `Zhat^x`, which is already contained in the finite compact denominator.

Therefore the finite quotient has exactly `h_K` ideal-class components.

Fix one such finite component. The residual stabilizer acting on the archimedean quotient `C^x/R^x` consists exactly of global units modulo rational units:

`O_K^x/{+1,-1}`.

Its order is `u_K`. Thus each ideal-class component has archimedean quotient volume `V_infinity/u_K`.

The finite compact part contributes the product of local compact-quotient volumes `product_ell m_ell`. Summing the equal-volume components over the `h_K` ideal classes gives

`(h_K/u_K) * V_infinity * product_ell m_ell`.

No analytic class-number formula is used. QED.

## 3. Exact finite compact-volume product

Protected MATHFORGE WP54 gives:

- `m_ell=1` at every split finite place;
- `m_ell=1` at every unramified nonsplit finite place;
- `m_ell=|D_ell|^(1/2)` at every ramified finite place.

Because `D_K` is a quadratic fundamental discriminant and `(D_K,2)=1`, every ramified prime is odd and has local discriminant exponent one. Hence

`product_ell m_ell
 = product_{ell|D_K} ell^(-1/2)
 = |D_K|^(-1/2)`.

### Corollary `BSD-A1-WP54A-ARCH-VOLUME-001`

Choose `dt_infinity` so that Disegni's global normalization

`vol(H'(Q)\H'(A),dt)=1`

holds while retaining the CST quotient measure at every finite place. Then

`V_infinity
 = (u_K/h_K) |D_K|^(1/2)`.

### Proof

Insert the finite product `|D_K|^(-1/2)` into Lemma `IDELIC-VOLUME-001` and solve the equation

`1=(h_K/u_K) V_infinity |D_K|^(-1/2)`.

QED.

## 4. Exact local ledger in the chosen global decomposition

Use the CST quotient measure at every finite place and the formal archimedean measure fixed by Corollary `ARCH-VOLUME-001`.

Choose source-compatible pure tensors so that every numerator/denominator vector factor appearing in Disegni Lemma 4.3.3 is represented by the same nonzero local line in numerator and denominator. The explicit vector ratios are therefore exactly `1`.

Because protected MATHFORGE WP54 gives `Sigma=emptyset`, there is no surviving finite quaternion-ramified product.

The remaining ledger is:

### (a) Unramified finite places away from `2ND_K`

The spherical normalized factor is `1`.

### (b) Discriminant primes `ell|D_K`

The representation is unramified because `(D_K,N)=1`. The exact source-normalized factor is

`Q_ell=ell^(-1/2)`.

Thus

`product_{ell|D_K} Q_ell
 = |D_K|^(-1/2)`.

### (c) Odd semistable bad primes `ell|N`

Protected WP53A gives

`Q_ell=1+ell^(-1)`.

Hence

`product_{ell|N} Q_ell
 = product_{ell|N}(1+ell^(-1))`.

### (d) The selected prime `2`

Protected MATHFORGE WP54 gives, in the CST local measure,

`Q^ord_2=2`.

### (e) Infinity

Protected MATHFORGE WP54 gives

`Q^ord_infinity=V_infinity/2`.

Therefore the combined `2`-and-infinity ordinary factor is

`Q^ord_{2,infinity}
 = 2 * (V_infinity/2)
 = V_infinity
 = (u_K/h_K)|D_K|^(1/2)`.

The factor `2` introduced by changing from WP42B's canonical local measure to the CST finite measure is therefore not lost. It cancels only the explicit archimedean `1/2` in Disegni's ordinary normalization.

## 5. Global theorem

### Theorem `BSD-A1-WP54A-GLOBAL-QORD-001`

For the protected BSD-001 auxiliary field and the source-compatible selected ordinary/test-vector packet, using CST quotient measures at every finite place and the unique formal archimedean scaling giving Disegni's adelic volume one,

`Q^ord
 = (u_K/h_K)
   * product_{ell|N}(1+ell^(-1))`.

No unspecified unit occurs.

### Proof

Disegni Lemma 4.3.3 decomposes `Q^ord` into the finite local factors, the `p-infinity` ordinary factor, and vector ratios. Under the selected packet:

- `Sigma=emptyset`;
- all vector ratios are exactly one;
- all unramified finite places away from `D_K` contribute one;
- the product over `ell|D_K` is `|D_K|^(-1/2)`;
- the product over `ell|N` is `product(1+ell^(-1))`;
- the combined `2`-and-infinity factor is `(u_K/h_K)|D_K|^(1/2)`.

Multiplying gives exact cancellation of the formal square-root discriminant factors:

`(u_K/h_K)|D_K|^(1/2)
 * |D_K|^(-1/2)
 * product_{ell|N}(1+ell^(-1))`

`= (u_K/h_K)
   * product_{ell|N}(1+ell^(-1))`.

QED.

## 6. Exact `2`-adic valuation

### Corollary `BSD-A1-WP54A-GLOBAL-QORD-VAL-001`

One has

`ord_2(Q^ord)
 = ord_2(u_K)-ord_2(h_K)
   + sum_{ell|N} ord_2(ell+1)`.

### Proof

Every `ell|N` is odd, so `ord_2(ell)=0`. Therefore

`ord_2(1+ell^(-1))=ord_2(ell+1)`.

Apply `ord_2` to Theorem `GLOBAL-QORD-001`. QED.

The formula remains valid in the exceptional-unit imaginary quadratic cases because `u_K` is retained rather than silently set equal to one.

## 7. D2c disposition

The boundary

`MISSING_P2_DISEGNI_GLOBAL_MEASURE_AND_AUXILIARY_QORD_RECONCILIATION`

is resolved by the exact formula above:

`RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`.

This result closes the automorphic `Q^ord` ledger only. It does not prove any cancellation with the separate Tamagawa, determinant/Fitting, Bockstein, regulator, or period ledgers.

## 8. Surviving campaign boundaries

After WP54A:

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`;
- D2b: `RESOLVED_WP52A_FINITE_COMPARISON_DETERMINANT`;
- D2c: `RESOLVED_WP54A_GLOBAL_QORD_RECONCILIATION`;
- D2d: `MISSING_P2_CLASSICAL_GROSS_ZAGIER_WP00_NORMALIZATION`;
- D2e: `MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

## 9. Claim firewall

WP54A does not prove:

- D1c;
- fixed-`2` height nondegeneracy D2a;
- cancellation of `u_K/h_K` or `product(1+ell^(-1))` with another campaign ledger;
- the classical Gross–Zagier/WP00 normalization D2d;
- exact WP06 quadratic descent D2e;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, priority, patentability, or commercial claims.
