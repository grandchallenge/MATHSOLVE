import PNPAbove.WP28B2Value
import MIPRE.Foundations.Cost.BinaryArithmetic

/-!
A native uniform source-program transformation recognizing the special
2^k input index used by the EXACT original MIPRE GapCompression theorem.
-/

namespace PNPAbove.WP28C
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun

/-- Fixed source polynomial-time bit-length of any original natural index. -/
noncomputable def originalBitLength : PolyTimeFun Nat Nat :=
  unaryToBin.comp ((length (α := Bool)).comp natBits)

theorem originalBitLength_correct (n : Nat) :
    originalBitLength n = Nat.size n := by
  simp [originalBitLength, Nat.size_eq_bits_len]

/-- This fixed source program extracts k from an original natural
input of the form 2^k, using source binary decrement. -/
noncomputable def levelIndexProgram : PolyTimeFun Nat Nat :=
  predN.comp originalBitLength

theorem levelIndexProgram_correct (n : Nat) :
    levelIndexProgram n = Nat.size n - 1 := by
  simp [levelIndexProgram, originalBitLength_correct]

/-- Exactly the original source GapCompression index translation. -/
theorem levelIndexProgram_two_pow (k : Nat) :
    levelIndexProgram (2 ^ k) = k := by
  rw [levelIndexProgram_correct, Nat.size_pow]
  omega

/-- One fixed original source indexed answer checker reads an arbitrary
SAT formula at k from the special native game input index 2^k. -/
noncomputable def powerIndexedTupleChecker :
    PolyTimeFun PNPAbove.WP27.Raw Bool :=
  PNPAbove.WP28B2.indexedAnswerCheckProgram.comp
    (((levelIndexProgram.comp fst).pair PNPAbove.WP26.rawAlice).pair
      PNPAbove.WP26.rawBob)

/-- The one fixed original source code accepts all raw data through
the original all-data normalizer, without formula hardcoding. -/
noncomputable def powerIndexedRawChecker : PolyTimeFun Data Bool :=
  powerIndexedTupleChecker.comp PNPAbove.WP27.parseRaw

theorem powerIndexedRawChecker_correct (f : MIPRE.SAT.Fml)
    (x y a b : BitStr) :
    powerIndexedRawChecker
      (encode (2 ^ PNPAbove.WP28B.formulaIndex f, x, y, a, b)) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [powerIndexedRawChecker, powerIndexedTupleChecker,
    PNPAbove.WP27.parseRaw_encode, PNPAbove.WP26.rawAlice,
    PNPAbove.WP26.rawBob, levelIndexProgram_two_pow,
    PNPAbove.WP28B2.indexedAnswerCheckProgram_correct]

end PNPAbove.WP28C
