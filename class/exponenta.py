# from random import shuffle
import numpy as np
import math
n = 20
m = 1000000
a = []


for i in range(0, m):
    a.append(np.random.permutation(n))
k = 0
for i in range(0, m):
    for j in range(0, n):
        if a[i][j] == j:
            k += 1
            break
# print(a)
# print(k)
# print((math.factorial(n)-k)/math.factorial(n))
p = (m-k)/m
print(p)
print(abs(p - 1 / np.e))

