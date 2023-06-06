import random


def rand_coin_side():
    return random.randint(0, 1)


N, num = 100000, 100000
summa = 0
for i in range(N):
    l, m, n = 4, 7, 9
    k = 0
    while (l * m * n) != 0:
        k += 1
        # print(k)
        a = rand_coin_side()
        b = rand_coin_side()
        c = rand_coin_side()

        if (a == b) and (a != c):
            l -= 1
            m -= 1
            n += 2
        elif (b == c) and (a != c):
            l += 2
            m -= 1
            n -= 1
        elif (a == c) and (a != b):
            l -= 1
            m += 2
            n -= 1
        else:
            continue
    summa += k

print(summa / num)
