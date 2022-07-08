import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5,5,30) #points on the x axis
len = int(1e6) #number of samples
err = [] #declaring probability list
randvar = np.loadtxt('gau.dat',dtype='double')

for i in range(0,30):
	err_ind = np.nonzero(randvar < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/len) #storing the probability values in a list

plt.plot(x,err,'.')
plt.plot(x.T,err) #plotting the CDF
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_X(x)$')
plt.legend(["Numerical", "Theory"])
plt.savefig('gau_cdf.png')
plt.savefig('gau_cdf.pdf')
plt.savefig('gau_cdf.eps')