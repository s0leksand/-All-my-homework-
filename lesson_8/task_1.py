import random

n = input("Введіть число N: ")
int_n = int(n)

arr = [[random.randint(-int_n, -1) if i % 2 != 0 else i for j in range(int_n)] for i in range(int_n)]

for i in range(int_n):
    for j in range(int_n):
        print(f'{arr[i][j]:>{len(n*2)}}', end="\t")
    print('')
