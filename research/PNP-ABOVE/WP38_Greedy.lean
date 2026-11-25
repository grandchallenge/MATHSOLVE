import MIPRE.Foundations.SAT.FmlProg
import MIPRE.Foundations.Cost.BinaryCompare

namespace PNPAbove.WP38
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

abbrev Sat (f : Fml) : Prop := ∃ a : Nat → Bool, f.eval a = true
def Correct (D : PolyTimeFun Data Bool) : Prop :=
  ∀ f : Fml, D (encode f) = true ↔ Sat f

noncomputable def rawFml : PolyTimeFun Fml Data :=
  PolyTimeFun.ofEncodeEq (encode : Fml → Data) (fun _ => rfl)


def lit (i : Nat) (b : Bool) : Fml :=
  if b then .inp i else .not (.inp i)

theorem lit_eval (i : Nat) (b : Bool) (a : Nat → Bool) :
    (lit i b).eval a = true ↔ a i = b := by
  cases b <;> simp [lit,Fml.eval]

theorem pin_eval (f : Fml) (i : Nat) (b : Bool) (a : Nat → Bool) :
    (Fml.and f (lit i b)).eval a = true ↔ f.eval a = true ∧ a i = b := by
  simp only [Fml.eval,Bool.and_eq_true,lit_eval]

abbrev State := Fml × BitStr
abbrev Input := State × Nat

def choose (D : PolyTimeFun Data Bool) (f : Fml) (i : Nat) : Bool :=
  D (encode (Fml.and f (.inp i)))

def step (D : PolyTimeFun Data Bool) (s : State) (i : Nat) : State :=
  let b := choose D s.1 i
  (.and s.1 (lit i b),b::s.2)

theorem step_sat (D : PolyTimeFun Data Bool) (hD : Correct D)
    (s : State) (i : Nat) (hs : Sat s.1) :
    Sat (step D s i).1 := by
  change Sat (.and s.1 (lit i (choose D s.1 i)))
  cases hb : choose D s.1 i with
  | true =>
    rw [lit]
    exact (hD _).mp hb
  | false =>
    obtain ⟨a,ha⟩ := hs
    have hfalse : a i = false := by
      cases hi : a i with
      | false => rfl
      | true =>
        have h : D (encode (Fml.and s.1 (.inp i))) = true :=
          (hD _).mpr ⟨a,by simp [Fml.eval,ha,hi]⟩
        exact Bool.noConfusion (hb.symm.trans h)
    exact ⟨a,(pin_eval _ _ _ _).mpr ⟨ha,hfalse⟩⟩

noncomputable def formulaP : PolyTimeFun Input Fml := fst.comp fst
noncomputable def bitsP : PolyTimeFun Input BitStr := snd.comp fst
noncomputable def posP : PolyTimeFun Input Fml := Fml.inpF.comp snd
noncomputable def testP (D : PolyTimeFun Data Bool) : PolyTimeFun Input Bool :=
  D.comp (rawFml.comp (Fml.andF.comp (formulaP.pair posP)))

noncomputable def litP (D : PolyTimeFun Data Bool) : PolyTimeFun Input Fml :=
  PolyTimeFun.ite (testP D) posP (Fml.notF.comp posP)

noncomputable def stepP (D : PolyTimeFun Data Bool) : PolyTimeFun Input State :=
  (Fml.andF.comp (formulaP.pair (litP D))).pair ((testP D).cons bitsP)

theorem testP_correct (D : PolyTimeFun Data Bool) (s : State) (i : Nat) :
    testP D (s,i) = choose D s.1 i := rfl

theorem stepP_correct (D : PolyTimeFun Data Bool) (s : State) (i : Nat) :
    stepP D (s,i) = step D s i := by
  change (Fml.and s.1 (if testP D (s,i) then .inp i else .not (.inp i)),
    testP D (s,i)::s.2) = _
  rw [testP_correct]
  rfl

theorem inp_size (i : Nat) : esize (Fml.inp i) = esize i + 4 := by
  change (1+esize i+1)+1+1 = _
  omega

theorem lit_size (i : Nat) (b : Bool) : esize (lit i b) ≤ esize i + 16 := by
  cases b <;> simp [lit,inp_size,esize_not_fml]

theorem stepP_growth (D : PolyTimeFun Data Bool) (s : State) (i : Nat) :
    esize (stepP D (s,i)) ≤ esize s + (X + C 27 : Polynomial Nat).eval (esize i) := by
  rw [stepP_correct]
  rcases s with ⟨f,bs⟩
  change esize (Fml.and f (lit i (choose D f i)),choose D f i::bs) ≤ _
  simp only [esize_prod,esize_and_fml,esize_list_cons,Polynomial.eval_add,Polynomial.eval_X,Polynomial.eval_C]
  have h1 := lit_size i (choose D f i)
  have h2 := esize_bool_le (choose D f i)
  omega

noncomputable def runP (D : PolyTimeFun Data Bool) : PolyTimeFun (List Nat × Fml) State :=
  (foldlAdd (stepP D) (X+C 27) (stepP_growth D)).comp
    (fst.pair (snd.pair (PolyTimeFun.const ([] : BitStr))))

def run (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) : State :=
  xs.foldl (step D) (f,[])

theorem runP_correct (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) :
    runP D (xs,f) = run D xs f := by
  change foldlAdd (stepP D) (X+C 27) (stepP_growth D) (xs,(f,[])) = _
  simp only [foldlAdd_apply,stepP_correct,run]

noncomputable def searchP (D : PolyTimeFun Data Bool) : PolyTimeFun (List Nat × Fml) BitStr :=
  PolyTimeFun.reverse.comp (snd.comp (runP D))

theorem searchP_correct (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) :
    searchP D (xs,f) = (run D xs f).2.reverse := by
  simp [searchP,runP_correct]

/-- Every model of the final conjunction satisfies the initial formula and
the recorded decisions, regardless of whether the oracle was correct. -/
theorem fold_models (D : PolyTimeFun Data Bool) (xs : List Nat) (s : State)
    (a : Nat → Bool) (h : (xs.foldl (step D) s).1.eval a = true) :
    s.1.eval a = true ∧ (xs.foldl (step D) s).2 = (xs.map a).reverse ++ s.2 := by
  induction xs generalizing s with
  | nil => exact ⟨h,by simp⟩
  | cons i xs ih =>
    have hh := ih (step D s i) h
    have hp := (pin_eval s.1 i (choose D s.1 i) a).mp hh.1
    refine ⟨hp.1,?_⟩
    change (xs.foldl (step D) (step D s i)).2 = _
    rw [hh.2]
    change (xs.map a).reverse ++ choose D s.1 i :: s.2 = _
    simp [hp.2,List.reverse_cons,List.append_assoc]

theorem fold_sat (D : PolyTimeFun Data Bool) (hD : Correct D)
    (xs : List Nat) (s : State) (hs : Sat s.1) :
    Sat (xs.foldl (step D) s).1 := by
  induction xs generalizing s with
  | nil => exact hs
  | cons i xs ih => exact ih (step D s i) (step_sat D hD s i hs)

theorem fold_length (D : PolyTimeFun Data Bool) (xs : List Nat) (s : State) :
    (xs.foldl (step D) s).2.length = xs.length + s.2.length := by
  induction xs generalizing s with
  | nil => simp
  | cons i xs ih =>
    rw [List.foldl_cons,ih]
    simp [step]
    omega

theorem search_length (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) :
    (searchP D (xs,f)).length = xs.length := by
  rw [searchP_correct,List.length_reverse,run,fold_length]
  simp

theorem search_model (D : PolyTimeFun Data Bool) (hD : Correct D)
    (xs : List Nat) (f : Fml) (hf : Sat f) :
    ∃ a : Nat → Bool, f.eval a = true ∧ searchP D (xs,f) = xs.map a := by
  obtain ⟨a,ha⟩ := fold_sat D hD xs (f,[]) hf
  have h := fold_models D xs (f,[]) a ha
  refine ⟨a,h.1,?_⟩
  rw [searchP_correct,run,h.2,List.append_nil,List.reverse_reverse]

theorem searchP_runs (D : PolyTimeFun Data Bool) (xs : List Nat) (f : Fml) :
    ∃ t ≤ (searchP D).timeBound.eval (esize (xs,f)),
      (searchP D).code.Runs (encode (xs,f)) (encode (searchP D (xs,f))) t :=
  (searchP D).computes (xs,f)

end PNPAbove.WP38
