print('задание 1')
print('пункт 1')
import math
a=int(input())
if math.sqrt(a)%10!=0:
    print('error')
else:
    print(math.sqrt(a))

print('пункт 2')
import datetime
print(datetime.datetime.now())





print('задание 2')
from module_d import summa

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
res = summa(num1, num2)
print("Сумма равна: " ,res)






print('задание 3')
from pack1 import num, text
#numbers

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
Summa = num.sum(num1, num2)
Multiply = num.mult(num1, num2)2

print("Сумма чисел равна: ", Summa)
print("Произведение чисел равно: ", Multiply)


#text

a = input("Введите текст: ")
Upper = text.upper(a)
Reverse = text.rev(a)

print("Высокий регистр: ", Upper)
print("Задом наперёд: ", Reverse)
