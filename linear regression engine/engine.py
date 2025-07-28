from typing import List
from matplotlib import pyplot as plt
import numpy as np

""" Calculates the mean of a list"""
def mean(values: List[float]) -> float:
    sum: float = 0
    n: float = len(values)

    for i in range(0, n):
        sum += values[i]
    
    return (sum / n)

""" Calculates the summary statistic for either Sxx or Syy"""
def ss1(values: List[float]) -> float:
    sum: float = 0
    n: float = len(values)

    for i in range(0, n):
        sum += (values[i] - mean(values))**2

    return sum

""" Calculates the summary statistic for Sxy"""
def ss2(xValues: List[float], yValues: List[float]) -> float:
    sum: float = 0
    n: float = len(xValues)

    for i in range(0, n):
        sum += (xValues[i] - mean(xValues))*(yValues[i] - mean(yValues))
    
    return sum

""" Regresion line in the form y = a + bx"""
def regression_line(xValues: List[float], yValues: List[float]):
    b = ss2(xValues, yValues) / ss1(xValues)
    a = mean(yValues) - b * mean(xValues)

    r = ss2(xValues, yValues) / (ss1(xValues) * ss1(yValues))**0.5


    x = np.linspace(0, 100, 1000)
    y = a + b*x
    
    plt.scatter(xValues, yValues)
    plt.plot(x, y, color='blue')
    plt.title(f"y = {a} + {b}x, r = {r}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()