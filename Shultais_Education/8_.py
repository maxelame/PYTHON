'''Проверка пароля

В редакторе ниже находится переменная password с правильным паролем пользователя. Напишите программу, которая первым аргументом командной строки принимает пароль, а затем, проверяет, верный ли он.

Если переданный пароль верный, то программа должна вывести "Доступ открыт", а если пароль неверный, то "Доступ закрыт".
Пример использования:
> python program.py admin
> Доступ закрыт
 '''

import sys
new_password  = sys.argv[1]
password = "idY*49amd6z"

if new_password == password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")

'''Проверка реального пароля

В реальных программах пароли хранят в зашифрованном виде, чтобы в случае утечки их было сложно взломать. Когда пользователь пытается авторизоваться на сайте, то его пароль сперва зашифровывается, а затем этот шифр сравнивается с зашифрованным паролем в программе или в базе данных.

Простейшая схема шифрования с помощью алгоритма md5* выглядит так:

# Импортируем в программу библиотеку для шифрования.
import hashlib 

# Задаем "сырой" (незашифрованный) пароль.
raw_password = 'password'

# Кодируем "сырой" пароль.
# Нужно для того, чтобы воспользоваться md5.
raw_password = raw_password.encode()

# Получаем шифр-объект.
hash_password = hashlib.md5(raw_password)

# Получаем зашифрованный пароль.
hash_password = hash_password.hexdigest()

# Выводим зашифрованный пароль.
print(hash_password)
5f4dcc3b5aa765d61d8327deb882cf99

# Именно строка вида "5f4dcc3b5aa765d61d8327deb882cf99" 
# обычно хранится в программе или базе данных.

В редакторе ниже в переменной hash_password хранится зашифрованный пароль. Напишите программу, которая первым аргументом командной строки принимает "сырой" пароль пользователя, а затем, проверяет, верный ли он.

Если переданный пароль верный, то программа должна вывести "Доступ открыт", а если пароль неверный, то "Доступ закрыт".
Пример использования:
> python program.py admin
> Доступ закрыт

Примечание. В настоящий момент алгоритм md5 является небезопасным. Не используйте его в реальных программах.'''

import sys
password = sys.argv[1]
import hashlib
# Задаем "сырой" (незашифрованный) пароль.
raw_password = password
# Кодируем "сырой" пароль.
# Нужно для того, чтобы воспользоваться md5.
raw_password = raw_password.encode()
# Получаем шифр-объект.
new_hash_password = hashlib.md5(raw_password)

# Получаем зашифрованный пароль.
new_hash_password = new_hash_password.hexdigest()

hash_password = 'c8b667f4e6953d59b6ae9b9659772333'

if new_hash_password == hash_password:
    print("Доступ открыт")
else:
    print("Доступ закрыт")


'''Четность числа

Напишите программу, которая первым аргументом командной строки принимает целое число, а затем выводит слово "четное" если число четное и "нечетное" в противном случае.
Пример использования:
> python program.py 17
> нечетное'''

import sys
number = int(sys.argv[1])
if number % 2:
    print("нечетное")
else:
    print("четное")

'''Сравнение целых чисел

Напишите программу, которая принимает из аргументов командной строки два произвольных целых числа, а затем выводит то, которое больше по значению. Если числа равны, то можно выводить любое.
Пример использования:
> python program.py 17 33
> 33'''

import sys
numbers = list(map(int, sys.argv[1:]))
#numbers.sort(key = int)
#print(numbers[-1])
if numbers[0] > numbers[-1]:
    print(numbers[0])
else:
    print(numbers[-1])
#if numbers[0] < numbers[-1]:
#    print(numbers[-1])
#if numbers[0] == numbers[-1]:
#    print(numbers[0])



