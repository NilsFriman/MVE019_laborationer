import numpy as np

# g(x) - f(x)
def function_1a(x):
    return 30 / (x ** 2 + 4) - (6 * x * np.sin(x ** 2)) / (x ** 2 + 1)

# f(x) - g(x)
def function_1b(x):
    return 3 * np.e ** (-x / 2) * np.arctan(x ** 2) - 1 / (x + 1)

# sqrt(1 + f'(x) ** 2)
def function_2a(x):
    return np.sqrt(1 + (np.cos(x) - x * np.sin(x)) ** 2)

# f(x)
def function_2b(x):
    return x * np.cos(x)

# f(x)
def function_3(x):
    return np.e ** (- x ** 2)

def riemann(a, b, f, n):
    # Bestämmer bredden på varje rektangel
    delta_x = b - a / n

    # Definierar en summa för arean
    area = 0

    # Loopar över antalet rektanglar
    for rectanglecount in range(n):
        # Lägger till rektangelns area till summan
        # Detta beräknas som bredden gånger höjden
        # Bredden finns i variabeln delta_x
        # Höjden hittas genom att ta funktionens värde vid det aktuella x värdet

        # x värdet kommer att vara a (startvärdet) plus en halv (för att hamna mitt i en rektangel)
        # plus bredden gånger i (antalet rektanglar vi redan lagt till i summan)
        area += f(a + rectanglecount * delta_x + delta_x / 2) * delta_x

    return area

def arclength(a, b, f, n):

    delta_x = (b - a) / n
    length = 0

    for i in range(n):
        length += np.sqrt(delta_x ** 2 + (f((i + 1) * delta_x) - f(i * delta_x)) ** 2)

    return length

def trapezoid(a, b, f, n):
    delta_x = (b - a) / n
    area = 0

    for i in range(n):
        area += delta_x * (f(a + i * delta_x) + f(a + (i + 1) * delta_x)) / 2

    return area


print("Arean mellan graferna för f(x) och g(x) på intervallet [-3, 3] är", riemann(-3, 3, function_1a, 1000))

print("---------------------------------------------------------------------")

print("Arean mellan graferna för f(x) och g(x) är", riemann(0.539816, 7.311782, function_1b, 1000))

print("---------------------------------------------------------------------")

print("Båglängden för f(x) på intervallet [0, 2 * pi] beräknat med formeln för båglängd är", riemann(0, 2 * np.pi, function_2a, 1000))

print("---------------------------------------------------------------------")

print("Båglängden för f(x) på intervallet [0, 2 * pi] beräknat med summa av avstånd är", arclength(0, 2 * np.pi, function_2b, 1000))

print("---------------------------------------------------------------------")

for j in range(2, 5):

    c = 10 ** j

    print("Integralens värde för n =", c, "med trapetser är", trapezoid(-10, 10, function_3, c))
    print("Integralens värde för n =", c, "med riemann är", riemann(-10, 10, function_3, c))
