import PNPAbove.WP24CNF
import MIPRE.Foundations.SAT.FmlProg
import PNPAbove.WP28B2Value

/-! Uniform original SAT finite-3CNF source compiler, not merely a
Lean function. Explicit clauses are encoded as lists of 3 signed
natural indices. This yields a fixed closed Cost.Prog independent of
formula size, using native binary input positions. -/
namespace PNPAbove.WP29
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

abbrev EncLit := Nat × Bool
abbrev EncClause := EncLit × EncLit × EncLit
abbrev Enc3CNF := List EncClause

def literal (l : EncLit) : Fml :=
  if l.2 then .inp l.1 else .not (.inp l.1)

def clause (c : EncClause) : Fml :=
  .or (literal c.1) (.or (literal c.2.1) (literal c.2.2))

def formula (cs : Enc3CNF) : Fml :=
  Fml.andList (cs.map clause)

/-- Native source program, with original polynomial Cost.Prog execution,
for any signed binary literal, including negative indices (Nat only). -/
noncomputable def literalProgram : PolyTimeFun EncLit Fml :=
  PolyTimeFun.ite snd (Fml.inpF.comp fst)
    (Fml.notF.comp (Fml.inpF.comp fst))

theorem literalProgram_correct (l : EncLit) :
    literalProgram l = literal l := by
  rcases l with ⟨i, b⟩
  cases b <;> rfl

/-- The actual three-literal source compiler. -/
noncomputable def clauseProgram : PolyTimeFun EncClause Fml :=
  Fml.orF.comp
    ((literalProgram.comp fst).pair
      (Fml.orF.comp
        ((literalProgram.comp (fst.comp snd)).pair
          (literalProgram.comp (snd.comp snd)))))

theorem clauseProgram_correct (c : EncClause) :
    clauseProgram c = clause c := by
  rfl

/-- The same original Cost.Prog handles arbitrary-length finite
3CNF clause lists in source polynomial time. -/
noncomputable def formulaProgram : PolyTimeFun Enc3CNF Fml :=
  SAT.andListP.comp (PolyTimeFun.map clauseProgram)

theorem formulaProgram_correct (cs : Enc3CNF) :
    formulaProgram cs = formula cs := by
  change Fml.andList (cs.map clauseProgram) = Fml.andList (cs.map clause)
  simp only [List.map_congr_left (fun c _ => clauseProgram_correct c)]

theorem formulaProgram_polynomial (cs : Enc3CNF) :
    ∃ t ≤ formulaProgram.timeBound.eval (esize cs),
      formulaProgram.code.Runs (encode cs) (encode (formula cs)) t := by
  simpa only [formulaProgram_correct] using formulaProgram.computes cs

theorem formulaProgram_closed :
    formulaProgram.code.WellScoped 1 := formulaProgram.closed

/-- Source signed variable semantics. -/
def litValue (l : EncLit) (w : Nat → Bool) : Bool :=
  if l.2 then w l.1 else !(w l.1)

def clauseValue (c : EncClause) (w : Nat → Bool) : Bool :=
  litValue c.1 w || litValue c.2.1 w || litValue c.2.2 w

theorem literal_sound (l : EncLit) (w : Nat → Bool) :
    (literal l).eval w = litValue l w := by
  rcases l with ⟨i,b⟩
  cases b <;> rfl

theorem clause_sound (c : EncClause) (w : Nat → Bool) :
    (clause c).eval w = clauseValue c w := by
  simp [clause, clauseValue, Fml.eval, literal_sound, Bool.or_assoc]

theorem formula_sound (cs : Enc3CNF) (w : Nat → Bool) :
    (formula cs).eval w = cs.all (fun c => clauseValue c w) := by
  simp only [formula, Fml.eval_andList, List.all_map]
  exact List.all_congr rfl (fun c => by simpa only [Function.comp_apply] using clause_sound c w)


/-- Convert one genuine original signed SAT.Lit (Fin n) into a
source-encodable signed binary-index literal. -/
def fromOriginalLit {n : Nat} (l : SAT.Lit (Fin n)) : EncLit :=
  (l.var.val, l.pos)

def fromOriginalClause {n : Nat} (c : SAT.Clause3 (Fin n)) : EncClause :=
  (fromOriginalLit c.l₁, fromOriginalLit c.l₂, fromOriginalLit c.l₃)

/-- Mathematical bridge from original Fin-indexed clauses to the
explicit, source-encoded, polynomial-time machine input language. -/
def fromOriginal3CNF {n : Nat} (cs : List (SAT.Clause3 (Fin n))) : Enc3CNF :=
  cs.map fromOriginalClause

theorem fromOriginalLit_sound {n : Nat} (l : SAT.Lit (Fin n))
    (w : Fin n → Bool) :
    litValue (fromOriginalLit l) (PNPAbove.WP24.bitsAt w) = l.eval w := by
  rcases l with ⟨v, pos⟩
  cases pos <;> simp [litValue, fromOriginalLit, SAT.Lit.eval,
    PNPAbove.WP24.bitsAt_fin]

theorem fromOriginalClause_sound {n : Nat} (c : SAT.Clause3 (Fin n))
    (w : Fin n → Bool) :
    clauseValue (fromOriginalClause c) (PNPAbove.WP24.bitsAt w) = c.eval w := by
  rcases c with ⟨l₁, l₂, l₃⟩
  simp [clauseValue, fromOriginalClause, SAT.Clause3.eval,
    fromOriginalLit_sound, Bool.or_assoc]

/-- Executable 3CNF compiler agreement with original finite Cnf3.Sat
for all variable counts, clauses and assignments. -/
theorem originalFinite3CNF_correct {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) (w : Fin n → Bool) :
    (formula (fromOriginal3CNF cs)).eval (PNPAbove.WP24.bitsAt w) =
      cs.all (fun c => c.eval w) := by
  rw [formula_sound]
  simp only [fromOriginal3CNF, List.all_map]
  exact List.all_congr rfl (fun c => by
    simpa only [Function.comp_apply] using fromOriginalClause_sound c w)

/-- SAT of the original actual MIPRE finite Cnf3 is equivalent to
satisfiability of our uniform compiled original Fml. -/
theorem originalFinite3CNF_sat_iff {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) (w : Fin n → Bool) :
    (PNPAbove.WP24.threeCNFSet cs).Sat w ↔
      (formula (fromOriginal3CNF cs)).eval (PNPAbove.WP24.bitsAt w) = true := by
  rw [originalFinite3CNF_correct]
  exact (PNPAbove.WP24.original_3CNF_sat_iff cs w).trans
    (by rw [PNPAbove.WP24.from3CNF_correct])

/-- The original source indexed verifier accepts the *exact same*
SAT instances when the instance is an explicit finite 3CNF. -/
theorem native3CNF_sat_equivalence {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) :
    PNPAbove.WP28B.IndexedSAT n
        (PNPAbove.WP28B.formulaIndex (formula (fromOriginal3CNF cs))) ↔
      ∃ w : Fin n → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  rw [PNPAbove.WP28B.indexedSAT_formula_iff]
  unfold PNPAbove.WP24.Satisfiable
  exact exists_congr (fun w => (originalFinite3CNF_sat_iff cs w).symm)

/-- A fixed original source program composes BOTH actual original
polynomial-time compilers, not a metalevel SAT reduction. -/
noncomputable def source3CNFIndexProgram : PolyTimeFun Enc3CNF Nat :=
  PNPAbove.WP28B.formulaIndexProgram.comp formulaProgram

theorem source3CNFIndexProgram_correct (cs : Enc3CNF) :
    source3CNFIndexProgram cs =
      PNPAbove.WP28B.formulaIndex (formula cs) := by
  simp [source3CNFIndexProgram, formulaProgram_correct,
    PNPAbove.WP28B.formulaIndexProgram_correct]

/-- Exact original binary-index source-size accounting of the
compiled SAT source formula. -/
theorem source3CNFIndex_bit_length (cs : Enc3CNF) :
    Nat.size (source3CNFIndexProgram cs) = esize (formula cs) + 1 := by
  rw [source3CNFIndexProgram_correct]
  exact PNPAbove.WP28B.formulaIndex_bit_length (formula cs)

/-- Original source index decoder recovers the same compiled formula
data, for all finite 3CNF inputs. -/
theorem source3CNFIndex_roundtrip (cs : Enc3CNF) :
    PNPAbove.WP28B.decodeDataProgram (source3CNFIndexProgram cs) =
      encode (formula cs) := by
  rw [source3CNFIndexProgram_correct]
  have h := PNPAbove.WP28B.formulaIndex_decode (formula cs)
  simpa only [PNPAbove.WP28B.formulaIndexProgram_correct] using h

/-- An actual original Cost.Prog and source polynomial runtime proof
for arbitrary-size 3CNF-to-unique-verifier-index compilation. -/
theorem source3CNFIndex_polytime (cs : Enc3CNF) :
    ∃ t ≤ source3CNFIndexProgram.timeBound.eval (esize cs),
      source3CNFIndexProgram.code.Runs
        (encode cs) (encode (source3CNFIndexProgram cs)) t :=
  source3CNFIndexProgram.computes cs

theorem source3CNFIndex_closed :
    source3CNFIndexProgram.code.WellScoped 1 :=
  source3CNFIndexProgram.closed


/-- An original signed binary variable less than n stays inside the
declared formula variable budget. -/
theorem literal_inputs {n : Nat} (l : EncLit) (hl : l.1 < n) :
    (literal l).InputsLt n := by
  rcases l with ⟨i, b⟩
  cases b <;> simpa [literal, Fml.InputsLt] using hl

theorem originalClause_inputs {n : Nat}
    (c : SAT.Clause3 (Fin n)) :
    (clause (fromOriginalClause c)).InputsLt n := by
  rcases c with ⟨l₁,l₂,l₃⟩
  simp only [clause, Fml.InputsLt]
  exact ⟨literal_inputs (fromOriginalLit l₁) l₁.var.isLt,
    literal_inputs (fromOriginalLit l₂) l₂.var.isLt,
    literal_inputs (fromOriginalLit l₃) l₃.var.isLt⟩

/-- The compiler cannot reference undeclared SAT variables for
genuine source finite Cnf3 inputs; this is the prerequisite for
the source-native UNSAT rejection/quantum-value-zero theorem. -/
theorem original3CNF_scoped {n : Nat}
    (cs : List (SAT.Clause3 (Fin n))) :
    (formula (fromOriginal3CNF cs)).InputsLt n := by
  unfold formula fromOriginal3CNF
  rw [List.map_map]
  apply Fml.InputsLt.andList
  intro f hf
  obtain ⟨c, hc, rfl⟩ := List.mem_map.mp hf
  exact originalClause_inputs c

/-- The output binary numeral is polynomial in INPUT DESCRIPTION
length, despite the possibility that its NUMERIC VALUE is exponential.
This is source Cost.Prog execution evidence, not asymptotic guesswork. -/
theorem source3CNFIndex_binary_size_bound (cs : Enc3CNF) :
    Nat.size (source3CNFIndexProgram cs) ≤
      source3CNFIndexProgram.timeBound.eval (esize cs) := by
  calc
    Nat.size (source3CNFIndexProgram cs)
       ≤ esize (source3CNFIndexProgram cs) :=
         size_le_esize_nat _
    _ ≤ source3CNFIndexProgram.timeBound.eval (esize cs) :=
         source3CNFIndexProgram.esize_apply_le cs


/-- Each original source signed literal uses at most two gates. -/
theorem literal_gate_bound (l : EncLit) :
    (literal l).size ≤ 2 := by
  rcases l with ⟨i, b⟩
  cases b <;> simp [literal, Fml.size]

/-- A three-literal clause uses at most eight original source gates. -/
theorem clause_gate_bound (c : EncClause) :
    (clause c).size ≤ 8 := by
  have h1 := literal_gate_bound c.1
  have h2 := literal_gate_bound c.2.1
  have h3 := literal_gate_bound c.2.2
  dsimp [clause, Fml.size]
  omega

private theorem andList_gate_aux (l : List Fml) (acc : Fml)
    (h : ∀ f ∈ l, f.size ≤ 8) :
    (l.foldl Fml.and acc).size ≤ acc.size + 9 * l.length := by
  induction l generalizing acc with
  | nil => simp
  | cons f fs ih =>
    have hf : f.size ≤ 8 := h f (by simp)
    have hfs : ∀ g ∈ fs, g.size ≤ 8 := by
      intro g hg
      exact h g (by simp [hg])
    have hrec := ih (Fml.and acc f) hfs
    simp only [List.foldl_cons, List.length_cons]
    calc
      (List.foldl Fml.and (Fml.and acc f) fs).size
          ≤ (Fml.and acc f).size + 9 * fs.length := hrec
      _ ≤ acc.size + 9 * (fs.length + 1) := by
        simp only [Fml.size]
        omega

/-- The original gate-count bound of the uniform executable 3CNF
compiler is linear in its clause count, including the empty case. -/
theorem formula_gate_bound (cs : Enc3CNF) :
    (formula cs).size ≤ 9 * cs.length + 1 := by
  unfold formula Fml.andList
  have h : ∀ f ∈ cs.map clause, f.size ≤ 8 := by
    intro f hf
    obtain ⟨c, _, rfl⟩ := List.mem_map.mp hf
    exact clause_gate_bound c
  have hle := andList_gate_aux (cs.map clause) (Fml.const true) h
  simp only [List.length_map, Fml.size] at hle
  omega

/-- Every original explicit 3CNF clause necessarily contributes
at least one source Boolean formula gate. -/
private theorem foldl_and_size_lower (l : List Fml) (acc : Fml) :
    acc.size + l.length ≤ (l.foldl Fml.and acc).size := by
  induction l generalizing acc with
  | nil => simp
  | cons f fs ih =>
      simp only [List.foldl_cons, List.length_cons]
      calc
        acc.size + (fs.length + 1) ≤ (Fml.and acc f).size + fs.length := by
          simp only [Fml.size]
          omega
        _ ≤ (fs.foldl Fml.and (Fml.and acc f)).size := ih _

/-- Source circuit size is AT LEAST the number of input clauses,
in addition to the already proved at-most-nine-gates-per-clause bound. -/
theorem formula_gate_lower (cs : Enc3CNF) :
    cs.length ≤ (formula cs).size := by
  unfold formula Fml.andList
  have h := foldl_and_size_lower (cs.map clause) (Fml.const true)
  simp only [List.length_map, Fml.size] at h
  omega

/-- The numerical source index grows exponentially in input
CLAUSE COUNT in this particular encoding. This is a kernel-checked
obstruction to calling polynomial-in-numeric-index bounds polynomial
in the original explicit 3CNF description length. -/
theorem source3CNFIndex_numeric_exponential_lower (cs : Enc3CNF) :
    2 ^ cs.length ≤ source3CNFIndexProgram cs := by
  have hf : (formula cs).size ≤ esize (formula cs) := by
    change (formula cs).size ≤ esize (formula cs).rpn
    simpa only [Fml.length_rpn] using length_le_esize_list (formula cs).rpn
  have hindex : 2 ^ (esize (formula cs)) ≤
      PNPAbove.WP28B.formulaIndex (formula cs) := by
    apply Nat.lt_size.mp
    rw [PNPAbove.WP28B.formulaIndex_bit_length]
    omega
  rw [source3CNFIndexProgram_correct]
  exact (Nat.pow_le_pow_right (by omega : (1:Nat) ≤ 2)
    ((formula_gate_lower cs).trans hf)).trans hindex

/-- The actual original fixed source Verifier 7 game is value ONE
for a SAT 3CNF, after the real polynomial-time 3CNF-to-index
source compiler. This is not a surrogate game. -/
theorem native3CNFValStar_one_of_sat
    (U : MIPRE.Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (T : Nat) (hT : m ≤ T)
    (hSAT : ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w) :
    (PNPAbove.WP28B2.fixedIndexedVerifier U S).valStar
      (source3CNFIndexProgram (fromOriginal3CNF cs)) T = 1 := by
  rw [source3CNFIndexProgram_correct]
  apply PNPAbove.WP28B2.fixedIndexedVerifier_valStar_one_of_sat
    U S (formula (fromOriginal3CNF cs)) m T hT
  obtain ⟨w, hw⟩ := hSAT
  exact ⟨w, (originalFinite3CNF_sat_iff cs w).mp hw⟩

/-- The actual original fixed seven-level game's unrestricted tensor
quantum value is ZERO on UNSAT original 3CNF, without extra
restrictions on either prover's possible answers. -/
theorem native3CNFValStar_zero_of_unsat
    (U : MIPRE.Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    {m : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (T : Nat)
    (hUNSAT : ¬ ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w) :
    (PNPAbove.WP28B2.fixedIndexedVerifier U S).valStar
      (source3CNFIndexProgram (fromOriginal3CNF cs)) T = 0 := by
  rw [source3CNFIndexProgram_correct]
  apply PNPAbove.WP28B2.fixedIndexedVerifier_valStar_zero_of_unsat
    U S (formula (fromOriginal3CNF cs)) m T (original3CNF_scoped cs)
  intro ⟨w, hw⟩
  exact hUNSAT ⟨w, (originalFinite3CNF_sat_iff cs w).mpr hw⟩

/-- The only classical-algorithm transfer licensed by the source:
if someone SUPPLIES a genuine original polynomial-time oracle that
correctly decides the ORIGINAL fixed verifier's 1/0 promise on all
scoped source inputs, composing it with our source 3CNF compiler
is a genuine original polynomial-time SAT decider. NO such oracle
is constructed or assumed by our theorems. -/
noncomputable def conditionalSATProgram
    (oracle : Cost.PolyTimeFun Nat Bool) :
    Cost.PolyTimeFun Enc3CNF Bool :=
  oracle.comp source3CNFIndexProgram

/-- Exact original Cost.PolyTimeFun classical reduction, with the
unknown efficient-game-value algorithm named as a VISIBLE premise.
This is an IF-THEN theorem, not a proof of the antecedent. -/
theorem conditionalClassicalSATTransfer
    (U : MIPRE.Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (oracle : Cost.PolyTimeFun Nat Bool)
    (horacle : ∀ (f : SAT.Fml) (m T : Nat), f.InputsLt m → m ≤ T →
      (oracle (PNPAbove.WP28B.formulaIndex f) = true ↔
        (PNPAbove.WP28B2.fixedIndexedVerifier U S).valStar
          (PNPAbove.WP28B.formulaIndex f) T = 1))
    {m : Nat} (cs : List (SAT.Clause3 (Fin m)))
    (T : Nat) (hT : m ≤ T) :
    conditionalSATProgram oracle (fromOriginal3CNF cs) = true ↔
      ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  change oracle (source3CNFIndexProgram (fromOriginal3CNF cs)) = true ↔ _
  rw [source3CNFIndexProgram_correct]
  rw [horacle (formula (fromOriginal3CNF cs)) m T
    (original3CNF_scoped cs) hT]
  rw [PNPAbove.WP28B2.fixedIndexedVerifier_valStar_one_iff_sat
    U S (formula (fromOriginal3CNF cs)) m T (original3CNF_scoped cs) hT]
  exact exists_congr (fun w => (originalFinite3CNF_sat_iff cs w).symm)

/-- If the oracle above existed, the original source-composed SAT
decider would have a real polynomial source runtime certificate. -/
theorem conditionalClassicalSATPolytime
    (oracle : Cost.PolyTimeFun Nat Bool) (cs : Enc3CNF) :
    ∃ t ≤ (conditionalSATProgram oracle).timeBound.eval (esize cs),
      (conditionalSATProgram oracle).code.Runs
        (encode cs) (encode (conditionalSATProgram oracle cs)) t :=
  (conditionalSATProgram oracle).computes cs

end PNPAbove.WP29
