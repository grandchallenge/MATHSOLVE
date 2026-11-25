import PNPAbove.WP34Scope
import MIPRE.Foundations.Cost.BinaryCompare

namespace PNPAbove.WP35
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

/-- A source polynomial equality test for binary natural identifiers. -/
noncomputable def eqNatProgram : PolyTimeFun (Nat × Nat) Bool :=
  PolyTimeFun.ite leNat (leNat.comp (snd.pair fst)) (PolyTimeFun.const false)

theorem eqNat_correct (i j : Nat) : eqNatProgram (i,j) = decide (i = j) := by
  change (if decide (i ≤ j) then decide (j ≤ i) else false) = decide (i = j)
  by_cases h : i = j
  · subst j; simp
  · have hh : ¬ (i ≤ j ∧ j ≤ i) := by omega
    by_cases hij : i ≤ j
    · have hji : ¬ j ≤ i := by omega
      simp [hij, hji, h]
    · simp [hij, h]


/-- Right-fold rank: keep the target and increment/reset a binary index. -/
def rankStep (s : Nat × Nat) (a : Nat) : Nat × Nat :=
  (s.1, if a = s.1 then 0 else s.2 + 1)

noncomputable def rankStepProgram : PolyTimeFun ((Nat × Nat) × Nat) (Nat × Nat) :=
  (fst.comp fst).pair
    (PolyTimeFun.ite (eqNatProgram.comp (snd.pair (fst.comp fst)))
      (PolyTimeFun.const (0 : Nat)) (inc.comp (snd.comp fst)))

theorem rankStep_correct (s : Nat × Nat) (a : Nat) :
    rankStepProgram (s,a) = rankStep s a := by
  change (s.1, if eqNatProgram (a,s.1) then 0 else s.2 + 1) = _
  rw [eqNat_correct]
  simp [rankStep]

theorem rankStep_growth (s : Nat × Nat) (a : Nat) :
    esize (rankStepProgram (s,a)) ≤ esize s + (C 4 : Polynomial Nat).eval (esize a) := by
  rw [rankStep_correct]
  rcases s with ⟨i, j⟩
  simp only [rankStep, esize_prod, Polynomial.eval_C]
  split_ifs
  · have h0 : esize (0 : Nat) = 1 := rfl
    have hp := esize_pos j
    omega
  · have hh := esize_succ_le j
    omega

theorem rank_fold (xs : List Nat) (i : Nat) :
    (xs.foldr (fun a s => rankStep s a) (i,0)) = (i,xs.idxOf i) := by
  induction xs with
  | nil => rfl
  | cons a xs ih =>
    rw [List.foldr_cons, ih, List.idxOf_cons]
    simp [rankStep]

/-- First occurrence, or list length if absent. One fixed program. -/
noncomputable def rankProgram : PolyTimeFun (List Nat × Nat) Nat :=
  snd.comp
    ((foldlAdd rankStepProgram (C 4) rankStep_growth).comp
      ((PolyTimeFun.reverse.comp fst).pair (snd.pair (PolyTimeFun.const (0 : Nat)))))

theorem rankProgram_correct (xs : List Nat) (i : Nat) :
    rankProgram (xs,i) = xs.idxOf i := by
  change (foldlAdd rankStepProgram (C 4) rankStep_growth
    (xs.reverse,(i,0))).2 = _
  simp only [foldlAdd_apply, rankStep_correct, List.foldl_reverse, rank_fold]

noncomputable def lengthProgram : PolyTimeFun (List Nat) Nat :=
  unaryToBin.comp length

theorem lengthProgram_correct (xs : List Nat) : lengthProgram xs = xs.length := by
  simp [lengthProgram]

/-- Insert one identifier iff absent; order is deterministic. -/
def insertUnique (xs : List Nat) (i : Nat) : List Nat :=
  if i ∈ xs then xs else i::xs

noncomputable def insertUniqueProgram : PolyTimeFun (List Nat × Nat) (List Nat) :=
  PolyTimeFun.ite
    (leNat.comp ((lengthProgram.comp fst).pair rankProgram))
    (snd.cons fst) fst

theorem insertUniqueProgram_correct (xs : List Nat) (i : Nat) :
    insertUniqueProgram (xs,i) = insertUnique xs i := by
  change (if leNat (lengthProgram xs,rankProgram (xs,i)) then i::xs else xs) = _
  rw [lengthProgram_correct, rankProgram_correct, leNat_apply]
  by_cases hi : i ∈ xs
  · have hh := List.idxOf_lt_length_iff.mpr hi
    simp [insertUnique, hi, show ¬ xs.length ≤ xs.idxOf i by omega]
  · rw [List.idxOf_eq_length hi]
    simp [insertUnique, hi]

def supportStep (xs : List Nat) (nd : Fml.Node) : List Nat :=
  match nd with
  | .inp i => insertUnique xs i
  | _ => xs

noncomputable def supportStepProgram : PolyTimeFun (List Nat × Fml.Node) (List Nat) :=
  MIPRE.SAT.PolyTimeFun.casesNode insertUniqueProgram fst
    (PolyTimeFun.id _) (PolyTimeFun.id _) (PolyTimeFun.id _)

theorem supportStep_correct (xs : List Nat) (nd : Fml.Node) :
    supportStepProgram (xs,nd) = supportStep xs nd := by
  cases nd with
  | inp i => exact insertUniqueProgram_correct xs i
  | const b => rfl
  | and => rfl
  | or => rfl
  | not => rfl

theorem supportStep_growth (xs : List Nat) (nd : Fml.Node) :
    esize (supportStepProgram (xs,nd)) ≤ esize xs + (X + C 1 : Polynomial Nat).eval (esize nd) := by
  rw [supportStep_correct]
  cases nd with
  | inp i =>
    simp only [supportStep, insertUnique, Polynomial.eval_add, Polynomial.eval_X, Polynomial.eval_C,
      esize_node_inp]
    split_ifs
    · omega
    · rw [esize_list_cons]; omega
  | const b => simp [supportStep]
  | and => simp [supportStep]
  | or => simp [supportStep]
  | not => simp [supportStep]

def support (f : Fml) : List Nat := f.rpn.foldl supportStep []

noncomputable def supportProgram : PolyTimeFun Fml (List Nat) :=
  (foldlAdd supportStepProgram (X + C 1) supportStep_growth).comp
    (Fml.rpnF.pair (PolyTimeFun.const ([] : List Nat)))

theorem supportProgram_correct (f : Fml) : supportProgram f = support f := by
  change foldlAdd supportStepProgram (X + C 1) supportStep_growth (f.rpn,[]) = _
  simp only [foldlAdd_apply, supportStep_correct, support]

theorem supportProgram_polytime (f : Fml) :
    ∃ t ≤ supportProgram.timeBound.eval (esize f),
      supportProgram.code.Runs (encode f) (encode (support f)) t := by
  simpa only [supportProgram_correct] using supportProgram.computes f

theorem mem_supportStep (xs : List Nat) (nd : Fml.Node) (i : Nat) :
    i ∈ supportStep xs nd ↔ i ∈ xs ∨ nd = .inp i := by
  cases nd with
  | inp j =>
    by_cases hj : j ∈ xs
    · simp [supportStep, insertUnique, hj]
      exact fun h => by subst j; exact hj
    · simp [supportStep, insertUnique, hj, eq_comm, or_comm]
  | const b => simp [supportStep]
  | and => simp [supportStep]
  | or => simp [supportStep]
  | not => simp [supportStep]

theorem mem_support_fold (nds : List Fml.Node) (xs : List Nat) (i : Nat) :
    i ∈ nds.foldl supportStep xs ↔ i ∈ xs ∨ Fml.Node.inp i ∈ nds := by
  induction nds generalizing xs with
  | nil => simp
  | cons nd nds ih =>
    rw [List.foldl_cons, ih, mem_supportStep, List.mem_cons]
    tauto

theorem mem_support (f : Fml) (i : Nat) :
    i ∈ support f ↔ Fml.Node.inp i ∈ f.rpn := by
  simp [support, mem_support_fold]

theorem supportStep_nodup (xs : List Nat) (nd : Fml.Node) (h : xs.Nodup) :
    (supportStep xs nd).Nodup := by
  cases nd with
  | inp i =>
    by_cases hi : i ∈ xs <;> simp [supportStep, insertUnique, hi, h]
  | const b => exact h
  | and => exact h
  | or => exact h
  | not => exact h

theorem support_fold_nodup (nds : List Fml.Node) (xs : List Nat) (h : xs.Nodup) :
    (nds.foldl supportStep xs).Nodup := by
  induction nds generalizing xs with
  | nil => exact h
  | cons nd nds ih =>
    exact ih _ (supportStep_nodup xs nd h)

theorem support_nodup (f : Fml) : (support f).Nodup :=
  support_fold_nodup _ _ List.nodup_nil

theorem supportStep_length (xs : List Nat) (nd : Fml.Node) :
    (supportStep xs nd).length ≤ xs.length + 1 := by
  cases nd with
  | inp i =>
    by_cases hi : i ∈ xs <;> simp [supportStep, insertUnique, hi]
  | const b => simp [supportStep]
  | and => simp [supportStep]
  | or => simp [supportStep]
  | not => simp [supportStep]

theorem support_fold_length (nds : List Fml.Node) (xs : List Nat) :
    (nds.foldl supportStep xs).length ≤ xs.length + nds.length := by
  induction nds generalizing xs with
  | nil => simp
  | cons nd nds ih =>
    have h := ih (supportStep xs nd)
    have hs := supportStep_length xs nd
    simp only [List.foldl_cons, List.length_cons]
    omega

theorem support_length_le (f : Fml) : (support f).length ≤ f.size := by
  simpa [support, Fml.length_rpn] using support_fold_length f.rpn []


/-- Evaluation only reads input identifiers appearing in the original RPN. -/
theorem eval_congr_support (f : Fml) (a b : Nat → Bool)
    (h : ∀ i, Fml.Node.inp i ∈ f.rpn → a i = b i) :
    f.eval a = f.eval b := by
  induction f with
  | inp i => exact h i (by simp [Fml.rpn])
  | const c => rfl
  | and f g ihf ihg =>
    simp only [Fml.eval]
    rw [ihf (fun i hi => h i (by simp [Fml.rpn, hi])),
      ihg (fun i hi => h i (by simp [Fml.rpn, hi]))]
  | or f g ihf ihg =>
    simp only [Fml.eval]
    rw [ihf (fun i hi => h i (by simp [Fml.rpn, hi])),
      ihg (fun i hi => h i (by simp [Fml.rpn, hi]))]
  | not f ih =>
    simp only [Fml.eval]
    rw [ih (fun i hi => h i (by simp [Fml.rpn, hi]))]

theorem inputsLt_iff_support (f : Fml) (m : Nat) :
    f.InputsLt m ↔ ∀ i, Fml.Node.inp i ∈ f.rpn → i < m := by
  induction f with
  | inp i => simp [Fml.InputsLt, Fml.rpn]
  | const c => simp [Fml.InputsLt, Fml.rpn]
  | and f g ihf ihg =>
    rw [Fml.InputsLt, ihf, ihg]
    simp [Fml.rpn, List.mem_append, or_imp, forall_and]
  | or f g ihf ihg =>
    rw [Fml.InputsLt, ihf, ihg]
    simp [Fml.rpn, List.mem_append, or_imp, forall_and]
  | not f ih =>
    rw [Fml.InputsLt, ih]
    simp [Fml.rpn]

/-- The actual distinct-support renaming; every original identifier has
one rank and no two different active identifiers share a rank. -/
def dense (f : Fml) : Fml :=
  f.rename (fun i => (support f).idxOf i)

theorem rank_active_lt (f : Fml) (i : Nat) (hi : Fml.Node.inp i ∈ f.rpn) :
    (support f).idxOf i < (support f).length :=
  List.idxOf_lt_length_iff.mpr ((mem_support f i).mpr hi)

theorem rank_inverse (f : Fml) (i : Nat) (hi : Fml.Node.inp i ∈ f.rpn) :
    (support f).getD ((support f).idxOf i) 0 = i := by
  have h := rank_active_lt f i hi
  rw [List.getD_eq_getElem _ _ h]
  exact List.getElem_idxOf h

theorem rank_at_position (f : Fml) (j : Nat) (hj : j < (support f).length) :
    (support f).idxOf (support f)[j] = j := by
  have hmem := List.getElem_mem hj
  have hi := List.idxOf_lt_length_iff.mpr hmem
  exact (support_nodup f).getElem_inj_iff.mp (List.getElem_idxOf hi)

theorem dense_exact_support (f : Fml) (j : Nat) :
    Fml.Node.inp j ∈ (dense f).rpn ↔ j < (support f).length := by
  unfold dense
  rw [Fml.rpn_rename, List.mem_map]
  constructor
  · rintro ⟨nd, hn, he⟩
    cases nd with
    | inp i =>
      have heq : (support f).idxOf i = j := Fml.Node.inp.inj he
      exact heq ▸ rank_active_lt f i hn
    | const b => simp [Fml.Node.rename] at he
    | and => simp [Fml.Node.rename] at he
    | or => simp [Fml.Node.rename] at he
    | not => simp [Fml.Node.rename] at he
  · intro hj
    let i := (support f)[j]
    refine ⟨.inp i, (mem_support f i).mp (List.getElem_mem hj), ?_⟩
    change Fml.Node.inp ((support f).idxOf i) = .inp j
    rw [rank_at_position f j hj]

theorem dense_scope (f : Fml) : (dense f).InputsLt (support f).length := by
  exact (inputsLt_iff_support _ _).mpr (fun j h => (dense_exact_support f j).mp h)

theorem dense_scope_minimal (f : Fml) (m : Nat) :
    (dense f).InputsLt m ↔ (support f).length ≤ m := by
  rw [inputsLt_iff_support]
  simp only [dense_exact_support]
  constructor
  · intro h
    by_contra hn
    have hlt : m < (support f).length := by omega
    exact (Nat.lt_irrefl m) (h m hlt)
  · intro h i hi; omega

theorem dense_sat_iff (f : Fml) :
    (∃ w : Nat → Bool, (dense f).eval w = true) ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · rintro ⟨w, hw⟩
    exact ⟨w ∘ (fun i => (support f).idxOf i), by simpa only [dense, Fml.eval_rename] using hw⟩
  · rintro ⟨w, hw⟩
    let v : Nat → Bool := fun j => w ((support f).getD j 0)
    refine ⟨v, ?_⟩
    rw [dense, Fml.eval_rename]
    have h := eval_congr_support f (v ∘ fun i => (support f).idxOf i) w
      (fun i hi => by
        change w ((support f).getD ((support f).idxOf i) 0) = w i
        rw [rank_inverse f i hi])
    rw [h]
    exact hw

/-- Actual source code, including the support list for witness transport. -/
noncomputable def denseProgram : PolyTimeFun Fml (Fml × List Nat) :=
  ((Fml.renameProg rankProgram).comp (supportProgram.pair (PolyTimeFun.id Fml))).pair
    supportProgram

theorem denseProgram_correct (f : Fml) : denseProgram f = (dense f, support f) := by
  simp [denseProgram, supportProgram_correct, rankProgram_correct, dense]

theorem denseProgram_polytime (f : Fml) :
    ∃ t ≤ denseProgram.timeBound.eval (esize f),
      denseProgram.code.Runs (encode f) (encode (dense f, support f)) t := by
  simpa only [denseProgram_correct] using denseProgram.computes f

/-- Source-polynomial verifier with polynomial-length certificates,
even when original variable names are extremely large binary numerals. -/
noncomputable def denseWitnessVerifier : PolyTimeFun (Fml × BitStr) Bool :=
  WP25.evalFormulaProgram.comp
    (((fst.comp denseProgram).comp fst).pair snd)

theorem denseWitnessVerifier_correct (f : Fml) (a : BitStr) :
    denseWitnessVerifier (f,a) = (dense f).eval (fun i => a.getD i false) := by
  change WP25.evalFormulaProgram ((denseProgram f).1,a) = _
  rw [denseProgram_correct, WP25.evalFormulaProgram_correct]

theorem denseWitnessVerifier_sound (f : Fml) (a : BitStr)
    (ha : denseWitnessVerifier (f,a) = true) :
    ∃ w : Nat → Bool, f.eval w = true := by
  apply (dense_sat_iff f).mp
  exact ⟨fun i => a.getD i false, by simpa only [denseWitnessVerifier_correct] using ha⟩

theorem denseWitnessVerifier_complete (f : Fml)
    (hf : ∃ w : Nat → Bool, f.eval w = true) :
    ∃ a : BitStr, a.length = (support f).length ∧
      a.length ≤ f.size ∧ denseWitnessVerifier (f,a) = true := by
  obtain ⟨w, hw⟩ := (dense_sat_iff f).mpr hf
  let v : Fin (support f).length → Bool := fun i => w i.val
  let a : BitStr := List.ofFn v
  have hlen : a.length = (support f).length := List.length_ofFn
  refine ⟨a, hlen, hlen ▸ support_length_le f, ?_⟩
  rw [denseWitnessVerifier_correct]
  have heq : (dense f).eval (fun i => a.getD i false) = (dense f).eval w := by
    apply Fml.eval_congr_of_inputsLt (dense_scope f)
    intro i hi
    rw [show a.getD i false = WP24.bitsAt v i from WP25.ofFn_getD_eq_bitsAt v i]
    simp [WP24.bitsAt, hi, v]
  rwa [heq]

theorem denseWitnessVerifier_iff (f : Fml) :
    (∃ a : BitStr, a.length ≤ f.size ∧ denseWitnessVerifier (f,a) = true) ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · rintro ⟨a, _, h⟩; exact denseWitnessVerifier_sound f a h
  · intro h
    obtain ⟨a, _, hlen, ha⟩ := denseWitnessVerifier_complete f h
    exact ⟨a, hlen, ha⟩

theorem denseWitnessVerifier_polytime (f : Fml) (a : BitStr) :
    ∃ t ≤ denseWitnessVerifier.timeBound.eval (esize f + esize a + 1),
      denseWitnessVerifier.code.Runs (encode (f,a)) (encode (denseWitnessVerifier (f,a))) t := by
  simpa only [esize_prod] using denseWitnessVerifier.computes (f,a)


/-- Count only literal/input occurrences, not connective or padding nodes. -/
def inputWeight : Fml.Node → Nat
  | .inp _ => 1
  | _ => 0

def countInputs (nds : List Fml.Node) : Nat := (nds.map inputWeight).sum

theorem countInputs_append (a b : List Fml.Node) :
    countInputs (a ++ b) = countInputs a + countInputs b := by
  simp [countInputs, List.sum_append]

theorem supportStep_weight (xs : List Nat) (nd : Fml.Node) :
    (supportStep xs nd).length ≤ xs.length + inputWeight nd := by
  cases nd with
  | inp i => exact supportStep_length xs _
  | const b => rfl
  | and => rfl
  | or => rfl
  | not => rfl

theorem support_fold_weight (nds : List Fml.Node) (xs : List Nat) :
    (nds.foldl supportStep xs).length ≤ xs.length + countInputs nds := by
  induction nds generalizing xs with
  | nil => simp [countInputs]
  | cons nd nds ih =>
    have h := ih (supportStep xs nd)
    have hs := supportStep_weight xs nd
    simp only [List.foldl_cons, countInputs, List.map_cons, List.sum_cons] at *
    omega

theorem support_le_input_count (f : Fml) :
    (support f).length ≤ countInputs f.rpn := by
  simpa [support] using support_fold_weight f.rpn []

theorem count_literal (l : WP29.EncLit) :
    countInputs (WP29.literal l).rpn = 1 := by
  rcases l with ⟨i,b⟩
  cases b <;> simp [WP29.literal, Fml.rpn, countInputs, inputWeight]

theorem count_clause (c : WP29.EncClause) :
    countInputs (WP29.clause c).rpn = 3 := by
  simp [WP29.clause, Fml.rpn, countInputs_append, count_literal,
    show countInputs [Fml.Node.or, Fml.Node.or] = 0 by rfl]

theorem count_fold_clauses (cs : WP29.Enc3CNF) (f : Fml) :
    countInputs ((cs.map WP29.clause).foldl Fml.and f).rpn =
      countInputs f.rpn + 3 * cs.length := by
  induction cs generalizing f with
  | nil => simp
  | cons c cs ih =>
    rw [List.map_cons, List.foldl_cons, ih]
    simp only [Fml.rpn, countInputs_append, count_clause, List.length_cons]
    change countInputs f.rpn + 3 + 0 + 3 * cs.length =
      countInputs f.rpn + 3 * (cs.length + 1)
    omega

theorem formula_count (cs : WP29.Enc3CNF) :
    countInputs (WP29.formula cs).rpn = 3 * cs.length := by
  unfold WP29.formula Fml.andList
  rw [count_fold_clauses]
  simp [Fml.rpn, countInputs, inputWeight]

theorem dense_3CNF_support_le (cs : WP29.Enc3CNF) :
    (support (WP29.formula cs)).length ≤ 3 * cs.length := by
  rw [← formula_count]
  exact support_le_input_count _

/-- The actual normalizer on original encoded 3CNF returns its dense formula
and distinct active identifier list. Its code does not depend on input. -/
noncomputable def dense3CNFProgram : PolyTimeFun WP29.Enc3CNF (Fml × List Nat) :=
  denseProgram.comp WP29.formulaProgram

theorem dense3CNFProgram_correct (cs : WP29.Enc3CNF) :
    dense3CNFProgram cs = (dense (WP29.formula cs), support (WP29.formula cs)) := by
  simp [dense3CNFProgram, WP29.formulaProgram_correct, denseProgram_correct]

theorem dense3CNFProgram_polytime (cs : WP29.Enc3CNF) :
    ∃ t ≤ dense3CNFProgram.timeBound.eval (esize cs),
      dense3CNFProgram.code.Runs (encode cs) (encode (dense3CNFProgram cs)) t :=
  dense3CNFProgram.computes cs

theorem dense3CNFProgram_sat (m : Nat) (cs : List (SAT.Clause3 (Fin m))) :
    let p := dense3CNFProgram (WP29.fromOriginal3CNF cs)
    p.1.InputsLt p.2.length ∧
      p.2.length ≤ 3 * cs.length ∧
      (WP24.Satisfiable p.2.length p.1 ↔
        ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w) := by
  dsimp only
  rw [dense3CNFProgram_correct]
  let f := WP29.formula (WP29.fromOriginal3CNF cs)
  change (dense f).InputsLt (support f).length ∧ (support f).length ≤ 3 * cs.length ∧ _
  refine ⟨dense_scope f, ?_, ?_⟩
  · simpa only [f, WP29.fromOriginal3CNF, List.length_map] using
      dense_3CNF_support_le (WP29.fromOriginal3CNF cs)
  · rw [WP34.satisfiable_iff_global _ _ (dense_scope f), dense_sat_iff,
      ← WP34.satisfiable_iff_global f m (WP29.original3CNF_scoped cs)]
    exact exists_congr (fun w => (WP29.originalFinite3CNF_sat_iff cs w).symm)

/-- A short certificate in bits, with an actual original polynomial verifier. -/
theorem denseWitnessVerifier_source_length_iff (f : Fml) :
    (∃ a : BitStr, a.length ≤ esize f ∧ denseWitnessVerifier (f,a) = true) ↔
      ∃ w : Nat → Bool, f.eval w = true := by
  constructor
  · rintro ⟨a, _, h⟩; exact denseWitnessVerifier_sound f a h
  · intro h
    obtain ⟨a, _, hlen, ha⟩ := denseWitnessVerifier_complete f h
    exact ⟨a, hlen.trans (WP32.source_fml_node_count_le_encoded f), ha⟩


/-- The actual dense-normalized compiler feeding the original formula
index and native compression threshold. -/
noncomputable def denseIndexProgram (r : Nat) : PolyTimeFun WP29.Enc3CNF Nat :=
  WP28B.formulaIndexProgram.comp
    ((WP32.padTrueProgram r).comp (fst.comp dense3CNFProgram))

theorem denseIndexProgram_correct (r : Nat) (cs : WP29.Enc3CNF) :
    denseIndexProgram r cs =
      WP28B.formulaIndex (WP32.padTrue r (dense (WP29.formula cs))) := by
  simp [denseIndexProgram, WP28B.formulaIndexProgram_correct,
    WP32.padTrueProgram_correct, dense3CNFProgram_correct]

theorem denseIndex_threshold (r : Nat) (cs : WP29.Enc3CNF) :
    r ≤ denseIndexProgram r cs := by
  rw [denseIndexProgram_correct]
  let f := WP32.padTrue r (dense (WP29.formula cs))
  have hsize : r ≤ esize f :=
    (WP32.padTrue_size_lower r _).trans (WP32.source_fml_node_count_le_encoded _)
  exact (Nat.le_of_lt Nat.lt_two_pow_self).trans
    ((Nat.pow_le_pow_right (by decide : 0 < (2 : Nat)) hsize).trans
      (WP28B2.formulaIndex_numeric_exponential_lower f))

theorem denseIndexProgram_polytime (r : Nat) (cs : WP29.Enc3CNF) :
    ∃ t ≤ (denseIndexProgram r).timeBound.eval (esize cs),
      (denseIndexProgram r).code.Runs (encode cs) (encode (denseIndexProgram r cs)) t :=
  (denseIndexProgram r).computes cs

theorem padded_dense_scope_exact (r : Nat) (f : Fml) :
    WP34.scope (WP32.padTrue r (dense f)) = (support f).length := by
  rw [WP34.scope_padTrue]
  apply Nat.le_antisymm
  · exact (WP34.scope_le_iff _ _).mpr (dense_scope f)
  · exact (dense_scope_minimal f _).mp ((WP34.scope_le_iff _ _).mp le_rfl)

theorem denseIndex_budget (G : GapCompression) (U : Cost.UniversalMachine)
    (lam : Nat) (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (cs : WP29.Enc3CNF) :
    (support (WP29.formula cs)).length ≤ (2 ^ denseIndexProgram G.C₀ cs) ^ lam := by
  rw [denseIndexProgram_correct, ← padded_dense_scope_exact G.C₀ (WP29.formula cs)]
  exact WP34.canonical_budget G U _ lam hB

/-- Dense normalization plus the native compressed promise, on arbitrary
original finite 3CNF, needs no ambient scope or external budget. -/
theorem dense_classical_transfer
    (G : GapCompression) (U : Cost.UniversalMachine)
    (oracle : PolyTimeFun Nat Bool) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam)
    (ho : WP34.SolvesValidPromise G U lam oracle)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m))) :
    (oracle.comp (denseIndexProgram G.C₀)) (WP29.fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
  let f := WP29.formula (WP29.fromOriginal3CNF cs)
  let d := WP32.padTrue G.C₀ (dense f)
  have hk : G.C₀ ≤ WP28B.formulaIndex d := by
    simpa only [denseIndexProgram_correct] using
      denseIndex_threshold G.C₀ (WP29.fromOriginal3CNF cs)
  have hs : (∃ w : Nat → Bool, d.eval w = true) ↔
      ∃ w : Fin m → Bool, (WP24.threeCNFSet cs).Sat w := by
    simp only [d, WP32.padTrue_eval]
    rw [dense_sat_iff, ← WP34.satisfiable_iff_global f m (WP29.original3CNF_scoped cs)]
    exact exists_congr (fun w => (WP29.originalFinite3CNF_sat_iff cs w).symm)
  have he : oracle (WP28B.formulaIndex d) = true ↔ ∃ w : Nat → Bool, d.eval w = true := by
    constructor
    · intro ht
      by_contra hu
      have hf := (ho d hk).2 (WP34.canonical_compressed_no G U d lam hB hk hu)
      rw [hf] at ht
      contradiction
    · intro ht
      exact (ho d hk).1 (WP34.canonical_compressed_yes G U d lam hB hk ht)
  change oracle (denseIndexProgram G.C₀ (WP29.fromOriginal3CNF cs)) = true ↔ _
  rw [denseIndexProgram_correct]
  exact he.trans hs

end PNPAbove.WP35
