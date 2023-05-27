x = 19 # people that don't know the news
y = 1  # people that know and are happy to share the news
z = 0  # people that don't give
N = 19
p1 = (x * y) / (x * y + y * (y - 1) / 2 + (N + 1 - x - y) * y)
p2 = (y * (y - 1) / 2) / (x * y + y * (y - 1) / 2 + (N + 1 - x - y) * y)
p3 = ((N + 1 - x - y) * y) / (x * y + y * (y - 1) / 2 + (N + 1 - x - y) * y)

while (x != 0 ) and (y != 0):

