from z3 import *

# Input arrays
len = Int("len")
arr0 = Int("arr0")
arr1 = Int("arr1")
arr2 = Int("arr2")
arr3 = Int("arr3")
arr4 = Int("arr4")
arr5 = Int("arr5")
arr6 = Int("arr6")
arr7 = Int("arr7")
arr8 = Int("arr8")
arr9 = Int("arr9")

# Results
res0 = Int("res0")
res1 = Int("res1")
res2 = Int("res2")
res3 = Int("res3")
res4 = Int("res4")
res5 = Int("res5")
res6 = Int("res6")
res7 = Int("res7")
res8 = Int("res8")
res9 = Int("res9")


p = Bool("p") # Program behaviour
s = Bool("s") # Program specification

solver = Solver()

# add pre-execution assumptions
#solver.add(And(len < 11, len > 0))
solver.add(len == 10)
solver.add(arr0 == 1)
solver.add(arr1 == 2)
solver.add(arr2 == 3)
solver.add(arr3 == 4)
solver.add(arr4 == 5)
solver.add(arr5 == 6)
solver.add(arr6 == 7)
solver.add(arr7 == 8)
solver.add(arr8 == 9)
solver.add(arr9 == 10)

p = And(
		res0 == arr0,
		res1 == res0+arr1,
	    res2 == res1+arr2,
		res3 == res2+arr3,
	    res4 == res3+arr4,
		res5 == res4+arr5,
		res6 == res5+arr6,
		res7 == res6+arr7,
		res8 == res7+arr8,
		res9 == res8+arr9
	   )

s = Or(
	    And(len == 1,res0 == len*(len+1)/2),
		And(len == 2, res1 == len*(len+1)/2),
		And(len == 3, res2 == len*(len+1)/2),
		And(len == 4, res3 == len*(len+1)/2),
		And(len == 5, res4 == len*(len+1)/2),
		And(len == 6, res5 == len*(len+1)/2),
		And(len == 7, res6 == len*(len+1)/2),
		And(len == 8, res7 == len*(len+1)/2),
		And(len == 9, res8 == len*(len+1)/2),
		And(len == 10, res9 == len*(len+1)/2)
	   )

# add BMC formulae
solver.add(And(p, Not(s)))

c = solver.check()
if c == unsat:
  print "Program is correct!"
elif c == unknown:
  print "Unable to check program!"
else:
  print solver.model()
  print "Program is incorrect!" 
