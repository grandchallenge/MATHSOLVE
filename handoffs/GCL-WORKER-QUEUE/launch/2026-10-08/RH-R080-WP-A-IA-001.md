GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: RH-001
TRANCHE: RH-R080-P1-POSITIVITY-001
ASSIGNMENT_ID: RH-R080-WP-A
DISPATCH_ID: RH-R080-WP-A-IA-001
AGENT_REF: INDEPENDENT-AGENT-RH-R080-A
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

# RH-R080 WP-A — finite CCM positivity mechanism

Timebox: 60 minutes of substantive work.

Protected campaign context:
- MATHSOLVE protected Route C repair: RH-R077, merge `d3f753345998b9c1692dc61c29c921bf2ef2dc1c`.
- Current Route C tracker: #414.
- R080 bounded parent: #753.
- Read `handoffs/RH-001/README.md`, `handoffs/RH-001/routes/ROUTE_C_PROJECTIVE_MEASURE_CLOSURE.md`, and the R077/R056 protected work packages before reasoning.

Mission: determine whether the exact finite CCM operator/matrix under the source simple-even hypotheses admits a theorem-grade positivity-preserving, Perron-Frobenius/Krein-Rutman, oscillation, total-positivity, or related mechanism that forces the simple even ground eigenfunction to be pointwise nonnegative.

Do not assume that "simple even" implies pointwise positive. The protected source interface does not supply that theorem.

Preferred outputs, in order:
1. an exact positivity theorem with all hypotheses matched to the actual CCM finite object;
2. a precise reduction to one smallest missing source/operator lemma;
3. a rigorous obstruction showing why standard positivity machinery does not apply.

Primary sources are allowed where needed, but identify theorem/section precisely. No novelty or RH claim.

Return exactly one RESULT/1 comment on issue #1003 with:
GCL-CONTRIBUTION-RESULT/1
dispatch_id: RH-R080-WP-A-IA-001
agent_ref: INDEPENDENT-AGENT-RH-R080-A
assignment: RH-R080-WP-A
disposition: <EXACT_REDUCTION|SOURCE_INTERFACE_FOUND|COUNTEREXAMPLE|EXACT_BLOCKER|NO_MATERIAL_DELTA>
context_class: ZERO_CONTEXT
external_sources: <PROTECTED_PACKET_ONLY|PRIMARY_SOURCES_USED>
timebox_observed: <YES|NO>

## Strongest exact statement
...
## Derivation
...
## Assumptions beyond bootstrap
...
## Verification / falsification hooks
...
## Claim boundary
...
## Next residual
...
