# Importerar nödvändigt bibliotek
import numpy as np

# Definierar funktionen
def f(x):
    return np.sin(x) * np.cos(x ** 2)

def riemann(a, b, function, totalrectangles):
    # Bestämmer bredden på varje rektangel
    width = np.abs(b - a) / totalrectangles

    # Definierar en summa
    rectanglesum = 0

    # Loopar över antalet rektanglar
    for rectanglecount in range(totalrectangles):
        # Lägger till rektangelns area till summan
        # Detta beräknas som bredden gånger höjden
        # Bredden finns i variabeln width
        # Höjden hittas genom att ta funktionens värde vid det aktuella x värdet

        # x värdet kommer att vara a (startvärdet) plus en halv (för att hamna mitt i en rektangel)
        # plus bredden gånger i (antalet rektanglar vi redan lagt till i summan)
        rectanglesum += function(a + rectanglecount * width + width / 2) * width

    return rectanglesum

# Loopar för att snyggt kunna printa våra integraler beroende på hur många rektanglar vi gör
# (Det behöver inte göras på ett såhär komplicerat sätt)
for i in range(6):
    n = i * 500 + 1000
    print("n =", str(n) + ":", riemann(0, 3, f, n))
