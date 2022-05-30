#Знакомство с языком Python (семинары). Урок 3. Данные, функции и модули в Python

#1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
sum_not_odd_position = 0
numbers_in_not_odd_position = ''
for item in range(1, len(list), 2):
    sum_not_odd_position = sum_not_odd_position + list[item]
    numbers_in_not_odd_position = numbers_in_not_odd_position + str(list[item]) + ", "
print('\n', (list), '-> на нечётных позициях элементы ', numbers_in_not_odd_position, 'ответ: ', sum_not_odd_position, '\n')