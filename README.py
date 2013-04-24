code
====
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
