#Знакомство с языком Python (семинары). Урок 2. Знакомство с Python. Продолжение

#2. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
#Пример: n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input('n = '))
sum = 0
for i in range(1, n + 1):
    print(i, ')', (1 + 1/i)**i)
    sum = sum + ((1 + 1/i)**i)
print('\nСумма: ', sum, '\n')