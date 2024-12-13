import numpy as np

def fun(x):
    return 3 * np.sin(x) - 4 * np.cos(x) - 2

def der_fun(x):
    return 3 * np.cos(x) + 4 * np.sin(x)

def recursive_bisect(f, a, b, tolerance):
    c = (a + b) / 2
    if abs(f(c)) <= tolerance:
        return c
    elif f(a) * f(c) < 0:
        return recursive_bisect(f, a, c, tolerance)
    else:
        return recursive_bisect(f, c, b, tolerance)

def boring_bisect(f, a, b, tolerance):
    c = (a + b) / 2
    while abs(f(c)) > tolerance:
        if f(a) * f(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
    return c

def recursive_newton(f, df, x, tolerance):
    new_x = x - f(x) / df(x)
    if abs(f(new_x)) < tolerance:
        return new_x
    else:
        return recursive_newton(f, df, new_x, tolerance)

def boring_newton(f, df, x0, tolerance):
    x = x0 - f(x0) / df(x0)
    while abs(f(x)) > tolerance:
        x = x - f(x) / df(x)
    return x

# Uppgift 1
for i in range(-1, -6, -1):
    print("Recursive bisect for tolerance 10^" + str(i) + ":", recursive_bisect(fun, 0, 2, 10 ** i))
    print("Boring bisect for tolerance 10^" + str(i) + ":", boring_bisect(fun, 0, 2, 10 ** i))

# Uppgift 2
for i in range(-1, -6, -1):
    print("Recursive newton for tolerance 10^" + str(i) + ":", recursive_newton(fun, der_fun, 1.5, 10 ** i))
    print("Boring newton for tolerance 10^" + str(i) + ":", boring_newton(fun, der_fun, 1.5, 10 ** i))

