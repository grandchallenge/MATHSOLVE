# BSD-R2-A1-WP60 — literal-p=2 frontier research programme

## 1. Status and authority

- Campaign: `BSD-001 — Birch-Swinnerton-Dyer selected rank-one 2-primary campaign`.
- Parent programme owner: `grandchallenge/MATHSOLVE#164`.
- WP60 execution tracker: `grandchallenge/MATHSOLVE#215`.
- Constitutional authority at programme issuance: `grandchallenge/INTELLECT@fc9ee5537bf07586dffcc621e753204ecd835365`.
- Protected mathematical baseline: `grandchallenge/MATHSOLVE@aae4320432a5510146a5af0bebcfd966e36d7419`.
- Protected provider baseline: `grandchallenge/MATHFORGE@c8af223d0e05f999b4977a0dae5b1b5281eff93e`.
- Selected theorem state: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

This package is a research execution programme. It does not certify a theorem and does not alter the protected claim state by itself.

Before any mutation, every executing agent must re-fetch protected `main` for INTELLECT, MATHSOLVE, and any provider repository it will use. The SHAs above are issuance anchors, not permission to use stale state.

## 2. Exact entering boundary

Protected WP59 isolates the substantive D2d residual

`R_2(E,K,f) := 2 ord_2(m_K(f)) - ord_2(lambda_D)`,

where

`lambda_D := L(E^D,1)/Omega(E^D) in Q^x`.

The current named theorem/source boundary is

`MISSING_LITERAL_P2_COMBINED_HEEGNER_INDEX_TWIST_LRATIO_THEOREM_WITHOUT_EXTRA_MOD2_LOG_OR_RANKZERO_SEED`.

WP59 explicitly permits reopening D2d through any one of five forms:

- `R1`: exact literal-`p=2` Heegner-index valuation;
- `R2`: exact WP00-normalized twist-L-ratio valuation under all WP09 constraints;
- `R3`: a theorem forcing the Kriz–Li mod-`2` Heegner-log condition for a WP09-compatible auxiliary field;
- `R4`: a direct theorem determining the combined residual `R_2(E,K,f)`;
- `R5`: literal-`p=2` integral height-one-`(2)` main-conjecture/reciprocity control that specializes to the protected determinant line.

WP60 is designed to attack `R5`, `R3`, and `R1` directly, and to generate exact theorem-discovery evidence relevant to all five forms.

## 3. Research lanes and priority

### WP60A — finite-level literal-p=2 analytic determinant generator

**Priority:** primary.

**Purpose:** bypass the separate Heegner-index and twist-L-ratio valuations. Construct an integral analytic generator on the finite-level primitive determinant/Fitting line and prove exact compatibility with the protected algebraic determinant object at the height-one prime `(2)`.

**Success condition:** establish WP59 reopening form `R5`, or a comparably strong exact determinant identity implying `R4`.

**Reason for priority:** the protected campaign already contains the finite primitive `2`-Selmer/Fitting invariant, square-presentation machinery, exact strict/Kummer comparison, local correction terms, Bockstein structure, and exact analytic normalization. The remaining D1c defect is specifically the analytic generator at height one `(2)`.

### WP60B — force the Kriz–Li literal-p=2 condition

**Priority:** secondary, parallel with WP60A.

**Purpose:** translate the exact Kriz–Li mod-`2` logarithmic condition into the protected WP00/WP09/WP38 normalization, determine which part is fixed by the rational rank-one generator and which part varies with the auxiliary field `K`, and prove or falsify that a WP09-compatible `K` can always be chosen to satisfy it.

**Success condition:** establish WP59 reopening form `R3`, or derive `R1` directly.

**Critical anti-circularity test:** if the translated Kriz–Li condition is equivalent to the unknown parity of `m_K(f)` plus already-known local data, record that equivalence and do not present the route as independent progress.

### WP60C — exact real-data p=2 Heegner-log reconnaissance

**Priority:** supporting lane; start early because it can falsify bad conjectures cheaply.

**Purpose:** compute the exact mod-`2` Heegner-log condition and correlated protected invariants on real selected curves and WP09-compatible auxiliary fields. Use the results to discover finite local criteria, counterexamples, or candidate structural statements for WP60A/WP60B.

**Success condition:** produce a reproducible exact dataset and at least one mathematically precise candidate criterion, falsification, or dependency statement that changes the proof search.

**Claim boundary:** computational evidence is never a proof of `BSD-R2-A1`, R1–R5, height nondegeneracy, Heegner primitivity, or a uniform nonvanishing theorem.

## 4. Parallel boundaries retained

The following independent lanes remain live:

- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2a: `MISSING_P2_K_HEIGHT_NONDEGENERACY`.

WP60A is the direct D1c attack. A materially new D2a theorem may also create a new route into D2d and must trigger a fresh WP59 reopening analysis.

D2e remains downstream:

`MISSING_P2_WP06_EXACT_QUADRATIC_DESCENT_OF_NORMALIZATION`.

Do not execute D2e as if D2d were resolved.

## 5. Required evidence hierarchy

From strongest to weakest:

1. exact protected theorem/proof in MATHSOLVE;
2. exact external theorem admitted through MATHFORGE with hypotheses matched literally at `p=2`;
3. exact symbolic or finite arithmetic derivation with reproducible code and proof-level justification of the computation interface;
4. numerical/computational reconnaissance used only to formulate or falsify conjectures.

An equality after inverting `2`, an unspecified `2`-unit, a theorem with a hidden or explicit `p>2` hypothesis, or numerical agreement on examples is insufficient to close D1c, D2a, or D2d.

## 6. Execution order

An executing Codex agent should proceed as follows.

1. Re-fetch protected live state and reconstruct the WP59 boundary from repository artifacts.
2. Start WP60A with an exact dependency map of the finite-level primitive determinant objects already proved in WP16–WP19 and WP35–WP52.
3. In parallel, perform WP60B normalization reduction before any new broad source search.
4. Start WP60C only with real curves satisfying the selected hypotheses and real WP09-compatible fields. Do not use dummy or synthetic examples as evidence.
5. When a lane reaches an external theorem premise, route it through MATHFORGE before using it in a MATHSOLVE proof.
6. When a candidate appears to satisfy R1–R5, explicitly replay the WP59 reopening contract before claiming D2d is reopened or resolved.
7. Keep D2e closed until the D2d residual is actually on an exact protected line.

## 7. Governance and completion

Routine bounded research, source screening, implementation, exact-head non-authoring Adversary/Referee review, ordinary CI, protected merge, readback, tracker maintenance, and handoff maintenance may proceed under the current delegated agent authority.

Do not:

- write directly to protected branches;
- manufacture reserved authority or certification;
- infer mathematical truth from CI;
- promote source admission to MATHCERT certification;
- silently enlarge the selected curve class or weaken WP09 auxiliary-field constraints;
- repeat the WP59 rejected-route sweep without a materially new theorem or hypothesis.

A WP60 sublane stops only at a named theorem/source/evidentiary/authority boundary. Recoverable tooling, connector, compiler, CI, or environment failures require recovery, not abandonment.

## 8. Programme completion criterion

WP60 as a research programme is complete when at least one of the following occurs:

1. one lane satisfies an R1–R5 reopening condition and the next exact theorem package is protected;
2. the lanes prove a sharper bounded barrier with materially stronger exclusion/reduction information than WP59 and record a new executable successor;
3. a genuine authority, source, or theorem boundary prevents further bounded work and is recorded with exact reopening criteria.

`BSD-R2-A1` remains unproved unless and until the selected equality itself is established and later routed through the required certification process.