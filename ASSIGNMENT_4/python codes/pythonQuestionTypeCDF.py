import numpy as np
from sympy import *
from scipy.stats import binom
import matplotlib.pyplot as plt

y = 1
p = 9/14
# defining the list of r values
y_values = list(range(y + 1))

cdfValues = [binom.cdf(r, y, p) for r in y_values ]

xVal = y_values
yVal = cdfValues

print("The probabilities of all the events are as follows:")
print("Y\tP(Y)")
for i in range(y + 1):
    print(str(y_values[i]) + "\t" + str(cdfValues[i]))

plt.xlabel("Y value")
plt.ylabel("P(Y) value")
plt.title("CDF for the type of question asked")
plt.plot(xVal, yVal, 'o', color = "#202A44")
plt.vlines(xVal, 0, yVal, linestyle = 'dashed', color = "#202A44")
plt.ylim(bottom = 0)
plt.grid()
plt.show()