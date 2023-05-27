import random


def disc1(pos):
    win = 0
    if pos <= p11:
        disc1(random.random())
    elif pos <= p12:
        disc2(random.random())
    else:
        win = 1
    return win


def disc2(pos):
    loss = 0
    if pos <= p21:
        disc1(random.random())
    elif pos <= p22:
        disc2(random.random())
    else:
        loss = 2
    return loss


n = N = 1000000
p11, p12, p21, p22 = 0.2, 0.4, 0.3, 0.35
k = 0

while n != 0:
    pos = random.random()
    prob = disc1(pos)
    if prob == 1:
        k += 1
    n -= 1
print("Вероятность выйграть в эту игру равна " + str(k/N))
