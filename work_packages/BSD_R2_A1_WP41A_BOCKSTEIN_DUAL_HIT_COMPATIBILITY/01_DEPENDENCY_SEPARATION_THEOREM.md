# WP41A theorem — protected-interface separation of cyclotomic Bockstein and fixed-level local-condition defect

## 1. Objects already protected

Let `T=T_2(E)` over the protected auxiliary imaginary quadratic field `K`.

Protected WP37 fixes the source-compatible strict/ordinary Nekovar Selmer complex

`C_str := RΓ_f(K,T)`

and its cyclotomic deformation over the augmentation algebra. The augmentation exact sequence produces the first cyclotomic Bockstein

`beta_str : H~^1_f(K,T) -> H~^2_f(K,T) tensor Gamma_K`,

and Selmer duality converts this into the first p-adic height pairing. The construction differentiates one fixed Selmer complex in the cyclotomic parameter.

Protected WP39 fixes, at augmentation level, the nested compact local conditions

`U_str subset U_Kum`

and proves

`0 -> H~^1_f(K,T) -> S_2(E/K) -> J_K -> 0`.

Protected WP40 dualizes the corresponding finite local quotient

`R_K := U_Kum/U_str`

and defines

`D_K := im((G_A intersect U_str^perp) -> U_str^perp/U_Kum^perp)`,

proving

`ann(J_K)=D_K`.

Thus `D_K` is a finite defect created by changing local conditions at fixed augmentation level.

## 2. The two operations are formally different

There are two independent operations in play.

### Cyclotomic deformation

Fix a Selmer structure `U`. Lift its Selmer complex from `Z_2` to the cyclotomic Iwasawa algebra `Λ_K`, then apply augmentation. The connecting morphism for the augmentation ideal gives a Bockstein.

Symbolically:

`C_U,∞ --augmentation--> C_U`

produces

`beta_U`.

### Change of local condition

Fix the coefficient ring and base field. Replace `U_str` by the larger `U_Kum`. The difference is measured by the finite local quotient

`R_K=U_Kum/U_str`

and its dual quotient.

Symbolically:

`C_str -> C_Kum -> RΓ_local(R_K) -> C_str[1]`

would be the expected comparison triangle if such a compatible derived construction has been supplied.

WP39 proves the required degree-one fixed-level exact sequence, but it does not construct this triangle over the cyclotomic Iwasawa algebra.

## 3. Protected data do not supply a commuting square

To identify `D_K` with a Bockstein image, radical, kernel, or cokernel, one needs compatibility of the two operations above.

At minimum, one requires:

1. a cyclotomic strict Selmer complex `C_str,∞` over `Λ_K`;
2. a cyclotomic classical-Kummer comparison object `C_Kum,∞` over the same algebra;
3. a distinguished comparison triangle

   `C_str,∞ -> C_Kum,∞ -> Q_∞ -> C_str,∞[1]`;

4. derived base-change at augmentation identifying `Q_∞ tensor^L_{Λ_K} Z_2` with the fixed-level local-condition quotient that yields WP39/WP40's `R_K` and `D_K`;
5. naturality of the augmentation connecting morphisms with respect to this triangle.

Only after these data are available can the snake/long-exact or octahedral comparison be used to relate the Bockstein of `C_str` to the finite local-condition defect.

The protected BSD chain contains items analogous to (1) for the strict Nekovar complex and a separate primitive-Kummer cyclotomic presentation over `Q` in WP35. It does not contain items (2)–(5) over the protected field `K` for the strict-versus-Kummer comparison.

WP35 cannot fill the gap: it is a `Q`-side primitive classical-Kummer cyclotomic square presentation with its own augmentation defect `C_E^vee`, not a `K`-side comparison morphism from the WP37 strict Selmer complex.

WP36 cannot fill the gap: it concerns finite formal universal-norm membership and does not construct a derived comparison of Selmer complexes.

## 4. Theorem `BSD-A1-WP41A-SEPARATION-001`

From the protected interfaces through WP40, none of the following identities is derivable without an additional compatibility theorem:

`D_K = im(beta_str)`,

`D_K = ker(beta_str)`,

`D_K = coker(beta_str)`,

`D_K = rad(h_str)`,

or equality of their `Z_2`-lengths.

### Proof

The protected definition of `beta_str` uses the augmentation connecting morphism of the cyclotomic deformation of the fixed strict Selmer complex. Its source and target are cohomology groups of that fixed Selmer structure.

The protected definition of `D_K` uses the quotient of annihilator local conditions

`U_str^perp/U_Kum^perp`

at fixed augmentation level and the image of global discrete cohomology in that quotient.

No protected morphism identifies this quotient with a subquotient of the target of `beta_str`, and no protected distinguished triangle makes the augmentation connecting morphism natural with respect to the strict-to-Kummer change of local conditions.

Therefore an equality of the displayed objects would require an unproved comparison morphism. It cannot be obtained by formal substitution from the existing exact sequences alone. QED.

The theorem is a statement about the logical content of the protected interfaces. It does not assert that such an identification is mathematically impossible or absent from the literature.

## 5. Minimal missing bridge

The exact successor boundary is

`MISSING_P2_IWASAWA_STRICT_KUMMER_BOCKSTEIN_COMPATIBILITY_OVER_K`.

A sufficient successor theorem would construct an Iwasawa-level strict-to-Kummer comparison triangle over `K`, prove derived augmentation compatibility, and identify the specialized dual local quotient with WP40's `R_K^dual`.

That theorem could then determine whether `D_K` is an explicit Bockstein defect and whether D2a and D2b genuinely merge.

A weaker theorem that only compares the two Selmer groups after tensoring with `Q_2`, or only up to finite error, is insufficient because `D_K` is itself the exact finite `2`-primary error being measured.

## 6. Claim firewall

WP41A does not prove:

- theorem nonexistence;
- `D_K != im(beta_str)` or any other inequality in a future enlarged framework;
- `D_K=0`;
- height nondegeneracy;
- a value for `d_K` or `j_K`;
- an analytic determinant identity;
- BSD or MATHCERT certification.