import matplotlib.pyplot as plt
import random

n = 1000
Oy, Ox = [], []

for j in range(1, 100):
    p = j/100
    sum = 0
    for i in range(n):
        x = 1
        y = 1
        wet = 0
        trips = 0
        location = -1
        while wet < 1:
            if (random.random() > p):
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
        sum += trips
    Oy.append(sum/n)
    Ox.append(p)

min_trips = min(Oy)
ind_min_trips = Oy.index(min_trips)
prob_min = Ox[ind_min_trips]
print('Минимальное количество поездок: ' + str(min_trips))
print('Вероятность дождя при минимальном количестве поездок: ' + str(prob_min))
plt.plot(Ox, Oy, label = 'График средних')
plt.ylabel("число поездок")
plt.xlabel("вероятность дождя")
plt.grid()
plt.legend()
plt.show()
