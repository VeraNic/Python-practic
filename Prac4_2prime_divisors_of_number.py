#Знакомство с языком Python (семинары). Урок 4. Данные, функции и модули в Python. Продолжение

# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input('Задайте натуральное число: N = '))

factors = []
d = 2
m = N 
while d * d <= N:
        if N % d == 0:
            factors.append(d)
            N //= d
        else:
            d += 1
factors.append(N) 

print('{} -> {}' .format(m, factors)) 