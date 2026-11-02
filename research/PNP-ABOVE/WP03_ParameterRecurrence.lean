import Init
namespace PNPAbove
/-- Exact numerical recurrence underlying MIPRE.Pipeline.sigmaFun,
    as seen in Foundations/Pipeline/Compress.lean at pinned upstream SHA.
    This is only its value function, NOT the upstream PolyTimeFun proof object.
    Binary length for nonnegative Nat. Matches Nat.size on positive arguments;
    every sigmaValue intermediate is strictly positive. -/
def positiveBitLength (n : Nat) : Nat := if n == 0 then 0 else Nat.log2 n + 1

def sigmaValue : Nat → Nat → Nat
  | 0, n => 2 * n + 1
  | c + 1, n => 2 ^ (2 * positiveBitLength (sigmaValue c n))

def sampledLowerBound : Bool :=
  (List.range 6).all fun c =>
    (List.range 21).all fun n =>
      c * (n+1)^c ≤ sigmaValue c n

#eval (List.range 5).map (fun c => (c, sigmaValue c 3))
#guard sampledLowerBound
#guard sigmaValue 0 3 == 7
#guard sigmaValue 1 3 == 64
#guard sigmaValue 2 3 == 16384
#guard sigmaValue 3 3 == 1073741824
end PNPAbove
