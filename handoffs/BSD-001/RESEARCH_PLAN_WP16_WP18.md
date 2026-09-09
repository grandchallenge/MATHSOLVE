# BSD-001 — WP16-WP18 research plan for unsquared `p=2` length control

## 1. Authority and protected starting state

- Campaign: `BSD-001`.
- Native mathematical repository: `grandchallenge/MATHSOLVE`.
- Programme owner: `grandchallenge/MATHSOLVE#164`.
- Protected MATHSOLVE starting head: `1aa2e76e596cd76061ac03590ff79db0b0b499d6`.
- Protected MATHFORGE starting head: `118ae1b5c2fc2630f53000921b742c610c50db16`.
- Current frontier: `BSD-R2-A1-S3-UNSQUARED-P2-LENGTH-CONTROL`.
- Current named boundary: `MISSING_UNIFORM_UNSQUARED_P2_LENGTH_CONTROL`.
- Selected claim: `BSD-R2-A1 = SELECTED_RESEARCH_TARGET_UNPROVED`.
- Certification authority: MATHCERT only; certification remains pending.

The Human Steward approved this programme as the next theorem-construction path. The objective is to change the representation of the unresolved integer-valued `2`-primary defect rather than continue broad source screening or parity-level arguments.

## 2. Exact mathematical target

Protected WP15 leaves

`delta_2(E) := ord_2(L'(E,1)/(Omega_E Reg_E)) - sum_{ell|N} ord_2(c_ell)`

and the exact target

`delta_2(E) = len_Z2 Sha(E/Q)[2^infinity]`.

WP15 also proves that square-class or parity information is structurally insufficient: the right-hand side is an even nonnegative integer, and parity does not determine its magnitude.

The new programme therefore targets **integer-valued unsquared `2`-primary control**.

## 3. Strategic representation change

The core idea is:

`complex BSD defect`

`-> stabilized finite-level 2^n-Selmer length`

`-> integral Selmer-complex length / Fitting valuation`

`-> integral Euler-system or determinant control over the WP09 imaginary quadratic field K`

`-> exact quadratic descent back to Q using the already-protected WP06 discrepancy ledger`.

This is a research programme, not an assertion that every arrow is already available.

## 4. WP16 — finite-level `2^n`-Selmer reduction

### 4.1 Objective

Replace `len_Z2 Sha(E/Q)[2^infinity]` by a stabilized finite-level quantity that is suitable for determinant/Fitting arguments.

For each `n >= 1`, define

`s_n(E) := ord_2 #Sel_{2^n}(E/Q) - n`.

The first theorem target is

`s_n(E) = ord_2 #Sha(E/Q)[2^n]`.

The second is stabilization:

`lim_{n -> infinity} s_n(E) = len_Z2 Sha(E/Q)[2^infinity]`.

The campaign target then becomes

`delta_2(E) = lim_{n -> infinity} s_n(E)`.

### 4.2 Required proof ingredients

Use only protected or in-package inputs:

1. analytic rank one and algebraic rank one;
2. finiteness of `Sha(E/Q)`;
3. odd rational torsion from residual mod-2 irreducibility;
4. the Kummer exact sequence

   `0 -> E(Q)/2^n E(Q) -> Sel_{2^n}(E/Q) -> Sha(E/Q)[2^n] -> 0`;

5. the rank-one decomposition of `E(Q)` to prove

   `#(E(Q)/2^n E(Q)) = 2^n`;

6. finiteness of the `2`-primary subgroup of Sha to prove eventual stabilization.

No BSD leading-term identity may be used in this reduction.

### 4.3 Selmer-complex reformulation

After proving the elementary finite-level theorem, identify the precise Selmer complex whose finite cohomology realizes the same stabilized length.

The target is an exact statement of the form

`stable 2-primary length = ord_2(Fitt/det of a finite Selmer object)`

with all local conditions named explicitly.

This step must specify:

- the coefficient ring;
- the local condition at `2`;
- local conditions at bad semistable primes;
- the treatment of the rank-one free direction;
- whether the object is a torsion quotient, cone, determinant line, Fitting ideal, or another integral invariant;
- exact compatibility with the WP00 normalization and WP13 Tamagawa bookkeeping.

If more than one Selmer-complex normalization is possible, record the equivalence or the defect term rather than choosing silently.

### 4.4 WP16 success criterion

WP16 succeeds if it gives a protected theorem reducing `BSD-R2-A1` to an exact equality between `delta_2(E)` and a named integral Selmer-complex invariant while retaining every power of `2`.

WP16 need not prove that final equality.

## 5. WP17 — imaginary-quadratic integral Selmer-complex lane

### 5.1 Why work over `K`

Protected WP09 supplies an imaginary quadratic field `K` with the required splitting and analytic nonvanishing properties. The programme should exploit `K` as the primary integral `p=2` arena rather than force every characteristic-2 duality argument directly over `Q`.

Protected WP06 already records the exact quadratic descent discrepancy terms. Therefore a theorem over `K` is useful only if its integral content can be descended without discarding `2`-power information.

### 5.2 Source-reconnaissance requirement

Any external theorem premise must be admitted through MATHFORGE before protected theorem use.

Candidate lines of inquiry include, but are not limited to:

- modern Selmer-complex/Euler-system/Fitting-ideal machinery over complete local or Gorenstein coefficient rings;
- `p=2`-aware self-duality and determinant-line results over totally imaginary fields;
- integral Heegner-point, Euler-system, or Kolyvagin-system statements that retain Tamagawa defects at `2`;
- exact explicit reciprocity laws connecting the integral algebraic object to the normalized analytic derivative;
- recent work by Bullach-Burns or successors, to be audited from primary sources before use.

These are **reconnaissance candidates only**. Their applicability is not presumed by this plan.

### 5.3 Mandatory applicability matrix

For each candidate theorem, record:

1. prime range: does it include `p=2` literally?
2. coefficient-ring hypotheses;
3. residual representation hypotheses;
4. ordinary/nonordinary local condition at `2`;
5. self-duality and archimedean hypotheses;
6. conductor and Tamagawa hypotheses;
7. whether imprimitive factors are removed;
8. whether the theorem gives inclusion, divisibility, equality, primitivity, characteristic/Fitting ideal, or only a unit class;
9. whether the result is integral enough to recover exact `Z_2` length;
10. whether an explicit reciprocity law reaches the WP00 complete-complex-`L` normalization;
11. whether the theorem covers both WP13 regimes, including residual-conductor drop at even Tamagawa primes;
12. what exact descent defect appears when returning from `K` to `Q`.

### 5.4 Primary theorem target over `K`

Seek an equality or pair of opposite inclusions strong enough to determine the integral Selmer-complex length over `K`.

Preferred hierarchy:

1. exact determinant/Fitting equality;
2. two opposite divisibilities whose quotient is a controlled unit;
3. one divisibility plus a new primitivity/nonvanishing theorem sufficient to force equality;
4. a sharp integer upper/lower bound which, together with an independent congruence/rigidity statement, determines the exact length.

Parity, square class, mod-2 nonvanishing, and numerical agreement alone are insufficient.

### 5.5 Descent target

Compose the strongest valid theorem over `K` with WP06 and the later WP09-WP15 protected deductions to obtain an exact `Q`-side statement.

Every `2`-power discrepancy must be accounted for explicitly. No “up to a `2`-adic unit” statement may be promoted to exact length without proving that the unit contributes zero valuation and that no omitted local factor remains.

## 6. WP18 — finite-level `2^n`-Selmer reconnaissance atlas

### 6.1 Purpose

WP18 is diagnostic, not certifying. Its purpose is to falsify wrong theorem shapes early and identify which integral invariant should be proved.

### 6.2 Cohort design

Select representative curves satisfying the protected `BSD-R2-A1` hypotheses from both WP13 local regimes:

- regime A: all bad Tamagawa numbers odd, residual conductor equal to the conductor;
- regime B: at least one even bad Tamagawa number, with the exact residual-conductor drop already identified by WP13.

Where practical, vary:

- split versus nonsplit multiplicative primes;
- the depth `v_2(ord_ell Delta_min)`;
- the number of even-Tamagawa bad primes;
- observed `2`-primary Sha size;
- local behaviour at `2` consistent with the selected good-ordinary hypotheses.

### 6.3 Measurements

For each curve record, with provenance:

- curve identifier and minimal model;
- conductor and minimal discriminant;
- analytic rank evidence used for reconnaissance only;
- `c_ell` and `ord_2(c_ell)` for all bad primes;
- residual conductor and WP13 regime;
- `#Sel_{2^n}` or equivalent finite-level data for increasing `n`;
- `s_n(E)`;
- observed stabilization index;
- any independently available Sha information;
- Cassels-Tate pairing data where computationally available;
- `delta_2(E)` under the fixed WP00 normalization, with numerical precision and provenance clearly separated from proof;
- the discrepancy

  `epsilon_n(E) := delta_2(E) - s_n(E)`;

- whether the discrepancy is already explained by known WP06/WP13 local terms.

### 6.4 Computational discipline

- Use reproducible scripts/notebooks and pinned software versions.
- Retain raw machine-readable outputs and human-readable summaries.
- Distinguish exact arithmetic from numerical analytic evaluation.
- Never promote observed stabilization to a theorem.
- Never use the atlas as a substitute for MATHCERT evidence.

Candidate computational literature or software interfaces, including explicit `2`-Selmer/Cassels-Tate methods such as Shukla-Stoll or successors, must be source-audited when their mathematical correctness is relied upon beyond routine software execution.

### 6.5 WP18 success criterion

WP18 succeeds if it either:

1. supports the exact determinant/Fitting theorem shape without unexplained defects; or
2. identifies a repeatable missing local/global correction, allowing the theorem target to be repaired before deeper proof work.

## 7. Cross-thread order of execution

The default order is:

1. **WP16A:** prove the elementary finite-level Selmer stabilization theorem.
2. **WP16B:** identify the exact Selmer-complex/determinant invariant.
3. **WP17A:** conduct narrowly targeted source reconnaissance against that exact invariant.
4. **WP18:** begin the atlas as soon as the finite-level invariant is fixed; run it in parallel with WP17 source admission.
5. **WP17B:** prove the strongest admissible integral theorem over `K` and descend it exactly.
6. **Decision gate:** nominate the final theorem-building package.

Do not begin with a broad literature survey. The WP16 invariant should determine what theorem is being searched for.

## 8. Decision gate after WP16-WP18

### Case A — one integral inclusion is proved

If the work yields

`Fitt_algebraic subseteq analytic_ideal`

or the reverse, isolate the missing opposite inclusion. The next work package should attack only the missing direction or the primitivity statement that implies it.

### Case B — algebraic determinant is controlled but analytic comparison is missing

Then the next theorem target is a narrowly specified `p=2` explicit reciprocity law. It must connect the exact integral Selmer/Euler-system object to the WP00-normalized complex leading term, including every local correction.

### Case C — atlas detects an unexplained correction

Do not force the old target. Identify whether the correction comes from:

- local condition at `2`;
- split/nonsplit multiplicative normalization;
- residual-conductor drop;
- quadratic descent;
- imprimitive/primitive Euler factors;
- period/regulator normalization;
- finite-level versus stabilized Selmer indexing.

Repair the theorem statement and replay the relevant prior deduction before continuing.

### Case D — candidate source theorem excludes `p=2`

Terminate that route immediately unless the proof itself is brought into MATHSOLVE and a genuine `p=2` extension is proved. Do not substitute analogy.

## 9. Claim firewall

Throughout WP16-WP18:

- `BSD-R2-A1` remains unproved until the exact protected equality is established and subsequently certified through the required MATHCERT route.
- Numerical data are observation only.
- Modulo squares and parity are not exact length.
- Odd-prime theorems do not specialize silently to `p=2`.
- Restricted twist-family or CM results do not become uniform selected-class results.
- “Up to a unit” does not become equality of integral ideals or lengths without proof.
- Search failure is not theorem nonexistence.
- Source admission is not mathematical certification.
- No novelty, priority, patentability, or commercial claim follows from this programme.

## 10. Exact-head and review discipline

For each substantive tranche:

1. re-fetch protected MATHSOLVE and any materially used provider head;
2. post or update the owner issue with an exact preflight before theorem mutation;
3. bind all theorem files to the exact protected baseline and admitted source identities;
4. keep source reconnaissance in MATHFORGE when it creates a new external theorem premise;
5. use non-authoring Adversary and Referee passes on the exact candidate head;
6. require ordinary repository CI and GCL conformance;
7. merge only the exact reviewed head;
8. read back protected main;
9. close the tranche owner only after protected readback;
10. update this handoff when the frontier changes materially.

Routine execution does not require Human Steward intervention unless a protected governing instrument reserves the transition.

## 11. Legitimate stop conditions

Stop only when one of the following is reached:

- the exact selected BSD equality is proved and the next step belongs to MATHCERT;
- a materially new external theorem premise is required and source admission cannot yet establish it;
- a genuinely new global `p=2` theorem must be invented beyond the bounded work package and its proof cannot be completed in the current tranche;
- target/hypothesis/normalization drift is detected;
- an authentication, authority, safety, or protected-state boundary prevents the next authorized action.

Recoverable CI, connector, tooling, source-fetch, formatting, or workflow failures are not stopping conditions.

## 12. Immediate next executable tranche

The smallest safe next tranche is **WP16A**:

> Prove the finite-level identity `s_n(E) = ord_2 #Sha(E/Q)[2^n]`, prove stabilization to the full `2`-primary Sha length, and state the resulting exact reformulation `delta_2(E) = lim_n s_n(E)`.

This tranche should require no new external theorem beyond already protected rank-one/finiteness/Kummer inputs. Only after WP16A is protected should the campaign commit to a particular Selmer-complex formalism for WP16B.