n = int(input("Введіть число: "))
for a in range(n):
    square = a * a
    if str(square).endswith(str(a)):
        print (square)