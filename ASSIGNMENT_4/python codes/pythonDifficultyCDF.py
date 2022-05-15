import numpy as np
from sympy import *
from scipy.stats import binom
import matplotlib.pyplot as plt

x = 1
p = 6/14
# defining the list of r values
x_values = list(range(x + 1))
#generates the probabilities for each n value
# list of cdf values
cdfValues = [binom.cdf(r, x, p) for r in x_values ]

print("The probabilities of all the events are as follows:")
print("X\tP(X)")
for i in range(x + 1):
    print(str(x_values[i]) + "\t" + str(cdfValues[i]))

xVal = x_values
yVal = cdfValues

plt.xlabel("X values")
plt.ylabel("P(X) values")
plt.title("CDF for the difficulty of the question")
plt.plot(xVal, yVal, 'o', color = "green")
plt.vlines(xVal, 0, yVal, linestyle = 'dashed', color = "green")
plt.ylim(bottom = 0)
plt.grid()
plt.show()