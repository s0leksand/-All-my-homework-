n = int(input("Введіть число: "))
for a in range(n):
    square = a * a
    if square >= n:
        break
    print (square)