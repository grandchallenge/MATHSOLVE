# RH-001 Forward Route A — Local analytic continuation of the simple-even theorem

Status: ACTIVE_PARALLEL_ROUTE

Route role: extend the explicit full-operator simple-even interval beyond the current protected endpoint without relying on finite-Galerkin positivity.

Current protected campaign head at pack creation:
grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c

Current protected route frontier:
RH-R050-TRIAL-REWEIGHTED-EXTENSION-001
work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md

## 1. Mission

Prove a strictly larger explicit interval

0 < a = log(lambda) <= a_1

with

a_1 > 171/1000,

on which the full localized Weil operator has:

1. a strict even-below-odd parity gap;
2. a simple lowest even-sector eigenvalue;
3. hence a simple-even global ground state by RH-R036.

This route is theorem development on the actual infinite-dimensional localized Weil operator. It is not a finite-matrix extrapolation route.

A successful contribution need not prove the best possible endpoint. A clean new inequality, coercivity lemma, trial-space theorem, or remainder estimate that materially increases the certified budget is a meaningful route contribution.

## 2. Why this route exists

The Connes–Consani–Moscovici Zeta Spectral Triples construction requires a simple-even minimal eigenspace for the localized Weil form.

The campaign reduced that condition in RH-R036 to:

- simplicity of the lowest even eigenvalue;
- strict parity ordering epsilon_+(lambda) < epsilon_-(lambda).

Suzuki's full-operator small-a analysis supplied the qualitative mechanism. R040 made it effective. R045 through R050 progressively improved the analytic certificate.

The current protected theorem R050 proves the full simple-even statement for

0 < a <= 171/1000.

The current protected lower bounds at the endpoint are:

epsilon_-(lambda) - epsilon_+(lambda)
>
775974967 / 3355931250000,

and

epsilon_{+,2}(lambda) - epsilon_{+,1}(lambda)
>
12508575979 / 71025000000.

The parity-gap budget is now much tighter than the even internal-gap budget. Further microscopic retuning of the same one-parameter quadratic trial is explicitly not the preferred direction.

## 3. Protected lineage to context-load

Read these before changing mathematics:

- handoffs/RH-001/README.md at protected main.
- work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- work_packages/RH_R040_EFFECTIVE_SMALL_A_SIMPLE_EVEN.md
- work_packages/RH_R045_PARITY_SENSITIVE_REMAINDER.md
- work_packages/RH_R046_ODD_LOWER_BOUND_EXTENSION.md
- work_packages/RH_R047_INTEGRATED_REMAINDER_EXTENSION.md
- work_packages/RH_R048_SECTOR_COERCIVITY_EXTENSION.md
- work_packages/RH_R049_HIGHER_ODD_COERCIVITY.md
- work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- MATHFORGE@d722e6a27edbb66f6ae7ef08dd36f79b00b4b320:
  reports/discovery/rh_001/rh_r040_small_a_parity_transfer.md
- AGENTS.md

Do not infer current protected main from the SHA recorded in this pack. Re-fetch live protected state before mutation. The SHAs above identify protected mathematical predecessors.

## 4. Core objects and normalization

Use

a = log(lambda).

After scaling to L2(-1,1), the localized Weil form has the protected decomposition used in R040-R050:

scaled form
=
common scalar shift
+
limiting closed form
+
smooth no-prime remainder.

Parity reduces the operator into even and odd sectors.

The present protected route remains inside the no-prime regime. The first prime term enters when

2a = log 2.

Therefore any attempt to cross

a = (1/2) log 2

is a material regime change. Do not silently reuse the no-prime formulas beyond that threshold.

The protected R050 proof currently uses:

- increasingly sharp limiting odd-sector coercivity from positive terms of the logarithmic potential;
- a lower bound for the second even limiting eigenvalue;
- a positive even trial function for an upper bound on the even ground energy;
- parity-sensitive control of the smooth remainder kernel q(t);
- exact rational endpoint arithmetic.

## 5. Preferred contribution classes

### A1. Richer positive even trial space

The highest-value direct improvement is a genuinely richer trial family, not another tiny retuning of one quadratic coefficient.

Examples:

- positive quartic or sextic polynomials;
- a two- or three-dimensional analytic Ritz space with a rigorously controlled positive trial vector;
- a basis adapted to the limiting form rather than ordinary monomials.

Requirements:

- positivity where positivity is used;
- exact or rigorously bounded form integrals;
- no numerical optimizer as proof;
- certified endpoint inequalities in closed form or exact rational bounds.

A useful output is a theorem that gives a better upper bound on the even ground state as a function of a.

### A2. Stronger odd-sector coercivity

R046-R050 improve the odd sector by retaining positive terms in the logarithmic-potential expansion and weighted Cauchy estimates.

A structural improvement is preferable to merely retaining one more Taylor term.

Promising directions include:

- an exact weighted Hardy/Poincare inequality for the odd limiting form;
- a sharper lower bound for the Hilbert-kernel contribution;
- optimizing the Cauchy weight analytically;
- using the complete logarithmic potential rather than a finite truncation.

A useful output is an improved explicit lower bound for mu_{-,1} with a transparent proof.

### A3. Sharper smooth-remainder control

The protected q(t) analysis has moved from uniform pointwise bounds to integrated envelopes.

Meaningful improvements include:

- a sharper certified upper bound on q'(t);
- a parity-specific operator bound smaller than the current generic Lipschitz budget;
- an exact convexity/monotonicity statement for q on a larger interval;
- a higher-order cancellation estimate in the odd or even reduced kernels.

The goal is not to enlarge the t interval alone. The resulting operator error must improve the spectral budget.

### A4. Combined coercivity/trial theorem

A clean combined theorem that balances A1-A3 and yields one larger explicit endpoint is fully admissible.

## 6. Minimum meaningful deliverable

A route contribution should do at least one of:

1. prove a new full simple-even interval with endpoint strictly above 171/1000;
2. prove a reusable stronger even or odd limiting-sector inequality;
3. prove a reusable sharper parity-sensitive remainder theorem;
4. rigorously show that a proposed continuation mechanism cannot improve the current endpoint and identify the exact obstruction.

For an endpoint theorem, retain:

- the exact interval;
- explicit positive lower bounds for the parity gap and even internal gap;
- the no-prime threshold check;
- exact source/protected dependencies;
- a false-proof firewall;
- claim boundaries;
- canonical handoff update.

## 7. What is not evidence

Do not use any of the following as proof of a larger interval:

- finite Galerkin gaps alone;
- ordinary floating-point eigenvalues;
- symbolic optimizer output without exact verification;
- plots of q or spectral margins;
- numerical minimization of a trial coefficient;
- extrapolation from R039;
- the fact that all previous endpoint extensions succeeded.

Numerics are permitted for reconnaissance only. Convert any selected candidate into an exact inequality before promotion.

## 8. Anti-loop directives

Do not spend a tranche on a negligible one-parameter retuning unless it creates a mathematically reusable lemma.

Before opening a new work package, ask:

- Does this add a new coercivity mechanism?
- Does this add a richer analytic trial space?
- Does this reduce a protected error term structurally?
- Does it cross or clarify a meaningful threshold?

If all answers are no, redirect to Route B.

## 9. Regime-change boundary

The no-prime analysis is valid only while

2a < log 2.

If a candidate theorem approaches or crosses the first prime-entry threshold:

1. stop reusing the no-prime formula;
2. source-audit the first prime contribution exactly;
3. create a new work package that explicitly includes the p=2 term;
4. re-derive parity and remainder estimates with that term present.

Crossing the prime threshold is a legitimate major milestone, not an automatic continuation.

## 10. Governance and claim boundary

MATHSOLVE owns theorem development.
MATHFORGE owns new source/prior-art claims.
MATHCERT is not needed for ordinary route progress.

Never claim:

- RH;
- determinant convergence to Xi;
- all-a simple-evenness;
- positivity at the R039 large-a test points;
- novelty or priority;
- publication readiness;

unless a separate governed process establishes it.

## 11. Recommended first actions for a new agent

1. Read AGENTS.md.
2. Re-fetch protected main.
3. Read the canonical RH handoff.
4. Read R048-R050 in full.
5. Recompute the R050 endpoint margins independently.
6. Identify whether the parity budget is dominated by:
   - odd limiting coercivity;
   - even ground upper bound;
   - smooth remainder.
7. Choose one structural improvement only.
8. Open a bounded issue and branch from current protected main.
9. Prove the improvement with exact arithmetic.
10. Run non-authoring Adversary and Referee passes.
11. Compose onto the then-current protected head before using CI as merge evidence.

## 12. Completion criterion for Route A

Route A is not globally complete until either:

- simple-evenness is carried through all parameter values required by the CCM limiting construction; or
- another route makes that global extension unnecessary for the terminal RH bridge.

For an individual agent, completion means one protected theorem or one protected negative/obstruction result that materially advances the explicit analytic frontier.

## 13. Zero-context handoff prompt

The copy-ready prompt is stored separately at:

handoffs/RH-001/routes/prompts/ROUTE_A_ZERO_CONTEXT.txt
