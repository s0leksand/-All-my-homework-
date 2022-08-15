rows = int(input("Задай від 3 до 9: "))
rows_1 = rows + 1

if 3 <= rows_1 <= 9:
    for i in range(1, rows_1 + 1):
        for j in range(1, i - 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()