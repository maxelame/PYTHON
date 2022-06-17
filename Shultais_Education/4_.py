'''Реанимируем программу

Программа ниже, принимает из аргументов командной строки четыре параметра — квартальные доходы. Далее она рассчитывает среднее значение и выводит результат в консоль. Причем выводиться должна только целая часть итогового числа.

Однако программист, который писал код, допустил несколько ошибок. Исправьте их, чтобы программа работала правильно.
Пример использования:
> python program.py 100 200 300 400
> Средний доход: 250 руб.
 '''

import sys

q1 = int(sys.argv[1])
q2 = int(sys.argv[2])
q3 = int(sys.argv[3])
q4 = int(sys.argv[4])

# Помещаем значения в список.
year = [q1, q2, q3, q4]

# Вычисляем среднее.
avg = int(sum(year) / len(year))

# Выводим результат.
print("Средний доход: {} руб.".format(avg))


'''Сортируем продукты

Напишите программу, которая принимает из аргументов командной строки список товаров, а затем сортирует их и выводит результат.
Пример использования:
> python program.py яблоки ананас бананы
> ['ананас', 'бананы', 'яблоки']'''

import sys
spisok = sys.argv[1:]
sorted_spisok = sorted(spisok, key = str.upper)
print(sorted_spisok)
#spisok.sort(key = str.upper)
#print(spisok)
