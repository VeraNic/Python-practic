# Знакомство с языком Python (семинары). Урок 5. Ускоренная обработка данных: lambda, filter, map, zip, enumerate, list comprehension
# 1. Напишите программу, удаляющую из текста все слова содержащие "абв".

text = 'Вот вам стол, а вот скамейка. \nВзяли в руки карандаш! \nНаша абвгдейка на экран приходит наш: \nабвгдейка, абвгдейка — это учёба и игра, \nабвгдейка, абвгдейка, азбуку детям знать пора.'

def delete_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

new_text = delete_words(text)
print ('\n\nТекст:')
print (text)
print ('\nНовый текст:')
print(new_text)