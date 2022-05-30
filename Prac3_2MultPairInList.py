#Знакомство с языком Python (семинары). Урок 3. Данные, функции и модули в Python

#2. Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:[2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

list1 = [2, 3, 4, 5, 6]
#list2 = [2, 3, 5, 6] # Для проверки примера № 2 )

def multPairs(list0: list):
    result = []
    if len(list0) % 2 != 0:
        n = len(list0) + 1
    else:
        n = len(list0)

    for i in range(n // 2):
        mult = list0[i] * list0[len(list0)- 1 - i]
        result.append(mult)
    print('\n', list1, '=>', result, '\n')
    
multPairs(list1)
#multPairs(list2)  # Вывод результата примера № 2