# NSCI-C2-B-COOP-001 — contribution adjudication

## Binding

- Campaign: NS-CI-001
- Restricted target: NS-CI-R014-A2
- Dispatch: NSCI-C2-B-COOP-001
- Assignment: B — D4 physical-charge audit
- Protected raw-evidence merge: 8b2bdb2f0be6515b2eedea1d784d2d97f53c694e
- GitHub issue: #426
- GitHub comment: 5768723180
- Raw SHA-256: 3a86149e1cfac0ea3dc6ec1e43a4efeb19e7745b5e2ab011b3606de9583bb2f9
- Contributor disposition: REFUTED
- Intake state at adjudication start: received_unadjudicated
- MATHCERT status: absent
- Canonical A2 status: open

This record adjudicates mathematical content only. It does not alter the immutable raw contribution or intake receipt.

## Formalist review

### F1 — exact moment-level separator: ACCEPT

The contribution's core construction is correct as a separator for the moment-reconstruction interface.

Fix S > 0, K > 0, and a fixed scaled annulus 0 < c_- < c_+ < infinity. Choose a nonnegative integrable profile w on [0,S] with w(0)=0 and integral w(s) ds = 1. For sufficiently large lambda > c_+, define

    delta_lambda(s) = K w(s) / lambda^4

so that 0 <= delta_lambda(s) <= 1, and define the spectral probability measure

    mu_s^(lambda)
      = (1-delta_lambda(s)) delta_0
        + delta_lambda(s) delta_lambda.

Then

    M0(s) = 1,
    Q4(s) = K w(s),
    D4 = integral_0^S Q4(s) ds = K,
    Q2(s) = K w(s) / lambda^2,

and the measure of [c_-,c_+] is zero for every s. Hence sup_s Q2(s) tends to zero as lambda tends to infinity while D4 remains fixed and positive. Because w(0)=0, the separator also respects the protected moment-level initialization Q2(0)=0.

Therefore a positive lower bound on D4, together with finite positive zeroth mass, does not by itself imply positive mass in any fixed scaled annulus or a positive Q2 lower bound.

This is a theorem about the moment interface. It is sufficient to reject any proposed bridge that uses only those moment facts.

### F2 — packet realizability: NOT ESTABLISHED

The raw contribution calls the two-point measures valid limiting packet states. That stronger statement is not established.

The protected L5-35 packet variables satisfy coupled evolution equations for J, H, and R, including H(0,Z)=0 and

    R_s = -2 J^(-2) H^2 R.

No construction in the contribution realizes the abstract two-point measure family by such a packet trajectory.

The accepted theorem is therefore deliberately limited to the spectral-moment interface. It is not a dynamical L5-35 realization theorem and is not a selected whole-space NSE counterexample.

### F3 — physical-order interpretation: ACCEPT WITH BOUNDARY

Under the physical scaling already supplied by the dispatch,

    dt = h^2 / (nu N^2) ds

and physical frequency is of order N h^(-1) xi for xi = h n.

With the protected normalization

    ||u||_2^2 ~ N^(-1) M0,

the corresponding derivative orders scale as

    ||grad u||_2^2 ~ N h^(-2) Q2,
    ||grad^2 u||_2^2 ~ N^3 h^(-4) Q4.

Thus

    nu integral ||grad u||_2^2 dt
      ~ N^(-1) integral Q2 ds,

whereas

    nu integral ||grad^2 u||_2^2 dt
      ~ N h^(-2) D4.

Consequently D4 is a higher-differential-order packet quantity. The finite Leray-Hopf L_t^2 Hdot^1 energy budget does not, from the supplied inputs alone, give a uniform direct bound on D4.

This is a scaling/interface conclusion. It is not a new global Hdot^2 estimate and does not prove that every large-D4 episode occurs in a selected NSE solution.

### F4 — necessary-and-sufficient concentration criterion: REJECT AS STATED

The contribution claims that a bound

    M0 Q4 / Q2^2 <= C_*

plus an upper envelope for Q4 is necessary and sufficient for converting D4 into fixed critical-band mass.

The derivation does not prove necessity.

The sufficiency statement is also under-specified. To obtain a fixed annulus from the stated Paley-Zygmund/Markov route one must explicitly supply enough uniform information to fix both lower and upper frequency cutoffs on a positive-measure time set. At minimum, the proof must account for:

- a positive-measure subset on which Q4 is bounded below;
- an upper bound on Q4;
- the moment-ratio bound;
- the mass normalization needed to turn normalized moment bounds into fixed physical mass and a fixed lower scaled frequency.

A lower bound on D4 plus an upper bound on Q4 can produce a positive-measure set with Q4 bounded below, but the remaining normalization hypotheses must still be stated and proved in the packet setting.

No minimal, necessary, or necessary-and-sufficient claim is admitted.

## Adversary review

### A1 — high-frequency escape

The two-point construction survives. For every fixed annulus, the positive fourth moment can be carried by vanishing mass at frequency lambda tending to infinity. This defeats any D4-only fixed-annulus conclusion.

### A2 — protected initialization

The raw constant-in-time example would have Q2(0) > 0, while the protected packet normalization has Q2(0)=0. The corrected profile w(0)=0 removes this defect at the moment level. It still does not establish packet realizability.

### A3 — dynamical consistency

No argument shows that arbitrary mu_s^(lambda) satisfying the desired moments is generated by the coupled L5-35 characteristic equations. Any successor must not promote the moment separator into a packet or NSE counterexample without a realization theorem.

### A4 — concentration criterion

The necessary-and-sufficient wording fails. The contribution gives, at most, the outline of one sufficient moment-tightness route after additional uniform hypotheses. Alternative mechanisms could yield fixed-band mass without that exact kurtosis condition, so necessity is unsupported.

### A5 — physical dissipation identification

Calling D4 ordinary Leray dissipation is rejected. Under the supplied scaling it is one derivative order above the finite Leray-Hopf dissipation budget and carries the singular h^(-2) factor after physical-time restoration.

## Referee disposition

PARTIAL_ADMISSION__D4_ALONE_ROUTE_REFUTED_AT_MOMENT_INTERFACE

### Admitted

1. D4 > 0 alone does not force positive mass in any fixed scaled critical annulus at the moment-measure interface.
2. D4 > 0 alone does not force a positive Q2 lower bound at the moment-measure interface.
3. Under the supplied packet scaling, D4 is a higher-order quantity with no direct finite Leray-Hopf dissipation-budget control from the stated inputs.
4. Any successful D4-based selector bridge therefore requires additional tightness, localization, lower-moment information, or an equation-specific dynamical mechanism.

### Not admitted

1. The abstract separator is not established as an actual L5-35 packet trajectory.
2. It is not a whole-space NSE counterexample.
3. The proposed kurtosis condition is not established as necessary.
4. The proposed kurtosis-plus-Q4-envelope package is not admitted as a complete sufficient theorem in its present form.
5. No MATHCERT, A2, novelty, priority, publication, or certification claim is made.

## Campaign effect

The branch convert-large-D4-directly-into-selector-charge-from-sign-and-size-alone is closed negatively at the protected moment-reconstruction interface.

The live residual is narrower:

1. prove a correctly quantified D4-plus-tightness/Q2 reconstruction lemma on a positive-measure time set and derive its needed hypotheses from selected dynamics; or
2. close another compression-ledger channel, especially Q2(S), C2^+, or P_tot.

The Assignment-A blind cohort is unaffected and remains sealed.
