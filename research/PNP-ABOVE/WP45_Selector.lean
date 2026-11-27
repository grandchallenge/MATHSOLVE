import PNPAbove.WP45TotalClock
import PNPAbove.WP45Enumeration
import MIPRE.Foundations.CL.DetypingProgParse

namespace PNPAbove.WP45
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial
open MIPRE.CL.Detyping.Program

variable {α : Type} [SizedEncoding α]

/-- Form the inner interpreter's raw input, without treating a malformed
program description as a typed program. -/
noncomputable def innerInputP : PolyTimeFun (Data × (Unary × α)) Data :=
  encoded.comp ((fst.comp snd).pair (fst.pair (snd.comp snd)))

theorem innerInputP_correct (d : Data) (u : Unary) (a : α) :
    innerInputP (d,u,a) = .cons (.ofNat u.length) (.cons d (encode a)) := by
  change encode (u,d,a) = _
  rw [encode_prod,encode_prod,encode_data,← encode_unary,unary_length]

/-- Every malformed or timed-out attempt still yields a bounded, total
bit-string output. Only the subsequent witness checker can accept it. -/
noncomputable def rawAttempt (U : ClockedUniversalMachine) :
    PolyTimeFun (Data × (Unary × α)) BitStr :=
  readBits.comp (treeTail.comp (treeTail.comp ((safeClock U).comp innerInputP)))

theorem rawAttempt_success (U : ClockedUniversalMachine) (c : Prog)
    (u : Unary) (a : α) (w : BitStr) (t : Nat)
    (hr : c.Runs (encode a) (encode w) t) (ht : t ≤ u.length) :
    rawAttempt U (encode c,u,a) = w := by
  change readBits (treeTail (treeTail (safeClock U (innerInputP (encode c,u,a))))) = _
  rw [innerInputP_correct,safeClock_success U c _ _ t _ hr ht,
    treeTail_cons,treeTail_cons,readBits_encode]

noncomputable def attemptsP (U : ClockedUniversalMachine) :
    PolyTimeFun (Unary × α) (List BitStr) :=
  (mapWith (rawAttempt U)).comp ((codeListP.comp fst).pair (PolyTimeFun.id _))

theorem attempts_contains (U : ClockedUniversalMachine) (c : Prog)
    (u : Unary) (a : α) (w : BitStr) (t : Nat)
    (hr : c.Runs (encode a) (encode w) t)
    (hc : 2^(esize c) ≤ u.length) (ht : t ≤ u.length) :
    w ∈ attemptsP U (u,a) := by
  change w ∈ (codeListP u).map (fun d => rawAttempt U (d,u,a))
  exact List.mem_map.mpr ⟨encode c,codeList_contains u c hc,
    rawAttempt_success U c u a w t hr ht⟩

/-- Verify each output once. Preserve the accepted candidate, not the
description or any unverified result of the interpreter. -/
noncomputable def checkAttempt (V : PolyTimeFun (α × BitStr) Bool) :
    PolyTimeFun (BitStr × α) (Bool × BitStr) :=
  (V.comp (snd.pair fst)).pair fst

def selectStep (s : BitStr) (a : Bool × BitStr) : BitStr :=
  if a.1 then a.2 else s

noncomputable def selectStepP : PolyTimeFun (BitStr × (Bool × BitStr)) BitStr :=
  PolyTimeFun.ite (fst.comp snd) (snd.comp snd) fst

theorem selectStepP_correct (s : BitStr) (a : Bool × BitStr) :
    selectStepP (s,a) = selectStep s a := rfl

theorem selectStep_growth (s : BitStr) (a : Bool × BitStr) :
    esize (selectStepP (s,a)) ≤ esize s + (X : Polynomial Nat).eval (esize a) := by
  rw [selectStepP_correct]
  rcases a with ⟨b,w⟩
  cases b <;> simp [selectStep,esize_prod] <;> omega

noncomputable def selectP : PolyTimeFun (List (Bool × BitStr)) BitStr :=
  (foldlAdd selectStepP X selectStep_growth).comp
    ((PolyTimeFun.id _).pair (PolyTimeFun.const ([] : BitStr)))

theorem selectP_correct (xs : List (Bool × BitStr)) :
    selectP xs = xs.foldl selectStep [] := by
  change foldlAdd selectStepP X selectStep_growth (xs,[]) = _
  simp only [foldlAdd_apply,selectStepP_correct]

theorem select_preserve (P : BitStr → Prop) (xs : List (Bool × BitStr))
    (h : ∀ w, (true,w) ∈ xs → P w) (s : BitStr) (hs : P s) :
    P (xs.foldl selectStep s) := by
  induction xs generalizing s with
  | nil => exact hs
  | cons a xs ih =>
    rw [List.foldl_cons]
    apply ih (fun w hw => h w (by simp [hw]))
    rcases a with ⟨b,w⟩
    cases b
    · exact hs
    · exact h w (by simp)

theorem select_find (P : BitStr → Prop) (xs : List (Bool × BitStr))
    (h : ∀ w, (true,w) ∈ xs → P w)
    (he : ∃ w, (true,w) ∈ xs) (s : BitStr) :
    P (xs.foldl selectStep s) := by
  induction xs generalizing s with
  | nil => simp at he
  | cons a xs ih =>
    rw [List.foldl_cons]
    rcases a with ⟨b,w⟩
    cases b
    · apply ih (fun w hw => h w (by simp [hw]))
      simpa using he
    · apply select_preserve P xs (fun w hw => h w (by simp [hw]))
      exact h w (by simp)

noncomputable def budgetSelector (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) :
    PolyTimeFun (Unary × α) BitStr :=
  selectP.comp ((mapWith (checkAttempt V)).comp ((attemptsP U).pair snd))

theorem budgetSelector_complete (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool)
    (u : Unary) (a : α) (c : Prog) (w : BitStr) (t : Nat)
    (hc : 2^(esize c) ≤ u.length) (ht : t ≤ u.length)
    (hr : c.Runs (encode a) (encode w) t) (hv : V (a,w) = true) :
    V (a,budgetSelector U V (u,a)) = true := by
  let xs := (attemptsP U (u,a)).map (fun b => (V (a,b),b))
  change V (a,selectP xs) = true
  rw [selectP_correct]
  apply select_find (fun b => V (a,b) = true)
  · intro b hb
    obtain ⟨v,_,he⟩ := List.mem_map.mp hb
    have h1 := congrArg Prod.fst he
    have h2 := congrArg Prod.snd he
    simpa [h2] using h1
  · refine ⟨w,List.mem_map.mpr ⟨w,attempts_contains U c u a w t hr hc ht,?_⟩⟩
    simp [hv]

/-- One fixed polynomial program suffices on every input having a short
description of a successful run within the supplied unary budget. -/
theorem budgetSelector_runs (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) (u : Unary) (a : α) :
    ∃ t ≤ (budgetSelector U V).timeBound.eval (esize (u,a)),
      (budgetSelector U V).code.Runs (encode (u,a))
        (encode (budgetSelector U V (u,a))) t :=
  (budgetSelector U V).computes (u,a)

noncomputable def polynomialSelector (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) (p : Polynomial Nat) :
    PolyTimeFun α BitStr :=
  (budgetSelector U V).comp
    (((unaryPolynomial p).comp (encodedSizeU α)).pair (PolyTimeFun.id α))

theorem polynomialSelector_complete (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) (p : Polynomial Nat)
    (a : α) (c : Prog) (w : BitStr) (t : Nat)
    (hc : 2^(esize c) ≤ p.eval (esize a))
    (ht : t ≤ p.eval (esize a))
    (hr : c.Runs (encode a) (encode w) t) (hv : V (a,w) = true) :
    V (a,polynomialSelector U V p a) = true := by
  change V (a,budgetSelector U V (unaryPolynomial p (encodedSizeU α a),a)) = true
  apply budgetSelector_complete U V _ _ c w t _ _ hr hv
  · simpa [unaryPolynomial_correct] using hc
  · simpa [unaryPolynomial_correct] using ht

def HasWitness (V : PolyTimeFun (α × BitStr) Bool) (a : α) : Prop :=
  ∃ w, V (a,w) = true

def WeightedBound (V : PolyTimeFun (α × BitStr) Bool) (p : Polynomial Nat) : Prop :=
  ∀ a, HasWitness V a →
    ∃ c : Prog, ∃ w : BitStr, ∃ t : Nat,
      c.WellScoped 1 ∧ c.Runs (encode a) (encode w) t ∧
      V (a,w) = true ∧ 2^(esize c)*(t+1) ≤ p.eval (esize a)

def Solves (V : PolyTimeFun (α × BitStr) Bool) (S : PolyTimeFun α BitStr) : Prop :=
  ∀ a, HasWitness V a → V (a,S a) = true

theorem weightedBound_solves (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) (p : Polynomial Nat)
    (h : WeightedBound V p) : Solves V (polynomialSelector U V p) := by
  intro a ha
  obtain ⟨c,w,t,_,hr,hv,hb⟩ := h a ha
  have hp : 0 < 2^(esize c) := by positivity
  have hc := (Nat.le_mul_of_pos_right (2^(esize c)) (by omega : 0 < t+1)).trans hb
  have ht := (Nat.le_mul_of_pos_left (t+1) hp).trans hb
  exact polynomialSelector_complete U V p a c w t hc (by omega) hr hv

theorem solver_weightedBound (V : PolyTimeFun (α × BitStr) Bool)
    (S : PolyTimeFun α BitStr) (h : Solves V S) :
    WeightedBound V (C (2^(esize S.code)) * (S.timeBound+1)) := by
  intro a ha
  obtain ⟨t,ht,hr⟩ := S.computes a
  refine ⟨S.code,S a,t,S.closed,hr,h a ha,?_⟩
  simpa using Nat.mul_le_mul_left (2^(esize S.code)) (Nat.add_le_add_right ht 1)

theorem weightedBound_iff_solver (U : ClockedUniversalMachine)
    (V : PolyTimeFun (α × BitStr) Bool) :
    (∃ p : Polynomial Nat, WeightedBound V p) ↔
      ∃ S : PolyTimeFun α BitStr, Solves V S := by
  constructor
  · rintro ⟨p,hp⟩
    exact ⟨_,weightedBound_solves U V p hp⟩
  · rintro ⟨S,hS⟩
    exact ⟨_,solver_weightedBound V S hS⟩

end PNPAbove.WP45
