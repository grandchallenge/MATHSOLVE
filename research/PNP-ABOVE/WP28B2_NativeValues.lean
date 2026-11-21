import PNPAbove.WP28B2Raw
import MIPRE.Foundations.SAT.Rename

/-!
Actual original source-normal-form Verifier7 SAT quantum and classical
witness promises at the exact encoded source index. This is NOT a claim
that the MIPRE GapCompression's 2^k-index premise is automatically met.
-/

namespace PNPAbove.WP28B2
open MIPRE MIPRE.Cost

/-- The actual source-native seven-level verifier is synchronous at any
formula's exact binary index: it never accepts different answers to
identical questions there. -/
theorem fixedIndexedVerifier_synchronous (U : Cost.UniversalMachine)
    (S : MIPRE.CL.Sampler 7) (f : MIPRE.SAT.Fml) :
    (fixedIndexedVerifier U S).IsSynchronousAt
       (PNPAbove.WP28B.formulaIndex f) := by
  intro q a b hab hacc
  exact hab ((fixedIndexedVerifier_accepts_iff U S f q q a b).mp hacc).2.2.2

/-- An actual original PCC strategy wins surely on the source-native
Game, not on an abstract witness predicate. -/
theorem fixedIndexedVerifier_HasPerfectPCC_of_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (fixedIndexedVerifier U S).HasPerfectPCC
      (PNPAbove.WP28B.formulaIndex f) T := by
  obtain ⟨w, hw⟩ := hSAT
  let a : BitStr := List.ofFn w
  have ha : a.length ≤ T := by
    simp only [a, List.length_ofFn]
    omega
  apply (fixedIndexedVerifier U S).hasPerfectPCC_of_accepts_diagonal ⟨a, ha⟩
  intro x y
  rw [fixedIndexedVerifier_accepts_iff]
  refine ⟨MIPRE.CL.length_toBits x, MIPRE.CL.length_toBits y, ?_, rfl⟩
  have heval : (fun i => a.getD i false) = PNPAbove.WP24.bitsAt w := by
    funext i
    exact PNPAbove.WP25.ofFn_getD_eq_bitsAt w i
  simpa only [heval] using hw

/-- A formula with bounded original source input variables and no SAT
assignment makes every canonical raw source response fail, in every
question pair for the precise formula index. -/
theorem fixedIndexedVerifier_rejects_all_of_unsat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f)
    (x y a b : BitStr) :
    ¬ (fixedIndexedVerifier U S).decider.Accepts
      (PNPAbove.WP28B.formulaIndex f) x y a b := by
  intro hacc
  obtain ⟨_, _, hf, _⟩ :=
    (fixedIndexedVerifier_accepts_iff U S f x y a b).mp hacc
  apply hunsat
  let w : Fin m → Bool := fun i => a.getD i.val false
  refine ⟨w, ?_⟩
  have heq : f.eval (fun i => a.getD i false) =
      f.eval (PNPAbove.WP24.bitsAt w) := by
    apply MIPRE.SAT.Fml.eval_congr_of_inputsLt hscope
    intro i hi
    simp [PNPAbove.WP24.bitsAt, hi, w]
  exact heq ▸ hf

/-- Actual ORIGINAL source MIPRE.Verifier.valStar is exactly ZERO for
each UNSAT source instance at its exact binary source game index. -/
theorem fixedIndexedVerifier_valStar_zero_of_unsat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hscope : f.InputsLt m) (hunsat : ¬ PNPAbove.WP24.Satisfiable m f) :
    (fixedIndexedVerifier U S).valStar
      (PNPAbove.WP28B.formulaIndex f) T = 0 := by
  apply (fixedIndexedVerifier U S).valStar_eq_zero_of_rejects_all
  intro x y a b
  exact fixedIndexedVerifier_rejects_all_of_unsat U S f m
    hscope hunsat x y a b

/-- Exact original native tensor quantum value ONE on satisfiable
source instances with sufficient response budget. -/
theorem fixedIndexedVerifier_valStar_one_of_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hT : m ≤ T) (hSAT : PNPAbove.WP24.Satisfiable m f) :
    (fixedIndexedVerifier U S).valStar
      (PNPAbove.WP28B.formulaIndex f) T = 1 :=
  (fixedIndexedVerifier U S).valStar_eq_one_of_hasPerfectPCC
    (fixedIndexedVerifier_HasPerfectPCC_of_sat U S f m T hT hSAT)

/-- Exact unconditional original-source SAT/quantum-game promise for a
SINGLE fixed seven-level verifier with one UNIFORM IsBounded lambda.
The game index is formulaIndex f, not the 2^k index used by the
source GapCompression theorem. -/
theorem fixedIndexedVerifier_valStar_one_iff_sat
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    (f : MIPRE.SAT.Fml) (m T : Nat)
    (hscope : f.InputsLt m) (hT : m ≤ T) :
    ((fixedIndexedVerifier U S).valStar
      (PNPAbove.WP28B.formulaIndex f) T = 1) ↔
      PNPAbove.WP24.Satisfiable m f := by
  constructor
  · intro hv
    by_contra h
    have hz := fixedIndexedVerifier_valStar_zero_of_unsat U S
      f m T hscope h
    rw [hz] at hv
    norm_num at hv
  · exact fixedIndexedVerifier_valStar_one_of_sat U S f m T hT

/-- Original source finite 3CNF SAT is equivalent to a perfect original
source-game PCC strategy at the injectively encoded formula index. -/
theorem fixedIndexedVerifier_3CNF_PCC_iff
    (U : Cost.UniversalMachine) (S : MIPRE.CL.Sampler 7)
    {m T : Nat} (hT : m ≤ T)
    (cs : List (MIPRE.SAT.Clause3 (Fin m))) :
    (fixedIndexedVerifier U S).HasPerfectPCC
        (PNPAbove.WP28B.formulaIndex (PNPAbove.WP24.from3CNF cs)) T ↔
      ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  have hf : (PNPAbove.WP24.from3CNF cs).InputsLt m :=
    PNPAbove.WP24.from3CNF_inputs cs
  constructor
  · rintro ⟨S', _, hS⟩
    have hv : (fixedIndexedVerifier U S).valStar
       (PNPAbove.WP28B.formulaIndex (PNPAbove.WP24.from3CNF cs)) T = 1 :=
      (fixedIndexedVerifier U S).valStar_eq_one_of_hasPerfectPCC ⟨S', by assumption, hS⟩
    have hsat := (fixedIndexedVerifier_valStar_one_iff_sat U S
      (PNPAbove.WP24.from3CNF cs) m T hf hT).mp hv
    exact (PNPAbove.WP28B.indexedSAT_source_3CNF_iff cs).mp
      ((PNPAbove.WP28B.indexedSAT_formula_iff _ _).mpr hsat)
  · rintro ⟨w, hw⟩
    have hSAT : PNPAbove.WP24.Satisfiable m (PNPAbove.WP24.from3CNF cs) :=
      ⟨w, (PNPAbove.WP24.original_3CNF_sat_iff cs w).mp hw⟩
    exact fixedIndexedVerifier_HasPerfectPCC_of_sat U S
      (PNPAbove.WP24.from3CNF cs) m T hT hSAT

/-- IMPORTANT SOURCE SIZE ACCOUNTING: despite an encoding with
O(|f|) BITS, its numeric INDEX is at least 2 ^ |f|. A source
n^lambda bound therefore is not a polynomial bound in formula
DESCRIPTION length, and we never claim such a complexity transfer. -/
theorem formulaIndex_numeric_exponential_lower (f : MIPRE.SAT.Fml) :
    2 ^ (esize f) ≤ PNPAbove.WP28B.formulaIndex f := by
  apply Nat.lt_size.mp
  rw [PNPAbove.WP28B.formulaIndex_bit_length]
  omega

end PNPAbove.WP28B2
