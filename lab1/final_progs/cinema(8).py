import random

num_of_exp = 10000
tickets = 100
match = 0

for i in range(num_of_exp):
    ticket = []
    for j in range(0, tickets):
        ticket.append(j)
    random.shuffle(ticket)
    for j in range(tickets):
        if ticket[j] == j:
            match += 1
            break

print(1 - match/num_of_exp)
