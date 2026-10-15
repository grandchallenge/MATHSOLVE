GCL-CONTRIBUTION-DISPATCH/1

# QFT-COND-005 EXT-015A: Quotient-stage liquid realization and Ext¹ injectivity

**Dispatch:** `QFT-COND-005-EXT-015A-IA-001`
**Assignment:** `EXT-015A`
**Agent ref:** `INDEPENDENT-SPECIALIST-QFT-COND-005-EXT-015A` (role identifier, **not** a separate GitHub account)
**Return issue:** https://github.com/grandchallenge/MATHSOLVE/issues/1081
**Original research issue:** https://github.com/grandchallenge/MATH-PROGRAMME/issues/2653
**Parent:** https://github.com/grandchallenge/MATH-PROGRAMME/issues/2617
**Mathematical handoff/source commit:** `c4c49545a279494c0c085b81aeaf245f4c3ace5a`
**Collaboration:** independent blind; do not use sibling research returns.
**External mathematical sources:** allowed; primary citations and exact propositions required.
**Execution/claim:** NOT PERMITTED until the MATHSOLVE protected dispatch is READY with lease ACTIVE and `/claim` has received `GCL-WORKER-RESERVATION/1` confirmation for this exact issue and authenticated actor.
**Authority:** bounded mathematical investigation and issue-comment return only. No protected repository change, theorem certification, priority claim, or publication.

## Immutable zero-context inputs

Read each item fully before mathematical work:

- The approved A/B worker handoff: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/EXT-015/handoffs/EXT-015A.md
- The canonical specification: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/EXT-015/SPEC.md
- Run/acceptance matrix: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/EXT-015/RUN_MATRIX.md
- Worker contract: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/EXT-015/WORK_PACKAGES.md
- Hostile control docket: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/EXT-015/EXTENSION_DOCKET.md
- Mathematical underived precedent: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/LFO3_SURJECTIVITY_THEOREM_013.md
- Derived precedent: https://github.com/grandchallenge/MATH-PROGRAMME/blob/c4c49545a279494c0c085b81aeaf245f4c3ace5a/research/condensed-qft/DERIVED_MAPPING_OBSTRUCTION_014.md
- Parent documentation of the programme's open boundary: https://github.com/grandchallenge/MATH-PROGRAMME/issues/2617

**Guiding question:** Can an extension carry genuinely global analytic information that no compact-support stage can capture?

## Specific assignment

Prove or refute the liquid quotient identification Q_b = colim_{c>=b} Liq(D_{L_c}(V)/D_{L_b}(V)), prove or refute fixed-Fréchet-source Hom factorization through one quotient stage, and prove or refute injectivity of colim_b Ext¹(H,G_b) -> Ext¹(H,G) using naturality of connecting homomorphisms. Do not investigate surjectivity as if assigned.

The starting coefficients are real `p`-liquid modules, `0<p<=1`; fix a compact-support nuclear Fréchet source `H`, with the concrete primary case `D_{[-1,1]}(R)`; output support stages are `D_{[-b,b]}(R)`. Declare the ambient exact/stable category for every claimed Ext class. No strict locally convex extension is admitted as liquid Ext without exact-realization proof.

### Mandatory adversarial checks

Verify categorical cokernel versus Fréchet quotient topology; closed quotient transition maps; continuity and separation of quotient probes; Baire uniformization on the fixed Fréchet source; profinite-plot naturality; the exact connecting long-exact-sequence diagram. Test missing quotient stage, global points without profinite lifts, and accidental dependence on EXT-015B.

Do not assert a theorem solely because a finite-dimensional fixture agrees, because nuclearity implies tensor flatness, or because a strict Fréchet extension is nonsplit. State the precise missing lemma if a source theorem cannot be verified. New mathematical claims require independent critical review downstream.

## Result contract

After authorized reservation and before posting a result, refresh issue comments and protected intake state. If this dispatch already has a preserved or accepted RESULT/1, stop without duplication. Use the authenticated GitHub identity that holds the active reservation. Post exactly one complete issue comment beginning:

```text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: QFT-COND-005-EXT-015A-IA-001
assignment: EXT-015A
agent_ref: INDEPENDENT-SPECIALIST-QFT-COND-005-EXT-015A
disposition: PROVED | REFUTED | EXACT_BLOCKER
source_programme_head: c4c49545a279494c0c085b81aeaf245f4c3ace5a
```

Then supply sections:
- `## Strongest exact mathematical statement`
- `## Definitions and categorical hypotheses`
- `## Proof or counterexample`
- `## Adversarial controls`
- `## Primary references (exact theorem/page)`
- `## Named unresolved lemma` (write NONE if fully resolved)
- `## Consequences for EXT-015 RUN_MATRIX`
- `## Bounded next step` (no execution or certification authority)

Do not copy another worker's results or synthesize sibling outputs in the blind phase. The accepted return is evidence pending mathematical review. It is not a certification or protected-merge approval.

## Worker bootstrap

Read https://github.com/grandchallenge/MATHSOLVE/blob/main/WORKERS.md for `reservation_controlled` pickup. Open the task issue, post exactly `/claim`, and execute only after receiving the controller's lease-backed reservation response. If abandoning without a return, use `/release`. A GitHub issue's `AVAILABLE` label is not itself an execution lease.

No Codex, GPU, Colab or Lean prerequisite is imposed. Tools may be used where justified by a specific mathematical subtask.
