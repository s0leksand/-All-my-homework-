x = list(input("Введіть числа: "))
y = int(input("Введіть індекс числа: "))

for i in range(y, len(x)-1):
    x[i] = x[i+1]
x.pop()
print(x)