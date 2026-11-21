import PNPAbove.WP28B2NodeReader

/-! Fixed original Cost.Prog for SAT evaluation from an original binary-index. -/

namespace PNPAbove.WP28B2
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

/-- A single source code object interprets RPN instructions obtained
from the index, rather than any hardcoded formula. -/
noncomputable def indexedEvalStack :
    PolyTimeFun (Nat × BitStr) PNPAbove.WP25.EvalState :=
  PNPAbove.WP25.scanProgram.comp
    ((indexNodeProgram.comp fst).pair
      (snd.pair (PolyTimeFun.const ([] : List Bool))))

/-- The source-indexed evaluator produces precisely the original SAT
formula Boolean value on arbitrary source witness strings. -/
theorem indexedEvalStack_formula (f : MIPRE.SAT.Fml) (xs : BitStr) :
    indexedEvalStack (PNPAbove.WP28B.formulaIndex f, xs) =
      (xs, [f.eval (fun i => xs.getD i false)]) := by
  change (indexNodeProgram (PNPAbove.WP28B.formulaIndex f)).foldl
    (fun s nd => PNPAbove.WP25.nodeStepP (s, nd)) (xs, []) = _
  rw [indexNodeProgram_formula]
  simp_rw [PNPAbove.WP25.nodeStepP_correct]
  exact PNPAbove.WP25.executeRpn f xs []

/-- FIXED original source polynomial-time evaluator of arbitrary formula
indices plus arbitrary source answer strings. -/
noncomputable def indexedEvalProgram : PolyTimeFun (Nat × BitStr) Bool :=
  (ArrayProg.getD false).comp
    ((PolyTimeFun.const (0 : Nat)).pair (snd.comp indexedEvalStack))

theorem indexedEvalProgram_formula (f : MIPRE.SAT.Fml) (xs : BitStr) :
    indexedEvalProgram (PNPAbove.WP28B.formulaIndex f, xs) =
      f.eval (fun i => xs.getD i false) := by
  change (indexedEvalStack (PNPAbove.WP28B.formulaIndex f, xs)).2.getD 0 false = _
  rw [indexedEvalStack_formula]
  rfl

/-- One original source machine checks that Alice satisfies the indexed
SAT instance AND Bob agrees; its PROGRAM CODE is shared by all instances. -/
noncomputable def indexedAnswerCheckProgram :
    PolyTimeFun ((Nat × BitStr) × BitStr) Bool :=
  let sat : PolyTimeFun ((Nat × BitStr) × BitStr) Bool :=
    indexedEvalProgram.comp fst
  let agree : PolyTimeFun ((Nat × BitStr) × BitStr) Bool :=
    ArrayProg.eqBits.comp ((snd.comp fst).pair snd)
  PNPAbove.WP25.andBoolP.comp (sat.pair agree)

/-- Actual original typed native answer checker, correct for arbitrary
formula instances, with no instance-specific compiled program. -/
theorem indexedAnswerCheckProgram_correct (f : MIPRE.SAT.Fml)
    (a b : BitStr) :
    indexedAnswerCheckProgram
      ((PNPAbove.WP28B.formulaIndex f, a), b) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [indexedAnswerCheckProgram, PNPAbove.WP25.andBoolP,
    indexedEvalProgram_formula]

/-- The ORIGINAL source source-execution certificate, uniformly in the
binary input index and all possible answer strings. -/
theorem indexedAnswerCheckProgram_polytime
    (p : ((Nat × BitStr) × BitStr)) :
    ∃ t ≤ indexedAnswerCheckProgram.timeBound.eval (esize p),
      indexedAnswerCheckProgram.code.Runs
        (encode p) (encode (indexedAnswerCheckProgram p)) t :=
  indexedAnswerCheckProgram.computes p

end PNPAbove.WP28B2
