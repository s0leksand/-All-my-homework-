
y = 0
summ = 0
maxim = 0
minimum = 0
para = 0
ne_para = 0

while True:
    n = int(input("Введіть саме позитивне число: "))
    summ += n
    y += 1
    if n == 0:
        y = (y - 1)
        break
    if n%2 == 0:
        para += 1
    else:
        ne_para +=1
    if n > maxim:
        maxim = n
    if n < minimum:
        minimum = n
arif = (summ / y)

print("Сумма чисел", summ)
print("Середне", arif)
print("Максимальное число", maxim)
print("Минимальное число", minimum)
print("парное", para)
print("парное", ne_para)