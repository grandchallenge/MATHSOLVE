GCL-ZERO-CONTEXT-LAUNCH/2
STATE: ACTIVE
CAMPAIGN: RH-001
TRANCHE: RH-R080-P1-POSITIVITY-001
ASSIGNMENT_ID: RH-R080-WP-C
DISPATCH_ID: RH-R080-WP-C-IA-001
AGENT_REF: INDEPENDENT-AGENT-RH-R080-C
RETURN_PROTOCOL: GCL-CONTRIBUTION-RESULT/1
EXECUTION_MODE: SELF_CONTAINED_INDEPENDENT_BLIND
CANONICAL_MUTATION_AUTHORIZED: NO
CERTIFICATION_AUTHORIZED: NO

# RH-R080 WP-C — positivity-free signed-projective normality

Timebox: 60 minutes.

Protected starting point: RH-R077 projective-measure repair. The candidate signed measure for real even `f` is
`d mu_f = f(x) cosh(x/2) dx / A_f`, `A_f != 0`, with
`kappa(f)=||mu_f||_TV`.

Mission:
1. independently prove the strongest exact strip bound of the form `|F_f(z)| <= (1/2) kappa(f)` for `|Im z|<=1/2`, or a sharper valid statement;
2. state the minimal uniform quantity on an admitted CCM family sufficient for Montel normality;
3. identify a plausible protected/source-specific route to bound that quantity, or prove an obstruction.

Do not assume positivity. Do not promote the abstract criterion to the actual CCM family unless the uniform source-specific estimate is proved.

Return one RESULT/1 on #1005 using dispatch_id `RH-R080-WP-C-IA-001`, agent_ref `INDEPENDENT-AGENT-RH-R080-C`, assignment `RH-R080-WP-C`, with the standard six sections.
