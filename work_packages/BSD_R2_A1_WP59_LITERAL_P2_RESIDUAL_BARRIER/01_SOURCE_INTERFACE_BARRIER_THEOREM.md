# WP59 theorem — bounded source-interface barrier at literal p=2

## 1. Protected arithmetic state

Work on the protected selected `BSD-R2-A1` lane at MATHSOLVE

`55434c50ae05c3bdb66f329ee15d4ece4534d4fd`.

Protected WP58A proves, for its explicit optimal-composite modular parametrization,

`(A)
 delta_2(E)
 = 1 + 2 ord_2(m_K(f))
   - ord_2(c_infinity(E^D))
   - ord_2(lambda_D)
   - sum_{ell|N} ord_2(c_ell)`,

where

`lambda_D=L(E^D,1)/Omega(E^D) in Q^x`.

The remaining substantive D2d term is therefore

`R_2(E,K,f) := 2 ord_2(m_K(f)) - ord_2(lambda_D)`.

A theorem determining the two summands separately is sufficient but not necessary; an exact theorem for their combination is admissible.

## 2. Protected source screen

Protected MATHFORGE WP59 at

`c8af223d0e05f999b4977a0dae5b1b5281eff93e`

records a bounded source/applicability screen. Its disposition is

`QUALIFIED_NO_CURRENT_ADMITTED_LITERAL_P2_RESIDUAL_CLOSURE`.

The protected screen is deliberately not a claim of literature exhaustiveness or mathematical impossibility.

## 3. Route-barrier proposition

### Proposition `BSD-A1-WP59-SOURCE-BARRIER-001`

From the source interfaces currently protected in MATHFORGE and the mathematical hypotheses currently protected for `BSD-R2-A1`, there is no valid inference that determines `R_2(E,K,f)` uniformly for the selected class.

**Status:** `PROVED_FROM_ADMITTED_SOURCE_INTERFACES`.

### Proof

The candidate routes represented in the protected source interfaces fall into the following exhaustive classes **within the bounded WP59 screen**.

#### (i) Integral Iwasawa/main-conjecture control

Protected WP17B records that Kato's literal-`p=2` theorem controls the ordinary characteristic information away from the height-one prime containing `2`; the integral clauses needed to include that prime impose `p != 2`.

Therefore the admitted Kato interface does not determine the missing height-one-`(2)` exponent. A proof of `R_2` cannot cite Kato alone for that exponent.

The modern uniform good-ordinary main-conjecture candidates screened in WP59 retain an odd-prime standing assumption, so they also cannot be specialized to the selected literal-`2` branch.

#### (ii) Standard Heegner primitivity

Protected WP10 already proves that the screened odd-prime rank-lowering/primitivity mechanism does not mechanically specialize to `p=2`.

Thus the protected odd-prime Heegner-index formula cannot be substituted into `(A)`.

#### (iii) Kriz–Li literal-2 congruences

Kriz–Li do supply a genuine literal-`2` Heegner-point mechanism. The source interface, however, requires an additional mod-`2` logarithmic nonvanishing hypothesis `(star)` on the chosen Heegner point.

The protected selected hypotheses and protected WP09 auxiliary-field theorem do not contain `(star)`, and no admitted theorem currently proves that a WP09 field may always be chosen to satisfy `(star)` simultaneously with all protected local splitting and nonvanishing conditions.

Hence this route is conditional on an additional unproved premise and does not yield a uniform deduction of `R_2`.

#### (iv) Exact or sharp quadratic-twist central-value results

The screened exact-family results of Zhai and of Adachi–Nomoto–Shii either provide only a lower bound in general or require a finite rank-zero/nonzero central-value seed for the exact propagation mechanism.

For the protected selected base curve,

`L(E,1)=0`

because the analytic rank is one. Thus the base curve does not supply the required rank-zero seed, and no protected theorem supplies a substitute seed compatible with every selected curve and all WP09 local constraints.

The older modular-symbol nonvanishing results guarantee nonzero twists but do not determine the exact WP00-normalized `2`-adic valuation required in `(A)` under the simultaneous WP09 splitting conditions.

#### (v) Special families

Literal-`2` exact theorems for CM curves, congruent-number curves, rational-`2`-torsion families, or other special classes have hypotheses not implied by `BSD-R2-A1`, whose residual `E[2]` is irreducible.

They therefore cannot serve as a uniform theorem for the selected class.

These cases cover the routes admitted in the bounded WP59 source screen. Each route lacks at least one premise required to infer `R_2(E,K,f)` under the protected selected hypotheses. Consequently no currently admitted source interface entails the desired uniform value. QED.

## 4. What the proposition does not say

Proposition `SOURCE-BARRIER-001` is a statement about the current admitted implication graph, not about mathematical truth.

It does not assert:

- that `R_2(E,K,f)` is indeterminate in principle;
- that no theorem proving it exists in the literature;
- that no new theorem can be proved;
- that the two residual valuations must be solved separately;
- that Kriz–Li's `(star)` condition cannot be forced by a stronger auxiliary-field theorem;
- that D1c or D2a cannot indirectly produce the missing comparison.

## 5. Exact reopening criteria

The source barrier is discharged by any protected theorem/source interface that supplies at least one of the following.

### R1 — literal-p=2 Heegner index

An exact theorem determining

`ord_2(m_K(f))`

for the protected selected class and a WP09-compatible auxiliary field.

### R2 — exact twist L-ratio

An exact theorem determining

`ord_2(lambda_D)`

with the WP00 whole-real-period normalization while permitting the protected simultaneous local constraints on `D_K`.

### R3 — force the Kriz–Li hypothesis

A theorem proving that, for every selected curve, a WP09-compatible field can be chosen so that the exact Kriz–Li mod-`2` Heegner-log condition holds, together with normalization compatibility sufficient to identify `m_K(f)`.

### R4 — combined residual theorem

A direct theorem determining

`R_2(E,K,f)
 = 2 ord_2(m_K(f)) - ord_2(lambda_D)`

without separately computing the two terms.

### R5 — genuine height-one-(2) integral reciprocity

A literal-`p=2` integral main-conjecture/reciprocity theorem controlling the height-one prime `(2)` and specializing to the protected primitive determinant line strongly enough to identify the left-hand side of `(A)`.

Any one of R1–R5 reopens D2d immediately.

## 6. Named boundary

The exact current D2d theorem/source boundary is

`MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.

This refines but does not mathematically enlarge the previous

`MISSING_P2_HEEGNER_INDEX_AND_TWIST_LRATIO_VALUATION_CONTROL`.

## 7. Parallel routes remain live

The following boundaries are independent enough to continue without violating this source barrier:

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.

A resolution of either may supply R5 or another combined route and must therefore trigger a fresh D2d replay.

D2e remains downstream of D2d and must not be replayed as if the missing residual had vanished.

## 8. Firewall

WP59 does not prove `BSD-R2-A1`, does not promote a conditional literature theorem to the selected class, does not assign a guessed `2`-adic valuation, does not claim literature exhaustiveness, and does not certify any theorem in MATHCERT.
