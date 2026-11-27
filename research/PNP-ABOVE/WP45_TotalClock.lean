import MIPRE.Foundations.Introspection.ClockedQueryProgram
import MIPRE.Foundations.Halting.Arith
import MIPRE.Foundations.Cost.SizeProgram
import MIPRE.Foundations.CL.DetypingClock

namespace PNPAbove.WP45
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

/-- Evaluate a fixed natural-coefficient polynomial on a unary budget,
using the original Horner program and its verified time certificate. -/
noncomputable def unaryPolynomial (p : Polynomial Nat) :
    PolyTimeFun Unary Unary := by
  classical
  let h := Prog.polyProg_runs (hornerCoeffs p)
  let q := Classical.choose h
  exact {
    toFun := fun u => unary (p.eval u.length)
    code := Prog.polyProg (hornerCoeffs p)
    closed := Prog.polyProg_wellScoped _
    timeBound := q
    computes := by
      intro u
      obtain ⟨t,ht,hr⟩ := Classical.choose_spec h u.length []
      have hu : encode u = Data.ofNat u.length := by
        rw [← encode_unary, unary_length]
      have hs : u.length ≤ esize u := length_le_esize_list u
      refine ⟨t,ht.trans (polynomial_eval_mono q hs),?_⟩
      rw [Prog.Runs,hu,encode_unary]
      simpa only [Data.polyEval_hornerCoeffs] using hr }

theorem unaryPolynomial_correct (p : Polynomial Nat) (u : Unary) :
    unaryPolynomial p u = unary (p.eval u.length) := rfl

noncomputable def outerBudget (U : ClockedUniversalMachine) :
    PolyTimeFun Data Unary :=
  (unaryPolynomial U.bound).comp (encodedSizeU Data)

theorem outerBudget_length (U : ClockedUniversalMachine) (d : Data) :
    (outerBudget U d).length = U.bound.eval d.size := by
  simp [outerBudget,unaryPolynomial_correct,esize_data]

/-- Total on ALL raw input trees. The outer source is always the fixed
well-typed universal interpreter. The inner raw source need not parse. -/
noncomputable def safeClock (U : ClockedUniversalMachine) :
    PolyTimeFun Data Data :=
  (MIPRE.Introspection.ClockedQuery.run U).comp
    ((outerBudget U).pair
      ((PolyTimeFun.const U.univT).pair (PolyTimeFun.id Data)))

theorem safeClock_spec (U : ClockedUniversalMachine) (d : Data) :
    safeClock U d = clockedResult U.univT d (U.bound.eval d.size) := by
  change clockedResult U.univT d (outerBudget U d).length = _
  rw [outerBudget_length]

theorem safeClock_runs (U : ClockedUniversalMachine) (d : Data) :
    ∃ t ≤ (safeClock U).timeBound.eval (esize d),
      (safeClock U).code.Runs (encode d) (encode (safeClock U d)) t :=
  (safeClock U).computes d

theorem safeClock_valid (U : ClockedUniversalMachine) (c : Prog) (v : Data) (k : Nat) :
    safeClock U (.cons (.ofNat k) (.cons (encode c) v)) =
      .cons (.cons .nil .nil) (clockedResult c v k) := by
  rw [safeClock_spec]
  obtain ⟨t,ht,hr⟩ := U.run c v k
  have hsize : k + esize c + v.size ≤
      (Data.cons (.ofNat k) (.cons (encode c) v)).size := by
    simp [esize]
    omega
  have hb := ht.trans (polynomial_eval_mono U.bound hsize)
  have he := (MIPRE.CL.Detyping.ClockProgram.evalWithin_eq_some_iff _ _ _ _).2
    ⟨t,hb,hr⟩
  simp [clockedResult,he]

theorem safeClock_success (U : ClockedUniversalMachine) (c : Prog) (v r : Data)
    (t k : Nat) (hr : c.Runs v r t) (ht : t ≤ k) :
    safeClock U (.cons (.ofNat k) (.cons (encode c) v)) =
      .cons (.cons .nil .nil) (.cons (.cons .nil .nil) r) := by
  rw [safeClock_valid]
  have he := (MIPRE.CL.Detyping.ClockProgram.evalWithin_eq_some_iff _ _ _ _).2
    ⟨t,ht,hr⟩
  simp [clockedResult,he]

end PNPAbove.WP45
