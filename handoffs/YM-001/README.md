# YM-001 — Handoff

## Target repository and authority

Target work repository: `grandchallenge/MATHSOLVE`.

INTELLECT work-package phase: not applicable.

MATHSOLVE owns bounded theorem development and research artifacts. MATHCERT remains the sole certification authority. The current MATH-PROGRAMME routing gate authorizes restricted-target selection and immediate theorem development only against `YM-D001` through `YM-D005`.

## Purpose

Continue native Solve theorem development for `YM-001` while preserving the open-problem boundary. Two native theorem tranches are already admitted: the abstract converse-spectral implication inside `YM-D005` and the strong-resolvent spectral-exclusion stability theorem inside `YM-D001`. The current selected tranche audits whether the admitted regulated Yang-Mills evidence can actually instantiate the hypotheses of the D001 stability theorem.

## Current primary deliverable

Prove or refute restricted target `YM-D001-R002` in

`work_packages/YM_D001_REGULATED_APPLICATION_AUDIT/01_EVIDENCE_AUDIT.md`.

The target asks whether the currently admitted inputs `YM-T-010` and `YM-T-030` supply a cutoff-indexed physically normalized Hamiltonian/generator family, state-space comparison, common physical spectral exclusion, and convergence data sufficient to instantiate the admitted `YM-D001-R001` theorem. If not, the package must name the first exact missing interface without inflating that absence into an impossibility theorem.

## Material acceptance criteria

- freeze one common `Delta > 0` in the same physical energy units for all regulated operators;
- permit regulator-dependent operator domains by formulating convergence through `(I+H_n)^(-1)`;
- prove that `sigma(H_n) subset {0} union [Delta,infinity)` plus strong resolvent convergence forces `sigma(H) subset {0} union [Delta,infinity)`, or produce a counterexample;
- test whether a weaker topology suffices and preserve an exact failure fixture when it does not;
- separate spectral-exclusion survival from persistence/uniqueness of a zero-energy vacuum;
- preserve the distinction between a uniform physical-unit lower bound and merely positive regulator-dependent gaps;
- identify exactly which Yang–Mills-specific scaling, state-space comparison, convergence, and uniform-bound obligations remain open;
- preserve `YM-D001` through `YM-D005` as open research debts unless their full discharge conditions are met.

## Current substantive state

- `YM-WP01`: promoted eliminative false-proof infrastructure.
- `YM-WP02`: promoted theorem/dependency interface infrastructure.
- `YM-D005-R001` / `YM-D005-L001`: admitted in native Solve at protected merge `bbadc7953b26afadeb4014e2e4980232df46097b`; the theorem proves the abstract dense-observable converse spectral bridge after reconstruction.
- Post-R001 reconciliation: protected at `adaae95545abcb02db4ab9b2281981fc0f8ce07b`; `YM-D005-R002` is explicitly blocked by `YM-D002`/`YM-D003` before it can be instantiated in the target four-dimensional limiting theory.
- `YM-D001-R001`: admitted at protected merge `5b137761c217f96e4cf9afaf270b897025b44480`; it proves the abstract strong-resolvent spectral-exclusion stability implication only.
- `YM-D001-R002`: current selected native target; the candidate audit finds that `YM-T-010` plus `YM-T-030` do not yet provide the cutoff-indexed physical generator family required to apply R001.
- `YM-D001`: still open; the first currently exposed application obstruction is the missing regulator-to-generator/state-space interface, before a uniform physical spectral lower bound or convergence theorem can be posed on the admitted evidence.
- `YM-D002` through `YM-D004`: remain open construction/reconstruction/observable-identification debts.
- `YM-D006` through `YM-D009`: source/scope dispositions remain recorded and do not bypass D001-D005.

## Authoritative pointers

- `grandchallenge/INTELLECT:CONSTITUTION.md`
- `grandchallenge/INTELLECT:governance/constitutional_authority_schedule.json`
- `grandchallenge/INTELLECT:governance/handoffs/README.md`
- `grandchallenge/MATHSOLVE:AGENTS.md`
- `grandchallenge/MATH-PROGRAMME:campaigns/yang_mills/YM_CURRENT_ROUTING_GATE.json`
- `grandchallenge/MATH-PROGRAMME:campaigns/yang_mills/WP02_THEOREM_LEDGER/04_DEPENDENCY_DEBT_GATE.json`
- `grandchallenge/MATHSOLVE:campaign_manifests/YM-001.json`
- `grandchallenge/MATHSOLVE:work_packages/YM_D005_CONVERSE_SPECTRAL_BRIDGE/03_PROOF_OBLIGATION_DAG.json`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_STRONG_RESOLVENT_GAP_STABILITY/00_README.md`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_STRONG_RESOLVENT_GAP_STABILITY/01_STRONG_RESOLVENT_GAP_STABILITY.md`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_STRONG_RESOLVENT_GAP_STABILITY/02_CLAIM_LEDGER.yaml`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_STRONG_RESOLVENT_GAP_STABILITY/03_PROOF_OBLIGATION_DAG.json`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_REGULATED_APPLICATION_AUDIT/00_README.md`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_REGULATED_APPLICATION_AUDIT/01_EVIDENCE_AUDIT.md`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_REGULATED_APPLICATION_AUDIT/02_CLAIM_LEDGER.yaml`
- `grandchallenge/MATHSOLVE:work_packages/YM_D001_REGULATED_APPLICATION_AUDIT/03_PROOF_OBLIGATION_DAG.json`

## Selected theorem and falsification boundary

The candidate theorem uses the bounded transforms

`B_n = (I+H_n)^(-1)`

and the polynomial sign condition associated with the common gap. It proves strong-resolvent preservation without requiring norm-resolvent convergence.

Three exact firewalls accompany it:

1. weak convergence of the resolvents can fill the forbidden interval;
2. a moving zero-energy state can disappear even while the spectral exclusion survives strong-resolvent convergence;
3. positive gaps `Delta_n` with `inf Delta_n = 0` provide no positive limiting lower bound.

## Smallest safe successor after R002 admission

The R002 candidate identifies the first missing typed object as a cutoff-indexed, physically normalized self-adjoint generator family with explicit cross-regulator state-space comparison. Do not jump directly to estimating a continuum gap constant before that object exists.

The next bounded target is `YM-D001-R003`:

1. search the admitted source estate for a theorem that supplies a regulator-to-generator interface with explicit lattice-spacing/scale-setting data;
2. if found, bind its state spaces and physical normalization exactly and test whether it can feed R001;
3. if not found, isolate whether the missing construction belongs irreducibly to `YM-D002` (OS reconstruction) or `YM-D003` (four-dimensional continuum construction);
4. keep `YM-D005` separate: a spatial correlation-decay exponent may not be promoted to the bottom of the full physical Hamiltonian spectrum without the converse/completeness bridge.

The absence of such a theorem in the current evidence is a source-interface obstruction, not a proof that no future construction can exist.

## Material dependencies and boundaries

- `YM-D003` remains responsible for constructing and identifying a nontrivial four-dimensional continuum theory along a controlled physical trajectory.
- `YM-D002` remains responsible for a complete limiting Osterwalder-Schrader/reconstruction hierarchy if the Hamiltonian is obtained by that route.
- `YM-D004` remains responsible for renormalized local gauge-invariant curvature observables and perturbative normalization.
- `YM-D005` remains open despite its admitted abstract lemma because its four-dimensional reconstruction/density/common-decay hypotheses are not established.
- `YM-D001-R001` cannot create a uniform physical gap, a state-space identification, a continuum Hamiltonian, or a vacuum; it only proves stability once the stated hypotheses hold.
- no result in this tranche is certified until independently adjudicated by MATHCERT.

## Reserved authority / stop conditions

Stop or re-plan only for a material contradiction in the target formulation, failure of the operator-theoretic argument, evidence that the selected target is vacuous or already superseded by protected work, a reserved INTELLECT transition, authentication/safety failure, or material closure requiring certification/claim promotion outside MATHSOLVE authority.

## Notes intentionally omitted

This handoff intentionally omits constitutional doctrine, the generic handoff contract, historical WP00-WP02 material already protected in Programme, external-source audit detail already protected in MATHFORGE/MATH-PROGRAMME, and any terminal Yang–Mills solution claim.
