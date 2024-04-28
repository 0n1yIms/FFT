from sympy import *
import numpy as np

x = symbols('x')

e = 2.7

fun = e**(-x**2)


i = integrate(fun, (x, 0, 10)).evalf()
print(i)
pprint(i)

