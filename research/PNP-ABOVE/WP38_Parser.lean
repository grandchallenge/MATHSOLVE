import PNPAbove.WP38Greedy

namespace PNPAbove.WP38
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun
open Polynomial

abbrev Stack := List Fml


noncomputable def binTailP (op : PolyTimeFun (Fml × Fml) Fml) :
    PolyTimeFun (Fml × Stack) Stack :=
  casesList
    ((PolyTimeFun.id Fml).cons (PolyTimeFun.const ([] : Stack)))
    ((op.comp ((fst.comp snd).pair fst)).cons (snd.comp snd))

noncomputable def binStackP (op : PolyTimeFun (Fml × Fml) Fml) : PolyTimeFun Stack Stack :=
  (casesList (PolyTimeFun.const ([] : Stack)) ((binTailP op).comp snd)).comp
    ((PolyTimeFun.const ()).pair (PolyTimeFun.id Stack))

noncomputable def notStackP : PolyTimeFun Stack Stack :=
  (casesList (PolyTimeFun.const ([] : Stack))
    ((Fml.notF.comp (fst.comp snd)).cons (snd.comp snd))).comp
    ((PolyTimeFun.const ()).pair (PolyTimeFun.id Stack))

noncomputable def parseStepP : PolyTimeFun (Stack × Fml.Node) Stack :=
  SAT.PolyTimeFun.casesNode
    ((Fml.inpF.comp snd).cons fst)
    ((Fml.constF.comp snd).cons fst)
    (binStackP Fml.andF) (binStackP Fml.orF) notStackP

theorem parseStepP_correct (s : Stack) (nd : Fml.Node) :
    parseStepP (s,nd) = Fml.parseStep s nd := by
  cases nd with
  | inp i => rfl
  | const b => rfl
  | and =>
    cases s with
    | nil => rfl
    | cons g rest => cases rest <;> rfl
  | or =>
    cases s with
    | nil => rfl
    | cons g rest => cases rest <;> rfl
  | not => cases s <;> rfl

theorem parseStep_growth (s : Stack) (nd : Fml.Node) :
    esize (parseStepP (s,nd)) ≤ esize s + (X+C 12 : Polynomial Nat).eval (esize nd) := by
  rw [parseStepP_correct]
  simp only [Polynomial.eval_add,Polynomial.eval_X,Polynomial.eval_C]
  cases nd with
  | inp i =>
    simp only [Fml.parseStep,esize_list_cons,inp_size,esize_node_inp]
    omega
  | const b =>
    simp only [Fml.parseStep,esize_list_cons,esize_node_const]
    have h := esize_constFml_le b
    omega
  | and =>
    cases s with
    | nil => simp [Fml.parseStep]
    | cons g rest =>
      cases rest with
      | nil => simp [Fml.parseStep]
      | cons f tail =>
        simp only [Fml.parseStep,esize_list_cons,esize_and_fml]
        omega
  | or =>
    cases s with
    | nil => simp [Fml.parseStep]
    | cons g rest =>
      cases rest with
      | nil => simp [Fml.parseStep]
      | cons f tail =>
        simp only [Fml.parseStep,esize_list_cons,esize_or_fml]
        omega
  | not =>
    cases s with
    | nil => simp [Fml.parseStep]
    | cons f rest =>
      simp only [Fml.parseStep,esize_list_cons,esize_not_fml]
      omega

noncomputable def parseStackP : PolyTimeFun (List Fml.Node) Stack :=
  (foldlAdd parseStepP (X+C 12) parseStep_growth).comp
    ((PolyTimeFun.id (List Fml.Node)).pair (PolyTimeFun.const ([] : Stack)))

noncomputable def topP : PolyTimeFun Stack Fml :=
  (casesList (PolyTimeFun.const (.const false : Fml)) (fst.comp snd)).comp
    ((PolyTimeFun.const ()).pair (PolyTimeFun.id Stack))

noncomputable def parseNodesP : PolyTimeFun (List Fml.Node) Fml :=
  topP.comp parseStackP

theorem parseStackP_correct (xs : List Fml.Node) :
    parseStackP xs = xs.foldl Fml.parseStep [] := by
  change foldlAdd parseStepP (X+C 12) parseStep_growth (xs,[]) = _
  simp only [foldlAdd_apply,parseStepP_correct]

theorem parseNodesP_rpn (f : Fml) : parseNodesP f.rpn = f := by
  change topP (parseStackP f.rpn) = f
  rw [parseStackP_correct]
  have h := Fml.foldl_parseStep_rpn f [] []
  simp only [List.append_nil,List.foldl_nil] at h
  rw [h]
  rfl

end PNPAbove.WP38
