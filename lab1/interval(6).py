import random


def expected_product(n):
    int  = random.uniform(0, 1)
    pr = int
    for i in range(2, n+1):
        int = random.uniform(int, 1)
        pr *= (1 - int)
    # random.uniform(0.5, 1)
    return pr


n = 100
print(expected_product(n))
