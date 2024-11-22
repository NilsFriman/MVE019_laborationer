
# Importerar nödvändigt bibliotek
import numpy as np

# Definierar funktionen
def function(x):
    return np.sin(x)*np.cos(x**2)


def Riemann(a, b, f, n):

    # Bestämmer bredden på varje rektangel
    width = np.abs(b - a) / n

    # Definierar en summa
    sum = 0

    # Loopar över antalet rektanglar
    for i in range(n):
        # Lägger till rektangelns area till summan
        # Detta beräknas som bredden gånger höjden
        # Bredden finns i variabeln width
        # Höjden hittas genom att ta funktionens värde vid det aktuella x värdet

        # x värdet kommer att vara a (startvärdet) plus en halv (för att hamna mitt i en rektangel)
        # plus bredden gånger i (antalet rektanglar vi redan lagt till i summan)
        sum += f(a + i * width + width / 2) * width

    return sum

    
# Loopar för att snyggt kunna printa våra integraler beroende på hur många rektanglar vi gör
# (Det behöver inte göras på ett såhär komplicerat sätt)
for i in range(6):
    n = i * 500 + 1000
    print("n =", str(n) + ":", Riemann(0, 3, function, n))
