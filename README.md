%time
cython("""
def f(a,b):
  c = (a**2+b**2)**0.5
  sinb = b/c
  cosb = a/c
  tanb = a/c
  cosa = sinb
  sina = cosb  
  tana = 1/tanb
  print("This program is working for Trig functions given by 2 sides a and b")  
  print("The sin, cos and tan of alpha bounded by side b and c, in order, is")
  print(sinb, cosb, tanb)
  print("The sin, cos and tan of Beta bounded by side a and c, in order, is")
  print(sina, cosa, tana)
""")

make the code faster by deleting "tana = 1/tanb", "cosa = sinb", "sina = cosb" and "sina, cosa," on the buttom, then 
replacing "tana" in the last line by "1/tanb" 

save time from "CPU time: 0.10 s,  Wall time: 1.68 s" for previous to "CPU time: 0.09 s,  Wall time: 1.59 s" after editing
