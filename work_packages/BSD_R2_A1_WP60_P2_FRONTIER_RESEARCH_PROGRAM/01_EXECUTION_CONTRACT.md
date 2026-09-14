# WP60 execution contract for Codex agents

## 1. Operating rule

Treat this file as an execution contract, not as mathematical authority. Protected repository state is authoritative. Re-fetch it before every mutation tranche.

A Codex agent assigned WP60 is authorized to continue autonomously through bounded proof work, source reconnaissance, source admission requests, exact computations, implementation, diagnostics, repair, replay, non-authoring audit passes, CI, protected merge, readback, issue maintenance, and handoff maintenance until:

- the bounded objective is completed; or
- a genuine theorem, source, governance, authority, authentication, safety, materially changed-state, or substantive evidentiary boundary is reached.

Recoverable connector, GitHub, compiler, Lean, Sage/PARI, package, CI, logging, or environment failures are not stopping conditions.

## 2. Mandatory startup sequence

Before modifying any repository:

1. fetch protected `main` for `grandchallenge/INTELLECT` and record the exact SHA;
2. fetch protected `main` for `grandchallenge/MATHSOLVE` and record the exact SHA;
3. if external mathematics is needed, fetch protected `main` for `grandchallenge/MATHFORGE` and record the exact SHA;
4. read `grandchallenge/MATHSOLVE/AGENTS.md` from the current protected head;
5. read `handoffs/BSD-001/README.md` and `handoffs/BSD-001/WP60_FRONTIER.md` from the current protected head;
6. read the current WP60 tracker `grandchallenge/MATHSOLVE#215` and campaign owner `#164` only as mutable operational records, not as theorem authority;
7. reject any stale branch, review, CI run, or artifact that does not bind to the current exact candidate head.

If protected state has advanced, reconcile the change before continuing. Do not silently replay a stale candidate against a new base.

## 3. Lane-selection rule

Choose the highest-value executable lane in this order:

1. WP60A, if an exact finite-level determinant construction/comparison can be advanced from protected machinery;
2. WP60B, if the Kriz–Li condition can be reduced, translated, or forced without assuming the desired Heegner-index parity;
3. WP60C, when exact computation can discriminate between competing proof hypotheses or produce a falsifiable local criterion;
4. D2a only if a materially new literal-`p=2` height theorem or proof mechanism is available.

Do not spend a tranche on a broad literature search that merely reproduces the WP59 screen.

## 4. WP60A execution contract

### A0 — dependency reconstruction

Build an exact dependency table for the primitive determinant line from protected WP16A/WP16B/WP19 and the literal-`p=2` comparison machinery through WP52A. Record:

- the exact modules/complexes;
- the exact determinant/Fitting ideals;
- every local condition at `2` and at bad primes;
- every finite correction already resolved;
- the precise location where the analytic generator is missing.

A0 is documentary but proof-critical. Do not proceed from slogans such as “main conjecture should imply it.”

### A1 — finite-level analytic object

Seek an integral finite-level analytic object whose specialization can be compared to the primitive Kummer determinant without first invoking the odd-prime-only all-height-one Iwasawa theorem.

Candidate sources include modular-symbol, zeta-element, Beilinson–Kato, explicit reciprocity, or finite-layer constructions, but any external theorem used at literal `p=2` must be admitted through MATHFORGE.

Required output: an exact object, coefficient ring, integrality statement, and specialization map.

### A2 — local-condition matching

Prove that the analytic object lands in or controls the exact protected primitive determinant line. Explicitly account for:

- ordinary versus primitive Kummer conditions at `2`;
- the two split places above `2` after passage to `K`, when applicable;
- primitive/imprimitive bad-prime factors;
- any exceptional zero, unit-root, or torsion term;
- the height-one prime `(2)` itself.

“No difference up to a unit” is insufficient unless the unit is proved odd and the theorem only needs valuation.

### A3 — exact determinant comparison

Derive an equality of determinant/Fitting ideals or a preferred generator identity strong enough to determine the missing height-one-`(2)` exponent.

Success means the result satisfies WP59 `R5` or directly determines `R_2(E,K,f)` as in `R4`.

### A4 — replay and promotion guard

On apparent success:

1. replay WP59's R1–R5 contract explicitly;
2. recompute the selected valuation identity from protected WP58A;
3. check that no power of `2` was hidden in a normalization change;
4. only then open the theorem PR that claims D2d reopened/resolved.

## 5. WP60B execution contract

### B0 — theorem statement normalization

Obtain the exact literal Kriz–Li theorem statement through an admitted source record if it is to be used as theorem authority. Record every hypothesis and the exact normalization of the `2`-adic logarithm.

### B1 — translate to the protected line

Write the condition entirely in WP00/WP09/WP38 notation. With

`P_K(f)=m_K(f)P+T`,

separate:

- fixed curve-local factors;
- the contribution of `m_K(f)`;
- genuinely `K`-varying data;
- any differential/period normalization.

The output must make circularity visible.

### B2 — anti-circularity decision

Classify the translated condition as one of:

- `INDEPENDENT_AUXILIARY_NONVANISHING`: enough genuinely varying information remains to seek a field-forcing theorem;
- `EQUIVALENT_TO_UNKNOWN_INDEX_PARITY`: the condition simply repackages the unknown parity of `m_K(f)`;
- `MIXED`: an independent local/global condition remains after isolating the unknown index parity.

If the second case holds, stop treating Kriz–Li as an independent route and record the reduction as a theorem-level negative result about strategy, not about BSD.

### B3 — field-forcing theorem

Only in the independent or mixed case, prove or source a theorem that a WP09-compatible imaginary quadratic field exists satisfying the exact mod-`2` condition simultaneously with all required splitting, discriminant, and nonvanishing constraints.

Success must satisfy WP59 `R3` literally.

### B4 — Heegner-index consequence

If the Kriz–Li hypothesis is forced, carry the theorem through the fixed source-compatible parametrization and show exactly what follows for `ord_2(m_K(f))`. Do not silently replace the fixed parametrization or generator.

## 6. WP60C execution contract

### C0 — admissible sample

Use only real elliptic curves satisfying the selected class:

- semistable;
- odd conductor;
- good ordinary at `2`;
- irreducible `E[2]`;
- analytic rank one.

Every curve must have a reproducible source identifier and verification record for each selection condition.

### C1 — admissible fields

Enumerate only actual imaginary quadratic fields satisfying all protected WP09 constraints. Record the discriminant, splitting at `2N`, and the exact nonvanishing condition used by WP09.

### C2 — exact computations

For each admissible pair `(E,K)` compute, as available and exactly enough to determine parity/valuation:

- the protected Heegner point or source-compatible image;
- the normalized `2`-adic logarithm entering the Kriz–Li condition;
- `m_K(f)` when independently computable;
- local reduction and formal-group invariants at `2`;
- WP36 finite norm class / `tau_form(P)` / `rho_2(P)` where available;
- Tamagawa valuations;
- selected modular-symbol or twist-L-ratio data where exact rational values are available;
- the truth value of the translated Kriz–Li condition.

### C3 — outputs

Commit:

- one deterministic runner with pinned dependencies or a repository-approved environment;
- machine-readable results (`.json` or `.csv`);
- a manifest containing exact input curve/field identifiers and software versions;
- a short mathematical analysis separating observations from conjectures.

No dummy data. No hand-entered numerical tables without a generator script.

### C4 — theorem-discovery criterion

The lane is useful only if it yields at least one of:

- a reproducible counterexample to a proposed uniform criterion;
- a finite local invariant perfectly correlating with the mod-`2` condition on the tested sample and worth proving;
- evidence that the condition is equivalent to an already-known protected local class;
- evidence that WP09-compatible fields with both parities occur for the same curve;
- a concrete candidate statement narrow enough for proof.

Do not write “verified theorem” or equivalent language for computational patterns.

## 7. Source-admission rule

When an external theorem is materially required:

1. stop the MATHSOLVE theorem inference at the exact premise;
2. create a bounded MATHFORGE source audit on a branch from current protected MATHFORGE `main`;
3. identify the primary source, theorem number, hypotheses, prime range, normalization, and exclusions;
4. inspect primary PDFs visually when a PDF is the source;
5. protect the MATHFORGE audit through its normal review/CI path;
6. resume MATHSOLVE from the protected provider SHA.

A secondary survey or search snippet is not sufficient theorem authority when the primary source is reasonably obtainable.

## 8. Exact-head review and merge protocol

For every theorem or durable execution package:

1. branch from the current protected MATHSOLVE head;
2. keep changes bounded to the active work package and canonical handoff unless a broader change is necessary and justified;
3. compare candidate to protected base and record the exact candidate SHA;
4. perform a non-authoring Adversary pass on that exact SHA;
5. repair any defect on-branch;
6. after every repair, discard stale review evidence and repeat Adversary on the new exact head;
7. perform a distinct non-authoring Referee pass on the exact accepted head;
8. require ordinary Solve checks and GCL conformance on the same exact head;
9. before merge, re-fetch protected `main`, PR head, and all material provider anchors;
10. merge only if the expected head and protected base are unchanged or reconciled;
11. read back protected `main` and the canonical handoff after merge;
12. update #215 and #164 with the protected SHA and exact mathematical disposition.

## 9. Recovery ladder

On failure, continue through the following ladder unless a genuine boundary is reached:

1. inspect exact failing job/step/log or connector response;
2. distinguish infrastructure failure from proof/code failure;
3. retry transient infrastructure failures on the same exact head;
4. repair proof/code failures within the authorized lane;
5. rerun exact-head validation;
6. if a connector lacks a required supported operation, use the governed GitHub transport fallback available in the execution environment;
7. if computation is too expensive for CI, move it to a bounded reproducible runner and keep only smoke validation in CI;
8. if an external source is inaccessible, seek an authoritative alternate copy before relying on secondary descriptions;
9. stop only when the next action would require a new theorem, source premise, authority, authentication, safety exception, or materially changed scope.

Before stopping, state the boundary by its exact name.

## 10. Claim firewall

An agent may not infer or state without exact proof:

- `BSD-R2-A1`;
- `m_K(f)` is odd;
- `lambda_D` is a `2`-adic unit;
- the Kriz–Li condition always holds;
- D2a height nondegeneracy;
- a height-one-`(2)` main conjecture from an odd-prime theorem;
- a numerical pattern as a theorem;
- MATHCERT certification from MATHSOLVE review or CI.