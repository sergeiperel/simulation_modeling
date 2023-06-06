import random


def expected_product(n):
    int = random.uniform(0, 1)
    pr = int
    for i in range(2, n+1):
        int = random.uniform(int, 1)
        pr *= int
    return pr


n = 10000
num_of_exp = 1000
sum = 0
for i in range(num_of_exp):
    sum += expected_product(n)
print(sum / num_of_exp)
