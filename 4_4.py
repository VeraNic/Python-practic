#Знакомство с языком Python (семинары). Урок 4. Данные, функции и модули в Python. Продолжение

# 4. Задана натуральная степень n.
# Сформиoровать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени 
# пример записи в файл при n=3 ==> 33x^3 + 8x^2 + 64x + 85 = 0 
# при n=2 ==> 27x^2 + 95x + 79 = 0

import random
k = [random.randint(1, 100) for i in range(random.randint(2, 10))]
print('Натуральная степень: n =', len(k)-1) 

m = ''
for i in range(0, len(k)):
    m = m + str(k[i]) 
    if i < len(k) - 1:
        m += 'х'
    if i < len(k)- 2:
        m += '^'+ str(len(k) - i - 1)
    if i < len(k) - 1:
        m += ' + '
m += ' = 0'
print(m)
    