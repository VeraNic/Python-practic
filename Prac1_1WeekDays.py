# Знакомство с языком Python (семинары). Урок 1. Знакомство с Python
# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

weekDay = ['1', '2', '3', '4', '5', '6', '7']

day = int (input('Введите цифру, обозначающую день недели: '))

if day == weekDay[0] or  day == weekDay[1] or day == weekDay[2] or day == weekDay[3] or day == weekDay[4]:
    print('нет')
elif day == weekDay[5] or day == weekDay[6]:
    print('да')
else:
    print('Неверно введена цифра, обозначающая день недели.')

##########################################

# 2. Напишите программу для проверки истинности утверждения 
#    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

for X in 0, 1:
    for Y in 0, 1:
       for Z in 0, 1:
           print
