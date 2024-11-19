
# Importerar de nödvändiga biblioteken
import numpy as np
import matplotlib.pyplot as plt

# Definerar funktionen
def function(x):
    return np.sin(x) * np.cos(x ** 2)


def graph(a, b, f, n):

    # Fixar data
    x = np.linspace(a, b, n)
    y = f(x)

    # x och y är listor med värden, typ x = [0, 0.1, 0.2 ... ] och y = [5, 4.9, 4.8 ... ]

    # Plottar grafen
    plt.plot(x, y, color="green", linewidth=2)

    # Fixar så den blir snygg etc
    plt.axis('equal')
    plt.grid('on')
    plt.xlabel("X-axel")
    plt.ylabel("Y-axel")
    plt.title("Min supersexiga funktion")

    # Visar grafen
    plt.show()

# Detta kan ignoreras (men är korrekt)
def main():
    if __name__ == "__main__":

        # Kallar på funktionen
        graph(0, 3, function, 1000)


main()
