#Знакомство с языком Python (семинары). Урок 3. Данные, функции и модули в Python

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример: 45 -> 101101, 3 -> 11, 2 -> 10

import random
decNumber = 2 #random.randint(0, 2**100)

binNumber = str(bin(decNumber)).replace("0b", "")
print('\n', decNumber, '->', binNumber, '\n')
