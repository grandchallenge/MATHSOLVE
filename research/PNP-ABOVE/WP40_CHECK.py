#!/usr/bin/env python3
"""Finite independent checks of witness-tag syntax, semantics, and support order.
Not an asymptotic lower-bound test or a substitute for the Lean replay."""
from itertools import product

def payload(bits):
    out = ("not", ("const", True))
    for b in reversed(bits):
        out = ("and", ("const", b), out)
    return out

def tag(f, bits):
    return ("and", ("or", payload(bits), ("const", True)), f)

def evaluate(f, a):
    op = f[0]
    if op == "const": return f[1]
    if op == "inp": return a[f[1]]
    if op == "not": return not evaluate(f[1], a)
    if op == "and": return evaluate(f[1], a) and evaluate(f[2], a)
    if op == "or": return evaluate(f[1], a) or evaluate(f[2], a)
    raise ValueError(op)

def rpn(f):
    if f[0] in ("const", "inp"): return [f]
    if f[0] == "not": return rpn(f[1]) + [("not",)]
    return rpn(f[1]) + rpn(f[2]) + [(f[0],)]

def support(f):
    xs = []
    for nd in rpn(f):
        if nd[0] == "inp" and nd[1] not in xs:
            xs.insert(0, nd[1])
    return xs

def read(f):
    out = []
    for nd in rpn(f):
        if nd[0] != "const": break
        out.append(nd[1])
    return tuple(out[:-1])

def check():
    leaves = [("const",False),("const",True),("inp",0),("inp",1),("inp",2)]
    level = leaves + [("not",f) for f in leaves] + [
        (op,f,g) for op in ("and","or") for f,g in product(leaves,repeat=2)]
    formulas = level + [("not",f) for f in level] + [
        (op,f,g) for op in ("and","or") for f,g in product(level,repeat=2)]
    tags = [bits for n in range(4) for bits in product((False,True),repeat=n)]
    count = 0
    for f in formulas:
        sf = support(f)
        for bits in tags:
            g = tag(f,bits)
            if read(g) != bits or support(g) != sf:
                raise AssertionError((f,bits,g))
            for a in product((False,True),repeat=3):
                if evaluate(g,a) != evaluate(f,a):
                    raise AssertionError((f,bits,a))
            count += 1
    print(f"WP40 finite syntax, ordered support and truth-function checks: {count} formula/payload pairs")
if __name__ == "__main__":
    check()
