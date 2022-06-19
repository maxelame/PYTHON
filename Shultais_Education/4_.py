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


'''Сортировка по алфавиту

В редакторе ниже находится список товаров. Напишите программу, которая принимает из аргументов командной строки еще один список с продуктами, а затем дополняет им исходный и сортирует результат по алфавиту. Обратите внимание, что названия продуктов могут быть записаны в разном регистре.
Пример использования:
> python program.py яблоки Бананы
> ['апельсины', 'Бананы', 'Хлеб', 'яблоки']
 '''

import sys
new_products = sys.argv[1:]
products = ["апельсины", "Хлеб"]
products += new_products
#products.extend(new_products)
#sorted_products = sorted(products, key = str.upper)
#print(sorted_products)
products.sort(key = str.upper)
print(products)

'''Минимум и максимум

Напишите программу, которая принимает из аргументов командной строки список чисел, а затем выводит минимальное и максимальное из них. Учитывайте, что все данные из аргументов командной строки в программу поступают в виде строк, а нам нужно получить минимум и максимум с позиции чисел.
Пример использования:
> python program.py 120 56 3 17 100 9
> 3 120'''
import sys
spisok = sys.argv[1:]
#min_digit = min(map(int, spisok))
#max_digit = max(map(int, spisok))
#print(min_digit, max_digit)
#spisok.sort(key = int)
#print(spisok[0], spisok[-1])
sorted_spisok = sorted(spisok, key = int)
print(sorted_spisok[0], sorted_spisok[-1])


'''Спасаем сортировку

Программа ниже принимает из аргументов командной строки список автомобильных марок, а затем сортирует его в обратном порядке и выводит результат. Проблема в том, что код не работает. Исправьте все ошибки.
Пример использования:
> python program.py Toyota Honda BMW Kia
> ['Toyota', 'Kia', 'Honda', 'BMW']'''

import sys

# Получаем список автомобилей.
cars = sys.argv[1:]

# Сортируем в обратном порядке.
#sorted_cars = sorted(cars, key=str.upper, reverse=True )
sorted_cars = sorted(cars, reverse=True, key=str.upper )
# Выводим результат.
print(sorted_cars)

'''Сортировка чисел

Напишите программу, которая принимает из аргументов командной строки список чисел, а затем выводит их в порядке убывания. Учитывайте, что все данные из аргументов командной строки в программу поступают в виде строк, а нам нужно получить сортировку с позиции чисел.
Пример использования:
> python program.py 120 56 3 17 100 9
> ['120', '100' ,'56', '17', '9', '3']'''

import sys
spisok = sys.argv[1:]
#sorted_spisok = sorted(spisok, key = int, reverse = True)
#print(sorted_spisok)
spisok.sort(key = int, reverse = True)
print(spisok)

'''Цвета радуги, 2

Создайте список reverse_colors, в котором цвета радуги идут в обратном порядке.
Список colors изменять или удалять нельзя.
 '''
colors = ["красный", "оранжевый", "желтый", "зеленый", "голубой", "синий", "фиолетовый"]
#reverse_colors = list(reversed(colors))
reverse_colors = colors[::-1]

'''Первые с конца

Напишите программу, которая принимает из аргументов командной строки список фамилий, а затем выводит тройку лидеров с конца.
Пример использования:
> python program.py Шмидт Иванов Герасимов Базуев Васильев
> ['Васильев', 'Базуев', 'Герасимов']'''

import sys
spisok = sys.argv[1:]
#reversed_spisok = list(reversed(spisok))
#print(reversed_spisok[0:3])
#reversed_spisok = spisok[::-1]
#reversed_spisok = spisok.copy()
#reversed_spisok.reverse()
spisok.reverse()
print(spisok[:3])
#print(reversed_spisok[0:3])




