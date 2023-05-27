import random
import math

import numpy as np

l = 1000
m = 2**31 - 1
a = 7**5
def f(x):
    y = np.exp(np.exp(x))
    return y


sum = 0
x, y = [], []
x.append(1)
y.append(1)
for i in range(0, l-1):
    x.append(np.mod(a * x[i - 1], m))
    y.append(x[i] / m)
for i in range(0, l-1):
    sum += f(y[i])

print(sum / l)





