import random


def simulate():
    seats = ['free'] * 220
    seats[random.randint(0, 219)] = 'taken'

    for i in range(1, 219):
        if seats[i] != 'taken':
            seats[i] = 'taken'
        else:
            while True:
                seat_number = random.randint(0, 219)
                if seats[seat_number] != 'taken':
                    break
            seats[seat_number] = 'taken'
    return seats[219] == 'free'


num_trials = 10000
num_successes = 0
for i in range(num_trials):
    if simulate() == 1:
        num_successes += 1


print(num_successes)
print('Вероятность занять место согласно билету:', num_successes / num_trials)
