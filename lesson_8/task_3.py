import random

i = [random.randint(0, 20) for _ in range(15)]

g = []
q = []

for x in i:
    if x % 2 == 0:
        g.append(x)
    else:
        q.append(x)
if g > q:
    print("Ні")
else:
    print("Так")
