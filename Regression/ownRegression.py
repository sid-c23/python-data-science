#use PROMPT
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

Xs = np.array([1, 2, 3, 4, 5, 6], dtype=np.float64)
Ys = np.array([5, 4, 6 ,5, 6, 7], dtype=np.float64)

def bestFitSlopeAndIntercept(Xs, Ys):
    m = ( (mean(Xs) * mean(Ys)) - mean(Xs * Ys) ) / ( (mean(Xs)**2) - mean(Xs**2) )
    b = mean(Ys) - m * mean(Xs)
    return m, b

m, b = bestFitSlopeAndIntercept(Xs, Ys)
#print(m, b)
regressionLine = [(m * x) + b for x in Xs]

predictX = 8

predictY = m * predictX + b

plt.scatter(Xs, Ys)
plt.scatter(predictX, predictY, color="g")
plt.plot(Xs, regressionLine)
plt.show()
