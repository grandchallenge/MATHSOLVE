import PNPAbove.WP28UniformExponentObstruction
import MIPRE.Foundations.Halting.Serial
import MIPRE.Foundations.OracularDecider
import MIPRE.Foundations.Cost.BinaryArithmetic

/-!
WP28B: a fixed, source-program-compatible SAT instance index. This
construction moves original source SAT.Fml data OUT of the verifier
program description into the binary source game index.
-/

namespace PNPAbove.WP28B
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

/-- A trailing true bit makes every finite LSB-first bitstring canonical.
The trailing bit is a purely syntactic sentinel, not part of the SAT data. -/
theorem bitsVal_suffix_true_bits (s : BitStr) :
    (bitsVal (s ++ [true])).bits = s ++ [true] := by
  induction s with
  | nil => simp [bitsVal]
  | cons b s ih =>
      have hn : bitsVal (s ++ [true]) ≠ 0 := by
        intro hz
        have hc := ih
        rw [hz, Nat.zero_bits] at hc
        simp at hc
      change (Nat.bit b (bitsVal (s ++ [true]))).bits = b :: (s ++ [true])
      rw [Nat.bits_append_bit _ b (by intro hz; exact False.elim (hn hz))]
      exact congrArg (List.cons b) ih

/-- The total instance index, a natural with a binary numeral of size
exactly one bit more than the postorder source tree. -/
def indexData (d : Data) : Nat :=
  bitsVal (d.toBitsPost ++ [true])

/-- Exact source numeral representation: the data payload is not truncated. -/
theorem indexData_bits (d : Data) :
    (indexData d).bits = d.toBitsPost ++ [true] := by
  exact bitsVal_suffix_true_bits d.toBitsPost

/-- Appending the sentinel preserves the parsed original data. The source
postorder parser ignores a stray true bit on a one-element stack. -/
theorem parse_postorder_with_sentinel (d : Data) :
    Data.parse (d.toBitsPost ++ [true]) = d := by
  have h := Data.stackRun_toBitsPost d [true] []
  simp only [Data.parse]
  rw [h]
  rfl

/-- Exact roundtrip for every original raw data tree, not just formulas. -/
theorem data_index_roundtrip (d : Data) :
    Data.parse (indexData d).bits = d := by
  rw [indexData_bits]
  exact parse_postorder_with_sentinel d

/-- The binary size of the source index is exactly the original source
data size plus one sentinel bit, not the enormous NUMERIC value. -/
theorem indexData_bit_length (d : Data) :
    Nat.size (indexData d) = d.size + 1 := by
  rw [← Nat.size_eq_bits_len, indexData_bits, List.length_append,
    Data.length_toBitsPost]
  simp

/-- Original proven executable source serializer with an explicit
quadratic original Cost.Prog runtime certificate. -/
noncomputable def serializeData :
    PolyTimeFun Data BitStr where
  toFun := Data.toBitsPost
  code := Cost.Prog.serProg
  closed := Cost.Prog.serProg_wellScoped
  timeBound := (3 * X + 2) * (16 * X + 42) + (X + 2) * (5 * X + 30)
  computes d := by
    obtain ⟨t, ht, hr⟩ := Cost.Prog.serProg_runs d
    exact ⟨t, by simpa [Polynomial.eval_add, Polynomial.eval_mul, Polynomial.eval_X,
      Polynomial.eval_C] using ht, hr⟩

/-- Native original MIPRE source machine producing a binary source SAT
index from data, using polynomial serializer/append/bitsValue code. -/
noncomputable def indexDataProgram : PolyTimeFun Data Nat :=
  bitsValue.comp (append.comp
    (serializeData.pair (PolyTimeFun.const ([true] : BitStr))))

theorem indexDataProgram_correct (d : Data) :
    indexDataProgram d = indexData d := rfl

/-- Original executable source decoder recovers the EXACT source tree
from a supplied binary index: no preselected formula is hardcoded. -/
noncomputable def decodeDataProgram : PolyTimeFun Nat Data :=
  MIPRE.OracleDecider.parseF.comp natBits

theorem decodeDataProgram_correct (n : Nat) :
    decodeDataProgram n = Data.parse n.bits := rfl

/-- No SAT instance is embedded in the code of either fixed source
original machine; both programs are the same for every formula. -/
theorem source_index_program_roundtrip (d : Data) :
    decodeDataProgram (indexDataProgram d) = d := by
  rw [indexDataProgram_correct, decodeDataProgram_correct, data_index_roundtrip]

/-- The original Fml encoder is also the identity source program
because a source formula is its own original RPN data encoding. -/
noncomputable def originalFormulaData : PolyTimeFun MIPRE.SAT.Fml Data :=
  PolyTimeFun.ofEncodeEq (encode : MIPRE.SAT.Fml → Data) (fun _ => rfl)

/-- ONE fixed Cost.Prog for the formula-to-index mapping, valid for
arbitrary source formula sizes and arbitrary variable counts. -/
noncomputable def formulaIndexProgram :
    PolyTimeFun MIPRE.SAT.Fml Nat :=
  indexDataProgram.comp originalFormulaData

def formulaIndex (f : MIPRE.SAT.Fml) : Nat :=
  indexData (encode f)

/-- No code changes with f: the same source compiler program
produces its original binary index for every SAT instance. -/
theorem formulaIndexProgram_correct (f : MIPRE.SAT.Fml) :
    formulaIndexProgram f = formulaIndex f := rfl

/-- Strong original-source data roundtrip. The recovered tree is the
actual original encoded formula, without SAT semantics assumptions. -/
theorem formulaIndex_decode (f : MIPRE.SAT.Fml) :
    decodeDataProgram (formulaIndexProgram f) = encode f := by
  rw [formulaIndexProgram_correct]
  change Data.parse (indexData (encode f)).bits = encode f
  exact data_index_roundtrip (encode f)

/-- SAT formulas of size s map to binary indices using exactly s+1 bits. -/
theorem formulaIndex_bit_length (f : MIPRE.SAT.Fml) :
    Nat.size (formulaIndex f) = esize f + 1 :=
  indexData_bit_length (encode f)

/-- The exact original input-to-index map is injective: different
SAT instances never become the same game index. -/
theorem formulaIndex_injective : Function.Injective formulaIndex := by
  intro f g heq
  apply encode_injective
  have h := congrArg (fun n : Nat => Data.parse n.bits) heq
  simpa [formulaIndex, data_index_roundtrip] using h

/-- Exact mathematical SAT assertion for an encoded binary game index.
This is a source-index predicate, NOT YET a source-normal-form Decider. -/
def IndexedSAT (m n : Nat) : Prop :=
  ∃ f : MIPRE.SAT.Fml,
    decodeDataProgram n = encode f ∧ PNPAbove.WP24.Satisfiable m f

/-- The binary index names exactly the supplied original SAT formula.
No other SAT instance can masquerade as this source index. -/
theorem indexedSAT_formula_iff (f : MIPRE.SAT.Fml) (m : Nat) :
    IndexedSAT m (formulaIndex f) ↔ PNPAbove.WP24.Satisfiable m f := by
  constructor
  · rintro ⟨g, henc, hg⟩
    have hd := formulaIndex_decode f
    rw [formulaIndexProgram_correct] at hd
    have hfg : f = g := encode_injective (hd.symm.trans henc)
    subst g
    exact hg
  · intro hf
    exact ⟨f, by simpa [formulaIndexProgram_correct] using formulaIndex_decode f, hf⟩

/-- Original finite 3CNF SAT is preserved EXACTLY through the binary
instance index, using the original source 3CNF semantic bridge. -/
theorem indexedSAT_source_3CNF_iff {m : Nat}
    (cs : List (MIPRE.SAT.Clause3 (Fin m))) :
    IndexedSAT m (formulaIndex (PNPAbove.WP24.from3CNF cs)) ↔
      ∃ w : Fin m → Bool, (PNPAbove.WP24.threeCNFSet cs).Sat w := by
  rw [indexedSAT_formula_iff]
  simpa [PNPAbove.WP24.Satisfiable] using
    (exists_congr (fun w =>
      (PNPAbove.WP24.original_3CNF_sat_iff cs w).symm))

/-- The source binary numeral occupies at most a LINEAR number of
original source encoding nodes (with a constant factor from Bool). -/
theorem formulaIndex_source_esize_le (f : MIPRE.SAT.Fml) :
    esize (formulaIndex f) ≤ 4 * (esize f + 1) + 1 := by
  have h := esize_nat_le (formulaIndex f)
  rw [formulaIndex_bit_length] at h
  exact h

/-- The source index constructor has a REAL ORIGINAL polynomial time
certificate for every formula, beyond a normal Lean runtime assertion. -/
theorem formulaIndex_source_polytime (f : MIPRE.SAT.Fml) :
    ∃ t ≤ formulaIndexProgram.timeBound.eval (esize f),
      formulaIndexProgram.code.Runs
        (encode f) (encode (formulaIndexProgram f)) t :=
  formulaIndexProgram.computes f

/-- The source decoder similarly has an executable original polynomial
time certificate on arbitrary natural index values. -/
theorem indexDecoder_source_polytime (n : Nat) :
    ∃ t ≤ decodeDataProgram.timeBound.eval (esize n),
      decodeDataProgram.code.Runs (encode n)
        (encode (decodeDataProgram n)) t :=
  decodeDataProgram.computes n

end PNPAbove.WP28B
