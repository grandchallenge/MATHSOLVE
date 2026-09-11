# BSD-R2-A1-WP23 — primitive good-ordinary local control at `2`

## Metadata

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Parent: protected `BSD-R2-A1-WP22-ODD-LOCAL-TAMAGAWA-CONTROL`.
- Protected MATHSOLVE baseline: `4a649ace4e513871c84c6fbe11c2a16885fcc386`.
- Protected MATHFORGE source admission: `e6f025896532021a84edf05b54034edc9834a022`.
- Admitted source audit: `sources/BSD-001/GREENBERG_P2_PRIMITIVE_LOCAL_CONTROL_SOURCE_AUDIT.md`.
- Claim boundary: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Primary type: source-bound local-control theorem and exact finite `Z_2`-length calculation.

## Material result

Protected WP21 defines the primitive classical-Kummer ambient local-control kernel at `2` by

`K_2 := ker(H^1(Q_2,E)[2^infinity]
           -> H^1(Q_{infty,2},E)[2^infinity]^Gamma_2)`.

The protected MATHFORGE admission of Greenberg's local control theorem applies literally at `p=2` and uses the same classical Kummer quotient. Composing that admitted theorem with protected WP21 and protected WP07 gives

`#K_2 = #E_tilde(F_2)[2^infinity]^2
      = (3-a_2)^2`.

Because protected WP07 proves `a_2 in {+1,-1}`, one obtains exactly

`len_Z2(K_2^vee) = 2 ord_2(3-a_2)`.

Thus:

- if `a_2=+1`, then `#K_2=4` and `len_Z2(K_2^vee)=2`;
- if `a_2=-1`, then `#K_2=16` and `len_Z2(K_2^vee)=4`.

Equivalently,

`Fitt^0_Z2(K_2^vee) = (3-a_2)^2 Z_2`.

Protected WP07 independently proves

`ord_2((1-alpha^(-1))^2)=2 ord_2(3-a_2)`

for the normalization-specific squared unit-root factor. WP23 records the resulting exact equality of valuations

`len_Z2(K_2^vee)
 = ord_2((1-alpha^(-1))^2)`

when that normalization is in force. This is not an analytic determinant identity.

## Combined ambient local-control length

Protected WP22 gives

`len_Z2(K_bad^vee)=sum_{ell|N} ord_2(c_ell)`.

All odd good-prime kernels and the real-place kernel vanish. Therefore the full finite ambient primitive local-control kernel has exact total length

`len_Z2(K_loc^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)`.

This is the length of the **ambient** local kernel. Protected WP21's actual specialization defect remains

`C_E := im(loc_Q) intersect K_loc`,

which can be a proper subgroup.

## Boundary closed

WP23 closes

`MISSING_P2_GOOD_ORDINARY_LOCAL_CONTROL_KERNEL_AT_2`.

The remaining D1b boundary is now exactly

`MISSING_P2_GLOBAL_HIT_SUBGROUP_OF_LOCAL_CONTROL_KERNELS`.

## Claim firewall

WP23 does not prove:

- `C_E=K_loc`;
- surjectivity of global localization onto `K_2` or any bad-prime kernel;
- the order or length of `C_E`;
- equality of finite Kummer and Greenberg local conditions by assumption;
- a primitive cyclotomic perfect determinant realization;
- an analytic determinant generator at height one `(2)`;
- the WP20 Bockstein/WP00 normalization;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.
