import sympy

symbols = sympy.symbols("x y")

true_list = [[0,1],[1,0]]
trfr = sympy.SOPform(symbols,true_list)


print(trfr)