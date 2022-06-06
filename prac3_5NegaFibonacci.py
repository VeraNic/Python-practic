#Знакомство с языком Python (семинары). Урок 3. Данные, функции и модули в Python

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример: для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 
# [Негафибоначчи(https://u.to/WVUsHA)]

import random
k = random.randint(0, 17)
print('\nk = ', k)

def negafib(n):
    if n == -1:
        return 1
    if n == -2:
        return -1
    if n != -1 and n!= -2:
        return negafib(n+2) - negafib(n+1)

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n > 2:
        return fib(n-2) + fib(n-1)

list = []

for item in range(-k, 0):
    list.append(negafib(item))
for item in range(0, k+1):
    list.append(fib(item))
print(list, '\n')