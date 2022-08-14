
while True:
    x = input("Введи два слова через пробіл:")
    if x.find(" ") != -1:
        w1 = x[:x.find(" ")][::-1]
        w2 = x[x.find(" ") + 1:][::-1]
        a = (w1+ " " +w2)
        print(a.title())
        break
    continue

# для заміни слів місцями
#  w1 = x[:x.find(" ")]
#  w2 = x[x.find(" ") + 1:]
#  print((w2 + " " + w1).title())





