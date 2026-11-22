
Задача 1
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
a = 0 
y = 0
if num1 > a:
    a = num1 + a
    y = y + 1
if num2 > a:
    a = num2 + a
    y = y + 1
if num3 > a:
    a = num3 + a
    y = y + 1
if num4 > a:
    a = num4 + a
    y = y + 1 
if y > 0:
    print (a/y)
else:
    print("нет пол.чисел")

Задача 2
num = int(input())
num1 = int(input())
if num % 2 == 1 and num1 % 2 == 1:
    print("true")
else:
    print("false")

Задача 3
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = b**2 - 4*a*c
if d>0:
    x1 = (-b - d**0.5)/2*a
    x2 = (-b + d**0.5)/2*a
    print("x1 = ",x1,"\n","x2 = ",x2)
if d == 0:
    x = -b/2*a
    print(x)
else:
    print("Нет решения")

Задача 4
nums = input("введите 5 целых чисел через пробелов: ", )+" "
num_list = []
x = ""
for symbol in nums:
    if symbol != " ":
        x+=symbol
    else:
        num_list.append(int(x))
        x = ""
print(num_list)


Задача 5
fruits = input("введите 7 фруктов через пробел: ")+" "
fruits_list = []
x = ''
for fruit in fruits:
    if fruit != " ":
        x += fruit
    else:
        fruits_list.append(x)
        x = ""
print(fruits_list[0],fruits_list[2],fruits_list[-1])

Задание 6
nums = input("Введите 10 целых чисел черези пробел: ")+" "
x = ""
nums_list = []
for number in nums:
    if number != " ":
        x += number
    else:
        nums_list.append(int(x))
        x = ""
print(nums_list[::-1])

Задание 7
words = input("введите 7 слов через побел: ",)+" "
x = ""
words_list = []
for word in words:
    if word != " ":
        x += word 
    else:
        words_list.append(x)
        x = ""
for y in words_list:
    wrd = list(y)
    if wrd[0] == "a":
        print(y)

Задание 8
nums = input()+" "
nums_list = []
x = ""
for num in nums:
    if num != " ":
        x += num
    else:
        nums_list.append(float(x))
        x = ""
for y in nums_list:
    print(y**2)