# WP45A strengthening — local `Tor_1` vanishing and quotient-torsion kernel

This note strengthens the general defect calculation in `01_DERIVED_LOCAL_CONDITION_THEOREM.md` for the actual BSD-001 local Iwasawa cohomology.

## 1. Ambient local Iwasawa augmentation

Let

`C_w:=RΓ_Iw(K_w,T)`

over

`Lambda_w=Z_2[[Gamma_w]]`,

with `Gamma_w~=Z_2` and `t_w=gamma_w-1`.

The protected Nekovář cyclotomic augmentation formalism gives the canonical derived specialization

`C_w derived_tensor_{Lambda_w} Z_2 ~= RΓ(K_w,T)`.

Both source and target have degree-zero cohomology equal to zero:

- `H^0(K_w,T)=0` because `E(K_w)[2^infinity]` is finite;
- `H^0(C_w)=0` because every finite-layer `H^0(K_{n,w},T)` is zero.

Since `Z_2=Lambda_w/(t_w)` has projective dimension one, the hyper-Tor edge sequence in degree zero is

`0 -> H^0(C_w)_{Gamma_w}
   -> H^0(K_w,T)
   -> H^1(C_w)[t_w]
   -> 0`.

The first two terms vanish. Therefore

### Theorem `BSD-A1-WP45A-IW-TORSION-005`

`H^1_Iw(K_w,T)[t_w]=0`.

## 2. Vanishing of the point-module `Tor_1`

Protected WP45A has a canonical injection

`M_w^Kum -> H^1_Iw(K_w,T)`.

Hence

`M_w^Kum[t_w]=0`.

Therefore the group denoted

`T_w^Kum:=M_w^Kum[t_w]`

in the general defect calculation vanishes on the selected BSD-001 local tower.

Equivalently,

`Tor_1^{Lambda_w}(M_w^Kum,Z_2)=0`.

The derived augmentation of the Kummer local source has no degree-zero `Tor_1` correction.

## 3. Identification of the remaining coinvariant kernel

Put

`H_w^Iw:=H^1_Iw(K_w,T)`

and

`Q_w^Iw:=H_w^Iw/M_w^Kum`.

The short exact sequence

`0 -> M_w^Kum -> H_w^Iw -> Q_w^Iw -> 0`

gives, after taking `t_w`-torsion and coinvariants,

`0 -> Q_w^Iw[t_w]
   -> (M_w^Kum)_{Gamma_w}
   -> (H_w^Iw)_{Gamma_w}`

because both `M_w^Kum[t_w]` and `H_w^Iw[t_w]` vanish.

The ambient Iwasawa specialization edge sequence gives an injection

`(H_w^Iw)_{Gamma_w} -> H^1(K_w,T)`.

Under this injection the map from `(M_w^Kum)_{Gamma_w}` is the base Kummer map induced by norm-compatible points. Therefore its kernel

`B_w^Kum
 := ker((M_w^Kum)_{Gamma_w} -> E(K_w)^hat_2)`

is canonically

### Theorem `BSD-A1-WP45A-KERNEL-006`

`B_w^Kum ~= Q_w^Iw[t_w]`.

Thus the only unknown kernel term is the augmentation torsion of the **quotient of local Iwasawa cohomology by the Kummer norm-limit submodule**.

## 4. Strengthened local defect

The local derived specialization cone of WP45A therefore has only

`H^0(Delta_w^Kum)=B_w^Kum ~= Q_w^Iw[t_w]`,

`H^1(Delta_w^Kum)=U_w`,

and

`H^{-1}(Delta_w^Kum)=0`.

At `w|2`, `U_w` retains the protected exact filtration

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`.

## 5. Refined remaining question

WP45A has therefore removed the generic `Tor_1(M_w^Kum,Z_2)` ambiguity. The remaining local derived-control question is exactly

`Q_w^Iw[t_w]`

and its map into the strict-to-Kummer comparison cone.

This note does not assert that `Q_w^Iw[t_w]=0`.

## Claim firewall

No statement here proves:

- `B_w^Kum=0`;
- perfectness of the Kummer Iwasawa Selmer complex;
- cancellation of the formal universal-norm term at `2`;
- equality of `D_K` with a Bockstein defect;
- BSD or certification.