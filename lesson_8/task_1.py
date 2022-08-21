x = int(input('Введите размер таблицы: '))
for i in range(1, x + 1):
    for col in range(1, x + 1):
        if i % 2 == 0:
            print(i, end='\t')
        else:
            print(col, end='\t')
    print()