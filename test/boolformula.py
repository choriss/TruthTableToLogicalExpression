import sympy

x,y = sympy.symbols("x y")

true_list = [[0,1],[1,0]]
trfr = sympy.SOPform([x,y],true_list)

print(trfr)