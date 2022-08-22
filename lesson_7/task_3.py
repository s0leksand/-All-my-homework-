x = list(input("Введіть список: "))
y = list(input("Введіть список 2: "))

a = x + y

q = []
for i in a:
    if i not in q:
        q.append(i)
print(q)
