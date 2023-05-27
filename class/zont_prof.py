import numpy as np
import random
import matplotlib.pyplot as plt

n = 10000
p = 0.2

wet = 0

Ox, Oy = [], []
for j in range (1, 99):
    p = j / 100
    s = 0
    for i in range(n):
        x = 1
        y = 1
        wet = 0  #
        trips = 0
        location = -1  # a = -1,  b = 1

        while wet < 1:
            if (random.random()>p):
                location = location * (-1)
                trips += 1
            else:
                if (location == -1):
                    if (x == 0):
                        wet = 1
                    else:
                        x = x - 1
                        trips = trips + 1
                        y = y + 1
                        location = location * (-1)
                else:
                    if (y == 0):
                        wet = 1
                    else:
                        y = y - 1
                        trips = trips + 1
                        x = x + 1
                        location = location * (-1)

        s += trips
    Ox.append(p)
    Oy.append(s / n)

print(s / n)


plt.plot(Ox, Oy, label = "graph")
plt.legend()
plt.show()
