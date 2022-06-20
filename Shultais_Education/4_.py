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

'''Средняя оценка

Во многих видах спорта на соревнованиях работает следующая схема выставления оценок. Сперва убирается одна максимальная и минимальная оценка, а уже после рассчитывается среднее значение из оставшихся. Это позволяет исключить заниженные и завышенные оценки.

Напишите программу, которая принимает произвольное количество оценок, затем исключает минимум и максимум, а после рассчитывает среднее из оставшихся. Программа должна вывести список оригинальных оценок, а также среднее с двумя знаками после десятичной точки.
Пример использования:
> python program.py 10 9 8 7 9 10 9 9 8 9
> [10, 9, 8, 7, 9, 10, 9, 9, 8, 9] 8.88'''


import sys

votes = sys.argv[1:]

#copy_votes = votes.copy()
# Преобразуем каждый элемент в целое число.
# Элемент функционального программирования, будем изучать в отдельном курсе.
votes = list(map(int, votes))
copy_votes = votes[:]
votes.sort()

srednee = sum(votes[1:-1])/len(votes[1:-1])
print("{} {:.2f}" .format(copy_votes, srednee))


'''Фамилия И. О.

Напишите программу, которая принимает фамилию, имя и отчество записанные в одну строку, а затем выводит данные в формате: Фамилия И. О.

Учитывайте следующие особенности получаемых данных: между словами может быть любое количество пробелов, а сами слова могут быть набраны в разных регистрах. При этом выводить их нужно в формате, описанном выше.
Пример использования
> python program.py "ИваноВ иван   Иванович"
> Иванов И. И.
 '''

import sys
fio = sys.argv[1]
#full_name.lower().title()
f, i, o = fio.split()
print(f.capitalize(), "{}. {}." .format(i[0].upper(), o[0].upper()))

'''Фамилия И. О.

Напишите программу, которая принимает фамилию, имя и отчество записанные в одну строку, а затем выводит данные в формате: Фамилия И. О.

Учитывайте следующие особенности получаемых данных: между словами может быть любое количество пробелов, а сами слова могут быть набраны в разных регистрах. При этом выводить их нужно в формате, описанном выше.
Пример использования
> python program.py "ИваноВ иван   Иванович"
> Иванов И. И.
 '''
import sys
fio = sys.argv[1]
#full_name.lower().title()
f, i, o = fio.split()
print(f.capitalize(), "{}. {}." .format(i[0].upper(), o[0].upper()))


'''Самое длинное слово

Напишите программу, которая первым аргументом командной строки принимает строку со списком слов, разделенных пробелом, а после выводит самое длинное из этих слов.
Пример использования:
> python program.py "кошки собаки пингвины зебры"
> пингвины
 '''
import sys
#принимаем и сразу разбиваем на отдельные слова в списке
words = sys.argv[1].split()
#words.sort(key = len())
sorted_words = sorted(words, key = len)
print(sorted_words[-1])


'''Новые товары

Ниже в редакторе кода содержится список товаров — products. Напишите программу, которая принимает из первого аргумента командной строки один параметр — строку продуктов разделенных запятой с пробелом. Эти продукты нужно добавить в исходный список, а затем отсортировать его и напечатать.
Пример использования:
> python program.py "апельсины, ватрушки"
> ['ананас', 'апельсины', 'ватрушки', 'макароны', 'помидоры', 'яблоки']
'''
import sys
spisok = sys.argv[1].split(", ")
products = ["ананас", "макароны", "помидоры", "яблоки"]
products.extend(spisok)
products.sort()
print(products)

'''Разбираем логи

Напишите программу, которая первым аргументом командной строки принимает лог веб-сервера, а затем выводит HTTP-метод и адрес страницы.

Строка лога передается в следующем виде:
212.158.128.234 [10/Feb/2016:00:20:13] GET /cars/toyota HTTP/2 200, где:

    212.158.128.234 — IP адрес пользователя;
    [10/Feb/2016:00:20:13] — дата и время обращения к ресурсу;
    GET — HTTP-метод обращения, может принимать значения GET, POST, HEAD и тд.
    /cars/toyota — адрес страницы, может быть любым;
    HTTP/2 — HTTP-протокол;
    200 — код ответа.

Пример использования:
> python program.py "212.158.128.234 [10/Feb/2016:00:20:13] GET /cars/toyota HTTP/2 200"
> GET /cars/toyota
 '''

import sys
log = sys.argv[1].split()
print(log[2], log[3])

'''ерсия HTTP-протокола

Напишите программу, которая первым аргументом командной строки принимает лог веб-сервера, а затем выводит версию HTTP-запроса. Формат логов такой же как в прошлом уроке.

Версия HTTP-протокола указывается в строке HTTP-протокола после слеша: HTTP/2 — версия 2.
Пример использования:
> python program.py "22.15.18.24 [10/Feb/2016:00:20:13] GET /cars/toyota HTTP/2 200"
> 2
 '''














