import PNPAbove.WP38Lex
import PNPAbove.WP38Parser
import PNPAbove.WP35Dense

namespace PNPAbove.WP38
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun

noncomputable def denseSearchP (D : PolyTimeFun Data Bool) : PolyTimeFun Fml BitStr :=
  (searchP D).comp (WP35.supportProgram.pair (PolyTimeFun.id Fml))

theorem denseSearchP_correct (D : PolyTimeFun Data Bool) (f : Fml) :
    denseSearchP D f = searchP D (WP35.support f,f) := by
  change searchP D (WP35.supportProgram f,f) = _
  rw [WP35.supportProgram_correct]

theorem denseSearch_length (D : PolyTimeFun Data Bool) (f : Fml) :
    (denseSearchP D f).length = (WP35.support f).length := by
  rw [denseSearchP_correct,search_length]

theorem denseSearch_canonical (D : PolyTimeFun Data Bool) (hD : Correct D)
    (f : Fml) (hf : Sat f) :
    CanonicalWitness (WP35.support f) f (denseSearchP D f) := by
  rw [denseSearchP_correct]
  exact search_canonical D hD _ _ hf

/-- The support-order bit string of any satisfying assignment is accepted by
the existing source witness verifier. No assignment expansion is required. -/
theorem model_bits_verified (f : Fml) (a : Nat → Bool) (ha : f.eval a = true) :
    WP35.denseWitnessVerifier (f,(WP35.support f).map a) = true := by
  rw [WP35.denseWitnessVerifier_correct,WP35.dense,Fml.eval_rename]
  have he := WP35.eval_congr_support f
    ((fun i => ((WP35.support f).map a).getD i false) ∘
      (fun i => (WP35.support f).idxOf i)) a (fun i hi => by
        have hj := WP35.rank_active_lt f i hi
        simp only [Function.comp_apply]
        rw [List.getD_eq_getElem _ _ (by simpa using hj),List.getElem_map,
          List.getElem_idxOf hj])
  rwa [he]

theorem canonical_verified (f : Fml) (bs : BitStr)
    (h : CanonicalWitness (WP35.support f) f bs) :
    WP35.denseWitnessVerifier (f,bs) = true := by
  obtain ⟨a,ha,he⟩ := h.1
  rw [he]
  exact model_bits_verified f a ha

/-- Only YES inputs require successful witness generation. On NO inputs
the total program may return arbitrary bits. -/
def SolvesWitness (S : PolyTimeFun Fml BitStr) : Prop :=
  ∀ f, Sat f → WP35.denseWitnessVerifier (f,S f) = true

def SolvesCanonical (S : PolyTimeFun Fml BitStr) : Prop :=
  ∀ f, Sat f → CanonicalWitness (WP35.support f) f (S f)

theorem canonical_implies_witness (S : PolyTimeFun Fml BitStr) (hS : SolvesCanonical S) :
    SolvesWitness S :=
  fun f hf => canonical_verified f (S f) (hS f hf)

theorem denseSearch_solvesCanonical (D : PolyTimeFun Data Bool) (hD : Correct D) :
    SolvesCanonical (denseSearchP D) :=
  fun f hf => denseSearch_canonical D hD f hf

/-- Native total decoder: arbitrary raw data is mapped to some formula;
valid encoded formulas are recovered exactly. -/
noncomputable def decodeFmlP : PolyTimeFun Data Fml :=
  parseNodesP.comp WP28B2.decodeNodeList

theorem decodeFmlP_encode (f : Fml) :
    decodeFmlP (encode f) = f := by
  change parseNodesP (WP28B2.decodeNodeList (encode f)) = f
  rw [WP28B2.decodeNodeList_formula,parseNodesP_rpn]

noncomputable def witnessDecisionP (S : PolyTimeFun Fml BitStr) : PolyTimeFun Data Bool :=
  (WP35.denseWitnessVerifier.comp ((PolyTimeFun.id Fml).pair S)).comp decodeFmlP

theorem witnessDecisionP_correct (S : PolyTimeFun Fml BitStr) (hS : SolvesWitness S) :
    Correct (witnessDecisionP S) := by
  intro f
  change WP35.denseWitnessVerifier (decodeFmlP (encode f),S (decodeFmlP (encode f))) = true ↔ _
  rw [decodeFmlP_encode]
  exact ⟨WP35.denseWitnessVerifier_sound f (S f),hS f⟩

theorem native_decision_iff_witness :
    (∃ D : PolyTimeFun Data Bool, Correct D) ↔
      ∃ S : PolyTimeFun Fml BitStr, SolvesWitness S := by
  constructor
  · rintro ⟨D,hD⟩
    exact ⟨denseSearchP D,canonical_implies_witness _ (denseSearch_solvesCanonical D hD)⟩
  · rintro ⟨S,hS⟩
    exact ⟨witnessDecisionP S,witnessDecisionP_correct S hS⟩

theorem native_witness_iff_canonical :
    (∃ S : PolyTimeFun Fml BitStr, SolvesWitness S) ↔
      ∃ S : PolyTimeFun Fml BitStr, SolvesCanonical S := by
  constructor
  · rintro ⟨S,hS⟩
    exact ⟨denseSearchP (witnessDecisionP S),denseSearch_solvesCanonical _ (witnessDecisionP_correct S hS)⟩
  · rintro ⟨S,hS⟩
    exact ⟨S,canonical_implies_witness S hS⟩

theorem valid_promise_iff_witness
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (∃ oracle : PolyTimeFun Nat Bool, WP34.SolvesValidPromise G U lam oracle) ↔
      ∃ S : PolyTimeFun Fml BitStr, SolvesWitness S :=
  (WP34.valid_promise_polytime_iff_formula_SAT G U lam hB).trans native_decision_iff_witness

theorem valid_promise_iff_canonical
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (∃ oracle : PolyTimeFun Nat Bool, WP34.SolvesValidPromise G U lam oracle) ↔
      ∃ S : PolyTimeFun Fml BitStr, SolvesCanonical S :=
  (valid_promise_iff_witness G U lam hB).trans native_witness_iff_canonical

theorem valid_promise_lower_iff_witness_lower
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (¬ ∃ oracle : PolyTimeFun Nat Bool, WP34.SolvesValidPromise G U lam oracle) ↔
      ¬ ∃ S : PolyTimeFun Fml BitStr, SolvesWitness S :=
  not_congr (valid_promise_iff_witness G U lam hB)

theorem valid_promise_lower_iff_canonical_lower
    (G : GapCompression) (U : UniversalMachine) (lam : Nat)
    (hB : (WP28C.powerIndexedVerifier U (G.sampler 0)).IsBounded lam) :
    (¬ ∃ oracle : PolyTimeFun Nat Bool, WP34.SolvesValidPromise G U lam oracle) ↔
      ¬ ∃ S : PolyTimeFun Fml BitStr, SolvesCanonical S :=
  not_congr (valid_promise_iff_canonical G U lam hB)

end PNPAbove.WP38
