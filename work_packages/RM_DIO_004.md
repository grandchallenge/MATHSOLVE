# RM-DIO-004 bounded Diophantine route

## Metadata

- Domain: Diophantine equations
- Work Package: `WP-RM-DIO-004`
- Source: MATHFORGE `RM-AMPHORA-001` at protected commit `bab7ae57f54601b49ad9fc870051095ad487c64a`
- Claim status: exactly computed on a bounded interval; global completeness withheld
- Certification target: MATHCERT Level 2

## Problem and source posture

Determine the integer solutions of `x^2 - x = y^5 - y`. The source corpus is an intake source, not a theorem oracle. Its status-search prose is not imported as mathematical evidence.

## Exact reduction

For fixed integer `y`, the quadratic in `x` has an integral solution precisely when `D = 1 + 4(y^5-y)` is a nonnegative odd square. If `D = z^2`, both possible roots are recovered exactly as `x = (1 +/- z)/2`. This equivalence lets the bounded screen enumerate `y` while leaving `x` unrestricted.

## Bounded result

The exact screen exhausts every integer `y` from `-1,000,000` through `1,000,000`. It finds twelve ordered pairs, including the nontrivial branches at `y = 2`, `3`, and `30`. The committed validator recomputes the full interval and rejects any changed bound, source identity, solution, or promoted global claim.

## Certification boundary

The MATHCERT request is only for the finite-domain statement. The unrestricted problem is not certified, not claimed solved, and remains dependent on a global arithmetic argument that supplies a valid height bound or otherwise proves completeness.

## Replay

`python ci/validate_rm_dio_004.py` and `python ci/test_validate_rm_dio_004.py`
