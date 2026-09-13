# WP47A theorem — map-level identification of strict `H^2` and formal universal norms

## 1. Setup

Fix one protected split place `w|2`. Then

`K_w ~= Q_2`

and the local cyclotomic extension is totally ramified with unchanged residue field `F_2`.

Put

`T:=T_2(E)`

and use the protected good-ordinary exact sequence

`0 -> T_w^+ -> T -> T_w^- -> 0`.

Define

`V_w^-:=T_w^- tensor Q_2`,

`A_w^-:=V_w^-/T_w^-`.

Protected WP39 gives

`H^0(K_w,V_w^-)=0`

and defines the finite compact strict/Kummer local target

`R_w:=H^1(K_w,T_w^-)_tors`.

Protected WP46A gives

`0 -> Z_w^str -> U_w -> R_w -> 0`,

where

`U_w:=E(K_w)^hat_2/N_w^infinity`

and

`Z_w^str=H^2(U_{w,infty}^{+,str})`.

Protected WP28 gives independently

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`,

with the last map induced by literal reduction.

The purpose of WP47A is to compare the maps, not the orders.

## 2. Canonical identification of the ordinary target with reduction

Consider

`0 -> T_w^- -> V_w^- -> A_w^- -> 0`.

Since `H^0(K_w,V_w^-)=0`, its long exact cohomology sequence begins

`0 -> H^0(K_w,A_w^-)
   --delta_w--> H^1(K_w,T_w^-)
   -> H^1(K_w,V_w^-)`.

The target on the right is a `Q_2`-vector space and hence torsion-free. Therefore the image of `delta_w` is exactly

`H^1(K_w,T_w^-)_tors=R_w`.

Protected WP39 shows `H^0(K_w,A_w^-)` is finite, so it has no divisible subgroup. Hence:

### Theorem `BSD-A1-WP47A-ORDINARY-TARGET-001`

The connecting map is a canonical isomorphism

`delta_w:H^0(K_w,A_w^-) ~= R_w`.

For good ordinary reduction, `A_w^-` is the unramified etale quotient of the `2`-divisible group. Its inertia invariants are the etale `2`-power torsion of the special fibre. Thus

`H^0(K_w,A_w^-)
 ~= E_tilde(F_2)[2^infinity]`.

On the selected branch

`#E_tilde(F_2)=3-a_2 in {2,4}`,

so the entire reduction group is `2`-primary. We therefore obtain a canonical isomorphism

`rho_w:E_tilde(F_2) ~= R_w`.

No choice of generator is involved.

## 3. The compact strict/Kummer map is reduction followed by `rho_w`

Let

`kappa_w:E(K_w)^hat_2 -> H^1(K_w,T)`

be the compact Kummer map.

The protected finite strict local condition is

`ker(H^1(K_w,T) -> H^1(K_w,T_w^-))`,

while the compact Kummer local condition is the preimage of

`H^1(K_w,T_w^-)_tors`.

Thus the local quotient map used in WP39 is

`q_w:E(K_w)^hat_2
     --kappa_w--> H^1(K_w,T)
     -> H^1(K_w,T_w^-)_tors=R_w`.

### Lemma `BSD-A1-WP47A-KUMMER-REDUCTION-002`

The square

`E(K_w)^hat_2 --q_w--> R_w`

`      | red_w             ^ rho_w`

`      v                   |`

`E_tilde(F_2) ------------>`

commutes. Equivalently,

`q_w=rho_w o red_w`.

### Proof

Work first modulo `2^r`. For a point class `P in E(K_w)/2^rE(K_w)`, choose

`Q in E(K_wbar)`

with

`2^r Q=P`.

The Kummer cocycle is

`sigma |-> sigma(Q)-Q in E[2^r]`.

Project this cocycle through the ordinary etale quotient

`E[2^r] -> A_w^-[2^r]`.

Because `E` has good reduction, properness gives reduction of `Q`; projecting to the etale ordinary quotient commutes with reduction. The projected cocycle is therefore

`sigma |-> sigma(Qbar)-Qbar`,

which is exactly the connecting cocycle of the reduction point

`Pbar in E_tilde(F_2)[2^infinity]`

for the coefficient sequence

`0 -> T_w^-/2^rT_w^-
   -> V_w^-/2^rT_w^-
   -> A_w^-[2^r]
   -> 0`.

Consequently the composition of the finite Kummer map with the ordinary quotient equals the finite-level connecting map applied to literal reduction.

Pass to the inverse limit over `r`. The left side becomes the compact Kummer quotient map `q_w`; the right side becomes the connecting isomorphism `rho_w` applied to `red_w(P)`. Hence

`q_w=rho_w o red_w`.

This is also the compact-`T` form of the formal-group/reduction Kummer diagram underlying protected Greenberg Proposition 2.5. QED.

## 4. Passage to the universal-norm quotient

Protected WP28 proves that the stabilized universal norm subgroup

`N_w^infinity subset E(K_w)^hat_2`

lies in the kernel of literal reduction. Indeed, at finite local layer degree `2^n`, norm on the unchanged residue group is multiplication by `2^n`; the intersection of these images in the finite `2`-group `E_tilde(F_2)` is zero.

Therefore `red_w` factors canonically through

`U_w=E(K_w)^hat_2/N_w^infinity`:

`redbar_w:U_w -> E_tilde(F_2)`.

By Lemma `KUMMER-REDUCTION-002`, `q_w` has the same kernel on universal norms and factors as

`qbar_w:U_w -> R_w`

with

### Theorem `BSD-A1-WP47A-QUOTIENT-SQUARE-003`

`qbar_w = rho_w o redbar_w`.

The map `redbar_w` is the protected WP28 quotient map, and `qbar_w` is the protected WP46A/WP39 derived-control quotient map.

## 5. Equality of the two filtrations

Protected WP28 identifies

`ker(redbar_w)=F_w^norm`.

Protected WP46A identifies

`ker(qbar_w)=Z_w^str`.

Since `rho_w` is an isomorphism and

`qbar_w=rho_w o redbar_w`,

the kernels are equal as subgroups of the same ambient group `U_w`.

### Theorem `BSD-A1-WP47A-FILTRATION-004`

At each `w|2`,

`Z_w^str=F_w^norm`

inside `U_w`, and the diagram

`0 -> Z_w^str -> U_w -> R_w -> 0`

`     ||            ||     ^ rho_w`

`0 -> F_w^norm -> U_w -> E_tilde(F_2) -> 0`

commutes with exact rows.

Thus the strict-Iwasawa higher cohomology correction and Tan's formal universal-norm subgroup are the same **mapped subgroup**, not merely abstract cyclic groups of the same length.

Likewise

`R_w ~= E_tilde(F_2)`

canonically through `rho_w`, and the WP39 quotient map is literal reduction after this canonical identification.

## 6. Compatibility with the protected module descriptions

Protected WP46A gives

`Z_w^str
 ~= Lambda_w/(2^{m_2},gamma_w-1)`.

Protected WP28/WP30 gives

`F_w^norm
 ~= Gamma_w/(1-alpha)Gamma_w`

up to the already-protected exact unit-root principal-ideal convention, with

`ord_2(1-alpha)=m_2`.

Theorem `FILTRATION-004` identifies these two descriptions through their actual embeddings into `U_w`. WP47A does not introduce a new generator or scalar normalization; it identifies the subgroup defined by the maps.

In particular no `2`-power or unit can be hidden between the strict higher-cohomology correction and the formal universal-norm term.

## 7. Both split places above `2`

Protected WP09 makes `2` split in `K`. The two completions are copies of `Q_2` with conjugate copies of the same ordinary representation and cyclotomic tower. The construction above is functorial under this conjugation.

### Corollary `BSD-A1-WP47A-SPLIT-PAIR-005`

The map-level filtration identification holds at both places above `2`, with no additional global base-change index.

## 8. Consequence for D2b

The local strict/Kummer/formal normalization mismatch is closed.

The surviving D2b task is no longer local:

`MISSING_P2_GLOBAL_STRICT_KUMMER_COMPARISON_CONE_TO_WP40_BOCKSTEIN_DEFECT`.

The next operation must assemble the protected local reverse comparison triangles into the global Selmer-complex comparison and identify derived augmentation of that global cone with the protected finite global pair

`J_K` and `D_K=ann(J_K)`.

Only after that map-level global comparison is fixed may `D_K` be related to the protected WP37/WP43A Bockstein or height data.

## 9. Claim firewall

WP47A does not prove:

- `D_K` equals a Bockstein image, kernel, cokernel, or radical;
- `D_K=0` or `J_K=R_K`;
- fixed-`2` height nondegeneracy;
- D1c;
- remaining Disegni bad-prime/global normalization factors;
- classical/WP00 normalization;
- final WP06 descent;
- `BSD-R2-A1`;
- certification.