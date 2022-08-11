x = input('Введите число:')

result = False
for i in range(len(x)):
    for j in range(len(x)):
        if i != j and x[i] == x[j]:
            result = True
            print(x[i], x[j], "рівні")
            break
    if result:
        break

if not result:
    print('Not equal')











