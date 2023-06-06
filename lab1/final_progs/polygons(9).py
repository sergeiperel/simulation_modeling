import random


def polygon(n):
    a = random.randint(0, n - 2)
    if a <= 1:
        return n + a
    else:
        return n - a + 1

N = 100
n = 10000
count = 0
for j in range(n):
    start = 3
    for i in range(N):
        a = polygon(start)
        start = a
    if start == 3:
        count += 1
print(count / n)
