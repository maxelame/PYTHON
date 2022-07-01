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




