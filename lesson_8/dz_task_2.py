import random

x = int(input('Розмір таблиці:'))
a = 0
b = 0
sum = []

for matrix in range(x):
        a += 1
        for matrix_1 in range(x):
            b += 1
            matrix_1 = [random.randint(0,9) for _ in range(x)]
            if (a == b):
                sum.append(matrix_1)
            break

diagonalSumma = 0
print(sum)


i = 0
for x in sum:
    diagonalSumma += sum[i][i]
    i+=1
print('----------')
print('По діагоналі', diagonalSumma)


lastRowSum = 0


for x in sum[(len(sum) - 1)]:
    lastRowSum += x

print('----------')
print('Сума останнього рядка ', lastRowSum)

