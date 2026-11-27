direction = input("Введите направление (left, right, straight, back): ").strip().lower()

match direction:
    case "left":
        print("Иду влево")
    case "right":
        print("Иду вправо")
    case "straight":
        print("Иду прямо")
    case "back":
        print("Иду назад")
    case _:
        print("Неправильное направление")

# 2)
password = input("Придумайте пароль: ")
confirm_password = input("Подтвердите пароль: ")

if password != confirm_password:
    print("Пароли не совпадают!")
else:
    login_password = input("Введите пароль для авторизации: ")
    if login_password == password:
        print("Access")
    else:
        print("Denied")

# 3)
text = input("Введите произвольный текст: ")
word = input("Введите слово для поиска: ")

if word in text:
    count = text.count(word)
    print(f"Слово есть в тексте. Количество вхождений: {count}")
else:
    print("Данного слова нет в тексте.")

# 4)
year = int(input("Введите год: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Год високосный")
else:
    print("Год не високосный")

#  5)

import math

parts = input("Введите выражение через пробел (например: 5 + 3 или 9 /**): ").split()

num1 = float(parts[0])
op = parts[1]
num2 = float(parts[2]) if len(parts) > 2 else None

match op:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Ошибка: деление на ноль!")
    case "%":
        if num2 != 0:
            print(num1 % num2)
        else:
            print("Ошибка: деление на ноль!")
    case "//":
        if num2 != 0:
            print(num1 // num2)
        else:
            print("Ошибка: деление на ноль!")
    case "**":
        print(num1 ** num2)
    case "%%":
        # число 2 процентов от числа 1
        print((num1 * num2) / 100)
    case "/**":
        # корень числа
        if num1 >= 0:
            print(math.sqrt(num1))
        else:
            print("Ошибка: корень из отрицательного числа!")
    case _:
        print("Неизвестный оператор")
