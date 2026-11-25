# YM-D003-MRS-R002-R2P1-C3-A — source-concordant quadratic local projector

Status: `PROVED__SOURCE_CONCORDANCE_CLOSED`

Parent: `YM-D003-MRS-R002-R2P1-C3`

## Source basis

For pure SU(2), MRS lists the local operators that require independent cutoff-restoring counterterms. The quadratic part of that list is exactly:

- `A^2`;
- `A(-Delta)A`;
- `(dA)^2`.

MRS then introduces the corresponding quadratic counterterms in Eq. (III.1), with `b_rho` multiplying `A^2/2`, and states separately that this relevant mass coefficient must be tuned exactly while the marginal counterterms can be treated perturbatively for the stated construction.

## Projector

After the C2 Mayer step has removed hard-core constraints, the divergent two-point contribution is translation invariant and can be expanded at zero external momentum.

Define `P_2,loc` as the unique projection of the Taylor jet through superficial degree two onto the three source-admitted quadratic local structures above.

Define `P_mass` as the `A^2/2` component of `P_2,loc`.

No additional quadratic local operator is introduced.

## Concordance statement

The original C3 wording identified `P_mass` with the whole two-point localization. That identification is false as a statement about the full two-point remainder, because the two marginal quadratic structures remain after mass subtraction.

The corrected identities are:

`P_mass K = mass channel used by MT1`,

`P_2,loc K = complete relevant+marginal local two-point jet`,

`R_2 K = (1-P_2,loc)K = genuinely irrelevant remainder candidate`.

This separation is exactly compatible with the MRS statement that two-point divergences are cancelled by counterterms of the desired local form after the Mayer step.

## Subtraction-forest compatibility

For a nested proper two-point subgraph, `SUBTRACT(gamma)` in C0 records its complete local divergent part. Replacing the former symbolic `A^2/2`-only local slot by `P_2,loc` does not change the finite grammar: it refines that slot into the complete source-admitted quadratic basis. The mass component remains tagged separately for the running exact mass recursion.

## Disposition

`C3_A_CLOSED__FULL_QUADRATIC_LOCAL_PROJECTOR_SOURCE_CONCORDANT__MASS_COMPONENT_SEPARATED`
