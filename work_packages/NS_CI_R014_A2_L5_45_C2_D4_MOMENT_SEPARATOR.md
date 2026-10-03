# NS-CI-R014-A2-L5-45 — D4 moment separator and narrowed reconstruction residual

## Disposition

- Campaign: NS-CI-001
- Restricted target: NS-CI-R014-A2
- Tracker: MATHSOLVE#59
- Protected mathematical predecessor: L5-44 critical second-moment density balance
- Evidence source: independent contribution NSCI-C2-B-COOP-001
- Evidence raw SHA-256: 3a86149e1cfac0ea3dc6ec1e43a4efeb19e7745b5e2ab011b3606de9583bb2f9
- Adjudication: PARTIAL_ADMISSION__D4_ALONE_ROUTE_REFUTED_AT_MOMENT_INTERFACE
- Result class: exact moment-interface separator plus physical-order audit
- Result: D4_ALONE_DOES_NOT_FORCE_FIXED_CRITICAL_BAND_MASS__TIGHTNESS_OR_LOWER_MOMENT_REQUIRED
- A2 theorem: open
- L5: active
- MATHCERT adjudication: absent

## 1. Starting point

L5-44 gives the exact compression ledger

    C2^- = Q2(S) + C2^+ - P_tot + 2 D4,

where

    D4 = integral_0^S Q4(s) ds.

The open question was whether a large positive D4 term could itself be converted
into a fixed physical selector charge.

## 2. Exact moment-interface separator

Fix

    S > 0,
    K > 0,
    0 < c_- < c_+ < infinity.

Choose a nonnegative integrable profile w on [0,S] satisfying

    w(0) = 0,
    integral_0^S w(s) ds = 1.

For sufficiently large lambda > c_+, define

    delta_lambda(s) = K w(s) / lambda^4

and the probability measure

    mu_s^(lambda)
      = (1-delta_lambda(s)) delta_0
        + delta_lambda(s) delta_lambda.

For large lambda, 0 <= delta_lambda <= 1. Its moments are

    M0(s) = 1,

    Q4(s) = K w(s),

    D4 = integral_0^S Q4(s) ds = K,

    Q2(s) = K w(s) / lambda^2.

Moreover,

    mu_s^(lambda)([c_-,c_+]) = 0

for every s, because its support is {0,lambda} with lambda > c_+.

Thus

    sup_s Q2(s) -> 0

as lambda -> infinity, while D4 remains fixed and positive.

The choice w(0)=0 also gives Q2(0)=0, matching the protected moment-level
initialization.

Therefore:

    positive D4
    + finite positive M0
    does not imply
    fixed-annulus mass
    or a positive Q2 lower bound.

This is an exact obstruction at the moment-reconstruction interface.

## 3. Scope of the separator

The separator is not a realization theorem for the full L5-35 characteristic
system.

The protected packet variables J, H, and R obey coupled dynamics. No theorem
here constructs a packet trajectory whose spectral measure is exactly
mu_s^(lambda).

Accordingly this result closes only the moment-only implication.

It does not prove that selected whole-space NSE dynamics can realize arbitrary
high-frequency escape of this form.

## 4. Physical-order audit

Under the established packet scaling,

    dt = h^2 / (nu N^2) ds,

and physical frequency corresponding to scaled frequency xi=hn is of order

    N h^(-1) xi.

With

    ||u||_2^2 ~ N^(-1) M0,

the second and fourth scaled moments correspond to

    ||grad u||_2^2 ~ N h^(-2) Q2,

    ||grad^2 u||_2^2 ~ N^3 h^(-4) Q4.

Hence

    nu integral ||grad u||_2^2 dt
      ~ N^(-1) integral Q2 ds,

while

    nu integral ||grad^2 u||_2^2 dt
      ~ N h^(-2) D4.

Thus D4 is one differential order above the finite Leray-Hopf dissipation
budget used in the selected problem. No direct finite Leray budget for D4
follows from the current inputs.

## 5. Consequence for the compression ledger

The L5-44 balance remains exact, but the D4 branch is now classified.

Large D4 cannot be converted into selector charge from sign and size alone.

Any successful use of the D4 channel must supply at least one additional
ingredient, such as:

- lower-moment control, especially a quantitative Q2 lower bound;
- spectral tightness preventing high-frequency escape;
- a correctly quantified relation among M0, Q2, and Q4;
- an equation-specific dynamical mechanism that forces such tightness.

## 6. Rejected stronger claim

The independent contribution proposed the ratio

    M0 Q4 / Q2^2 <= C_*

together with an upper envelope on Q4 as a necessary-and-sufficient missing
hypothesis.

That claim is not protected.

Necessity was not proved.

A sufficiency theorem also requires enough uniform normalization to produce
both fixed lower and upper frequency cutoffs on a positive-measure time set.
Those hypotheses must be stated exactly and then derived from selected packet
dynamics before the route can be used.

## 7. Updated live residual

C2-MIX-DIRECTION-COMPRESSION-LEDGER-CHARGE is narrowed to three live routes:

1. Q2/Q4 reconstruction:
   prove a sufficient positive-measure-time tightness lemma and derive its
   hypotheses from the selected dynamics;

2. expansion:
   control or sign C2^+ strongly enough that it cannot absorb persistent
   compression without paying a physical cost;

3. signed phase source:
   control or sign P_tot strongly enough that it cannot absorb persistent
   compression without paying a physical cost.

The D4-alone route is closed negatively at the moment interface.

## 8. Claim boundary

Protected disposition:

D4_ALONE_DOES_NOT_FORCE_FIXED_CRITICAL_BAND_MASS
__TIGHTNESS_OR_LOWER_MOMENT_REQUIRED

It proves:

- an exact high-frequency-escape separator at the moment interface;
- D4 alone cannot force fixed critical-band mass;
- D4 alone cannot force a Q2 lower bound;
- D4 is not directly the finite Leray-Hopf dissipation quantity under the
  supplied packet scaling.

It does not prove:

- packet realization of the separator;
- a selected whole-space NSE counterexample;
- a necessary-and-sufficient tightness criterion;
- control of C2^+, P_tot, or Q2(S);
- A2.

No MATHCERT, novelty, priority, publication, patent, product, or commercial
claim is asserted.

## 9. Next live obligation

Prove the smallest correct D4-plus-tightness/Q2 reconstruction lemma that yields
fixed critical-band mass on a positive-measure time set, with every mass and
moment normalization stated explicitly. Then audit which of those hypotheses
can actually be derived from the selected L5 packet dynamics.
