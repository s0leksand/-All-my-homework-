
z = list(input("Введіть список: "))
x = int(input("Введіть значення: "))
y = int(input("Введіть індекс числа: "))

z.append(0)


for i in range(len(z) - 1, y, -1):
    z[i] = z[i - 1]
z[y] = x
print(" ".join([str(i) for i in z]))



print(z)




#z = list(input("Введіть список: "))
#x = int(input("Введіть значення: "))
#y = int(input("Введіть індекс числа: "))