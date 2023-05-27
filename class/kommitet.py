import math
import random
n = 1000000
m = 0
for i in range(0, n):
    # 1-6 prof, 7-12 doc, 13-22 - prep, 23-34 - assist
    kafedra = []
    for j in range(0, 34):
        kafedra.append(j)
# print(len(kafedra))
    for i in range(len(kafedra)-1, -1, -1):
        y = math.floor(i * random.random())
        num = kafedra[i]
        kafedra[i] = kafedra[y]
        kafedra[y] = num
    komitet = []
    for k in range(0, 6):
        komitet.append(kafedra[33 - k])
    prof = 0
    doc = 0
    prep = 0
    assist = 0
    for k in range(0, 6):
        if komitet[k] < 6:
            prof += 1
        elif (komitet[k] >= 6) and (komitet[k] <= 11):
            doc += 1
        elif (komitet[k] >= 12) and (komitet[k] <= 21):
            prep += 1
        elif (komitet[k] >= 22) and (komitet[k] <= 33):
            assist += 1
    if (prof*doc*prep*assist > 0):
        m += 1


print(m/n)