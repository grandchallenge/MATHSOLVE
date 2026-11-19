import PNPAbove.WP20Native

/-!
PNP-ABOVE WP21: a support-masked CHSH predicate.
The two support masks enforce global synchrony without comparing
arbitrary nine-bit questions. This is a mathematical source lemma,
not yet a proof about an executable Cost.Prog.
-/
namespace PNPAbove.WP21
open MIPRE MIPRE.CL MIPRE.Cost
open PNPAbove.WP20

def maskedParityAccept (x y : Questions) (a b : Bool) : Bool :=
  (!bit (x 8) && !bit (y 0)) &&
    decide (a.xor b = (bit (x 0) && bit (y 8)))

theorem maskedParity_synchronous (x : Questions) (a b : Bool)
    (hne : a ≠ b) :
    maskedParityAccept x x a b = false := by
  cases h0 : bit (x 0) <;> cases h8 : bit (x 8) <;>
    cases a <;> cases b <;>
    simp_all [maskedParityAccept, Bool.xor]

theorem maskedParity_source (z : Questions) (a b : Bool) :
    maskedParityAccept (aliceCL.eval z) (bobCL.eval z) a b =
      parityAccept (aliceCL.eval z) (bobCL.eval z) a b := by
  rw [parityAccept_source]
  simp [maskedParityAccept, alice_eval, bob_eval, bit]
  rfl

end PNPAbove.WP21
