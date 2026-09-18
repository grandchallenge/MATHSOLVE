# RH-R034-RINDLER-PRIME-FIXED-DOMAIN-001 — Prime mechanism confirmed; fixed-domain zero correspondence not established

- Campaign: RH-001
- Solve tracker: grandchallenge/MATHSOLVE#358
- Protected provider audit: grandchallenge/MATHFORGE@2e66cdb836ea4228d70462f5eddca73ee91a504a
- Predecessor: RH-R033-SYMMETRIC-BK-TLOGT-001
- Parent campaign route: RH-T-200 — Hilbert–Pólya sufficient-route contract
- Terminal target: RH-T-000 — OPEN
- Novelty / priority claim: none
- Certification status: not certified; MATHSOLVE theorem-development result only

## 1. Purpose

RH-R033 established that one fixed self-adjoint discrete operator family can reproduce the first two smooth Riemann counting terms. The next missing ingredient was the arithmetic fluctuation mechanism: prime-labelled structure that is independently specified rather than reconstructed from the target zero list.

Sierra's 2014 Rindler mirror model supplies a concrete positive control for that ingredient. Its mirror geometry and Möbius reflection amplitudes encode prime structure without taking the zero ordinates as input.

However, the published point-state construction does not establish one fixed self-adjoint operator containing all target ordinates as eigenvalues. The observer-boundary phase is fine-tuned to the target zero, and several additional source steps are conditional, formal, or limiting.

This package records that exact positive/negative boundary.

## 2. Exact imported source class

The protected MATHFORGE audit binds the source to Germán Sierra (2014), DOI 10.1088/1751-8113/47/32/325204.

The model is a massless Dirac Hamiltonian in the right Rindler wedge with an infinite sequence of mirror interactions. A self-adjoint realization is characterized by:

- a boundary phase \(e^{i\vartheta}\) at the observer worldline \(\rho=\ell_1\);
- fixed mirror locations \(\ell_n\);
- fixed reflection data \(r_n,r'_n\).

For one fixed self-adjoint operator, all of these data, including \(\vartheta\), are part of the operator/domain identity and must be fixed independently of the spectral value under test.

All operator-theoretic statements in this section are imported from the protected source audit; Solve does not independently certify the paper's limiting construction.

## 3. Independently specified arithmetic mechanism

For the Riemann model, the source chooses

\[
\ell_n=n^{1/2},
\qquad
\varrho_n=\varepsilon\,\frac{\mu(n)}{n^\sigma},
\]

where \(\mu(n)\) is the Möbius function.

This supplies arithmetic information independently of the zeta-zero list.

At the source-model level:

- the mirror geometry produces primitive trajectories associated with primes;
- the corresponding observer-time periods are \(\log p\);
- the reflection amplitudes encode multiplicative information through \(\mu(n)\).

Therefore the campaign may admit the following bounded positive result:

\[
\boxed{\text{prime-labelled arithmetic structure can be specified without inserting the target zero ordinates}}
\]

This closes the specific mechanism deficit identified in RH-R033. It does not yet establish any zero-to-eigenvalue theorem.

## 4. Fixed-domain obstruction in the published point-state construction

Near a critical-line zero

\[
\zeta\left(\frac12+iE_n\right)=0,
\]

the source derives a normalizability condition involving the Riemann–Siegel phase and the observer-boundary phase. For positive zeros, the source writes a target-dependent phase of the form

\[
\frac{\vartheta(E_n)}{\pi}
=
n+\frac12-\frac{\theta(E_n)}{\pi}
\]

up to the source's indexing convention, and explicitly states that to "hear" a given zero one must fine-tune \(\vartheta\).

The governed consequence is exact.

### Proposition RH-P034-FIXED-DOMAIN

If the self-adjoint boundary parameter \(\vartheta\) is chosen as a function of the target ordinate \(E_n\), then the resulting point-state construction does not by itself define one fixed self-adjoint operator whose point spectrum contains all target ordinates.

### Proof

The boundary phase is part of the self-adjoint domain data. Let \(H_{\vartheta}\) denote the self-adjoint realization obtained with fixed mirror data and fixed phase \(\vartheta\).

If the construction for \(E_n\) requires \(\vartheta=\vartheta(E_n)\), while the construction for \(E_m\) requires a different value \(\vartheta(E_m)\), then the two states belong to spectral problems for different self-adjoint realizations:

\[
H_{\vartheta(E_n)}
\quad\text{and}\quad
H_{\vartheta(E_m)}.
\]

No single fixed operator follows unless one proves the existence of one energy-independent phase \(\vartheta_*\) for which every target ordinate is an eigenvalue of \(H_{\vartheta_*}\).

The published construction does not prove such a theorem.

QED.

This proposition does not prove that no fixed-phase repair exists. It proves only that target-dependent tuning is insufficient evidence for the protected Hilbert–Pólya contract.

## 5. Conditional reciprocal-zeta boundary

In the weak-reflection calculation, the source obtains formally

\[
e^{-i\Phi_\infty}R_\infty
=
\varepsilon
\sum_{n=1}^{\infty}
\frac{\mu(n)}{n^{\sigma+iE}}
=
\frac{\varepsilon}{\zeta(\sigma+iE)}.
\]

The protected audit records the source's own qualification:

- for \(\sigma\ge 1\), the reciprocal-zeta Dirichlet series is in its unconditional convergence region;
- for \(1/2<\sigma<1\), the source invokes the representation conditionally on RH.

Therefore an argument that imports this critical-strip identity under RH may not later use it as an independent proof of RH.

This is a circularity exclusion, not a judgment about possible alternative derivations.

## 6. Additional source obligations blocking an RH claim

The provider audit binds four additional unresolved obligations.

### 6.1 Simple-zero assumption

The critical-line point-state analysis assumes the target zero is simple. General simplicity of all nontrivial zeta zeros is not established.

### 6.2 Formal residue/Perron step

The finite partial-sum analysis uses residue formulas that the source itself describes as formal and whose validity range is left for future proof.

### 6.3 Weak-coupling / infinite-array limit

The spectral construction is studied through an infinitesimal-reflection and infinite-mirror limit. For an exact Hilbert–Pólya theorem, one needs a fixed limiting self-adjoint operator together with rigorous operator/domain convergence and spectral control.

### 6.4 Off-critical-zero contradiction

The source argues heuristically that an off-critical zero would produce a contribution incompatible with normalizability and notes an apparent tension with self-adjointness. It also explicitly cautions that this argument rests on unproved assumptions.

Accordingly, the campaign may not promote that passage to an RH proof.

## 7. Exact theorem-development result

### Theorem RH-R034-RINDLER-PRIME-FIXED-DOMAIN-001

The protected Sierra source supports the following governed conclusions.

1. A concrete prime-labelled arithmetic mechanism can be specified independently of the target zeta-zero list.
2. The published critical-line point-state construction does not establish one fixed self-adjoint Hilbert–Pólya operator for all target ordinates because the observer-boundary phase is target-zero dependent.
3. The source's RH-like off-critical-zero contradiction is not admissible as an RH proof in the campaign because material steps remain RH-conditional, simple-zero-dependent, formal, or uncontrolled in the weak-coupling/infinite-array limit.
4. Therefore the live spectral frontier is to retain the independently specified prime mechanism while replacing target-dependent spectral tuning with one fixed energy-independent self-adjoint domain and a rigorous limiting spectral theorem.

The theorem is a governed source-semantic and operator-contract result. It does not prove or disprove RH.

## 8. Proof-obligation DAG

    RH-P034-01  bind exact Rindler mirror source/model
          |
          +--> RH-P034-02  arithmetic mirror data are zero-list independent
          |         |
          |         v
          |    prime-labelled log(p) mechanism admitted
          |
          +--> RH-P034-03  self-adjoint boundary phase is domain data
                    |
                    v
              target-specific vartheta(E_n)
                    |
                    v
    RH-P034-04  one fixed all-zero domain not established

    RH-P034-05  reciprocal-zeta critical-strip use is RH-conditional
    RH-P034-06  simple-zero assumption is material
    RH-P034-07  residue formulas include formal steps
    RH-P034-08  weak-coupling/infinite-array spectral limit not closed
          \        |        |        /
                   v
    RH-P034-09  source RH-like contradiction not admissible as proof

    RH-P034-04 + RH-P034-09
                   |
                   v
    RH-P034-10  frontier = fixed domain + rigorous noncircular prime spectrum

## 9. False-proof firewall

Reject the following moves.

1. Prime-labelled dynamics do not imply a zero-to-eigenvalue correspondence.
2. A different boundary phase for each target zero is not one fixed self-adjoint operator.
3. Numerical concentration of the target-dependent phases near one value does not prove that one exact constant phase works for all zeros.
4. An RH-conditional reciprocal-zeta identity cannot be used to prove RH.
5. An all-zero conclusion may not rest on a simple-zero assumption without discharging multiplicity.
6. Formal residue identities may not be promoted to exact spectral theorems.
7. Weak-coupling or infinite-array heuristics may not substitute for operator/domain/spectral convergence.
8. A heuristic contradiction with self-adjointness does not establish RH while these assumptions remain open.

## 10. Non-implications

This package does not:

- prove or disprove RH;
- show that Sierra's model fails for every fixed boundary phase;
- exclude repaired Rindler or prime-mirror models;
- prove convergence of the infinite mirror Hamiltonian;
- prove exact point-spectrum correspondence with zeta zeros;
- claim novelty or priority;
- certify the source theorem or render a MATHCERT disposition.

## 11. Next smallest safe target

The next tranche should no longer ask merely whether primes can appear in a fixed spectral model. RH-R034 answers that mechanism question positively.

The next exact target must address the missing composition:

\[
\text{fixed prime-labelled arithmetic data}
+
\text{one energy-independent self-adjoint domain}
+
\text{rigorous limiting operator}
\Longrightarrow
\text{noncircular point-spectrum selection}.
\]

Before selecting a new operator class, MATHFORGE should audit current literature for one of two things:

1. a fixed-domain Rindler/prime-mirror repair that removes the target-dependent phase tuning and proves a limiting spectral theorem; or
2. a different fixed self-adjoint construction with prime-labelled trace/orbit structure and no zero-dependent parameters.

A claimed construction that hard-codes the known zero ordinates, spectral determinant, or Riemann–Siegel phase into adjustable domain data does not satisfy this gate.

## 12. Terminal state

RH-R034_PROVED__PRIME_MECHANISM_CONFIRMED__FIXED_DOMAIN_CORRESPONDENCE_OPEN

RH-T-000 remains open.
