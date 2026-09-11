# BSD-001 frontier after WP25

## Status and authority

This is the continuity record for the WP25 candidate. It acquires protected status only after exact-head admission to MATHSOLVE `main` and protected readback.

- Campaign: `BSD-001`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Candidate protected-base MATHSOLVE head: `eac82bf2809ff70317a3542a58247e6a11299bc0`.
- Protected WP25 source authority: `grandchallenge/MATHFORGE@b09faf74936611616465186c8702ea0ce6f36828`.
- Mathematical certification remains exclusively a MATHCERT function.
- Selected target: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.

## Protected chain entering WP25

WP24 gives

`C_E = ker(chi_P|K_loc)`

and defines

`rho_E := len_Z2 im(chi_P|K_loc)`.

It proves

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - rho_E`.

Thus the only remaining D1b information entering WP25 is the order of one finite rank-one local Tate character.

## WP25 representation

For each finite place `v`, let

`N_v^infty := intersection_n N_{F_{v,n}/Q_v}E(F_{v,n})`.

Using protected Tan local norm duality and the protected finiteness of `K_v`, WP25 proves that the finite-layer norm images stabilize and that

`U_v := E(Q_v)/N_v^infty ~= K_v^vee`.

For a saturated rank-one generator `P`, define

`[P]_v in U_v`

and the finite tuple

`u(P) := ([P]_v)_{v in S_def}`,

where `S_def` is the finite support of the nonzero local control groups.

WP25 proves that under

`K_loc^vee ~= product_{v in S_def} U_v`,

the WP24 character `chi_P|K_loc` is exactly the dual element `u(P)`.

Hence

`2^{rho_E}=ord(u(P))`.

If

`rho_v(P):=ord_2(ord([P]_v))`,

then exactly

`rho_E=max_{v in S_def} rho_v(P)`.

The local bounds are

`rho_2(P) <= 2 ord_2(3-a_2)`

and

`rho_ell(P) <= ord_2(c_ell)`

for odd bad semistable `ell`; odd good and real places contribute zero.

Therefore

`len_Z2(C_E^vee)
 = 2 ord_2(3-a_2)
   + sum_{ell|N} ord_2(c_ell)
   - max_v rho_v(P)`.

## New substantive boundary

The former scalar boundary

`MISSING_P2_GLOBAL_HIT_CHARACTER_IMAGE_LENGTH`

is replaced by

`MISSING_P2_SATURATED_GENERATOR_LOCAL_UNIVERSAL_NORM_ORDER`.

The unknown is now concrete: determine the order of the saturated generator in a finite list of explicit local universal-norm quotients.

## Preferred next tranche

Do not return to broad literature screening.

Split the next investigation by local reduction type:

1. **odd multiplicative places**: use protected WP22's Neron-component reduction to identify the universal-norm quotient and the class `[P]_ell` in component-group terms. The target is an exact formula for `rho_ell(P)` in terms of the component of the saturated global generator. Preserve split/nonsplit distinctions and WP13 regime A/B data.
2. **place `2`**: keep the primitive Kummer condition. Seek an exact decomposition of the order-`(3-a_2)^2` universal-norm quotient into reduction and connected/formal contributions, and locate `[P]_2` inside it. Do not infer the order from `a_2` alone.
3. Only after both lanes are exact should one test whether the resulting maximum local norm order is identical to a protected WP20 Bockstein/regulator term. Similarity of rank-one roles is not evidence of equality.

Any new external theorem premise must first be admitted through MATHFORGE.

## Other determinant boundaries remain

- D1a: `MISSING_P2_PRIMITIVE_CYCLOTOMIC_PERFECT_DETERMINANT_REALIZATION`;
- D1c: `MISSING_P2_ANALYTIC_DETERMINANT_GENERATOR_AT_HEIGHT_ONE_2`;
- D2: `MISSING_P2_BOCKSTEIN_TO_WP00_NORMALIZATION`.

## Claim firewall

WP25 does not prove:

- any numerical value of `rho_v(P)` or `rho_E`;
- a component-group formula for `[P]_ell`;
- a formal-group formula for `[P]_2`;
- equality with a regulator, height, Bockstein, or analytic factor;
- D1a, D1c, or D2;
- `delta_2(E)=len_Z2 Sha(E/Q)[2^infinity]`;
- `BSD-R2-A1`;
- any MATHCERT certification, novelty, priority, patentability, or commercial claim.

## Continuation rule

Before successor mutation, re-fetch protected state. Use WP25 only if its exact theorem bytes are protected on MATHSOLVE `main`. Continue through bounded proof, MATHFORGE admission where required, exact-head non-authoring/read-only Adversary and Referee passes, affected CI/GCL checks, protected merge, protected readback, and #164/handoff maintenance.

Stop only at a genuine theorem, source, authority, authentication, safety, material-state, target-drift, or MATHCERT boundary, and name that boundary exactly.
