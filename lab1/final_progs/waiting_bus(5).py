import random

num_arrivals = 10000
time = 0
num_of_rand_buses = 1

for i in range(num_arrivals):
    wait_time = 0
    arr_time = random.random()
    route = [0]
    for i in range(num_of_rand_buses):
        route.append(random.random())
    route.sort()
    if arr_time > route[num_of_rand_buses]:
        wait_time = 1 - arr_time
    else:
        test = 1
        k = 1
        while test == 1:
            if arr_time < route[k]:
                wait_time = route[k] - arr_time
                test = 0
    time += wait_time

print("Следующего автобуса ждать примерно", time/num_arrivals * 60, "минут")
