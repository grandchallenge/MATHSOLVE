# WP19 final theorem-building gate

## Nominated theorem

`BSD-R2-A1-P2-RANK1-PRIMITIVE-FIRST-FITTING-RECIPROCITY`

Let `E/Q` satisfy the protected selected `BSD-R2-A1` hypotheses. Define, exactly as in WP16B,

`X_E := Sel_{2^infinity}^{Kum}(E/Q)^vee`,

where every finite-level local condition is the full classical Kummer image, including at `2` and at every bad semistable prime.

The final theorem must prove

`Fitt^1_{Z_2}(X_E) = 2^{delta_2(E)} Z_2`,

where

`delta_2(E)
 := ord_2(L'(E,1)/(Omega_E Reg_E))
    - sum_{ell|N} ord_2(c_ell)`.

Equivalently, it must prove

`v_2(Fitt^1_{Z_2}(X_E))=delta_2(E)`.

The equality is an equality of integral `Z_2` ideals. No inversion of `2`, unspecified `2`-power, or residual unit ambiguity may hide an exponent.

## Why `Fitt^1`, not a chosen quotient

Protected WP19 proves

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.

Thus the first Fitting ideal automatically removes the one free rank-one direction. A theorem can act on the canonical module `X_E` itself.

This eliminates the following interface from the final theorem:

- choosing a Mordell-Weil, Heegner, or Euler-system generator merely to define the finite quotient;
- proving that such a chosen generator spans the saturated free line before the algebraic target can even be stated.

If a proof uses a nonprimitive generator internally, its index still has to be computed exactly; the point is that the theorem statement and target ideal no longer depend on that choice.

## Mandatory theorem clauses

A proof of the nominated theorem must discharge all of the following inside one exact composition.

### F1 — coefficient and residual branch

- coefficient ring exactly `Z_2` or an explicitly finite flat coefficient ring whose norm/specialization back to `Z_2` preserves the complete exponent;
- literal prime `p=2`;
- selected good-ordinary reduction at `2`;
- globally irreducible/surjective residual representation `E[2]` with image `GL_2(F_2) ~= S_3`;
- no use of odd-prime residual distinguishedness unless an exact characteristic-2 replacement is proved.

### F2 — primitive local conditions

The algebraic theorem must control the WP16B primitive Kummer module, or prove exact finite kernel/cokernel comparisons from its own Selmer structure.

In particular:

- at `2`: no silent Kummer -> Greenberg substitution;
- at bad primes: no silent primitive -> unramified/strict/relaxed/imprimitive substitution;
- at infinity: retain the protected `2`-primary convention or prove its exact defect is zero.

### F3 — both WP13 Tamagawa regimes

The theorem must cover:

- regime A: every bad Tamagawa number odd;
- regime B: one or more even Tamagawa numbers with the exact residual-conductor drop proved by WP13.

A theorem assuming `2 not| product c_ell` is a regime-A theorem only and cannot close the selected class.

### F4 — rank-one Fitting output

The output must determine the intrinsic ideal

`Fitt^1_{Z_2}(X_E)`

or an exactly comparable derived determinant/Fitting ideal whose comparison to it is proved with no lost `2`-power.

`Fitt^0(X_E)` is not the target: `X_E` has rank one, so the zeroth ideal does not encode the finite torsion length in the required way.

### F5 — analytic reciprocity

The same theorem composition must identify the valuation of the analytic/determinant element with

`delta_2(E)`

in the protected WP00 normalization.

If a proof passes through a cyclotomic or anticyclotomic `2`-adic L-function, p-adic height, Heegner class, modular element, theta element, or Euler-system determinant, it must supply the exact chain back to

`L'(E,1)/(Omega_E Reg_E)`

and retain every unit-root, Euler, period, regulator, Tamagawa, isogeny, Manin, interpolation, and primitive/imprimitive correction with explicit `ord_2` contribution.

### F6 — integral exactness at `(2)`

A theorem controlling all height-one primes except `(2)` is insufficient unless the missing `(2)` exponent is independently determined. Likewise, a theorem after tensoring with `Q_2` is insufficient.

## Preferred proof architecture

WP19 does not prescribe a single proof technology, but it ranks the current architectures by unresolved comparison burden.

### Route 1 — direct finite-level / derived strong-Fitting over `Q` — preferred

Construct a literal `p=2` rank-one extension of the strong finite-level Fitting/Mazur-Tate/determinant philosophy that is native to the primitive Selmer structure and whose rank-one analytic leading object satisfies F5.

This route is preferred because, if formulated natively, it avoids separate:

- cyclotomic height-one `(2)` repair;
- Greenberg/Kummer comparison;
- primitive/imprimitive repair;
- quadratic descent and twist subtraction.

The protected MATHFORGE WP19 audit shows that the nearest existing strong finite-layer theorems currently screened are odd-prime and Tamagawa-prime-to-`p`; extending the architecture is therefore theorem construction, not source substitution.

### Route 2 — cyclotomic ordinary Iwasawa — admissible but longer

This route must first supply literal selected-branch base `mu_2` / height-one `(2)` control. Protected Kato gives the away-from-`(2)` part; protected Matsuno can propagate a known base `mu_2=0` through twists but assumes that base input.

After the `(2)` exponent is solved, the route still owes exact:

1. Greenberg/ordinary -> primitive Kummer comparison at `2`;
2. imprimitive -> primitive comparison at bad primes;
3. rank-one specialization to `Fitt^1(X_E)`;
4. analytic normalization to WP00.

### Route 3 — auxiliary imaginary quadratic `K` — admissible but longer

Protected WP09 supplies `K` with every prime dividing `2N` split and gives corrected p-adic Gross-Zagier applicability. Protected WP06 removes local descent defects at those split places.

A K-side theorem still owes:

- integral rank-one `p=2` Fitting/primitivity over `K`;
- exact global `I_n/Q_n` and plus/minus descent accounting where relevant;
- rank-zero twist contribution or an exact retained twist defect;
- exact p-adic-height/p-adic-derivative -> WP00 complex normalization.

Thus it remains admissible, but it has more independent interfaces than a native direct-Q first-Fitting theorem.

## Conditional closure theorem `BSD-A1-WP19-CLOSE-001`

Assume the nominated theorem

`Fitt^1_{Z_2}(X_E) = 2^{delta_2(E)} Z_2`

holds uniformly for every curve in the protected selected class.

Then `BSD-R2-A1` holds uniformly for that class.

### Proof

Protected WP19 gives

`Fitt^1_{Z_2}(X_E)=Fitt^0_{Z_2}(T_E)`.

Protected WP16B gives

`v_2(Fitt^0_{Z_2}(T_E))
 = len_{Z_2} Sha(E/Q)[2^infinity]`.

Taking `v_2` of the nominated theorem gives

`delta_2(E)=v_2(Fitt^1_{Z_2}(X_E))`.

Substitute the protected first-Fitting equality and the WP16B length identity:

`delta_2(E)=len_{Z_2} Sha(E/Q)[2^infinity]`.

Protected WP15/WP16A identify this equality with the selected rank-one `2`-primary BSD target. Therefore `BSD-R2-A1` follows. QED.

No further source, local-condition, descent, or normalization premise is hidden in this conditional deduction: all such obligations are requirements of the nominated theorem itself.

## Exact stopping boundary

WP19 can complete the representation reduction and theorem nomination from protected inputs. It cannot manufacture evidence for F1-F6 merely by restating them.

If no admitted source supplies the nominated theorem and no proof is constructed, the legitimate substantive boundary is

`MISSING_P2_RANK1_PRIMITIVE_FIRST_FITTING_RECIPROCITY_THEOREM`.

At that boundary the next work is genuine new theorem construction, not additional atlas expansion or generic literature screening.

## Claim firewall

- The conditional closure theorem is not an unconditional proof of `BSD-R2-A1`.
- Odd-prime strong Fitting theorems are design templates only at `p=2`.
- `Fitt^1(X_E)` is proved equivalent to the protected torsion invariant; its analytic evaluation is still missing uniformly.
- No MATHCERT certification is invoked.
