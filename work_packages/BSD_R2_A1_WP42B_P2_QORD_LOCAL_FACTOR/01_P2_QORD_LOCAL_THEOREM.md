# WP42B theorem — exact canonical ordinary local toric factor at `2`

## 1. Protected setup

Let `v=2` in the selected BSD-001 auxiliary lane. Protected facts are:

1. `2` is split in the WP09 imaginary quadratic field `K`;
2. the Hecke character is trivial;
3. `E/Q` has good ordinary reduction at `2`, so `2` does not divide the conductor and the local automorphic representation is unramified;
4. the ordinary refinement is the unramified refinement determined by the protected `2`-adic unit root `alpha`;
5. protected MATHFORGE WP42B at `a014559b89897bcfa2078147224e598ab6aaedca` admits the exact Appendix-A.3 local normalization.

## 2. Source-normalized local formula

Disegni equation (A.3.3) gives

`Q^ord_{v,dt}((f1 tensor f2)/(f3 tensor f4))`

`= mu^+(j_v) * vol^circ(H'_v,dt) * (f1 tensor f2)/(f3 tensor f4)`.

For the split extension, equation (A.1.2) gives

`j_v=(-1,1)`,

hence

`N(j_v)=-1`.

For the canonical ordinary vectors in the proof of Proposition A.3.4,

`f1=f3`, `f2=f4`,

so the vector ratio is one. The canonical local measure used there satisfies

`vol^circ(H'_v,dt_v^can)=1`.

Finally

`mu^+ = chi_v * (alpha |.|) o N`.

The selected `chi_v` is trivial. Since `alpha` is unramified, it is trivial on `Z_2^x`, in particular on `-1`; also `|-1|_2=1`. Thus

`mu^+(j_2)=1`.

### Theorem `BSD-A1-WP42B-P2-QORD-001`

For the selected lane and Disegni's canonical local vectors and measure,

`Q^ord_{2,dt_2^can}=1`.

Consequently

`ord_2(Q^ord_{2,dt_2^can})=0`.

### Proof

Substitute the preceding four exact terms into (A.3.3). QED.

## 3. Relation to WP41

Protected WP41 proves for the source-compatible ordinary normalization

`e_{2,infinity}^{-1}Q_special=Q^ord`.

WP42B evaluates only the canonical `2`-adic local toric term inside the source product for `Q^ord`. It does not imply that the whole product has zero valuation.

In particular, the positive valuation previously associated with a separate unit-root interpolation factor is not contradicted. WP41 transfers that normalization into the ordinary pairing. WP42B then evaluates the resulting canonical split-`2` toric term; any other normalization scalar needed to reconcile the global adelic measure remains elsewhere in the product ledger.

## 4. Measure-scaling theorem

Let

`dt_2' = c_2 dt_2^can`

for a nonzero scalar `c_2` in the coefficient field. Since the local toric integral is linear in the Haar measure,

`Q^ord_{2,dt_2'}=c_2 Q^ord_{2,dt_2^can}=c_2`.

Therefore

`ord_2(Q^ord_{2,dt_2'})=ord_2(c_2)`.

Any use of a noncanonical local measure must retain this exact scalar and its compensating global measure factor. There is no measure-independent zero-valuation theorem here.

## 5. Refined D2c ledger

Write schematically

`Q^ord = Q^ord_2 * Q^ord_bad * Q^ord_aux * Q^ord_measure * Q^ord_infty`,

where each symbol abbreviates exactly the corresponding source factors of Disegni (4.3.4), not an asserted canonical factorization beyond that formula.

With canonical `dt_2`, WP42B gives

`ord_2(Q^ord_2)=0`.

The surviving D2c task is to evaluate the other source factors and any measure-rescaling term exactly.

## 6. Claim firewall

WP42B does not prove:

- `ord_2(Q^ord)=0`;
- any bad-prime or auxiliary factor is a unit;
- a global measure term has zero valuation;
- cancellation with Tamagawa numbers or the WP40 finite dual hit;
- height nondegeneracy;
- the WP00 real normalization;
- D1c or final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification.