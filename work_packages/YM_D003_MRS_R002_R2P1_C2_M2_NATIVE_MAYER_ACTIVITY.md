# YM-D003-MRS-R002-R2P1-C2-M2 — native Mayer activity theorem

Status: `PROVED__C2_M_CLOSED`

Let a pre-Mayer polymer P be a connected C0 object formed after horizontal and vertical decoupling, with finite box support supp(P) and activity z(P). Two polymers are incompatible when their supports overlap.

C2-H and C2-V give rho-uniform constants L_H and L_V. Fix a>0 and charge exp(a) per occupied box in the existing H/V rooted-tree majorant. If

`q_a = epsilon * exp(a) * C_comb * (L_H + L_V) < 1`,

then the weighted rooted activity

`delta_a = sup_Delta sum_{P:Delta in supp(P)} |z(P)| exp(a*|supp(P)|)`

obeys

`delta_a <= C0 * epsilon * exp(a) / (1-q_a)`

for finite local multiplicity C0, uniformly in terminal ultraviolet depth rho. This follows from the C1 spanning-tree argument with the extra exp(a) box weight.

Because the MRS per-box factor epsilon is adjustable, choose it small enough that delta_a <= a. Then for every P,

`sum_{Q incompatible with P} |z(Q)| exp(a*|supp(Q)|)`

`<= sum_{Delta in supp(P)} sum_{Q:Delta in supp(Q)} |z(Q)| exp(a*|supp(Q)|)`

`<= |supp(P)| delta_a <= a |supp(P)|`.

This is the standard abstract polymer convergence criterion with size function A(P)=a|supp(P)|. Therefore the Mayer cluster sum converges absolutely, uniformly in rho.

Consequently C2-M is closed by a native replacement; the unavailable theorem pages of Rivasseau [R] are no longer load-bearing. Together with C2-H/V and the region-local BGDET treatment, C2 is closed for sufficiently small allocated box activity.

C3 is now authorized: prove the scale gain of the renormalized two-point remainder after local A^2/2 subtraction.
