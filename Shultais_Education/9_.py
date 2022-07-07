'''Нечетные числа

Заполните список numbers нечетными числами от 11 до 27 включительно. Используйте цикл while.
 '''

numbers = []
j = 11
while j <=27:
    if j % 2 == 1:
        numbers.append(j)
    j += 1
print(numbers)


'''Таблица умножения, часть 2

Напишите программу, которая получает из первого аргумента командной строки целое число, а после выводит результат произведения переданного значения на числа от 1 до 9.

Финальный результат должен быть записан в одну строку с разделением чисел пробелами.
Передаваемые числа могут быть как положительными, так и отрицательными, а также равняться нулю.
Пример использования:
> python program.py 4
4 8 12 16 20 24 28 32 36
 '''

import sys
number = int(sys.argv[1])    # получаем число из коммандной строки
#spisok = []
i = 1
while i <= 9:
    print(number * i, end=" ")
    i += 1
#str_from_spisok = " ".join(spisok)
#print(str_from_spisok)

'''Четные числа

Заполните список numbers четными числами от 30 до 18 включительно.
Числа должны идти в обратном порядке. Используйте цикл while.
 '''

numbers = []
i = 30
while i>=18:
    if i%2==0:
        numbers.append(i)
    i -=1
print(numbers)

'''Степени двойки

Заполните список numbers степенями числа 2 начиная с нулевой и заканчивая 10 включительно: 1, 2, 4, ..., 1024.
Используйте цикл while.'''


numbers = []
i = 0
while i<=10:
    numbers.append(2 ** i)
    i+=1
print(numbers)

'''Сумма элементов списка

Посчитайте и выведете на экран сумму элементов списка numbers. Используйте цикл while.
 '''

numbers = [1, 7, 8, 34, 56, 14, 9]
"""
i = 0
summa = 0
while i <= (len(numbers)-1):
    summa += numbers[i]
    i += 1
print(summa)
"""
summa = 0
while len(numbers):
    summa += numbers.pop()
print(summa)

'''Факториал

Факториал числа N — это произведение всех целых чисел от 1 до N. Например, факториал 5 равен 120 и вычисляется так:
Вычисление факториала 5

Напишите программу, которая принимает первым аргументом командной строки число n, а затем вычисляет факториал этого числа и печатает результат. Используйте цикл while.
Пример использования:'''


import sys
number = int(sys.argv[1])
i = 1
summa = 1
while i <= number:
    summa *= i
    i += 1
print(summa)

'''Авторизация

В редакторе ниже находится словарь users, который в качестве ключей хранит имена пользователей, в качестве значений их пароли.

Напишите программу, которая первым аргументом командной строки принимает имя пользователя, а вторым — его пароль. Далее программа должна проверить переданные логин и пароль и вывести "Доступ открыт" если пароль верный и "Доступ закрыт" если пароль ошибочный.

Если пользователя, который передается в программу, в словаре нет, то нужно вывести "Пользователь не найден".
Пример использования:
> python program.py user2 abcde
> Доступ открыт'''


"""
import sys
user, password = sys.argv[1], sys.argv[2]
users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}
if user not in users:
    print ("Пользователь не найден")
elif user in users:
    if users.get(user) == password:
        print ("Доступ открыт")
    else:
        print ("Доступ закрыт")
"""
import sys

users = {
    "user1": "password1",
    "user2": "abcde",
    "user3": "123456",
    "user4": "lovelove",
    "user5": "kdmUdmk84M",
}

# Получаем имя пользователя.
username = sys.argv[1]
password = sys.argv[2]

# Получаем пароль пользователя.
user_password = users.get(username)

if user_password is None:
    print("Пользователь не найден")
elif user_password == password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")


'''Проверка длины пароля, часть 2

В переменной password содержится пароль введенный пользователем.
Выведите фразу «Пароль слишком короткий» (без кавычек), если длина пароля меньше 6 символов.
Если длина от 6 до 8 символов, то выведите «Хорошо, но можно и лучше».
Если длина более 8 символов — «Пароль подходит».'''

import sys

password = sys.argv[1]

# Используем функцию len()
if len(password) < 6:
    print("Пароль слишком короткий")
# Используем метод __len__()
elif 6 <= password.__len__() <= 8:
    print("Хорошо, но можно и лучше")
else:
    print("Пароль подходит")

# Функция len() и метод __len__() равнозначны


"""
import sys
password = sys.argv[1]
len_password = len(password)
if len_password > 8 :
    print("Пароль подходит")
elif len_password > 5 :
    print("Хорошо, но можно и лучше")
else:
    print("Пароль слишком короткий")
"""


'''Алкогольная продукция

В переменной age содержится возраст пользователя, а в hour — текущее время в часах (например, 14). Напишите программу, которая проверяет может ли продавец продать покупателю алкогольную продукцию.

Алкогольную продукцию разрешено продавать с 7 часов утра до 22 часов вечера лицам достигшим 18 лет.

Если продавать можно, то программа должна вывести «Разрешено» иначе «Запрещено».
 '''
import sys
age = int(sys.argv[1])
hour = int(sys.argv[2])
if age > 17 and hour >=7 and hour <22:
    print("Разрешено")
else:
    print("Запрещено")



'''Нечетные числа

Заполните список numbers нечетными числами от 11 до 27 включительно. Используйте цикл while.'''

numbers = []
j = 11
while j <=27:
    if j % 2 == 1:
        numbers.append(j)
    j += 1
print(numbers)

'''Таблица умножения, часть 2

Напишите программу, которая получает из первого аргумента командной строки целое число, а после выводит результат произведения переданного значения на числа от 1 до 9.

Финальный результат должен быть записан в одну строку с разделением чисел пробелами.
Передаваемые числа могут быть как положительными, так и отрицательными, а также равняться нулю.
Пример использования:
> python program.py 4
4 8 12 16 20 24 28 32 36'''
import sys
number = int(sys.argv[1])    # получаем число из коммандной строки
#spisok = []
i = 1
while i <= 9:
    print(number * i, end=" ")
    i += 1
#str_from_spisok = " ".join(spisok)
#print(str_from_spisok)



'''Четные числа

Заполните список numbers четными числами от 30 до 18 включительно.
Числа должны идти в обратном порядке. Используйте цикл while.'''

numbers = []
i = 30
while i>=18:
    if i%2==0:
        numbers.append(i)
    i -=1
print(numbers)



'''Посчитайте и выведете на экран сумму элементов списка numbers. Используйте цикл while.'''

numbers = [1, 7, 8, 34, 56, 14, 9]
"""
i = 0
summa = 0
while i <= (len(numbers)-1):
    summa += numbers[i]
    i += 1
print(summa)
"""
summa = 0
while len(numbers):
    summa += numbers.pop()
print(summa)


'''Факториал

Факториал числа N — это произведение всех целых чисел от 1 до N. Например, факториал 5 равен 120 и вычисляется так:
Вычисление факториала 5

Напишите программу, которая принимает первым аргументом командной строки число n, а затем вычисляет факториал этого числа и печатает результат. Используйте цикл while.
Пример использования:
> python program.py 5
120
 '''

import sys
number = int(sys.argv[1])
i = 1
summa = 1
while i <= number:
    summa *= i
    i += 1
print(summa)



'''Номера в отеле

Номера в отелях обычно имеют структуру вида FN, где F-это номер этажа, а N-номер комнаты. Например, комната 712 — находится на 7 этаже и идет двенадцатой по счету.

Напишите программу, которая первым аргументом командной строки получает количество номеров на этаже, а вторым — количество этажей, а затем выводит все возможные номера в отеле (см. пример работы программы).
Пример работы программы:
> python program.py 3 4
11 12 13 21 22 23 31 32 33 41 42 43'''

import sys
n, f = sys.argv[1], sys.argv[2]
floor = 1

li = []
while floor <= int(f):
    room = 1
    while room <= int(n):
        li.append(str(floor)+str(room))
        room +=1
    floor +=1
print(" ".join(li))

'''Печать в линию

Напишите программу, которая принимает из аргументов командной строки два значения: итоговое число и количество чисел в строке, а затем выводит все числа от 1 до итогового с разбивкой по строкам (см. пример):
Пример работы программы:
> python program.py 8 4
1 2 3 4
5 6 7 8
 '''

import sys
for n in range(1, int(sys.argv[1]) + 1):
    end = ' ' if n % int(sys.argv[2]) else '\n'
    print(n, end=end)


'''Напишите программу, которая принимает из аргументов командной строки произвольное количество чисел, а затем выводит то, у которого максимальная сумма цифр.
Пример работы программы (сумма цифр у 33 равна 6):
> python program.py 111 2 33 41
33'''

import sys
numbers = sys.argv[1:]
max_num = numbers[0]
for n in numbers:
    if sum(list(map(int, list(max_num)))) < sum(list(map(int, list(n)))):
        max_num = n
print(max_num)

'''Потребительская корзина

В редакторе ниже находится список товаров. Каждый товар — это словарь из имени и цены. Напишите программу, которая принимает из аргументов командной строки один параметр — количество денег, а затем выводит список товаров, которые можно купить за эти деньги.

Предполагается, что за доступные деньги мы покупаем товары в той последовательности, в которой они расположены в списке. Выводить нужно только имена товаров, разделенные запятой и пробелом.

Пропускать товары из списка нельзя. В примере ниже мы имеем 200 рублей и покупаем гречку, хлеб и молоко, при этом у нас остается еще 40 рублей и яйца мы уже купить не можем. Теоретическим мы еще могли бы купить сахар и картофель, но пропускать товары нельзя, поэтому в финальный список они не попадают.
Пример использования:
> python program.py 200
> Гречка, Хлеб, Молоко
 '''

import sys

money = int(sys.argv[1])
products = [
    {"name": "Гречка", "price": 69},
    {"name": "Хлеб", "price": 34},
    {"name": "Молоко", "price": 57},
    {"name": "Яйца", "price": 78},
    {"name": "Рис", "price": 88},
    {"name": "Макароны", "price": 49},
    {"name": "Сахар", "price": 22},
    {"name": "Яблоки", "price": 79},
    {"name": "Картофель", "price": 18},
    {"name": "Свинина", "price": 120},
    {"name": "Масло", "price": 66},
    {"name": "Помидоры", "price": 64}
]
busket = []
for i in products:
    if money >= int(i["price"]):
        money -= int(i["price"])
        busket.append(i["name"])
    else:
        break

print(", ".join(busket))


'''Годы с превышающим населением

В редакторе ниже находится список population, который хранит население России с 2003 по 2020 год включительно. Данные упорядочены по годам.

Напишите программу, которая первым аргументом командной строки принимает год, а затем выводит те годы, в которых население было больше или равно населению переданного года.

Годы нужно вывести через запятую в возрастающем порядке. Переданный год также нужно выводить.
Пример использования:
> python program.py 2020
> 2017, 2018, 2019, 2020
 '''

import sys
year = int(sys.argv[1])
population = [
    144_963_650,  # 2003
    144_168_205,
    143_474_219,
    142_753_551,
    142_220_968,
    142_008_838,
    141_903_979,
    142_856_536,
    142_865_433,
    143_056_383,
    143_347_059,
    143_666_931,
    146_267_288,
    146_544_710,
    146_804_372,
    146_880_432,
    146_780_720,
    146_748_590  # 2020
]
s = []
k = 0
for i in population:
    if i >= population[year-2003]:
        s.append(str(k + 2003))
    k +=1
print(", ".join(s))

'''Сумма элементов списка, 2

Посчитайте и выведете на экран сумму элементов списка numbers. Используйте цикл for.'''

numbers = [41, 5, 83, 4, 16, 14, 59]
summ = 0
for item in numbers:
    summ += item
print(summ)
"""
i = 0
for a in numbers:
    i += a
    print(a, i)
"""


'''Выручка нарастающим итогом

Напишите программу, которая принимает из аргументов командной строки ежедневную выручку, а затем выводит эти данные нарастающим итогом.

Нарастающий итог часто используется в финансах и рассчитывается сложением значения текущего периода с суммой значений прошлых периодов.
Пример использования:
> python program.py 1 2 3 4 5
> 1 3 6 10 15'''

"""
import sys
daily_revenue = sys.argv[1:]

summ = 0
#spisok = []
for item in daily_revenue:
    i = int(item)
    summ += i
    print(summ, end=" ")
#spisok.append(str(summ))
#print(summ, end=" ")
"""
import sys
daily_revenue = sys.argv[1:]
summ = 0
spisok = []
for item in daily_revenue:
    i = int(item)
    summ += i
    spisok.append(str(summ))
print(" ".join(spisok))


'''Сравнение с лучшим месяцем

Напишите программу, которая принимает из аргументов командной строки ежемесячные показатели регистраций пользователей, а затем сравнивает показатели каждого месяца с лучшим и выводит разницу.
Пример использования:
> python program.py 127 624 235 235 77 288
> -497 0 -389 -389 -547 -336
 '''

import sys
indicators = sys.argv[1:]
best_indicator = max(map(int, indicators))
s = []
for i in map(int, indicators):
    s.append(str(i-best_indicator))
print(" ".join(s))

'''Заполняем пропуски

Иногда данные в программу попадают с пропусками и одна из стратегий нормализации данных — это заполнение пропусков предыдущими значениями.

Напишите программу, которая принимает из аргументов командной строки набор данных, среди которых встречаются пропуски обозначенные словом null. Нужно заменить эти пропуски предшествующими значениями.

Если перед null значений не было, то изменять null не нужно.
Выведите итоговую последовательность в командную строку (терминал).
Пример использования:
> python program.py null null 2017 null 2019 null
> null null 2017 2017 2019 2019
 '''
import sys

values = sys.argv[1:]
s = [values[0]]
x = values[0]
for value in values[1:]:
    if value == "null":
        value = x
    x = value
    s.append(value)
print(" ".join(s))

"""import sys
data = sys.argv[1:]
result = [data[0]] # Создаём список с результатом и сразу помещаем в него первый элемент искомого списка (т.к. он в любом случае останется неизменным, будь то значение или "null") 
pred = data[0] # Создаём переменную с предыдущим значением
for i in data[1:]:
    if i == "null":
        i = pred
    pred = i
    result.append(i)
print(" ".join(result))
"""


'''Доходы и расходы

Напишите программу, которая принимает из аргументов командной строки значения платежей компании. Положительные значения отвечают за доходы, а отрицательные за расходы.

Посчитайте общую сумму доходов и расходов, а затем выведите результат как в примере ниже.
Пример использования:
> python program.py 100 -23 301 401 -194
> Доходы: 802 руб.
> Расходы: 217 руб.'''

import sys
a = map(int, sys.argv[1:])
doh = []
rash = []
for i in a:
    if i >= 0:
        doh.append(i)
    else:
        rash.append(i)
print("Доходы: {} руб.".format(sum(doh)))
print("Расходы: {} руб.".format(sum(rash)*(-1)))

'''Суммирование до нуля

Напишите программу, которая первым аргументом командной строки получает строку, содержащую набор целых чисел разделенных пробелом, а затем считает сумму этих чисел до тех пор, пока не встретит ноль.

Учитывайте, что могут быть варианты, когда среди получаемых чисел нуля нет, тогда нужно получить сумму всех передаваемых чисел.
Пример использования (считаем сумму 2 -3 -5 7 11):
> python program.py "2 -3 -5 7 11 0 13 17 19"
> 12'''

"""
import sys
a = sys.argv[1]
b = a.split(' ')
i = s = 0
while i < len(b):
    if int(b[i]) == 0:
       break
    s += int(b[i])
    i += 1

print(s)
"""

import sys

numbers = sys.argv[1]
# преобразуем строку в список с помощью split
numbers = numbers.split(" ")

i = 0
summa = 0
while i < len(numbers):
    if int(numbers[i]) == 0:
        break
    summa += int(numbers[i])
    i += 1

print(summa)





