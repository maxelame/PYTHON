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

'''Поиск пользователя

В редакторе ниже содержится список пользователей. Каждый пользователь представлен словарем из трёх ключей: id, first_name и last_name. Напишите программу, которая получает id пользователя из первого аргумента командной строки, а затем выводит его имя и фамилию.

Программа гарантированно будет получать только те id, которые есть в списке.
Пример использования:
> python program.py 156
> Виктор Осипов'''

import sys
id_num = int(sys.argv[1])    # получаем id номер
users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев"},
    {"id": 21, "first_name": "София", "last_name": "Зинько"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков"}
]
i = 0
while users[i]["id"] != id_num:
    i +=1
print("{first_name} {last_name}" .format(**users[i]))


'''Первый подходящий программист

В редакторе ниже содержится список программистов. Каждый программист представлен словарем и одним из ключей является lang, который хранит информацию о языке, с которым работает разработчик.

Напишите программу, которая получает из первого аргумента командной строки название языка программирования, а затем выводит имя и фамилию первого программиста, который на нем пишет.

Программа гарантированно будет получать только те названия языков, которые есть в списке.
Пример использования:
> python program.py java
> Алёна Гордеева'''

import sys
lang = sys.argv[1]
users = [
    {"id": 17, "first_name": "Дмитрий", "last_name": "Иванов", "lang": "python"},
    {"id": 156, "first_name": "Виктор", "last_name": "Осипов", "lang": "php"},
    {"id": 23, "first_name": "Алёна", "last_name": "Гордеева", "lang": "java"},
    {"id": 84, "first_name": "Семён", "last_name": "Васильев", "lang": "python"},
    {"id": 21, "first_name": "София", "last_name": "Зинько", "lang": "java"},
    {"id": 55, "first_name": "Антон", "last_name": "Ватутин", "lang": "python"},
    {"id": 287, "first_name": "Виталий", "last_name": "Новиков", "lang": "c++"}
]
i = 0
while i < len(users):
    user = users[i]
    if user["lang"] == lang:
        print("{first_name} {last_name}" .format(**user))
        break
    i +=1


'''Первый активный программист

В редакторе ниже содержится список программистов. Каждый программист представлен словарем из трёх элементов: id, язык (lang) и активность (active).

Напишите программу, которая получает из первого аргумента командной строки название языка программирования, а затем выводит id первого активного программиста, который пишет на переданном языке.

Программа гарантированно будет получать только те названия языков, которые есть в списке.
Пример использования:
> python program.py python
> 84
 '''

import sys
lang = sys.argv[1]
users = [
    {"id": 17,  "lang": "python", "active": False},
    {"id": 156, "lang": "php",    "active": True},
    {"id": 23,  "lang": "java",   "active": True},
    {"id": 84,  "lang": "python", "active": True},
    {"id": 21,  "lang": "java",   "active": False},
    {"id": 55,  "lang": "python", "active": True},
    {"id": 88,  "lang": "python", "active": True},
    {"id": 287, "lang": "c++",    "active": False},
    {"id": 481, "lang": "php",    "active": False},
    {"id": 134, "lang": "c++",    "active": True}
]
i = 0
while i < len(users):
    user = users[i]
    if user["lang"] == lang and user["active"]:
        break
    i +=1
print("{id}".format(**user))


'''Код из SMS

Часто при входе на различные сайты или при совершении платежа, вам присылают на SMS код подтверждения, который нужно ввести. Как правило, телефон сам распознает код из сообщения и предлагает сразу вставить его без ручного набора:
Скриншот с телефона

Нам предстоит решить похожую задачу.
Напишите программу, которая из первого аргумента командной строки получает текст SMS сообщения, а после выводит код из этого сообщения.

Для простоты будем считать, что кроме кода никаких других цифр в сообщении нет.
Пример использования:
> python program.py 'Никому не говорите код: 3987! Вход в Тинкькофф.'
> 3987'''

import sys
sms = sys.argv[1]
pin =""
for i in sms:
    if i in "0123456789":
        pin +=i
print(pin)


'''Разделяем символы

Напишите программу, которая первым аргументом командной строки получает строку символов, набранных в разных регистрах, а затем разделяет их на символы в нижнем регистре и символы в верхнем регистре.

В конце программа должна вывести сперва все символы в нижнем регистре, а затем все символы в верхнем регистре. Порядок следования символов нужно сохранить.
Пример использования:
> python program.py aBcDeFGhiKL
> acehiBDFGKL'''

import sys
word = sys.argv[1]
syllables_H = ""
syllables_L = ""
for char in word:
    if char in "qwertyuiopasdfghjklzxcvbnm":
        syllables_L += char
    elif char in "QWERTYUIOPASDFGHJKLZXCVBNM":
        syllables_H += char
print(syllables_L+syllables_H)

'''азделяем числа

Напишите программу, которая принимает через аргументы командной строки произвольное количество целых чисел, а затем разделят их на отрицательные и положительные.

Программа должна сперва вывести отрицательные числа, а затем положительные.
Ноль нужно отнести к положительным.
Числа следует выводить через пробел.
Порядок следования чисел нужно сохранить (то есть сортировать числа не нужно).
Пример использования:
> python program.py 5 1 -3 6 -8 9
> -3 -8 5 1 6 9'''

import sys
numbers = map(int, sys.argv[1:])
s_positive = []
s_negative = []
for number in numbers:
    if number < 0:
        s_negative.append(str(number))
    else:
        s_positive.append(str(number))

print(" ".join(s_negative + s_positive))



'''ледим за трендами

В сервисе сквозной аналитики Roistat есть такой отчет:

Этот отчет показывает ежедневное количество событий, которые приняла система. В случае если в определенный день данных пришло больше, чем в предыдущий, то столбец раскрашивается зеленым цветом. Если данных пришло меньше, то столбец раскрашивается в красный. Если данных столько же, сколько и вчера, то столбец раскрашивается в тот же цвет, что и в предыдущий день.

Напишите программу, которая получает из аргументов командной строки произвольное количество аргументов, каждый из которых отвечает за количество событий, которые пришли за один день. Программа должна вывести цвета для раскраски столбцов для каждого полученного элемента.

Для положительных трендов нужно выводить green, а для отрицательных red. Выводимые цвета надо разделить пробелом. Считаем что первый день всегда положительный.
Пример использования:
> python trend.py 129 130 135 110 109 123
green green green red red green'''


import sys
trend = list(map(int, sys.argv[1:]))
start = int(sys.argv[1])
previous_color = "green"
s = ["green"]
for item in trend[1:]:
    if item - start > 0:
        s.append("green")
        previous_color = "green"
        start = item
    elif item - start < 0:
        s.append("red")
        previous_color = "red"
        start = item
    else:
        s.append(previous_color)
        start = item
print(" ".join(s))


'''Четные числа в обратном порядке

Измените параметры функции range так, чтобы в список numbers попали четные числа от 10 до 2 включительно.'''

numbers = list(range(10, 1, -2))


'''Факториал с помощью for

Перепишите решение задачи «Факториал» с использованием цикла for и функции range.
Пример использования:
> python program.py 5
120'''

"""import sys
n = list(range(1, int(sys.argv[1])+1))

factorial = 1
for i in n:
    factorial *=i
print(factorial)"""

import sys

n = int(sys.argv[1])

# Задаем начальное значение factorial.
factorial = 1
# Запускаем цикл.
for i in range(2, n + 1):
    factorial *= i

print(factorial)

'''Баланс торговой точки

Рядом с программой находится файл transactions.txt, который содержит список доходов и расходов торговой точки. Каждый платеж записан в отдельной строке и состоит из двух частей разделенных точкой с запятой: Объект;Сумма.

Пример такого файла:

Продажа муки;4900
Закуп муки;-1200
Продажа кефира;2900
Продажа молока;1500

Сумма платежа может быть как положительной, так и отрицательной.

Напишите программу, которая проходится по всем платежам в файле и выводит общий финансовый результат торговой точки. Для файла из примера ответ будет равен 8100.
Пример использования:
> python program.py
> 8100
 '''

temp = []
for line in open("transactions.txt", "r"):
    line1 = line.split(";")
    temp.append(line1[-1])
summ = 0
for element in temp:
    summ += int(element)
print(summ)
##################################


total = 0
# Проходимся по всем строка файла
for transaction in open("transactions.txt", "r"):
    # Разбиваем строку ну две переменные
    subject, amount = transaction.split(";")
    # Подсчитываем результат
    total += int(amount.strip())

print(total)

'''Баланс магазина

В прошлой задаче вы посчитали баланс торговой точки, теперь нужно сделать это для магазина. Просто скопировать программу не получится, так как у магазина другой формат хранения платежей.

Каждый платеж всё также хранится в отдельной строке, но состоит из трёх частей Объект;Направление платежа;Сумма. Где «Направление платежа» может быть income — доход или outcome — расход. При этом само значение суммы всегда положительное.

Пример такого файла:

Продажа муки;income;4900
Закуп муки;outcome;1200
Продажа кефира;income;2900
Продажа молока;income;1500

Если посмотреть на вторую строку файла, то мы увидим outcome;1200 — это значит, что произошел расход в размере 1200 рублей или другими словами, баланс уменьшился на 1200 рублей.

Напишите программу, которая проходится по всем платежам в файле и выводит общий финансовый результат магазина. Для файла из примера ответ будет равен 8100.
Пример использования:
> python program.py
> 8100'''

total = 0
# Проходимся по всем строка файла
for transaction in open("transactions.txt", "r"):
    # Разбиваем строку ну две переменные
    subject, sign,  amount = transaction.split(";")
    if sign == "income":
        total += int(amount.strip())
    else:
        total += (-1)*int(amount.strip())
    # Подсчитываем результат
print(total)


'''Вид треугольника

Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.

Формат входных данных
На вход программе подаются три числа – длины сторон существующего треугольника.

Формат выходных данных
Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).
Тестовые данные 🟢

Sample Input 1:

145
145
139'''
