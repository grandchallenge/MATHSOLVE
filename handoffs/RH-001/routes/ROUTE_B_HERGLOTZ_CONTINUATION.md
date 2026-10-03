# RH-001 Forward Route B — Herglotz continuation of the parity theorem

Status: ACTIVE_PARALLEL_ROUTE

Coordination tracker:
grandchallenge/MATHSOLVE#412

Route role: transport the already-proved local simple-even theorem by controlling two scalar/spectral continuation margins rather than extending the small-a perturbation argument incrementally.

Current protected campaign head at pack creation:
grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c

## 1. Mission

Use the protected rank-one odd-sector decomposition to prove that the strict parity gap persists beyond the current explicit local interval.

The preferred output is a quantitative continuation theorem for the two margins

d(a)
=
inf sigma(B_{a,-}) - epsilon_+(e^a),

and

Delta_H(a)
=
1/2
-
<S_a,(B_{a,-}-epsilon_+(e^a))^{-1}S_a>,

on the region d(a)>0.

Protected RH-R041 gives the exact sign criterion. Protected RH-R043 gives continuity. The missing step is quantitative variation control strong enough to prevent either margin from reaching zero over a nontrivial interval.

## 2. Why this route exists

Route A proves simple-evenness directly by perturbative/variational estimates near a=0.

Route B exploits a different structure: the odd pole term is exactly rank one.

The protected decomposition is

A_{a,-}
=
B_{a,-}
-
2|S_a><S_a|.

Let

mu(a)=epsilon_+(e^a),

beta_-(a)=inf sigma(B_{a,-}),

d(a)=beta_-(a)-mu(a).

Whenever d(a)>0, define

m(a)
=
<S_a,(B_{a,-}-mu(a))^{-1}S_a>,

and

Delta_H(a)=1/2-m(a).

Protected RH-R041 proves the exact trichotomy:

Delta_H(a)>0
iff
epsilon_+(e^a)<epsilon_-(e^a),

Delta_H(a)=0
iff
the parity gap closes,

Delta_H(a)<0
iff
the odd sector lies below the even ground,

provided d(a)>0.

It also proves the quantitative lower bound

g(a)
=
epsilon_-(e^a)-epsilon_+(e^a)
>=
2 d(a) Delta_H(a)

when both margins are positive.

This turns continuation into a two-margin problem.

## 3. Protected lineage to context-load

Read:

- handoffs/RH-001/README.md
- work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- work_packages/RH_R041_ODD_HERGLOTZ_GAP_CRITERION.md
- work_packages/RH_R042_PARITY_BOTTOM_PARAMETER_CONTINUITY.md
- work_packages/RH_R043_HERGLOTZ_MARGIN_CONTINUITY.md
- work_packages/RH_R044_EXPLICIT_INITIAL_HERGLOTZ_MARGINS.md
- work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- work_packages/RH_R051_RANK_ONE_COERCIVITY_EXTENSION.md
- work_packages/RH_R052_REFRESHED_HERGLOTZ_MARGINS.md
- MATHFORGE@f9aa9ad64812df42ad079958ecff88c84e0e4648:
  reports/discovery/rh_001/rh_r041_pole_resolvent_interface.md
- MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:
  reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md
- AGENTS.md

Protected theorem identities of particular importance:

- RH-R041: exact Herglotz trichotomy and gap lower bound.
- RH-R042: continuity of epsilon_+ and epsilon_-.
- RH-R043: continuity of beta_-, d, and Delta_H on the pole-localized region; first failure is d=0 or Delta_H=0.
- RH-R044: explicit positive initial d and Delta_H margins on an earlier interval (a<=2/15).
- RH-R051: direct simple-even theorem through a=178/1000.
- RH-R052: refreshed explicit positive initial d and Delta_H margins through a=178/1000.

RH-R052 has refreshed R044's explicit quantitative Herglotz margins to the full R051 endpoint a=178/1000, establishing d(a) > 55428698889/23675000000000 and Delta_H(a) >= 1210515093544258/12367528439608125 > 0.

## 4. Fixed-Hilbert-space normalization

Use the protected scaling to L2(-1,1).

The scaled odd pole vector is

s_a(t)
=
sqrt(a) sinh(a t/2).

The pole-free odd operator and full operator are related by

A_tilde_{a,-}
=
B_tilde_{a,-}
-
2|s_a><s_a|.

The relevant scalar is

m(a)
=
<s_a,(B_tilde_{a,-}-mu(a))^{-1}s_a>.

Do not drop the a-dependence of s_a.

Do not define the inverse when d(a)<=0.

## 5. Immediate high-value contribution: refresh the initial margins

R044 gave explicit d/Delta_H bounds only through an earlier endpoint (a<=2/15).

RH-R052 has fully discharged this task through the current simple-even frontier:

a_0 = 178/1000 = 89/500,

establishing the explicit protected pair:

d(a) > 55428698889 / 23675000000000 > 0,

and

Delta_H(a) >= 1210515093544258 / 12367528439608125 > 0,

uniformly across 0 < a <= 178/1000.

This advances the initial continuation base from a=2/15 to a=178/1000, reducing the remaining distance to the prime threshold a=(1/2)log 2 by 21%.

## 6. Preferred continuation theorems

### B1. Local Lipschitz bounds for sector bottoms

Prove explicit bounds of the form

|mu(a)-mu(b)| <= C_mu |a-b|,

|beta_-(a)-beta_-(b)| <= C_beta |a-b|

on a compact interval.

Then

d(a)
>=
d(a_0)
-
(C_mu+C_beta)|a-a_0|.

This alone can preserve pole localization over a certified interval.

Possible tools:

- min-max with explicit form differences;
- bounded-form perturbation estimates;
- piecewise estimates between prime-entry thresholds.

### B2. Quantitative resolvent variation

On d(a)>=delta>0, use the resolvent identity to bound

||(B_{a,-}-mu(a))^{-1}
-
(B_{b,-}-mu(b))^{-1}||,

or a weaker bound sufficient for the scalar matrix element m(a).

A norm-resolvent theorem is not required if a direct quadratic-form or scalar resolvent estimate closes.

### B3. Direct Delta_H variation

Differentiate or compare

m(a)
=
<s_a,R_a s_a>

piecewise on intervals where the form depends smoothly on a.

A useful bound is

|Delta_H(a)-Delta_H(b)|
<=
C_H |a-b|.

Combined with refreshed initial Delta_0, this yields a continuation interval.

### B4. Prime-threshold crossing

This route is especially attractive near and beyond

a=(1/2)log2,

because it can, in principle, handle the arithmetic term as a bounded perturbation rather than rebuilding the entire local variational proof.

However:

- do not assume differentiability across a prime-entry threshold;
- treat thresholds piecewise;
- prove continuity/one-sided bounds at entry;
- account for every new prime power explicitly.

Crossing the first prime threshold is a major target.

## 7. Structural warning: compressed translations

The scaled source form contains compressed translations whose shifts depend on a.

Translation is strongly continuous in shift, but not norm-continuous on the full ambient space in the naive sense.

Protected RH-R043 deliberately uses strong continuity plus local uniform resolvent bounds.

Do not silently upgrade that to norm continuity.

If a quantitative theorem needs operator-norm control, derive it for the actual compressed form/operator being used, or work directly at the form/quadratic level.

## 8. Structural warning: eigenvalue derivatives

The even ground is simple on the currently protected local interval, so a Feynman-Hellmann style formula may be available piecewise if the operator family has enough differentiability.

But do not assume:

- differentiability at prime-entry thresholds;
- differentiability of beta_- if the pole-free odd bottom is not simple;
- a globally smooth eigenvector branch.

Subgradient/min-max variation bounds may be safer than exact derivatives.

## 9. Minimum meaningful deliverable

A contribution is useful if it does at least one of:

1. refresh explicit d and Delta_H lower bounds at the current frontier (completed by RH-R052 through a=178/1000);
2. prove a quantitative Lipschitz/variation theorem for d;
3. prove a quantitative variation theorem for Delta_H;
4. use those estimates to extend the parity theorem to an explicit larger interval;
5. prove a rigorous obstruction showing why one of these quantitative strategies cannot close.

Prefer reusable scalar/operator inequalities over another local endpoint micro-tuning.

## 10. Anti-loop directives

Do not return to finite Galerkin evidence unless it directly supplies a rigorously enclosed bound for d or Delta_H.

Do not attempt to prove global monotonicity merely because a finite plot looks monotone.

Do not import the rejected Krein-Rutman argument from R038.

Do not import secondary Andrade inertia/Perron claims unless independently source-audited and proved.

The route should remain anchored to the protected R041 rank-one identity.

## 11. Governance and stop conditions

MATHSOLVE owns theorem development.

Use MATHFORGE if:

- a new external theorem or paper is needed;
- a claimed Loewner/Herglotz monotonicity theorem is to be imported;
- the route crosses into a source claim not already protected.

Stop and name the boundary if:

- d reaches zero;
- the inverse in Delta_H ceases to exist;
- a source normalization conflict appears;
- a prime-threshold formula is ambiguous;
- the next step would require claiming RH or global simple-evenness without proof.

## 12. Completion criterion for Route B

Route B closes its main objective if it supplies a protected continuation theorem carrying positive d and Delta_H across a substantial parameter range, ideally through the first prime threshold and onward.

An individual agent contribution is complete when it produces one protected quantitative margin theorem, one protected explicit extension, or one protected obstruction result.

## 13. Zero-context handoff prompt

The copy-ready prompt is stored at:

handoffs/RH-001/routes/prompts/ROUTE_B_ZERO_CONTEXT.txt
