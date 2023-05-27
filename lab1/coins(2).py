# import random
#
#
# def rand_coin_side():
#     return random.randint(0, 1)
#
#
# def analysis(k):
#     k += 1
#     print(k)
#     a = rand_coin_side()
#     b = rand_coin_side()
#     c = rand_coin_side()
#
#     if ((a == b) and (a != c)) or ((b == c) and (a != c)) or ((a == c) and (a != b)):
#         coins_review(a, b, c, k)
#     else:
#         analysis(k)
#
#
#
#
# def coins_review(a, b, c, k):
#     global l, m, n
#     # print(l)
#     if (l == 0) or (m == 0) or (n == 0):
#         analysis(k)
#     else:
#         if a == b:
#             l -= 1
#             m -= 1
#             n += 1
#         elif a == c:
#             l -= 1
#             m += 1
#             n -= 1
#         else:
#             l += 1
#             m -= 1
#             n -= 1
#         analysis(k)
#
#
#
# N, num = 5, 10
# sum = 0
# while N != 0:
#     l, m, n = 4, 7, 9
#     k = 0
#     analysis(k)
#     N -= 1
#
# # print(sum / num)
# # print(type(rounds))




import random


def rand_coin_side():
    return random.randint(0, 1)



N, num = 100000, 100000
summa = 0
while N != 0:
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
            n += 1
        elif (b == c) and (a != c):
            l += 1
            m -= 1
            n -= 1
        else:
            l -= 1
            m += 1
            n -= 1
    N -= 1
    summa += k
print(summa / num)