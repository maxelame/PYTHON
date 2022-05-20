'''Скорость движения

Напишите программу, которая принимает из аргументов командной строки два параметра: расстояние и время, за которое было пройдено данное расстояние. Программа должна рассчитать и вывести скорость движения в км/ч с двумя знаками после десятичной точки.

Передаваемые параметры могут быть как целыми, так и вещественными числами. Расстояние передается в километрах, а время в часах.

При форматировании вещественных чисел используется следующий спецификатор: %.Nf, где N — это число знаков после десятичной точки.
Пример использования:
> python program.py 60.2 1.5
> 40.13
'''
import sys
s = float(sys.argv[1])
t = float(sys.argv[2])
vv = s/t
v = "%.2f" % vv
print(v)

'''Знакомство
Отформатируйте строку hello так, чтобы она получила осмысленный вид. Выводить строку с помощью print не надо.
'''

age = 18
street = 'Ленина'
first_name = 'Олег'
house = 58
city_r = 'Москве'

hello = 'Привет! Меня зовут %s, мне %d лет. Я живу в %s, на улице %s, дом %d.' % (first_name, age,city_r,street,house)

'''Погода

По умолчанию положительные числа выводятся без знака «плюс»:
print(10)
10  # Положительное число. Выводится без знака +
print(-10)
-10  # Отрицательное число. Выводится со знаком -

Однако иногда требуется явно указать знак для числа, например при выводе температуры.
Для этого используется спецификатор %+d

Если в спецификатор передается отрицательное число, то оно будет выведено со знаком «минус», а если положительное, то со знаком «плюс»:

print("%+d, %+d" % (10, -10))
+10, -10

Напишите программу, которая принимает из аргументов командной строки три параметра: температуру на начало периода, температуру на конец периода и скорость ветра. Все параметры передаются в виде вещественных чисел.

Программа должна вывести строку в следующем виде: «A°…B°, C м/с», где A - это температура на начало периода, B — температура на конец периода и C — скорость ветра. Для вывода температуры используйте только целую часть числа, а при выводе скорости ветра оставьте только один знак после десятичной точки.

Обратите внимание на символ градуса °, а также на троеточие … в предлагаемом шаблоне. Это специальные символы, копируйте их прямо из текста задачи.
Пример использования:
> python program.py -5.2 7.6 2.45
> -5°…+7°, 2.5 м/с'''

import sys
A = float(sys.argv[1])
B = float(sys.argv[2])
C = float(sys.argv[3])
print("%+d°…%+d°, %.1f м/с" % (A,B,C))

'''Выравнивание по правому краю, часть 3

Часто на практике нужно выровнять число по правому краю, заполнив пространство слева пробелами или нулями. Для этого можно преобразовать число к строке и воспользоваться методом rjust, а можно использовать спецификатор вида «%Nd» или «%0Nd», где N — это длина конечной строки.

При использовании спецификатора «%Nd» строка будет заполнена слева пробелами.
При использовании спецификатора «%0Nd» строка будет заполнена слева нулями.

Заполняем пробелами и нулями строку длиной в 10 символов и числом 1200, выровненным по правому краю:

# Используем метод rjust.
price = 1200
print(str(price).rjust(10, " "))
      1200
print(str(price).rjust(10, "0"))
0000001200

# Используем форматирование.
print("%10d" % price)
      1200
print("%010d" % price)
0000001200

Напишите программу, которая принимает из аргументов командной строки один параметр: итоговую сумму, представленную целым числом. Программа должна вывести фразу «Итого: A руб.», где A — это целое число, выровненное по правому краю с пробелами слева. Общая длина A должна быть 7 знаков. Обратите внимание, что между Итого: и А руб. стоит пробел, который не входит в состав 7 знаков, выделенных под A.
Пример использования:
> python program.py 1200
> Итого:    1200 руб.'''

import sys
itogo = int(sys.argv[1])
print("Итого: %7d руб." % itogo)







