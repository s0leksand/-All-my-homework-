# my home work 3

print("Вирішуємо задачу №3")
print("----Реєстрація----")
a = input("Введіть пароль:")
print("Молодець! Дякую за реєстрацію!")

print("----Вхід в систему!----")
b = input("Ваш пароль:")

if a == b:
   print("Пароль вірний!")
else:
    print("Неа, не вірно! Ще 2 спроби")
    b = input("Ваш пароль. Сроба №2:")
    if a == b:
        print("Пароль вірний!")
    else:
        print("Неа, нажаль не вірно!")
        b = input("Ваш пароль. Спроба №3:")
        if a == b:
            print("Пароль вірний!")
        else:
            print("Неа, не вірно! Зверніться в нашу технічну підтримку.")



