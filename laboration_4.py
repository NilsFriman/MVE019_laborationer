import numpy as np
import matplotlib.pyplot as plt

def function_2(x, y):
    return y * np.sin(x)

def function_3(x, y):
    return np.sin(x + y)

def euler(F, a, b, A, h):
    n = int((b - a) // h)
    values = np.zeros(n)
    values[0] = A
    print(values)
    for i in range(1, n):
        values[i] = values[i - 1] + h * F(a + h * i, values[i - 1])
    return values

def graph(x, y):
    plt.plot(x, y)
    plt.show()

# Uppgift 2
graph(np.linspace(0, 4 * np.pi, int((4 * np.pi) // 0.5)), euler(function_2, 0, 4 * np.pi, 1, 0.5))
graph(np.linspace(0, 4 * np.pi, int((4 * np.pi) // 0.1)), euler(function_2, 0, 4 * np.pi, 1, 0.1))
graph(np.linspace(0, 4 * np.pi, int((4 * np.pi) // 0.01)), euler(function_2, 0, 4 * np.pi, 1, 0.01))

# Efter att undersökt med Geogebra verkar det som att y = pi * sin(x - pi / 2) + pi + 1

# Uppgift 3
graph(np.linspace(0, 4 * np.pi, int((4 * np.pi) // 0.1)), euler(function_3, 0, 4 * np.pi, 1, 0.1))

# Efter att ha undersökt verkar det inte finnas någon tydlig lösning
