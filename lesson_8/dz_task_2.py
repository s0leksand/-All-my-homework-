import random

n = input("Введіть N: ")
int_n = int(n)

arr = [[random.randint(1, 20) for j in range(int_n)] for i in range(int_n)]

print("Матриця:")
for i in range(int_n):
    for j in range(int_n):
        print(f'{arr[i][j]:>{len(n*2)}}', end="\t")
    print('\n')


x = arr[0][0]
for a in range(int_n-1):
    x += arr[a + 1][a + 1]
print("Сума по діагоналі:", x)
print('')

y = arr[0][-1]
for a in range(int_n-1):
    y += arr[a + 1][-1]
print("Сума останього стовпця:", y)
