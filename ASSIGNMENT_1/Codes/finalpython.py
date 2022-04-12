#NAME: JANGA TUSHITA SHARVA
#ROLL NUMBER: CS21BTECH11022
#ASSIGNMENT 1 solution

import numpy as np
from sympy import *
from sympy.plotting import plot

print("To find the value of k for which the equation 'x^2 - 4kx + k^2 - k + 2' has equal roots.")

#THE DISCRIMINANT POLYNOMIAL
k = np.poly1d([12, 4, -8])
print("The values of k for the which roots will be equal :")
print(1-k.r[0], round((k.r[1]), 2))

a = k.r[0]
b = k.r[1]
c = round(k.r[1],2)

#CHECKING IF THE ROOTS ARE EQUAL FOR THE GIVEN k

x = np.poly1d ([1, 4* a , a**2 - a + 2])
print("The roots of equation when k is " + str(a))
print(str(x.r[0]) + ", " + str(x.r[1]))

y = np.poly1d ([1, 4* b , b**2 - b + 2])
print("The roots of equation when k is " + str(c))
print(np.round((y.r[0]), 2), np.round((y.r[1]),2))

print("Thus roots of equation are equal for k = " + str(k.r[0]) + " and " + str(c))

print("Checking it using graph method: ")

x = symbols('x')

print("\n")
print("When k = -1")
p = plot(x**2 - 4 * x + 4, xlim = [-1, 5], ylim = [-1, 5], show = False)
p[0].line_color = 'r'
p.show()

print("\n")
print("when k = 2/3")
q = plot(x**2 + (8/3) * x + 16/9, xlim = [-5, 3], ylim = [-1, 5], show = False)
q[0].line_color = 'g'
q.show()

print("Note that in both graphs, the parabola touches x axis at only one point, that is the equal root of the equation.")