# NS-CI-WP02 — Source-normalized conditional-regularity ledger

## Status

- Campaign: `NS-CI-001`
- Work Package: `WP02`
- Parent: `grandchallenge/MATH-PROGRAMME#55`
- Tracker: `grandchallenge/MATHSOLVE#20`
- Result class: source-normalized reconstruction of classical conditional analysis
- Claim boundary: this ledger does not prove universal critical integrability or global regularity.

## Canonical whole-space problem

Let `u_0` be smooth, divergence-free, and rapidly decreasing with every derivative in the sense of Fefferman's whole-space positive branch. Let `u` be a Leray–Hopf weak solution of

```math
\partial_tu-\nu\Delta u+(u\cdot\nabla)u+\nabla p=0,
\qquad \nabla\cdot u=0
```

on `\mathbb R^3`. Define

```math
I_T(u)=\int_0^T\|u(t)\|_{L^6(\mathbb R^3)}^4dt.
```

The open target asks whether `I_T(u)<\infty` for every finite `T`, every admissible datum, and every Leray–Hopf solution.

## Source normalization policy

Historical priority, operational theorem use, and programme inference are separate fields.

- `NS-CI-SRC-PRODI-1959` supplies the original uniqueness exponent law, with space exponent `6` giving time exponent `4`.
- `NS-CI-SRC-SERRIN-1962` and `NS-CI-SRC-LADYZHENSKAYA-1967` remain historical sources whose exact theorem-body normalization is incomplete.
- `NS-CI-SRC-OPERATIONAL-LPS-2024` supplies the explicit modern whole-space Leray–Hopf theorem interface used operationally.
- `NS-CI-SRC-OZANSKI-POOLEY` supplies a modern reconstruction of Leray's local strong theory, global weak existence, blow-up lower bounds, and weak–strong uniqueness.
- `NS-CI-SRC-CLAY-FEFFERMAN` fixes the official whole-space data and solution classes.

An operational theorem does not erase historical provenance debt. Historical provenance debt does not prevent use of a separately audited modern theorem.

---

## CR-000 — Domain, forcing, data, and norm convention

### Hypotheses

- Domain: `\mathbb R^3`.
- Viscosity: `\nu>0`.
- Forcing: zero.
- Data: smooth, divergence-free, rapidly decreasing with every derivative.
- Mixed norm: `L_t^qL_x^p`, with time exponent written first.
- Critical pair: `(q,p)=(4,6)`.

### Criticality

```math
\frac2q+\frac3p=\frac24+\frac36=1.
```

### Prohibited drift

- Reversing the pair to `L_t^6L_x^4`.
- Replacing the full rapid-decay class by compact support without naming a restricted lane.
- Transferring a periodic or bounded-domain theorem without a domain bridge.

---

## CR-001 — Leray–Hopf existence and energy inequality

### Operational source

- `NS-CI-SRC-OZANSKI-POOLEY`, audited at statement level.
- Historical source: `NS-CI-SRC-LERAY-1934`, exact theorem concordance pending.

### Working theorem interface

For divergence-free `u_0\in L^2(\mathbb R^3)`, there exists a global weak solution satisfying

```math
u\in L^\infty(0,T;L^2)
\cap L^2(0,T;\dot H^1)
```

for every finite `T`, together with the energy inequality

```math
\|u(t)\|_2^2
+2\nu\int_0^t\|\nabla u(s)\|_2^2ds
\le \|u_0\|_2^2
```

for the selected representative and admissible times in the operational theorem.

### Claim state

`LITERATURE_DERIVED / OPERATIONAL_SOURCE_AUDITED`.

### Downstream use

Supports `CR-003`, weak compactness, and the existence arrow in `CR-009`.

### Unresolved debt

Exact theorem-number and representative convention in Leray's original paper.

---

## CR-002 — Three-dimensional Sobolev bridge

For suitable whole-space fields,

```math
\|v\|_6\le C_S\|\nabla v\|_2.
```

This is used in the homogeneous whole-space sense. The energy inequality therefore controls the `L^6` norm only in square-integrable time.

### Claim state

`STANDARD_CONTINUUM_LEMMA`.

### Formalization route

Whole-space Sobolev infrastructure and Bochner integration; no Navier–Stokes-specific theorem is required.

---

## CR-003 — Energy consequence

Combining `CR-001` and `CR-002`,

```math
\int_0^T\|u(t)\|_6^2dt
\le C_S^2\int_0^T\|\nabla u(t)\|_2^2dt
\le \frac{C_S^2}{2\nu}\|u_0\|_2^2.
```

Thus

```math
u\in L_t^2L_x^6.
```

### Boundary

This does not imply `L_t^4L_x^6`. WP01 fixture `FP-001` gives the exact scalar obstruction, and `FP-002` shows that energy interpolation yields `L_t^4L_x^3` instead.

---

## CR-004 — Operational LPS theorem at `(4,6)`

### Source state

- Historical exponent/uniqueness source: `NS-CI-SRC-PRODI-1959`.
- Historical regularity source: `NS-CI-SRC-SERRIN-1962`.
- Historical smoothness/uniqueness source: `NS-CI-SRC-LADYZHENSKAYA-1967`.
- Operational explicit theorem: `NS-CI-SRC-OPERATIONAL-LPS-2024`, Theorem 1.1.

### Operational statement

For two Leray–Hopf weak solutions with the same initial datum on `\mathbb R^3`, if one solution satisfies

```math
u\in L^r(0,T;L^q(\mathbb R^3)),
\qquad \frac2r+\frac3q=1,
\qquad q\in(3,\infty],
```

then uniqueness holds on the interval. At `r=4`, `q=6`, this is the campaign norm. For `H^1` initial data, the solution lies in the strong class on `[0,T]`; for `L^2` data, it is strong on `[t_*,T]` for every `t_*>0`, under the source's precise convention.

### Claim state

`LITERATURE_DERIVED / OPERATIONAL_STATEMENT_AUDITED`.

### Prohibited overstatement

This theorem consumes the critical hypothesis. It does not prove that the hypothesis holds universally.

---

## CR-005 — Exact `H^1` differential inequality

### Regularity level

Perform the calculation for a smooth or sufficiently strong solution, or for a regularized approximation with all limit passages justified. It is not an unconditional Leray–Hopf test.

### Step 1: test by `-\Delta u`

Using incompressibility and whole-space decay,

```math
\frac12\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
=-\int_{\mathbb R^3}(u\cdot\nabla)u\cdot\Delta u\,dx.
```

The pressure term cancels at this regularity because `\nabla\cdot\Delta u=0` and the relevant integrations by parts are valid.

### Step 2: Hölder

```math
\left|\int(u\cdot\nabla)u\cdot\Delta u\right|
\le \|u\|_6\|\nabla u\|_3\|\Delta u\|_2.
```

### Step 3: Gagliardo–Nirenberg

```math
\|\nabla u\|_3
\le C\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{1/2}.
```

Hence

```math
|\text{nonlinear term}|
\le C\|u\|_6
\|\nabla u\|_2^{1/2}
\|\Delta u\|_2^{3/2}.
```

### Step 4: Young

Using conjugate exponents `4/3` and `4`, with viscosity inserted,

```math
C\|u\|_6\|\nabla u\|_2^{1/2}\|\Delta u\|_2^{3/2}
\le \frac\nu2\|\Delta u\|_2^2
+C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

Therefore

```math
\frac d{dt}\|\nabla u\|_2^2
+\nu\|\Delta u\|_2^2
\le C\nu^{-3}\|u\|_6^4\|\nabla u\|_2^2.
```

### Structural conclusion

The fourth power is forced by the `3/2` power of `\|\Delta u\|_2` and Young's exponents. It is not selected cosmetically.

### Grönwall consequence

If `I_t(u)<\infty`, then

```math
\|\nabla u(t)\|_2^2
\le
\|\nabla u_0\|_2^2
\exp\!\left(C\nu^{-3}I_t(u)\right).
```

### Claim state

`CONTINUUM_PROOF_RECONSTRUCTION`.

### Protected by WP01

- `FP-004`: circular closure.
- `FP-005`: inadmissible testing at weak regularity.
- `FP-006`: pressure cancellation does not create admissibility.

---

## CR-006 — Weak–strong difference inequality

Let `u` be a strong solution and `v` a Leray–Hopf solution with the same initial datum. Set `w=v-u`. Formally, then rigorously by the standard weak–strong argument,

```math
\frac12\frac d{dt}\|w\|_2^2
+\nu\|\nabla w\|_2^2
=-\int (w\cdot\nabla)u\cdot w\,dx.
```

Using incompressibility,

```math
\int (w\cdot\nabla)u\cdot w
=-\int (w\cdot\nabla)w\cdot u.
```

Then

```math
\left|\int (w\cdot\nabla)w\cdot u\right|
\le \|u\|_6\|w\|_3\|\nabla w\|_2.
```

Gagliardo–Nirenberg gives

```math
\|w\|_3
\le C\|w\|_2^{1/2}\|\nabla w\|_2^{1/2},
```

so Young yields

```math
\frac d{dt}\|w\|_2^2
+\nu\|\nabla w\|_2^2
\le C\nu^{-3}\|u\|_6^4\|w\|_2^2.
```

If `u\in L_t^4L_x^6` and `w(0)=0`, Grönwall gives `w=0`.

### Claim state

`CONTINUUM_PROOF_RECONSTRUCTION`, aligned with the operational weak–strong theorem.

### Quantifier role

This is the bridge from one strong solution to every Leray–Hopf solution with the same datum on the interval.

---

## CR-007 — Maximal-time continuation criterion

Let `u` be the maximal `H^1` strong solution on `[0,T_*)` supplied by the local theory. Suppose

```math
\int_0^{T_*}\|u(t)\|_6^4dt<\infty.
```

Then `CR-005` gives a uniform `H^1` bound on `[0,T_*)`. Choose times `t_n\uparrow T_*`. The local existence theorem, applied at `t_n`, has a lifespan bounded below in terms of the uniform `H^1` bound and `\nu`. For sufficiently large `n`, this extends the strong solution beyond `T_*`, contradicting maximality.

Therefore

```math
T_*<\infty
\quad\Longrightarrow\quad
\int_0^{T_*}\|u(t)\|_6^4dt=\infty.
```

### Source route

- Local strong existence and maximal-time framework: `NS-CI-SRC-OZANSKI-POOLEY`.
- Critical control: `CR-005`.

### Required semantic detail

The restart time, solution topology, and lifespan dependence must match the local theorem. The ledger uses the operational `H^1` interface; it does not claim a more general endpoint continuation theorem.

---

## CR-008 — Conditional regularity of a Leray–Hopf solution

Assume a Leray–Hopf solution satisfies

```math
u\in L^4(0,T;L^6(\mathbb R^3)).
```

The operational LPS theorem places it in the strong class on the appropriate interval, depending on the initial data regularity. For the campaign's smooth rapid-decay data, the initial datum is in `H^1`, so the strong interval begins at time zero. `CR-006` then identifies every Leray–Hopf solution with that strong solution.

### Conclusion

Critical integrability implies regularity and uniqueness on `[0,T]` for the campaign data class.

### Boundary

This remains conditional. No step supplies the critical integrability hypothesis.

---

## CR-009 — One-way implication to Fefferman statement (A)

### Assumption

For every smooth divergence-free rapidly decreasing datum in Fefferman's whole-space class, every corresponding Leray–Hopf solution satisfies

```math
I_T(u)<\infty
```

for every finite `T`.

### Chain

1. `CR-001` supplies at least one global Leray–Hopf solution.
2. The universal assumption gives that solution `L_t^4L_x^6` control on every finite interval.
3. `CR-008` upgrades it to the strong class and gives weak–strong uniqueness.
4. `CR-007` excludes finite maximal strong-solution time.
5. Standard parabolic bootstrapping from smooth rapidly decreasing data yields the smooth velocity and pressure class required by the official positive branch, with the energy bound inherited from `CR-001`.

### Promoted conclusion

Universal full-data critical integrability is **sufficient for** Fefferman's whole-space statement (A).

### Claim state

`CHECKED_ONE_WAY_BRIDGE`, conditional on the audited operational theorem interfaces.

### Prohibited wording

Do not call this bidirectional equivalence until `CR-010` is discharged.

---

## CR-010 — Reverse correspondence

### Desired statement

Starting from the exact globally smooth solution class in Fefferman statement (A), prove that:

1. the smooth solution belongs to `L_t^4L_x^6` on every finite interval;
2. every Leray–Hopf solution with the same datum agrees with it;
3. the quantifiers and decay/energy conditions match the canonical campaign target.

### Current state

`PENDING_SOURCE_NORMALIZATION`.

### Why separate

Smoothness on space-time does not by itself encode the precise whole-space integrability and uniformity assumptions needed for the mixed norm. These properties are expected under the official decay and energy class, but the campaign requires a written bridge rather than an informal assertion.

### Promotion condition

Provide an authoritative strong-class theorem or a complete derivation of finite-interval `L_t^4L_x^6` membership and weak–strong identification in the exact official class.

---

## CR-011 — Compact-support restricted lane

`NS-CI-R-COMPACT` replaces the full data class by

```math
u_0\in C_c^\infty(\mathbb R^3).
```

This is a strict subclass of the rapidly decreasing class. A theorem in this lane advances a restricted target only.

### Missing extension bridge

To promote a compact-support theorem to the full data class, one needs:

- approximation of rapidly decreasing data by compactly supported divergence-free data;
- uniform critical estimates along the approximation;
- stability or convergence strong enough to pass the `L_t^4L_x^6` bound;
- preservation of the universal weak-solution quantifier.

No such bridge is assumed.

---

## Dependency chain

```text
CR-000
  ├─> CR-001 ─> CR-003
  ├─> CR-002 ─> CR-003
  ├─> CR-004 ─> CR-008
  ├─> CR-005 ─> CR-007
  ├─> CR-006 ─> CR-008
  └─> full-data universal hypothesis
          └─> CR-009 ─> Fefferman statement (A)

Fefferman statement (A) ─> CR-010 [pending]
NS-CI-R-COMPACT ─> data-class extension [missing]
```

## Proof and source debt

| Debt | State | Blocking WP02 ledger? | Blocking open theorem? |
|---|---|---:|---:|
| Leray original theorem concordance | pending historical audit | no | no |
| Serrin original theorem-body extraction | pending | no | no |
| Ladyzhenskaya mathematical translation | pending | no | no |
| Modern operational LPS theorem | audited | no | no |
| Reverse Clay correspondence | pending | no | no |
| Universal critical estimate | open | not a WP02 deliverable | yes |
| Compact-support extension | absent | no | blocks full-data promotion of restricted result |
| Lean scaling formalization | separate MATHCERT route | no | no |

## Acceptance record

WP02 is internally complete when:

- every theorem entry is mirrored in the machine-readable ledger;
- the `H^1` and difference estimates are independently checked;
- source IDs resolve to the MATHFORGE source ledger;
- no historical source is represented as more fully audited than it is;
- `CR-009` remains one-way;
- `CR-010` and the compact-support extension remain explicit debt;
- no statement implies that the universal estimate has been proved.