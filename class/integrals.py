import random
import math
l = 5000
m = 0
def f(x):
    y = 1 / math.sqrt(x ** 3 + 1)
    return y

sum = 0
x, y = [], []
for i in range(0, l):
    x.append(random.random() * 2.0)
    y.append(random.random() * 1.0)
    sum += f(x[i])
    if y[i] <= f(x[i]):
        m += 1
print(2 * m / l)
print(2 * sum / l)





