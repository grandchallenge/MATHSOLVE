import MIPRE.Foundations.SAT.FmlProg
import MIPRE.Foundations.Cost.BinaryCompare

namespace PNPAbove.WP40
open MIPRE MIPRE.SAT MIPRE.Cost MIPRE.Cost.PolyTimeFun Polynomial

/-- Constant-only payload. The initial run of constant nodes encodes the
bits followed by a delimiter constant; the next node is always negation. -/
def payload : BitStr → Fml
  | [] => .not (.const true)
  | b::bs => .and (.const b) (payload bs)

def tag (f : Fml) (bs : BitStr) : Fml :=
  .and (.or (payload bs) (.const true)) f

theorem tag_eval (f : Fml) (bs : BitStr) (a : Nat → Bool) :
    (tag f bs).eval a = f.eval a := by
  simp [tag,Fml.eval]

theorem payload_prefix (bs : BitStr) :
    ∃ tail : List Fml.Node,
      (payload bs).rpn = bs.map Fml.Node.const ++ [.const true,.not] ++ tail := by
  induction bs with
  | nil => exact ⟨[],rfl⟩
  | cons b bs ih =>
    obtain ⟨tail,ht⟩ := ih
    refine ⟨tail ++ [.and],?_⟩
    simp [payload,Fml.rpn,ht,List.append_assoc]

theorem tag_prefix (f : Fml) (bs : BitStr) :
    ∃ tail : List Fml.Node,
      (tag f bs).rpn = bs.map Fml.Node.const ++ [.const true,.not] ++ tail := by
  obtain ⟨tail,ht⟩ := payload_prefix bs
  refine ⟨tail ++ [.const true,.or] ++ f.rpn ++ [.and],?_⟩
  simp [tag,Fml.rpn,ht,List.append_assoc]

theorem payload_esize (bs : BitStr) :
    esize (payload bs) ≤ 16*bs.length+21 := by
  induction bs with
  | nil =>
    change esize (Fml.not (.const true)) ≤ 21
    rw [esize_not_fml]
    have h := esize_constFml_le true
    omega
  | cons b bs ih =>
    rw [payload,esize_and_fml,List.length_cons]
    have h := esize_constFml_le b
    omega

theorem tag_esize (f : Fml) (bs : BitStr) :
    esize (tag f bs) ≤ esize f + 16*bs.length+46 := by
  unfold tag
  rw [esize_and_fml,esize_or_fml]
  have h := payload_esize bs
  have hc := esize_constFml_le true
  omega

theorem tag_short (f : Fml) (bs : BitStr) (hb : bs.length ≤ esize f) :
    esize (tag f bs) ≤ 17*esize f+46 := by
  have h := tag_esize f bs
  omega

abbrev ScanState := Bool × BitStr

def scanStep (s : ScanState) (nd : Fml.Node) : ScanState :=
  match nd with
  | .const b => if s.1 then (true,b::s.2) else s
  | _ => (false,s.2)

theorem scan_frozen (ns : List Fml.Node) (bs : BitStr) :
    ns.foldl scanStep (false,bs) = (false,bs) := by
  induction ns with
  | nil => rfl
  | cons nd ns ih =>
    rw [List.foldl_cons]
    have h : scanStep (false,bs) nd = (false,bs) := by cases nd <;> rfl
    rw [h,ih]

theorem scan_constants (bs acc : BitStr) :
    (bs.map Fml.Node.const).foldl scanStep (true,acc) = (true,bs.reverse ++ acc) := by
  induction bs generalizing acc with
  | nil => rfl
  | cons b bs ih =>
    simp only [List.map_cons,List.foldl_cons,scanStep,ite_true]
    rw [ih]
    simp [List.reverse_cons,List.append_assoc]

def scan (ns : List Fml.Node) : BitStr :=
  (ns.foldl scanStep (true,[])).2.tail.reverse

theorem scan_tag (f : Fml) (bs : BitStr) :
    scan (tag f bs).rpn = bs := by
  obtain ⟨tail,ht⟩ := tag_prefix f bs
  rw [scan,ht,List.foldl_append,List.foldl_append,scan_constants]
  simp [scanStep,scan_frozen]

noncomputable def stopP : PolyTimeFun ScanState ScanState :=
  (PolyTimeFun.const false).pair snd

noncomputable def constStepP : PolyTimeFun (ScanState × Bool) ScanState :=
  PolyTimeFun.ite (fst.comp fst)
    ((PolyTimeFun.const true).pair (snd.cons (snd.comp fst))) fst

noncomputable def scanStepP : PolyTimeFun (ScanState × Fml.Node) ScanState :=
  SAT.PolyTimeFun.casesNode (stopP.comp fst) constStepP stopP stopP stopP

theorem scanStepP_correct (s : ScanState) (nd : Fml.Node) :
    scanStepP (s,nd) = scanStep s nd := by
  cases nd <;> rfl

theorem scanStepP_growth (s : ScanState) (nd : Fml.Node) :
    esize (scanStepP (s,nd)) ≤ esize s + (C 7 : Polynomial Nat).eval (esize nd) := by
  rw [scanStepP_correct,Polynomial.eval_C]
  rcases s with ⟨active,bs⟩
  cases nd <;> cases active <;> simp [scanStep,esize_prod,esize_list_cons] <;>
    first | decide | (have h := esize_bool_le ‹Bool›; omega) | omega

noncomputable def tailP : PolyTimeFun BitStr BitStr :=
  (casesList (PolyTimeFun.const ([] : BitStr)) (snd.comp snd)).comp
    ((PolyTimeFun.const ()).pair (PolyTimeFun.id BitStr))

theorem tailP_correct (bs : BitStr) : tailP bs = bs.tail := by
  cases bs <;> rfl

noncomputable def scanP : PolyTimeFun (List Fml.Node) BitStr :=
  (PolyTimeFun.reverse.comp (tailP.comp snd)).comp
    ((foldlAdd scanStepP (C 7) scanStepP_growth).comp
      ((PolyTimeFun.id (List Fml.Node)).pair (PolyTimeFun.const (true,([] : BitStr)))))

theorem scanP_correct (ns : List Fml.Node) : scanP ns = scan ns := by
  change (tailP (foldlAdd scanStepP (C 7) scanStepP_growth (ns,(true,[]))).2).reverse = _
  simp only [tailP_correct,foldlAdd_apply,scanStepP_correct,scan]

noncomputable def readP : PolyTimeFun Fml BitStr := scanP.comp Fml.rpnF

theorem readP_tag (f : Fml) (bs : BitStr) : readP (tag f bs) = bs := by
  change scanP (tag f bs).rpn = bs
  rw [scanP_correct,scan_tag]

theorem readP_runs (f : Fml) :
    ∃ t ≤ readP.timeBound.eval (esize f),
      readP.code.Runs (encode f) (encode (readP f)) t :=
  readP.computes f

noncomputable def payloadStepP : PolyTimeFun (Fml × Bool) Fml :=
  Fml.andF.comp ((Fml.constF.comp snd).pair fst)

theorem payloadStep_growth (f : Fml) (b : Bool) :
    esize (payloadStepP (f,b)) ≤ esize f + (C 16 : Polynomial Nat).eval (esize b) := by
  change esize (Fml.and (.const b) f) ≤ _
  rw [esize_and_fml,Polynomial.eval_C]
  have h := esize_constFml_le b
  omega

noncomputable def payloadP : PolyTimeFun BitStr Fml :=
  (foldlAdd payloadStepP (C 16) payloadStep_growth).comp
    (PolyTimeFun.reverse.pair (PolyTimeFun.const (Fml.not (.const true))))

theorem payloadP_correct (bs : BitStr) : payloadP bs = payload bs := by
  change foldlAdd payloadStepP (C 16) payloadStep_growth
    (bs.reverse,Fml.not (.const true)) = _
  rw [foldlAdd_apply,List.foldl_reverse]
  induction bs with
  | nil => rfl
  | cons b bs ih =>
    simp only [List.foldr_cons,payload]
    change Fml.and (.const b) _ = _
    rw [ih]
    rfl

noncomputable def tagP : PolyTimeFun (Fml × BitStr) Fml :=
  Fml.andF.comp ((Fml.orF.comp ((payloadP.comp snd).pair (PolyTimeFun.const (Fml.const true)))).pair fst)

theorem tagP_correct (f : Fml) (bs : BitStr) : tagP (f,bs) = tag f bs := by
  change Fml.and (Fml.or (payloadP bs) (.const true)) f = _
  rw [payloadP_correct]
  rfl

end PNPAbove.WP40
