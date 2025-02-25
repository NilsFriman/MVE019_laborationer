import numpy as np

def fun(x):
    # Skrev om ekvationen så att allt var på vänsterledet, detta blev funktionen.
    return 3 * np.sin(x) - 4 * np.cos(x) - 2

def der_fun(x):
    # Deriverade funktionen.
    return 3 * np.cos(x) + 4 * np.sin(x)

# Parametrar: Funktion, begynnelsevärde a och b, tolerans.
def bisect(f, a, b, tolerance):

    # Hittar mittpunkten.
    c = (a + b) / 2

    # Loopar tills tillräcklig bra värde är hittat.
    while tolerance < abs(f(c)):
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        # Uppdaterar värdet på c, då a eller b har ändrats.
        c = (a + b) / 2
    return c

# Parametrar: Funktion, derivatan, begynnelsevärde och tolerans.
def newton(f, df, x, tolerance):

    # Loopar tills tillräcklig bra värde är hittat.
    while abs(f(x)) > tolerance:

        # Uppdaterar värdet på x
        x = x - f(x) / df(x)
    return x

# Uppgift 1
# Raden under gör så att vi loopar från -1 till -6 med steg -1 varje iteration
for i in range(-1, -6, -1):
    print("Bisect method for tolerance 10^" + str(i) + ":", bisect(fun, 0, 2, 10 ** i))

# Uppgift 2
# Raden under gör så att vi loopar från -1 till -6 med steg -1 varje iteration
for i in range(-1, -6, -1):
    # Begynnelsevärdet blev mitt på intervallet given i uppgiften
    print("Newton method for tolerance 10^" + str(i) + ":", newton(fun, der_fun, 1.5, 10 ** i))

