import PNPAbove.WP26UniformCompiler
import MIPRE.Foundations.CL.DetypingProgParse

/-!
Original, total, polynomial-time normalization from ANY raw Data to a
canonical native verifier five-tuple; malformed inputs always terminate.
This supports closing the all-raw-data IsBounded obligation without
assuming the native evaluator itself is total on arbitrary malformed data.
-/
namespace PNPAbove.WP27
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun
open MIPRE.CL.Detyping.Program

abbrev Raw := Nat × BitStr × BitStr × BitStr × BitStr

/-- Structural original-source tuple parsing, valid for arbitrary Data. -/
noncomputable def parseRaw : PolyTimeFun Data Raw :=
  (readNat.comp treeHead).pair
    ((readBits.comp (treeHead.comp treeTail)).pair
     ((readBits.comp (treeHead.comp (treeTail.comp treeTail))).pair
      ((readBits.comp (treeHead.comp (treeTail.comp (treeTail.comp treeTail)))).pair
       (readBits.comp (treeTail.comp (treeTail.comp (treeTail.comp treeTail)))))))

/-- Native normal-form verifier tuples survive the original total parser
without changing ANY source field. -/
theorem parseRaw_encode (n : Nat) (x y a b : BitStr) :
    parseRaw (encode (n,x,y,a,b)) = (n,x,y,a,b) := by
  simp [parseRaw, encode_prod, readNat_encode, readBits_encode]

/-- Fixed source code evaluating a formula and the fully parsed raw tuple.
Its input type Fml × Data admits all raw malformed Data on its right. -/
noncomputable def rawCore : PolyTimeFun (MIPRE.SAT.Fml × Data) Bool :=
  PNPAbove.WP26.sourceCoreChecker.comp
    ((fst : PolyTimeFun (MIPRE.SAT.Fml × Data) MIPRE.SAT.Fml).pair
     (parseRaw.comp snd))

theorem rawCore_correct (f : MIPRE.SAT.Fml) (n : Nat) (x y a b : BitStr) :
    rawCore (f, encode (n,x,y,a,b)) =
      (f.eval (fun i => a.getD i false) && decide (a = b)) := by
  simp [rawCore, parseRaw_encode, PNPAbove.WP26.sourceCoreChecker_correct]

/-- The source generator is polynomial in f and emits a CLOSED original
Cost.Prog which is robust under all arbitrary raw Data. -/
noncomputable def robustSourceGenerator : PolyTimeFun MIPRE.SAT.Fml Prog :=
  (PolyTimeFun.smn MIPRE.SAT.Fml).comp
    ((PolyTimeFun.const rawCore.code).pair
      (PolyTimeFun.id MIPRE.SAT.Fml))

theorem robustSourceGenerator_correct (f : MIPRE.SAT.Fml) :
    robustSourceGenerator f =
      Cost.hardcode rawCore.code (encode f) := rfl

theorem robustSourceGenerator_polytime (f : MIPRE.SAT.Fml) :
    ∃ t ≤ robustSourceGenerator.timeBound.eval (esize f),
      robustSourceGenerator.code.Runs
        (encode f) (encode (robustSourceGenerator f)) t :=
  robustSourceGenerator.computes f

/-- Original native formula witness acceptance in the *generated*
programme, with malformed data normalized before evaluation. -/
theorem robustSourceGenerator_accepts_iff (f : MIPRE.SAT.Fml)
    (n : Nat) (x y a b : BitStr) :
    (∃ t, (robustSourceGenerator f).Runs
       (encode (n,x,y,a,b)) (encode true) t) ↔
      (f.eval (fun i => a.getD i false) = true ∧ a = b) := by
  rw [robustSourceGenerator_correct]
  constructor
  · rintro ⟨t, hrun⟩
    obtain ⟨t₁, _, hcore⟩ := Cost.hardcode_time_rev rawCore.closed hrun
    obtain ⟨t₀, _, hcanonical⟩ :=
      rawCore.computes (f, encode (n,x,y,a,b))
    have heq : encode true = encode (rawCore (f, encode (n,x,y,a,b))) :=
      (Cost.Eval.deterministic hcore hcanonical).1
    have hresult : rawCore (f, encode (n,x,y,a,b)) = true := by
      cases h : rawCore (f, encode (n,x,y,a,b)) with
      | false => simp [h] at heq
      | true => rfl
    rw [rawCore_correct] at hresult
    simpa only [Bool.and_eq_true, decide_eq_true_eq] using hresult
  · intro hacc
    obtain ⟨t, _, hcore⟩ :=
      rawCore.computes (f, encode (n,x,y,a,b))
    have hresult : rawCore (f, encode (n,x,y,a,b)) = true := by
      rcases hacc with ⟨hf, rfl⟩
      simp only [rawCore_correct, Bool.and_eq_true, decide_eq_true_eq]
      refine ⟨?_, trivial⟩
      simpa [List.getD] using hf
    have hrun : rawCore.code.Runs (encode (f, encode (n,x,y,a,b)))
        (encode true) t := by
      simpa only [hresult] using hcore
    exact ⟨t + (encode f).size + (encode (n,x,y,a,b)).size + 3,
      Cost.hardcode_time rawCore.closed hrun⟩

end PNPAbove.WP27
