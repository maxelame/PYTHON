# В программе ниже определена строка distance_str, которая содержит текст "Расстояние: N км".
# Также программа получает из первого аргумента командной строки значение расстояния и сохраняет его в переменной distance.
#
# Начинающий разработчик решил заменить символ N в строке distance_str на значение из переменной distance, но у него ничего не получилось и программа вывела ошибку TypeError.
#
# Исправьте код так, чтобы строка distance_str вместо символа N содержала реальное расстояние из переменной distance. Изменения вносите только в 9 строку программы.





import sys

# Не меняйте строки ниже.
distance = sys.argv[1]
distance_str = "Расстояние: N км"

# Исправьте код так, чтобы символ N в строке distance_str  был заменен на значение
# из переменной distance.
distance_str = distance_str[:12] + distance+" "+ distance_str[-2:]

# Вывод distance_str.
print(distance_str)


# Меняем оператора
#
# В программе ниже определена строка phone, которая содержит номер телефона.
# Также программа получает из первого аргумента командной строки новый код оператора из трех символов и сохраняет его в переменной code.
#
# Молодой программист решил заменить несколько символов в строке phone на значение из переменной code, но у него снова ничего не получилось и программа вывела ошибку TypeError.
#
# Исправьте код так, чтобы строка phone вместо старого кода оператора получила новый из переменной code. Изменения вносите только в 9 строку программы.

import sys

# Не меняйте строки ниже.
code = sys.argv[1]
phone = "+7 (951) 783-13-14"

# Исправьте код так, чтобы код 951 в строке phone был заменен на значение
# из переменной code.
phone = phone[:4]+code+phone[7:]

# Вывод нового номера.
print(phone)


# upper и lower
#
# В уроке «Изменение строк» мы познакомились с методом lower(), который приводит строку к нижнему регистру. У этого метода есть парный метод upper(), который преобразует все символы строки в прописные.
#
# Напишите программу, которая первым аргументом командной строки принимает слово, а затем выводит три его варианта разделенных запятыми с пробелом: оригинальное, в нижнем регистре и в верхнем регистре.
#
# Для разделения слов используйте функцию print вместе с параметром sep.

import sys
text = sys.argv[1]
print(text, text.lower(),text.upper(),sep=', ')














