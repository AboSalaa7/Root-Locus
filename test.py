import control as co
import math
import cmath
from sympy import *
from matplotlib import pyplot as plt

def fEquation(roots):
    x=symbols('x')
    whole =1
    if len(roots)==0:
        return 0
    for root in roots:
        whole*=(x-root)
    return whole.expand()

pole1= complex(0,0)
pole2 = complex(-25,0)
pole3 = complex(-50,10)
pole4 = complex(-50,-10)
print(pole3.real)
roots = [pole1,pole2,pole3,pole4]
denominator = fEquation(roots)
k = symbols('k')
equation = 1/denominator

diffEquation = diff(equation)
breakAwayPoints=solve(diffEquation)
alist=Poly(denominator).all_coeffs()
 
G = co.TransferFunction(1, (1, 125, 5100, 65000, 0))
rlist, klist = co.rlocus(G)
plt.show()


