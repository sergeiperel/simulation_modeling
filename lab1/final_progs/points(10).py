import random


def is_in_triange(x, y):
    a = (x[1] - x[0]) * (y[2] - y[1]) - (x[2] - x[1]) * (y[1] - y[0])
    b = (x[2] - x[0]) * (y[3] - y[2]) - (x[3] - x[2]) * (y[2] - y[0])
    c = (x[3] - x[0]) * (y[1] - y[3]) - (x[1] - x[3]) * (y[3] - y[0])
    if a >= 0 and b >= 0 and c >= 0 or a <= 0 and b <= 0 and c <= 0:
        return True  # точка х0 у0 внутри треугольника
    else:
        return False


ratio = 2
N = 100000
count = 0
for j in range(N):
    x = []
    y = []
    for i in range(4):
        x.append(random.uniform(-ratio, ratio))
        y.append((random.uniform(-(ratio ** 2 - x[i] ** 2) ** 1 / 2, (ratio ** 2 - x[i] ** 2) ** 1 / 2)))
    a = False
    for i in range(1, 4):
        a = is_in_triange(x, y)
        if a:
            break
        x[0], x[i] = x[i], x[0]
        y[0], y[i] = y[i], y[0]
    else:
        count += 1
print(1 - count / N)