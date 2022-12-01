#Задание 1:
a = int(input("Введите день недели"))
if a == 6 or 7:
    print("да")
else:
    print("нет")
a = int(input("Введите x"))
b = int(input("Введите y"))
#Задание 2:
#Задание 3:
if a > 0 and b > 0:
    print("1")
if a < 0 and b < 0:
    print("3")
if a < 0 and b > 0:
    print("2")
if a > 0 and b < 0:
    print("4")
#Задание 4:
a = int(input("Введите  номер четверти"))
if a == 1:
    print('x = 1-5, y = 1-5')
if a == 2:
    print('x = (-1)-(-5), y = 1-5')
if a == 3:
    print('x = (-1)-(-5), y = (-1)-(-5)')
if a == 4:
    print('x = 1-5, y = (-1)-(-5)')
#Задание 5:
import math
a1 = float(input('Введите x1'))
b1 = float(input('Введите b1'))
a2 = float(input('Введите x2'))
b2 = float(input('Введите b2'))
R1 = math.sqrt((a2 - a1)**2 + (b2 - b1)**2)
print(R1)