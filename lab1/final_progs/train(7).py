import random
N = 1000
villagers = 2500
prob = 6 / 30
overflow = 1 / 100
capacity = 540
p = 1
while p > overflow:
    capacity += 1
    over = 0
    for i in range(N):
        sum = 0
        for j in range(villagers):
            if random.random() < prob:
                sum += 1
        if sum > capacity:
            over += 1
    p = over / N
print(capacity)
