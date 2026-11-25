GCL-ZERO-CONTEXT-LAUNCH/2
CAMPAIGN: RH-001
WORK_PACKAGE: RH-R080
ASSIGNMENT_ID: RH-R080-WP-B
DISPATCH_ID: RH-R080-WP-B-IA-001
AGENT_REF: INDEPENDENT-AGENT-RH080B
PROTECTED_LEASE_IDENTITY: RH-R080-WP-B :: RH-R080-WP-B-IA-001 :: INDEPENDENT-AGENT-RH080B
INTENDED_RETURN: https://github.com/grandchallenge/MATHSOLVE/issues/755
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
GITHUB_ACCESS_REQUIRED: PARTICIPANT_ENVIRONMENT_AUTHENTICATED_COMMENT_CAPABILITY
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

Read this entire immutable task. Execute only this bounded assignment. Before substantive work, verify that your environment can post one authenticated GitHub issue comment to INTENDED_RETURN. If it cannot, report RETURN_TRANSPORT_UNAVAILABLE and do not begin substantive work.

GCL-CONTRIBUTION-DISPATCH/1
dispatch_id: RH-R080-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-RH080B
campaign: RH-001
work_package: RH-R080
assignment: RH-R080-WP-B
concurrency_mode: independent_blind
return_protocol: GCL-CONTRIBUTION-RESULT/1
intended_return: https://github.com/grandchallenge/MATHSOLVE/issues/755

# FINITE-POSITIVITY-FALSIFICATION

You are an independent zero-context mathematical contributor. This document is your complete bounded work-set. Do not inspect RH-R080 sibling dispatches, sibling return issues, campaign discussion threads, unpublished notes, or other contributors' results before returning. You may use only the external-source class declared below.

Timebox: 35 minutes of substantive work, then return the strongest exact result reached.

External sources: PRIMARY_SOURCES_ALLOWED

## Protected packet shared by all RH-R080 contributors

Campaign: RH-001, Forward Route C.

Protected campaign facts you may treat as inputs:

1. In Connes–Consani–Moscovici, *Zeta Spectral Triples* (arXiv:2511.22755v1), Theorem 5.10 assumes that the smallest eigenvalue \(\epsilon_N\) of \(QW_\lambda^N\) is simple and that its corresponding eigenvector \(\xi\) is even, normalized by \(\delta_N(\xi)=1\). The theorem does not state pointwise positivity of \(\xi\).

2. The finite Galerkin space is
\[
E_N=\operatorname{span}\{V_n:|n|\le N\},
\]
with parity \(V_n\leftrightarrow V_{-n}\). The finite Weil matrix is real symmetric and commutes with parity. In the source basis its entries have the structured form
\[
\tau_{ii}=a_i,\qquad
\tau_{ij}=\frac{b_i-b_j}{i-j}\quad(i\ne j),
\]
with \(a_{-j}=a_j\), \(b_{-j}=-b_j\), assembled from the exact semilocal decomposition
\[
QW_\lambda=W_{0,2}-W_{\mathbb R}-\sum_p W_p.
\]

3. Protected RH-R038 rejected a prior Krein–Rutman closure. In particular, it did not establish that the continuum prime operator is compact or strongly positive, and simplicity of a prime-sector Perron root would not by itself imply simplicity or pointwise positivity of the full Weil ground state. Do not reuse those rejected implications.

4. Protected RH-R077 corrected Route C. Pointwise nonnegativity would imply the strip modulus bound, but no global CCM positivity theorem is protected. RH-R077 introduced the projective kernel
\[
K_z(x)=\frac{\cos(zx)}{\cosh(x/2)}
\]
and proved \(|K_z(x)|\le1\) for \(|\operatorname{Im}z|\le1/2\).

5. No contributor may assume RH, global simple-evenness, cofinal admissibility, pointwise positivity, determinant convergence, or any unprotected candidate-convergence statement.

A negative theorem, exact blocker, or counterexample is fully acceptable.

## Objective

Try to falsify pointwise positivity for the actual finite CCM simple-even ground state. Find the smallest exact or rigorously certified finite pair \((\lambda,N)\) for which the lowest eigenvalue is simple, the ground eigenvector is even, but the corresponding even trigonometric polynomial changes sign on the physical interval.

## Bounded work

Work adversarially.

1. Reconstruct finite \(QW_\lambda^N\) only from the primary CCM formulas or another source you explicitly identify.
2. Small \(N\) is preferred. Search \(N=1,2,3,\ldots\) and simple exact or rigorously bounded \(\lambda\) values.
3. A floating-point sign plot is not a counterexample. To return COUNTEREXAMPLE, certify:
   - the finite matrix entries to rigorous intervals or exact expressions;
   - simplicity of the lowest eigenvalue;
   - evenness / strict parity ordering as needed;
   - a point \(x_0\) or interval where the normalized ground trigonometric polynomial is rigorously negative while it is positive elsewhere (or otherwise sign-changing).
4. If exhaustive exact certification is not feasible in the timebox, return the smallest promising candidate together with the exact missing certification step as EXACT_BLOCKER. Do not promote numerics.
5. If you prove instead that sign change is impossible in a bounded regime such as \(N=1\), state the exact theorem and hypotheses.

A valid finite counterexample disproves the universal implication “finite simple-even => pointwise nonnegative” and immediately redirects Route C to positivity-free normality.

## Independence and authority

This dispatch is a member of blind cohort `RH-R080-BLIND-COHORT-001`.

You have no repository mutation, adjudication, certification, publication, or claim-promotion authority. Do not strengthen an unsupported statement merely to match the proposed route.

## Required return

Return exactly one narrative-only comment on INTENDED_RETURN. No branches, pull requests, attachments, side files, or supplementary comments.

\`\`\`text
GCL-CONTRIBUTION-RESULT/1
dispatch_id: RH-R080-WP-B-IA-001
agent_ref: INDEPENDENT-AGENT-RH080B
assignment: RH-R080-WP-B
disposition: <PROVED_REDUCTION|EXACT_CERTIFICATE|FORMAL_LEMMA_PROVED|COUNTEREXAMPLE|NO_MATERIAL_DELTA|EXACT_BLOCKER>
context_class: ZERO_CONTEXT
external_sources: PRIMARY_SOURCES_ALLOWED
timebox_observed: <YES|NO>

## Strongest exact statement
<Exact theorem, counterexample, reduction, or blocker.>

## Derivation
<Complete argument. If code is used, include the smallest replayable code inline.>

## Assumptions beyond bootstrap
<List every extra assumption, or NONE.>

## Verification / falsification hooks
<Concrete checks another reasoner can perform.>

## Claim boundary
<State exactly what follows and what does not. No certification claim.>

## Next residual
<At most three sentences.>
\`\`\`

The first valid conforming return is the durable contribution for this dispatch. Intake preserves evidence only; it does not adjudicate correctness or confer institutional authority.
