# WP41B theorem — exact absorption of Disegni's interpolation factor into the ordinary toric pairing

## 1. Protected input

Protected WP09 applies corrected Disegni Theorem B at `p=2` to the weight-two modular representation of the selected elliptic curve with trivial Hecke character over the protected all-`2N`-split auxiliary field `K`.

For suitable test vectors it gives

`h_V(P_Pi(f1),P_{Pi^vee}(f2))/(f3,f4)_Pi`

`= e_{2,infinity}(V_(pi,1))^(-1)
   * L'_2(V_(pi,1),0)
   * Q((f1 tensor f2)/(f3 tensor f4)).`                    `(B)`

Protected MATHFORGE WP41B at

`ab5e1c4d429bb36cce9927e62bcee5279870dec7`

admits Disegni Proposition 4.3.4, Theorem `B^ord`, Lemma 7.1.2, and Lemma 4.3.3 in the exact normalization needed below.

## 2. Trivial weight removes the archimedean interpolation factor

The selected elliptic lane is the source's trivial-weight case. Therefore the algebraic coefficient representation `W` is trivial and

`dim W=1`.

Disegni equation (1.4.5) gives

`e_infinity = 1`

at this weight. Hence

`e_{2,infinity}=e_2`.

This is an equality of source-normalized factors, not merely an equality of valuations.

## 3. Ordinary-vector transformation

For ordinary vectors `f1,f2,f3,f4`, let the source-defined special quadruple be

`f1' = gamma_H'^ord(f1)`,

`f2' = gamma_H'^ord(f2)`,

`f3' = w_a^ord(f3)`,

`f4' = f4`.

Protected Proposition 4.3.4 gives

`Q((f1' tensor f2')/(f3' tensor f4'))`

`= e_2(V_(pi,1)) * dim(W)
   * Q^ord((f1 tensor f2)/(f3 tensor f4)).`

Since `dim(W)=1` and `e_{2,infinity}=e_2`, this becomes

### Theorem `BSD-A1-WP41B-CANCEL-001`

`e_{2,infinity}^{-1}
 * Q((f1' tensor f2')/(f3' tensor f4'))`

`= Q^ord((f1 tensor f2)/(f3 tensor f4)).`                    `(C)`

### Proof

Substitute `dim(W)=1` and `e_{2,infinity}=e_2` into Proposition 4.3.4 and multiply by `e_{2,infinity}^{-1}`. QED.

No unit is inserted and no factor of `2` is discarded.

## 4. Ordinary Gross–Zagier formula

Substituting `(C)` into the protected Theorem-B identity `(B)` for the special quadruple gives the ordinary formula

`h_V^ord(P^ord,P^ord-dual)/(ordinary denominator)`

`= L'_2(V_(pi,1),0) * Q^ord`.                              `(Bord)`

This is exactly Disegni Theorem `B^ord`; protected Lemma 7.1.2 proves its equivalence to Theorem B in the protected non-exceptional lane.

### Corollary `BSD-A1-WP41B-NO-SEPARATE-E-001`

In the source-compatible ordinary normalization, D2c contains no independent valuation term

`ord_2(e_{2,infinity})`.

Any `2`-adic contribution represented by that factor in Theorem B has been transferred exactly into the definition of the ordinary test vectors and ordinary toric pairing. The remaining scalar normalization is `Q^ord`.

This statement must not be read as saying that the transferred contribution is zero.

## 5. Exact decomposition of `Q^ord`

Fix Disegni's decomposition of the adelic measure and the finite sets `Sigma`, `Sigma'` used in Lemma 4.3.3. In the source notation, equation (4.3.4) writes

`Q^ord =`

`  product_{v in Sigma'} Q_{v,dt_v}(local vector ratio)`

`* product_{v in Sigma}
     [ vol(E_v^x/F_v^x,dt_v)
       * L(V_(pi,1),v,0)^(-1)
       * local vector ratio ]`

`* (S p infinity vector ratio)`

`* Q^ord_{p infinity,dt_{p infinity}}(ordinary p-infinity vectors).`  `(Qord)`

The displayed formula is schematic only in typography; every factor refers to the exact source factor in Lemma 4.3.3 / (4.3.4). No source factor is omitted.

Taking a `2`-adic valuation is therefore legitimate only after the individual factors have been placed in the protected coefficient field/lattice and shown nonzero. When that is done,

`ord_2(Q^ord)`

is the sum of the exact local/measure/vector valuations in `(Qord)`.

## 6. What has been closed

The former D2c label

`MISSING_P2_DISEGNI_INTERPOLATION_FACTOR_VALUATIONS`

mixed two logically different tasks:

1. whether the explicit interpolation factor had to be valued separately;
2. how to value the residual test-vector normalization.

WP41B closes the first task by exact source normalization. The surviving task is only the second:

`MISSING_P2_DISEGNI_QORD_LOCAL_FACTOR_VALUATIONS`.

A successor should now bind the exact ordinary test-vector packet place by place and compute each factor of `(Qord)`, beginning with the two split places above `2` and the split bad primes dividing `N`.

## 7. Claim firewall

WP41B does not prove:

- `ord_2(Q^ord)=0`;
- any local factor in `(Qord)` is a unit;
- equality between the ordinary toric factor and a WP07/WP30 local factor merely from equal valuations;
- p-adic-height nondegeneracy;
- equality with the WP00 Neron–Tate regulator;
- an analytic determinant generator at `(2)`;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification.