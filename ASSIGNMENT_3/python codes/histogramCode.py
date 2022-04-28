import sys
import numpy as np
import matplotlib.pyplot as plt
from random import *
import pandas as pd

sys.path.append('/home/SECOND_SEMESTER/AI1110/ASSIGN_3')
df = pd.read_excel('AnswerTable2.xlsx', 'Sheet1')

binArray = [0, 20, 30, 40, 50, 60, 70, 100]
classWidths = np.diff(binArray)

frequency = df['Frequency'].to_numpy()
rectangleLength = np.divide(frequency, classWidths) * 10
x = [randint(0, 19), randint(20,29), randint(30,39), randint(40, 49), randint(50,59), randint(60,69), randint(70,100)]

plt.hist(x, bins = binArray, weights = rectangleLength, ec = 'black')

plt.title('Histogram', fontsize=17)
plt.xlabel('Marks -->')
plt.ylabel('Proportion of students per ten marks interval')

plt.show()

