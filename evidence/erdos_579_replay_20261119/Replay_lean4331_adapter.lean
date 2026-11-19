/-
Kernel replay of a bounty proof, for `lake env lean --run Replay.lean <SolutionModule> <ChallengeModule> <target>`.

1. Imports the solution module (all olean data, private level) and collects the transitive
   closure of constants that `<target>` depends on (types, values, whole mutual inductive blocks,
   their constructors and recursors).
2. Replays that closure, in dependency order, into an EMPTY kernel environment with
   `Lean.Kernel.Environment.replay`, so every declaration the proof rests on (Lean core, Mathlib,
   formal-conjectures and the submission) is re-checked by the kernel of the running toolchain.
3. Prints the axioms in the closure.
4. Imports the challenge module separately and checks that its `<target>` has the identical type
   and that every constant reachable from that type has an identical `ConstantInfo` in both
   environments (the statement and the definitions it uses were not changed by the submission).
-/
import Lean
import Lean.Replay
open Lean

/-- The transitive dependency closure of `root` in `env`. -/
partial def dependencyClosure (env : Environment) (roots : Array Name) (typesOnly : Bool := false) :
    IO (Std.HashMap Name ConstantInfo) := do
  let mut seen : Std.HashMap Name ConstantInfo := {}
  let mut todo : Array Name := roots
  while 0 < todo.size do
    let name := todo.back!
    todo := todo.pop
    if seen.contains name then continue
    let some info := env.find? name | throw <| IO.userError s!"missing constant {name}"
    seen := seen.insert name info
    let used := if typesOnly && !(info matches .defnInfo _) && !(info matches .inductInfo _)
      then info.type.getUsedConstantsAsSet else info.getUsedConstantsAsSet
    for other in used do
      unless seen.contains other do todo := todo.push other
    match info with
    | .inductInfo value =>
      for other in value.all do todo := todo.push other
      for other in value.ctors do todo := todo.push other
    | .ctorInfo value => todo := todo.push value.induct
    | .recInfo value => for other in value.all do todo := todo.push other
    | _ => pure ()
  return seen

def kindOf : ConstantInfo → String
  | .axiomInfo _ => "axiom" | .defnInfo _ => "def" | .thmInfo _ => "theorem"
  | .opaqueInfo _ => "opaque" | .quotInfo _ => "quot" | .inductInfo _ => "inductive"
  | .ctorInfo _ => "ctor" | .recInfo _ => "rec"

unsafe def main (args : List String) : IO UInt32 := do
  let [solutionModule, challengeModule, targetString] := args
    | IO.eprintln "usage: Replay SOLUTION_MODULE CHALLENGE_MODULE TARGET"; return 2
  let target := targetString.toName
  initSearchPath (← findSysroot)
  IO.println s!"lean_version: {Lean.versionString} ({Lean.githash})"
  let startImport ← IO.monoMsNow
  let solutionEnv ← importModules #[{ module := solutionModule.toName }] {} (trustLevel := 0)
  IO.println s!"imported {solutionModule} with {solutionEnv.constants.fold (fun n _ _ => n + 1) 0} constants in {(← IO.monoMsNow) - startImport} ms"
  let closure ← dependencyClosure solutionEnv #[target]
  let mut counts : Std.HashMap String Nat := {}
  for (_, info) in closure.toList do
    counts := counts.insert (kindOf info) (counts.getD (kindOf info) 0 + 1)
  IO.println s!"closure of {target}: {closure.size} constants {counts.toList}"
  let skipped := closure.toList.filter fun (_, info) => info.isUnsafe || info.isPartial
  IO.println s!"unsafe or partial constants in closure (not replayed by Environment.replay): {skipped.map (·.1)}"
  let axioms := (closure.toList.filterMap fun (name, info) =>
    if info matches .axiomInfo _ then some name else none).toArray.qsort Name.lt
  IO.println s!"axioms in closure: {axioms}"
  let empty ← mkEmptyEnvironment
  let startReplay ← IO.monoMsNow
  let replayed ← Lean.Environment.replay closure empty
  IO.println s!"kernel replay into an empty environment: OK in {(← IO.monoMsNow) - startReplay} ms"
  let some replayedTarget := replayed.toKernelEnv.find? target
    | IO.eprintln s!"target {target} missing after replay"; return 1
  let some solutionTarget := solutionEnv.find? target | return 1
  unless replayedTarget.type == solutionTarget.type do
    IO.eprintln "replayed target type differs from the imported one"; return 1
  let challengeEnv ← importModules #[{ module := challengeModule.toName }] {} (trustLevel := 0)
  let some challengeTarget := challengeEnv.find? target
    | IO.eprintln s!"challenge has no {target}"; return 1
  let typeMatches := challengeTarget.type == solutionTarget.type
  IO.println s!"challenge {target} type == solution {target} type: {typeMatches}"
  let statementClosure ← dependencyClosure challengeEnv
    (challengeTarget.type.getUsedConstantsAsSet.toArray) (typesOnly := true)
  let mut mismatches : Array Name := #[]
  for (name, info) in statementClosure.toList do
    match solutionEnv.find? name with
    | some other =>
      unless other.type == info.type && other.levelParams == info.levelParams &&
          (match info, other with
            | .defnInfo a, .defnInfo b => a.value == b.value
            | .inductInfo a, .inductInfo b => a.ctors == b.ctors && a.numParams == b.numParams
            | .ctorInfo a, .ctorInfo b => a.induct == b.induct
            | .thmInfo _, .thmInfo _ => true
            | .axiomInfo _, .axiomInfo _ => true
            | .opaqueInfo a, .opaqueInfo b => a.value == b.value
            | .recInfo a, .recInfo b => a.rules.length == b.rules.length
            | .quotInfo _, .quotInfo _ => true
            | _, _ => false) do
        mismatches := mismatches.push name
    | none => mismatches := mismatches.push name
  IO.println s!"statement closure: {statementClosure.size} constants, identical in challenge and solution: {mismatches.isEmpty} {mismatches}"
  let ok := typeMatches && mismatches.isEmpty
  IO.println s!"RESULT: {if ok then "PASS" else "FAIL"}"
  return if ok then 0 else 1
