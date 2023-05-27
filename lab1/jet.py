import random

def simulate():
    seats = ['free'] * 220
    seats[random.randint(0, 219)] = 'taken'

    for i in range(1, 219):
        seat_number = i
        while seats[seat_number - 1] == 'taken':
            # seat_number = random.randint(1, 220)
            seat_number += 1
        seats[seat_number - 1] = 'taken'
    print(seats)
    return seats[219] == 'free'


num_trials = 100000
num_successes = 0
for i in range(num_trials):
    if simulate() == 1:
        num_successes += 1


print(num_successes)
print('Вероятность занять место согласно билету:', num_successes / num_trials)
