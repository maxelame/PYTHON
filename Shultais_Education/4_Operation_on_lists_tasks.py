'''Значения по умолчанию

Напишите программу, которая создает и заполняет список значениями по умолчанию. Первым аргументом программа должна принимать строку, которая будет помещена в список, а вторым число повторений этой строки. В конце программа должна вывести полученный список.

Пример использования:
> python program.py blank 5
> ['blank', 'blank', 'blank', 'blank', 'blank']'''

import sys
mention, repeat = sys.argv[1], int(sys.argv[2])
j = [mention] * repeat
print(j)


import sys
mention, repeat = sys.argv[1], int(sys.argv[2])
result = [mention] * repeat
print(result)


'''Расширяем города

Аргументы командной строки, которые передаются в программу, хранятся в списке sys.argv.
Это обычный Python-список, который поддерживает срезы, а также все стандартные методы и операции доступные спискам. Вы можете манипулировать им как угодно.

Нулевым элементом списка sys.argv передается имя запускаемой программы.
А далее следуют непосредственно аргументы командной строки, передаваемые в программу.
Если дополнительных аргументов 4, то список будет состоять из 5 элементов.

Следующая программа выводит длину sys.argv, а также его содержимое:
import sys
print(len(sys.argv))
print(sys.argv)

Изучите пример её работы:
> python fruits.py Банан Яблоко Апельсин Манго
> 5
> ['fruits.py', 'Банан', 'Яблоко', 'Яблоко', 'Манго']
Задание

В программе ниже создан список содержащий города. Программа принимает из аргументов командной строки дополнительные города. Расширьте список cities новыми городами и выведите его.
Пример использования:
> python program.py Нью-Йорк Москва
> ['Прага', 'Вена', 'Санкт-Петербург', 'Нью-Йорк', 'Москва']'''

import sys
new = sys.argv
del sys.argv[0]
cities = ["Прага", "Вена", "Санкт-Петербург"]
cities = cities + sys.argv
print(cities)


import sys
new = sys.argv
del sys.argv[0]
cities = ["Прага", "Вена", "Санкт-Петербург"]
cities +=sys.argv
print(cities)
