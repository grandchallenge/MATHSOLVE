# WP60A-A0 exact determinant dependency map

## 1. Primitive finite target

Protected WP16A fixes

`s_n(E)=ord_2 #Sel_{2^n}(E/Q)-n`.

The exact Kummer sequence and the selected rank-one, odd-torsion hypotheses give

`s_n(E)=ord_2 #Sha(E/Q)[2^n]`

and hence

`lim_n s_n(E)=len_{Z_2} Sha(E/Q)[2^infinity]`.

Protected WP16B defines the primitive Kummer Pontryagin dual

`X_E=Sel_{2^infinity}^{Kum}(E/Q)^vee`

with torsion submodule

`T_E=Tor_{Z_2}(X_E)=Sha(E/Q)[2^infinity]^vee`.

Therefore

`Fitt^0_{Z_2}(T_E)=2^{lim_n s_n(E)} Z_2`.

Protected WP19 identifies the rank-one derived Fitting ideal:

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.

Thus

`v_2(Fitt^1_{Z_2}(X_E))
 = lim_n (ord_2 #Sel_{2^n}(E/Q)-n)`.

No analytic input has yet entered this equality.

## 2. Cyclotomic presentation

Let

`Lambda=Z_2[[T]]`

and

`X_infty=Sel_{2^infinity}^{Kum}(E/Q_infty)^vee`.

Protected WP35 proves that `X_infty` has projective dimension one and admits a square presentation

`0 -> Lambda^r --A(T)--> Lambda^r -> X_infty -> 0`.

Specialization at augmentation gives

`M_0=coker A(0) ~= (X_infty)_Gamma`.

Protected cyclotomic control gives

`0 -> C_E^vee -> M_0 -> X_E -> 0`

and hence on torsion

`0 -> C_E^vee -> Tor(M_0) -> T_E -> 0`.

Therefore the finite specialization defect is already algebraically explicit.

## 3. Leading determinant coefficient

The rank-one augmentation-zero situation makes `det A(T)` vanish at least to first order at `T=0`.

Protected WP20/WP35 give the exact ideal identity

`(coeff_T det A(T)) Z_2
 = Fitt^0_{Z_2}(C_E^vee)
   Fitt^1_{Z_2}(X_E)
   B_A`,

where `B_A` is the protected Bockstein/specialization factor in the chosen determinant normalization.

Consequently, once the analytic generator is identified with `det A(T)` integrally, the primitive first-Fitting factor occurs on an already fixed algebraic line. No untracked finite Selmer factor is permitted.

## 4. Local and strict/Kummer corrections are not open inputs

Protected WP36 computes the finite local reciprocity/control defect entering the cyclotomic specialization.

Protected WP39–WP51 establish the source-compatible literal-`p=2` Kummer/Greenberg/strict comparison, specialization, silent-kernel control, and duality needed to make the determinant comparison integral.

Protected WP52A packages the finite strict/Kummer comparison into a finite cone `V_K` and proves

`len_{Z_2} V_K
 = 4 ord_2(3-a_2)
   + 2 sum_{ell|N} ord_2(c_ell)`.

Thus the full finite comparison determinant is known. A future analytic proof may have to transport these factors through its own normalization, but it may not treat them as new unknown exponents.

## 5. Analytic line already normalized downstream

Protected WP53A and WP54A reconcile the split bad-prime and global ordinary/test-vector factors.

Protected WP55A–WP58A place the real analytic expression on the exact rational line

`delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`

for the fixed source-compatible parametrization with `ord_2(C_f)=0`.

WP59 isolates the residual

`R_2(E,K,f)=2 ord_2(m_K(f))-ord_2(lambda_D)`.

This is a distinct D2d presentation of the same unresolved literal-`2` arithmetic. WP60A seeks to bypass its separate two-term evaluation by constructing the analytic determinant generator directly.

## 6. Exact analytic insertion point

The missing theorem must supply an integral analytic element `z_an` on the determinant line such that its image under the protected specialization/Bockstein maps agrees with the normalized analytic leading term and such that the determinant coordinate is controlled at the height-one prime `(2)`.

At minimum, two logically separate statements are required.

### A1-LIFT

Construct an integral determinant element whose image in first cohomology is the relevant Kato/analytic zeta class, or an exact finite-level substitute with the same primitive specialization.

Boundary:

`MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.

### A1-PRIMITIVITY

Show that the lifted element generates the correct determinant lattice at `(2)`, equivalently that no additional factor `2^a`, `a>0`, remains between the analytic element and the primitive algebraic determinant generator.

Boundary:

`MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.

A lift without primitivity gives only a divisibility/containment statement and is insufficient for the exact valuation theorem.

## 7. Why the BKS route does not close A1 as imported

Protected MATHFORGE `e44baeeed5d508fd4e5332c883c837951e51c000` audits Burns–Kurihara–Sano and Burns–Sakamoto–Sano.

The BKS determinantal-zeta construction is structurally the correct model: it lifts Kato's Iwasawa zeta class into an inverse determinant line and then compares the resulting special element with arithmetic Fitting data.

However:

1. BKS Hypothesis 2.2 excludes `p=2` directly;
2. the proof of their determinant lift passes through Stark/Kolyvagin-system machinery;
3. the decisive regulator isomorphism used in that machinery is stated under `p>3`;
4. equality/primitivity of the determinant special element is a further obligation beyond existence of the lift.

Therefore no protected source currently licenses either A1-LIFT or A1-PRIMITIVITY for the selected literal-`p=2` class.

## 8. Preferred finite-level bypass

The next proof attempt should avoid reconstructing the entire odd-prime Kolyvagin-system theory if the required determinant statement can be obtained directly.

A successful finite-level argument must provide all of the following on one exact integral line:

1. a perfect finite-level Selmer or cohomology complex over `Z_2` or the relevant finite group ring;
2. an integral determinant lattice;
3. an analytic/modular-symbol/Kato-derived class in the corresponding first cohomology;
4. a proof that this class lies in the determinant image;
5. exact primitive Kummer local-condition comparison at `2` and every bad prime;
6. compatibility with the protected cyclotomic specialization/Bockstein map;
7. a basis/primitivity or reverse-divisibility theorem at `(2)`.

If item 4 can be proved but item 7 cannot, record partial success and continue; do not promote R5.

## 9. Formal reduction proposition

### Proposition `BSD-A1-WP60A-A0-REDUCTION-001`

Assume the protected WP16A/B, WP19, WP35–WP36, WP39–WP52A chain and the protected source-normalization inputs through WP58A.

Then all algebraic finite-level, specialization, and strict/Kummer determinant factors needed to identify the primitive rank-one first-Fitting ideal are already fixed. To close D1c by the determinantal-zeta route it is sufficient to prove:

1. `A1-LIFT`: an integral literal-`p=2` determinant lift, or exact finite-level replacement, of the normalized analytic/Kato class; and
2. `A1-PRIMITIVITY`: exact primitivity/reverse divisibility of that determinant element at the height-one prime `(2)`.

A theorem satisfying both and compatible with the protected normalization supplies the analytic determinant-generator input required by WP59 reopening condition `R5` and triggers full D2d replay.

**Status:** `PROVED_REDUCTION_FROM_PROTECTED_DEPENDENCIES`.

### Proof

WP16A/B and WP19 identify the target primitive first-Fitting ideal exactly. WP35 supplies the square cyclotomic presentation and expresses the first nonzero determinant coefficient as the product of the protected control factor, primitive first-Fitting ideal, and Bockstein/specialization factor. WP36 and WP39–WP52A determine the finite control and strict/Kummer determinant corrections. WP53A–WP58A separately fix the analytic normalization factors used downstream. Therefore no additional algebraic finite correction remains to be discovered before the analytic determinant can be compared with the primitive first-Fitting line.

Any determinant-lift theorem provides the missing analytic element on this fixed line; exact equality of ideals additionally requires the element to be primitive at `(2)`. Conversely, if both properties hold with the protected normalization, the analytic element is an integral generator of the required determinant line and the height-one-`(2)` exponent is determined. QED.

## 10. Current boundary map after A0

- D1c parent: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`.
- D1c/A1-LIFT: `MISSING_P2_KATO_ZETA_DETERMINANT_LIFT_AT_RESIDUE_CHARACTERISTIC_2`.
- D1c/A1-PRIMITIVITY: `MISSING_P2_DETERMINANTAL_ZETA_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- Combined refinement: `MISSING_LITERAL_P2_KATO_ZETA_DETERMINANT_LIFT_AND_PRIMITIVITY_AT_HEIGHT_ONE_2`.
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.
- D2d: unchanged WP59 boundary.
- D2e: downstream and unchanged.
- `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
