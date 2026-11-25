import PNPAbove.WP28BIndex
import MIPRE.Foundations.CL.DetypingProgParse
import MIPRE.Foundations.SAT.Formula

/-!
First stage of a FIXED-code source indexed-SAT decider: decode every
arbitrary original raw Data into a total original SAT.Node list, with
an original Cost.PolyTimeFun and verified agreement on encoded formulas.
-/

namespace PNPAbove.WP28B2
open MIPRE MIPRE.Cost MIPRE.Cost.PolyTimeFun
open MIPRE.CL.Detyping.Program

/-- Compare the original source unary Node tag with a constant, on
every raw original Data input. -/
noncomputable def nodeTagIs (tag : Nat) : PolyTimeFun Data Bool :=
  MIPRE.OracleDecider.eqD treeHead (PolyTimeFun.const (Data.ofNat tag))

/-- Construct an ORIGINAL source node from an arbitrary input datum;
all malformed tags select a harmless fixed NOT instruction. -/
noncomputable def readNode : PolyTimeFun Data MIPRE.SAT.Fml.Node :=
  let payload := treeTail
  let inputNode : PolyTimeFun Data MIPRE.SAT.Fml.Node :=
    (PolyTimeFun.tagged 0 MIPRE.SAT.Fml.Node.inp MIPRE.SAT.Fml.Node.encode_inp).comp
      (readNat.comp payload)
  let boolNode : PolyTimeFun Data MIPRE.SAT.Fml.Node :=
    (PolyTimeFun.tagged 1 MIPRE.SAT.Fml.Node.const MIPRE.SAT.Fml.Node.encode_const).comp
      (rawTruthProg.comp payload)
  PolyTimeFun.ite (nodeTagIs 0) inputNode
    (PolyTimeFun.ite (nodeTagIs 1) boolNode
      (PolyTimeFun.ite (nodeTagIs 2)
        (PolyTimeFun.const MIPRE.SAT.Fml.Node.and)
        (PolyTimeFun.ite (nodeTagIs 3)
          (PolyTimeFun.const MIPRE.SAT.Fml.Node.or)
          (PolyTimeFun.const MIPRE.SAT.Fml.Node.not))))

/-- Any valid ORIGINAL source node survives the total polynomial source
node reader, across all 5 constructors and arbitrary binary indices. -/
theorem readNode_encode (nd : MIPRE.SAT.Fml.Node) :
    readNode (encode nd) = nd := by
  cases nd with
  | inp i =>
      simp [readNode, nodeTagIs, MIPRE.OracleDecider.eqD,
        MIPRE.SAT.Fml.Node.encode_inp, readNat_encode, Data.ofNat]
  | const b =>
      cases b <;>
        simp [readNode, nodeTagIs, MIPRE.OracleDecider.eqD,
          MIPRE.SAT.Fml.Node.encode_const, Data.ofNat, rawTruthProg,
          MIPRE.CL.Detyping.Program.rawTruth, rawTruthProg_encode_bool]
  | and =>
      simp [readNode, nodeTagIs, MIPRE.OracleDecider.eqD,
        MIPRE.SAT.Fml.Node.encode_and, Data.ofNat]
  | or =>
      simp [readNode, nodeTagIs, MIPRE.OracleDecider.eqD,
        MIPRE.SAT.Fml.Node.encode_or, Data.ofNat]
  | not =>
      simp [readNode, nodeTagIs, MIPRE.OracleDecider.eqD,
        MIPRE.SAT.Fml.Node.encode_not, Data.ofNat]

/-- Original MIPRE data tree, regarded as a list of raw node encodings;
this source program is the identity on its exact source encoding. -/
noncomputable def rawDataList : PolyTimeFun Data (List Data) :=
  PolyTimeFun.ofEncodeEq rawList encode_rawList

/-- Total, original-source polynomial decoding for ANY raw original Data,
not only valid source formula lists. -/
noncomputable def decodeNodeList : PolyTimeFun Data (List MIPRE.SAT.Fml.Node) :=
  (PolyTimeFun.map readNode).comp rawDataList

/-- Right-spine decoding of an original list is exact. -/
theorem rawList_encode_nodes (nodes : List MIPRE.SAT.Fml.Node) :
    rawList (encode nodes) = nodes.map encode := by
  induction nodes with
  | nil => rfl
  | cons node nodes ih =>
      simpa only [encode_list_cons, rawList, List.map_cons] using
        congrArg (List.cons (encode node)) ih

/-- The actual executable source PTF decoder returns the source
postfix serialization of ANY original Boolean formula f. -/
theorem decodeNodeList_formula (f : MIPRE.SAT.Fml) :
    decodeNodeList (encode f) = f.rpn := by
  change (rawList (encode f)).map readNode = f.rpn
  rw [MIPRE.SAT.Fml.encode_fml, rawList_encode_nodes]
  simp only [List.map_map]
  change (f.rpn.map (fun nd => readNode (encode nd))) = f.rpn
  simp [readNode_encode]

/-- A SINGLE fixed original source program computes the full list of
node instructions from the binary instance index. -/
noncomputable def indexNodeProgram :
    PolyTimeFun Nat (List MIPRE.SAT.Fml.Node) :=
  decodeNodeList.comp PNPAbove.WP28B.decodeDataProgram

/-- The original source PTF node reader identifies precisely the
source program nodes at the binary index of every SAT formula. -/
theorem indexNodeProgram_formula (f : MIPRE.SAT.Fml) :
    indexNodeProgram (PNPAbove.WP28B.formulaIndex f) = f.rpn := by
  change decodeNodeList
    (PNPAbove.WP28B.decodeDataProgram (PNPAbove.WP28B.formulaIndex f)) = _
  rw [show PNPAbove.WP28B.decodeDataProgram (PNPAbove.WP28B.formulaIndex f) =
      encode f by
    simpa only [PNPAbove.WP28B.formulaIndexProgram_correct] using
      PNPAbove.WP28B.formulaIndex_decode f]
  exact decodeNodeList_formula f

end PNPAbove.WP28B2
