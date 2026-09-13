# WP51A theorem — finite Matlis correction is invisible to the first `Z_2`-valued height

## 1. Protected setup

Let

`H2_str := H~^2_f(K,T;Delta_str)`

for the protected strict Greenberg Selmer complex over the protected imaginary quadratic field `K`.

Protected WP50A defines the finite subgroup

`K_K^sil
 := ker(
      H2_str
      -> H^2(C_Kum,0) direct_sum Zloc
    )`

and proves

`D_K^vee ~= K_K^sil`.

Protected MATHFORGE WP51 admits Nekovar Theorem 6.3.4 and §6.3.5, literally at `p=2` over the totally imaginary field `K`, for the source-compatible orthogonal Greenberg local conditions.

Put

`A^*(1):=Hom(T,Q_2/Z_2(1))`

and

`S_str^dual
 := H~^1_f(K,A^*(1);Delta_str^perp)`.

The admitted source interface supplies a canonical perfect Pontryagin pairing

`< , >_M : H2_str x S_str^dual -> Q_2/Z_2`.

Protected WP37 separately supplies the cyclotomic Bockstein and the integral first p-adic height. The latter is obtained by composing the Bockstein with the source-compatible `Z_2`-valued degree-(2,1) Selmer duality pairing on the lattice side.

## 2. Exact discrete-dual quotient attached to the silent kernel

Define the Matlis annihilator

`N_K
 := (K_K^sil)^perp
 := { y in S_str^dual : <k,y>_M=0 for every k in K_K^sil }`.

### Theorem `BSD-A1-WP51A-MATLIS-QUOTIENT-001`

There is a canonical short exact sequence

`0 -> N_K -> S_str^dual -> D_K -> 0`.

Equivalently,

`D_K ~= S_str^dual/N_K`.

### Proof

The WP51 source interface gives perfect Pontryagin duality between `H2_str` and `S_str^dual`. Therefore restriction of the pairing to the finite subgroup `K_K^sil` induces a surjection

`S_str^dual -> (K_K^sil)^vee`

with kernel exactly `N_K`.

Protected WP50A gives

`(K_K^sil)^vee ~= D_K`.

Composing the two canonical identifications yields the displayed exact sequence. QED.

### Relation to protected WP40

Protected WP40 independently gives

`D_K ~= Sel_A^{str-perp}(K)/Sel_A^{Kum}(K)`.

The source-compatible object `S_str^dual` is the strict-perpendicular discrete Selmer group at the level of local conditions. WP51A does not identify `N_K` with `Sel_A^{Kum}(K)` merely from the fact that the two quotients are isomorphic. Such an equality requires compatibility of the two quotient maps and is not needed for the separation theorem below.

## 3. Finite strict `H^2` is killed by the integral height duality

Let

`L_str^dual`

denote the source-compatible compact/lattice degree-one dual Selmer module entering the WP37 first-height construction, and write

`< , >_G : H2_str x L_str^dual -> Z_2`

for the corresponding integral degree-(2,1) Selmer-duality pairing used after the Bockstein.

### Lemma `BSD-A1-WP51A-TORSION-BLIND-002`

Every finite subgroup of `H2_str` lies in the left kernel of `< , >_G`. In particular,

`<K_K^sil,L_str^dual>_G = 0`.

### Proof

Let `k in H2_str` have finite order `2^m`. For any `y in L_str^dual`, `Z_2`-bilinearity gives

`2^m <k,y>_G = <2^m k,y>_G = 0`.

The additive group `Z_2` is torsion-free, so `<k,y>_G=0`. Since `K_K^sil` is finite by WP50A, the assertion follows. QED.

No arithmetic nondegeneracy input is used.

## 4. First height factors through strict `H^2` modulo torsion

Protected WP37/WP43A give the first cyclotomic Bockstein

`beta_str:
 H~^1_f(K,T;Delta_str)
 -> H2_str tensor t_cyc`

and the first height

`h_str(x,y)
 := <beta_str(x),y>_G`.

Let

`H2_str,tf := H2_str/H2_str[tors]`.

### Theorem `BSD-A1-WP51A-HEIGHT-FACTORIZATION-003`

The first height factors canonically through the torsion-free quotient of its `H^2` target:

`H~^1_f(K,T;Delta_str)
 --beta_str--> H2_str tensor t_cyc
 -> H2_str,tf tensor t_cyc
 --duality--> Hom_Z2(L_str^dual,Z_2) tensor t_cyc`.

In particular, changing `beta_str(x)` by any element of

`K_K^sil tensor t_cyc`

does not change `h_str(x,y)` for any `y`.

### Proof

Apply Lemma `TORSION-BLIND-002` to the full torsion subgroup `H2_str[tors]`, then compose with the protected Bockstein definition of the first height. QED.

## 5. Separation of the finite WP40 correction from height nondegeneracy

Protected D2a asks whether the first `Z_2`-valued height on the rank-one free Selmer line is nonzero/nondegenerate.

Protected WP50A and Theorem `MATLIS-QUOTIENT-001` show that the finite WP40 defect `D_K` is instead the Pontryagin dual quotient attached to the finite subgroup

`K_K^sil subset H2_str[tors]`.

Theorem `HEIGHT-FACTORIZATION-003` shows that this finite subgroup is invisible to the first integral height.

### Theorem `BSD-A1-WP51A-D2-SEPARATION-004`

The finite strict/Kummer correction represented by `D_K` and fixed-`2` first-height nondegeneracy are distinct mathematical obligations.

More precisely:

1. `D_K` is canonically controlled by Matlis/Pontryagin duality on the finite subgroup `K_K^sil`;
2. the first height factors through `H2_str/H2_str[tors]` and therefore cannot detect `K_K^sil`;
3. no canonical identity of `D_K` with the image, kernel, cokernel, or radical of the first `Z_2`-valued height follows from the protected duality formalism;
4. proving the first height nondegenerate does not, by formal consequence alone, prove `D_K=0`;
5. proving `D_K=0` does not, by formal consequence alone, prove the first height nondegenerate.

The theorem does not rule out an arithmetic theorem imposing both conclusions simultaneously; it proves only that one is not the formal duality avatar of the other.

## 6. What remains of the finite correction

Write

`d_K := len_Z2 D_K = len_Z2 K_K^sil`.

Protected WP40 gives

`j_K+d_K
 = len_Z2 R_K
 = 2 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Thus the total ambient finite comparison length is already exact. However the protected chain contains no theorem that evaluates `d_K` individually or proves that the finite Matlis correction cancels from the eventual integral determinant normalization.

Accordingly WP51A does not erase `D_K`; it moves it out of the height-nondegeneracy problem and leaves it as an explicit finite determinant-normalization correction.

## 7. Refined D2b boundary

WP50A left

`MISSING_P2_STRICT_H2_SILENT_KERNEL_TO_BOCKSTEIN_HEIGHT_DUALITY`.

WP51A closes that question by exact separation rather than by a height-radical identification.

The surviving D2b boundary is

`MISSING_P2_FINITE_MATLIS_CORRECTION_EVALUATION_OR_CANCELLATION_IN_DETERMINANT_NORMALIZATION`.

A successor must either:

1. compute `d_K=len_Z2 D_K` exactly; or
2. prove an exact determinant comparison in which the `D_K` contribution cancels against a separately identified finite term.

An equality of total lengths `j_K+d_K=len R_K` alone is not sufficient unless the determinant comparison itself depends only on that total and this dependence is proved map-by-map.

## 8. Claim firewall

WP51A does not prove:

- `D_K=0` or `K_K^sil=0`;
- `N_K=Sel_A^{Kum}(K)`;
- fixed-`2` height nondegeneracy;
- the value of `d_K`;
- cancellation of `d_K` in a determinant formula;
- the height-one `(2)` analytic determinant generator;
- remaining Disegni normalization or global `Q^ord=1`;
- equality of p-adic and Neron-Tate heights;
- WP00 normalization;
- final quadratic descent;
- `BSD-R2-A1`;
- MATHCERT certification, novelty, or priority.
