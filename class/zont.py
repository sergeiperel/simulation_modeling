import random

n = 10000  # num of experiments
p = 0.2
x = 1
y = 1
k = 0
s = 0
for i in range(0, n):
    wet = 0
    s = 0
    while wet != 1:
        if ((i % 2 == 0) and (x == 0)) or ((i % 2 == 1) and (y == 0)):
            wet = 1
        if random.random() < p:
            if i % 2 == 0:
                x -= 1
                y += 1
                s += 1
            else:
                y -= 1
                x += 1
                s += 1

print(s / n)
print(s)




