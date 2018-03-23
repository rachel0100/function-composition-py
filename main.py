from functools import reduce

def function_composition(x):
  return lambda z: reduce(lambda w,y: y(w), x, z)
  
function_list = [ lambda x: x+3, lambda x: x**2 ]

h = function_composition(function_list)
print(h(4))
