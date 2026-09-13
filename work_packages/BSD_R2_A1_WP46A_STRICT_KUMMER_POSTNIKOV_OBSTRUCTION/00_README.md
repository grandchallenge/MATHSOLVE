# BSD-R2-A1 WP46A — strict-to-Kummer Iwasawa Postnikov obstruction

## State

`PROVED_BOUNDED_DERIVED_REDUCTION`

## Protected predecessors

- MATHSOLVE WP45A: `5f7ea71f2d86457575b2bc2f1e8c281f09ce4b87`.
- WP39/WP40: exact finite strict-Greenberg/classical-Kummer comparison over `K` and its Poitou–Tate dual defect.
- WP43A: protected strict Greenberg Iwasawa augmentation/Bockstein naturality.
- MATHFORGE WP39/WP43A source admissions: Nekovář's literal-`p=2` strict/Kummer finite comparison and strict augmentation formalism.

No new external theorem premise is used.

## Result

Let `S_{w,infty}` be the protected strict Greenberg local-condition complex at a local place `w` of `K`, with morphism

`S_{w,infty} -> C_{w,infty}:=RΓ_Iw(K_w,T)`.

Let `U_{w,infty}^{+,Kum}` be the protected WP45A simple Kummer local condition, quasi-isomorphic to

`M_w^Kum[-1]`.

WP46A proves:

1. `H^0(S_{w,infty})=0` and the induced strict degree-one local condition
   `N_w^str:=H^1(S_{w,infty})`
   injects into the Kummer norm-limit module
   `M_w^Kum`;
2. the canonical truncation
   `tau_{<=1}S_{w,infty} ~= N_w^str[-1]`
   therefore maps canonically to `U_{w,infty}^{+,Kum}`;
3. writing
   `Z_w^str:=H^2(S_{w,infty})`,
   the strict local complex is determined by its Postnikov class
   `kappa_w^str in Ext^2_{Lambda_w}(Z_w^str,N_w^str)`;
4. the canonical `H^1` inclusion `u_w:N_w^str->M_w^Kum` extends to a derived local-condition morphism
   `S_{w,infty}->U_{w,infty}^{+,Kum}`
   if and only if
   `(u_w)_*(kappa_w^str)=0`
   in
   `Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)`;
5. when this obstruction vanishes, the set of lifts inducing `u_w` is a torsor under
   `Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`.

At odd non-`2` places the protected unramified strict local complex has no degree-two term, so `Z_w^str=0`; the comparison lift is therefore canonical there. The only possible derived lifting obstruction is concentrated at the good-ordinary places `w|2`.

## Refined boundary

The former boundary

`MISSING_P2_STRICT_TO_KUMMER_IWASAWA_COMPARISON_AND_DERIVED_DEFECT_IDENTIFICATION_OVER_K`

is narrowed to

`MISSING_P2_ORDINARY_STRICT_POSTNIKOV_PUSHFORWARD_AND_LIFT_CHOICE_AT_2`.

A successor must evaluate the two ordinary local groups

`Ext^2_{Lambda_w}(Z_w^str,M_w^Kum)`

and

`Ext^1_{Lambda_w}(Z_w^str,M_w^Kum)`,

show whether the pushed-forward Postnikov class vanishes, and then compare the resulting global cone with WP39/WP40.

## Claim firewall

WP46A does not prove:

- vanishing of the ordinary Postnikov obstruction;
- uniqueness of a strict-to-Kummer comparison lift at `w|2`;
- perfectness of the Kummer Iwasawa Selmer complex;
- `B_w^Kum=0`;
- cancellation of the formal universal-norm term;
- that `D_K` is a Bockstein defect;
- fixed-`2` height nondegeneracy;
- D1c, D2c–D2e;
- BSD or MATHCERT certification.