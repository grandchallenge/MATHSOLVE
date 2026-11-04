import MIPRE.Foundations.CL.Sampler

/-!
PNP-ABOVE WP10: a source-native nine-level conditionally linear identity
presentation for both players. Pinned upstream MIPRE-formalization commit:
5926bdff5db621f44682a101007ef2fe3ae8d970.

This establishes the geometric CL presentation component. It is not yet
the complete MIPRE.CL.Sampler 9, which additionally requires an executable
query program and four families of Runs witnesses plus uniform halting.
-/

namespace PNPAbove.WP10
open MIPRE
open MIPRE.CL

/-- A stage that copies exactly one coordinate, independently of previous values. -/
def coordinateStage (i : Fin 9) {k : Nat}
    (tail : CLFun 𝔽₂ (Fin 9) k) : CLFun 𝔽₂ (Fin 9) (k + 1) :=
  .cons {i} (RegLinear.id {i}) (fun _ => tail)

/-- Nine successive coordinate projections: stage j extracts coordinate j-1. -/
def identityNine : CLFun 𝔽₂ (Fin 9) 9 :=
  coordinateStage 0 <|
  coordinateStage 1 <|
  coordinateStage 2 <|
  coordinateStage 3 <|
  coordinateStage 4 <|
  coordinateStage 5 <|
  coordinateStage 6 <|
  coordinateStage 7 <|
  coordinateStage 8 <|
  .zero

/-- Each of the nine register factors occurs exactly once: exact support. -/
theorem identityNine_exactlyOn :
    identityNine.ExactlyOn (Finset.univ : Finset (Fin 9)) := by
  simp [identityNine, coordinateStage, CLFun.ExactlyOn]

/-- The complete nine-stage map is the identity on the full vector space. -/
theorem identityNine_eval (x : Fin 9 → 𝔽₂) : identityNine.eval x = x := by
  funext i
  fin_cases i <;>
    simp [identityNine, coordinateStage, CLFun.eval, RegLinear.id_apply,
      proj_apply]

/-- The identity game uses this same native presentation for both provers. -/
def playerPresentation (_w : Player) : CLFun 𝔽₂ (Fin 9) 9 := identityNine

theorem playerPresentation_exactlyOn (w : Player) :
    (playerPresentation w).ExactlyOn (Finset.univ : Finset (Fin 9)) :=
  identityNine_exactlyOn

theorem playerPresentation_eval (w : Player) (x : Fin 9 → 𝔽₂) :
    (playerPresentation w).eval x = x :=
  identityNine_eval x

/-- Check all 512 diagonal pairs against the native presentation. -/
def allDiagonalIdentity : Bool :=
  (List.range 512).all fun n =>
    let bits : BitStr := (List.range 9).map (Nat.testBit n)
    decide (toBits (identityNine.eval (ofBits 9 bits)) = bits)

#guard allDiagonalIdentity

end PNPAbove.WP10
