#Знакомство с языком Python (семинары). Урок 2. Знакомство с Python. Продолжение
#3. Реализуйте алгоритм перемешивания списка.

import random
list = [1, 2, 3, 4, 5]
result = random.sample(list, len(list))
print ('\n', str(list), ' --> ', str(result), '\n')