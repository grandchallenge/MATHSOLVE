# NS-CI-R014-A2-L5-44 — critical second-moment density balance

## Disposition

- Campaign: NS-CI-001
- Restricted target: NS-CI-R014-A2
- Tracker: MATHSOLVE#59
- Protected mathematical predecessor: f03793eb9eddcd5ca9222eb0f66750671e97a8ba (L5-43)
- Protected integration base: f03793eb9eddcd5ca9222eb0f66750671e97a8ba
- Result class: exact L5-35 limiting density-balance identity
- Result: CRITICAL_SECOND_MOMENT_DENSITY_HAS_EXACT_COMPRESSION_PRODUCTION__BALANCE_CHANNELS_IDENTIFIED
- A2 theorem: open
- L5: active
- L3/L4: closed
- MATHCERT adjudication: absent

L5-43 showed that packet-weighted compression is the correct intrinsic
first-order object, but the previous q_h interface was abstract.

This tranche instantiates the actual limiting L5-35 critical second-moment
density and derives its exact evolution law.

## 1. Protected L5-35 limiting variables

Use the L5-35 characteristic frame. Write

    alpha(s,Z) = partial_Y v(s,chi(s,Z)),
    J_s = alpha J,
    F_s = G(s,chi(s,Z)),
    H = F_Z.

Then

    H_s = J (partial_Y G)(s,chi(s,Z)).

Let A be the limiting L5-35 amplitude. Its equation is

    A_s = -J^(-2) H^2 A.

Hence, for R=|A|^2,

    R_s = -2 J^(-2) H^2 R.

## 2. Critical second- and fourth-moment densities

Define the label-space densities

    q2 = J^(-1) H^2 R,

and

    q4 = J^(-3) H^4 R.

The total moments are exactly the protected L5-35 limits

    Q2(s) = integral q2(s,Z) dZ,

    Q4(s) = integral q4(s,Z) dZ.

Q2 is the limiting physical scaled second Fourier moment and Q4 is the
limiting physical scaled fourth Fourier moment.

## 3. Exact pointwise density balance

Differentiate q2. Using

    (J^(-1))_s = -alpha J^(-1),
    (H^2)_s = 2 H J (partial_Y G)(s,chi),
    R_s = -2 J^(-2) H^2 R,

gives

    partial_s q2
      = -alpha q2
        + 2 H (partial_Y G)(s,chi) R
        - 2 q4.

Thus

    q2_s
      = alpha_- q2
        - alpha_+ q2
        + P
        - 2 q4,

where

    alpha_- = (-alpha)_+,
    alpha_+ = (alpha)_+,
    P = 2 H (partial_Y G)(s,chi) R.

This is exact.

Compression is a positive production term for the critical second-moment
density. Expansion removes it. The phase-gradient term is signed. q4 is the
fourth-moment damping channel.

## 4. Integrated compression ledger

Integrating over labels gives

    Q2'(s)
      = integral alpha_- q2 dZ
        - integral alpha_+ q2 dZ
        + integral P dZ
        - 2 Q4(s).

Therefore

    integral alpha_- q2 dZ
      = Q2'(s)
        + integral alpha_+ q2 dZ
        - integral P dZ
        + 2 Q4(s).

Integrating over one critical interval [0,S] gives

    C2^-
      = Q2(S)-Q2(0)
        + C2^+
        - P_tot
        + 2 D4,

with

    C2^- = integral_0^S integral alpha_- q2 dZ ds,
    C2^+ = integral_0^S integral alpha_+ q2 dZ ds,
    P_tot = integral_0^S integral P dZ ds,
    D4 = integral_0^S Q4(s) ds.

Since F(0,Z)=0 for the accumulated L5-35 phase, H(0,Z)=0 and hence

    Q2(0)=0.

Thus on the protected normalization

    C2^- = Q2(S) + C2^+ - P_tot + 2 D4.

## 5. Absolute consequence

Because C2^-, C2^+, Q2 and D4 are nonnegative,

    C2^-
      <= Q2(S)
         + C2^+
         + |P_tot|
         + 2 D4.

Therefore packet-weighted compression of the actual L5-35 second-moment
density cannot become large without at least one balancing channel becoming
large:

1. terminal second-moment growth Q2(S);
2. expansion overlap C2^+;
3. signed phase-gradient source |P_tot|;
4. integrated fourth-moment damping D4.

This is an exact balance-channel dichotomy.

## 6. Relation to L5-43

L5-43 treated a fixed label density q and its transported pushforward.

The actual L5-35 q2 is not materially transported. It is source driven.

The exact source law above explains why identifying the abstract q_h from
L5-40/L5-41 with a passive transported density would have been incorrect.

The packet-compression object relevant to q2 is now

    integral alpha_- q2 dZ ds.

This is intrinsic in the characteristic frame and has a complete balance
ledger.

## 7. Relation to physical critical mixing

Protected L5-35 uses Q2 together with a uniform fourth-moment bound to obtain
positive physical critical-band mass.

The present identity does not itself supply that uniform moment regime.

In particular:

- large Q2 with controlled Q4 is favorable for critical-band reconstruction;
- large D4 may instead represent escape into a stronger fourth-moment
  damping channel;
- large C2^+ means expansion is dynamically competing with compression;
- large |P_tot| means the scalar phase source is dynamically essential.

Therefore large compression overlap cannot yet be identified with selector
charge alone.

## 8. What selected whole-space NSE still must supply

A whole-space closure now has a sharply finite list of obligations.

It is enough to show, on the selected active packet, that the non-charge
balance channels cannot all absorb persistent compression:

- control or sign the expansion overlap C2^+;
- control or sign the phase source P_tot;
- convert large D4 into a physical selector/dissipation charge;
- or show large terminal Q2 with suitable fourth-moment tightness reconstructs
  a threshold-violating LP block.

No generic A2/Leray theorem currently supplies those implications for the
extracted packet.

## 9. Hard rejection tests

Reject any successor that:

- treats q2 as passively transported;
- drops the signed phase source P;
- treats q4 as an error rather than an exact damping channel;
- infers selector charge from C2^- without controlling the other ledger terms;
- identifies a large fourth moment with threshold violation without an
  amplitude/reconstruction argument;
- promotes limiting L5-35 identities to selected whole-space NSE without
  deriving the packet/frame hypotheses;
- promotes tangent control to U2, U3, or U4.

## 10. Claim boundary

Protected disposition:

CRITICAL_SECOND_MOMENT_DENSITY_HAS_EXACT_COMPRESSION_PRODUCTION
__BALANCE_CHANNELS_IDENTIFIED

It proves:

- an explicit equation-derived critical density q2;
- its exact source law under the L5-35 limiting characteristic frame;
- compression enters with positive sign alpha_- q2;
- expansion, phase-gradient source, and q4 damping are the only balancing
  terms in this first-order density ledger;
- persistent compression therefore cannot disappear without appearing in one
  of those channels.

It does not prove selected whole-space NSE controls C2^-.
It does not prove one balance channel necessarily yields selector charge.
It does not prove A2.
No MATHCERT, novelty, priority, publication, patent, product, or commercial claim is asserted.

## 11. Next live obligation

C2-MIX-DIRECTION-COMPRESSION-LEDGER-CHARGE:

Determine whether selected active-band dynamics can control expansion and the
signed phase source, or convert the fourth-moment damping / terminal second
moment produced by persistent compression into a physical LP threshold and
selector/dissipation charge.

Audit D4 and the Q2/Q4 reconstruction interface first.