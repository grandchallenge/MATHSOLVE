import PNPAbove.WP21Total

/-!
Finite source-native executable regression matrix; quantified correctness
remains a separate theorem obligation. All checks use the imported source evaluator; no proof shortcuts.
-/
namespace PNPAbove.WP21
open MIPRE MIPRE.Cost
open PNPAbove.WP20

/-- Source images of the uniform nine-bit seed, with genuine masked edge bits. -/
def leftBits (z : BitStr) : BitStr := z.take 8 ++ [false]
def rightBits (z : BitStr) : BitStr := false :: z.drop 1

def sourceExpected (z : BitStr) (a b : Bool) : Bool :=
  decide (a.xor b = (z[0]! && z[8]!))

def nativeDecision (n : Nat) (x y a b : BitStr) : Data :=
  WP12.evalValue maskedParityDeciderProg [WP08.sample n x y a b]

def allSourceChecks : Bool :=
  (List.range 512).all fun k =>
    let z := WP08.vectorNine k
    ([false, true] : List Bool).all fun a =>
      ([false, true] : List Bool).all fun b =>
        nativeDecision 2 (leftBits z) (rightBits z) [a] [b] ==
          encode (sourceExpected z a b)

#guard allSourceChecks

/- Every sampled answer has exactly one canonical bit; malformed/extra answer
strings cannot accidentally inherit a positive source decision. -/
#guard nativeDecision 2 (WP08.zeroNine) (WP08.zeroNine) [] [false] == encode false
#guard nativeDecision 2 (WP08.zeroNine) (WP08.zeroNine) [false] [] == encode false
#guard nativeDecision 2 (WP08.zeroNine) (WP08.zeroNine) [false,false] [false] == encode false
#guard nativeDecision 2 (WP08.zeroNine) (WP08.zeroNine) [false] [false,false] == encode false
#guard nativeDecision 0 (WP08.zeroNine) (WP08.zeroNine) [false] [false] == encode false
#guard nativeDecision 2 (WP08.eightBits) (WP08.zeroNine) [false] [false] == encode false
#guard nativeDecision 2 (WP08.zeroNine) (WP08.tenBits) [false] [false] == encode false
#guard nativeDecision 2 (List.replicate 9 true) (List.replicate 9 true) [false] [true] == encode false
#guard nativeDecision 2 (WP08.zeroNine) (WP08.zeroNine) [false] [true] == encode false

end PNPAbove.WP21
