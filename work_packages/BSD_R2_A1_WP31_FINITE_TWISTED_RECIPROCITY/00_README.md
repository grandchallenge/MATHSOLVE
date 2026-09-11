# BSD-R2-A1-WP31 — finite-layer twisted-reciprocity evaluation

## Metadata

- Campaign: `BSD-001`.
- Work package: `BSD-R2-A1-WP31-FINITE-TWISTED-RECIPROCITY`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Protected MATHSOLVE baseline: `2049332f1df605563b5bb155a93d3fc16fb8e7bb`.
- Protected MATHFORGE source authority: `5b07785c9ca96ec0c2003bbe3ada46c807e50882`.
- Claim state: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Certification state: unchanged; no MATHCERT promotion.

## Purpose

Protected WP29 reduced the remaining place-`2` formal universal-norm uncertainty to the canonical truncated toroidal depth

`tau_form(P)`.

Protected WP30 then removed the auxiliary twist convention by proving

`u=alpha`

and therefore

`(1-u)Gamma_2=(1-alpha^(-1))Gamma_2`.

WP31 asks the next non-lateral question:

> Can the infinite-tower toroidal class be evaluated by an explicit finite-layer twisted-reciprocity computation?

The answer is yes.

## Result

Let

`m_2=ord_2(3-a_2) in {1,2}`.

For the degree-`2^n` local cyclotomic layer `L_n/Q_2`, put

`G_n=Gal(L_n/Q_2)`.

Hall's admitted finite-layer theorem and protected WP30 give

`Ehat(2Z_2)/N_{L_n/Q_2}Ehat(O_{L_n}) ~= G_n/(1-alpha)G_n`.

The right side has order

`2^{min(n,m_2)}`.

The protected infinite formal quotient has order `2^{m_2}`. Hence the natural projection from the infinite universal-norm quotient to the finite quotient is an isomorphism for every `n>=m_2`. In particular, `n=m_2` suffices.

WP31 then writes Hall's Snake-Lemma connecting map elementwise. For the toroidal representative `v=k(z_form(P))`, choose a finite-layer norm lift `y`. Applying `phi-alpha` sends `y` into Hall's explicit norm kernel. Invert Hall's injection

`i_n(g)=[pi^{g-1}]`

to obtain a Galois element `g_n(P)`. Its class modulo `(1-alpha)G_n` is independent of the norm lift and represents the protected toroidal class, up to the harmless conventional inversion of the Snake connecting map.

At the stabilization layer `n=m_2`, choose a generator `sigma` of `G_{m_2}` and write

`g_{m_2}(P)=sigma^{c(P)}`.

Then

`tau_form(P)=min(m_2,ord_2(c(P)))`.

Thus the remaining infinite-tower local datum is reduced to one explicit finite exponent modulo `2` or `4`.

## Concrete finite cases

If `a_2=+1`, then `m_2=1` and only a quadratic layer is needed:

- `c(P)=1 mod 2` gives `tau_form(P)=0`;
- `c(P)=0 mod 2` gives `tau_form(P)=1`.

If `a_2=-1`, then `m_2=2` and only a quartic layer is needed:

- `c(P)` odd gives `tau_form(P)=0`;
- `c(P)=2 mod 4` gives `tau_form(P)=1`;
- `c(P)=0 mod 4` gives `tau_form(P)=2`.

## Why this is a strict reduction

WP29 represented the class in an infinite pro-`2` quotient. WP31 proves that the class stabilizes at a finite layer of degree at most four and gives the exact connecting-map procedure that computes its exponent there.

This does not assign a uniform value to that exponent. It changes the remaining task from an infinite universal-norm problem to a finite local reciprocity calculation.

## Source discipline

No new external theorem is imported. WP31 composes only:

- the already admitted Hall/Lubin-Rosen finite-layer toroidal norm theorem and its explicit commutative diagram;
- protected WP28 finite formal quotient size;
- protected WP29 toroidal depth;
- protected WP30 `u=alpha` normalization.

Laurent Berger's 2026 universal-norm note was screened during reconnaissance but is not used because its Iwasawa-cohomology statements are `Q_p`-linear and therefore do not retain the finite integral `2`-power datum measured by `tau_form(P)`.

## Claim firewall

WP31 does not prove a value of `tau_form(P)`, a formal logarithm formula, a Bockstein/regulator identity, an analytic determinant theorem, D1a, D1c, D2, `BSD-R2-A1`, or certification.
