import numpy as np

l = 1000000
m = 2**31 - 1
a = 7**5


def I(x, y):
    if (y <= x):
        return 1
    else:
        return 0


def f(x, y):
    f = (1/x**2) * (1/y**2) * np.exp(-(1/x + 1/y - 2)) * I(1/x - 1, 1/y - 1)
    return f


sum = 0
x, y = [], []
x.append(1)
y.append(2)
for i in range(0, l-1):
    x.append(np.mod(a * x[i], m))
    y.append(np.mod(a * y[i], m))
for i in range(0, l - 1):
    x[i] /= m
    y[i] /= m
for i in range(0, l-1):
    sum += f(x[i], y[i])

print(sum / l)





