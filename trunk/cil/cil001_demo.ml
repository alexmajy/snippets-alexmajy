open Cil
open Pretty

let getLogFunction logFuncName =
    let v = makeGlobalVar logFuncName
            (TFun(voidType,
                  Some [("msg", charConstPtrType, [])],
                  false,
                  [])
            )
    in
       v.vstorage <- Extern;
       v
;;

class insertWatchpoints host watchVar = object
    inherit nopCilVisitor

    method vfunc f =
        if f.svar.vname = host then DoChildren
        else SkipChildren

    method vinst i = match i with
    Set ((Var v, _), _, _)
    | Call (Some (Var v, _), _, _, _) when v.vname = watchVar ->
            ChangeTo [
                i;
                Call (None, Lval(var (getLogFunction "printf")) ,[mkString
                ("variable " ^ v.vname ^ " is set to: %d"); Lval(var v)], !currentLoc);
            ]
    | _ -> SkipChildren;
end



let mainFunction () =

    Cil.initCIL ();

    let cilFile = Frontc.parse "./foo.i" () in
    let wp = new insertWatchpoints "foo" "m_state" in
    visitCilFileSameGlobals wp cilFile;

    dumpFile !printerForMaincil stdout cilFile.fileName cilFile;
;;

mainFunction ();;
