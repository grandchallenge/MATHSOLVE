# NS-CI-R014-A2-L5-43 — packet-weighted intrinsic compression overlap

## Disposition

- Campaign: NS-CI-001
- Restricted target: NS-CI-R014-A2
- Tracker: MATHSOLVE#59
- Protected mathematical predecessor: 5bbc55c82982328f2a3246e0de1ef8869595789b (L5-42)
- Protected integration base: 618840447a59af771ca7ce13a6f15cce3c3a5c06
- Result class: exact packet-weighted stopping theorem plus reconstruction-interface audit
- Result: PACKET_WEIGHTED_COMPRESSION_EXIT_LOSES_NO_EXPONENTIAL_FACTOR__CRITICAL_DENSITY_RECONSTRUCTION_REMAINS_OPEN
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-42 identified the intrinsic one-sided Eulerian compression variation

    V_v^- = integral_0^S integral (-partial_Y v)_+ dY ds

and proved the unweighted label estimate

    |C_K^-| <= exp(K) K^(-1) V_v^-.

The exponential factor appears because an Eulerian scalar budget is converted
back to unweighted label measure. The downstream object is instead the mass
of the critical packet or observable. Keeping that density inside the
Lagrangian integral removes the exponential loss exactly.

## 1. Direction flow and first compression time

Let chi solve

    partial_s chi(s,Z) = v(s,chi(s,Z)),   chi(0,Z)=Z,

with J(s,Z)=partial_Z chi(s,Z)>0. Then

    partial_s log J = partial_Y v(s,chi).

For K>0 define the first compression time tau_K^-(Z) as the first s in [0,S]
with log J(s,Z)=-K, capped at S, and define

    C_K^- = { Z : inf_{0<=s<=S} log J(s,Z) <= -K }.

Every Z in C_K^- satisfies

    K <= integral_0^{tau_K^-(Z)} (-partial_Y v(s,chi(s,Z)))_+ ds.

## 2. Exact packet-weighted stopping theorem

Let q(Z)>=0 be any fixed L1 label density and define

    W_{q,K}^-
      = integral q(Z)
          integral_0^{tau_K^-(Z)}
            (-partial_Y v(s,chi(s,Z)))_+ ds dZ.

Multiplying the first-hit inequality by q and integrating gives

    integral_{C_K^-} q(Z) dZ <= K^(-1) W_{q,K}^-.

No change of variables is used. Therefore no factor exp(K) appears.

Because the integrand is nonnegative, W_{q,K}^- <= W_q^-, where

    W_q^-
      = integral q(Z)
          integral_0^S (-partial_Y v(s,chi(s,Z)))_+ ds dZ.

Hence also

    integral_{C_K^-} q(Z) dZ <= K^(-1) W_q^-.

This is the exact packet-weighted first-order compression theorem.

## 3. Exact Eulerian representation

Set Z=chi^{-1}(s,Y) and define the pushed-forward density

    rho_q(s,Y)
      = q(chi^{-1}(s,Y)) / J(s,chi^{-1}(s,Y)).

Then

    rho_q(s,Y) dY = q(Z) dZ,

and rho_q obeys the continuity equation

    partial_s rho_q + partial_Y(v rho_q) = 0

in the classical setting, and in the corresponding weak sense at lower
regularity.

Therefore

    W_q^-
      = integral_0^S integral
          rho_q(s,Y) (-partial_Y v(s,Y))_+ dY ds.

For the stopped cost, let a_K(s,Z)=1_{s<tau_K^-(Z)}. Then

    W_{q,K}^-
      = integral_0^S integral
          a_K(s,chi^{-1}(s,Y))
          rho_q(s,Y)
          (-partial_Y v(s,Y))_+ dY ds.

This is the intrinsic Eulerian packet/compression overlap.

## 4. Why this is sharper than L5-42

L5-42 discarded packet location first and then returned from Eulerian space
to label measure using dZ=J^(-1)dY <= exp(K)dY before first compression.

Here the packet density is retained:

    q(Z)dZ = rho_q(s,Y)dY.

The Jacobian is already part of the transported density. No bootstrap bound
for J^(-1) is needed. Thus:

    unweighted Eulerian compression -> exp(K)/K loss
    packet-weighted compression overlap -> 1/K loss.

## 5. Persistent overlap is an intrinsic cost

Let E be a measurable subset of [0,S] x T. If

    (-partial_Y v)_+ >= gamma > 0

on E, then

    W_q^- >= gamma integral_E rho_q(s,Y) dY ds.

Thus persistent compressive strain overlapping transported packet mass cannot
hide from W_q^-.

This is a cost statement. It is not yet a selector-charge theorem.

## 6. Critical-scale family

For a family h -> 0, let q_h be fixed label densities and let rho_h be their
pushforwards by chi_h. If for some fixed K>0

    W_{q_h}^- -> 0,

then

    integral_{C_{K,h}^-} q_h(Z) dZ -> 0.

This gives exactly the almost-everywhere packet-mass conclusion required by
the first-order tangent route, without uniform integrability and without
smallness of the unweighted compression set.

## 7. Critical-observable reconstruction audit

L5-40 introduced q_h(Z)dZ only as a nonnegative label-space density
representing the portion of a critical observable under consideration.
L5-41 retained the same abstract interface.

No protected result currently supplies an identity

    q_h = Q[A_h, F_h, J_h]

for the L5-35 metric moment.

No protected result proves that the abstract q_h is a material density
transported by the direction characteristic.

No protected result supplies an NF5-style reconstruction theorem converting
large W_{q_h}^-, or large q_h-mass on C_{K,h}^-, directly into a physical
Littlewood-Paley threshold event.

Therefore a selector-charge conclusion cannot be derived from the current
protected hypotheses without an additional reconstruction theorem.

## 8. Relation to L5-35

L5-35 has explicit metric-weighted physical moments

    M2 = integral J^(-1) |F_Z A|^2 dZ

and

    M4 = integral J^(-3) |F_Z|^4 |A|^2 dZ.

Their integrands are candidate sources for an actual critical-observable
density, but the identification is not automatic:

- they depend on the current frame;
- they are not shown to satisfy the continuity equation above;
- fourth-moment control remains separate;
- finite-h LP reconstruction has not been localized to compressed labels.

This tranche therefore does not identify either moment integrand with q_h.

## 9. Exact interface split

The selected whole-space problem now separates into two interfaces.

Geometric transport:

    q_h -> rho_h -> packet/compression overlap -> compressed q_h-mass.

Physical reconstruction:

    q_h or rho_h -> physical critical observable -> LP block -> selector charge.

The first interface is now exact for any fixed label density.
The second interface is absent from the protected hypotheses.

## 10. Hard rejection tests

Reject any successor that:

- reintroduces exp(K) after retaining a label-space packet density;
- treats an arbitrary q_h as automatically transported by the characteristic;
- identifies the L5-35 second-moment integrand with q_h without deriving its evolution;
- infers selector charge from large W_q^- without LP reconstruction;
- assumes physical incompressibility makes the frame-density overlap vanish;
- promotes tangent control to U2, U3, or U4;
- reopens L3 or L4 without their protected reopening conditions.

## 11. Claim boundary

Protected disposition:

PACKET_WEIGHTED_COMPRESSION_EXIT_LOSES_NO_EXPONENTIAL_FACTOR
__CRITICAL_DENSITY_RECONSTRUCTION_REMAINS_OPEN

It proves:

- exact packet-weighted first-hit compression control;
- removal of the L5-42 exp(K) loss when packet density is retained;
- exact Eulerian continuity-density representation;
- persistent compression overlapping transported packet mass forces positive
  intrinsic packet-compression cost;
- the prior q_h interface is not yet tied by a protected theorem to the
  L5-35 metric moment or NF5 reconstruction.

It does not prove selected NSE makes W_{q_h}^- small.
It does not prove persistent overlap pays selector charge.
It does not control U2, U3, or U4.
It does not prove A2.
No MATHCERT, novelty, priority, publication, patent, product, or commercial claim is asserted.

## 12. Next live obligation

C2-MIX-DIRECTION-CRITICAL-DENSITY-RECONSTRUCTION:

Construct an equation-derived critical-observable density from the actual
selected packet, prove its relation to the direction characteristic
(transported, source-driven, or otherwise), and derive the reconstruction
rule that converts compressed critical mass into a physical LP threshold or
selector/dissipation charge.

Audit the L5-35 second-moment density first. Higher frame jets remain downstream.