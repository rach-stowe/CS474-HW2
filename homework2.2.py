# Problem 2
from z3 import *

p, q, r = Bools('p q r')

s = Solver()

# Original Formula
f1 = And(Or(q, Not(r)), Or(Not(p), r), Or(Not(q), r, p))
s.add(f1)
print("Original formula:", s.check())

# Resolved Formula
s.reset()
f2 = And(f1, Or(q, Not(p)), Or(Not(q), r))
s.add(f2)
print("Resolved formula:", s.check())

# Check if two formulas are eqivalent
s.reset()
s.add(f1==f2)
print("Checking formula equivalence:", s.check())

