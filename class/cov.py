import random
import numpy

m = 2 ** 31 - 1
a = 7 ** 5
n = 10000
x = [1]
y = [1]

# def I(x,y):
# if (0 < y <= x): return 1
# else: return 0

def f(x):
    return x * numpy.exp(x)

def g(x):
    return numpy.exp(x)

for i in range(n):
    x.append((a * x[i] % m))

for i in range(n):
    x[i] = x[i] / m

b1 = 1
a1 = 0
fig = []
fig2 = []

for i in range(n):
    fig.append(f(x[i]))

for i in range(n):
    fig2.append(g(x[i]))

integral = (b1 - a1) * (sum(fig)) / n
integral2 = (b1 - a1) * (sum(fig2)) / n

print(integral - 1/2 * integral2)





