import random

x = 0
y = 0

arr = [random.randint(1, 20) for j in range(15)]

for i in range(15):
    if arr[i] % 2 == 0:
        x += arr[i]
    else:
        y += arr[i]

if x < y:
    print("Так")
else:
    print("Ні")
