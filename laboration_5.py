import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

def function_1(y, x):
    return [y[0] - 3 * y[1] - 5 * x, y[0] + 2 * y[1] + x]

# Skrev om funktionen
def function_2(y, x):
    return [y[1], 0.1 + 0.7 * np.sin(x) + np.sin(1.3 * x) + 4.5 * y[1] + 11.2 * y[0]]

def solve(f, a, b, y1_0, y2_0):
    x = np.linspace(a, b, 100000)
    y = odeint(f, [y1_0, y2_0], x).T

    plt.plot(x, y[0])
    plt.plot(x, y[1])
    plt.show()

# Uppgift 1
solve(function_1, 0, 5, 1, -1)

# Uppgíft 2
solve(function_2, 0.3, 5, -2.4, -0.7)
