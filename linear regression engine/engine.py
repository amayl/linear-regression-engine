from typing import List
from matplotlib import pyplot as plt
import numpy as np

""" Calculates the mean of a list"""
def mean(values: List[float]) -> float:
    sum: float = 0
    n: int = len(values)

    for i in range(0, n):
        sum += values[i]
    
    return (sum / n)

""" Calculates the summary statistic for either Sxx or Syy"""
def ss1(values: List[float]) -> float:
    sum: float = 0
    n: int = len(values)
    avg = mean(values)

    for i in range(0, n):
        sum += (values[i] - avg)**2

    return sum

""" Calculates the summary statistic for Sxy"""
def ss2(xValues: List[float], yValues: List[float]) -> float:
    sum: float = 0
    n: int = len(xValues)
    avgx, avgy = mean(xValues), mean(yValues)

    for i in range(0, n):
        sum += (xValues[i] - avgx)*(yValues[i] - avgy)
    
    return sum

""" Regresion line in the form y = a + bx"""

def regression_line(xValues: List[float], yValues: List[float]):
    if len(xValues) < 2 or len(yValues) < 2:
        print("Error: at least two data points are required.")
        return None

    ss1_x = ss1(xValues)
    ss1_y = ss1(yValues)
    ss2_xy = ss2(xValues, yValues)

    if ss1_x == 0:
        print("Error: all X values are identical. can't perform regression.")
        return None
    if ss1_y == 0:
        print("Error: all Y values are identical. can't compute correlation coefficient.")
        return None

    b = ss2_xy / ss1_x
    a = mean(yValues) - b * mean(xValues)
    r = ss2_xy / (ss1_x * ss1_y) ** 0.5

    import numpy as np
    from matplotlib import pyplot as plt

    x = np.linspace(0, 100, 1000)
    y = a + b * x

    plt.scatter(xValues, yValues)
    plt.plot(x, y, color='blue')
    plt.title(f"y = {a} + {b}x, r = {r}")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend()
    plt.show()

    return a, b, r
