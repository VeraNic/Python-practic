#Знакомство с языком Python (семинары). Урок 3. Данные, функции и модули в Python

#3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
#Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random
lengthList = random.randint(3, 12)
list = []
minFrac = 100.00
maxFrac = 0.00
for item in range(lengthList):
    number =  random.randint(0, 9999) 
    intPart = number // 100
    number = number / 100.00
    fracPart = round(number - intPart, 2)
    list.append(number)
    if fracPart < minFrac:
        minFrac = fracPart
    if fracPart > maxFrac:
        maxFrac = fracPart
print('\n', list, '=>', round((maxFrac - minFrac), 2), '\n') 
