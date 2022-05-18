"""Только цифры

Напишите программу, которая принимает первым аргументом командной строки автомобильный номер, состоящий из цифр и заглавных букв латинского алфавита, а после очищает все буквы, оставляя только цифры. Количество букв слева и справа может быть произвольным.

В качестве букв могут приниматься только следующие латинские символы: E, T, O, P, A, H, K, C, B, M, Y, X.
Пример использования:
> python program.py A741BC
> 741
python program.py BC2345KM
> 2345
 """

import sys
number = sys.argv[1]
print(number.strip("ETOPAHKCBMYX"))

