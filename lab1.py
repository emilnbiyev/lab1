import math
def hesabla(x):
    p = 0
    term = 1
    n = 1
    epsilon = 0.001
    while math.fabs(term) > epsilon:
        p += term
        n += 1
        term = (-1) ** (n - 1) * (x ** n) / n
    return p


print(hesabla(0.1))
