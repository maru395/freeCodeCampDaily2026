import math

def is_integer_hypotenuse(a ,b):
  c = math.sqrt((a*a)+(b*b))
  return c.is_integer()
