# RH-001 Forward Route C — Determinant convergence to Xi

Status: ACTIVE_PARALLEL_ROUTE

Route role: attack the terminal sufficient RH bridge directly, without requiring construction of one limiting self-adjoint Hilbert-Polya operator first.

Current protected campaign head at pack creation:
grandchallenge/MATHSOLVE@7387aa8993355ab854630cf0683b4120a813884c

Protected route foundation:
RH-R035-ZETA-SPECTRAL-TRIPLES-LIMIT-001
work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md

Protected provider audit:
grandchallenge/MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790
reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md

## 1. Mission

Prove local uniform convergence on C of a correctly normalized cofinal family of finite Zeta Spectral Triple determinants to the classical Xi function.

The protected terminal bridge is:

If entire functions F_j have only real zeros and

F_j -> Xi

locally uniformly on C, then Xi has only real zeros by Rouché/Hurwitz. Under the standard normalization, RH follows.

Therefore this route does not need to first construct one limiting self-adjoint operator.

This is the smallest exact terminal target presently known in the campaign.

## 2. Finite source theorem already available

For finite scale lambda and Galerkin parameter N, the CCM source defines a finite self-adjoint rank-one perturbation under its simple-even hypothesis.

The protected R035 audit records the finite determinant formula

det_reg(D_log^(lambda,N)-z)
=
-i lambda^(-iz) xi_hat(z),

where xi is the relevant finite minimal eigenvector under the source normalization.

The source theorem gives:

- finite self-adjointness under the stated hypothesis;
- an entire determinant factor;
- real zeros of the finite entire function;
- identification of those zeros with the finite approximant spectrum.

The finite construction uses prime/arithmetic data and does not fit a supplied list of zeta zeros.

## 3. What is still open

None of the following is currently protected as a theorem:

- one canonical cofinal schedule (lambda_j,N_j) sufficient for the limit;
- the exact normalization F_{lambda,N} needed for convergence to Xi;
- locally uniform convergence of the normalized determinants;
- a strong enough k_lambda -> xi_lambda theorem;
- global simple-evenness for the full range of scales needed by the limiting construction;
- a limiting self-adjoint operator;
- complete spectral convergence to all zeta ordinates.

Route C may close RH without the last two items, but not without determinant convergence and the finite real-zero property along the chosen cofinal family.

## 4. Protected lineage to context-load

Read:

- handoffs/RH-001/README.md
- work_packages/RH_R035_ZETA_SPECTRAL_TRIPLES_LIMIT.md
- work_packages/RH_R036_QW_PARITY_GAP_REDUCTION.md
- work_packages/RH_R037_QW_SECTOR_GALERKIN.md
- work_packages/RH_R050_TRIAL_REWEIGHTED_EXTENSION.md
- MATHFORGE@564f6e2b41c9b13334bc8a5b84914a85c6b70790:
  reports/discovery/rh_001/rh_r035_zeta_spectral_triples_limit.md
- MATHFORGE@51042c94185cc9db1fa457ae40f26276747a0a4d:
  reports/discovery/rh_001/rh_r036_qw_parity_substrate.md
- MATHFORGE@76221c214bcb8227557d25741d83927051e62e8b:
  reports/discovery/rh_001/rh_r037_finite_parity_galerkin.md
- AGENTS.md

Also acquire and read the exact primary CCM Zeta Spectral Triples source before asserting any normalization not already protected.

## 5. The proof-obligation chain

A useful decomposition is:

C0. Exact finite normalization.

C1. Select and justify a cofinal parameter schedule.

C2. Establish a compact-set transform/determinant stability estimate.

C3. Prove approximation of the true finite/full eigenvector by the source candidate strongly enough to use C2.

C4. Prove local boundedness / normal-family control of the normalized determinants.

C5. Identify every subsequential locally uniform limit with Xi.

C6. Conclude full local uniform convergence.

C7. Apply the already-protected R035 Rouché/Hurwitz bridge.

An agent does not need to solve C0-C7 in one tranche. Clean progress on one dependency is meaningful.

## 6. C0 — Freeze the exact normalization

This is the first mandatory task before any convergence theorem.

The raw finite identity contains factors such as

-i lambda^(-iz) xi_hat(z).

The limiting strategy uses a normalization toward Xi.

Do not guess that normalization.

A route agent should:

1. inspect the exact source normalization;
2. record every scalar/exponential factor;
3. distinguish normalization depending on lambda, N, and z;
4. prove that multiplying by the chosen nonvanishing entire factor does not alter the real-zero property;
5. define one canonical F_{lambda,N}(z) for the campaign.

If the source normalization is ambiguous or changed between versions, send that question to MATHFORGE before proceeding.

A durable normalization theorem/definition is itself a valuable contribution.

## 7. C1 — Cofinal schedule

The family has two parameters.

Do not write lambda,N -> infinity without specifying what that means.

Possible outputs:

- prove convergence uniformly for all sufficiently large N=N(lambda);
- identify a source-mandated relation N(lambda);
- prove diagonal extraction is sufficient;
- define a cofinal directed set and formulate the theorem as a net.

The chosen indexing must preserve every hypothesis needed for finite self-adjointness and real zeros.

## 8. C2 — Compact-set transform stability

This is a high-value standalone theorem.

If f and g live on the logarithmic interval [-a,a], then for z in a compact K subset C, a generic Fourier/Laplace transform difference obeys a bound of the form

sup_{z in K}
|f_hat(z)-g_hat(z)|
<=
C(K,a) ||f-g||_X

for a suitable norm X.

But a grows with lambda. Therefore the dependence of C(K,a) matters critically.

An agent should determine the weakest eigenvector norm and rate that imply compact-uniform transform convergence after the exact determinant normalization.

Useful targets include:

- weighted L1 bounds;
- L2 plus explicit interval-length/exponential factors;
- Sobolev/Paley-Wiener estimates;
- bounds exploiting parity or boundary normalization.

This lemma should state exact dependence on compact height and a=log lambda.

## 9. C3 — Source k_lambda approximation

The protected R035 source audit identifies the source's k_lambda approximation as a named missing theorem.

The task is not merely to show

||k_lambda-xi_lambda|| -> 0.

One needs a rate/norm strong enough to feed C2.

A good contribution can be:

- determine the exact required rate from C2;
- prove that a known source estimate is insufficient;
- derive a stronger variational estimate;
- exploit the spectral gap to convert Rayleigh-quotient error into eigenvector error.

This is a natural place where Route A/B can feed Route C: a quantitative simple-even spectral gap can turn energy approximation into vector approximation through Davis-Kahan/min-max style estimates.

## 10. C4 — Normal-family route

Another useful approach is to prove local boundedness of normalized determinants.

If the normalized entire family is locally bounded, Montel gives subsequential locally uniform convergence.

Then it remains to identify any subsequential limit.

Possible limit-identification data include:

- convergence on a set with an accumulation point;
- a functional equation plus sufficiently rich value data;
- convergence of logarithmic derivatives on a domain;
- an explicit entire-function representation.

Do not assume pointwise convergence automatically supplies local boundedness.

## 11. C5 — Identify the limit as Xi

A subsequential entire limit with real zeros is not enough. It must be Xi.

The identification theorem must also control normalization. Multiplying Xi by a nonzero entire exponential factor preserves zeros but is not equality to Xi.

For the RH bridge, convergence to any nonvanishing entire multiple of Xi may be enough if that factor is rigorously known never to vanish. If using this relaxation:

1. state it explicitly;
2. prove the factor is zero-free;
3. update the protected R035 bridge or prove the generalized version.

Do not silently change the target.

## 12. Interaction with simple-evenness

The finite source theorem uses a simple-even hypothesis.

The campaign now proves full-operator simple-evenness only on an explicit local interval near lambda=1.

A determinant-convergence route with lambda -> infinity cannot assume this local theorem supplies simple-evenness at all large scales.

An agent must explicitly determine which simple-even statement the selected finite/cofinal determinant family needs.

Possible outcomes:

- Route A/B eventually supplies the needed global scale theorem;
- the finite theorem needs a weaker condition than the full-form global statement;
- the determinant convergence can be formulated on a verified cofinal subsequence;
- or simple-evenness remains a separate unresolved dependency.

Do not suppress it.

## 13. Minimum meaningful deliverable

A contribution is meaningful if it provides one protected result such as:

1. exact canonical determinant normalization;
2. a theorem reducing compact-uniform determinant convergence to a quantitative eigenvector norm/rate;
3. a cofinal-index theorem;
4. a Montel/local-boundedness theorem;
5. a rigorous k_lambda-to-xi_lambda estimate;
6. a limit-identification theorem;
7. a negative theorem showing a proposed norm/rate is insufficient.

This route is expected to advance through such modular results.

## 14. False-proof firewall

Reject:

- low-zero numerical agreement as convergence;
- pointwise convergence as local uniform convergence;
- real zeros of approximants as RH without a specified limit;
- an unspecified normalization;
- a family of self-adjoint operators as one limiting self-adjoint operator;
- finite self-adjointness as limiting self-adjointness;
- numerical eigenvector overlap as a k_lambda theorem;
- convergence on the real axis alone unless a theorem upgrades it;
- use of Hurwitz/Rouché before local uniform convergence is established.

## 15. Governance

MATHSOLVE owns theorem development.

MATHFORGE must be used for:

- exact source normalization not already protected;
- source-version discrepancies;
- new external convergence theorems or literature;
- claims about what the CCM paper proves.

MATHCERT should be involved only after a bounded terminal convergence claim has a complete exact proof/checker surface.

Any claim that Route C has proved RH must pass the full governed terminal process. Do not make that claim inside ordinary theorem development.

## 16. Completion criterion for Route C

Route C is mathematically complete when there is a protected theorem giving a cofinal family of normalized finite entire determinants with real zeros and locally uniform convergence to Xi, or to a rigorously identified zero-free entire multiple of Xi.

At that point the protected R035 Rouché/Hurwitz bridge supplies the RH implication, subject to the programme's certification/governance process.

An individual agent contribution is complete when it protects one missing lemma or one rigorous obstruction in the C0-C6 chain.

## 17. Zero-context handoff prompt

The copy-ready prompt is stored at:

handoffs/RH-001/routes/prompts/ROUTE_C_ZERO_CONTEXT.txt
