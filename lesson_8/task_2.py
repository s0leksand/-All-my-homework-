import random

x = int(input('Введите размер таблицы: '))

i = [random.randint(0, x + 1) for _ in range(x)]
a = 0

for q in i:
    for y in i:
        a += 1
        if a == a:
            print(q, end='\t')
        else:
            print(y, end='\t')
    print()