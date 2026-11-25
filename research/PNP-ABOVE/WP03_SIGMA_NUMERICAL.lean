/-
PNP-ABOVE-WP03: standalone, numerical analogue of the upstream sigmaFun
recurrence (NOT the MIPRE PolyTimeFun program or proof object).

Upstream source: vidick/MIPRE-formalization,
commit 5926bdff5db621f44682a101007ef2fe3ae8d970,
MIPRE/Foundations/Pipeline/Compress.lean, sigmaFun_zero/sigmaFun_succ.

This deliberately imports Init only. The original Nat.size definition lives
in the upstream import environment; positive natural-number bit size is
implemented here recursively. Build status is separately recorded; the
presence of this file is NOT evidence that the full upstream Lean project
was built or that DecisionCompiler.compute ran.
-/
import Init

namespace PNPAbove

/-- Positive-number binary length, with zero assigned size zero. -/
partial def bitSize (n : Nat) : Nat :=
  if n == 0 then 0 else 1 + bitSize (n / 2)

/-- Source numerical recurrence: sigma(0,n)=2n+1,
    sigma(c+1,n)=2^(2 * bitSize(sigma(c,n))). -/
def sigmaValue : Nat → Nat → Nat
  | 0, n => 2 * n + 1
  | c + 1, n => 2 ^ (2 * bitSize (sigmaValue c n))

/-- Elementary closed form for positive c; if c=0 use base. -/
def sigmaClosed (c n : Nat) : Nat :=
  if c == 0 then 2 * n + 1
  else 2 ^ ((2 ^ c) * (bitSize (2*n+1) + 1) - 2)

/-- Finite smoke test of recurrence/closed-form equality. -/
def sampledAgreement : Bool :=
  (List.range 8).all fun c =>
    (List.range 40).all fun n =>
      decide (sigmaValue c n = sigmaClosed c n)

/-- Finite smoke test of the source's universal lower-bound theorem. -/
def sampledLowerBound : Bool :=
  (List.range 6).all fun c =>
    (List.range 21).all fun n =>
      decide (c * (n+1)^c ≤ sigmaValue c n)

#eval (List.range 6).map (fun c => sigmaValue c 3)
#eval sampledAgreement
#eval sampledLowerBound
end PNPAbove
