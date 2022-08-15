r = input("Речення string")
x = input("Вводимо char для пошуку")

start = -1
count = 0

while True:
    start = r.find(x, start+1)
    if start == -1:
        break
    count += 1
print("Кількість char в string: ", count )
