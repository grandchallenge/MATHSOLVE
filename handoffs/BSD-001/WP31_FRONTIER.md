# BSD-001 — WP31 frontier

## Protected predecessor

WP30 is protected at

`grandchallenge/MATHSOLVE@2049332f1df605563b5bb155a93d3fc16fb8e7bb`.

Its source authority is protected at

`grandchallenge/MATHFORGE@5b07785c9ca96ec0c2003bbe3ada46c807e50882`.

WP30 closes the twist/unit-root convention ambiguity by proving

`u=alpha`

under the shared Frobenius-substitution convention.

## WP31 result

WP31 composes the already admitted Hall finite-layer norm theorem with protected WP28–WP30 and proves that the remaining infinite formal universal-norm class stabilizes at the single finite layer

`n=m_2=ord_2(3-a_2) in {1,2}`.

Thus:

- if `a_2=+1`, a quadratic local layer suffices;
- if `a_2=-1`, a quartic local layer suffices.

At that layer, Hall's Snake-Lemma construction is written elementwise.

For the toroidal representative `v=k(z_form(P))`, choose a finite-layer norm lift `y`. Then

`(phi-alpha)y`

lies in the kernel of the norm map. Hall's explicit injection

`i_n(g)=[pi^{g-1}]`

recovers a unique Galois element `g_n(P;y)`. Its class modulo `(1-alpha)G_n` is independent of `y` and represents the toroidal formal class up to the harmless inversion convention of the connecting homomorphism.

Choosing a generator of `G_{m_2}` gives a finite exponent

`c_tw(P) mod 2^{m_2}`,

defined up to multiplication by an odd unit, and WP31 proves

`tau_form(P)=min(m_2,ord_2(c_tw(P)))`.

The complete possibilities are therefore:

- `a_2=+1`: `c_tw(P) mod 2`;
- `a_2=-1`: `c_tw(P) mod 4`.

No infinite-tower calculation above this finite layer is needed for D1b.

## Active D1b boundary

The former boundary

`MISSING_P2_TOROIDAL_FORMAL_COORDINATE_CONGRUENCE_DEPTH`

is refined to

`MISSING_P2_FINITE_TWISTED_RECIPROCITY_EXPONENT`.

A successor should not rebuild Hall's quotient, re-prove `u=alpha`, or resume broad universal-norm screening.

The next useful operation must do one of the following:

1. evaluate `c_tw(P)` from exact local coordinates of the saturated global generator, uniformly or by an exact computable criterion; or
2. compare `c_tw(P)` exactly with another protected **integral** invariant that determines its class modulo `2` or `4`.

Potential routes must preserve integral `2`-power information. Rational Iwasawa-cohomology universal-norm results that tensor with `Q_2` do not qualify because they erase the finite datum measured here.

## Parallel obligations unchanged

The following remain open and separate:

- D1a `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2 `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

Do not identify the finite twisted-reciprocity exponent with the WP20 Bockstein, a regulator, a formal logarithm, or an analytic interpolation factor without a separate exact theorem.

`BSD-R2-A1` remains `SELECTED_RESEARCH_TARGET_UNPROVED`.

No MATHCERT promotion is authorized by WP31.
